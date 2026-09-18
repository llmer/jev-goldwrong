"""v4 dataset specs: v3 plus a second feedback loop and three fixes from the v3 findings.

  * FIT_STYLE = "scope": the absolute fit question leads with what the category covers, not the label name, so
    'World' stops being read literally on US election stories (v3: 174 agree-but-gold-unfit rows on AG News)
  * second criteria loop: every not_for / example added here comes from a v3 reviewer's reason on a row Jev got wrong
    (rows no v2 reviewer saw), so v3's held-out rows are now in-sample and v4 must be measured on rows neither saw
  * no `none` on Banking77 (v3: 7 of 15 none rows were Jev choosing none for classifiable messages)
  * no `needs_context` convention (v3: flat ~0.7 on every band)
"""
import copy

from datasets_v3 import (AG_NEWS as _AG3, BANKING77 as _B3, CONVENTIONS as _C3, DATASETS as _D3, EMOTION as _E3,
                         NONE_DESC, NONE_ID, SST2 as _S3, TREC as _T3, desc_text)

FIT_STYLE = "scope"


def _merge(base, extra):
    out = copy.deepcopy(base)
    for k, v in extra.items():
        cur = out[k] if isinstance(out.get(k), dict) else {"what": out[k]}
        for f, val in v.items():
            if f in cur and isinstance(cur[f], list) and isinstance(val, list):
                cur[f] = cur[f] + val
            elif f in cur and isinstance(cur[f], str) and isinstance(val, str):
                cur[f] = cur[f] + "; " + val
            else:
                cur[f] = val
        out[k] = cur
    return out


BANKING77 = _merge(_B3, {
    "card_arrival": {"what": "an ordered card has not come yet, or the user wants to track a card in transit",
                     "not_for": "how long delivery takes in general (card_delivery_estimate)",
                     "examples": ["How do I track my card?", "Is there tracking info available?"]},
    "card_delivery_estimate": {"what": "how long card delivery takes, or how fast a card can be delivered",
                               "not_for": "tracking a specific card already sent (card_arrival); where cards can be "
                                          "delivered (order_physical_card)",
                               "examples": ["How long until my card is delivered?", "How fast can you deliver?"]},
    "order_physical_card": {"what": "ordering a physical card, including where cards can be delivered",
                            "examples": ["Where can cards be delivered?", "Where do you deliver cards by mail?"]},
    "why_verify_identity": {"what": "asking why identity verification is required, whether it can be skipped, or whether "
                                    "the account can be used before verification is done",
                            "not_for": "a verification attempt that failed or was rejected (unable_to_verify_identity)",
                            "examples": ["Can I make transfers before identity verification?",
                                         "Can I make transactions before identity verification is complete?"]},
    "unable_to_verify_identity": {"not_for": "asking whether things can be done before verification (why_verify_identity)"},
    "top_up_by_bank_transfer_charge": {"what": "is there a fee for topping up by bank transfer, or for receiving money "
                                               "into the account",
                                       "examples": ["What are the charges for receiving money?",
                                                    "Do I have to pay any fees in order to receive money?"]},
    "receiving_money": {"not_for": "fees for receiving money (top_up_by_bank_transfer_charge)"},
    "apple_pay_or_google_pay": {"examples": ["I got my American Express in Apple Bay but top up is not working"],
                                "note": "'Apple Bay' is a typo for Apple Pay"},
    "change_pin": {"examples": ["I need a new Pin how do I go about that?"]},
    "wrong_exchange_rate_for_cash_withdrawal": {"examples": ["Why is the exchange rate so exorbitant? This should have "
                                                             "been a much higher amount of cash."]},
    "exchange_rate": {"not_for": "a complaint that the rate applied to a cash withdrawal or card payment was wrong"},
    "balance_not_updated_after_bank_transfer": {"examples": ["I didn't get the money I transferred"]},
    "declined_cash_withdrawal": {"examples": ["My withdrawal was cancelled."]},
    "card_payment_fee_charged": {"examples": ["Is using my card free?"]},
    "atm_support": {"examples": ["How can I withdraw money?"]},
    "country_support": {"examples": ["What locations are you in?"]},
    "card_payment_not_recognised": {"examples": ["I'm not familiar with a card payment."]},
    "get_disposable_virtual_card": {"examples": ["how secure is a disposable virtual card"]},
    "transfer_into_account": {"examples": ["How do I send my account money through transfer?"]},
})

TREC = _merge(_T3, {"DESC": {"examples": ["What is Wimbledon?"]},
                    "ENTY": {"not_for": "a bare 'What is <proper name>?' asking what something is (DESC)"}})

AG_NEWS = _merge(_AG3, {
    "World": {"what": "including United States national politics, elections, campaigns, and congressional debate"},
    "Business": {"examples": ["The New York Times appoints a deputy managing editor",
                              "Volkswagen may be close to settling its wage talks"]},
    "Sci/Tech": {"not_for": "a story where a technology company is mentioned only in passing (Business or World)"},
})

SST2 = _merge(_S3, {
    "negative": {"also_covers": "an unfavorable comparison to another film or work ('X did it better'); 'only "
                                "superficially understands'; sarcasm that praises a grim subject as pretty; 'no "
                                "telegraphing is too obvious for this movie'",
                 "examples": ["holden caulfield did it better.", "rarely has leukemia looked so shimmering and benign."]},
    "positive": {"also_covers": "a mild but genuine recommendation ('a fun little timewaster'); an 'intriguing' verdict "
                                "with a hedged qualifier",
                 "examples": ["... a fun little timewaster, helped especially by the cool presence of jean reno."]},
})

EMOTION = _merge(_E3, {"sadness": {"also_covers": "feeling fake, unwelcome, or rejected"},
                       "fear": {"not_for": "feeling fake, unwelcome, or rejected (sadness)"}})

CONVENTIONS = copy.deepcopy(_C3)
CONVENTIONS["banking77"].pop("needs_context")

DATASETS = copy.deepcopy(_D3)
DATASETS["banking77"].update(labels=BANKING77, none=False)
DATASETS["trec"].update(labels=TREC)
DATASETS["sst2"].update(labels=SST2)
DATASETS["ag_news"].update(labels=AG_NEWS)
DATASETS["emotion"].update(labels=EMOTION)
