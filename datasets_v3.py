"""v3 dataset specs.

Changes from v2, each tied to the TypeSafe docs:
  * structured criteria (what / not_for / examples) for the option pairs v2 reviewers found Jev confusing
    (Choice page: "Structured instructions and criteria"; jaggedness: "Literal reading")
  * per-dataset convention questions, literal yes/no nouls combined in code (jaggedness: "split it into two
    literal questions and combine them in code")
  * `none` only where absence is real (Emotion, Banking77); dropped on SST-2, TREC, AG News (Choice page: add
    none "when the list might not cover every input")
The text of every not_for / example below comes from a v2 reviewer verdict on a row Jev got wrong.
"""
from datasets_v2 import BANKING77 as _B77_V2, BANKING77_FAMILY

NONE_ID = "none"
NONE_DESC = {"what": "no offered label fits: the text is empty, contentless, off-topic for this label set, or could only "
                     "be labeled by guessing"}


def desc_text(d):
    """Render a criteria value (string or object) as one line for use inside a noul instruction."""
    if isinstance(d, str):
        return d
    parts = []
    for k, v in d.items():
        if isinstance(v, list):
            v = "; ".join(f"'{x}'" for x in v)
        parts.append(f"{k}: {v}")
    return " | ".join(parts)


# ---------------------------------------------------------------- Banking77: overlay structured entries on the v2 text
BANKING77 = dict(_B77_V2)
BANKING77.update({
    "get_physical_card": {
        "what": "how to obtain a physical card, or where to find / how to check the PIN of a newly received card",
        "not_for": "changing or resetting a PIN (change_pin)",
        "examples": ["What do I need to do for a PIN?", "If I need a PIN for my card, where is it located?",
                     "I just got my new card but am not sure how to check its PIN."]},
    "change_pin": {
        "what": "how to change, set, or reset the card PIN",
        "not_for": "finding out or checking what the PIN of a new card is (get_physical_card)",
        "examples": ["How do I change my PIN?", "Can I set my own PIN?"]},
    "balance_not_updated_after_bank_transfer": {
        "what": "money the user sent into this account from another bank account of theirs has not shown up yet",
        "not_for": "a transfer sent to another person that shows as pending (pending_transfer) or that the recipient "
                   "did not get (transfer_not_received_by_recipient)",
        "examples": ["I made a transfer a few hours ago from my UK bank account and I do not see it yet.",
                     "Hey, I tried to make a bank transfer from my UK account a few hours ago, but it hasn't shown up."]},
    "pending_transfer": {
        "what": "a transfer the user sent to someone else is still showing as pending in the app",
        "not_for": "money sent from the user's other bank into this account that has not appeared "
                   "(balance_not_updated_after_bank_transfer)",
        "examples": ["Why is my transfer still pending?", "My payment to my friend says pending."]},
    "transfer_not_received_by_recipient": {
        "what": "the user sent money and it has not arrived or the recipient says they did not get it",
        "examples": ["My money transfer has not arrived.", "My friend says the money I sent isn't there."]},
    "transfer_timing": {
        "what": "a general question about how long transfers take, with no specific transfer that is late or missing",
        "not_for": "a specific transfer that is late (pending_transfer, transfer_not_received_by_recipient)",
        "examples": ["How long do transfers usually take?"]},
    "Refund_not_showing_up": {
        "what": "a refund was requested or promised and has not appeared, or asking how long a refund takes to show",
        "not_for": "how to start a refund request (request_refund)",
        "examples": ["How long does it take for a refund?",
                     "I contacted the seller for a refund a week ago but nothing has shown up."]},
    "request_refund": {
        "what": "wants a refund for a purchase, or asks how to request one from a merchant",
        "not_for": "waiting for a refund already requested, or asking how long refunds take (Refund_not_showing_up)",
        "examples": ["How do I get a refund for something I bought?"]},
    "top_up_reverted": {
        "what": "a top-up went through and was then reversed, refunded, or cancelled afterwards",
        "not_for": "a top-up that was declined or did not go through at the time (top_up_failed)",
        "examples": ["I think my top-up was cancelled.", "Has my top-up been cancelled?",
                     "My top-up was canceled and I have no idea why."]},
    "top_up_failed": {
        "what": "a top-up attempt was declined, rejected, or did not go through",
        "not_for": "a top-up that succeeded and was later cancelled or reversed (top_up_reverted)",
        "examples": ["My top-up was not successful.", "Why did my top-up get declined?"]},
    "apple_pay_or_google_pay": {
        "what": "anything involving Apple Pay, Google Pay, or an Apple Watch: adding the card to them, paying with them, "
                "or topping up with them",
        "not_for": "top-ups by an ordinary debit or credit card (topping_up_by_card)",
        "examples": ["How do I top up with Apple Pay?", "Is Apple Pay eligible for top up?",
                     "Can Google Pay be used to make a top-up?", "How do I top up? Can I use my Apple Watch?"]},
    "topping_up_by_card": {
        "what": "how to top up using a debit or credit card, or a card top-up not working generally",
        "not_for": "top-ups via Apple Pay or Google Pay (apple_pay_or_google_pay); fees for card top-ups "
                   "(top_up_by_card_charge)",
        "examples": ["Is it okay to use a bank card to top up?"]},
    "supported_cards_and_currencies": {
        "what": "which card types (e.g. Amex, prepaid, Visa, Mastercard) and which currencies can be used to top up",
        "not_for": "Apple Pay or Google Pay (apple_pay_or_google_pay)"},
    "contactless_not_working": {
        "what": "contactless / tap payment fails, or asking whether or how contactless is enabled on the card",
        "examples": ["Are contactless payments enabled on my new card?",
                     "How do I check my security settings to allow contactless pay?"]},
    "declined_cash_withdrawal": {
        "what": "an ATM cash withdrawal was declined, or the user cannot withdraw funds; asking why",
        "examples": ["I want to know why I have been unable to withdraw funds."]},
    "balance_not_updated_after_cheque_or_cash_deposit": {
        "what": "deposited cash or a cheque and the balance has not changed",
        "examples": ["Where is my deposit?"]},
    "cash_withdrawal_charge": {
        "what": "a fee was charged for an ATM cash withdrawal, or asking whether ATM withdrawals cost anything",
        "not_for": "the exchange rate applied to a foreign withdrawal (wrong_exchange_rate_for_cash_withdrawal)",
        "examples": ["Will there be additional costs if I withdraw British pounds from a local ATM?"]},
    "lost_or_stolen_card": {
        "what": "the card is lost, missing, or stolen; what to do, block it",
        "not_for": "a lost or stolen phone (lost_or_stolen_phone)",
        "examples": ["Someone stole my cards!"]},
    "unable_to_verify_identity": {
        "what": "identity verification is failing, was rejected, or has not passed yet and the user asks what that means",
        "not_for": "asking why verification is needed at all (why_verify_identity)",
        "examples": ["Can I still use my account even though identity verification has not passed yet?"]},
})

