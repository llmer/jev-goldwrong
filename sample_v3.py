"""Stratified review samples from out_v3/queue.jsonl, held out from every row v2 reviewers saw.

Writes review_v3/<dataset>.jsonl   what the reviewer sees: id, text, gold, jev, top3 (no band, no noul values)
       review_v3/<dataset>.meta.json  id -> band / tier / fit values, for the report only
Usage: python3 sample_v3.py [--datasets a,b] [--force]
"""
import argparse, json, os, random
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
VERSION = os.environ.get("VERSION", "v3")
OUT, REV = HERE / f"out_{VERSION}", HERE / f"review_{VERSION}"
QUOTA = {("error_candidate", "high"): 50, ("error_candidate", "mid"): 20, ("error_candidate", "low"): 10,
         ("ambiguous_candidate", None): 25, ("none_candidate", None): 15, ("weak_disagree", None): 10}

ap = argparse.ArgumentParser()
ap.add_argument("--datasets", default="")
ap.add_argument("--force", action="store_true")
a = ap.parse_args()
random.seed(11)
rows = [json.loads(l) for l in (OUT / "queue.jsonl").read_text().splitlines()]
by = defaultdict(lambda: defaultdict(list))
for q in rows:
    if q["seen_v2"]:
        continue
    by[q["dataset"]][(q["band"], q["tier"])].append(q)
REV.mkdir(exist_ok=True)
for ds in (a.datasets.split(",") if a.datasets else sorted(by)):
    out = REV / f"{ds}.jsonl"
    if out.exists() and not a.force:
        print(ds, "exists, skipping")
        continue
    sample, counts = [], {}
    for key, n in QUOTA.items():
        items = by[ds].get(key, [])
        pick = items if len(items) <= n else random.sample(items, n)
        sample += pick
        counts[f"{key[0]}/{key[1]}"] = f"{len(pick)}/{len(items)}"
    random.shuffle(sample)
    with out.open("w") as fh:
        for q in sample:
            fh.write(json.dumps({k: q[k] for k in ("id", "text", "gold", "jev", "top3")}) + "\n")
    (REV / f"{ds}.meta.json").write_text(json.dumps(
        {q["id"]: {k: q[k] for k in ("band", "tier", "rank", "queue_pos", "confidence", "fit_gold", "fit_choice",
                                      "ambiguous", "conventions", "v2_flag")} for q in sample}, indent=0))
    print(ds, len(sample), counts)
