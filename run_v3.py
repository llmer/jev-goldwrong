# /// script
# requires-python = ">=3.11"
# dependencies = ["datasets>=3", "pyarrow", "httpx[http2]"]
# ///
"""v3 label-error hunt: absolute per-label nouls, an explicit ambiguity question, convention nouls, no gold-tuned threshold.

Per row, ONE call with:
  label        choice over the dataset's labels (+ "none" where the spec says absence is real), structured criteria
  fit__<L>     noul per label L, absolute: "does label L apply to this text?"  (small label sets: every label;
               Banking77: only the gold label's noul here, the chosen label's noul in a second call when they differ)
  ambiguous    noul: could a careful annotator defensibly assign more than one label?
  <convention> dataset-specific literal nouls (negation, reversal, definition, ...), combined in code later
Nothing in any question says which label the dataset chose. The gold label enters only as the subject of one
absolute fit question, worded exactly like the others.

Usage: uv run run_v3.py [--limit N] [--datasets a,b] [--concurrency 16] [--dry-run]
Env: OPENROUTER_API_KEY, BUDGET_USD (hard cap, default 4.0)
"""
import argparse, asyncio, importlib, json, os, time
from pathlib import Path

import httpx
from datasets import load_dataset

VERSION = os.environ.get("VERSION", "v3")   # v3 or v4: selects datasets_<VERSION>.py and out_<VERSION>/
_spec = importlib.import_module(f"datasets_{VERSION}")
CONVENTIONS, DATASETS, NONE_DESC, NONE_ID, desc_text = (_spec.CONVENTIONS, _spec.DATASETS, _spec.NONE_DESC,
                                                       _spec.NONE_ID, _spec.desc_text)
FIT_STYLE = getattr(_spec, "FIT_STYLE", "label")   # v4: "scope" leads with the meaning, not the label name

HERE = Path(__file__).parent
OUT = HERE / f"out_{VERSION}"
LEDGER = OUT / "ledger.json"
URL = "https://openrouter.ai/api/alpha/decisions"
MODEL = "typesafe/jev-1.13"
EXPECT_MODEL = "typesafe/jev-1.13-20260917"   # the versioned id the endpoint reported on 2026-09-18; logged per row
ALL_FITS_UPTO = 8                             # ask a fit noul for every label when the set is this small or smaller

RULES = ("Choose the single label a careful human annotator following the dataset guidelines and the option "
         "descriptions would assign. Text may be lowercased, tokenized, or informal. Judge the text itself.")
RULES_NONE = RULES + f" Choose '{NONE_ID}' only when no offered label fits."


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
        if data.get("model") != EXPECT_MODEL:
            stats["model_drift"] += 1
        return data
    raise RuntimeError("gave up after retries")


def fit_question(spec, label):
    meaning = desc_text(spec["labels"][label])
    if FIT_STYLE == "scope":
        return {"type": "noul",
                "instructions": {"question": f"Is this text about the following, so that it belongs in this category? "
                                             f"Category: {meaning}",
                                 "category_name": label, "task": spec["task"]},
                "criteria": {"true": "the text is about what the category describes; a careful annotator could file it there",
                             "false": "the text is not about what the category describes"}}
    return {"type": "noul",
            "instructions": {"question": f"Does the label '{label}' apply to this text?",
                             "label_meaning": meaning, "task": spec["task"]},
            "criteria": {"true": f"a careful annotator following the guidelines could assign '{label}' to this text",
                         "false": f"'{label}' does not fit this text"}}


def label_index(spec):
    """What the ambiguity question shows: names only for big sets, name + one line for small ones."""
    labels = spec["labels"]
    if len(labels) > ALL_FITS_UPTO:
        return sorted(labels)
    return {k: desc_text(v).split(" | ")[0] for k, v in labels.items()}


