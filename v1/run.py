# /// script
# requires-python = ">=3.11"
# dependencies = ["datasets>=3", "pyarrow", "httpx[http2]"]
# ///
"""Label-error hunt pilot: ask Jev (via OpenRouter) to relabel every row; keep the full distribution.

Usage: uv run run.py [--limit N] [--datasets a,b] [--concurrency 8]
Env:   OPENROUTER_API_KEY (from .env.jev), BUDGET_USD (hard cap, default 3.0)
Output: out/<dataset>.jsonl (resumable), out/ledger.json (cumulative spend)
"""
import argparse, asyncio, json, os, sys, time
from pathlib import Path

import httpx
from datasets import load_dataset

HERE = Path(__file__).parent
OUT = HERE / "out"
LEDGER = OUT / "ledger.json"
URL = "https://openrouter.ai/api/alpha/decisions"
MODEL = "typesafe/jev-1.13"

RULES = ("Choose the single label a careful human annotator following the dataset guidelines would assign. "
         "Text may be lowercased, tokenized, or informal. Judge the text itself, not what it might imply.")

DATASETS = {
    "banking77": dict(
        hf="mteb/banking77", config=None, split="test", text="text", label="label_text",
        task="Banking customer-support intent classification. Each message is a single customer query to a "
             "retail bank; pick the one intent it expresses.",
        labels=None,  # discovered from data; description = name with underscores replaced
    ),
    "trec": dict(
        hf="SetFit/TREC-QC", config=None, split="test", text="text", label="label_coarse_text",
        task="TREC question classification (coarse). Classify each English question by the TYPE of answer it "
             "expects.",
        gold_map={"description and abstract concepts": "DESC", "numeric values": "NUM", "entities": "ENTY",
                  "locations": "LOC", "human beings": "HUM", "abbreviation": "ABBR"},
        labels={"ABBR": "abbreviation or expansion of an abbreviation", "ENTY": "an entity: thing, animal, "
                "color, product, event, language, etc.", "DESC": "a description, definition, reason, or manner",
                "HUM": "a human: person, group, organization, or title", "LOC": "a location: city, country, "
                "mountain, or other place", "NUM": "a number: count, date, distance, money, percent, period, etc."},
    ),
    "sst2": dict(
        hf="stanfordnlp/sst2", config=None, split="validation", text="sentence", label="label",
        task="Stanford Sentiment Treebank binary sentiment. Each item is a movie-review sentence or phrase; "
             "label the sentiment the writer expresses about the film.",
        labels={"negative": "negative sentiment toward the film", "positive": "positive sentiment toward the film"},
    ),
    "ag_news": dict(
        hf="fancyzhx/ag_news", config=None, split="test", text="text", label="label",
        task="AG News topic classification. Each item is a news headline plus lead; pick the section it belongs to.",
        labels={"World": "world news, politics, conflict, international affairs", "Sports": "sports",
                "Business": "business, markets, economy, companies, finance",
                "Sci/Tech": "science and technology, including tech companies and products"},
    ),
    "emotion": dict(
        hf="dair-ai/emotion", config="split", split="test", text="text", label="label",
        task="Twitter emotion classification (dair-ai/emotion). Each item is an English tweet; pick the single "
             "dominant emotion the author expresses.",
        labels={"sadness": "sadness", "joy": "joy, happiness, contentment", "love": "love, affection, caring",
                "anger": "anger, annoyance, hate", "fear": "fear, anxiety, nervousness", "surprise": "surprise"},
    ),
}

