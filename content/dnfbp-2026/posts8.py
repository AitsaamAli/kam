"""Competitor-gap series: 8 tax explainers (facts checked 20 November 2026; see gap_common.py)."""
from gap_common import DATE, DLONG, WA, SL
from gap_a import ADJ, ZAK
from gap_b import CASH, EVA
from gap_c import W8, SIM
from gap_d import INEL, DS

POSTS = [ADJ, ZAK, CASH, EVA, W8, SIM, INEL, DS]

ANSWERS = {
SL["adj"]: {
    "adjustable": "Adjustable tax is tax deducted or collected in advance that Section 168 credits against your total tax for the year; any excess is refundable.",
    "final": "Final tax is deducted on income that Section 169 keeps out of your normal tax calculation; no expense, allowance or refund applies to it.",
    "separate": "An individual's profit on debt up to Rs 5 million is taxed separately under Section 7B; the bank's deduction is credited against that tax.",
    "minimum": "Minimum tax is a floor: you pay at least that amount on the income even if the normal calculation gives less.",
    "table": "Adjustable tax reduces your final bill; final tax is the bill for that income; minimum tax sets the least you pay.",
    "examples": "Salary tax (Section 149) and the 2.75% property advance tax (Section 236C) are adjustable; prize bond tax is final.",
    "claim": "Enter each deduction with its certificate in the tax credits part of your IRIS return; the credit offsets your tax.",
    "mistakes": "The costliest mistakes are not claiming adjustable deductions and adding final-tax income to normal income.",
},
SL["zak"]: {
    "law": "Section 60 allows zakat paid under the Zakat and Ushr Ordinance 1980 as a deductible allowance against taxable income.",
    "allowance": "The saving is zakat multiplied by your marginal tax rate, because an allowance reduces income, not tax.",
    "final-tax": "Zakat cannot reduce income taxed under the final tax regime, and unused zakat is lost (Section 60(3)).",
    "who": "Salaried people and business owners with normal taxable income gain most; people with only final-tax income gain nothing.",
    "bank-zakat": "Zakat deducted by your bank under the Zakat Ordinance counts; keep the bank's zakat deduction certificate.",
    "claim": "Enter the zakat paid in the deductible allowances part of the IRIS return and keep the certificate.",
    "example": "Rs 100,000 zakat at an 11% marginal rate saves about Rs 11,000 of income tax.",
    "mistakes": "Common mistakes are claiming zakat as a tax credit, claiming it against final-tax income, and not keeping certificates.",
},
SL["cash"]: {
    "law": "Banks deduct 0.8% advance tax when a person off the ATL withdraws more than Rs 50,000 cash in a day (Section 231AB).",
    "filers": "No. People on the Active Taxpayers List pay no cash withdrawal tax.",
    "history": "Sections 231A, 231AA and 236P were omitted in 2021; Section 231AB brought the tax back in 2023 for non-filers only.",
    "examples": "A non-filer withdrawing Rs 1,000,000 in a day pays Rs 8,000; a filer pays nothing.",
    "recover": "Claim it as a credit in your return; refunds are issued only once you are on the ATL (Section 182A).",
    "other-banking": "Bank profit is taxed at 20% for filers and 40% for others; the Section 114C cash cap applies only once notified.",
    "steps": "Check your ATL status, file the return and wealth statement, and use the surcharge or Form ATL-U route if late.",
},
SL["eva"]: {
    "three-zones": "The law separates legal planning, tax avoidance schemes (Section 109) and evasion (Sections 182, 192, 192A).",
    "planning": "Using zakat, donations, pension credits and filer rates as the law intends is legal tax planning.",
    "section-109": "The Commissioner can disregard or recharacterise a transaction whose main purposes include reducing tax (Section 109).",
    "evasion": "Concealment carries a penalty of Rs 100,000 or the tax evaded, whichever is higher (Section 182, entry 12).",
    "prosecution": "Concealment with revenue impact of Rs 500,000 or more can mean up to two years' imprisonment (Section 192A).",
    "grey": "An arrangement is safe when it has real substance and documents; paper-only transfers are the usual target.",
    "fix": "Revising before an audit or Section 122(9) notice, with tax and surcharge paid, avoids penalty (Section 114(6A)).",
},
SL["w8"]: {
    "what": "Form W-8BEN certifies to a US payer that you are a non-US individual and the beneficial owner of the income.",
    "who": "Pakistani individuals paid by US clients, platforms or brokers need it; companies use W-8BEN-E.",
    "services": "Services performed in Pakistan are generally not US-source income, so no US tax is usually withheld.",
    "lines": "Enter your name, Pakistan, your home address and your NTN (CNIC) as foreign TIN; leave Part II blank unless claiming a treaty rate.",
    "treaty": "Part II claims a US-Pakistan treaty rate on US-source income such as dividends; most freelancers do not need it.",
    "mistakes": "Common errors are a missing NTN, a business address, a wrong date order and an unneeded treaty claim.",
    "pakistan": "The W-8BEN does not change your Pakistani tax; freelance income is reported in your FBR return.",
    "renew": "A W-8BEN is generally valid until the end of the third calendar year after signing.",
},
SL["sim"]: {
    "law": "Section 114B lets the Board order SIM blocking, power and gas cuts and travel limits for people liable to file but not on the ATL.",
    "conditions": "A Section 114(4) notice must have been issued, its date passed, and the return still unfiled.",
    "who": "Only people liable to file under Section 114 can be listed: income above the exempt amount, property, vehicles above 1000 cc or an NTN.",
    "check": "Check your ATL status and your IRIS inbox for a Section 114(4) notice.",
    "restore": "File the return, then ask your Commissioner to order restoration under Section 114B(3).",
    "penalties": "Restoration does not cancel other action; late filing penalties still apply (Section 114B(5)).",
    "mistakes": "Not every non-filer is blocked, and paying a fine alone does not restore a SIM; filing does.",
},
SL["inel"]: {
    "status": "Section 114C applies only from a date the Federal Government notifies in the official Gazette (Section 114C(5)).",
    "thresholds": "Cars above Rs 7 million, property above Rs 100 million, investments above Rs 50 million, and cash withdrawals of Rs 100 million a year.",
    "eligible": "An eligible person filed last year's return with sufficient resources, or a sources of investment and expenditure statement.",
    "sufficient": "Sufficient resources means 130% of declared cash and equivalent assets.",
    "sie": "The sources of investment statement allows the deal but is not proof of the source of income under Section 111.",
    "prepare": "File on time, declare liquid assets fully, reconcile the wealth statement, and revise before buying if needed.",
    "myths": "Filing alone is not enough, only cars above Rs 7 million are covered, and non-residents are outside clauses (a) to (c).",
},
SL["ds"]: {
    "what": "Default surcharge is a charge for paying tax, penalties or other amounts late; it is not a penalty.",
    "rates": "Unpaid tax carries the higher of 12% or KIBOR plus 3% a year; advance tax and withholding defaults carry 12%.",
    "due": "Tax with a return is due on the return due date (Section 137(1)); order demands are due on the notice date.",
    "formula": "Unpaid amount × annual rate × days late ÷ 365.",
    "examples": "Rs 100,000 paid 73 days late at 12% costs Rs 2,400 in default surcharge.",
    "advance": "Missed advance tax carries 12% a year until paid or the return due date, whichever is earlier (Section 205(1A)).",
    "withholding": "Agents who fail to deduct or deposit tax owe the tax (Section 161) plus 12% a year surcharge (Section 205(3)).",
    "relief": "Surcharge is refunded to the extent the underlying amount is held not payable (Section 205(2)).",
    "assess": "Default surcharge is assessed, recovered and appealed as if it were tax (Section 205(5) and (6)).",
    "tips": "Pay the tax first; the surcharge stops the day you pay.",
},
}
for _p in POSTS:
    _p["answers"] = ANSWERS.get(_p["slug"], {})