TREC = {
    "ABBR": {"what": "the answer is an abbreviation, or the expansion of one; 'What is <acronym>?' asks for the expansion",
             "examples": ["What does NASA stand for?", "What is the abbreviation for Texas?", "What is TMJ?"]},
    "ENTY": {"what": "the answer is a thing: an animal, color, food, product, event, language, invention, substance, symbol, "
                     "body part, sport, disease name, currency, or other named entity; also a term or word ('What do you "
                     "call ...?'), a technique or method ('What is the easiest way to ...?'), or what an instrument measures",
             "not_for": "organizations, companies, and teams (HUM); definitions of a common noun or a people ('What are "
                        "Aborigines?' is DESC); numbers and amounts (NUM)",
             "examples": ["What do you call a professional map drawer?", "What's the easiest way to remove wallpaper?",
                          "What does a barometer measure?", "What is foot and mouth disease?"]},
    "DESC": {"what": "the answer is a description: a definition ('What is X?' where X is a word, concept, or a people that "
                     "needs explaining), a reason ('Why ...?'), a manner ('How do you ...?'), or an open description",
             "not_for": "'What is <acronym>?' (ABBR); 'what is the best/easiest way to' asking for a method (ENTY); "
                        "'what do you call' asking for a term (ENTY)",
             "examples": ["What is an atom?", "What are Aborigines?", "Why is the sky blue?", "How does a clock work?"]},
    "HUM": {"what": "the answer is a person, a group of people, an organization, a company, a team, a title or job, or a "
                    "description of a person; TREC files organizations, companies, and sports teams here",
            "not_for": "a definition of a people or group ('What are Aborigines?' is DESC); a term for a kind of person "
                       "('What do you call a professional map drawer?' is ENTY)",
            "examples": ["Who wrote Hamlet?", "What did Jesse Jackson organize?", "What company makes Bentley cars?"]},
    "LOC": {"what": "the answer is a place: city, country, state, river, mountain, address; TREC also files planets, stars, "
                    "moons, buildings, bridges, dams, streets, and web sites here",
            "examples": ["Where is the Taj Mahal?", "What is the largest planet?"]},
    "NUM": {"what": "the answer is a number: count, date, year, distance, weight, money, percent, temperature, speed, period "
                    "of time, rank, code, or phone number; 'when' questions and seasons or months are NUM",
            "examples": ["How far is it from Denver to Aspen?", "What is the sales tax in Minnesota?",
                         "What is the electrical output in Madrid, Spain?", "When was the telephone invented?"]},
}