TWEET = "TweetEval {name}. Each item is an English tweet (user mentions replaced by @user)."
DATASETS.update({
    "tweet_sentiment": dict(hf="cardiffnlp/tweet_eval", config="sentiment", split="test", text="text", label="label",
        task=TWEET.format(name="sentiment") + " Label the overall sentiment of the tweet.",
        labels={"negative": "negative", "neutral": "neutral or mixed, no clear sentiment", "positive": "positive"}),
    "tweet_hate": dict(hf="cardiffnlp/tweet_eval", config="hate", split="test", text="text", label="label",
        task=TWEET.format(name="hate speech detection (SemEval-2019 HatEval)") + " Hate speech here means "
             "hateful content targeting immigrants or women. Other offensive or aggressive content is non-hate.",
        labels={"non-hate": "not hate speech against immigrants or women", "hate": "hate speech against immigrants or women"}),
    "tweet_irony": dict(hf="cardiffnlp/tweet_eval", config="irony", split="test", text="text", label="label",
        task=TWEET.format(name="irony detection (SemEval-2018)") + " Decide whether the tweet is ironic (says the "
             "opposite of what is meant, or a situational irony).",
        labels={"non_irony": "not ironic", "irony": "ironic"}),
    "tweet_offensive": dict(hf="cardiffnlp/tweet_eval", config="offensive", split="test", text="text", label="label",
        task=TWEET.format(name="offensive language (OffensEval 2019)") + " Offensive means it contains insults, threats, "
             "profanity directed at someone, or targeted abuse.",
        labels={"non-offensive": "not offensive", "offensive": "offensive"}),
    "tweet_emotion": dict(hf="cardiffnlp/tweet_eval", config="emotion", split="test", text="text", label="label",
        task=TWEET.format(name="emotion (SemEval-2018)") + " Pick the dominant emotion.",
        labels={"anger": "anger", "joy": "joy", "optimism": "optimism, hope", "sadness": "sadness"}),
    "sst5": dict(hf="SetFit/sst5", config=None, split="test", text="text", label="label_text",
        task="Stanford Sentiment Treebank five-way. Each item is a movie-review sentence; rate the reviewer's "
             "sentiment toward the film.",
        labels={"very negative": "very negative", "negative": "negative", "neutral": "neutral",
                "positive": "positive", "very positive": "very positive"}),
    "rotten_tomatoes": dict(hf="cornell-movie-review-data/rotten_tomatoes", config=None, split="test", text="text",
        label="label", task="Rotten Tomatoes movie-review sentence polarity. Label the reviewer's sentiment.",
        labels={"neg": "negative", "pos": "positive"}),
    "imdb": dict(hf="stanfordnlp/imdb", config="plain_text", split="test", text="text", label="label", max_chars=3000,
        sample=8000, task="IMDB movie review polarity. Each item is a full user review; label its overall verdict.",
        labels={"neg": "negative review (1-4 stars)", "pos": "positive review (7-10 stars)"}),
    "newsgroups": dict(hf="SetFit/20_newsgroups", config=None, split="test", text="text", label="label_text",
        max_chars=2500, task="20 Newsgroups. Each item is a Usenet post body (headers removed); pick the newsgroup "
        "it was posted to.", labels=None),
    "dbpedia": dict(hf="fancyzhx/dbpedia_14", config="dbpedia_14", split="test", fields=["title", "content"],
        label="label", sample=15000, task="DBpedia ontology classification. Each item is a Wikipedia article title "
        "and abstract; pick the entity type.", labels=None),
    "yelp": dict(hf="fancyzhx/yelp_polarity", config="plain_text", split="test", text="text", label="label",
        max_chars=2500, sample=8000, task="Yelp review polarity. Label the review's overall verdict.",
        labels={"1": "negative review (1-2 stars)", "2": "positive review (4-5 stars)"}),
    "sms_spam": dict(hf="ucirvine/sms_spam", config="plain_text", split="train", text="sms", label="label",
        task="SMS spam collection. Label each text message.", labels={"ham": "legitimate personal message", "spam": "spam"}),
    "enron_spam": dict(hf="SetFit/enron_spam", config=None, split="test", fields=["subject", "text"], label="label_text",
        max_chars=2500, task="Enron email spam. Label each email.", labels={"ham": "legitimate email", "spam": "spam"}),
    "mnli": dict(hf="nyu-mll/glue", config="mnli", split="validation_matched", fields=["premise", "hypothesis"],
        label="label", task="MultiNLI natural language inference. Given the premise, does the hypothesis follow?",
        labels={"entailment": "the hypothesis is definitely true given the premise",
                "neutral": "the hypothesis might be true; the premise does not decide it",
                "contradiction": "the hypothesis is definitely false given the premise"}),
    "rte": dict(hf="nyu-mll/glue", config="rte", split="validation", fields=["sentence1", "sentence2"], label="label",
        task="RTE textual entailment. Does sentence2 follow from sentence1?",
        labels={"entailment": "sentence2 follows from sentence1", "not_entailment": "sentence2 does not follow"}),
})

for _base, _split in [("banking77", "train"), ("trec", "train"), ("sst2", "train"), ("ag_news", "train"),
                      ("emotion", "train")]:
    DATASETS[f"{_base}_{_split}"] = {**DATASETS[_base], "split": _split}


def load_rows(name, spec, limit):
    ds = load_dataset(spec["hf"], spec["config"], split=spec["split"]) if spec["config"] else \
        load_dataset(spec["hf"], split=spec["split"])
    names = ds.features[spec["label"]].names if hasattr(ds.features[spec["label"]], "names") else None
    rows = []
    mc = spec.get("max_chars")
    for i, r in enumerate(ds):
        gold = r[spec["label"]]
        gold = names[gold] if names else gold
        gold = spec.get("gold_map", {}).get(gold, gold)
        if "fields" in spec:
            text = {k: (str(r[k])[:mc] if mc else r[k]) for k in spec["fields"]}
        else:
            text = r[spec["text"]][:mc] if mc else r[spec["text"]]
        rows.append({"id": f"{name}:{spec['split']}:{i}", "text": text, "gold": gold})
    if spec.get("sample") and len(rows) > spec["sample"]:
        import random
        random.Random(7).shuffle(rows)
        rows = rows[:spec["sample"]]
    labels = spec["labels"] or {g: g.replace("_", " ") for g in sorted({r["gold"] for r in rows})}
    if names and not spec["labels"]:
        labels = {n: n for n in names}
    return rows[:limit] if limit else rows, labels


