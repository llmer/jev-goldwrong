# /// script
# requires-python = ">=3.11"
# dependencies = ["datasets>=3", "pyarrow", "httpx[http2]"]
# ///
"""v2 label-error hunt following TypeSafe cookbook conventions.

Per row, ONE call with three questions (parallel questions cookbook):
  label      choice over the dataset's labels + "none", rich descriptions with conventions
  fits_any   noul: does the text clearly fit at least one label?
  gold_wrong noul: the dataset says <gold>; is that wrong?  (gold is in this question's instructions only;
             questions are evaluated in isolation so the choice question never sees it)
Banking77 adds a rerank call (skill-suggestion cookbook) when the top probability < RERANK_BELOW:
  top-3 candidates + none, instruction to read each description closely.
Rows with index < DEV are the dev split for choosing the confidence threshold (classification cookbook).

Usage: uv run run_v2.py [--limit N] [--datasets a,b] [--concurrency 16] [--dry-run]
Env: OPENROUTER_API_KEY, BUDGET_USD (hard cap, default 3.0)
"""
import argparse, asyncio, json, os, time
from pathlib import Path

import httpx
from datasets import load_dataset

from datasets_v2 import DATASETS, NONE_DESC, NONE_ID

HERE = Path(__file__).parent
OUT = HERE / "out"
LEDGER = OUT / "ledger.json"
URL = "https://openrouter.ai/api/alpha/decisions"
MODEL = "typesafe/jev-1.13"
DEV = 500
RERANK_BELOW = 0.9
RERANK_K = 3

RULES = ("Choose the single label a careful human annotator following the dataset guidelines and the option "
         "descriptions would assign. Text may be lowercased, tokenized, or informal. Judge the text itself. "
         f"Choose '{NONE_ID}' only when no offered label fits.")


def load_rows(name, spec, limit):
    ds = load_dataset(spec["hf"], spec["config"], split=spec["split"]) if spec["config"] else \
        load_dataset(spec["hf"], split=spec["split"])
    names = getattr(ds.features[spec["label"]], "names", None)
    rows = []
    for i, r in enumerate(ds):
        gold = r[spec["label"]]
        gold = names[gold] if names else gold
        gold = spec.get("gold_map", {}).get(gold, gold)
        rows.append({"id": f"{name}:{spec['split']}:{i}", "idx": i, "text": r[spec["text"]], "gold": gold})
    return rows[:limit] if limit else rows


def load_ledger():
    return json.loads(LEDGER.read_text()) if LEDGER.exists() else {"cost_usd": 0.0, "calls": 0, "input_tokens": 0}


class Budget:
    def __init__(self, cap):
        self.ledger, self.cap, self.lock = load_ledger(), cap, asyncio.Lock()

    def exceeded(self):
        return self.ledger["cost_usd"] >= self.cap

    async def add(self, usage):
        async with self.lock:
            self.ledger["cost_usd"] += usage.get("cost", 0.0)
            self.ledger["calls"] += 1
            self.ledger["input_tokens"] += usage.get("input_tokens", 0)
            LEDGER.write_text(json.dumps(self.ledger))


async def post(client, key, body, budget, stats):
    for attempt in range(5):
        try:
            r = await client.post(URL, json=body, headers={"Authorization": f"Bearer {key}"})
        except httpx.HTTPError:
            stats["errors"] += 1
            await asyncio.sleep(0.5 * 2**attempt)
            continue
        if r.status_code in (429, 500, 502, 503, 504) or 520 <= r.status_code <= 529:
            stats["retries"] += 1
            await asyncio.sleep(0.5 * 2**attempt)
            continue
        if r.is_error:
            raise RuntimeError(f"HTTP {r.status_code}: {r.text[:200]}")
        data = r.json()
        await budget.add(data.get("usage", {}))
        return data
    raise RuntimeError("gave up after retries")


def first_call(spec, row):
    labels = spec["labels"]
    criteria = {**labels, NONE_ID: NONE_DESC}
    gold_desc = labels.get(row["gold"], "")
    return {
        "model": MODEL,
        "state": {"text": row["text"]},
        "questions": {
            "label": {"type": "choice", "criteria": criteria,
                      "instructions": {"question": "Which label does this text belong to?",
                                       "task": spec["task"], "rules": RULES}},
            "fits_any": {"type": "noul",
                         "instructions": {"question": "Does this text clearly fit at least one of these labels?",
                                          "task": spec["task"], "labels": labels},
                         "criteria": {"true": "at least one label clearly applies",
                                      "false": "no label applies, or the text is empty, contentless, or unclassifiable"}},
            "gold_wrong": {"type": "noul",
                           "instructions": {"question": f"The dataset labels this text as '{row['gold']}' ({gold_desc}). "
                                                        "Is that label wrong for this text under the task guidelines?",
                                            "task": spec["task"], "labels": labels},
                           "criteria": {"true": "the given label is wrong; a careful annotator would pick a different label "
                                                "or say none fits",
                                        "false": "the given label is correct or defensible"}},
        },
    }


