"""Wealth statement revision series: 10 guides (5 visa, 5 general). Facts checked 24 November 2026.
Sources, all read in full or verbatim on that date:
- Income Tax Ordinance 2001, amended up to 30 June 2026 (FBR PDF): s.39(1)(la), 39(3)-(4), 85(5), 111, 114(6), 116(1)-(3), 116A,
  122(9), 182 Table rows 1AA and 1AAA, 195A.
- GOV.UK: Guide to supporting documents, visiting the UK (updated 8 October 2026); Standard Visitor page.
- IRCC: Apply for a visitor visa (modified 16 Nov 2026); Visitor visa eligibility (28 Aug 2026); Reasons for inadmissibility (23 Jul 2026).
- EU Visa Code (Reg. 810/2009) Art. 14(1)(c), 14(3), 14(5a); Schengen Borders Code (Reg. 2016/399) Art. 6(4), read verbatim.
Not used (not verified): US State Department pages (403), Schengen Pakistan harmonised list, any refusal-code or ban period.
Fees: only /pricing figures (wealth statement Rs 2,000, individual return from Rs 3,500, notice response from Rs 5,000,
overseas Pakistani return Rs 6,000); a revision itself is a fixed fee confirmed before work starts."""
import sys
sys.path.insert(0, "/home/user/kam/content/dnfbp-2026")
from posts import WA, a, table  # noqa: F401

DATE = "2026-11-24"
DLONG = "24 November 2026"

S_ITO = ("FBR: Income Tax Ordinance 2001 (to 30 June 2026)",
         "https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf")
S_IRIS = ("FBR: IRIS", "https://iris.fbr.gov.pk/")
S_FBR = ("Federal Board of Revenue", "https://www.fbr.gov.pk/")
S_UKG = ("GOV.UK: Guide to supporting documents, visiting the UK (updated 8 October 2026)",
         "https://www.gov.uk/government/publications/visitor-visa-guide-to-supporting-documents/guide-to-supporting-documents-visiting-the-uk")
S_UKSV = ("GOV.UK: Standard Visitor visa, eligibility", "https://www.gov.uk/standard-visitor")
S_CA = ("IRCC: Apply for a visitor visa to Canada (modified 16 November 2026)",
        "https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada/apply-visitor-visa.html")
S_CAE = ("IRCC: Visitor visa eligibility (modified 28 August 2026)",
         "https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada/eligibility.html")
S_CAR = ("IRCC: Reasons you may be inadmissible to Canada (modified 23 July 2026)",
         "https://www.canada.ca/en/immigration-refugees-citizenship/services/admissibility-enforcement/inadmissibility/reasons.html")
S_VC = ("EUR-Lex: EU Visa Code, Regulation (EC) No 810/2009, Article 14", "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02009R0810-20200202")
S_SBC = ("EUR-Lex: Schengen Borders Code, Regulation (EU) 2016/399, Article 6", "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0399")

SL = dict(visa="wealth-statement-revision-before-visa-application-pakistan",
          schengen="schengen-visa-wealth-statement-revision-pakistan",
          canada="canada-visitor-visa-wealth-statement-revision-pakistan",
          sponsor="sponsor-parent-wealth-statement-revision-student-visa-pakistan",
          refused="visa-refused-funds-wealth-statement-correction-pakistan",
          cash="cash-in-hand-wealth-statement-revision-pakistan",
          gift="gift-loan-family-wealth-statement-revision-pakistan",
          prop="property-sale-purchase-wealth-statement-revision-pakistan",
          foreign="foreign-assets-wealth-statement-revision-116a-pakistan",
          bank="bank-balance-wealth-statement-revision-pakistan")
B = {k: "/blogs/" + v for k, v in SL.items()}
X = {"svc": "/wealth-statement", "pricing": "/pricing", "notice": "/fbr-notice-defense", "how": "/blogs/wealth-statement-revise-kab-kaise-iris-pakistan-2026",
     "five": "/blogs/revise-wealth-statement-last-5-years-pakistan", "recon": "/blogs/wealth-reconciliation-match-nahi-ho-rahi-fix-pakistan-2026",
     "missing": "/blogs/assets-missing-from-wealth-statement-pakistan", "guide": "/blogs/wealth-statement-guide-pakistan-2026",
     "uk": "/blogs/uk-visitor-visa-wealth-statement-pakistan-2026", "us": "/blogs/usa-b1-b2-visitor-visa-wealth-statement-pakistan-2026",
     "au": "/blogs/australia-visitor-visa-wealth-statement-pakistan-2026", "rev": "/blogs/revised-return-tax-year-2026-60-days-pakistan",
     "gift": "/blogs/gift-tax-pakistan-2026", "goldtax": "/blogs/tax-on-gold-jewelry-pakistan", "ukstu": "/blogs/uk-student-visa-fbr-tax-documents-pakistan-2026",
     "f1": "/blogs/usa-f1-student-visa-fbr-affidavit-support-pakistan-2026", "canpr": "/blogs/canada-immigration-fbr-tax-return-pakistan-2026",
     "germany": "/blogs/germany-visa-fbr-tax-return-pakistan-2026", "spain": "/blogs/spain-visa-fbr-tax-return-pakistan-2026",
     "inherit": "/blogs/wirasat-inherited-property-wealth-statement-return-pakistan-2026", "after": "/blogs/wealth-statement-mismatch-discovered-after-filing-pakistan"}

FEE = ("Wealth statement preparation Rs 2,000 and an individual return from Rs 3,500 (both on /pricing). "
       "A revision with a fresh reconciliation is a fixed fee confirmed before work starts, after we see the filed statement.")


NAMES = {"visa": "before a visa", "schengen": "Schengen", "canada": "Canada", "sponsor": "sponsor parents", "refused": "after a refusal",
         "cash": "cash in hand", "gift": "gifts and loans", "prop": "property", "foreign": "foreign assets", "bank": "bank balances"}
PICK = {"visa": ["schengen", "canada", "refused", "bank"], "schengen": ["visa", "sponsor", "gift"], "canada": ["visa", "prop", "foreign"],
        "sponsor": ["visa", "gift", "prop"], "refused": ["visa", "cash", "bank"], "cash": ["bank", "gift", "visa"],
        "gift": ["cash", "prop", "sponsor"], "prop": ["gift", "foreign", "visa"], "foreign": ["bank", "gift", "visa"], "bank": ["cash", "foreign", "visa"]}


def SERIES(cur):
    links = " &middot; ".join(a(B[k], NAMES[k]) for k in PICK[cur])
    return f'<p class="tf-primary"><strong>More on revising:</strong> {links}</p>'


def svc(h2, intro, items, risks, hook, btn="Get my wealth statement revised"):
    return dict(h2=h2, intro=intro, items=items, risks=risks, hook=hook, fee=FEE, btn=btn)


COMMON = dict(category="Wealth Statement", icon="📑",
              cta_h="Wealth statement revision, done for you",
              cta_p="Send the IRIS copy of your filed wealth statement on WhatsApp. We tell you what needs fixing and the fixed fee before any work starts.")


def post(**kw):
    p = dict(COMMON)
    p.update(kw)
    return p
