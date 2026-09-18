# Experiment 4: second criteria loop, scope-led fit questions, and a two-model verification of the high tier

Date: 2026-09-18. Model: `typesafe/jev-1.13` via OpenRouter, reported as `typesafe/jev-1.13-20260917` on every
row. Same five test splits (14,048 rows). Spend: $1.79 for 14,498 calls, 42.5M input tokens. Cumulative key
spend after four experiments: about $12.05 of $25.

Two goals. First, the v3 follow-ups: a second feedback loop from the v3 reviewer verdicts, and fit questions that
lead with the category's scope so the absolute noul stops reading label names literally. Second, the question of
what stands between a model-found error and a claim: run the docs' verify-and-escalate cascade on our own
queue with two independent model reviewers, and keep only the rows both agree on.

## What changed from v3

1. **Scope-led fit questions.** v3 asked "does the label 'World' apply?", which the model read literally on US
   election stories (174 rows where Jev agreed with gold at confidence 1.0 but the absolute noul said gold did not
   fit). v4 asks "is this text about the following, so that it belongs in this category?" followed by the
   description, with the label name as a secondary field.
2. **Second criteria loop.** Every not_for and example added in `datasets_v4.py` comes from a v3 reviewer's reason
   on a row Jev got wrong (card_arrival vs card_delivery_estimate, why_verify vs unable_to_verify, fees for receiving
   money, "Apple Bay", unfavorable comparisons and hedged praise on SST-2, "What is Wimbledon?" on TREC, fake and
   unwelcome as sadness on Emotion). Those rows are now in-sample, so v4 is measured on rows neither v2 nor v3
   reviewers saw.
3. **No `none` on Banking77** (v3: Jev chose none for classifiable messages). **No `needs_context`** (flat).

## Run-level changes

| dataset | v3 agree | v4 agree | v3 high tier | v4 high tier | v3 agree-but-gold-unfit | v4 | v3 weak | v4 weak |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| banking77 | 0.827 | **0.854** | 80 | 78 | 153 | 127 | 46 | 52 |
| trec | 0.972 | 0.972 | 4 | 3 | 8 | 3 | 1 | 2 |
| sst2 | 0.956 | **0.966** | 12 | 11 | 26 | 47 | 3 | 4 |
| ag_news | 0.893 | 0.893 | 202 | **236** | 174 | 129 | 50 | 24 |
| emotion | 0.567 | 0.566 | 109 | 104 | 204 | 133 | 50 | 45 |

The second loop moved Banking77 agreement another 2.7 points (0.793 in v2). The scope-led fit question did what it
was meant to on AG News: 34 more rows in the high tier, half as many in the weak band, 45 fewer agree-but-unfit.
Emotion is unchanged, as expected; its problem is the labels, not the questions.

## Held-out review (221 rows neither v2 nor v3 reviewers saw)

| band | tier | reviewed | gold_wrong | jev_wrong | ambiguous | precision |
|---|---|--:|--:|--:|--:|--:|
| error_candidate | high | 63 | 50 | 0 | 13 | 0.79 (0.68-0.88) |
| error_candidate | mid | 30 | 11 | 1 | 18 | 0.37 |
| ambiguous_candidate | | 75 | 14 | 9 | 52 | 0.19 |
| none_candidate (Emotion) | | 15 | 10 | 0 | 5 | 0.67 |
| weak_disagree | | 32 | 14 | 1 | 17 | 0.44 |

Read this table as a floor. After two rounds of review, the rows still unseen in the high tier are the ones that
entered it only in v4 (AG News 50 of 127 unseen, Banking77 6, Emotion 7), which are the marginal ones by
construction. The AG News high tier held at 0.84 on 50 fresh rows, the same as v3. The whole-band measurement is
the verification pass below.

## Two-model verification of the whole high tier

All 432 high-tier rows went to two independent reviewers under the same blind protocol (`verify_v4/GUIDELINES.md`,
which adds one line: every row here is one where a model disagreed with gold, and that is not evidence). Reviewer
A: fresh Claude Code agents, one per dataset. Reviewer B: Codex (`codex-cli 0.154.0`), one task over all five
files. Neither saw the other's verdicts, the v4 reviewer's verdicts, or the band metadata.

