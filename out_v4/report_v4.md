# v4 report: bands, held-out precision, v2 comparison

Spend: $1.79 for 14,498 calls, 42,520,391 input tokens. Model reported by the API: typesafe/jev-1.13-20260917.

## Band precision on held-out rows (never seen by v2 reviewers)

| dataset | band | tier | in band | reviewed | gold_wrong | jev_wrong | ambiguous | precision (95% CI) |
|---|---|---|--:|--:|--:|--:|--:|--:|
| banking77 | ambiguous_candidate |  | 285 | 25 | 2 | 4 | 19 | 0.08 (0.02-0.25) |
| banking77 | error_candidate | high | 78 | 6 | 2 | 0 | 4 | 0.33 (0.10-0.70) |
| banking77 | error_candidate | low | 4 | 2 | 0 | 1 | 1 | 0.00 (0.00-0.66) |
| banking77 | error_candidate | mid | 31 | 14 | 2 | 1 | 11 | 0.14 (0.04-0.40) |
| banking77 | weak_disagree |  | 52 | 10 | 3 | 0 | 7 | 0.30 (0.11-0.60) |
| trec | weak_disagree |  | 2 | 1 | 0 | 1 | 0 | 0.00 (0.00-0.79) |
| sst2 | weak_disagree |  | 4 | 1 | 0 | 0 | 1 | 0.00 (0.00-0.79) |
| ag_news | ambiguous_candidate |  | 539 | 25 | 3 | 0 | 22 | 0.12 (0.04-0.30) |
| ag_news | error_candidate | high | 236 | 50 | 42 | 0 | 8 | 0.84 (0.71-0.92) |
| ag_news | error_candidate | low | 1 | 1 | 0 | 0 | 1 | 0.00 (0.00-0.79) |
| ag_news | error_candidate | mid | 11 | 6 | 3 | 0 | 3 | 0.50 (0.19-0.81) |
| ag_news | weak_disagree |  | 24 | 10 | 3 | 0 | 7 | 0.30 (0.11-0.60) |
| emotion | ambiguous_candidate |  | 470 | 25 | 9 | 5 | 11 | 0.36 (0.20-0.55) |
| emotion | error_candidate | high | 104 | 7 | 6 | 0 | 1 | 0.86 (0.49-0.97) |
| emotion | error_candidate | low | 4 | 3 | 1 | 0 | 2 | 0.33 (0.06-0.79) |
| emotion | error_candidate | mid | 30 | 10 | 6 | 0 | 4 | 0.60 (0.31-0.83) |
| emotion | none_candidate |  | 195 | 15 | 10 | 0 | 5 | 0.67 (0.42-0.85) |
| emotion | weak_disagree |  | 45 | 10 | 8 | 0 | 2 | 0.80 (0.49-0.94) |
| **all** | ambiguous_candidate |  | | 75 | 14 | 9 | 52 | 0.19 (0.11-0.29) |
| **all** | error_candidate | high | | 63 | 50 | 0 | 13 | 0.79 (0.68-0.88) |
| **all** | error_candidate | low | | 6 | 1 | 1 | 4 | 0.17 (0.03-0.56) |
| **all** | error_candidate | mid | | 30 | 11 | 1 | 18 | 0.37 (0.22-0.54) |
| **all** | none_candidate |  | | 15 | 10 | 0 | 5 | 0.67 (0.42-0.85) |
| **all** | weak_disagree |  | | 32 | 14 | 1 | 17 | 0.44 (0.28-0.61) |

Bands are fixed in advance from Jev's own answers (cutoff 0.5 on every noul; confidence tiers 0.9 / 0.5), not tuned against gold. error_candidate = gold label does not fit, Jev's label fits, not ambiguous.

## v2 vs v3 on the same datasets

