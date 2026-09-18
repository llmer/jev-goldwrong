"""v3 scorecard: fixed bands from Jev's own answers (no gold-tuned threshold), a ranked review queue, convention
signals, and where the v2 flags landed. Writes out_v3/summary.json and out_v3/queue.jsonl.

Bands for a row whose choice differs from gold (all cutoffs fixed at 0.5 up front; confidence tiers at the
Confidence page's 0.5 / 0.9 defaults):
  error_candidate      gold does not fit (fit_gold < .5), Jev's label does (fit_choice >= .5), not ambiguous (< .5)
  ambiguous_candidate  ambiguous >= .5, or both labels fit
  weak_disagree        everything else (neither fits, or only gold fits)
  none_candidate       Jev chose none and gold does not fit
  none_weak            Jev chose none but gold fits
Rows where Jev agrees with gold are 'agree'; 'agree_gold_unfit' counts the odd ones where the absolute noul still
says gold does not fit.
"""
import importlib, json, os
from collections import Counter, defaultdict
from pathlib import Path

VERSION = os.environ.get("VERSION", "v3")
_spec = importlib.import_module(f"datasets_{VERSION}")
CONVENTIONS, DATASETS, NONE_ID = _spec.CONVENTIONS, _spec.DATASETS, _spec.NONE_ID

HERE = Path(__file__).parent
OUT = HERE / f"out_{VERSION}"
PRIOR_REVIEWS = ["review"] + [f"review_v{i}" for i in range(3, int(VERSION[1:]))]
V2 = HERE / "out"
T = 0.5
TIERS = [("high", 0.9), ("mid", 0.5), ("low", 0.0)]


def tier(c):
    return next(name for name, lo in TIERS if c >= lo)


def band(r):
    g, c = r["gold"], r["choice"]
    fg, fc, amb = r["fit_gold"], r.get("fit_choice"), r["ambiguous"]
    if c == g:
        return "agree" if fg >= T else "agree_gold_unfit"
    if c == NONE_ID:
        return "none_candidate" if fg < T else "none_weak"
    if amb >= T or (fg >= T and fc >= T):
        return "ambiguous_candidate"
    if fg < T and fc >= T:
        return "error_candidate"
    return "weak_disagree"


def ece(recs, bins=10):
    total, err, buckets = len(recs), 0.0, defaultdict(list)
    for r in recs:
        p = max(r["probabilities"].values())
        buckets[min(int(p * bins), bins - 1)].append((p, r["choice"] == r["gold"]))
    for items in buckets.values():
        err += len(items) / total * abs(sum(p for p, _ in items) / len(items) - sum(c for _, c in items) / len(items))
    return err


def v2_reviewed_ids():
    """Every row any earlier experiment's reviewers saw (v2 under review/, v3 under review_v3/, ...)."""
    ids = set()
    for d in PRIOR_REVIEWS:
        for p in (HERE / d).glob("*.jsonl"):
            if ".verdicts" in p.name:
                continue
            ids |= {json.loads(l)["id"] for l in p.read_text().splitlines()}
    return ids