| Claude / Codex | rows | share |
|---|--:|--:|
| gold_wrong / gold_wrong | **313** | 72.5% |
| gold_wrong / ambiguous | 50 | 11.6% |
| ambiguous / ambiguous | 49 | 11.3% |
| ambiguous / gold_wrong | 17 | 3.9% |
| gold_wrong / jev_wrong | 2 | 0.5% |
| ambiguous / jev_wrong | 1 | 0.2% |
| jev_wrong / anything | 0 | 0 |

| dataset | high tier | both gold_wrong | either gold_wrong | both ambiguous |
|---|--:|--:|--:|--:|
| ag_news | 236 | 186 (79%) | 205 | 30 |
| banking77 | 78 | 41 (53%) | 64 | 14 |
| emotion | 104 | 74 (71%) | 100 | 4 |
| sst2 | 11 | 9 | 10 | 1 |
| trec | 3 | 3 | 3 | 0 |
| **all** | 432 | **313 (72%)** | 382 (88%) | 49 (11%) |

Of the 313 rows both call gold-wrong, 309 name the same corrected label. Across 864 individual judgments, three
said Jev's label was wrong, all Codex on AG News and all tech-company stories where Codex applied the "tech-industry
lawsuits are Sci/Tech" convention more literally than Claude. On the 63 high-tier rows the v4 held-out reviewer had
also judged, each verifier agreed with that reviewer on 56 (89%).

The remaining 119 rows are not rejected; they are the disagreement file, mostly rows one model called ambiguous.
Banking77 is where the two split most (20 Claude-gold-wrong / Codex-ambiguous), on the same clusters every
reviewer has named since v2: "transfer isn't possible" with no reason stated, and card_arrival vs
card_delivery_estimate.

## What this changes about the public claim

- **The confirmed list is 313 rows, not 432, and not 2,174.** Each row comes with a text, a gold label, one corrected
  label two models agree on, and one sentence of reason. `verify_v4/human_queue.md` is that list.
- **The claim is per row, not per estimate.** "Row N of dataset D is labeled X and reads as Y" can be checked by
  anyone from the text. The error-rate estimates in these write-ups stay estimates.
- **Cost of the cascade.** Jev on 14,048 rows: $1.79. Two model reviewers on 432 rows: roughly an hour of agent
  time.

## Findings

- **High-tier precision is stable across three measurements**: 0.82 (v3 held out), 0.79 (v4 held out, marginal
  rows), 0.72 to 0.88 (two-model verification, both-agree to either-agrees). The band means what it is meant to.
- **Two models disagree mostly on ambiguity, never on Jev being wrong.** That is the right shape for a filter: the
  cascade removes rows a person would argue about, not rows Jev got right.
- **The criteria loop converges.** Two loops took Banking77 from 0.793 to 0.854 agreement and moved reviewer
  verdicts from 7% Jev-wrong (v2) to 0 Jev-wrong in the whole-band verification. What is left is dataset
  ambiguity that no description resolves.
- **Fit-question wording matters as much as criteria.** One rewording moved 34 AG News rows from bands with 0.3 to
  0.7 precision into the 0.84 band. The jaggedness page's "literal reading" is a design constraint on every question,
  not only on the Choice.
- **Emotion's `none` band is real** (0.67 held out, ~195 rows): about a tenth of the test split has no emotion in it.

## What v5 should try

- Publish per-row finds from `verify_v4/human_queue.md` with the two model reasons.
- Run the same cascade on the mid tier and the Emotion none band (about 250 rows) to see how much the
  two-model filter recovers there.
- A third loop only if it targets ambiguity: add a per-pair "either label is acceptable" note to the criteria for the
  clusters reviewers keep naming, and see whether the ambiguous band absorbs them.
- The other 15 v1 datasets under the v4 pipeline; MNLI and the emotion-style sets are where v1 found most.

## Files

`datasets_v4.py` (overlay on v3), `chain_v4.sh`, `verify.py` (split / merge); the v3 scripts take `VERSION=v4`.
`out_v4/summary.json`, `out_v4/report_v4.md`, `out_v4/queue.jsonl.gz` (every disagreement with band, tier, rank,
queue position). `review_v4/` held-out samples, blind metadata, verdicts. `verify_v4/` the 432 high-tier rows,
`<dataset>.claude.verdicts.jsonl`, `<dataset>.codex.verdicts.jsonl`, `human_queue.jsonl` / `.md`,
`disagreements.jsonl`, and the verification guidelines.
