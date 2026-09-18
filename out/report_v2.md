# Experiment 2 (v2): cookbook conventions

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
