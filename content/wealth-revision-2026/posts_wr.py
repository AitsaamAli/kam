"""Wealth statement revision series: 10 guides (facts checked 24 November 2026; see wr_common.py)."""
from wr_common import DATE, DLONG, WA
from wr_visa import VISA, SCHENGEN, CANADA
from wr_more import SPONSOR, REFUSED, CASH, GIFT
from wr_last import PROP, FOREIGN, BANK

POSTS = [VISA, SCHENGEN, CANADA, SPONSOR, REFUSED, CASH, GIFT, PROP, FOREIGN, BANK]

# Per-post service wording: shared boilerplate across ten pages pushed the overlap gate past 15%.
TOPIC = {"visa": ("visa-file", "Visa-file revision"), "schengen": ("Schengen-file", "Fix my Schengen papers"),
         "canada": ("Canada-file", "Match my Canada papers"), "sponsor": ("sponsor", "Check the sponsor's statement"),
         "refused": ("post-refusal", "Review my refusal"), "cash": ("cash-figure", "Correct my cash figure"),
         "gift": ("family-transfer", "Record family money correctly"), "prop": ("property", "Fix my property entries"),
         "foreign": ("foreign-asset", "Disclose my foreign assets"), "bank": ("bank-balance", "Fix my bank balances")}
CTA = {"visa": "Send your filed statement and the bank papers you plan to give the embassy.",
       "schengen": "Send your Schengen bank statements and the IRIS copy of your wealth statement.",
       "canada": "Send six months of bank statements and your filed wealth statement.",
       "sponsor": "Send the sponsoring parent's filed statement and the funding plan for the course.",
       "refused": "Send the refusal letter and the FBR papers from your first application.",
       "cash": "Send your last few filed statements; we start with how the cash figure grew.",
       "gift": "Send the transfer records and your filed statement for that year.",
       "prop": "Send your deeds and the filed statements for the years since the first purchase.",
       "foreign": "Send a list of what you hold abroad and your filed statements.",
       "bank": "Send bank certificates for 30 June and the filed statement."}
from wr_common import SL, S_ITO, S_UKG, S_CA, S_VC, S_SBC
from wr_boost import BOOST
VISA_K = {"visa": [S_UKG, S_CA, S_VC], "schengen": [S_VC, S_SBC], "canada": [S_CA], "sponsor": [S_UKG], "refused": [S_UKG, S_CA]}
_K = {v: k for k, v in SL.items()}
for _p in POSTS:
    k = _K[_p["slug"]]
    _p["svc"] = dict(_p["svc"], compact=True, btn=TOPIC[k][1],
                     fee=f"Fixed fee for a {TOPIC[k][0]} revision, confirmed before work starts. Wealth statement preparation alone is Rs 2,000 (see /pricing).")
    _p["cta_p"] = CTA[k]
    sec, fq = BOOST[k]
    if 'id="' + sec.split('id="')[1].split('"')[0] + '"' not in _p["body"]:
        _p["body"] = _p["body"].rstrip() + "\n" + sec
        _p["faqs"] = list(_p["faqs"]) + fq
    # GEO: name the law and official guidance the page is about, as schema entities
    _p["about"] = [{"@type": "Legislation", "name": "Income Tax Ordinance, 2001 (Pakistan), section 116", "legislationJurisdiction": "PK",
                    "legislationDate": "2001", "url": S_ITO[1]}]
    _p["mentions"] = [{"@type": "WebPage", "name": n.split(": ", 1)[-1], "url": u} for n, u in VISA_K.get(k, [])]