| dataset | rows | v2 agree | v3 agree | v2 flag% | v3 error% (hi/mid/lo) | v3 amb% | v3 none% | v2 precision | v3 error-band precision | where v2 flags landed in v3 (error/amb/agree/other) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| banking77 | 3076 | 0.793 | 0.854 | 4.9 | 3.7 (78/31/4) | 9.3 | 0.0 | 0.66 (n=100) | 0.18 (n=22) | 125: 63/48/12/2 |
| trec | 500 | 0.964 | 0.972 | 3.2 | 1.0 (3/2/0) | 1.4 | 0.0 | 0.23 (n=13) | 0.00 (n=0) | 13: 4/3/6/0 |
| sst2 | 872 | 0.928 | 0.966 | 2.4 | 1.6 (11/3/0) | 1.4 | 0.0 | 0.71 (n=17) | 0.00 (n=0) | 17: 11/6/0/0 |
| ag_news | 7600 | 0.876 | 0.893 | 5.4 | 3.3 (236/11/1) | 7.1 | 0.0 | 0.44 (n=100) | 0.79 (n=57) | 383: 210/144/25/4 |
| emotion | 2000 | 0.547 | 0.566 | 10.0 | 6.9 (104/30/4) | 23.5 | 10.8 | 0.88 (n=100) | 0.65 (n=20) | 160: 80/78/0/2 |

v2 flag rate is over the v2 test split (rows after the dev split); v3 rates are over all rows.

## Convention nouls: mean value by band

- **banking77**: reports_problem agree=0.456, agree_gold_unfit=0.207, ambiguous_candidate=0.56, error_candidate=0.411, weak_disagree=0.274
- **trec**: asks_definition agree=0.515, ambiguous_candidate=0.811, error_candidate=0.694; asks_term agree=0.226, ambiguous_candidate=0.467, error_candidate=0.08; answer_is_number agree=0.258, ambiguous_candidate=0.056, error_candidate=0.694; asks_abbrev agree=0.044, ambiguous_candidate=0.274, error_candidate=0.022
- **sst2**: reversal agree=0.168, agree_gold_unfit=0.09, ambiguous_candidate=0.416, error_candidate=0.25; subject_matter_dark agree=0.207, agree_gold_unfit=0.287, ambiguous_candidate=0.175, error_candidate=0.298; sarcastic agree=0.329, agree_gold_unfit=0.233, ambiguous_candidate=0.372, error_candidate=0.567
- **ag_news**: about_technology agree=0.267, agree_gold_unfit=0.337, ambiguous_candidate=0.528, error_candidate=0.254, weak_disagree=0.123; about_money agree=0.254, agree_gold_unfit=0.127, ambiguous_candidate=0.397, error_candidate=0.306, weak_disagree=0.105; about_politics agree=0.327, agree_gold_unfit=0.194, ambiguous_candidate=0.447, error_candidate=0.279, weak_disagree=0.105
- **emotion**: negated agree=0.053, agree_gold_unfit=0.082, ambiguous_candidate=0.144, error_candidate=0.193, none_candidate=0.171, none_weak=0.188, weak_disagree=0.342; not_own_current_feeling agree=0.191, agree_gold_unfit=0.208, ambiguous_candidate=0.243, error_candidate=0.268, none_candidate=0.417, none_weak=0.575, weak_disagree=0.262; no_emotion agree=0.092, agree_gold_unfit=0.226, ambiguous_candidate=0.109, error_candidate=0.152, none_candidate=0.372, none_weak=0.155, weak_disagree=0.224

## Other v3 measurements

- **banking77**: ECE 0.070, agree-but-gold-unfit 127, weak_disagree 52, second calls 450, p50 239 ms, $0.689
- **trec**: ECE 0.020, agree-but-gold-unfit 3, weak_disagree 2, second calls 0, p50 226 ms, $0.066
- **sst2**: ECE 0.016, agree-but-gold-unfit 47, weak_disagree 4, second calls 0, p50 288 ms, $0.063
- **ag_news**: ECE 0.063, agree-but-gold-unfit 129, weak_disagree 24, second calls 0, p50 207 ms, $0.754
- **emotion**: ECE 0.266, agree-but-gold-unfit 133, weak_disagree 45, second calls 0, p50 210 ms, $0.214

## Verified gold errors from the error band (held-out sample)

