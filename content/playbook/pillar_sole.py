"""A2 pillar: sole proprietor lifecycle hub (playbook, 22 Nov 2026).
Facts reused from the already fact-checked sole proprietor series (ITO 2001 amended to 30.06.2026: ss.21, 116, 118, 147, 149, 153, 155,
161, 165, 174, 181, 182) and the PRA series (PRA Registration Rules 2012). Build:
PYTHONPATH=content/playbook POSTS_MODULE=pillar_sole python3 content/dnfbp-2026/build.py"""
import sys
sys.path.insert(0, "/home/user/kam/content/dnfbp-2026")
from posts import WA, a, table  # noqa: F401

DATE = "2026-11-22"
DLONG = "22 November 2026"
S_ITO = ("FBR: Income Tax Ordinance, 2001 (amended up to 30.06.2026)", "https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf")
S_IRIS = ("FBR IRIS portal", "https://iris.fbr.gov.pk/")
S_FBR = ("Federal Board of Revenue", "https://www.fbr.gov.pk/")
S_PRA = ("PRA: Punjab Sales Tax on Services (Registration and De-registration) Rules 2012", "https://reg.pra.punjab.gov.pk/ptms/SOP/Download/Rules/2-Registration%20&%20De-reg.pdf")

L = {k: "/blogs/" + v for k, v in dict(
    reg="sole-proprietorship-registration-pakistan", regl="sole-proprietorship-registration-lahore",
    cmp="sole-proprietorship-vs-partnership-vs-pvt-ltd-lahore", rec="sole-proprietor-records-books-fbr-pakistan",
    cash="sole-proprietor-cash-payment-rules-section-21-pakistan", wht="sole-proprietor-withholding-tax-duties-pakistan",
    adv="sole-proprietor-advance-tax-pakistan", ret="sole-proprietor-tax-return-pakistan-2026",
    ws="sole-proprietor-wealth-statement-pakistan", fee="sole-proprietor-tax-services-fees-pakistan",
    close="close-sole-proprietorship-remove-business-ntn-pakistan", pra="pra-registration-sole-proprietor-punjab",
    cal="pakistan-tax-calendar-2026-27").items()}

