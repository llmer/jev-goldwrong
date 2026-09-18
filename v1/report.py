"""Join reviewer verdicts with flags; precision per dataset; extrapolate; write out/report.md"""
import json, math
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
summary = {s["dataset"]: s for s in json.loads((HERE / "out/summary.json").read_text())}
ledger = json.loads((HERE / "out/ledger.json").read_text())
lines = ["# Label-error hunt pilot (Jev via OpenRouter)", "",
         f"Spend: ${ledger['cost_usd']:.2f} for {ledger['calls']:,} calls, {ledger['input_tokens']:,} input tokens.", "",
         "| dataset | rows | agree w/ gold | agree @conf>=.9 | coverage @.9 | ECE | flagged | reviewed | gold wrong | jev wrong | ambiguous | precision | est. gold errors |",
         "|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|"]
striking = []
tot_flag = tot_est = tot_rows = tot_rev = tot_gw = tot_jw = tot_amb = 0
rows_out = []
for ds, s in summary.items():
    vpath = HERE / f"review/{ds}.verdicts.jsonl"
    if not vpath.exists():
        continue
    flags = {json.loads(l)["id"]: json.loads(l) for l in (HERE / f"review/{ds}.jsonl").read_text().splitlines()}
    verdicts = [json.loads(l) for l in vpath.read_text().splitlines()]
    c = Counter(v["verdict"] for v in verdicts)
    n = len(verdicts)
    prec = c["gold_wrong"] / n if n else 0
    # Wilson 95% interval on precision
    z = 1.96
    centre = (prec + z*z/(2*n)) / (1 + z*z/n) if n else 0
    half = z * math.sqrt(prec*(1-prec)/n + z*z/(4*n*n)) / (1 + z*z/n) if n else 0
    est = round(prec * s["flagged"])
    tot_flag += s["flagged"]; tot_est += est; tot_rows += s["rows"]; tot_rev += n
    tot_gw += c["gold_wrong"]; tot_jw += c["jev_wrong"]; tot_amb += c["ambiguous"]
    rows_out.append((ds, s, n, c, prec, est))
    lines.append(f"| {ds} | {s['rows']} | {s['agreement']:.3f} | {(s['agreement_at_conf90'] or 0):.3f} | "
                 f"{s['coverage_at_conf90']:.2f} | {s['ece']:.3f} | {s['flagged']} | {n} | {c['gold_wrong']} | "
                 f"{c['jev_wrong']} | {c['ambiguous']} | {prec:.2f} ({centre-half:.2f}-{centre+half:.2f}) | ~{est} "
                 f"({est/s['rows']*100:.1f}% of rows) |")
    for v in verdicts:
        if v["verdict"] == "gold_wrong" and v["id"] in flags:
            f = flags[v["id"]]
            striking.append((ds, f["p_gold"], f["text"], f["gold"], v.get("correct_label", f["jev"]), v.get("reason", "")))
lines.append(f"| **total** | {tot_rows} | | | | | {tot_flag} | {tot_rev} | {tot_gw} | {tot_jw} | {tot_amb} | "
             f"{tot_gw/tot_rev:.2f} | ~{tot_est} ({tot_est/tot_rows*100:.1f}%) |")
lines += ["", f"Rows judged: {tot_rows:,}. Flags: {tot_flag:,}. Flags reviewed: {tot_rev}. "
          f"Estimated true gold errors among flags: ~{tot_est:,}. Jev was the wrong party in {tot_jw} of {tot_rev} reviewed flags.", "",
          "## Where the flags land", "",
          "- Mostly real label errors (precision >= 0.5): " + ", ".join(f"{d} ({p:.2f})" for d, _, _, _, p, _ in sorted(rows_out, key=lambda r: -r[4]) if p >= 0.5),
          "- Mixed, mostly ambiguous or convention (0.25-0.5): " + ", ".join(f"{d} ({p:.2f})" for d, _, _, _, p, _ in sorted(rows_out, key=lambda r: -r[4]) if 0.25 <= p < 0.5),
          "- Mostly Jev missing dataset conventions or ground truth by construction (< 0.25): " + ", ".join(f"{d} ({p:.2f})" for d, _, _, _, p, _ in sorted(rows_out, key=lambda r: -r[4]) if p < 0.25), "",
          "Flag rule: P(gold) < 0.2 and P(Jev choice) > 0.7. Reviewer: Claude Code, one strict annotator per dataset, "
          "verdicts gold_wrong / jev_wrong / ambiguous. Precision = gold_wrong / reviewed, Wilson 95% CI.", "",
          "## Verified gold errors (sample)", ""]
by = Counter()
for ds, p, text, gold, corr, reason in sorted(striking, key=lambda x: (x[0], x[1])):
    if by[ds] >= 8:
        continue
    by[ds] += 1
    lines.append(f"- **{ds}** gold=`{gold}` -> `{corr}`: \"{text[:140].strip()}\" ({reason})")
(HERE / "out/report.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