def load_ledger():
    return json.loads(LEDGER.read_text()) if LEDGER.exists() else {"cost_usd": 0.0, "calls": 0, "input_tokens": 0}


class Budget:
    def __init__(self, cap):
        self.ledger = load_ledger()
        self.cap = cap
        self.lock = asyncio.Lock()

    def exceeded(self):
        return self.ledger["cost_usd"] >= self.cap

    async def add(self, usage):
        async with self.lock:
            self.ledger["cost_usd"] += usage.get("cost", 0.0)
            self.ledger["calls"] += 1
            self.ledger["input_tokens"] += usage.get("input_tokens", 0)
            LEDGER.write_text(json.dumps(self.ledger))


async def ask(client, key, spec, labels, row, budget, sem, stats):
    body = {
        "model": MODEL,
        "state": row["text"] if isinstance(row["text"], dict) else {"text": row["text"]},
        "questions": {"label": {"type": "choice", "criteria": labels,
                                "instructions": {"task": spec["task"], "rules": RULES}}},
    }
    async with sem:
        if budget.exceeded():
            return None
        for attempt in range(5):
            t0 = time.perf_counter()
            try:
                r = await client.post(URL, json=body, headers={"Authorization": f"Bearer {key}"})
            except httpx.HTTPError as e:
                stats["errors"] += 1
                await asyncio.sleep(0.5 * 2**attempt)
                continue
            if r.status_code in (429, 500, 502, 503, 504) or 520 <= r.status_code <= 529:
                stats["retries"] += 1
                await asyncio.sleep(0.5 * 2**attempt)
                continue
            if r.is_error:
                stats["errors"] += 1
                return {"id": row["id"], "error": f"HTTP {r.status_code}: {r.text[:200]}"}
            data = r.json()
            await budget.add(data.get("usage", {}))
            a = data["answers"]["label"]
            return {"id": row["id"], "text": row["text"], "gold": row["gold"], "choice": a["choice"],
                    "confidence": a["confidence"], "probabilities": a["probabilities"],
                    "p_gold": a["probabilities"].get(row["gold"]), "usage": data.get("usage", {}),
                    "latency_ms": round((time.perf_counter() - t0) * 1000), "model": data.get("model")}
        stats["errors"] += 1
        return {"id": row["id"], "error": "gave up after retries"}


async def run_dataset(name, spec, limit, concurrency, key, budget):
    rows, labels = load_rows(name, spec, limit)
    out = OUT / f"{name}.jsonl"
    done = set()
    if out.exists():
        for line in out.read_text().splitlines():
            rec = json.loads(line)
            if "error" not in rec:
                done.add(rec["id"])
    todo = [r for r in rows if r["id"] not in done]
    print(f"[{name}] {len(rows)} rows, {len(labels)} labels, {len(done)} done, {len(todo)} to go", flush=True)
    if not todo:
        return
    stats = {"errors": 0, "retries": 0}
    sem = asyncio.Semaphore(concurrency)
    t0 = time.perf_counter()
    f = out.open("a")
    async with httpx.AsyncClient(http2=True, timeout=30) as client:
        tasks = [ask(client, key, spec, labels, r, budget, sem, stats) for r in todo]
        n = 0
        for coro in asyncio.as_completed(tasks):
            rec = await coro
            if rec is None:
                continue
            f.write(json.dumps(rec) + "\n")
            n += 1
            if n % 500 == 0:
                f.flush()
                print(f"[{name}] {n}/{len(todo)} spent ${budget.ledger['cost_usd']:.4f} "
                      f"{stats} {n/(time.perf_counter()-t0):.1f} rows/s", flush=True)
    f.close()
    print(f"[{name}] finished {n} in {time.perf_counter()-t0:.0f}s, spent ${budget.ledger['cost_usd']:.4f} {stats}",
          flush=True)
    if budget.exceeded():
        print(f"BUDGET CAP ${budget.cap} REACHED; stopping", flush=True)


async def main():
    p = argparse.ArgumentParser()
    p.add_argument("--limit", type=int, default=0)
    p.add_argument("--datasets", default=",".join(DATASETS))
    p.add_argument("--concurrency", type=int, default=8)
    p.add_argument("--dry-run", action="store_true", help="load datasets, print label sets and a sample; no API calls")
    args = p.parse_args()
    if args.dry_run:
        for name in args.datasets.split(","):
            rows, labels = load_rows(name, DATASETS[name], args.limit)
            golds = {r["gold"] for r in rows}
            missing = golds - set(labels)
            print(f"[{name}] rows={len(rows)} labels={len(labels)} gold_not_in_labels={sorted(missing)[:5]} "
                  f"sample_gold={rows[0]['gold']!r} sample_text={json.dumps(rows[0]['text'])[:160]}")
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
