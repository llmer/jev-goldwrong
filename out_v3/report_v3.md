# v3 report: bands, held-out precision, v2 comparison

Spend: $1.65 for 14,496 calls, 39,174,111 input tokens. Model reported by the API: typesafe/jev-1.13-20260917.

## Band precision on held-out rows (never seen by v2 reviewers)

| dataset | band | tier | in band | reviewed | gold_wrong | jev_wrong | ambiguous | precision (95% CI) |
|---|---|---|--:|--:|--:|--:|--:|--:|
| banking77 | ambiguous_candidate |  | 280 | 25 | 6 | 5 | 14 | 0.24 (0.11-0.43) |
| banking77 | error_candidate | high | 80 | 23 | 14 | 2 | 7 | 0.61 (0.41-0.78) |
| banking77 | error_candidate | low | 6 | 5 | 2 | 0 | 3 | 0.40 (0.12-0.77) |
| banking77 | error_candidate | mid | 36 | 20 | 4 | 3 | 13 | 0.20 (0.08-0.42) |
| banking77 | none_candidate |  | 74 | 15 | 2 | 7 | 6 | 0.13 (0.04-0.38) |
| banking77 | weak_disagree |  | 46 | 10 | 0 | 4 | 6 | 0.00 (-0.00-0.28) |
| trec | ambiguous_candidate |  | 8 | 5 | 1 | 1 | 3 | 0.20 (0.04-0.62) |
| trec | error_candidate | high | 4 | 1 | 0 | 0 | 1 | 0.00 (0.00-0.79) |
| sst2 | ambiguous_candidate |  | 20 | 14 | 3 | 5 | 6 | 0.21 (0.08-0.48) |
| sst2 | error_candidate | high | 12 | 2 | 2 | 0 | 0 | 1.00 (0.34-1.00) |
| sst2 | error_candidate | mid | 3 | 2 | 1 | 1 | 0 | 0.50 (0.09-0.91) |
| sst2 | weak_disagree |  | 3 | 3 | 1 | 2 | 0 | 0.33 (0.06-0.79) |
| ag_news | ambiguous_candidate |  | 555 | 25 | 7 | 1 | 17 | 0.28 (0.14-0.48) |
| ag_news | error_candidate | high | 202 | 50 | 42 | 0 | 8 | 0.84 (0.71-0.92) |
| ag_news | error_candidate | mid | 6 | 5 | 1 | 0 | 4 | 0.20 (0.04-0.62) |
| ag_news | weak_disagree |  | 50 | 10 | 7 | 1 | 2 | 0.70 (0.40-0.89) |
| emotion | ambiguous_candidate |  | 471 | 25 | 9 | 2 | 14 | 0.36 (0.20-0.55) |
| emotion | error_candidate | high | 109 | 50 | 45 | 0 | 5 | 0.90 (0.79-0.96) |
| emotion | error_candidate | low | 4 | 4 | 3 | 0 | 1 | 0.75 (0.30-0.95) |
| emotion | error_candidate | mid | 29 | 20 | 18 | 0 | 2 | 0.90 (0.70-0.97) |
| emotion | none_candidate |  | 198 | 15 | 9 | 0 | 6 | 0.60 (0.36-0.80) |
| emotion | weak_disagree |  | 50 | 10 | 6 | 0 | 4 | 0.60 (0.31-0.83) |
| **all** | ambiguous_candidate |  | | 94 | 26 | 14 | 54 | 0.28 (0.20-0.37) |
| **all** | error_candidate | high | | 126 | 103 | 2 | 21 | 0.82 (0.74-0.88) |
| **all** | error_candidate | low | | 9 | 5 | 0 | 4 | 0.56 (0.27-0.81) |
| **all** | error_candidate | mid | | 47 | 24 | 4 | 19 | 0.51 (0.37-0.65) |
| **all** | none_candidate |  | | 30 | 11 | 7 | 12 | 0.37 (0.22-0.54) |
| **all** | weak_disagree |  | | 33 | 14 | 7 | 12 | 0.42 (0.27-0.59) |

Bands are fixed in advance from Jev's own answers (cutoff 0.5 on every noul; confidence tiers 0.9 / 0.5), not tuned against gold. error_candidate = gold label does not fit, Jev's label fits, not ambiguous.

## v2 vs v3 on the same datasets