AG_NEWS = {
    "World": {"what": "world and national news: politics, government, elections, war, terrorism, crime, disasters, courts, "
                      "diplomacy, and general human-interest news",
              "not_for": "sports (Sports); markets and company finances (Business); stories whose main subject is a "
                         "technology, a scientific finding, the environment, or wildlife (Sci/Tech)",
              "examples": ["ACLU files FOIA requests over FBI monitoring of activists",
                           "Japan won't open its market to US beef anytime soon"]},
    "Sports": {"what": "any sports story: results, players, teams, leagues, the Olympics, cricket, F1, rugby, football, "
                       "baseball, athlete obituaries, and sports business such as club sales or player contracts",
               "examples": ["Michael Owen heads England's winner in the World Cup qualifier",
                            "Ken Caminiti, 1996 NL MVP, dies at 41"]},
    "Business": {"what": "markets, stocks, oil prices, economic indicators, earnings, mergers, company news, labor disputes, "
                         "consumer prices, trade, airlines, retail, banking; business figures such as Martha Stewart",
                 "not_for": "a technology company's product, service, or industry story (Sci/Tech)",
                 "examples": ["Oil prices hit a new high", "Airline reports quarterly loss"]},
    "Sci/Tech": {"what": "science and technology: research, space, medicine, environment and climate, wildlife and nature, "
                         "software, hardware, internet, telecoms, gadgets, security, video games, digital music and "
                         "file-sharing, e-voting, tech-industry mergers and lawsuits, and tech workforce policy",
                 "not_for": "a story about an earthquake's or storm's human toll rather than the science (World)",
                 "examples": ["Apple iTunes accused of overcharging in the UK", "E-voting problems cause loss of votes",
                              "China reports births of two giant pandas", "Senate weighs H-1B visa changes",
                              "Men, women more different than thought, researchers find"]},
}

SST2 = {
    "negative": {"what": "the writer's verdict on the film is negative or disapproving",
                 "also_covers": "a concession followed by 'but ... little else'; sarcastic praise; faint praise that "
                                "dismisses ('routine, harmless diversion and little else'); an accusation of manipulation "
                                "('leaves no heartstring untugged and no liberal cause unplundered')",
                 "examples": ["... routine, harmless diversion and little else.",
                              "detox is ultimately a pointless endeavor."]},
    "positive": {"what": "the writer's verdict on the film is positive or approving",
                 "also_covers": "praise of a film about sad or ugly subject matter ('compelling anatomy of grief'); a "
                                "caveat followed by 'but' and real praise; praise of energy or grip with a minor aside; "
                                "comedy praised for boldness ('nothing is sacred in this gut-buster')",
                 "examples": ["somewhat clumsy and too lethargically paced -- but its story offers a solid build-up and a "
                              "terrific climax.",
                              "drops you into a dizzying, volatile, pressure-cooker of a situation that quickly snowballs."]},
}

EMOTION = {
    "sadness": {"what": "sadness, grief, disappointment, loneliness, feeling worthless, hopeless, or let down",
                "also_covers": "embarrassed or ashamed; numb from emotional overload; feeling like a burden"},
    "joy": {"what": "joy, happiness, contentment, relief, pride, gratitude, feeling good, confident, or excited"},
    "love": {"what": "love, affection, tenderness, caring, feeling loved or wanted, romantic or sexual desire, sympathy",
             "also_covers": "nostalgic, fond longing; love for a person despite disapproving of what they did"},
    "anger": {"what": "anger, irritation, frustration, hate, disgust, feeling insulted or vengeful",
              "not_for": "worry about danger ('extremely dangerous' is fear); a hypothetical rebellion the writer says "
                         "they do not feel"},
    "fear": {"what": "fear, anxiety, nervousness, stress, feeling threatened, insecure, overwhelmed, helpless, or "
                     "uncomfortable",
             "also_covers": "reluctant or hesitant; awkward or self-conscious; worried that something is dangerous"},
    "surprise": {"what": "surprise, shock, amazement, being caught off guard",
                 "also_covers": "curious about something new",
                 "not_for": "feeling overwhelmed (fear)"},
}

