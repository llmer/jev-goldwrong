"""v3 report: per-band precision from held-out verdicts, v2 comparison, convention signals, verified examples.
Writes out_v3/report_v3.md"""
import json, math, os
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).parent
VERSION = os.environ.get("VERSION", "v3")
OUT, REV = HERE / f"out_{VERSION}", HERE / f"review_{VERSION}"
summary = {s["dataset"]: s for s in json.loads((OUT / "summary.json").read_text())}
v2sum = {s["dataset"]: s for s in json.loads((HERE / "out/summary.json").read_text())}
ledger = json.loads((OUT / "ledger.json").read_text())


def wilson(k, n, z=1.96):
    if not n:
        return (0, 0)
    p = k / n
    c = (p + z*z/(2*n)) / (1 + z*z/n)
    h = z * math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / (1 + z*z/n)
    return (c - h, c + h)


def load(ds):
    vp = REV / f"{ds}.verdicts.jsonl"
    if not vp.exists():
        return [], {}, {}
    v = [json.loads(l) for l in vp.read_text().splitlines()]
    meta = json.loads((REV / f"{ds}.meta.json").read_text())
    rows = {json.loads(l)["id"]: json.loads(l) for l in (REV / f"{ds}.jsonl").read_text().splitlines()}
    return v, meta, rows


def v2_precision(ds):
    p = HERE / f"review/{ds}.verdicts.jsonl"
    if not p.exists():
        return 0, 0
    v = [json.loads(l) for l in p.read_text().splitlines()]
    return sum(x["verdict"] == "gold_wrong" for x in v), len(v)


L = [f"# {VERSION} report: bands, held-out precision, v2 comparison", "",
     f"Spend: ${ledger['cost_usd']:.2f} for {ledger['calls']:,} calls, {ledger['input_tokens']:,} input tokens. "
     f"Model reported by the API: {', '.join(sorted({m for s in summary.values() for m in s['models']}))}.", "",
     "## Band precision on held-out rows (never seen by v2 reviewers)", "",
     "| dataset | band | tier | in band | reviewed | gold_wrong | jev_wrong | ambiguous | precision (95% CI) |",
     "|---|---|---|--:|--:|--:|--:|--:|--:|"]
tot = defaultdict(Counter)
examples, conv_lines = [], []
for ds, s in summary.items():
    v, meta, rows = load(ds)
    by = defaultdict(Counter)
    for x in v:
        m = meta.get(x["id"])
        if not m:
            continue
        by[(m["band"], m["tier"])][x["verdict"]] += 1
        by[(m["band"], m["tier"])]["n"] += 1
        tot[(m["band"], m["tier"])][x["verdict"]] += 1
        tot[(m["band"], m["tier"])]["n"] += 1
    for (b, t), c in sorted(by.items()):
        n_band = s["error_tiers"].get(t, 0) if b == "error_candidate" else s["bands"].get(b, 0)
        lo, hi = wilson(c["gold_wrong"], c["n"])
        L.append(f"| {ds} | {b} | {t or ''} | {n_band} | {c['n']} | {c['gold_wrong']} | {c['jev_wrong']} | "
                 f"{c['ambiguous']} | {c['gold_wrong']/c['n']:.2f} ({lo:.2f}-{hi:.2f}) |")
    k = 0
    for x in v:
        m = meta.get(x["id"])
        if x["verdict"] == "gold_wrong" and m and m["band"] == "error_candidate" and k < 4:
            r = rows[x["id"]]
            examples.append(f"- **{ds}** gold=`{r['gold']}` -> `{x.get('correct_label', r['jev'])}` "
                            f"(fit_gold {m['fit_gold']:.2f}, fit_jev {m['fit_choice']:.2f}, ambiguous {m['ambiguous']:.2f}): "
                            f"\"{str(r['text'])[:140].strip()}\" ({x.get('reason', '')})")
            k += 1
    conv_lines.append(f"- **{ds}**: " + "; ".join(
        f"{q} " + ", ".join(f"{b}={v}" for b, v in sorted(bb.items())) for q, bb in s["conventions"].items()))
for (b, t), c in sorted(tot.items()):
    lo, hi = wilson(c["gold_wrong"], c["n"])
    L.append(f"| **all** | {b} | {t or ''} | | {c['n']} | {c['gold_wrong']} | {c['jev_wrong']} | {c['ambiguous']} | "
             f"{c['gold_wrong']/c['n']:.2f} ({lo:.2f}-{hi:.2f}) |")

L += ["", "Bands are fixed in advance from Jev's own answers (cutoff 0.5 on every noul; confidence tiers 0.9 / 0.5), not "
      "tuned against gold. error_candidate = gold label does not fit, Jev's label fits, not ambiguous.", "",
      "## v2 vs v3 on the same datasets", "",
      "| dataset | rows | v2 agree | v3 agree | v2 flag% | v3 error% (hi/mid/lo) | v3 amb% | v3 none% | v2 precision | "
      "v3 error-band precision | where v2 flags landed in v3 (error/amb/agree/other) |",
      "|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|"]
for ds, s in summary.items():
    v2 = v2sum.get(ds, {})
    k2, n2 = v2_precision(ds)
    v, meta, _ = load(ds)
    ec = Counter(x["verdict"] for x in v if meta.get(x["id"], {}).get("band") == "error_candidate")
    ne = sum(ec.values())
    land = s["v2_flag_landing"]
    other = s["v2_flags"] - land.get("error_candidate", 0) - land.get("ambiguous_candidate", 0) - land.get("agree", 0) \
        - land.get("agree_gold_unfit", 0)
    t = s["error_tiers"]
    L.append(f"| {ds} | {s['rows']} | {v2.get('agreement', 0):.3f} | {s['agreement']:.3f} | {v2.get('flag_rate', 0)*100:.1f} | "
             f"{s['error_rate']*100:.1f} ({t.get('high',0)}/{t.get('mid',0)}/{t.get('low',0)}) | "
             f"{s['ambiguous_rate']*100:.1f} | {s['none_rate']*100:.1f} | {k2/n2 if n2 else 0:.2f} (n={n2}) | "
             f"{ec['gold_wrong']/ne if ne else 0:.2f} (n={ne}) | {s['v2_flags']}: {land.get('error_candidate',0)}/"
             f"{land.get('ambiguous_candidate',0)}/{land.get('agree',0)+land.get('agree_gold_unfit',0)}/{other} |")
L += ["", "v2 flag rate is over the v2 test split (rows after the dev split); v3 rates are over all rows.", "",
      "## Convention nouls: mean value by band", ""] + conv_lines
L += ["", "## Other v3 measurements", ""]
for ds, s in summary.items():
    L.append(f"- **{ds}**: ECE {s['ece']:.3f}, agree-but-gold-unfit {s['bands'].get('agree_gold_unfit', 0)}, "
             f"weak_disagree {s['bands'].get('weak_disagree', 0)}, second calls {s['second_calls']}, "
             f"p50 {s['median_latency_ms']} ms, ${s['cost_usd']:.3f}")
L += ["", "## Verified gold errors from the error band (held-out sample)", ""] + examples
(OUT / f"report_{VERSION}.md").write_text("\n".join(L) + "\n")
print("\n".join(L))
