# Experiment 2: label-error hunt v2, following the TypeSafe cookbooks

Date: 2026-09-18. Model: `typesafe/jev-1.13` via OpenRouter. Same five test splits as the v1 pilot
(Banking77, TREC, SST-2, AG News, Emotion; 14,048 rows). Same Claude Code review protocol as v1 so
flag precision is comparable. Cumulative key spend after both experiments: about $8.60 of $25.

## What changed from v1 (each maps to a cookbook)

1. **Rich option descriptions with conventions and examples** (classification_using_confidence):
   every label has a one-line description; TREC and AG News descriptions state the dataset's filing
   conventions; Banking77's 77 intents each got a description written by hand (`datasets_v2.py`).
2. **A `none` option** on every choice (date/pre-parsed extraction cookbooks).
3. **Three questions per call** (parallel_questions): the `label` choice, a `fits_any` noul, and a
   `gold_wrong` noul that carries the dataset's label in its own instructions. Questions are isolated,
   so the choice never sees the gold label.
4. **Confidence threshold chosen on a dev split** (classification_using_confidence): the first 500 rows
   (or 20% for small sets) pick the smallest grid threshold whose confident subset agrees with gold at
   95% or better. Rows below it form an explicit "uncertain" band instead of being flagged or trusted.
5. **Coarse fallback** for Banking77: seven intent families, reported when the fine intent is unsure.
6. **Two-stage rerank** for Banking77 (skill_suggestion): top-3 candidates plus none re-read when the
   top probability was under 0.9. Run as an ablation.

Flag definition changed accordingly. v1: P(gold) < 0.2 and P(top) > 0.7. v2: Jev's confident
disagreement, label != gold, label != none, confidence at or above the dev threshold.

Spend: $1.45 for 14,866 calls, 34,562,244 input tokens.

## v1 vs v2 flag quality (same datasets, same reviewer protocol)

| dataset | rows | v1 agree | v2 agree | v1 flag% | v2 flag% | v2 none% | v2 unsure% | v1 precision | v2 precision | v1 jev-wrong | v2 jev-wrong | v1 est. errors | v2 est. errors |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| banking77 | 3076 | 0.796 | 0.793 | 9.6 | 4.9 | 4.1 | 27.6 | 0.45 (n=100) | 0.66 (0.56-0.75, n=100) | 7% | 7% | ~133 | ~82 |
| trec | 500 | 0.944 | 0.964 | 3.2 | 3.2 | 0.0 | 0.8 | 0.25 (n=16) | 0.23 (0.08-0.50, n=13) | 38% | 46% | ~4 | ~3 |
| sst2 | 872 | 0.961 | 0.928 | 1.9 | 2.4 | 3.3 | 5.3 | 0.71 (n=17) | 0.71 (0.47-0.87, n=17) | 6% | 6% | ~12 | ~12 |
| ag_news | 7600 | 0.892 | 0.876 | 7.0 | 5.4 | 0.4 | 16.7 | 0.46 (n=100) | 0.44 (0.35-0.54, n=100) | 0% | 3% | ~245 | ~169 |
| emotion | 2000 | 0.587 | 0.547 | 25.8 | 10.0 | 13.3 | 42.6 | 0.70 (n=100) | 0.88 (0.80-0.93, n=100) | 1% | 1% | ~360 | ~141 |
| **total** | 14048 | | | | | | | 0.53 (n=333) | 0.65 (n=330) | 5% | 5% | ~754 | ~407 |

v2 flag = Jev's confident disagreement: final label != gold, label != none, confidence >= the dev-split threshold (smallest grid value whose confident subset agrees with gold >= 95% on the first 500 rows). v1 flag = P(gold) < 0.2 and P(top) > 0.7 over all rows. Both reviewed by the same Claude Code protocol.

## Companion noul: 'is the gold label wrong?'

