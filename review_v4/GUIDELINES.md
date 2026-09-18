# Reviewer guidelines (v4), same protocol as experiments 1 and 2

You are a strict annotator for one dataset. For each row in `review_v4/<dataset>.jsonl` you see the text, the
dataset's gold label, Jev's label (`jev`), and Jev's top-3 probabilities. You do not see why the row was sampled.
Judge from the text alone under the dataset's own guidelines and conventions.

Write one JSON object per line to `review_v4/<dataset>.verdicts.jsonl`:

```
{"id": "...", "verdict": "gold_wrong" | "jev_wrong" | "ambiguous", "correct_label": "<label or none>", "reason": "<one sentence>"}
```

- `gold_wrong`: the gold label is wrong under the dataset's guidelines; `correct_label` is the label a careful
  annotator would assign (it may equal `jev`, another label, or `none` when no label fits the text at all).
- `jev_wrong`: the gold label is correct or clearly defensible and Jev's label is not.
- `ambiguous`: two or more labels are each defensible under the guidelines, or the text cannot be classified
  from its own words. Prefer this verdict whenever you find yourself arguing for gold from context the text does
  not contain. Set `correct_label` to the label you lean toward.
- One sentence of reason, quoting the decisive words of the text where possible.
- Do not skip rows. Do not be swayed by Jev's probabilities; they are shown only so you know what it chose.

## Dataset conventions

**banking77** (77 intents, UK app bank, one message each). Read literally; do not assume account context the
message does not state. Generic "how long does a transfer take" is `transfer_timing`; a specific late transfer
to someone else is `pending_transfer` or `transfer_not_received_by_recipient`; money sent in from the user's
other bank that has not arrived is `balance_not_updated_after_bank_transfer`. Questions about where to find or
check a new card's PIN are `get_physical_card`, not `change_pin`. Apple Pay / Google Pay / Apple Watch in any
role is `apple_pay_or_google_pay`. "How long does a refund take" is `Refund_not_showing_up`. A top-up cancelled
or reversed after the fact is `top_up_reverted`; declined at the time is `top_up_failed`. Fee questions split by
what the fee is on (card payment, transfer, top-up by card, top-up by bank transfer, cash withdrawal, exchange).
If a message is so generic that only account history could decide the intent, that is `ambiguous`.

**trec** (6 coarse answer types). ABBR: an abbreviation or its expansion, including "What is <acronym>?".
ENTY: a thing, including a term or word ("what do you call ..."), a technique or method ("what is the easiest
way to ..."), what an instrument measures, a disease, product, animal, colour, event, language, substance.
DESC: a definition ("What is an atom?", "What are Aborigines?"), a reason (why), a manner (how do you), or a
description. HUM: a person, group, organisation, company, team, or job; organisations and teams are HUM not
ENTY. LOC: a place; planets, stars, buildings, bridges, streets and web sites are LOC. NUM: any number, amount,
date, year, percentage, distance, money, code; "when" is NUM.

**sst2** (binary sentiment on a critic's sentence or phrase). Label the writer's verdict on the film, not the
mood of its subject matter. A concession followed by "but" takes the verdict of the "but" clause. Sarcastic
praise and dismissive faint praise ("harmless diversion and little else") are negative. A short phrase with no
evaluative content is `ambiguous`.

**ag_news** (4 sections, 2004 news). World: politics, government, war, crime, disasters, courts, diplomacy,
human interest. Sports: anything sports, including athlete obituaries and sports business. Business: markets,
earnings, deals, prices, trade, labour, company news. Sci/Tech: science, space, medicine, environment, wildlife,
software, hardware, internet, telecoms, security, games, digital music, e-voting, tech-industry deals and
lawsuits. A tech company's purely financial story sits between Business and Sci/Tech; call it `ambiguous`
unless the text makes one section clearly better.

**emotion** (6 classes, "i feel ..." tweets, labels derived from hashtags). Pick the dominant emotion the writer
expresses now. Negation flips the keyword ("i do not feel assured" is fear). Hypothetical, past-and-over, or
someone else's feeling does not count. Conventions: nostalgic is love; curious is surprise; reluctant, awkward,
overwhelmed, uncomfortable, and worry about danger are fear; embarrassed, ashamed, numb-from-overload, and
feeling like a burden are sadness. A physical sensation or neutral statement with no emotion is `gold_wrong`
with `correct_label` `none`.