def main():
    seen = v2_reviewed_ids()
    v2flags = {}
    if (V2 / "flags.jsonl").exists():
        v2flags = {json.loads(l)["id"]: json.loads(l) for l in (V2 / "flags.jsonl").read_text().splitlines()}
    summary, queue = [], []
    for name, spec in DATASETS.items():
        path = OUT / f"{name}.jsonl"
        if not path.exists():
            continue
        recs = [json.loads(l) for l in path.read_text().splitlines()]
        errors = sum("error" in r for r in recs)
        recs = [r for r in recs if "error" not in r]
        bands, tiers = Counter(), Counter()
        conv = defaultdict(lambda: defaultdict(list))
        for r in recs:
            r["band"] = band(r)
            bands[r["band"]] += 1
            if r["band"] == "error_candidate":
                r["tier"] = tier(r["confidence"])
                tiers[r["tier"]] += 1
            for q, v in r["conventions"].items():
                conv[q][r["band"]].append(v)
        # where did the v2 flags on this dataset land?
        v2_here = [v2flags[i] for i in v2flags if v2flags[i]["dataset"] == name]
        by_id = {r["id"]: r for r in recs}
        v2_landing = Counter(by_id[f["id"]]["band"] for f in v2_here if f["id"] in by_id)
        cand = [r for r in recs if r["band"] == "error_candidate"]
        held_out = sum(r["id"] not in seen for r in cand)
        lat = sorted(r["latency_ms"] for r in recs)
        cost = sum(r["usage"].get("cost", 0) + r.get("usage2", {}).get("cost", 0) for r in recs)
        s = dict(dataset=name, rows=len(recs), errors=errors,
                 agreement=sum(r["choice"] == r["gold"] for r in recs) / len(recs), ece=ece(recs),
                 bands=dict(bands), error_tiers=dict(tiers),
                 error_rate=len(cand) / len(recs), error_held_out=held_out,
                 ambiguous_rate=bands["ambiguous_candidate"] / len(recs),
                 none_rate=(bands["none_candidate"] + bands["none_weak"]) / len(recs),
                 v2_flags=len(v2_here), v2_flag_landing=dict(v2_landing),
                 second_calls=sum("usage2" in r for r in recs),
                 conventions={q: {b: round(sum(v) / len(v), 3) for b, v in bb.items() if len(v) >= 5}
                              for q, bb in conv.items()},
                 models=sorted({r["model"] for r in recs}),
                 cost_usd=cost, median_latency_ms=lat[len(lat) // 2], p95_latency_ms=lat[int(len(lat) * .95)])
        summary.append(s)
        for r in recs:
            if r["band"] in ("agree", "agree_gold_unfit"):
                continue
            top = sorted(r["probabilities"].items(), key=lambda kv: -kv[1])[:3]
            queue.append(dict(id=r["id"], dataset=name, band=r["band"], tier=r.get("tier"),
                              rank=(r.get("fit_choice") or 0) - r["fit_gold"], text=r["text"], gold=r["gold"],
                              jev=r["choice"], confidence=r["confidence"], p_gold=r["p_gold"], fit_gold=r["fit_gold"],
                              fit_choice=r.get("fit_choice"), ambiguous=r["ambiguous"], conventions=r["conventions"],
                              top3=top, seen_v2=r["id"] in seen, v2_flag=r["id"] in v2flags))
    order = {("error_candidate", "high"): 0, ("error_candidate", "mid"): 1, ("ambiguous_candidate", None): 2,
             ("error_candidate", "low"): 3, ("weak_disagree", None): 4, ("none_candidate", None): 5}
    queue.sort(key=lambda q: (q["dataset"], order.get((q["band"], q["tier"]), 9), -q["rank"], -q["confidence"]))
    pos = Counter()
    for q in queue:
        pos[q["dataset"]] += 1
        q["queue_pos"] = pos[q["dataset"]]
    (OUT / "summary.json").write_text(json.dumps(summary, indent=1))
    with (OUT / "queue.jsonl").open("w") as f:
        for q in queue:
            f.write(json.dumps(q) + "\n")
    print(f"{'dataset':10} {'rows':>5} {'agree':>6} {'ECE':>5} {'err%':>5} {'hi/mid/lo':>10} {'amb%':>5} {'none%':>5} "
          f"{'weak':>5} {'agrUnfit':>8} {'v2flags->err/amb/agree':>22} {'2nd':>4} {'cost':>7}")
    for s in summary:
        b, t, l = s["bands"], s["error_tiers"], s["v2_flag_landing"]
        print(f"{s['dataset']:10} {s['rows']:5d} {s['agreement']:6.3f} {s['ece']:5.3f} {s['error_rate']*100:5.1f} "
              f"{t.get('high',0):3d}/{t.get('mid',0):3d}/{t.get('low',0):<3d} {s['ambiguous_rate']*100:5.1f} "
              f"{s['none_rate']*100:5.1f} {b.get('weak_disagree',0):5d} {b.get('agree_gold_unfit',0):8d} "
              f"{s['v2_flags']:5d}->{l.get('error_candidate',0):3d}/{l.get('ambiguous_candidate',0):3d}/"
              f"{l.get('agree',0)+l.get('agree_gold_unfit',0):<3d} {s['second_calls']:4d} {s['cost_usd']:7.4f}")
    print(f"queue rows {len(queue)} -> {OUT}/queue.jsonl")


if __name__ == "__main__":
    main()
