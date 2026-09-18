"""v2 dataset specs: rich option descriptions with conventions and examples, coarse families, and a none option."""

NONE_ID = "none"
NONE_DESC = ("The text fits none of the offered labels: it is empty, contentless, off-topic for this label set, "
             "or could only be labeled by guessing.")

BANKING77 = {
    # card lifecycle
    "activate_my_card": "how to activate a newly received or found card so it can be used",
    "card_arrival": "asking when an ordered card will arrive; it has not come yet",
    "card_delivery_estimate": "asking how long card delivery takes in general, or delivery options and tracking",
    "card_about_to_expire": "the card is expiring soon; what happens, will a new one be sent",
    "order_physical_card": "wants to order a physical card (may already have a virtual one)",
    "get_physical_card": "asking how to obtain a physical card, e.g. is one available, who qualifies",
    "getting_spare_card": "wants an additional or spare card, or a card for someone else on the account",
    "getting_virtual_card": "how to get a virtual card",
    "get_disposable_virtual_card": "how to get a disposable (one-time) virtual card",
    "disposable_card_limits": "limits on disposable virtual cards: how many, spend caps, expiry",
    "virtual_card_not_working": "a virtual card fails when used",
    "card_not_working": "the physical card fails generally (not accepted, does not work), no decline message given",
    "contactless_not_working": "contactless / tap payment specifically fails",
    "card_swallowed": "an ATM retained or swallowed the card",
    "card_linking": "linking a card to the app or account, including re-adding a card that was previously removed or found again",
    "lost_or_stolen_card": "card is lost, missing, or stolen; what to do, block it",
    "lost_or_stolen_phone": "phone is lost or stolen; account security concerns",
    "compromised_card": "card details may have been leaked or used fraudulently; suspects fraud",
    "card_acceptance": "where the card is accepted: shops, countries, online, specific merchants",
    "visa_or_mastercard": "which card network the card is on, or can they choose Visa vs Mastercard",
    "supported_cards_and_currencies": "which cards (e.g. Amex, prepaid) and currencies can be used to top up or are supported",
    "country_support": "whether the service or cards are available in a given country or region",
    "age_limit": "minimum age to open an account or get a card, accounts for children",
    # PIN & identity
    "change_pin": "how to change or set the card PIN",
    "pin_blocked": "PIN is blocked after wrong attempts; how to unblock",
    "passcode_forgotten": "forgot the app passcode or login passcode",
    "verify_my_identity": "how to complete identity verification, what documents are needed",
    "unable_to_verify_identity": "identity verification is failing or was rejected",
    "why_verify_identity": "asking why identity verification is required, or refusing to do it",
    "verify_source_of_funds": "asked to prove where money comes from; source-of-funds checks, including whether salary or other income is acceptable",
    "edit_personal_details": "change name, address, email, phone or other personal details",
    "terminate_account": "close or delete the account",
    # top-ups
    "topping_up_by_card": "how to top up using a debit or credit card, or a card top-up not working generally",
    "top_up_by_card_charge": "is there a fee for topping up by card, or was a fee charged for it",
    "top_up_by_bank_transfer_charge": "is there a fee for topping up by bank transfer, or was a fee charged for it",
    "top_up_by_cash_or_cheque": "can they top up with cash or a cheque, how",
    "automatic_top_up": "setting up or changing automatic / recurring top-ups",
    "top_up_limits": "maximum or minimum top-up amounts, daily limits",
    "top_up_failed": "a top-up attempt failed or was declined",
    "top_up_reverted": "a top-up went through and was then reversed or refunded back",
    "pending_top_up": "a top-up is still pending, not yet credited",
    "verify_top_up": "asked to verify a top-up, or how to verify a top-up card",
    "balance_not_updated_after_cheque_or_cash_deposit": "deposited cash or a cheque but balance has not changed",
    # transfers
    "transfer_into_account": "how to transfer money into this account from an external bank, including whether SWIFT/SEPA/international transfers in are supported",
    "receiving_money": "how to receive money from someone else, e.g. salary or a friend paying them",
    "transfer_timing": "generic question about how long transfers take, no specific missing transfer",
    "pending_transfer": "a specific transfer the user sent is still showing as pending",
    "transfer_not_received_by_recipient": "the user sent money and the recipient says they did not get it",
    "balance_not_updated_after_bank_transfer": "expected an incoming bank transfer, balance not updated yet",
    "failed_transfer": "a transfer the user tried to send failed, with no specific reason given",
    "declined_transfer": "a transfer was declined or rejected; asking why",
    "beneficiary_not_allowed": "cannot add a beneficiary / recipient, or told the beneficiary is not allowed",
    "cancel_transfer": "wants to cancel a transfer already sent",
    "transfer_fee_charged": "a fee was charged on a transfer the user sent",
    # card payments & cash
    "declined_card_payment": "a card payment was declined at a shop or online; asking why",
    "pending_card_payment": "a card payment is showing as pending",
    "card_payment_not_recognised": "a card payment on the statement the user does not recognise",
    "card_payment_fee_charged": "a fee was charged on a card payment",
    "card_payment_wrong_exchange_rate": "a card payment in foreign currency used a wrong or unexpected exchange rate",
    "reverted_card_payment?": "a card payment was reversed or refunded unexpectedly, or asking if a payment will be reverted",
    "transaction_charged_twice": "the same transaction was charged twice",
    "extra_charge_on_statement": "an unexplained extra charge or fee on the statement (not a transaction they recognise as theirs)",
    "request_refund": "wants a refund for a purchase or how to request one from a merchant",
    "Refund_not_showing_up": "a refund was promised or issued but is not showing in the account",
    "declined_cash_withdrawal": "an ATM cash withdrawal was declined; asking why",
    "pending_cash_withdrawal": "a cash withdrawal is showing as pending",
    "cash_withdrawal_not_recognised": "a cash withdrawal on the statement the user did not make",
    "cash_withdrawal_charge": "a fee was charged for an ATM cash withdrawal, or asking about ATM fees",
    "wrong_amount_of_cash_received": "the ATM gave less or a different amount than requested",
    "wrong_exchange_rate_for_cash_withdrawal": "a foreign cash withdrawal used a wrong exchange rate",
    "atm_support": "which ATMs can be used, ATM availability, ATM limits",
    "apple_pay_or_google_pay": "adding the card to Apple Pay or Google Pay, or issues with them",
    "direct_debit_payment_not_recognised": "a direct debit on the statement the user does not recognise",
    # fx
    "exchange_rate": "asking what exchange rate is used or applied",
    "exchange_charge": "is there a fee or charge for currency exchange",
    "exchange_via_app": "how to exchange currencies inside the app, or exchange not working",
    "fiat_currency_support": "which fiat currencies are supported for holding or exchanging",
}
BANKING77_FAMILY = {}
for _k in BANKING77:
    if any(w in _k for w in ("top_up", "topping_up", "deposit", "automatic")): BANKING77_FAMILY[_k] = "top-up"
    elif any(w in _k for w in ("transfer", "beneficiary", "receiving_money")): BANKING77_FAMILY[_k] = "transfers"
    elif any(w in _k for w in ("exchange", "fiat")): BANKING77_FAMILY[_k] = "exchange"
    elif any(w in _k for w in ("cash", "atm")): BANKING77_FAMILY[_k] = "cash"
    elif any(w in _k for w in ("payment", "refund", "Refund", "charged", "charge", "direct_debit", "pay")): BANKING77_FAMILY[_k] = "payments"
    elif any(w in _k for w in ("pin", "passcode", "verify", "identity", "personal", "terminate", "age")): BANKING77_FAMILY[_k] = "account & identity"
    else: BANKING77_FAMILY[_k] = "cards"

