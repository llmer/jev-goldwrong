# Experiment 3: absolute fit questions, an ambiguity question, structured criteria, fixed bands

Date: 2026-09-18. Model: `typesafe/jev-1.13` via OpenRouter, reported by the API as `typesafe/jev-1.13-20260917`
on every row. Same five test splits as v1 and v2 (Banking77, TREC, SST-2, AG News, Emotion; 14,048 rows). Same
Claude Code review protocol (`review_v3/GUIDELINES.md`). Spend: $1.65 for 14,496 calls, 39.2M input tokens.
Cumulative key spend after three experiments: about $10.25 of $25.

v3 came out of a level-set against the TypeSafe docs (building guide, Choice and Noul pages, Confidence page,
classification cookbook, Jev 1.13 jaggedness page). Five changes, each tied to a specific piece of guidance.

## What changed from v2

1. **The gold label is never presented as the dataset's answer.** v2 asked "the dataset says X, is that wrong?",
   which anchors the model on state that argues for a classification and is negation-shaped, two things the
   jaggedness page warns about. v3 asks an absolute Noul per label, "does label X apply to this text?", worded
   identically for every label. `fit_gold` and `fit_choice` are read out of those. Small label sets get a fit
   question for every label in the one call; Banking77 gets the gold label's fit in the first call and the
   chosen label's fit in a second call when they differ (448 second calls).
2. **An explicit ambiguity question.** "Could a careful annotator defensibly assign more than one of these
   labels?" v2 reviewers called about a third of flags ambiguous; that judgment was hidden inside the flag. Now it
   is a band of its own.
3. **Structured criteria** (`what` / `not_for` / `examples` objects, per the Choice page) for the option pairs v2
   reviewers found Jev confusing. Every not_for and example was taken from a v2 reviewer's reason on a row Jev got
   wrong: TREC's definition-vs-term-vs-method rules, Banking77's PIN-location, transfer-direction, refund-timing,
   top-up-reverted, and Apple Pay conventions, AG News's Sci/Tech scope, Emotion's keyword conventions
   (nostalgic is love, curious is surprise, awkward is fear). `none` kept only on Emotion and Banking77.
4. **No gold-tuned threshold.** v2 picked a confidence threshold that made the confident subset agree with gold
   at 95%, but gold is what is being audited. v3 uses fixed cutoffs chosen before the run: 0.5 on every Noul, and
   the Confidence page's 0.9 / 0.5 tiers on the Choice. Precision is then measured per band and the operating
   point is picked after review, which is the docs' "thresholds scale with risk".
5. **Convention nouls**, literal yes/no questions combined in code rather than prose in the task card: negation
   and hypothetical feeling (Emotion), reversal and sarcasm (SST-2), definition / term / number / abbreviation
   (TREC), technology / money / politics angle (AG News), reports-a-problem and needs-context (Banking77).

Bands, for a row where Jev's label differs from gold:

| band | rule |
|---|---|
| `error_candidate` | gold does not fit (< 0.5), Jev's label fits (>= 0.5), not ambiguous (< 0.5); tiers high / mid / low by Choice confidence 0.9 / 0.5 |
| `ambiguous_candidate` | ambiguous >= 0.5, or both labels fit |
| `weak_disagree` | neither fits, or only gold fits |
| `none_candidate` | Jev chose none and gold does not fit |

Review samples were drawn only from rows no v2 reviewer had seen, so the structured criteria (written from v2
verdicts) are measured out of sample. 339 rows reviewed: 50 / 20 / 10 per error tier, 25 ambiguous, 15 none, 10
weak per dataset where available. Reviewers saw text, gold, Jev's label, and top-3 probabilities, not the band.

## Held-out precision by band

| band | tier | reviewed | gold_wrong | jev_wrong | ambiguous | precision (95% CI) |
|---|---|--:|--:|--:|--:|--:|
| error_candidate | high | 126 | 103 | 2 | 21 | **0.82** (0.74-0.88) |
| error_candidate | mid | 47 | 24 | 4 | 19 | 0.51 (0.37-0.65) |
| error_candidate | low | 9 | 5 | 0 | 4 | 0.56 |
| ambiguous_candidate | | 94 | 26 | 14 | 54 | 0.28 (0.20-0.37) |
| none_candidate | | 30 | 11 | 7 | 12 | 0.37 (0.22-0.54) |
| weak_disagree | | 33 | 14 | 7 | 12 | 0.42 (0.27-0.59) |

Per dataset, high tier: AG News 0.84 (n=50), Emotion 0.90 (n=50), Banking77 0.61 (n=23), SST-2 2/2, TREC 0/1.
Full table with every band in `out_v3/report_v3.md`.

## v2 vs v3

| dataset | rows | v2 agree | v3 agree | v2 flag% | v3 error% (hi/mid/lo) | v3 amb% | v2 flag precision | v3 high-tier precision |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| banking77 | 3076 | 0.793 | 0.827 | 4.9 | 4.0 (80/36/6) | 9.1 | 0.66 (n=100) | 0.61 (n=23) |
| trec | 500 | 0.964 | 0.972 | 3.2 | 1.0 (4/1/0) | 1.6 | 0.23 (n=13) | n=1 |
| sst2 | 872 | 0.928 | 0.956 | 2.4 | 1.7 (12/3/0) | 2.3 | 0.71 (n=17) | n=2 |
| ag_news | 7600 | 0.876 | 0.893 | 5.4 | 2.7 (202/6/0) | 7.3 | 0.44 (n=100) | 0.84 (n=50) |
| emotion | 2000 | 0.547 | 0.567 | 10.0 | 7.1 (109/29/4) | 23.5 | 0.88 (n=100) | 0.90 (n=50) |
| **all** | 14048 | | | | | | 0.65 (n=330) | **0.82** (n=126) |