BODY = f"""
<p class="tf-primary"><strong>This is the hub of our sole proprietor series.</strong> Each stage below gives the rule in short and links to the full guide.</p>

<h2 id="what">What a Sole Proprietorship Is for Tax</h2>
<p>A sole proprietorship is one person running a business in their own name. It has no legal identity separate from the owner, so for income tax the business is simply part of the owner: the owner's CNIC is the NTN, the business profit is the owner's income, and the business bank balances, stock and receivables sit in the owner's wealth statement. There is no SECP-style register for it. In practice it is recognised through the owner's income tax registration under section 181 of the Income Tax Ordinance, with the business name, address and branches added on IRIS.</p>
<p>That single fact shapes everything else on this page: every obligation below is the owner's personal obligation. If you are still deciding between this and a partnership or company, read {a(L["cmp"], "sole proprietorship vs partnership vs private limited")}.</p>

<h2 id="stages">The Five Stages at a Glance</h2>
{table(["Stage", "What you must do", "Law", "Full guide"], [
    ["1. Start", "IRIS profile, add business name, address and branches (Form 181); business bank account", "s.181", a(L["reg"], "Registration")],
    ["2. Register for indirect tax if it applies", "FBR sales tax (STRN) for goods; PRA/SRB/KPRA for services", "Sales Tax Act; PRA Act s.25", a(L["pra"], "PRA for sole proprietors")],
    ["3. Run the business", "Keep records 6 years; pay by bank above the s.21 limits; deduct and report withholding where required; quarterly advance tax if liable", "ss.21, 147, 149, 153, 155, 165, 174", a(L["rec"], "Records")],
    ["4. File every year", "Return with business accounts, wealth statement and reconciliation", "ss.114, 116, 118", a(L["ret"], "Return")],
    ["5. Close", "File the last return; deregister the business at the Regional Tax Office; keep records", "s.174; FBR guidance", a(L["close"], "Closing")],
])}

<h2 id="start">Stage 1: Starting</h2>
<p>Registration has four practical steps. Use (or create) the owner's IRIS profile. Add the business through Form 181: business name, address and every branch. Open a bank account in the business name and add it to IRIS. Then check whether the trade needs its own licence. Our {a(L["reg"], "registration guide")} walks through each screen; Lahore owners can read the {a(L["regl"], "Lahore version")} for local offices.</p>
<p>Two choices made here follow you for years: the business address (it appears on every later registration, including PRA, which copies your FBR record) and the bank account (it becomes the evidence for the section 21 payment rules in Stage 3).</p>

<h2 id="indirect">Stage 2: Sales Tax Registration, If It Applies</h2>
<p>Income tax registration does not cover sales tax. Goods and services are taxed by different authorities:</p>
<ul>
<li><strong>Goods:</strong> FBR sales tax registration (STRN). See {a("/sales-tax-registration", "sales tax registration")}.</li>
<li><strong>Services in Punjab:</strong> the Punjab Revenue Authority. Section 25 of the Punjab Sales Tax on Services Act 2012 requires anyone providing a taxable service from a place of business in Punjab to register; a sole proprietor registers in the Individual category under the owner's CNIC. Registration itself is free under rule 15 of PRA's 2012 Registration Rules. See {a(L["pra"], "PRA registration for sole proprietors")}.</li>
<li><strong>Property dealers and some accountants:</strong> DNFBP registration with FBR under the AML regime. See {a("/dnfbp-compliance-services", "DNFBP compliance")}.</li>
</ul>

<h2 id="run">Stage 3: Running the Business Year-Round</h2>
<h3>Records</h3>
<p>Section 174 requires the prescribed accounts, documents and records to be kept in Pakistan for six years after the end of the tax year they relate to, and longer while any proceeding is pending. Without a receipt or other evidence, the Commissioner can disallow a deduction. Details: {a(L["rec"], "records and books")}.</p>
<h3>How you pay</h3>
<p>Three clauses of section 21 bite cash businesses. Clause (l) disallows expenditure under one account head above Rs 250,000 in aggregate paid other than by crossed banking instrument or verifiable online transfer from the business account (with listed exceptions). Clause (q) disallows 10% of purchases from persons without an NTN. Clause (s) disallows 50% of expenditure claimed for a sale where more than Rs 200,000 on a single invoice was received other than through a banking channel or digital means. Worked examples: {a(L["cash"], "section 21 cash rules")}.</p>
<h3>Withholding you must deduct</h3>
<p>A sole proprietor deducts tax when paying salaries (s.149), when paying gross rent of Rs 1.5 million or more in a year (s.155), and on payments for goods, services and contracts once turnover reached Rs 100 million in any preceding tax year (s.153). Deductions are reported in quarterly statements under section 165, due by 20 April, 20 July, 20 October and 20 January. Section 161 makes the person who fails to deduct or deposit personally liable. Details: {a(L["wht"], "withholding duties")}.</p>
<h3>Advance tax</h3>
<p>Under section 147, an individual whose latest assessed taxable income (excluding salary and income under final or non-adjustable deductions) is Rs 1 million or more pays advance tax each quarter, on or before 15 September, 15 December, 15 March and 15 June. Each instalment is a quarter of last year's assessed tax less adjustable tax paid in that quarter. An estimate can be filed if this year's tax will be lower. Details: {a(L["adv"], "advance tax")}.</p>

<h2 id="file">Stage 4: Filing Every Year</h2>
<p>The return includes the business's profit and loss, the wealth statement and the wealth reconciliation. For individuals the due date under section 118 is 30 September after the tax year ends; for tax year 2026 FBR extended it to 31 October 2026. Under section 116(2) every resident individual filing a return must file the wealth statement and reconciliation; for a sole proprietor that means business assets, stock, receivables, bank balances and business debts appear as the owner's own. A missing statement or reconciliation carries a penalty under section 182 of 0.1% of taxable income per week or Rs 100,000, whichever is higher.</p>
<p>Full guides: {a(L["ret"], "the sole proprietor return")} and {a(L["ws"], "the sole proprietor wealth statement")}. For every due date in the year, see the {a(L["cal"], "Pakistan tax calendar 2026-27")}.</p>

<h2 id="close">Stage 5: Closing Down</h2>
<p>FBR's guidance is that discontinuing a business and deregistering it cannot be done through the online Form 181; the owner visits the Regional Tax Office with the relevant documents. The return for the closing year must still be filed, with closing stock, assets and bank balances shown in the wealth statement. Records stay for six years under section 174. If the business was registered with PRA, de-registration there is a separate application on Form PST-02, also free under rule 15. Details: {a(L["close"], "closing a sole proprietorship")}.</p>

<h2 id="mistakes">The Mistakes We See Most</h2>
<ol>
<li><strong>Mixing business and personal money</strong> in one account, which makes the section 21 evidence and the wealth reconciliation hard to defend.</li>
<li><strong>Cash purchases above the section 21 limits</strong>, disallowed at assessment.</li>
<li><strong>Not deducting withholding</strong> once the section 153 turnover threshold is crossed, which makes the owner personally liable (s.161).</li>
<li><strong>Treating FBR registration as covering sales tax on services</strong>; PRA, SRB or KPRA registration is separate.</li>
<li><strong>Closing the shop but not the registration</strong>, so returns stay due.</li>
</ol>
"""

