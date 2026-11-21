"""Shared bits for the PRA registration series (10 posts + /pra-registration service page).
Facts checked 21 November 2026 against official Punjab Revenue Authority texts only:
- Punjab Sales Tax on Services Act 2012, Chapter III (ss.17-24) and Chapter IV (ss.25-29), PRA SOP downloads
- Punjab Sales Tax on Services (Registration and De-registration) Rules 2012 (rules 2-15, Forms PST-01, PST-02, PST-03)
- PRAL/PRA "PRA-Registration Module User's Manual" v0.1 (January 2024) for the IRIS screens
- e-PRA login page (online verification services, helpline) and PRA Iris Sales Tax Return FAQs
No tax rate, threshold or penalty amount is stated anywhere in the series: those texts could not be checked from here.
Owner's decisions: promote registration only (not return filing); fee Rs 5,000 as on /pricing."""
import sys
sys.path.insert(0, "/home/user/kam/content/dnfbp-2026")
from posts import WA, a, table  # noqa: F401

DATE = "2026-11-21"
DLONG = "21 November 2026"

S_ACT4 = ("PRA: Punjab Sales Tax on Services Act 2012, Chapter IV (Registration)",
          "https://reg.pra.punjab.gov.pk/PTMS/SOP/Download/SalesTaxAct2012/Chapter%204-%20REGISTRATION.pdf")
S_ACT3 = ("PRA: Punjab Sales Tax on Services Act 2012, Chapter III (Payment and collection)",
          "https://reg.pra.punjab.gov.pk/PTMS/SOP/Download/SalesTaxAct2012/Chapter%203-%20PAYMENT%20AND%20COLLECTION%20OF%20TAX%20ON%20TAXABLE%20SERVICES.pdf")
S_RULES = ("PRA: Punjab Sales Tax on Services (Registration and De-registration) Rules 2012, with Forms PST-01, PST-02, PST-03",
           "https://reg.pra.punjab.gov.pk/ptms/SOP/Download/Rules/2-Registration%20&%20De-reg.pdf")
S_MAN = ("PRA/PRAL: PRA-Registration Module User's Manual (January 2024)",
         "https://e.pra.punjab.gov.pk/templates/PRA-Taxpayers-End-Registration-User-Manual-V0.1.pdf")
S_LOGIN = ("PRA: e-PRA portal (registration, e-Enrolment and online verification)", "https://e.pra.punjab.gov.pk/public/txplogin.xhtml")
S_ATL = ("PRA: Active Taxpayer List (Sales Tax)", "https://reg.pra.punjab.gov.pk/ActiveTaxpayer_List.aspx")
S_FAQ = ("PRA: PRA Iris Sales Tax Return FAQs", "https://e.pra.punjab.gov.pk/templates/PRA_Iris_Sales_Tax_Return_FAQs.pdf")
S_PRA = ("Punjab Revenue Authority", "https://pra.punjab.gov.pk/")

SL = dict(proc="pra-registration-process-online-punjab", docs="pra-registration-documents-required",
          fee="pra-registration-fee-punjab", cert="pra-registration-certificate-pst-03",
          ver="pra-ntn-verification-taxpayer-profile-inquiry", who="who-must-register-with-pra-punjab",
          comp="pra-compulsory-registration-notice-e-enrolment", sole="pra-registration-sole-proprietor-punjab",
          fbr="pra-registration-fbr-registered-business-p-ntn", chg="pra-registration-change-suspension-deregistration")
B = {k: "/blogs/" + v for k, v in SL.items()}
SVC = "/pra-registration"
X = {"ntn": "/ntn-registration", "pricing": "/pricing", "sole": "/blogs/sole-proprietor-tax-services-fees-pakistan",
     "strn": "/sales-tax-registration", "dual": "/blogs/double-registration-fbr-provincial-sales-tax-pakistan",
     "which": "/blogs/provincial-sales-tax-services-which-authority-applies-pakistan",
     "pst": "/blogs/punjab-sales-tax-services-pakistan", "cross": "/blogs/provincial-sales-tax-freelancers-cross-province-pakistan"}

FEE = "Rs 5,000 professional fee for PRA registration (published on /pricing). PRA itself charges nothing: rule 15 makes registration free. NTN first, if you have none: Rs 2,000."
TRUST = "Kamboh Associates is FBR Registered, works from Awan Town, Lahore and online, and replies within office hours (Mon–Sat 9:00–18:00, Friday till 12:30)."


def SERIES(cur):
    items = [("proc", "step-by-step on IRIS"), ("docs", "documents"), ("fee", "fee"), ("cert", "certificate"),
             ("ver", "verification"), ("who", "who must register"), ("comp", "compulsory notice"),
             ("sole", "sole proprietors"), ("fbr", "already on FBR"), ("chg", "changes and de-registration")]
    links = " &middot; ".join(a(B[k], t) for k, t in items if k != cur)
    return f'<p class="tf-primary"><strong>PRA registration guides:</strong> {links} &middot; {a(SVC, "PRA registration service")}</p>'


def svc(h2, intro, items, risks, hook, btn="Get my PRA registration done"):
    return dict(h2=h2, intro=intro, items=items, risks=risks, hook=hook, fee=FEE, btn=btn)


COMMON = dict(category="PRA Registration", icon="🏛️",
              cta_h="PRA registration, done for you",
              cta_p="Rs 5,000 professional fee. PRA charges nothing. Send your CNIC and a line about your service on WhatsApp.")


def post(**kw):
    p = dict(COMMON)
    p.update(kw)
    return p