Jev's agreement with gold rose on every dataset. Jev-wrong share in the top band fell from 5% (v2 flags) to 1.6%.

**Cross-check on the v2-reviewed rows** (421 rows with existing verdicts; these informed the criteria, so this is
in-sample for change 3 but a fair test of changes 1, 2, and 4):

| v3 band | n | gold_wrong | jev_wrong | ambiguous |
|---|--:|--:|--:|--:|
| error_candidate / high | 171 | 152 | 1 | 18 |
| ambiguous_candidate | 164 | 76 | 7 | 81 |
| agree (Jev now matches gold) | 52 | 0 | 43 | 9 |
| weak_disagree | 12 | 7 | 0 | 5 |
| error_candidate / mid | 9 | 4 | 1 | 4 |

Every v2 flag that v3 now agrees with gold on was a Jev error or ambiguous; none was a real gold error. The
structured criteria removed Jev's mistakes without hiding the dataset's.

## Estimated label errors in the review queue

Band count times held-out band precision (bands with fewer than five reviewed rows omitted):

| dataset | est. errors | share of rows |
|---|--:|--:|
| banking77 | ~135 | 4.4% |
| ag_news | ~361 | 4.8% |
| emotion | ~443 | 22.1% |
| sst2 | ~4 (+12 in the high tier, n=2) | ~2% |
| trec | ~2 | 0.3% |
| **total** | ~945 | |

v2 estimated ~407 from its flag band alone. The v3 queue is larger because the ambiguous, none, and weak bands
now carry measured precision instead of being dropped; the ambiguous band alone holds an estimated ~400 errors
at 0.28 precision. Wide confidence intervals apply.

## Findings

- **The high tier is the deliverable.** 0.82 precision held out, 1.6% Jev-wrong, 407 rows across five datasets.
  A reviewer working this queue top-down finds four real errors for every five rows read.
- **The ambiguity question sorts.** 57% of the ambiguous band is ambiguous by reviewer verdict, against 17% of
  the high tier. It also costs recall: about a quarter of the ambiguous band is real error. Rank it second.
- **Absolute fit nouls are stricter than the relative Choice.** On AG News, `fit_World` reads under 0.5 on US
  election stories Jev classifies as World at confidence 1.0 (174 "agree but gold unfit" rows), and
  `weak_disagree` on AG News is 0.70 real error because `fit_choice` was under 0.5 when Jev was right. The
  jaggedness page's point that a Choice is relative and a Noul absolute shows up as a literal reading of the
  label name "World". Requiring both signals is what makes the top band precise; the price is rows left in the
  weak band.
- **Banking77 confidence tiers matter more than elsewhere.** High tier 0.61, mid tier 0.20 and mostly ambiguous.
  Reviewers' ambiguous cluster is a family of "transfer isn't possible" messages where gold assumes a reason the
  text does not state; no criteria text fixes that.
- **Convention nouls work where they are literal.** TREC `answer_is_number` 0.70 on error candidates vs 0.26 on
  agreements; Emotion `negated` four times higher on error candidates; SST-2 `sarcastic` 0.56 vs 0.32. Banking77
  `needs_context` reads about 0.7 on every band and is useless as written, a literal-reading failure of its own.
- **`none` on Emotion is a real band** (0.60 precision, ~119 rows with no emotion at all). On Banking77 it is
  mostly Jev choosing none for classifiable messages (7 of 15 Jev-wrong); drop it there next time.
- **Structured criteria raised agreement everywhere**, most on Banking77 (+3.4 points) and SST-2 (+2.8, partly
  from dropping none). The remaining Jev errors reviewers found are new confusable pairs (card_arrival vs
  card_delivery_estimate, why_verify vs unable_to_verify), the same shape as before, so another loop of the same
  feedback would help; the held-out design makes each loop measurable.
- **Cost** $1.65, about 12 cents per thousand rows, roughly 1.1x v2 for three to eleven questions per row.

## What v4 should try

- Rank the queue: high tier, then mid, then ambiguous by `fit_choice - fit_gold`; measure precision at k.
- Rewrite the AG News and Banking77 fit questions to name the section's scope, not just the label, so the
  absolute noul stops reading "World" literally; expect the weak band to shrink into the error band.
- Second feedback loop on the new confusable pairs, measured on rows neither v2 nor v3 reviewers saw.
- Drop `none` on Banking77; drop `needs_context`.
- Human verification of the high tier before any public claim; it is 407 rows.

## Files

`run_v3.py`, `datasets_v3.py`, `analyze_v3.py`, `sample_v3.py`, `report_v3.py`, `chain_v3.sh`; raw answers in
`out_v3/<dataset>.jsonl` (not for git); `out_v3/queue.jsonl` (every disagreement with band, tier, fit values),
`out_v3/summary.json`, `out_v3/report_v3.md`; reviewer samples, blind metadata, and verdicts in
`review_v3/<dataset>.jsonl`, `.meta.json`, `.verdicts.jsonl`; protocol in `review_v3/GUIDELINES.md`.