| dataset | rows | v2 agree | v3 agree | v2 flag% | v3 error% (hi/mid/lo) | v3 amb% | v3 none% | v2 precision | v3 error-band precision | where v2 flags landed in v3 (error/amb/agree/other) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| banking77 | 3076 | 0.793 | 0.827 | 4.9 | 4.0 (80/36/6) | 9.1 | 2.7 | 0.66 (n=100) | 0.42 (n=48) | 125: 72/41/9/3 |
| trec | 500 | 0.964 | 0.972 | 3.2 | 1.0 (4/1/0) | 1.6 | 0.0 | 0.23 (n=13) | 0.00 (n=1) | 13: 4/3/6/0 |
| sst2 | 872 | 0.928 | 0.956 | 2.4 | 1.7 (12/3/0) | 2.3 | 0.0 | 0.71 (n=17) | 0.75 (n=4) | 17: 11/6/0/0 |
| ag_news | 7600 | 0.876 | 0.893 | 5.4 | 2.7 (202/6/0) | 7.3 | 0.0 | 0.44 (n=100) | 0.78 (n=55) | 383: 181/155/25/22 |
| emotion | 2000 | 0.547 | 0.567 | 10.0 | 7.1 (109/29/4) | 23.5 | 10.2 | 0.88 (n=100) | 0.89 (n=74) | 160: 83/74/0/3 |

v2 flag rate is over the v2 test split (rows after the dev split); v3 rates are over all rows.

## Convention nouls: mean value by band

- **banking77**: reports_problem agree=0.465, agree_gold_unfit=0.23, ambiguous_candidate=0.543, error_candidate=0.422, none_candidate=0.29, none_weak=0.331, weak_disagree=0.225; needs_context agree=0.656, agree_gold_unfit=0.651, ambiguous_candidate=0.687, error_candidate=0.717, none_candidate=0.709, none_weak=0.7, weak_disagree=0.677
- **trec**: asks_definition agree=0.515, agree_gold_unfit=0.296, ambiguous_candidate=0.83, error_candidate=0.7; asks_term agree=0.225, agree_gold_unfit=0.347, ambiguous_candidate=0.439, error_candidate=0.078; answer_is_number agree=0.26, agree_gold_unfit=0.073, ambiguous_candidate=0.056, error_candidate=0.698; asks_abbrev agree=0.044, agree_gold_unfit=0.021, ambiguous_candidate=0.249, error_candidate=0.022
- **sst2**: reversal agree=0.165, agree_gold_unfit=0.085, ambiguous_candidate=0.343, error_candidate=0.237; subject_matter_dark agree=0.207, agree_gold_unfit=0.344, ambiguous_candidate=0.236, error_candidate=0.282; sarcastic agree=0.324, agree_gold_unfit=0.263, ambiguous_candidate=0.396, error_candidate=0.555
- **ag_news**: about_technology agree=0.271, agree_gold_unfit=0.222, ambiguous_candidate=0.519, error_candidate=0.243, weak_disagree=0.143; about_money agree=0.256, agree_gold_unfit=0.082, ambiguous_candidate=0.403, error_candidate=0.311, weak_disagree=0.092; about_politics agree=0.319, agree_gold_unfit=0.512, ambiguous_candidate=0.438, error_candidate=0.22, weak_disagree=0.496
- **emotion**: negated agree=0.054, agree_gold_unfit=0.084, ambiguous_candidate=0.143, error_candidate=0.195, none_candidate=0.166, none_weak=0.14, weak_disagree=0.312; not_own_current_feeling agree=0.193, agree_gold_unfit=0.205, ambiguous_candidate=0.245, error_candidate=0.269, none_candidate=0.424, none_weak=0.4, weak_disagree=0.276; no_emotion agree=0.09, agree_gold_unfit=0.194, ambiguous_candidate=0.105, error_candidate=0.157, none_candidate=0.363, none_weak=0.163, weak_disagree=0.24

## Other v3 measurements

- **banking77**: ECE 0.074, agree-but-gold-unfit 153, weak_disagree 46, second calls 448, p50 241 ms, $0.617
- **trec**: ECE 0.013, agree-but-gold-unfit 8, weak_disagree 1, second calls 0, p50 238 ms, $0.064
- **sst2**: ECE 0.021, agree-but-gold-unfit 26, weak_disagree 3, second calls 0, p50 219 ms, $0.054
- **ag_news**: ECE 0.063, agree-but-gold-unfit 174, weak_disagree 50, second calls 0, p50 242 ms, $0.705
- **emotion**: ECE 0.262, agree-but-gold-unfit 204, weak_disagree 50, second calls 0, p50 238 ms, $0.205

## Verified gold errors from the error band (held-out sample)

