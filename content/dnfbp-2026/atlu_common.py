"""Shared bits for the Form ATL-U series. Facts checked 19 November 2026 against the Income Tax Ordinance 2001 amended up to
30.06.2026: s.182A(1) and (3), s.182, s.151, Tenth Schedule rule 1 (and omitted rule 1A), First Schedule Part IV Divisions X and XVIII.
SRO 2097(I)/2026 (10 November 2026) prescribes Form ATL-U under rule 81B of the Income Tax Rules 2002."""
from posts import WA, a, table, S_IRIS

DATE = "2026-11-19"
DLONG = "19 November 2026"

S_ITO = ("FBR: Income Tax Ordinance, 2001 (amended up to 30.06.2026), s.182A and Tenth Schedule", "https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf")
S_SRO = ("FBR: Income Tax SROs (SRO 2097(I)/2026, Form ATL-U)", "https://www.fbr.gov.pk/Categ/Income-Tax-SROs/334")
S_ATL = ("FBR: Active Taxpayers List (Income Tax)", "https://www.fbr.gov.pk/categ/active-taxpayer-list-income-tax/51147/30859/71168")

SL = dict(guide="form-atl-u-fbr-guide-2026", iris="form-atl-u-iris-submit-step-by-step",
          alf="active-late-filer-meaning-form-atl-u-2026", fee="filer-fee-2026-pakistan-late-filer-cost",
          sale="late-filer-tax-on-property-sale-form-atl-u", bank="late-filer-tax-on-bank-profit-form-atl-u",
          buy="form-atl-u-property-purchase-6-months-breach", sal="form-atl-u-salaried-pensioners-late-return",
          free="form-atl-u-freelancers-traders-overseas", ru="filer-kaise-bane-2026-form-atl-u")
B = {k: "/blogs/" + v for k, v in SL.items()}
X = {"cmp": "/blogs/late-filer-atl-surcharge-or-form-atl-u-undertaking-2026", "sur": "/blogs/atl-surcharge-2026-pakistan",
     "next": "/blogs/tax-return-deadline-passed-31-october-2026-next-steps", "calc": "/tools/late-filing-penalty-calculator",
     "chk": "/blogs/check-filer-status-atl-online-pakistan", "atl": "/atl-pakistan-guide", "pricing": "/pricing",
     "ws": "/blogs/wealth-statement-guide-pakistan-2026", "sale": "/blogs/tax-on-property-sale-pakistan-2026",
     "bank": "/blogs/tax-on-bank-profit-pakistan-2026", "free": "/blogs/tax-return-for-freelancers-2026",
     "ovs": "/blogs/overseas-pakistani-tax-return", "salr": "/blogs/tax-return-salaried-employee-pakistan",
     "r60": "/blogs/revised-return-tax-year-2026-60-days-pakistan"}

SERIES = (f'<p class="tf-primary"><strong>Form ATL-U guides:</strong> {a(B["guide"], "complete guide")} &middot; {a(B["iris"], "IRIS steps")} &middot; '
          f'{a(B["alf"], "active late filer")} &middot; {a(B["fee"], "filer fee 2026")} &middot; {a(B["sale"], "selling property")} &middot; '
          f'{a(B["bank"], "bank profit")} &middot; {a(B["buy"], "what you cannot buy")} &middot; {a(B["sal"], "salaried")} &middot; '
          f'{a(B["free"], "freelancers and traders")} &middot; {a(B["ru"], "Roman Urdu")}<br><strong>Calculators:</strong> {a("/tools/atl-surcharge-vs-form-atl-u-calculator", "surcharge vs Form ATL-U")} &middot; {a("/tools/form-atl-u-end-date-calculator", "six-month end date")} &middot; {a("/tools/late-filing-penalty-calculator", "late filing penalty")}</p>')

F_SAL = "Salaried or pensioner return Rs 3,500 + Form ATL-U Rs 2,000 = Rs 5,500 (published fees). FBR's late-filing penalty, if any, is paid to FBR separately."
F_FREE = "Freelancer return Rs 5,000 + Form ATL-U Rs 2,000 = Rs 7,000 (published fees). FBR's late-filing penalty, if any, is paid to FBR separately."
F_SOLE = "Sole proprietor return Rs 5,000 + Form ATL-U Rs 2,000 = Rs 7,000 (published fees). FBR's late-filing penalty, if any, is paid to FBR separately."
F_OVS = "Overseas Pakistani return Rs 6,000 + Form ATL-U Rs 2,000 = Rs 8,000 (published fees). FBR's late-filing penalty, if any, is paid to FBR separately."
F_ALL = "Return fee as published (salaried Rs 3,500, freelancer or sole proprietor Rs 5,000, overseas Rs 6,000) + Form ATL-U Rs 2,000. FBR's late-filing penalty, if any, is paid to FBR separately."
F_ONLY = "Already filed late? Form ATL-U on its own: Rs 2,000. With a return: return fee as published + Rs 2,000."
