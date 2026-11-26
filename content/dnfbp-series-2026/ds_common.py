"""DNFBP registration series 2: 10 guides (facts checked 26 November 2026), each on a topic no existing page targets.
Official texts read in full on that date (all FBR unless stated):
- FBR AML/CFT Regulations for DNFBPs 2020, S.R.O. 924(I)/2020 (regs 1-16) and the amendments in S.R.O. 1439(I)/2026 (27 Aug 2026)
- AML/CFT Sanctions Rules 2020, S.R.O. 950(I)/2020 (Ministry of Finance); Counter-measures for High Risk Jurisdictions Rules 2020, S.R.O. 951(I)/2020
- FBR FAQs on AML/CFT (February 2023), Q1-56; Condition No. 2 (2022) for Public Sector Development Departments (28 Feb 2022)
- Short Guidance for Real Estate Agents (Sept 2021) and for DPMS; S.R.O. 1497(I)/2026 (jurisdiction); Summarized NRA 2023 for DNFBPs
- FBR AML/CFT web pages: Introduction, Conditionalities, TFS Screening, DNFBP Mobile Application (portal and app links)
Condition No. 3 (2022) is a scanned PDF; its content is taken only from FBR FAQ Q29, which quotes it.
No DNFBP fee is on /pricing, so the service fee is "fixed fee confirmed before work starts"; NTN Rs 2,000 and sole proprietorship
registration Rs 5,000 are the published figures used."""
import sys
sys.path.insert(0, "/home/user/kam/content/dnfbp-2026")
from posts import WA, a, table  # noqa: F401

DATE = "2026-11-26"
DLONG = "26 November 2026"

S_REG = ("FBR: AML/CFT Regulations for DNFBPs 2020 (S.R.O. 924(I)/2020)", "https://download1.fbr.gov.pk/SROs/202092917976805SRO9242020.pdf")
S_1439 = ("FBR: S.R.O. 1439(I)/2026, amendments to the DNFBP Regulations (27 August 2026)",
          "https://download1.fbr.gov.pk/Docs/2026916149427921SRO1439-2026AmmendmentsinSRO924.pdf")
S_SANC = ("Ministry of Finance: AML/CFT Sanctions Rules 2020 (S.R.O. 950(I)/2020)",
          "https://download1.fbr.gov.pk/Docs/202010151510533067AML-CFT-Sanction-Rules-2020-SRO-NO-950I-2020.pdf")
S_HRJ = ("Ministry of Finance: Counter-measures for High Risk Jurisdictions Rules 2020 (S.R.O. 951(I)/2020)",
         "https://download1.fbr.gov.pk/Docs/2020101515105713464Counter-measures-for-High-Risk-Jurisdictions-Rules-2020REC19and23.3forDNFBPS.pdf")
S_FAQ = ("FBR: Frequently Asked Questions on AML/CFT for DNFBPs (February 2023)",
         "https://download1.fbr.gov.pk/Docs/20233281432019788FrequentlyAskedQuestions(FAQs)-February2023.pdf")
S_C2 = ("FBR: Condition No. 2 (2022) for Public Sector Development Departments/Authorities",
        "https://download1.fbr.gov.pk/Docs/20222281721234352ConditionNumber2.pdf")
S_C3 = ("FBR: Condition No. 3 (2022) for Sole Proprietorship Concerns", "https://download1.fbr.gov.pk/Docs/2022102718101732543condition3.pdf")
S_COND = ("FBR: Conditionalities on DNFBPs", "https://www.fbr.gov.pk/dnfbp-conditionalities/152366/163236")
S_1497 = ("FBR: S.R.O. 1497(I)/2026, jurisdiction of DNFBP authorities",
          "https://download1.fbr.gov.pk/Docs/2026916149312406SRO1497-2026JurisdictionofDNFBPAuthorities.pdf")
S_REA = ("FBR: Short Guidance on AML/CFT Obligations for Real Estate Agents", "https://download1.fbr.gov.pk/Docs/2021915091332570ShortGuidanceForREAs.pdf")
S_DPMS = ("FBR: Short Guidance on AML/CFT Obligations for DPMS", "https://download1.fbr.gov.pk/Docs/2022826883123108ShortGuidance-DPMS.pdf")
S_NRA = ("FBR: Summarized National Risk Assessment 2023 for DNFBPs", "https://download1.fbr.gov.pk/Docs/20245271555327769NationalRiskAssessment2023.pdf")
S_TFS = ("FBR: Targeted Financial Sanctions Screening (DNFBPs)", "https://www.fbr.gov.pk/Targeted-financial-sanctions-screening/152366/152886")
S_APP = ("FBR: DNFBP Mobile Application and portal links", "https://www.fbr.gov.pk/dnfbp-mobile-application/152366/152959")
S_PORTAL = ("FBR: DNFBP portal login (IRIS)", "https://iris.fbr.gov.pk/infosys/public/txplogin.xhtml")
S_GOAML = ("FMU: goAML portal", "https://goamlweb.fmu.gov.pk/PRD/Home")
S_UN = ("United Nations: Security Council Consolidated List", "https://www.un.org/securitycouncil/content/un-sc-consolidated-list")
S_NACTA = ("NACTA: Proscribed organizations", "https://nacta.gov.pk/proscribed-organizations-3/")
S_INTRO = ("FBR: AML/CFT for DNFBPs (introduction)", "https://www.fbr.gov.pk/introduction-aml-cft/152366/152367")