| dataset | gold_wrong >= 0.7 | also a flag | noul-only | noul-only reviewed | gold_wrong | jev_wrong | ambiguous | noul-only precision |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| banking77 | 493 | 112 | 290 | 30 | 1 | 18 | 11 | 0.03 |
| trec | 12 | 11 | 1 | 1 | 0 | 0 | 1 | 0.00 |
| sst2 | 20 | 14 | 0 | 0 | 0 | 0 | 0 | 0.00 |
| ag_news | 589 | 365 | 202 | 30 | 5 | 18 | 7 | 0.17 |
| emotion | 606 | 148 | 289 | 30 | 20 | 5 | 5 | 0.67 |

## Other v2 measurements

- **banking77**: rerank on 818 rows: agreement with gold 447 -> 362 (ablation; not used); coarse family agreement on unsure+flag rows: 0.79; threshold 0.9, ECE 0.097, fits_any<0.5 on 101 test rows, p50 266 ms
- **trec**: threshold 0.5, ECE 0.012, fits_any<0.5 on 0 test rows, p50 221 ms
- **sst2**: threshold 0.5, ECE 0.025, fits_any<0.5 on 49 test rows, p50 237 ms
- **ag_news**: threshold 0.9, ECE 0.073, fits_any<0.5 on 22 test rows, p50 221 ms
- **emotion**: threshold 0.9, ECE 0.272, fits_any<0.5 on 189 test rows, p50 240 ms

## Verified gold errors found by v2 (sample)

