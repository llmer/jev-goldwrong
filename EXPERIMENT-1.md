# Experiment 1: label-error hunt with Jev (v1)

Date: 2026-09-18. Model: `typesafe/jev-1.13` via OpenRouter `POST /api/alpha/decisions`.
Spend: $7.13 for 310,646 calls and 169,680,332 input tokens
($0.042 per million input tokens, output free). Budget cap was $12 of a $25 key; never approached.

## Question

If a cheap, fast, calibrated decision model relabels every row of popular text-classification datasets
using each dataset's own label set, do its confident disagreements point at real label errors?
The finds must be verifiable by a reader from the row text alone, so the claim does not depend on
trusting the model's calibration.

## Method

One request per row, one `choice` question, no other questions:

```json
{"model": "typesafe/jev-1.13",
 "state": {"text": "<row text>"},                       // or {"premise": ..., "hypothesis": ...} for NLI
 "questions": {"label": {"type": "choice",
   "criteria": {"<label id>": "<short description>", ...},   // dataset's own labels, no "none" option
   "instructions": {"task": "<one-paragraph dataset task card>",
                    "rules": "Choose the single label a careful human annotator following the dataset
                              guidelines would assign. Text may be lowercased, tokenized, or informal.
                              Judge the text itself, not what it might imply."}}}}
```

The answer carries `choice`, `probabilities` over every label, and `confidence`. All of it is stored.