- **banking77** gold=`card_not_working` -> `declined_card_payment` (fit_gold 0.20, fit_jev 0.96, ambiguous 0.34): "My card was declined today when eating and I need to know what's wrong." ("My card was declined today when eating" is a specific declined card payment, not the generic card_not_working.)
- **banking77** gold=`card_payment_wrong_exchange_rate` -> `exchange_rate` (fit_gold 0.10, fit_jev 0.95, ambiguous 0.38): "How can I check the exchange rate applied to my transaction?" ("How can I check the exchange rate applied" asks how to look up a rate and never claims the rate was wrong.)
- **banking77** gold=`top_up_reverted` -> `top_up_failed` (fit_gold 0.03, fit_jev 0.84, ambiguous 0.43): "I put money into my account for the minimum balance but the application didn't accept." ("the application didn't accept" is a top-up declined at the time, which is top_up_failed, not one reverted after the fact.)
- **banking77** gold=`transfer_not_received_by_recipient` -> `transfer_timing` (fit_gold 0.08, fit_jev 0.54, ambiguous 0.48): "How long until my friend receives my transaction?" ("How long until my friend receives my transaction?" is a generic timing question with no lateness stated, which is transfer_timing by convention.)
- **sst2** gold=`positive` -> `negative` (fit_gold 0.05, fit_jev 0.97, ambiguous 0.07): "hilariously inept and ridiculous ." ('inept and ridiculous' is a verdict on the film's craft, and 'hilariously' only signals unintentional comedy; nothing in the text supports positive.)
- **sst2** gold=`negative` -> `positive` (fit_gold 0.10, fit_jev 0.86, ambiguous 0.28): "this riveting world war ii moral suspense story deals with the shadow side of american culture : racial prejudice in its ugly and diverse fo" ('this riveting ... moral suspense story' is the writer's verdict; 'racial prejudice in its ugly and diverse forms' is the subject matter, not the judgment.)
- **sst2** gold=`positive` -> `negative` (fit_gold 0.40, fit_jev 0.61, ambiguous 0.48): "slick piece of cross-promotion ." (Calling the film a 'piece of cross-promotion' is dismissive, and 'slick' is faint praise at best.)
- **ag_news** gold=`World` -> `Business` (fit_gold 0.06, fit_jev 0.96, ambiguous 0.15): "Crude Price Spike May Send Gas Higher (AP) AP - Amid soaring crude oil prices, gasoline costs have been dropping. But don't expect that to l" ('soaring crude oil prices, gasoline costs' with 'economists say' is a prices story, Business not World.)
- **ag_news** gold=`Business` -> `World` (fit_gold 0.03, fit_jev 0.97, ambiguous 0.06): "EU foreign ministers hope to break deadlock over ASEM summit The European Union said Friday it  quot;hoped to reach a conclusion quot; at a" ('EU foreign ministers' deciding on 'military-ruled Myanmar' at a summit is diplomacy, World not Business.)
- **ag_news** gold=`World` -> `Business` (fit_gold 0.34, fit_jev 0.97, ambiguous 0.29): "Volkswagen May Be Close to Settling Its Wage Talks Volkswagen and its workers entered a critical week in their wage negotiations on Monday," ('wage negotiations' between Volkswagen and its workers is labour/company news, Business not World.)
- **ag_news** gold=`World` -> `Sports` (fit_gold 0.05, fit_jev 0.96, ambiguous 0.33): "Football: Spanish FA apologises The Spanish FA apologises to its English counterparts following racist chanting." ('Football: Spanish FA apologises to its English counterparts' is a football-governing-body story, Sports not World.)
- **emotion** gold=`anger` -> `joy` (fit_gold 0.01, fit_jev 0.55, ambiguous 0.44): "i tasted some hari raya cookies and feeling greedy i would go and prebook their kueh makmur and tart because i know their hygiene standard a" (Playful 'feeling greedy' about cookies she plans to 'prebook' expresses appetite and anticipation, not anger.)
- **emotion** gold=`sadness` -> `joy` (fit_gold 0.04, fit_jev 0.56, ambiguous 0.41): "i felt a stronger wish to be free from self cherishing through my refuge practice and a return to the feeling of freedom and protection from" ('a return to the feeling of freedom and protection from suffering' is positive; 'suffering' is what is escaped.)
- **emotion** gold=`sadness` -> `joy` (fit_gold 0.14, fit_jev 0.76, ambiguous 0.34): "im feeling a lot less ugly duckling and a lot more a href http" ('feeling a lot less ugly duckling' negates the negative keyword, so the writer feels better about herself.)
- **emotion** gold=`joy` -> `fear` (fit_gold 0.03, fit_jev 0.67, ambiguous 0.40): "i don t feel brave though" ('i don t feel brave' is a negated keyword, which flips brave to fear.)
