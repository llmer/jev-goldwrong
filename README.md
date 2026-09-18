# goldwrong

Hunting label errors in popular text-classification datasets with [TypeSafe's Jev](https://docs.typesafe.ai/introduction),
a fast, cheap decision model that returns a full probability distribution over labels you define at request time.

Relabel every row with the dataset's own label set. Where Jev confidently disagrees with the gold label, a reviewer
checks the row. The finds are single rows a reader can verify from the text alone, so the claim does not depend on
trusting the model's calibration.

Two experiments so far, about $8.60 of model spend in total:

| | rows | datasets | Jev calls | spend | flags reviewed | flag precision |
|---|--:|--:|--:|--:|--:|--:|
| [Experiment 1](EXPERIMENT-1.md) | 310,635 | 20 | 310,646 | $7.13 | 1,229 | 0.45 |
| [Experiment 2](EXPERIMENT-2.md) | 14,048 | 5 | 14,866 | $1.45 | 330 + 91 | 0.65 |

Experiment 1 estimates about 11,000 label errors (3.5% of rows) across 20 datasets. Experiment 2 reworks the pipeline
around the [TypeSafe cookbooks](https://docs.typesafe.ai/cookbooks/classification_using_confidence) (rich option
descriptions, a `none` option, companion yes/no questions in the same call, a dev-split confidence threshold) and
raises flag precision from 0.53 to 0.65 on the same five datasets, with two negative results kept as ablations.

Headline finds: about 20% of `dair-ai/emotion` is mislabeled (hashtag labels miss negation), 32 of 50 flagged MNLI
pairs are crowd-label errors, DBpedia-14 types a racing yacht as `Building`, AG News files cricket under `World`,
Banking77 labels "Someone stole my cards!" as `lost_or_stolen_phone`. Verified examples with reasons are in each
experiment's report.

## Layout

```
EXPERIMENT-1.md, EXPERIMENT-2.md   write-ups
run_v2.py, datasets_v2.py           v2 runner (three questions per call) and dataset specs with rich descriptions
analyze_v2.py, report_v2.py         v2 scorecard, bands, noul agreement, v1 comparison
run.py, analyze.py, report.py       v1 runner and analysis (also frozen under v1/)
sample_flags.py                     stratified flag samples for review
chain.sh, chain_v2.sh               detached full runs with a spend cap
out/                                v2 results: summary.json, report_v2.md, flags.jsonl.gz, noul_only.jsonl.gz
review/                             v2 reviewer samples and verdicts (JSONL, one reason per row)
v1/out/, v1/review/                 the same for experiment 1
```

Raw per-row answers (`out/*.jsonl`, hundreds of MB) are not committed; the runners regenerate them and resume from
whatever exists.

## Run it

```bash
cp .env.example .env    # add an OpenRouter key
uv run run_v2.py --dry-run                      # load datasets, print label sets, no API calls
BUDGET_USD=0.10 uv run run_v2.py --limit 10     # 10 rows per dataset
./chain_v2.sh                                   # full run, detached-friendly, $3 cap
python3 analyze_v2.py && python3 report_v2.py
```

Requests go to OpenRouter's `POST /api/alpha/decisions` with model `typesafe/jev-1.13` ($0.042 per million input
tokens, output free). Each call carries `state` (the row) and typed `questions`; the answer carries `choice`,
`probabilities`, `confidence`, and `noul` values. Reviews were done by Claude Code subagents acting as strict
annotators with each dataset's guidelines; a human pass is still needed before any public claim.