- **banking77** gold=`wrong_exchange_rate_for_cash_withdrawal` -> `cash_withdrawal_charge` (gold_wrong noul 0.94): "Will there be additional costs of I make a withdrawal from a local ATM of British pounds? I need some cash to feel comfortable on the journe" (Message is about fees/charges for an ATM withdrawal and never mentions an exchange rate, so cash_withdrawal_charge fits and wrong_exchange_rate_for_cash_withdrawal does not.)
- **banking77** gold=`why_verify_identity` -> `unable_to_verify_identity` (gold_wrong noul 0.91): "Can I still use my account, even though the identity verification has not passed yet?" (User asks whether they can use the account while verification has not passed; they are not asking why verification is required, so why_verify_identity is wrong and unable_to_verify_identity is the closest fit.)
- **banking77** gold=`top_up_reverted` -> `top_up_failed` (gold_wrong noul 0.92): "On my last transaction it seem that my top-up was not successful." (User says the top-up did not go through / was not accepted, with no mention of a reversal, so top_up_failed fits and top_up_reverted does not.)
- **banking77** gold=`lost_or_stolen_phone` -> `lost_or_stolen_card` (gold_wrong noul 0.96): "Someone stole my cards!" (User says their cards were stolen; nothing about a phone, so lost_or_stolen_card is clearly right and lost_or_stolen_phone is clearly wrong.)
- **banking77** gold=`top_up_by_card_charge` -> `topping_up_by_card` (gold_wrong noul 0.73): "Is it okay to use a bank card to top up" (User asks whether a bank card can be used to top up, with no mention of a charge, so topping_up_by_card fits and top_up_by_card_charge does not.)
- **trec** gold=`ENTY` -> `DESC` (gold_wrong noul 0.91): "What is foot and mouth disease ?" ('What is X?' asking for a definition of a disease is a DESC definition question by TREC convention, not a request for an entity.)
- **trec** gold=`ENTY` -> `NUM` (gold_wrong noul 0.85): "What is the electrical output in Madrid , Spain ?" (The expected answer is a numeric measurement (220 volts / 50 Hz), so NUM is right and ENTY does not fit.)
- **trec** gold=`ENTY` -> `NUM` (gold_wrong noul 0.93): "What is the sales tax in Minnesota ?" (The answer is a percentage (6.5%), a clear NUM:perc, not an entity.)
- **sst2** gold=`positive` -> `negative` (gold_wrong noul 0.73): "a working class `` us vs. them '' opera that leaves no heartstring untugged and no liberal cause unplundered ." ('leaves no heartstring untugged and no liberal cause unplundered' is a sardonic accusation of manipulation and pandering, not praise.)
- **sst2** gold=`negative` -> `positive` (gold_wrong noul 0.92): "it 's somewhat clumsy and too lethargically paced -- but its story about a mysterious creature with psychic abilities offers a solid build-u" (The 'but' clause carries the verdict: solid build-up, terrific climax, nice chills outweigh the opening caveat about pacing.)
- **sst2** gold=`negative` -> `positive` (gold_wrong noul 0.94): "moretti 's compelling anatomy of grief and the difficult process of adapting to loss ." ('compelling anatomy of grief' praises the film; the sad subject matter is not the writer's evaluation.)
- **sst2** gold=`negative` -> `positive` (gold_wrong noul 0.39): "nothing is sacred in this gut-buster ." ('gut-buster' means very funny and 'nothing is sacred' is admiring of the comedy's boldness.)
- **sst2** gold=`positive` -> `negative` (gold_wrong noul 0.87): "... routine , harmless diversion and little else ." ('routine, harmless diversion and little else' is dismissive faint praise, clearly a negative verdict.)
- **ag_news** gold=`World` -> `Sports` (gold_wrong noul 0.98): "Football: Azerbaijan 0-1 England Michael Owen heads England's winner in the World Cup qualifier against Azerbaijan." (World Cup qualifier match report is plainly Sports, not World.)
- **ag_news** gold=`Sci/Tech` -> `World` (gold_wrong noul 0.88): "Prying Into FBI Activities The ACLU files Freedom of Information Act requests to find out why antiterrorism task forces have been monitoring" (ACLU FOIA requests about FBI surveillance of activists is civil-liberties/politics news with no technology content.)
- **ag_news** gold=`Sci/Tech` -> `Sports` (gold_wrong noul 0.97): "The Bahamas - the real medal winner of the Athens Olympics A different way of calculating the medal standings brings some interesting result" (Olympic medal standings analysis belongs in Sports, not Sci/Tech.)
- **ag_news** gold=`World` -> `Sci/Tech` (gold_wrong noul 0.90): "Men, Women More Different Than Thought CHICAGO - Beyond the tired cliches and sperm-and-egg basics taught in grade school science class, res" (Medical research on gender differences in disease is science/health, not World.)
- **ag_news** gold=`World` -> `Sports` (gold_wrong noul 0.97): "Ken Caminiti, 1996 NL MVP, Dies at Age 41 NEW YORK - Ken Caminiti, the 1996 National League MVP who later admitted using steroids during his" (Obituary of an NL MVP baseball player is a Sports story.)
- **emotion** gold=`anger` -> `fear` (gold_wrong noul 0.92): "i feel that it is extremely dangerous for her to be wandering out to sea" (Calling it extremely dangerous for her to be out at sea is worry/fear, not anger; 'dangerous' is a keyword artifact.)
- **emotion** gold=`sadness` -> `fear` (gold_wrong noul 0.90): "i feel kind of awkward about doing this here goes" (Feeling awkward is nervous self-consciousness (fear), not sadness; 'awkward' is a keyword artifact.)
- **emotion** gold=`anger` -> `sadness` (gold_wrong noul 0.87): "i think itd be easier if i had parents that argued with me about it then i could feel rebellious or something p but right now i just feel li" ('I just feel like a burden' is sadness; 'rebellious' is a hypothetical the writer explicitly does not feel.)
- **emotion** gold=`joy` -> `love` (gold_wrong noul 0.93): "i feel that it only makes you a person that i love who happened to do something that i don t find acceptable" (The expressed emotion is love for a person despite disapproving of their act; 'acceptable' is a keyword artifact.)
- **emotion** gold=`surprise` -> `fear` (gold_wrong noul 0.96): "i feel overwhelmed how about you" (Feeling overwhelmed is stress/anxiety, not surprise; 'overwhelmed' is a keyword artifact.)

## Findings

- **Precision up, recall down.** Overall flag precision rose from 0.53 to 0.65 on the same datasets
  with the same reviewers. The confident band is stricter (threshold 0.9 on three datasets), so it flags
  about half as many rows; estimated errors found by the flag band fell from ~754 to ~407.
- **Banking77 is the clear win.** Precision 0.45 -> 0.66 at half the flag rate, with Jev-error share
  unchanged at 7%. Rich intent descriptions did this. The remaining Jev errors are dataset conventions
  no description covered (PIN-location questions filed under get_physical_card).
- **Emotion flags are now 88% real errors** (was 70%), and the `gold_wrong` noul finds a second, almost
  disjoint set: 20 of 30 noul-only rows were also real errors. Combined, v2 finds about as many Emotion
  errors as v1 but sorted into a high-precision band and a medium band.
- **TREC conventions in descriptions helped agreement** (0.944 -> 0.964) but the 13 remaining flags are
  still mostly Jev misreading TREC's DESC-vs-ENTY and ABBR rules. Conventions in prose only go so far.
- **AG News did not move.** Precision 0.46 -> 0.44 and the ambiguous half is structural: tech-company
  business stories sit between two sections. No description fixes a label set with an overlap.
- **The `gold_wrong` noul is dataset-dependent.** Noul-only precision: Emotion 0.67, AG News 0.17,
  Banking77 0.03. On Banking77 it fires on generic messages whose gold assumes context, which reviewers
  call ambiguous, not wrong. Use it as a second band, not a flag on its own.
- **`none` helps where absence is real and hurts where it is not.** On Emotion, 13% of rows went to
  none and a sample shows most have no emotion at all ("my fingers and toes feel numb"), which is a
  further kind of label error. On SST-2, none absorbed clear pans ("detox is ultimately a pointless
  endeavor") and cost 3 points of agreement. A none option on binary sentiment is a mistake.
- **The rerank stage hurt and is not used.** On 818 Banking77 rows it moved 36 to gold, 121 away, and
  180 to none: agreement 447 -> 362. With three candidates plus none, none takes too much mass. The
  skill-suggestion cookbook uses per-candidate noul checks at the shortlist stage; a rerank without a
  none option, or with noul verification, is the untested alternative.
- **Coarse fallback works.** On unsure and flagged Banking77 rows the intent family still agreed with
  gold 79% of the time, matching the classification cookbook's "report one level up" pattern.
- **Calibration is unchanged**: ECE 0.012 to 0.097 except Emotion (0.27), where gold is the problem.
- Cost per row roughly tripled (three questions plus 77 descriptions in two of them) and is still
  under a tenth of a cent for the most expensive dataset.

## What v3 should try

- Drop `none` on binary tasks; keep it for multi-class sets with real absence.
- Use the noul band as a second review queue ranked by `gold_wrong`, with per-dataset thresholds.
- Replace the rerank with the cookbook's per-candidate noul verification, or drop it.
- Feed reviewer verdicts back into descriptions for the convention cases (TREC, Banking77 PIN rows),
  the autoresearch cookbook's loop applied to criteria text, and measure on a held-out split.
- Human verification of a few hundred rows before any public claim.

## Files

`run_v2.py`, `datasets_v2.py`, `analyze_v2.py`, `report_v2.py`, `chain_v2.sh`; raw answers with all
three questions and rerank data in `out/<dataset>.jsonl` (not for git); `out/flags.jsonl`,
`out/noul_only.jsonl`, `out/summary.json`, `out/report_v2.md`; reviewer samples and verdicts in
`review/<dataset>.jsonl`, `review/<dataset>.verdicts.jsonl`, `review/<dataset>_noul*.jsonl`.