# ---------------------------------------------------------------- convention questions: literal nouls combined in code
CONVENTIONS = {
    "banking77": {
        "reports_problem": "Is the user reporting something that has already gone wrong with their account or a specific "
                           "transaction, rather than asking how something works or whether it is possible?",
        "needs_context": "Is the message so generic that the specific issue could only be identified by looking at the "
                         "user's account history rather than from the message itself?",
    },
    "trec": {
        "asks_definition": "Does the question ask what something is or what it means, i.e. for a definition or explanation?",
        "asks_term": "Does the question ask for the word, name, or term used for something, for example 'what do you call'?",
        "answer_is_number": "Would the expected answer be a number, amount, date, or percentage?",
        "asks_abbrev": "Does the question ask what an abbreviation or acronym stands for, or what the abbreviation of "
                       "something is?",
    },
    "sst2": {
        "reversal": "Does the sentence end on a judgment that reverses its opening clause, such as a concession followed "
                    "by 'but' and the opposite verdict?",
        "subject_matter_dark": "Is any bleak, sad, or ugly content in the sentence about the film's subject matter rather "
                               "than the writer's opinion of the film?",
        "sarcastic": "Is any praise in the sentence sarcastic or ironic?",
    },
    "ag_news": {
        "about_technology": "Is a technology, computing, the internet, a scientific finding, the environment, or wildlife "
                            "the main subject of this story?",
        "about_money": "Are markets, earnings, deals, prices, trade, or a company's finances the main subject of this story?",
        "about_politics": "Are government, politics, elections, war, terrorism, courts, or crime the main subject of this "
                          "story?",
    },
    "emotion": {
        "negated": "Is the main feeling word in the text negated or denied, for example 'i do not feel X' or "
                   "'im not feeling X'?",
        "not_own_current_feeling": "Is the feeling described as hypothetical, wished for, over and in the past, or felt by "
                                   "someone other than the writer, rather than what the writer feels now?",
        "no_emotion": "Does the text describe a physical sensation or a neutral fact rather than an emotion?",
    },
}

DATASETS = {
    "banking77": dict(hf="mteb/banking77", config=None, split="test", text="text", label="label_text",
        task="Banking77: intent classification of single customer messages to a UK app-based retail bank. Read the message "
             "literally. Generic 'how long does a transfer take' is transfer_timing, not a complaint. Generic 'how do I transfer "
             "money in' is transfer_into_account. Do not assume context the message does not state.",
        labels=BANKING77, family=BANKING77_FAMILY, none=True),
    "trec": dict(hf="SetFit/TREC-QC", config=None, split="test", text="text", label="label_coarse_text",
        gold_map={"description and abstract concepts": "DESC", "numeric values": "NUM", "entities": "ENTY",
                  "locations": "LOC", "human beings": "HUM", "abbreviation": "ABBR"},
        task="TREC question classification (coarse, 6 classes). Classify each English question by the TYPE of its expected "
             "answer, following TREC's conventions given in the option descriptions.", labels=TREC, none=False),
    "sst2": dict(hf="stanfordnlp/sst2", config=None, split="validation", text="sentence", label="label",
        task="Stanford Sentiment Treebank binary. Each item is a critic's sentence or phrase about a film, lowercased and "
             "tokenized. Label the writer's evaluation of the film, not the mood of its subject matter.", labels=SST2,
        none=False),
    "ag_news": dict(hf="fancyzhx/ag_news", config=None, split="test", text="text", label="label",
        task="AG News topic classification. Each item is a headline plus lead sentence from 2004 news feeds. Pick the section "
             "it belongs to using the option descriptions.", labels=AG_NEWS, none=False),
    "emotion": dict(hf="dair-ai/emotion", config="split", split="test", text="text", label="label",
        task="dair-ai/emotion: English tweets containing an 'i feel ...' phrase, lowercased, punctuation stripped. Pick the "
             "single dominant emotion the author expresses. Handle negation: 'i do not feel assured' is fear, 'im not feeling "
             "the jolly' is sadness. Do not label from a single keyword when the sentence says otherwise.", labels=EMOTION,
        none=True),
}
