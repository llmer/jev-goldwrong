"""Two-model verification of the high tier before a human sees it (the docs' verify-and-escalate cascade turned on
our own queue).

  python3 verify.py split     # verify_<VERSION>/<dataset>.jsonl: every high-tier row, blind (id, text, gold, jev, top3)
  python3 verify.py merge     # after <dataset>.claude.verdicts.jsonl and <dataset>.codex.verdicts.jsonl exist:
                              #   agreement matrix, human_queue.jsonl (both say gold_wrong), disagreements.jsonl,
                              #   and calibration against the experiment's own reviewer where rows overlap
Env: VERSION (default v4)
"""
import json, os, sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).parent
VERSION = os.environ.get("VERSION", "v4")
OUT, VER, REV = HERE / f"out_{VERSION}", HERE / f"verify_{VERSION}", HERE / f"review_{VERSION}"
REVIEWERS = ("claude", "codex")


def rows():
    return [json.loads(l) for l in (OUT / "queue.jsonl").read_text().splitlines()]


def split():
    VER.mkdir(exist_ok=True)
    by = defaultdict(list)
    for q in rows():
        if q["band"] == "error_candidate" and q["tier"] == "high":
            by[q["dataset"]].append(q)
    for ds, items in sorted(by.items()):
        items.sort(key=lambda q: q["queue_pos"])
        with (VER / f"{ds}.jsonl").open("w") as f:
            for q in items:
                f.write(json.dumps({k: q[k] for k in ("id", "text", "gold", "jev", "top3")}) + "\n")
        print(ds, len(items))


def load_verdicts(path):
    return {json.loads(l)["id"]: json.loads(l) for l in path.read_text().splitlines()} if path.exists() else {}


def merge():
    meta = {q["id"]: q for q in rows()}
    own = {}
    for p in REV.glob("*.verdicts.jsonl"):
        own.update(load_verdicts(p))
    matrix, per_ds = Counter(), defaultdict(Counter)
    human, disagree, calib = [], [], defaultdict(Counter)
    for p in sorted(VER.glob("*.jsonl")):
        if ".verdicts" in p.name or p.name in ("human_queue.jsonl", "disagreements.jsonl"):
            continue
        ds = p.stem
        vs = {r: load_verdicts(VER / f"{ds}.{r}.verdicts.jsonl") for r in REVIEWERS}
        for l in p.read_text().splitlines():
            row = json.loads(l)
            got = {r: vs[r].get(row["id"], {}).get("verdict", "missing") for r in REVIEWERS}
            key = "/".join(got[r] for r in REVIEWERS)
            matrix[key] += 1
            per_ds[ds][key] += 1
            rec = {**row, "queue_pos": meta[row["id"]]["queue_pos"], "fit_gold": meta[row["id"]]["fit_gold"],
                   "fit_jev": meta[row["id"]]["fit_choice"], "ambiguous": meta[row["id"]]["ambiguous"],
                   **{f"{r}_verdict": got[r] for r in REVIEWERS},
                   **{f"{r}_label": vs[r].get(row["id"], {}).get("correct_label") for r in REVIEWERS},
                   **{f"{r}_reason": vs[r].get(row["id"], {}).get("reason") for r in REVIEWERS}}
            if all(got[r] == "gold_wrong" for r in REVIEWERS):
                rec["labels_agree"] = len({vs[r][row["id"]].get("correct_label") for r in REVIEWERS}) == 1
                human.append(rec)
            elif "missing" not in got.values():
                disagree.append(rec)
            if row["id"] in own:
                for r in REVIEWERS:
                    calib[r][(own[row["id"]]["verdict"], got[r])] += 1
    for name, items in (("human_queue.jsonl", human), ("disagreements.jsonl", disagree)):
        with (VER / name).open("w") as f:
            for it in items:
                f.write(json.dumps(it) + "\n")
    n = sum(matrix.values())
    print(f"high-tier rows: {n}")
    print("claude/codex verdict pairs:")
    for k, c in matrix.most_common():
        print(f"  {k:28} {c:4d}  {c/n*100:5.1f}%")
    print("per dataset, both gold_wrong / any gold_wrong / n:")
    for ds, c in sorted(per_ds.items()):
        both = c["gold_wrong/gold_wrong"]
        anyg = sum(v for k, v in c.items() if "gold_wrong" in k.split("/"))
        print(f"  {ds:10} {both:4d} / {anyg:4d} / {sum(c.values()):4d}")
    same_label = sum(h["labels_agree"] for h in human)
    print(f"human queue: {len(human)} rows both call gold wrong, {same_label} with the same corrected label; "
          f"{len(disagree)} disagreements -> {VER}/")
    for r in REVIEWERS:
        if calib[r]:
            print(f"calibration vs this experiment's reviewer ({r}), (reviewer, {r}) -> n:")
            for (a, b), c in sorted(calib[r].items()):
                print(f"  {a:10} -> {b:10} {c}")


if __name__ == "__main__":
    {"split": split, "merge": merge}[sys.argv[1]]()