SL = dict(sro="sro-1439-2026-dnfbp-regulations-amendment-pakistan",
          dev="housing-society-developer-dnfbp-registration-noc-pakistan",
          cert="dnfbp-registration-certificate-status-pakistan",
          sole="dnfbp-registration-sole-proprietor-pakistan",
          docs="dnfbp-registration-documents-required-pakistan",
          pep="politically-exposed-persons-pep-dnfbp-pakistan",
          ubo="beneficial-owner-ubo-dnfbp-customer-pakistan",
          tfs="targeted-financial-sanctions-screening-dnfbp-pakistan",
          pen="dnfbp-penalty-aml-cft-sanctions-rules-pakistan",
          nra="national-risk-assessment-2023-dnfbp-real-estate-jewellers")
B = {k: "/blogs/" + v for k, v in SL.items()}
X = {"svc": "/dnfbp-compliance-services", "main": "/blogs/dnfbp-registration-pakistan", "goaml": "/blogs/goaml-registration-dnfbp-pakistan",
     "prog": "/blogs/aml-cft-compliance-programme-dnfbp-pakistan", "rea": "/blogs/real-estate-agent-dnfbp-registration-aml-pakistan",
     "jew": "/blogs/jeweller-dnfbp-registration-aml-pakistan", "acc": "/blogs/accountant-dnfbp-registration-aml-pakistan",
     "lhr": "/blogs/dnfbp-registration-lahore-punjab", "isb": "/blogs/dnfbp-registration-islamabad-rawalpindi",
     "khi": "/blogs/dnfbp-registration-karachi-sindh", "pew": "/blogs/dnfbp-registration-peshawar-kp", "qta": "/blogs/dnfbp-registration-quetta-balochistan",
     "ntn": "/ntn-registration", "sole": "/blogs/sole-proprietor-complete-guide-pakistan", "solefee": "/blogs/sole-proprietor-tax-services-fees-pakistan", "pricing": "/pricing", "pra": "/pra-registration"}

NAMES = {"sro": "2026 amendments", "dev": "developers and societies", "cert": "certificate and status", "sole": "sole proprietors",
         "docs": "documents", "pep": "PEPs", "ubo": "beneficial owners", "tfs": "sanctions screening", "pen": "penalties", "nra": "NRA 2023 risk"}
PICK = {"sro": ["dev", "docs", "nra"], "dev": ["sro", "cert", "ubo"], "cert": ["docs", "sole", "pen"], "sole": ["docs", "cert", "pen"],
        "docs": ["sole", "ubo", "pep"], "pep": ["ubo", "tfs", "docs"], "ubo": ["pep", "docs", "dev"], "tfs": ["pep", "pen", "nra"],
        "pen": ["cert", "tfs", "sro"], "nra": ["sro", "tfs", "pep"]}


def SERIES(cur):
    links = " &middot; ".join(a(B[k], NAMES[k]) for k in PICK[cur])
    return f'<p class="tf-primary"><strong>More DNFBP guides:</strong> {links} &middot; {a(X["main"], "complete DNFBP guide")}</p>'


def svc(h2, intro, items, risks, hook, btn, topic):
    return dict(h2=h2, intro=intro, items=items, risks=risks, hook=hook, btn=btn, compact=True,
                fee=f"Fixed fee for {topic}, confirmed before work starts. If you need an NTN first, that is Rs 2,000 (see /pricing).")


COMMON = dict(category="DNFBP & AML", icon="🛡️", cta_h="DNFBP registration and compliance, done for you")


def post(**kw):
    p = dict(COMMON)
    p.update(kw)
    return p


def about(*extra):
    return [{"@type": "Legislation", "name": "FBR Anti Money Laundering and Countering Financing of Terrorism Regulations for DNFBPs, 2020 (S.R.O. 924(I)/2020)",
             "legislationJurisdiction": "PK", "legislationDate": "2020-09-29", "url": S_REG[1]}] + list(extra)
