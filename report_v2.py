"""v2 report: precision from verdicts, v1 vs v2 on the same datasets, noul-only yield. Writes out/report_v2.md"""
import json, math
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
summary = {s["dataset"]: s for s in json.loads((HERE / "out/summary.json").read_text())}
v1sum = {s["dataset"]: s for s in json.loads((HERE / "v1/out/summary.json").read_text())}
ledger = json.loads((HERE / "out/ledger.json").read_text())


def verdicts(path):
    return [json.loads(l) for l in path.read_text().splitlines()] if path.exists() else []


def wilson(k, n, z=1.96):
    if not n:
        return (0, 0)
    p = k / n
    c = (p + z*z/(2*n)) / (1 + z*z/n)
    h = z * math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / (1 + z*z/n)
    return (c - h, c + h)


L = ["# Experiment 2 (v2): cookbook conventions", "",
     f"Spend: ${ledger['cost_usd']:.2f} for {ledger['calls']:,} calls, {ledger['input_tokens']:,} input tokens.", "",
     "## v1 vs v2 flag quality (same datasets, same reviewer protocol)", "",
     "| dataset | rows | v1 agree | v2 agree | v1 flag% | v2 flag% | v2 none% | v2 unsure% | v1 precision | v2 precision | v1 jev-wrong | v2 jev-wrong | v1 est. errors | v2 est. errors |",
     "|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|"]
tot = Counter()
examples = []
for ds, s in summary.items():
    v1 = v1sum.get(ds, {})
    v1v = verdicts(HERE / f"v1/review/{ds}.verdicts.jsonl")
    v2v = verdicts(HERE / f"review/{ds}.verdicts.jsonl")
    c1, c2 = Counter(v["verdict"] for v in v1v), Counter(v["verdict"] for v in v2v)
    n1, n2 = len(v1v), len(v2v)
    p1 = c1["gold_wrong"] / n1 if n1 else 0
    p2 = c2["gold_wrong"] / n2 if n2 else 0
    lo, hi = wilson(c2["gold_wrong"], n2)
    flags2 = s["bands"].get("flag", 0)
    est1 = round(p1 * v1.get("flagged", 0)); est2 = round(p2 * flags2)
    tot.update(dict(n1=n1, n2=n2, gw1=c1["gold_wrong"], gw2=c2["gold_wrong"], jw1=c1["jev_wrong"], jw2=c2["jev_wrong"],
                    est1=est1, est2=est2, rows=s["rows"], f1=v1.get("flagged", 0), f2=flags2))
    L.append(f"| {ds} | {s['rows']} | {v1.get('agreement', 0):.3f} | {s['agreement']:.3f} | {v1.get('flag_rate', 0)*100:.1f} | "
             f"{s['flag_rate']*100:.1f} | {s['none_rate']*100:.1f} | {s['uncertain_rate']*100:.1f} | "
             f"{p1:.2f} (n={n1}) | {p2:.2f} ({lo:.2f}-{hi:.2f}, n={n2}) | {c1['jev_wrong']/n1*100 if n1 else 0:.0f}% | "
             f"{c2['jev_wrong']/n2*100 if n2 else 0:.0f}% | ~{est1} | ~{est2} |")
    flags = {json.loads(l)["id"]: json.loads(l) for l in (HERE / f"review/{ds}.jsonl").read_text().splitlines()} \
        if (HERE / f"review/{ds}.jsonl").exists() else {}
    k = 0
    for v in v2v:
        if v["verdict"] == "gold_wrong" and v["id"] in flags and k < 5:
            f = flags[v["id"]]
            examples.append(f"- **{ds}** gold=`{f['gold']}` -> `{v.get('correct_label', f['jev'])}` "
                            f"(gold_wrong noul {f['gold_wrong']:.2f}): \"{str(f['text'])[:140].strip()}\" ({v.get('reason','')})")
            k += 1
L.append(f"| **total** | {tot['rows']} | | | | | | | {tot['gw1']/tot['n1']:.2f} (n={tot['n1']}) | "
         f"{tot['gw2']/tot['n2']:.2f} (n={tot['n2']}) | {tot['jw1']/tot['n1']*100:.0f}% | {tot['jw2']/tot['n2']*100:.0f}% | "
         f"~{tot['est1']} | ~{tot['est2']} |")
L += ["", "v2 flag = Jev's confident disagreement: final label != gold, label != none, confidence >= the dev-split threshold "
      "(smallest grid value whose confident subset agrees with gold >= 95% on the first 500 rows). v1 flag = P(gold) < 0.2 and "
      "P(top) > 0.7 over all rows. Both reviewed by the same Claude Code protocol.", "",
      "## Companion noul: 'is the gold label wrong?'", "",
      "| dataset | gold_wrong >= 0.7 | also a flag | noul-only | noul-only reviewed | gold_wrong | jev_wrong | ambiguous | noul-only precision |",
      "|---|--:|--:|--:|--:|--:|--:|--:|--:|"]
for ds, s in summary.items():
    nv = verdicts(HERE / f"review/{ds}_noul.verdicts.jsonl")
    c = Counter(v["verdict"] for v in nv)
    n = len(nv)
    L.append(f"| {ds} | {s['gold_wrong_hi']} | {s['flag_and_noul']} | {s['noul_only']} | {n} | {c['gold_wrong']} | "
             f"{c['jev_wrong']} | {c['ambiguous']} | {c['gold_wrong']/n if n else 0:.2f} |")
L += ["", "## Other v2 measurements", ""]
for ds, s in summary.items():
    extra = []
    if s.get("rerank_calls"):
        extra.append(f"rerank on {s['rerank_calls']} rows: agreement with gold {s['rerank_agree_before']} -> "
                     f"{s['rerank_agree_after']} (ablation; not used)")
    if s.get("family_agree_when_unsure") is not None:
        extra.append(f"coarse family agreement on unsure+flag rows: {s['family_agree_when_unsure']:.2f}")
    extra.append(f"threshold {s['threshold']}, ECE {s['ece']:.3f}, fits_any<0.5 on {s['fits_any_low']} test rows, "
                 f"p50 {s['median_latency_ms']} ms")
    L.append(f"- **{ds}**: " + "; ".join(extra))
L += ["", "## Verified gold errors found by v2 (sample)", ""] + examples
(HERE / "out/report_v2.md").write_text("\n".join(L) + "\n")
print("\n".join(L))
