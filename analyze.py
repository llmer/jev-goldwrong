"""Scorecard + flags from out/*.jsonl. Usage: python3 analyze.py [--p-gold 0.2] [--p-top 0.7]"""
import argparse, json, math
from collections import Counter, defaultdict
from pathlib import Path

OUT = Path(__file__).parent / "out"


def ece(records, bins=10):
    """Expected calibration error of top-choice confidence (max probability), equal-width bins."""
    total, err = len(records), 0.0
    buckets = defaultdict(list)
    for r in records:
        p = max(r["probabilities"].values())
        buckets[min(int(p * bins), bins - 1)].append((p, r["choice"] == r["gold"]))
    for items in buckets.values():
        conf = sum(p for p, _ in items) / len(items)
        acc = sum(c for _, c in items) / len(items)
        err += len(items) / total * abs(conf - acc)
    return err


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--p-gold", type=float, default=0.2, help="flag if P(gold) below this")
    ap.add_argument("--p-top", type=float, default=0.7, help="and P(Jev's choice) above this")
    a = ap.parse_args()
    summary, flags = [], []
    for path in sorted(p for p in OUT.glob("*.jsonl") if p.stem != "flags"):
        name = path.stem
        recs = [json.loads(l) for l in path.read_text().splitlines()]
        errs = [r for r in recs if "error" in r]
        recs = [r for r in recs if "error" not in r]
        if not recs:
            continue
        n = len(recs)
        agree = sum(r["choice"] == r["gold"] for r in recs)
        cost = sum(r["usage"].get("cost", 0) for r in recs)
        lat = sorted(r["latency_ms"] for r in recs)
        strong = [r for r in recs if r["p_gold"] is not None and r["p_gold"] < a.p_gold
                  and max(r["probabilities"].values()) > a.p_top]
        # selective accuracy: agreement among rows where confidence >= 0.9
        hi = [r for r in recs if r["confidence"] >= 0.9]
        summary.append(dict(dataset=name, rows=n, errors=len(errs), agreement=agree / n,
                            agreement_at_conf90=(sum(r["choice"] == r["gold"] for r in hi) / len(hi)) if hi else None,
                            coverage_at_conf90=len(hi) / n, ece=ece(recs),
                            flagged=len(strong), flag_rate=len(strong) / n,
                            cost_usd=cost, median_latency_ms=lat[len(lat) // 2],
                            p95_latency_ms=lat[int(len(lat) * 0.95)]))
        confusions = Counter((r["gold"], r["choice"]) for r in strong)
        summary[-1]["top_confusions"] = [f"{g} -> {c}: {k}" for (g, c), k in confusions.most_common(8)]
        for r in strong:
            top = sorted(r["probabilities"].items(), key=lambda kv: -kv[1])[:3]
            text = r["text"] if isinstance(r["text"], str) else json.dumps(r["text"], ensure_ascii=False)
            flags.append(dict(id=r["id"], dataset=name, text=text, gold=r["gold"], jev=r["choice"],
                              p_gold=r["p_gold"], p_jev=r["probabilities"][r["choice"]],
                              confidence=r["confidence"], top3=top))
    (OUT / "summary.json").write_text(json.dumps(summary, indent=1))
    flags.sort(key=lambda f: (f["p_gold"], -f["p_jev"]))
    with (OUT / "flags.jsonl").open("w") as f:
        for fl in flags:
            f.write(json.dumps(fl) + "\n")
    print(f"{'dataset':10} {'rows':>6} {'agree':>6} {'agr@.9':>7} {'cov@.9':>7} {'ECE':>5} {'flags':>6} {'rate':>6} "
          f"{'cost':>8} {'p50ms':>6} {'p95ms':>6}")
    for s in summary:
        print(f"{s['dataset']:10} {s['rows']:6d} {s['agreement']:6.3f} "
              f"{(s['agreement_at_conf90'] or 0):7.3f} {s['coverage_at_conf90']:7.3f} {s['ece']:5.3f} "
              f"{s['flagged']:6d} {s['flag_rate']:6.3f} {s['cost_usd']:8.4f} {s['median_latency_ms']:6d} "
              f"{s['p95_latency_ms']:6d}")
        for c in s["top_confusions"]:
            print(f"{'':10}   {c}")
    print(f"total flags {len(flags)} -> out/flags.jsonl")


if __name__ == "__main__":
    main()
