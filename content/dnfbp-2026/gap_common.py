"""Shared bits for the competitor-gap series (8 posts). Facts checked 20 November 2026 against the Income Tax Ordinance 2001
amended up to 30.06.2026 (FBR): ss.7B, 60, 109, 114B, 114C (Fifteenth Schedule), 147, 149, 156, 161, 165, 168, 169, 182 (entry 12),
192, 192A, 205, 231AB; Tenth Schedule rules 1 and 10; First Schedule Part III Division IA and Part I Division IIIA."""
from posts import WA, a, table, S_IRIS

DATE = "2026-11-20"
DLONG = "20 November 2026"

S_ITO = ("FBR: Income Tax Ordinance, 2001 (amended up to 30.06.2026)", "https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf")
S_FBR = ("Federal Board of Revenue", "https://www.fbr.gov.pk/")
S_ATL = ("FBR: Active Taxpayers List (Income Tax)", "https://www.fbr.gov.pk/categ/active-taxpayer-list-income-tax/51147/30859/71168")
S_W8 = ("IRS: Instructions for Form W-8BEN", "https://www.irs.gov/instructions/iw8ben")
S_W8A = ("IRS: About Form W-8BEN", "https://www.irs.gov/forms-pubs/about-form-w-8-ben")
S_TRE = ("IRS: United States income tax treaties A to Z", "https://www.irs.gov/businesses/international-businesses/united-states-income-tax-treaties-a-to-z")

SL = dict(adj="adjustable-vs-final-tax-pakistan", zak="zakat-deduction-income-tax-pakistan-section-60",
          cash="cash-withdrawal-tax-non-filer-pakistan-2026", eva="tax-avoidance-vs-tax-evasion-pakistan",
          w8="w-8ben-form-pakistan-freelancers", sim="fbr-sim-block-non-filers-section-114b",
          inel="ineligible-person-section-114c-pakistan", ds="default-surcharge-fbr-section-205")
B = {k: "/blogs/" + v for k, v in SL.items()}
X = {"atlu": "/blogs/form-atl-u-fbr-guide-2026", "chk": "/blogs/check-filer-status-atl-online-pakistan", "pricing": "/pricing",
     "notice": "/fbr-notice-defense", "bank": "/tools/bank-profit-tax-calculator", "don": "/blogs/charitable-donation-tax-pakistan",
     "min": "/blogs/minimum-tax-section-113-pakistan", "free": "/blogs/tax-return-for-freelancers-2026",
     "adv": "/tools/advance-tax-instalment-calculator", "pen": "/tools/late-filing-penalty-calculator",
     "ws": "/blogs/wealth-statement-guide-pakistan-2026", "prop": "/tools/property-transfer-tax-calculator",
     "wsr": "/tools/wealth-reconciliation-calculator", "rev": "/blogs/revised-return-before-notice-penalty-relief-section-114-6a",
     "atlroute": "/tools/atl-surcharge-vs-form-atl-u-calculator", "late": "/blogs/tax-return-deadline-passed-31-october-2026-next-steps"}

FEE_RET = "Salaried return Rs 3,500; freelancer or sole proprietor return Rs 5,000 (published fees)."
FEE_NOT = "FBR notice reply from Rs 5,000 (published fee); anything larger is a fixed fee confirmed before work starts."
FEE_FIX = "Fixed fee confirmed before work starts; returns from Rs 3,500 as published."

def SERIES(cur):
    items = [("adj", "adjustable vs final tax"), ("zak", "zakat deduction"), ("cash", "cash withdrawal tax"), ("eva", "avoidance vs evasion"),
             ("w8", "W-8BEN"), ("sim", "SIM block (114B)"), ("inel", "ineligible person (114C)"), ("ds", "default surcharge")]
    return ('<p class="tf-primary"><strong>Tax explainers:</strong> ' + " &middot; ".join(a(B[k], t) for k, t in items if k != cur) + '</p>')