from gap_more import MORE, DESC, TITLE
for _p in POSTS:
    _p["body"] = _p["body"].rstrip() + "\n" + MORE.get(_p["slug"], "")
    if DESC.get(_p["slug"]):
        _p["description"] = DESC[_p["slug"]]
    if TITLE.get(_p["slug"]):
        _p["title"] = TITLE[_p["slug"]]

DESC_Z = "Section 60: zakat paid under the Zakat and Ushr Ordinance reduces taxable income. Who can claim, the limits, final-tax income and the documents you need."
MORE_ANS = {
SL["zak"]: {"zakat-vs-donation": "Zakat under the Zakat law is a Section 60 allowance; gifts to approved bodies are a Section 61 tax credit. One amount cannot be claimed under both.",
            "wealth": "Show zakat paid as an outflow in the wealth statement so it reconciles.",
            "timing": "Zakat counts in the tax year (1 July to 30 June) in which it was actually paid."},
SL["adj"]: {"refund": "Adjustable tax above your liability is refundable once you are on the ATL; final tax is never refunded.",
            "return": "Adjustable taxes go under tax credits, final-tax income in its own part, and minimum tax is compared with the normal calculation.",
            "filer-rates": "Off the ATL, many deductions are higher, such as 40% instead of 20% on bank profit, and refunds are blocked."},
SL["cash"]: {"business": "A business off the ATL drawing Rs 250,000 a day pays about Rs 600,000 a year in cash withdrawal tax.",
             "bank-side": "The bank must deduct the tax and relies on FBR's Active Taxpayers List to decide who is a filer.",
             "dont": "Do not route cash through relatives or file a false nil return to avoid the 0.8%."},
SL["eva"]: {"how-found": "Most cases turn on Section 111: unexplained investments, money or expenditure are added to income.",
            "checklist": "Genuine ownership, full documents, a commercial purpose and a reconciling wealth statement keep planning legal.",
            "penalty-math": "Concealment costs the tax, default surcharge and a penalty of at least Rs 100,000; voluntary revision avoids the penalty."},
SL["w8"]: {"which-form": "Individuals use W-8BEN, non-US entities use W-8BEN-E, and US citizens or residents use W-9.",
           "platform-steps": "Choose individual and non-US person, enter your CNIC name and address, your NTN as foreign TIN, and skip the treaty claim unless needed.",
           "records": "Keep the platform earnings statement, bank remittance records and the W-8BEN together for FBR."},
SL["sim"]: {"notice": "A Section 114(4) notice gives 30 days (or the stated period) to file, and can cover up to five past tax years.",
            "not-liable": "Reply in writing with evidence; Section 114B(3)(b) allows restoration if you were not liable to file.",
            "cost": "A late return's penalty is reduced if filed within three months of the due date; a block costs more."},
SL["inel"]: {"scenarios": "A filer with Rs 7 million declared liquid assets can buy a car up to Rs 9.1 million; a car below Rs 7 million is outside 114C.",
             "fits": "Section 114C tests declared resources, not just filing, unlike Sections 231AB and 114B, which are already in force.",
             "timeline": "Eligibility rests on the previous tax year's return, so prepare a year before the purchase."},
SL["ds"]: {"vs-penalty": "Default surcharge is for paying late; Section 182 penalties are for filing late or concealing; Section 182A is the ATL surcharge.",
           "dates": "Rs 240,000 paid 76 days after 31 October at 12% costs Rs 5,996 in default surcharge.",
           "instalment-example": "A Rs 1,000,000 instalment paid 60 days late costs Rs 19,726 at 12% under Section 205(1A)."},
}
for _p in POSTS:
    _p["answers"].update(MORE_ANS.get(_p["slug"], {}))
    if _p["slug"] == SL["zak"]:
        _p["description"] = DESC_Z

EXTRA_ANS = {
SL["zak"]: {"business": "Any person, including an AOP or company, can claim zakat it paid itself under the Zakat law.",
            "checklist": "Confirm it was paid under the Zakat law, in the tax year, by you, against normal taxable income, with a certificate."},
SL["cash"]: {"overseas": "Non-residents are not exempt: anyone off the ATL pays 0.8% above Rs 50,000 a day.",
             "quick-calc": "Tax = the day's total cash withdrawn × 0.8%, once the total exceeds Rs 50,000 and you are off the ATL."},
SL["eva"]: {"abetment": "Knowingly helping someone evade tax is an offence under Section 199: a fine, up to three years' imprisonment, or both."},
SL["sim"]: {"prevent": "Keep IRIS contact details current, file on time, answer every notice and check the ATL after filing."},
SL["inel"]: {"companies": "Companies and AOPs are tested on cash and equivalents in the financial statements filed with the latest return."},
}
for _p in POSTS:
    _p["answers"].update(EXTRA_ANS.get(_p["slug"], {}))