- **banking77** gold=`beneficiary_not_allowed` -> `exchange_via_app` (fit_gold 0.04, fit_jev 0.83, ambiguous 0.45): "Hey I want to buy some crypto but the app doesn't allow me to! What's the issue, I really want to exchange this" ('buy some crypto ... I really want to exchange this' is an in-app exchange request with no transfer or beneficiary anywhere in the text.)
- **banking77** gold=`balance_not_updated_after_bank_transfer` -> `transfer_timing` (fit_gold 0.21, fit_jev 0.76, ambiguous 0.35): "How long will it take for my transferred money to show up?" ('How long will it take for my transferred money to show up' is a generic transfer-timing question, not a report of an incoming bank transfer that has failed to arrive.)
- **banking77** gold=`card_arrival` -> `card_delivery_estimate` (fit_gold 0.10, fit_jev 0.96, ambiguous 0.31): "How long does a card delivery take?" ('How long does a card delivery take' is a generic delivery-time estimate, not a customer reporting a card that has not arrived.)
- **banking77** gold=`exchange_via_app` -> `fiat_currency_support` (fit_gold 0.45, fit_jev 0.94, ambiguous 0.48): "What currencies will this app exchange?" ('What currencies will this app exchange' asks which currencies are supported, not how to exchange.)
- **ag_news** gold=`World` -> `Sports` (fit_gold 0.02, fit_jev 0.98, ambiguous 0.10): "Live: Olympics day four Richard Faulds and Stephen Parry are going for gold for Great Britain on day four in Athens." ("Olympics day four ... going for gold for Great Britain" is a live Olympics report, plainly Sports.)
- **ag_news** gold=`Sci/Tech` -> `World` (fit_gold 0.07, fit_jev 0.80, ambiguous 0.37): "OPM Delving Deeper Into Employees #39; Backgrounds which sets hiring and employment standards for the government -- is reviewing its employe" (OPM, "which sets hiring and employment standards for the government", reviewing employees is a government story, not Sci/Tech.)
- **ag_news** gold=`Sci/Tech` -> `Sports` (fit_gold 0.03, fit_jev 0.69, ambiguous 0.21): "How to take the perfect penalty A sports psychologist says how footballers should prepare themselves for the high-pressure penalties." ("how footballers should prepare themselves for the high-pressure penalties" is a football story, and anything sports is Sports.)
- **ag_news** gold=`Business` -> `Sci/Tech` (fit_gold 0.05, fit_jev 0.97, ambiguous 0.49): "IBM Claims Its BlueGene Supercomputer Is the Fastest IBM Corp. on Wednesday said it has developed the world #39;s fastest computer - a 16,00" ("the world's fastest computer - a 16,000-processor version of its BlueGene/L supercomputer" is hardware news, Sci/Tech.)
- **emotion** gold=`sadness` -> `fear` (fit_gold 0.23, fit_jev 0.86, ambiguous 0.33): "i feel an unpleasant drop in my stomach as the elevator doors open at my floor" ("an unpleasant drop in my stomach" as the doors open is dread/apprehension, not sadness.)
- **emotion** gold=`sadness` -> `fear` (fit_gold 0.36, fit_jev 0.65, ambiguous 0.45): "i mention my oldest child before my youngest will her feelings be hurt" ("will her feelings be hurt" is the writer worrying about a child's possible reaction; the hurt is someone else's hypothetical feeling and the writer's own state is worry (fear).)
- **emotion** gold=`anger` -> `joy` (fit_gold 0.09, fit_jev 0.69, ambiguous 0.42): "i feel like my irritable sensitive combination skin has finally met it s match" ("irritable" describes the writer's skin, and "has finally met it s match" is satisfaction with a product (joy), not anger.)
- **emotion** gold=`surprise` -> `sadness` (fit_gold 0.03, fit_jev 0.92, ambiguous 0.49): "i just feel like im going no where and that the period of time where i was so very much enthralled with life and the options it proposed is" ("im going no where" and being "enthralled with life ... is now over" is plain sadness; "enthralled" is a surprise hashtag artifact.)