def first_call(name, spec, row):
    labels = spec["labels"]
    criteria = dict(labels)
    if spec["none"]:
        criteria[NONE_ID] = NONE_DESC
    qs = {"label": {"type": "choice", "criteria": criteria,
                    "instructions": {"question": "Which label does this text belong to?", "task": spec["task"],
                                     "rules": RULES_NONE if spec["none"] else RULES}}}
    fit_labels = sorted(labels) if len(labels) <= ALL_FITS_UPTO else [row["gold"]]
    for lab in fit_labels:
        qs[f"fit__{lab}"] = fit_question(spec, lab)
    qs["ambiguous"] = {"type": "noul",
                       "instructions": {"question": "Could a careful annotator following the task guidelines defensibly "
                                                    "assign more than one of these labels to this text, because it fits "
                                                    "two labels about equally or their definitions overlap for it?",
                                        "task": spec["task"], "labels": label_index(spec)},
                       "criteria": {"true": "two or more labels are each defensible for this text",
                                    "false": "one label clearly fits better than every other"}}
    for qid, text in CONVENTIONS[name].items():
        qs[qid] = {"type": "noul", "instructions": text}
    return {"model": MODEL, "state": {"text": row["text"]}, "questions": qs}


def second_call(spec, row, chosen):
    return {"model": MODEL, "state": {"text": row["text"]}, "questions": {f"fit__{chosen}": fit_question(spec, chosen)}}


async def ask(client, key, name, spec, row, budget, sem, stats):
    async with sem:
        if budget.exceeded():
            return None
        t0 = time.perf_counter()
        try:
            data = await post(client, key, first_call(name, spec, row), budget, stats)
            a = data["answers"]
            lab = a["label"]
            fits = {k[len("fit__"):]: v["noul"] for k, v in a.items() if k.startswith("fit__")}
            rec = {"id": row["id"], "text": row["text"], "gold": row["gold"],
                   "choice": lab["choice"], "confidence": lab["confidence"], "probabilities": lab["probabilities"],
                   "p_gold": lab["probabilities"].get(row["gold"]),
                   "fits": fits, "ambiguous": a["ambiguous"]["noul"],
                   "conventions": {q: a[q]["noul"] for q in CONVENTIONS[name]},
                   "usage": data.get("usage", {}), "model": data.get("model")}
            chosen = lab["choice"]
            if chosen != row["gold"] and chosen != NONE_ID and chosen not in fits:
                d2 = await post(client, key, second_call(spec, row, chosen), budget, stats)
                rec["fits"][chosen] = d2["answers"][f"fit__{chosen}"]["noul"]
                rec["usage2"] = d2.get("usage", {})
            rec["fit_gold"] = rec["fits"].get(row["gold"])
            rec["fit_choice"] = rec["fits"].get(chosen)   # None when choice is none
            rec["latency_ms"] = round((time.perf_counter() - t0) * 1000)
            return rec
        except (RuntimeError, KeyError) as e:
            stats["errors"] += 1
            return {"id": row["id"], "error": repr(e)}


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
    stats = {"errors": 0, "retries": 0, "model_drift": 0}
    sem = asyncio.Semaphore(concurrency)
    t0 = time.perf_counter()
    f = out.open("a")
    async with httpx.AsyncClient(http2=True, timeout=30) as client:
        n = 0
        for coro in asyncio.as_completed([ask(client, key, name, spec, r, budget, sem, stats) for r in todo]):
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
            body = first_call(name, DATASETS[name], rows[0])
            print(f"[{name}] rows={len(rows)} labels={len(DATASETS[name]['labels'])} gold_not_in_labels={sorted(missing)} "
                  f"questions={len(body['questions'])} body_chars={len(json.dumps(body))}")
        return
    key = os.environ["OPENROUTER_API_KEY"]
    budget = Budget(float(os.environ.get("BUDGET_USD", "4.0")))
    print(f"ledger: {budget.ledger} cap ${budget.cap}")
    for name in args.datasets.split(","):
        if budget.exceeded():
            print("budget exhausted before", name)
            break
        await run_dataset(name, DATASETS[name], args.limit, args.concurrency, key, budget)
    print("final ledger:", json.dumps(budget.ledger))


if __name__ == "__main__":
    asyncio.run(main())