TREC = {
    "ABBR": "the answer is an abbreviation, or the expansion of one: 'What does NASA stand for?', 'What is the abbreviation for Texas?'",
    "ENTY": "the answer is a thing: an animal, color, food, product, event, language, invention, substance, symbol, technique or method, "
            "term or word ('What do you call a ...?'), body part, sport, disease name, currency, or other named entity that is not a "
            "person, place, number, or definition",
    "DESC": "the answer is a description: a definition ('What is X?' where X needs explaining), a reason ('Why ...?'), a manner "
            "('How do you ...?'), or an open description of something",
    "HUM": "the answer is a person, a group of people, an organization, a company, a team, a title or job, or a description of a person. "
           "TREC convention: organizations, companies and sports teams are HUM, not ENTY",
    "LOC": "the answer is a place: city, country, state, river, mountain, address. TREC convention: planets, stars, moons and other "
           "celestial bodies, buildings, bridges, dams, streets, and web sites are LOC",
    "NUM": "the answer is a number: count, date, year, distance, weight, money, percent, temperature, speed, period of time, "
           "rank, code or phone number. TREC convention: 'when' questions and seasons/months are NUM (date)",
}

AG_NEWS = {
    "World": "world news, politics, government, elections, war, terrorism, crime, disasters, courts, general human-interest news. "
             "Not sports, not markets",
    "Sports": "any sports story: results, players, teams, leagues, Olympics, cricket, F1, rugby, football, baseball, sports business "
              "such as club sales or player contracts",
    "Business": "markets, stocks, oil prices, economic indicators, earnings, mergers, company news, labor disputes, consumer prices, "
                "airlines, retail, banking. Tech companies' financial results and deals are also Business",
    "Sci/Tech": "science and technology: research, space, medicine studies, software, hardware, internet, telecoms, gadgets, "
                "security, tech-product launches. A tech company's earnings or lawsuits without a product/technology angle are Business",
}