SOLE = dict(
    slug="sole-proprietor-complete-guide-pakistan",
    title="Sole Proprietor in Pakistan: Complete Tax Guide (2026)",
    h1="Sole Proprietor in Pakistan: The Complete Tax Guide, From Registration to Closing (2026)",
    crumb="Sole Proprietor Complete Guide",
    description="Every tax duty of a sole proprietor in Pakistan in one place: registration, sales tax, records, cash rules, withholding, advance tax, return and closing.",
    keywords="sole proprietor tax pakistan, sole proprietorship tax guide pakistan, sole proprietor fbr requirements, sole proprietor compliance pakistan, sole proprietorship complete guide",
    category="Sole Proprietors", icon="🏪", read="14 min read",
    banner="One person, one CNIC, every obligation: the whole sole proprietor tax life on one page, with the law behind each step.",
    tldr=("A sole proprietorship has no legal identity separate from its owner, so every tax duty is the owner's. Register the business on IRIS through "
          "Form 181 (s.181) with a business bank account; register separately for sales tax if it applies (FBR for goods, PRA/SRB/KPRA for services). "
          "Keep records for six years (s.174), pay by bank above the section 21 limits, deduct and report withholding where required (ss.149, 153, 155, 165), "
          "pay quarterly advance tax if last year's income was Rs 1 million or more (s.147), and file the return with the wealth statement every year "
          "(ss.116, 118). Closing needs a visit to the Regional Tax Office."),
    lead=("Most sole proprietors learn their obligations one notice at a time. This page puts the whole cycle in order, from the day you register to the day "
          "you close, with the section of the Income Tax Ordinance behind each step and a link to our full guide on it."),
    answers={
        "what": "A business owned and run by one person, taxed as the owner's own income under the owner's CNIC-based NTN.",
        "stages": "Start, sales tax registration if it applies, run the business, file every year, and close properly.",
        "start": "Add the business to your IRIS profile through Form 181 and open a bank account in the business name.",
        "indirect": "Income tax registration does not cover sales tax: goods register with FBR, services with PRA, SRB or KPRA.",
        "run": "Keep records six years, pay by bank above the section 21 limits, deduct withholding where required, and pay advance tax if liable.",
        "file": "File the return with business accounts, wealth statement and reconciliation by the section 118 due date.",
        "close": "Deregister at the Regional Tax Office, file the closing-year return, and keep records for six years.",
    },
    svc=dict(h2="Your Sole Proprietorship, Handled All Year",
             intro="We take each stage off your hands: registration, the right sales tax registration, year-round withholding and advance tax, and the annual return.",
             items=["Sole proprietorship registration on IRIS with business name, branches and bank account",
                    "FBR sales tax (STRN) or PRA registration where it applies",
                    "Records set-up that satisfies sections 21 and 174",
                    "Quarterly advance tax and withholding statements where required",
                    "Annual return, wealth statement and reconciliation"],
             risks=["Section 21 disallowances on cash payments raise your tax at assessment",
                    "Missed withholding makes you personally liable under section 161",
                    "A missing wealth statement carries a penalty of at least Rs 100,000 (s.182)"],
             hook="Run a business in your own name?",
             fee="Sole proprietorship registration Rs 5,000; sole proprietor return Rs 5,000; NTN Rs 2,000; STRN Rs 3,000; PRA registration Rs 5,000 (all published on /pricing). Anything else is a fixed fee confirmed before work starts.",
             btn="Get my business compliant"),
    faqs=[
        ("Does a sole proprietorship need SECP registration?", "No. There is no SECP-style register for a sole proprietorship; it is recognised through the owner's income tax registration under section 181, with the business added on IRIS."),
        ("Is a sole proprietor's business income taxed separately?", "No. The business has no separate identity, so its profit is the owner's income and its assets and debts go in the owner's wealth statement."),
        ("Do I need a separate bank account for the business?", "It is the practical way to meet the section 21 payment rules and to explain the wealth reconciliation; add it to your IRIS profile."),
        ("When must a sole proprietor deduct withholding tax?", "On salaries (s.149), on gross rent of Rs 1.5 million or more a year (s.155), and on goods, services and contracts once turnover reached Rs 100 million in any preceding tax year (s.153)."),
        ("Do I need PRA registration as a sole proprietor?", "If you provide a taxable service from a place of business in Punjab, section 25 of the Punjab Sales Tax on Services Act requires it. Registration is free under rule 15."),
        ("How do I close my sole proprietorship?", "Visit your Regional Tax Office with the documents (it cannot be done through online Form 181), file the closing-year return and keep records for six years."),
    ],
    sources=[S_ITO, S_IRIS, S_FBR, S_PRA],
    related=[(L["reg"], "Sole proprietorship registration"), (L["ret"], "Sole proprietor tax return"), (L["fee"], "Sole proprietor services and fees")],
    cta_h="Sole proprietor compliance, done for you",
    cta_p="Registration, sales tax or PRA registration, withholding and the annual return, at published fees.",
    wa_text="Assalam o Alaikum, sole proprietorship ka tax kaam karwana hai.",
    body=BODY,
)

POSTS = [SOLE]