Flag rule (fixed in advance, not tuned): P(gold label) < 0.2 and P(Jev's choice) > 0.7.

Review: for each dataset a random sample of flags (100 for the first five test splits, 50 for the rest,
all flags when fewer) was judged by a Claude Code subagent acting as a strict annotator with the
dataset's guidelines and conventions in its prompt. Verdicts: `gold_wrong`, `jev_wrong`, `ambiguous`,
plus a corrected label and a one-sentence reason. Precision = gold_wrong / reviewed, Wilson 95% CI.
Estimated errors = precision x flag count.

Runtime: httpx async, concurrency 16, retries on 429/5xx, resumable JSONL output, cumulative spend
ledger with a hard cap. Throughput 55-73 rows/s. 310,646 calls; roughly 0.1% needed a retry; 17 rows
failed twice with Cloudflare 520 and were redone.

Datasets (20, 310,635 rows): AG News test+train, Banking77 (mteb mirror) test+train, TREC coarse
(SetFit mirror) test+train, SST-2 validation+train, dair-ai/emotion test+train, TweetEval sentiment,
hate, irony, offensive, emotion (test), SST-5 test, Rotten Tomatoes test, IMDB test (8k sample, 3000
chars), 20 Newsgroups test (2500 chars), DBpedia-14 test (15k sample), Yelp polarity test (8k sample),
SMS Spam, Enron spam test, MNLI validation_matched, RTE validation.

## Results

| dataset | rows | agree w/ gold | agree @conf>=.9 | coverage @.9 | ECE | flagged | reviewed | gold wrong | jev wrong | ambiguous | precision | est. gold errors |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| ag_news | 7600 | 0.892 | 0.941 | 0.84 | 0.061 | 533 | 100 | 46 | 0 | 54 | 0.46 (0.37-0.56) | ~245 (3.2% of rows) |
| ag_news_train | 120000 | 0.890 | 0.942 | 0.84 | 0.064 | 8321 | 50 | 25 | 2 | 23 | 0.50 (0.37-0.63) | ~4160 (3.5% of rows) |
| banking77 | 3076 | 0.796 | 0.922 | 0.68 | 0.092 | 296 | 100 | 45 | 7 | 48 | 0.45 (0.36-0.55) | ~133 (4.3% of rows) |
| banking77_train | 9993 | 0.775 | 0.910 | 0.66 | 0.103 | 1091 | 50 | 25 | 8 | 17 | 0.50 (0.37-0.63) | ~546 (5.5% of rows) |
| dbpedia | 15000 | 0.986 | 0.996 | 0.97 | 0.004 | 103 | 50 | 31 | 7 | 12 | 0.62 (0.48-0.74) | ~64 (0.4% of rows) |
| emotion | 2000 | 0.587 | 0.720 | 0.57 | 0.276 | 515 | 100 | 70 | 1 | 29 | 0.70 (0.60-0.78) | ~360 (18.0% of rows) |
| emotion_train | 16000 | 0.597 | 0.728 | 0.57 | 0.267 | 4157 | 50 | 39 | 1 | 10 | 0.78 (0.65-0.87) | ~3242 (20.3% of rows) |
| enron_spam | 2000 | 0.976 | 0.995 | 0.85 | 0.011 | 14 | 14 | 0 | 5 | 9 | 0.00 (0.00-0.22) | ~0 (0.0% of rows) |
| imdb | 8000 | 0.965 | 0.989 | 0.90 | 0.012 | 149 | 50 | 17 | 4 | 29 | 0.34 (0.22-0.48) | ~51 (0.6% of rows) |
| mnli | 9815 | 0.864 | 0.956 | 0.65 | 0.041 | 587 | 50 | 32 | 1 | 17 | 0.64 (0.50-0.76) | ~376 (3.8% of rows) |
| newsgroups | 7532 | 0.713 | 0.914 | 0.56 | 0.115 | 746 | 50 | 2 | 12 | 36 | 0.04 (0.01-0.13) | ~30 (0.4% of rows) |
| rotten_tomatoes | 1066 | 0.926 | 0.974 | 0.78 | 0.024 | 43 | 43 | 15 | 4 | 24 | 0.35 (0.22-0.50) | ~15 (1.4% of rows) |
| rte | 277 | 0.906 | 0.964 | 0.70 | 0.034 | 14 | 14 | 4 | 6 | 4 | 0.29 (0.12-0.55) | ~4 (1.4% of rows) |
| sms_spam | 5574 | 0.966 | 0.993 | 0.82 | 0.007 | 73 | 50 | 8 | 35 | 7 | 0.16 (0.08-0.29) | ~12 (0.2% of rows) |
| sst2 | 872 | 0.961 | 0.981 | 0.83 | 0.016 | 17 | 17 | 12 | 1 | 4 | 0.71 (0.47-0.87) | ~12 (1.4% of rows) |
| sst2_train | 67349 | 0.932 | 0.987 | 0.71 | 0.005 | 1571 | 50 | 14 | 9 | 27 | 0.28 (0.17-0.42) | ~440 (0.7% of rows) |
| sst5 | 2210 | 0.584 | 0.716 | 0.26 | 0.191 | 453 | 50 | 16 | 1 | 33 | 0.32 (0.21-0.46) | ~145 (6.6% of rows) |
| trec | 500 | 0.944 | 0.972 | 0.86 | 0.023 | 16 | 16 | 4 | 6 | 6 | 0.25 (0.10-0.49) | ~4 (0.8% of rows) |
| trec_train | 5452 | 0.901 | 0.960 | 0.78 | 0.034 | 275 | 50 | 9 | 29 | 12 | 0.18 (0.10-0.31) | ~50 (0.9% of rows) |
| tweet_emotion | 1421 | 0.837 | 0.946 | 0.66 | 0.060 | 109 | 50 | 30 | 2 | 18 | 0.60 (0.46-0.72) | ~65 (4.6% of rows) |
| tweet_hate | 2970 | 0.765 | 0.929 | 0.27 | 0.054 | 223 | 50 | 28 | 15 | 7 | 0.56 (0.42-0.69) | ~125 (4.2% of rows) |
| tweet_irony | 784 | 0.870 | 0.991 | 0.44 | 0.012 | 25 | 25 | 12 | 7 | 6 | 0.48 (0.30-0.67) | ~12 (1.5% of rows) |
| tweet_offensive | 860 | 0.816 | 0.938 | 0.60 | 0.090 | 74 | 50 | 30 | 9 | 11 | 0.60 (0.46-0.72) | ~44 (5.1% of rows) |
| tweet_sentiment | 12284 | 0.681 | 0.804 | 0.48 | 0.166 | 2180 | 50 | 20 | 14 | 16 | 0.40 (0.28-0.54) | ~872 (7.1% of rows) |
| yelp | 8000 | 0.985 | 0.996 | 0.94 | 0.001 | 52 | 50 | 18 | 3 | 29 | 0.36 (0.24-0.50) | ~19 (0.2% of rows) |
| **total** | 310635 | | | | | 21637 | 1229 | 552 | 189 | 488 | 0.45 | ~11026 (3.5%) |

Rows judged: 310,635. Flags: 21,637. Flags reviewed: 1229. Estimated true gold errors among flags: ~11,026. Jev was the wrong party in 189 of 1229 reviewed flags.


## Where the flags land

- Mostly real label errors (precision >= 0.5): emotion_train (0.78), sst2 (0.71), emotion (0.70), mnli (0.64), dbpedia (0.62), tweet_emotion (0.60), tweet_offensive (0.60), tweet_hate (0.56), ag_news_train (0.50), banking77_train (0.50)
- Mixed, mostly ambiguous or convention (0.25-0.5): tweet_irony (0.48), ag_news (0.46), banking77 (0.45), tweet_sentiment (0.40), yelp (0.36), rotten_tomatoes (0.35), imdb (0.34), sst5 (0.32), rte (0.29), sst2_train (0.28), trec (0.25)
- Mostly Jev missing dataset conventions or ground truth by construction (< 0.25): trec_train (0.18), sms_spam (0.16), newsgroups (0.04), enron_spam (0.00)

Flag rule: P(gold) < 0.2 and P(Jev choice) > 0.7. Reviewer: Claude Code, one strict annotator per dataset, verdicts gold_wrong / jev_wrong / ambiguous. Precision = gold_wrong / reviewed, Wilson 95% CI.


## Findings

- Across 1,229 reviewed flags, 45% were real gold errors, 40% ambiguous or dataset-convention cases,
  15% Jev errors. Extrapolated: about 11,000 label errors in 310k rows (3.5%).
- Datasets whose flags are mostly real errors: Emotion (about 20% of rows mislabeled; hashtag-derived
  labels latch onto one keyword and miss negation), MNLI (crowd treats "probably true" as entailment),
  DBpedia (ontology types: a racing yacht typed Building, "Politics of Yemen" typed Company), TweetEval
  hate/offensive/emotion, AG News (sports and market stories filed under World), Banking77, SST-2.
- Datasets where Jev was the problem: TREC train (ignores TREC conventions such as planets = LOC),
  SMS spam (calls jokes and chain forwards spam), Newsgroups and Enron (gold is where the post was
  filed, so disagreement is thread drift, not error).
- Calibration: agreement with gold at confidence >= 0.9 was 0.91-0.996 on 17 of 20 datasets; ECE
  under 0.1 on 17 of 20. The exceptions are the datasets whose gold is 15-20% wrong.

## Departures from the TypeSafe cookbooks (fixed in v2)

Compared against docs.typesafe.ai cookbooks (classification_using_confidence, hierarchical_classification,
skill_suggestion, sde_cascade, parallel_questions, consistency_choice, date/pre-parsed extraction):

1. Bare or one-phrase option descriptions instead of rich descriptions with examples and conventions.
   Most Jev errors trace to this.
2. No "none / fits no label" option, so unclassifiable rows were forced into a label.
3. Flag threshold fixed a priori on probabilities, not chosen on a dev split; `confidence` unused for routing;
   no coarse-level fallback for the 77-way set.
4. No uncertain band from Jev's own distribution; "ambiguous" came from reviewers after the fact.
5. One question per call; no companion noul questions ("does the text fit any label?", "is the given
   gold label wrong?"), which would have cost almost nothing extra.
6. No two-stage rerank for near-duplicate intents.

## Limitations

- Reviewers are Claude, not humans. Sample sizes give roughly +/- 13 points on per-dataset precision.
- Extrapolation assumes the random flag sample represents all flags.
- Newsgroups and Enron gold is ground truth by construction; their flag counts are not errors.
- OpenRouter rate limits were never reached at concurrency 16; the ceiling is unknown.

## Files

`v1/run.py` (runner), `v1/analyze.py` (scorecard + flags), `v1/sample_flags.py`, `v1/report.py`,
`v1/chain.sh`; `v1/out/<dataset>.jsonl` raw answers with full distributions (220 MB, not for git),
`v1/out/flags.jsonl`, `v1/out/summary.json`, `v1/out/report.md`; `v1/review/<dataset>.jsonl` sampled
flags and `v1/review/<dataset>.verdicts.jsonl` reviewer verdicts with reasons.