def rerank_call(spec, row, probs):
    top = [k for k, _ in sorted(probs.items(), key=lambda kv: -kv[1]) if k != NONE_ID][:RERANK_K]
    criteria = {k: spec["labels"][k] for k in top}
    criteria[NONE_ID] = NONE_DESC
    return top, {
        "model": MODEL,
        "state": {"text": row["text"]},
        "questions": {"label": {"type": "choice", "criteria": criteria,
                                "instructions": {"question": "Exactly one of these labels is the right one for this "
                                                             "text, or none fits. Which one? Read what each "
                                                             "description actually covers, not just its name.",
                                                 "task": spec["task"]}}},
    }


async def ask(client, key, spec, row, budget, sem, stats):
    async with sem:
        if budget.exceeded():
            return None
        t0 = time.perf_counter()
        try:
            data = await post(client, key, first_call(spec, row), budget, stats)
            a = data["answers"]
            rec = {"id": row["id"], "dev": row["idx"] < DEV, "text": row["text"], "gold": row["gold"],
                   "choice": a["label"]["choice"], "confidence": a["label"]["confidence"],
                   "probabilities": a["label"]["probabilities"], "p_gold": a["label"]["probabilities"].get(row["gold"]),
                   "fits_any": a["fits_any"]["noul"], "gold_wrong": a["gold_wrong"]["noul"],
                   "usage": data.get("usage", {}), "model": data.get("model")}
            rec["final"] = rec["choice"]
            if spec.get("rerank") and rec["choice"] != NONE_ID and rec["probabilities"][rec["choice"]] < RERANK_BELOW:
                top, body = rerank_call(spec, row, rec["probabilities"])
                d2 = await post(client, key, body, budget, stats)
                r2 = d2["answers"]["label"]
                rec["rerank"] = {"candidates": top, "choice": r2["choice"], "confidence": r2["confidence"],
                                 "probabilities": r2["probabilities"], "usage": d2.get("usage", {})}
                rec["final"] = r2["choice"]
                rec["final_confidence"] = r2["confidence"]
            rec["latency_ms"] = round((time.perf_counter() - t0) * 1000)
            return rec
        except RuntimeError as e:
            stats["errors"] += 1
            return {"id": row["id"], "error": str(e)}


async def run_dataset(name, spec, limit, concurrency, key, budget):
    rows = load_rows(name, spec, limit)
    out = OUT / f"{name}.jsonl"
    done = set()
    if out.exists():
        for line in out.read_text().splitlines():
            rec = json.loads(line)
            if "error" not in rec:
                done.add(rec["id"])
    todo = [r for r in rows if r["id"] not in done]
    print(f"[{name}] {len(rows)} rows, {len(spec['labels'])} labels, {len(done)} done, {len(todo)} to go", flush=True)
    if not todo:
        return
    stats = {"errors": 0, "retries": 0}
    sem = asyncio.Semaphore(concurrency)
    t0 = time.perf_counter()
    f = out.open("a")
    async with httpx.AsyncClient(http2=True, timeout=30) as client:
        n = 0
        for coro in asyncio.as_completed([ask(client, key, spec, r, budget, sem, stats) for r in todo]):
            rec = await coro
            if rec is None:
                continue
            f.write(json.dumps(rec) + "\n")
            n += 1
            if n % 500 == 0:
                f.flush()
                print(f"[{name}] {n}/{len(todo)} spent ${budget.ledger['cost_usd']:.4f} {stats} "
                      f"{n/(time.perf_counter()-t0):.1f} rows/s", flush=True)
    f.close()
    print(f"[{name}] finished {n} in {time.perf_counter()-t0:.0f}s, spent ${budget.ledger['cost_usd']:.4f} {stats}",
          flush=True)
    if budget.exceeded():
        print(f"BUDGET CAP ${budget.cap} REACHED; stopping", flush=True)


async def main():
    p = argparse.ArgumentParser()
    p.add_argument("--limit", type=int, default=0)
    p.add_argument("--datasets", default=",".join(DATASETS))
    p.add_argument("--concurrency", type=int, default=16)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    OUT.mkdir(exist_ok=True)
    if args.dry_run:
        for name in args.datasets.split(","):
            rows = load_rows(name, DATASETS[name], args.limit)
            missing = {r["gold"] for r in rows} - set(DATASETS[name]["labels"])
            body = first_call(DATASETS[name], rows[0])
            print(f"[{name}] rows={len(rows)} labels={len(DATASETS[name]['labels'])} gold_not_in_labels={sorted(missing)} "
                  f"body_chars={len(json.dumps(body))}")
        return
    key = os.environ["OPENROUTER_API_KEY"]
    budget = Budget(float(os.environ.get("BUDGET_USD", "3.0")))
    print(f"ledger: {budget.ledger} cap ${budget.cap}")
    for name in args.datasets.split(","):
        if budget.exceeded():
            print("budget exhausted before", name)
            break
        await run_dataset(name, DATASETS[name], args.limit, args.concurrency, key, budget)
    print("final ledger:", json.dumps(budget.ledger))


if __name__ == "__main__":
    asyncio.run(main())
