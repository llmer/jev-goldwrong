"""v2 scorecard: dev-split threshold, bands from Jev's own outputs, noul agreement, family fallback, v1 comparison."""
import json, math
from collections import Counter, defaultdict
from pathlib import Path

from datasets_v2 import DATASETS, NONE_ID

HERE = Path(__file__).parent
OUT = HERE / "out"
V1 = HERE / "v1/out"
TARGET_AGREE = 0.95
GRID = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
NOUL_T = 0.7
USE_RERANK = False  # ablation showed the rerank stage hurt Banking77 (447 -> 362 agree on 818 rows); first stage is final


def conf(r):
    return r.get("final_confidence", r["confidence"])


def ece(recs, bins=10):
    total, err, buckets = len(recs), 0.0, defaultdict(list)
    for r in recs:
        p = max(r["probabilities"].values())
        buckets[min(int(p * bins), bins - 1)].append((p, r["final"] == r["gold"]))
    for items in buckets.values():
        err += len(items) / total * abs(sum(p for p, _ in items) / len(items) - sum(c for _, c in items) / len(items))
    return err


def pick_threshold(dev):
    """Smallest grid threshold whose confident subset agrees with gold >= TARGET_AGREE (classification cookbook)."""
    for t in GRID:
        sub = [r for r in dev if conf(r) >= t]
        if sub and sum(r["final"] == r["gold"] for r in sub) / len(sub) >= TARGET_AGREE:
            return t
    return 0.9


def main():
    summary, flags, noul_only = [], [], []
    for name, spec in DATASETS.items():
        path = OUT / f"{name}.jsonl"
        if not path.exists():
            continue
        recs = [json.loads(l) for l in path.read_text().splitlines()]
        recs = [r for r in recs if "error" not in r]
        if not USE_RERANK:
            for r in recs:
                r["final"] = r["choice"]
                r.pop("final_confidence", None)
        ndev = min(500, len(recs) // 5)
        for r in recs:
            r["dev"] = int(r["id"].rsplit(":", 1)[1]) < ndev
        dev = [r for r in recs if r["dev"]]
        test = [r for r in recs if not r["dev"]]
        if not test:
            continue
        t = pick_threshold(dev)
        bands = Counter()
        fam = spec.get("family")
        fam_agree = fam_n = 0
        for r in test:
            if r["final"] == NONE_ID:
                b = "none"
            elif conf(r) < t:
                b = "uncertain"
            elif r["final"] == r["gold"]:
                b = "agree"
            else:
                b = "flag"
            r["band"] = b
            bands[b] += 1
            if fam and b in ("uncertain", "flag"):
                fam_n += 1
                fam_agree += fam.get(r["final"]) == fam.get(r["gold"])
        flag_recs = [r for r in test if r["band"] == "flag"]
        gw_hi = [r for r in test if r["gold_wrong"] >= NOUL_T]
        both = [r for r in flag_recs if r["gold_wrong"] >= NOUL_T]
        nonly = [r for r in gw_hi if r["band"] not in ("flag", "none")]
        lat = sorted(r["latency_ms"] for r in recs)
        cost = sum(r["usage"].get("cost", 0) + r.get("rerank", {}).get("usage", {}).get("cost", 0) for r in recs)
        rer = [r for r in recs if "rerank" in r]
        rer_changed = sum(r["rerank"]["choice"] != r["choice"] for r in rer)
        rer_before = sum(r["choice"] == r["gold"] for r in rer)
        rer_after = sum(r["rerank"]["choice"] == r["gold"] for r in rer)
        s = dict(dataset=name, rows=len(recs), dev=len(dev), test=len(test), threshold=t,
                 agreement=sum(r["final"] == r["gold"] for r in recs) / len(recs),
                 ece=ece(recs), bands=dict(bands),
                 flag_rate=bands["flag"] / len(test), none_rate=bands["none"] / len(test),
                 uncertain_rate=bands["uncertain"] / len(test),
                 gold_wrong_hi=len(gw_hi), flag_and_noul=len(both), noul_only=len(nonly),
                 fits_any_low=sum(r["fits_any"] < 0.5 for r in test),
                 family_agree_when_unsure=(fam_agree / fam_n) if fam_n else None,
                 rerank_calls=len(rer), rerank_changed=rer_changed, rerank_agree_before=rer_before,
                 rerank_agree_after=rer_after,
                 cost_usd=cost, median_latency_ms=lat[len(lat) // 2], p95_latency_ms=lat[int(len(lat) * .95)])
        # v1 comparison on the same dataset (v1 had no dev split; compare flag rate on all rows)
        v1p = V1 / f"{name}.jsonl"
        if v1p.exists():
            v1 = [json.loads(l) for l in v1p.read_text().splitlines()]
            v1 = [r for r in v1 if "error" not in r]
            v1flags = [r for r in v1 if r["p_gold"] is not None and r["p_gold"] < 0.2 and max(r["probabilities"].values()) > 0.7]
            s["v1_agreement"] = sum(r["choice"] == r["gold"] for r in v1) / len(v1)
            s["v1_flag_rate"] = len(v1flags) / len(v1)
        summary.append(s)
        for r in flag_recs:
            top = sorted(r["probabilities"].items(), key=lambda kv: -kv[1])[:3]
            flags.append(dict(id=r["id"], dataset=name, text=r["text"], gold=r["gold"], jev=r["final"],
                              confidence=conf(r), p_gold=r["p_gold"], gold_wrong=r["gold_wrong"],
                              fits_any=r["fits_any"], top3=top, rerank=r.get("rerank", {}).get("candidates")))
        for r in nonly:
            top = sorted(r["probabilities"].items(), key=lambda kv: -kv[1])[:3]
            noul_only.append(dict(id=r["id"], dataset=name, text=r["text"], gold=r["gold"], jev=r["final"],
                                  confidence=conf(r), p_gold=r["p_gold"], gold_wrong=r["gold_wrong"],
                                  fits_any=r["fits_any"], top3=top, band=r["band"]))
    (OUT / "summary.json").write_text(json.dumps(summary, indent=1))
    for fname, items in (("flags.jsonl", flags), ("noul_only.jsonl", noul_only)):
        with (OUT / fname).open("w") as f:
            for it in items:
                f.write(json.dumps(it) + "\n")
    print(f"{'dataset':10} {'rows':>5} {'thr':>4} {'agree':>6} {'v1agr':>6} {'ECE':>5} {'flag%':>6} {'v1flg%':>6} "
          f"{'none%':>6} {'unc%':>6} {'gw>.7':>6} {'both':>5} {'noul+':>5} {'famAgr':>6} {'rerank':>7} {'cost':>7}")
    for s in summary:
        print(f"{s['dataset']:10} {s['rows']:5d} {s['threshold']:4.2f} {s['agreement']:6.3f} {s.get('v1_agreement',0):6.3f} "
              f"{s['ece']:5.3f} {s['flag_rate']*100:6.1f} {s.get('v1_flag_rate',0)*100:6.1f} {s['none_rate']*100:6.1f} "
              f"{s['uncertain_rate']*100:6.1f} {s['gold_wrong_hi']:6d} {s['flag_and_noul']:5d} {s['noul_only']:5d} "
              f"{(s['family_agree_when_unsure'] or 0):6.2f} {s['rerank_calls']:3d}/{s['rerank_changed']:<3d} {s['cost_usd']:7.4f}")
    print(f"flags {len(flags)} -> out/flags.jsonl; noul-only {len(noul_only)} -> out/noul_only.jsonl")


if __name__ == "__main__":
    main()