SST2 = {
    "negative": "the writer's verdict on the film is negative or disapproving; a concession followed by 'but ... little else to offer' "
                "is negative; sarcastic praise is negative",
    "positive": "the writer's verdict on the film is positive or approving; praise of a film about sad or ugly subject matter is "
                "positive; 'somewhat clumsy, but offers a terrific climax' is positive",
}

EMOTION = {
    "sadness": "sadness, grief, disappointment, loneliness, feeling worthless, hopeless, or let down",
    "joy": "joy, happiness, contentment, relief, pride, gratitude, feeling good or confident",
    "love": "love, affection, tenderness, caring, feeling loved or wanted, romantic or sexual desire, sympathy for someone",
    "anger": "anger, irritation, frustration, hate, disgust, feeling insulted or vengeful",
    "fear": "fear, anxiety, nervousness, stress, feeling threatened, insecure, overwhelmed, or helpless",
    "surprise": "surprise, shock, amazement, being caught off guard",
}

DATASETS = {
    "banking77": dict(hf="mteb/banking77", config=None, split="test", text="text", label="label_text",
        task="Banking77: intent classification of single customer messages to a UK app-based retail bank. Read the message "
             "literally. Generic 'how long does a transfer take' is transfer_timing, not a complaint. Generic 'how do I transfer "
             "money in' is transfer_into_account. Do not assume context the message does not state.",
        labels=BANKING77, family=BANKING77_FAMILY, rerank=True),
    "trec": dict(hf="SetFit/TREC-QC", config=None, split="test", text="text", label="label_coarse_text",
        gold_map={"description and abstract concepts": "DESC", "numeric values": "NUM", "entities": "ENTY",
                  "locations": "LOC", "human beings": "HUM", "abbreviation": "ABBR"},
        task="TREC question classification (coarse, 6 classes). Classify each English question by the TYPE of its expected "
             "answer, following TREC's conventions given in the option descriptions.", labels=TREC),
    "sst2": dict(hf="stanfordnlp/sst2", config=None, split="validation", text="sentence", label="label",
        task="Stanford Sentiment Treebank binary. Each item is a critic's sentence or phrase about a film, lowercased and "
             "tokenized. Label the writer's evaluation of the film, not the mood of its subject matter.", labels=SST2),
    "ag_news": dict(hf="fancyzhx/ag_news", config=None, split="test", text="text", label="label",
        task="AG News topic classification. Each item is a headline plus lead sentence from 2004 news feeds. Pick the section "
             "it belongs to using the option descriptions.", labels=AG_NEWS),
    "emotion": dict(hf="dair-ai/emotion", config="split", split="test", text="text", label="label",
        task="dair-ai/emotion: English tweets containing an 'i feel ...' phrase, lowercased, punctuation stripped. Pick the "
             "single dominant emotion the author expresses. Handle negation: 'i do not feel assured' is fear, 'im not feeling "
             "the jolly' is sadness. Do not label from a single keyword when the sentence says otherwise.", labels=EMOTION),
}
