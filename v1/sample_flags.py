"""Write review/<dataset>.jsonl samples of flags. Usage: python3 sample_flags.py --n 60 [--datasets a,b] [--force]"""
import argparse, json, random, collections
from pathlib import Path
HERE = Path(__file__).parent
ap = argparse.ArgumentParser(); ap.add_argument("--n", type=int, default=60); ap.add_argument("--datasets", default="")
ap.add_argument("--force", action="store_true"); a = ap.parse_args()
random.seed(7)
fl = [json.loads(l) for l in (HERE / "out/flags.jsonl").read_text().splitlines()]
by = collections.defaultdict(list)
for f in fl: by[f["dataset"]].append(f)
want = a.datasets.split(",") if a.datasets else sorted(by)
(HERE / "review").mkdir(exist_ok=True)
for ds in want:
    out = HERE / f"review/{ds}.jsonl"
    if out.exists() and not a.force:
        print(ds, "exists, skipping"); continue
    items = by.get(ds, [])
    sample = items if len(items) <= a.n else random.sample(items, a.n)
    with out.open("w") as fh:
        for f in sample:
            fh.write(json.dumps({k: f[k] for k in ("id", "text", "gold", "jev", "p_gold", "p_jev", "top3")}) + "\n")
    print(ds, "flags", len(items), "sampled", len(sample))
