"""Sole proprietor series, batch 2 (4 posts). Facts checked 10 November 2026: Income Tax Ordinance 2001 amended to
30.06.2026 (ss.20, 21, 114, 116, 118, 147, 174, 182), fees as published on /pricing, office details from /contact."""
from posts import WA, a, table, S_IRIS

DATE = "2026-11-10"
DLONG = "10 November 2026"

S_ITO = ("FBR: Income Tax Ordinance, 2001 (amended up to 30.06.2026)", "https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf")
S_FBR = ("Federal Board of Revenue", "https://www.fbr.gov.pk/")
S_1497 = ("FBR: S.R.O. 1497(I)/2026 (names the Lahore tax offices)", "https://download1.fbr.gov.pk/Docs/2026916149312406SRO1497-2026JurisdictionofDNFBPAuthorities.pdf")

F_SLUG = "sole-proprietor-tax-services-fees-pakistan"
L_SLUG = "sole-proprietorship-registration-lahore"
WS_SLUG = "sole-proprietor-wealth-statement-pakistan"
CA_SLUG = "sole-proprietor-cash-payment-rules-section-21-pakistan"
B = {k: "/blogs/" + v for k, v in dict(fees=F_SLUG, lhr=L_SLUG, ws=WS_SLUG, cash=CA_SLUG, reg="sole-proprietorship-registration-pakistan",
     iris="add-business-to-ntn-iris-sole-proprietor", adv="sole-proprietor-advance-tax-pakistan", wht="sole-proprietor-withholding-tax-duties-pakistan",
     rec="sole-proprietor-records-books-fbr-pakistan", close="close-sole-proprietorship-remove-business-ntn-pakistan",
     ret="sole-proprietor-tax-return-pakistan-2026").items()}
X = {"pricing": "/pricing", "notice": "/fbr-notice-defense", "contact": "/contact", "lahore": "/tax-consultant-lahore", "ntnlhr": "/ntn-registration-lahore",
     "exp": "/blogs/business-expense-deductible-pakistan", "wsg": "/blogs/wealth-statement-guide-pakistan-2026"}
SERIES = (f'<p class="tf-primary"><strong>Sole proprietor guides:</strong> {a(B["reg"], "registration")} &middot; {a(B["fees"], "our services and fees")} &middot; '
          f'{a(B["ws"], "wealth statement")} &middot; {a(B["cash"], "cash payment rules")} &middot; {a(B["adv"], "advance tax")} &middot; {a(B["wht"], "withholding")} &middot; {a(B["rec"], "records")}</p>')
OFFICE = "Shop No 34, Rizwan Block Market, opposite Rizwan Park, Awan Town, Lahore 54660"
HOURS = "Monday to Saturday 9:00 to 18:00, Friday 9:00 to 12:30, Sunday closed"
FEES = table(["Service", "Fee (published on our pricing page)"], [
    ["Sole proprietorship registration (IRIS profile, business added, bank account linked)", "Rs 5,000"],
    ["NTN registration only (includes ATL guidance)", "Rs 2,000"],
    ["Sole proprietor annual income tax return", "Rs 5,000"],
    ["Wealth statement preparation", "Rs 2,000"],
    ["Withholding tax statements (Sections 149/165)", "Rs 3,000 a month"],
    ["FBR notice response (Sections 111, 114, 122, 177)", "From Rs 5,000"],
    ["Private limited company registration, if you later convert", "From Rs 15,000"],
])

# ───────────────────────────── Services & fees ─────────────────────────────
FEESP = dict(
    slug=F_SLUG,
    svc=dict(h2="Start With a Free Assessment", intro="Send us one message describing your business. We reply with exactly which of the services above you need, the total fee, and what documents to send.",
             hook="Not sure which services your business needs?", fee="Fees as published: registration Rs 5,000; annual return Rs 5,000; wealth statement Rs 2,000; withholding Rs 3,000 a month.",
             btn="Get my free assessment", items=["A one-message assessment of your registration, return, advance tax and withholding position", "A written quote with the published fees before any work starts", "One point of contact for the whole year", "Reminders before each deadline that applies to you"],
             risks=["Late return: 0.1% of tax per day under Section 182, minimum Rs 40,000", "Rs 25,000 surcharge to rejoin the Active Taxpayers List after a late return", "Missed advance tax: 12% a year default surcharge"]),
    title="Sole Proprietor Tax Services in Pakistan: What We Do & Fees",
    h1="Tax Services for Sole Proprietors in Pakistan: What Your Business Needs Each Year, and What It Costs",
    crumb="Sole Proprietor Services & Fees",
    description="Every tax service a sole proprietor needs, from registration and returns to advance tax, withholding and notices, with published fees and a calendar.",
    keywords="sole proprietor tax services Pakistan, tax consultant for sole proprietor, sole proprietor return fee, business tax return fee Pakistan, tax consultant Lahore small business",
    category="Sole Proprietorship",
    icon="🧰",
    read="11 min read",
    banner="Most small businesses need the same few tax services every year. Knowing which ones apply, and when, is what keeps penalties away.",
    tldr=("A sole proprietor in Pakistan typically needs: registration on IRIS with the business added (once), an annual income tax return with wealth statement "
          "(every year, due 30 September for individuals under Section 118), quarterly advance tax once latest assessed income reaches Rs 1 million (Section 147), "
          "withholding statements once you employ staff, pay rent of Rs 1.5 million a year or cross Rs 100 million turnover, and help with notices when they arrive. "
          "Our published fees are Rs 5,000 for sole proprietorship registration, Rs 5,000 for the annual return, Rs 2,000 for a wealth statement, Rs 3,000 a month "
          "for withholding statements, and from Rs 5,000 for a notice response."),
    lead=("Owners of small businesses often pay for tax help one emergency at a time: a notice here, a late return there. That is the most expensive way to do it. "
          "This guide lists what a sole proprietorship actually needs across a year, which of those you can do yourself, and where professional help pays for "
          "itself, with the fees we publish."),
    body=f"""
{SERIES}

<h2 id="what-you-need">What a Sole Proprietorship Needs, Service by Service</h2>
{table(["Service", "Who needs it", "How often", "Legal basis"], [
    ["Registration and business details on IRIS", "Every sole proprietor", "Once, then updates", "Section 181; Form 181"],
    ["Income tax return with wealth statement", "Every sole proprietor with taxable income or otherwise required to file", "Yearly, by 30 September", "Sections 114, 116, 118"],
    ["Advance tax", "Latest assessed income (excluding salary and final-tax income) of Rs 1 million or more", "Quarterly: 15 Sep, Dec, Mar, Jun", "Section 147"],
    ["Withholding on salaries", "Anyone paying salaries", "Monthly deduction; quarterly statements", "Sections 149, 165"],
    ["Withholding on rent", "Individuals paying rent of Rs 1.5 million or more a year", "Each payment; quarterly statements", "Sections 155, 165"],
    ["Withholding on suppliers", "Turnover of Rs 100 million or more in any preceding tax year", "Each payment; quarterly statements", "Sections 153, 165"],
    ["Notice replies", "Anyone who receives a notice", "As they arise", "Sections 111, 114, 122, 177 and others"],
])}

<h2 id="fees">Our Published Fees</h2>
{FEES}
<p>These are the fees shown on our {a(X['pricing'], 'pricing page')}. If your business needs something not listed, we quote a fixed fee before starting.</p>

<h2 id="diy-or-not">What You Can Do Yourself, and Where Help Pays</h2>
{table(["Task", "Do it yourself?", "Where help pays for itself"], [
    ["Creating an IRIS account", "Usually yes", "When IRIS rejects documents or the CNIC details do not match"],
    ["Adding the business through Form 181", "Often yes", "When the option is unavailable or an RTO application is needed"],
    ["Annual return and wealth statement", "Possible for very simple businesses", "When there is stock, assets, loans or more than one income source, because the wealth reconciliation must balance"],
    ["Advance tax", "Yes, if you follow the formula", "When business has slowed and a supported lower estimate could save cash"],
    ["Withholding statements", "Rarely", "Always: penalties start at Rs 10,000 even when no tax was due"],
    ["Notice replies", "Not recommended", "Always: deadlines are short and the reply shapes the outcome"],
])}

<h2 id="calendar">A Year in the Life of a Sole Proprietor's Tax File</h2>
{table(["Month", "What happens"], [
    ["July", "New tax year begins; start the year's record folders"],
    ["September", "15th: advance tax (if applicable). 30th: last year's return and wealth statement due"],
    ["October", "20th: withholding statement for July to September (if applicable)"],
    ["December", "15th: advance tax"],
    ["January", "20th: withholding statement for October to December"],
    ["March", "15th: advance tax"],
    ["April", "20th: withholding statement for January to March"],
    ["June", "15th: advance tax. 30th: year end; count stock"],
])}

<h2 id="costs-of-missing">What Missing a Step Costs</h2>
<ul>
<li><strong>Late return:</strong> 0.1% of tax payable for each day of default, up to 50%, minimum Rs 40,000 (Section 182).</li>
<li><strong>Rejoining the Active Taxpayers List after a late return:</strong> Rs 25,000 for an individual (Section 182A).</li>
<li><strong>Missing wealth statement or reconciliation:</strong> 0.1% of taxable income per week or Rs 100,000, whichever is higher (Section 182).</li>
<li><strong>Unpaid advance tax:</strong> default surcharge at 12% a year (Section 205(1A)).</li>
<li><strong>Late withholding statement:</strong> Rs 2,500 a day, minimum Rs 10,000, or Rs 50,000 if filed within 90 days after the tax was paid (Section 182).</li>
<li><strong>Records not kept:</strong> Rs 10,000 or 5% of the tax, whichever is higher (Section 182).</li>
</ul>
<p>Against these, the annual cost of doing it right is small.</p>

<h2 id="how-we-work">How We Work With Sole Proprietors</h2>
<ol>
<li><strong>Assessment:</strong> you send your CNIC and a description of the business on WhatsApp; we tell you what applies.</li>
<li><strong>Quote:</strong> a written fee from the table above, before any work.</li>
<li><strong>Documents:</strong> you send bank statements, invoices and certificates; we tell you exactly what is missing.</li>
<li><strong>Draft:</strong> we prepare the return or statement and share the figures for your approval.</li>
<li><strong>Filing:</strong> we file on IRIS and send you the acknowledgement.</li>
<li><strong>Reminders:</strong> we remind you before each deadline that applies to your business.</li>
</ol>
<p>Our office is at {OFFICE}, open {HOURS}. Most clients never need to visit: everything works over WhatsApp.</p>

<h2 id="choosing">Choosing a Tax Practitioner for Your Business</h2>
<ul>
<li>Ask for the fee in writing before work starts.</li>
<li>Ask to see the figures before anything is filed in your name.</li>
<li>Make sure you receive the acknowledgement and copies of everything filed.</li>
<li>Check that your IRIS password stays with you, or is changed after the work.</li>
<li>Prefer someone who explains which deadlines apply to you, not only the return.</li>
</ul>
""",
    faqs=[
        ("How much does it cost to register a sole proprietorship with Kamboh Associates?",
         "Our published fee for sole proprietorship registration is Rs 5,000, covering the IRIS profile, adding the business and linking the bank account. NTN registration alone is Rs 2,000."),
        ("What is your fee for a sole proprietor's tax return?",
         "Rs 5,000 for the annual return, as published on our pricing page. A separate wealth statement preparation is listed at Rs 2,000."),
        ("Do I need to visit your office?",
         "No. Most clients work with us entirely over WhatsApp. Our office in Awan Town, Lahore is open Monday to Saturday for those who prefer to visit."),
        ("Which tax services does every sole proprietor need?",
         "Registration with the business on IRIS, and an annual return with wealth statement. Advance tax and withholding depend on income, rent, staff and turnover."),
        ("What is the penalty for not filing a wealth statement?",
         "Under Section 182, 0.1% of taxable income per week or Rs 100,000, whichever is higher, for failing to furnish the wealth statement or reconciliation."),
        ("Can you handle FBR notices for my business?",
         "Yes. Notice responses start from Rs 5,000, depending on the notice and the work involved."),
        ("Do you charge before telling me what I need?",
         "No. The first assessment is free, and you receive the fee in writing before any work starts."),
        ("Can you work with businesses outside Lahore?",
         "Yes. We work with sole proprietors across Pakistan over WhatsApp."),
    ],
    sources=[S_ITO, S_IRIS, S_FBR],
    related=[(B["reg"], "Sole Proprietorship Registration"), (B["lhr"], "Sole Proprietorship in Lahore"), (B["ws"], "Sole Proprietor Wealth Statement")],
    cta_h="One Message, a Clear Answer",
    cta_p="Tell us about your business; we reply with what you need and the fee.",
    wa_text="Assalam o Alaikum, main sole proprietor hoon. Mujhe apne business ke liye tax services aur fees ki maloomat chahiye.",
)

# ───────────────────────────── Lahore ─────────────────────────────
LHRP = dict(
    slug=L_SLUG,
    svc=dict(h2="Register Your Lahore Business With Us", intro="Visit our Awan Town office or do everything on WhatsApp. Either way, your business is registered correctly the first time.",
             hook="Starting a business in Lahore?", fee="Sole proprietorship registration Rs 5,000; annual return Rs 5,000 (published fees).", btn="Register my Lahore business",
             items=["IRIS registration and the business added through Form 181", "Business bank account linked to IRIS", "Lahore RTO matters handled for you, including applications that need a visit", "Your first return and wealth statement when due", "Reminders for advance tax and withholding if they apply"],
             risks=["Mismatched names across IRIS, bank and signboard delay accounts and payouts", "Changes that need an RTO visit can take repeated trips if documents are incomplete"]),
    title="Sole Proprietorship Registration Lahore: Office Help & Fees",
    h1="Sole Proprietorship Registration in Lahore: How to Set Up Your Business, Which Tax Office Covers You, and Local Help",
    crumb="Sole Proprietorship Lahore",
    description="Register a sole proprietorship in Lahore: IRIS steps, Lahore tax offices, documents, common mistakes in local markets, and help from our Awan Town office.",
    keywords="sole proprietorship registration Lahore, register business Lahore, business NTN Lahore, tax consultant Awan Town Lahore, small business registration Lahore",
    category="Sole Proprietorship",
    icon="🏙️",
    read="10 min read",
    banner="Registering a business in Lahore is done online, but the Lahore tax offices still matter for some changes. Local help saves repeat visits.",
    tldr=("A sole proprietorship in Lahore is registered online on FBR's IRIS portal, like anywhere in Pakistan: the owner's CNIC is the NTN and the business is "
          "added through Form 181. Lahore businesses fall under one of the city's income tax offices named in FBR notifications, including RTO-I and RTO-II Lahore, "
          "the Corporate Tax Office and the Large Taxpayers' Office. Changes such as discontinuing a business, deregistration or a change of jurisdiction need a "
          "visit to your RTO. Kamboh Associates registers Lahore businesses from its Awan Town office or over WhatsApp, for a published fee of Rs 5,000."),
    lead=("Lahore has a huge number of small businesses, from shops in its markets to workshops, agencies and online stores run from home. Most start as sole "
          "proprietorships. This guide explains how registration works for a Lahore business, what differs locally, and how to avoid the mistakes we see most "
          "often in the city."),
    body=f"""
{SERIES}

<h2 id="online">Registration Is Online, Even in Lahore</h2>
<p>There is no separate Lahore registration. The process is the same national one:</p>
<ol>
<li>Create or activate your IRIS profile with your CNIC; under Section 181(4) the CNIC is your NTN.</li>
<li>Add the business name, start date, address and nature of business through Form 181.</li>
<li>Add any branches, such as a second shop or a warehouse, separately.</li>
<li>Open a business bank account and add it to IRIS.</li>
</ol>
<p>Our national guide to {a(B['reg'], 'sole proprietorship registration')} explains each step, and our {a(B['iris'], 'Form 181 guide')} covers the form itself.</p>

<h2 id="offices">Which Lahore Tax Office Covers You</h2>
<p>FBR assigns each taxpayer to an income tax office. FBR's notifications name the Lahore offices, including <strong>RTO-I Lahore</strong>, <strong>RTO-II Lahore</strong>, the <strong>Corporate Tax Office Lahore</strong> and the <strong>Large Taxpayers' Office Lahore</strong>. Most sole proprietors fall under one of the two RTOs. Your office is shown in your IRIS profile; check it before you write to FBR or plan a visit.</p>
<p>Your office matters for three reasons:</p>
<ul>
<li>Notices about your returns come from it.</li>
<li>Changes FBR does not allow online, such as discontinuing a business or deregistration, are made there.</li>
<li>Applications and replies should be addressed to it, or they are delayed.</li>
</ul>
<p>For addresses and a wider view of FBR's presence in the city, see our {a(X['ntnlhr'], 'NTN registration in Lahore')} page.</p>

<h2 id="markets">Lahore Situations We See Often</h2>
{table(["Business", "What to watch"], [
    ["Shop in a large market with a family partner informally involved", "If two people genuinely own the business, it is a partnership (AOP), not a sole proprietorship. Decide before registering."],
    ["Two shops in different markets", "Register one business with two branches, each with its own address."],
    ["Home-based online store", "Use your home address as the business address and register before opening marketplace and courier accounts."],
    ["Workshop or small unit in an industrial area", "Keep the electricity and premises documents; they support the business address and expenses."],
    ["Agency or consultancy working from a shared office", "Use the shared office address with the landlord's permission letter."],
])}

<h2 id="documents">Documents to Bring or Send</h2>
<ul>
<li>Original CNIC (and a copy for any RTO visit).</li>
<li>Rent agreement or ownership document for the premises, and a recent utility bill.</li>
<li>Business name exactly as it will appear on the signboard and bank account.</li>
<li>Start date of the business and a short description of the activity.</li>
<li>Bank account details, once opened.</li>
</ul>

<h2 id="visit">Visiting Our Lahore Office</h2>
<p>Our office is at <strong>{OFFICE}</strong>, open {HOURS}. You can bring your documents and leave with your business registered on IRIS in the same visit when the IRIS profile and documents are in order. If you prefer, send everything on WhatsApp instead; most Lahore clients never need to come in.</p>

<h2 id="after">After Registration in Lahore</h2>
<ul>
<li><strong>Annual return</strong> with wealth statement by 30 September after each tax year.</li>
<li><strong>Advance tax</strong> quarterly once your latest assessed income reaches Rs 1 million; see our {a(B['adv'], 'advance tax guide')}.</li>
<li><strong>Withholding</strong> if you employ staff, pay rent of Rs 1.5 million or more a year, or cross Rs 100 million turnover; see our {a(B['wht'], 'withholding guide')}.</li>
<li><strong>Records</strong> for six years; see our {a(B['rec'], 'records guide')}.</li>
</ul>

<h2 id="moving">Moving Your Business Within or Into Lahore</h2>
<p>A new address within your current office's area is updated through Form 181. Moving to Lahore from another city, or between offices, can change your jurisdiction, which FBR lists among changes that need an RTO visit. Apply early so notices do not keep going to the old office.</p>
""",
    faqs=[
        ("How do I register a sole proprietorship in Lahore?",
         "Online on FBR's IRIS portal: your CNIC is your NTN, and you add the business through Form 181 with its name, address, start date and branches."),
        ("Which FBR office covers my Lahore business?",
         "Most sole proprietors fall under RTO-I or RTO-II Lahore. Your office is shown in your IRIS profile."),
        ("Do I need to visit an FBR office to register?",
         "No. Registration is online. Visits are needed only for changes FBR does not allow online, such as discontinuing a business or a change of jurisdiction."),
        ("Where is Kamboh Associates' office in Lahore?",
         f"{OFFICE}. It is open {HOURS}."),
        ("What does registration cost?",
         "FBR charges no fee for IRIS registration. Our published fee for registering a sole proprietorship is Rs 5,000."),
        ("I run two shops in different Lahore markets. How do I register?",
         "Register one business on your NTN and add the second shop as a branch with its own address."),
        ("My brother and I run the shop together. Is it a sole proprietorship?",
         "If you both genuinely own it, it is a partnership (AOP), which registers separately. A sole proprietorship has one owner."),
    ],
    sources=[S_ITO, S_IRIS, S_1497],
    related=[(B["reg"], "Sole Proprietorship Registration"), (B["fees"], "Services & Fees"), (X["lahore"], "Tax Consultant Lahore")],
    cta_h="Lahore Business? Register It Properly",
    cta_p="Visit our Awan Town office or send your documents on WhatsApp.",
    wa_text="Assalam o Alaikum, main Lahore mein business shuru kar raha hoon. Sole proprietorship registration karwani hai.",
)

# ───────────────────────────── Wealth statement ─────────────────────────────
WSP = dict(
    slug=WS_SLUG,
    svc=dict(h2="Let Us Prepare Your Wealth Statement", intro="A sole proprietor's wealth statement is where business and personal figures meet. We prepare it so it reconciles, line by line.",
             hook="Wealth statement not balancing?", fee="Wealth statement Rs 2,000; sole proprietor annual return Rs 5,000 (published fees).", btn="Prepare my wealth statement",
             items=["Business assets, stock, receivables and payables taken from your records", "Drawings and household spending worked into the reconciliation", "Opening figures matched to last year's statement", "Revised statement prepared where an earlier year was wrong, before a notice arrives"],
             risks=["Penalty of 0.1% of taxable income per week or Rs 100,000, whichever is higher, for a missing statement or reconciliation", "Unexplained increases in wealth can be treated as income"]),
    title="Sole Proprietor Wealth Statement: Capital, Stock & Drawings",
    h1="Wealth Statement for Sole Proprietors: How Business Capital, Stock and Drawings Fit In",
    crumb="Sole Proprietor Wealth Statement",
    description="How a sole proprietor's wealth statement works under Section 116: business capital, stock, receivables, drawings, reconciliation, revisions, penalties.",
    keywords="sole proprietor wealth statement, wealth statement business capital, wealth reconciliation business, section 116 wealth statement Pakistan, drawings wealth statement",
    category="Sole Proprietorship",
    icon="⚖️",
    read="11 min read",
    banner="For a sole proprietor, the business is part of personal wealth. The wealth statement must show it, and the reconciliation must explain how it changed.",
    tldr=("Under Section 116(2), every resident individual filing a return must file a wealth statement and wealth reconciliation statement with it. For a sole "
          "proprietor, there is no separate business entity: business assets, stock, receivables, bank balances and business liabilities are the owner's assets and "
          "liabilities. The reconciliation explains the change in net wealth from one year to the next using income, including business profit, less personal "
          "spending. A missing statement or reconciliation carries a penalty of 0.1% of taxable income per week or Rs 100,000, whichever is higher. Mistakes can be "
          "corrected by a revised statement before a notice under Section 122(9) is received."),
    lead=("Many sole proprietors file a return that shows business profit correctly but a wealth statement that does not match it. The two are linked: the profit "
          "you declare has to explain how your wealth changed. This guide shows how business figures fit into the statement and how to make the reconciliation "
          "balance. For a general introduction, see our wealth statement guide."),
    body=f"""
{SERIES}

<h2 id="law">What the Law Requires</h2>
{table(["Rule", "Detail", "Section"], [
    ["Who files", "Every resident individual filing a return, with the return", "116(2)"],
    ["What it shows", "Assets and liabilities (including foreign), those of a dependent spouse, minor children and other dependents, assets transferred to others, and personal expenditure", "116(1)"],
    ["Reconciliation", "A wealth reconciliation statement must accompany the wealth statement", "116(1)(e), 116(2)"],
    ["Correction", "A revised statement, with revised reconciliation and reasons, can be filed before a notice under Section 122(9) is received", "116(3)"],
    ["Penalty", "0.1% of taxable income per week or Rs 100,000, whichever is higher, for failing to furnish the statement or reconciliation", "182"],
])}

<h2 id="business-in-wealth">How the Business Appears in Your Wealth Statement</h2>
<p>A sole proprietorship is not a separate person, so its assets and liabilities are yours. The usual approach is to show your <strong>capital in the business</strong>, meaning business assets minus business liabilities, supported by the business balance sheet:</p>
{table(["Business item", "Where it sits"], [
    ["Stock in trade at 30 June", "Business asset"],
    ["Business bank balances and cash", "Business asset"],
    ["Amounts customers owe you (receivables)", "Business asset"],
    ["Furniture, equipment, vehicles used in the business", "Business asset"],
    ["Amounts you owe suppliers (payables)", "Business liability"],
    ["Business loans", "Business liability"],
    ["Capital = assets minus liabilities", "Shown in the wealth statement as your investment in the business"],
])}

<h2 id="reconciliation">The Reconciliation, Step by Step</h2>
<p>The reconciliation answers one question: does last year's net wealth, plus this year's income, minus this year's spending, equal this year's net wealth?</p>
<ol>
<li><strong>Opening net wealth:</strong> taken from last year's statement.</li>
<li><strong>Add income:</strong> business profit as declared, plus any other income, including exempt income and amounts already taxed at source.</li>
<li><strong>Add other inflows:</strong> gifts, inheritance, loans received, sale proceeds of assets.</li>
<li><strong>Less personal expenditure:</strong> household spending, school fees, travel, and the like.</li>
<li><strong>Less other outflows:</strong> gifts given, loan repayments.</li>
<li><strong>Result:</strong> should equal closing net wealth. A gap means something is missing.</li>
</ol>

<h2 id="example">Worked Example</h2>
<p>A trader's net wealth at 30 June 2026 was Rs 6,000,000, including business capital of Rs 2,500,000. In tax year 2027, business profit is Rs 2,400,000; the trader received a gift of Rs 500,000 from a parent; household spending was Rs 1,500,000.</p>
{table(["Line", "Amount"], [
    ["Opening net wealth", "Rs 6,000,000"],
    ["Add business profit", "Rs 2,400,000"],
    ["Add gift received", "Rs 500,000"],
    ["Less personal expenditure", "(Rs 1,500,000)"],
    ["Less tax paid during the year", "(Rs 410,000)"],
    ["Expected closing net wealth", "Rs 6,990,000"],
])}
<p>The closing wealth statement must then add up to Rs 6,990,000, for example business capital of Rs 3,100,000 (more stock and receivables) plus personal assets. If it shows Rs 7,500,000, there is Rs 510,000 the trader must explain. The figures are illustrative.</p>

<h2 id="drawings">Drawings: The Line That Breaks Most Reconciliations</h2>
<p>Money taken out of the business for the household is not a business expense. It reduces business capital and appears as personal expenditure in the reconciliation. If drawings are recorded as business expenses, profit is understated and the personal spending line looks too low, which an officer will notice. Keep drawings in a separate record each month; our {a(B['rec'], 'records guide')} shows how.</p>

<h2 id="unexplained">Why an Unexplained Gap Matters</h2>
<p>If your wealth grows by more than your declared income explains, the difference can be questioned as unexplained income or assets. The answer is almost always in the records: a gift not shown, a loan not recorded, stock understated last year. Fixing the record before a notice arrives is far easier than explaining it afterwards.</p>

<h2 id="revise">Correcting an Earlier Year</h2>
<p>Section 116(3) allows a revised wealth statement, with a revised reconciliation and the reasons, before you receive a notice under Section 122(9) for that year. The Commissioner can declare a revision void if it is not a genuine correction of an omission or wrong statement. Revise when you find a real error, and keep the evidence that explains it.</p>

<h2 id="mistakes">Common Mistakes</h2>
<ul>
<li>Showing only personal assets and leaving out business stock and receivables.</li>
<li>Recording household spending as a business expense.</li>
<li>Starting the year with figures that differ from last year's closing statement.</li>
<li>Leaving out loans received or repaid.</li>
<li>Forgetting assets of a dependent spouse or minor children.</li>
</ul>
<p>For the general rules that apply to everyone, see our {a(X['wsg'], 'wealth statement guide')}.</p>
""",
    faqs=[
        ("Does a sole proprietor need to file a wealth statement?",
         "Yes. Under Section 116(2), every resident individual filing a return must file a wealth statement and reconciliation with it."),
        ("How do I show my business in the wealth statement?",
         "Show your capital in the business, meaning business assets such as stock, receivables, bank balances and equipment, minus business liabilities such as payables and loans."),
        ("Are drawings a business expense?",
         "No. Money taken for household use reduces business capital and appears as personal expenditure in the reconciliation."),
        ("What is the penalty for not filing a wealth statement?",
         "Under Section 182, 0.1% of taxable income per week or Rs 100,000, whichever is higher."),
        ("Can I correct last year's wealth statement?",
         "Yes. Section 116(3) allows a revised statement with a revised reconciliation and reasons, before a notice under Section 122(9) is received for that year."),
        ("What if my wealth increased more than my income?",
         "The difference needs an explanation, such as a gift, loan or inheritance. Unexplained increases can be questioned as income."),
        ("Do I include my spouse's assets?",
         "Assets of a dependent spouse, minor children and other dependents are included; a spouse's assets are included only if the spouse is dependent."),
    ],
    sources=[S_ITO, S_IRIS],
    related=[(B["ret"], "Sole Proprietor Tax Return"), (B["rec"], "Sole Proprietor Records"), (X["wsg"], "Wealth Statement Guide")],
    cta_h="Make Your Wealth Statement Balance",
    cta_p="We reconcile business and personal figures line by line, before you file.",
    wa_text="Assalam o Alaikum, mujhe apne business ke saath wealth statement banwana hai.",
)

# ───────────────────────────── Cash rules ─────────────────────────────
CASHP = dict(
    slug=CA_SLUG,
    svc=dict(h2="Let Us Check Your Payments Before FBR Does", intro="These rules are applied when your return is assessed, long after the money has moved. We review your payment patterns now and fix them going forward.",
             hook="Business runs mostly on cash?", fee="Fixed fee for a payments review, confirmed before we start; sole proprietor annual return Rs 5,000.", btn="Review my cash payments",
             items=["A review of expense heads that cross Rs 250,000 in cash", "A list of regular suppliers without an NTN", "A check of large cash receipts against single invoices", "A simple banking routine for suppliers and customers", "Your return prepared with these rules applied correctly"],
             risks=["Whole expense heads disallowed when paid in cash above the limit", "Half of sale-related expenses disallowed for large cash receipts"]),
    title="Cash Payment Rules for Sole Proprietors: Section 21 Explained",
    h1="Cash Payment Rules for Sole Proprietors: When FBR Disallows Your Expenses Under Section 21",
    crumb="Section 21 Cash Rules",
    description="Section 21 rules that cut a sole proprietor's expenses: cash over Rs 250,000 per head, 10% for non-NTN suppliers, 50% for cash receipts over Rs 200,000.",
    keywords="section 21 cash payment rule Pakistan, 250000 cash expense rule FBR, purchases from non NTN holders 10 percent, cash receipt 200000 disallowance, business banking channel FBR",
    category="Sole Proprietorship",
    icon="💵",
    read="10 min read",
    banner="Paying or getting paid in cash is legal. But Section 21 can disallow expenses linked to large cash transactions, increasing the tax on your business.",
    tldr=("Three clauses of Section 21 of the Income Tax Ordinance (as amended up to 30 June 2026) hit cash-based businesses: (l) disallows expenditure under a "
          "single account head that exceeds Rs 250,000 in aggregate when paid other than through a crossed banking instrument or verifiable online transfer from "
          "the business account (with exceptions for amounts up to Rs 25,000, utilities, freight, travel fare, postage and statutory payments); (q) disallows 10% of "
          "expenditure attributable to purchases from persons who are not NTN holders; and (s) disallows 50% of expenditure claimed in respect of a sale where "
          "payment above Rs 200,000 against a single invoice was received other than through a banking channel or digital means."),
    lead=("Most small businesses in Pakistan still pay suppliers and receive from customers partly in cash. The law does not prohibit it, but it changes the tax "
          "result: expenses linked to large cash transactions can be disallowed, which raises taxable profit. This guide explains the three rules in plain terms, "
          "with examples, and the habits that keep your expenses deductible."),
    body=f"""
{SERIES}

<h2 id="principle">The Starting Point: Section 20</h2>
<p>Section 20 allows a deduction for expenditure incurred wholly and exclusively for the purposes of the business. Section 21 then lists expenditure that is not allowed even if it is a genuine business cost. Three of those items are about how money moves, and they matter most to cash-based sole proprietors. For the wider list of what is and is not deductible, see our guide to {a(X['exp'], 'deductible business expenses')}.</p>

<h2 id="rule-l">Rule 1: Cash Expenses Over Rs 250,000 Under One Head (Section 21(l))</h2>
<p>No deduction is allowed for expenditure under a <strong>single account head</strong> that, in aggregate, exceeds <strong>Rs 250,000</strong>, if paid other than by a crossed cheque, crossed bank draft, crossed pay order or other crossed banking instrument showing transfer from the business bank account. Online transfers from the payer's business account to the payee's business account, and credit card payments, count as banking channel payments if they are verifiable from both bank statements.</p>
<p><strong>Exceptions:</strong> expenditures not exceeding Rs 25,000; utility bills; freight charges; travel fare; postage; and payment of taxes, duties, fees, fines or other statutory obligations.</p>
{table(["Situation", "Result"], [
    ["Repairs head: Rs 400,000 for the year, all paid in cash in amounts above Rs 25,000", "At risk of disallowance: the head exceeds Rs 250,000 and was not paid through the bank"],
    ["Same repairs paid by online transfer from the business account to the contractor's business account", "Allowed, if verifiable from both bank statements"],
    ["Electricity bills of Rs 600,000 paid in cash at the bank", "Excepted: utility bills"],
    ["Many small cash purchases of stationery, each under Rs 25,000", "Excepted: expenditures not exceeding Rs 25,000"],
])}
<p>Note the words "business bank account" and "business account of the payee". Paying from a personal account, or into a supplier's personal account, weakens the claim.</p>

<h2 id="rule-q">Rule 2: Purchases From Suppliers Without an NTN (Section 21(q))</h2>
<p>Ten per cent of the claimed expenditure attributable to purchases from persons who are <strong>not National Tax Number holders</strong> is not allowed. For agricultural produce, the rule applies only to purchases from middlemen.</p>
<p><strong>Example:</strong> a shop buys Rs 3,000,000 of stock in the year from suppliers who do not hold an NTN. Rs 300,000 of that cost is disallowed, increasing taxable profit by the same amount. At a 30% marginal rate, that is Rs 90,000 of extra tax. The figures are illustrative.</p>
<p>The practical answer is to keep each regular supplier's NTN on file and prefer registered suppliers where you can.</p>

<h2 id="rule-s">Rule 3: Large Cash Receipts From Customers (Section 21(s))</h2>
<p>Fifty per cent of the expenditure claimed in respect of a sale is not allowed where the business received payment <strong>exceeding Rs 200,000</strong> <strong>otherwise than through a banking channel or digital means</strong> against a <strong>single invoice</strong>, whether the invoice covers one or several supplies of goods or services.</p>
<p>This rule looks at how you are paid, not how you pay. A business that routinely accepts large cash payments against single invoices can lose half of the related expenses. Encourage customers to pay large invoices by bank transfer or digital means, and keep the bank records.</p>

<h2 id="combined">How the Three Rules Add Up: Example</h2>
<p>A wholesaler declares sales of Rs 30,000,000 and expenses of Rs 27,000,000 for the year, giving a profit of Rs 3,000,000. On review:</p>
<ul>
<li>Warehouse repairs of Rs 350,000 were paid in cash: disallowed under 21(l).</li>
<li>Purchases of Rs 2,000,000 were from suppliers without an NTN: Rs 200,000 disallowed under 21(q).</li>
<li>Several invoices over Rs 200,000 were collected in cash; the expenses attributable to those sales come to Rs 1,000,000: half, Rs 500,000, disallowed under 21(s).</li>
</ul>
<p>Taxable profit rises from Rs 3,000,000 to Rs 4,050,000, and the tax on it rises accordingly. The figures are illustrative; the exact attribution in a real case depends on the records.</p>

<h2 id="habits">Habits That Keep Your Expenses Deductible</h2>
<ol>
<li>Open a business bank account and run business payments through it.</li>
<li>Pay suppliers and contractors by online transfer or crossed cheque once a head approaches Rs 250,000 for the year.</li>
<li>Collect suppliers' NTNs and keep them on file.</li>
<li>Ask customers to pay invoices above Rs 200,000 by bank or digital means; show bank details on the invoice.</li>
<li>Keep bank statements and invoices together, so each payment can be matched.</li>
<li>Review the year's cash payments by head before 30 June, not after the return is filed.</li>
</ol>

<h2 id="withholding-link">The Link With Withholding</h2>
<p>Section 21(c) separately disallows expenditure from which you were required to deduct tax but did not deduct and pay it, with the disallowance on purchases of raw materials and finished goods capped at 20% of those purchases. If you are a withholding agent, see our {a(B['wht'], 'withholding guide')}.</p>
""",
    faqs=[
        ("Is it illegal to pay suppliers in cash?",
         "No. But under Section 21(l), expenditure under one account head that exceeds Rs 250,000 in the year and is paid other than through the banking channel can be disallowed, subject to exceptions."),
        ("What payments are exempt from the Rs 250,000 rule?",
         "Expenditures not exceeding Rs 25,000, utility bills, freight charges, travel fare, postage, and payment of taxes, duties, fees, fines or other statutory obligations."),
        ("Does an online transfer count as a banking channel?",
         "Yes, an online transfer from the payer's business account to the payee's business account, and credit card payments, count if verifiable from both bank statements."),
        ("What happens if I buy from suppliers without an NTN?",
         "Under Section 21(q), 10% of the expenditure attributable to those purchases is disallowed. For agricultural produce it applies only to purchases from middlemen."),
        ("Can receiving cash from customers affect my expenses?",
         "Yes. Under Section 21(s), 50% of the expenditure claimed in respect of a sale is disallowed where more than Rs 200,000 against a single invoice was received other than through a banking channel or digital means."),
        ("Does paying from my personal account count?",
         "Section 21(l) refers to transfer from the business bank account, so paying from a personal account weakens the claim."),
        ("How can I avoid these disallowances?",
         "Run business payments through a business bank account, keep suppliers' NTNs, ask customers to pay large invoices by bank, and review cash payments by expense head before the year ends."),
    ],
    sources=[S_ITO],
    related=[(X["exp"], "Deductible Business Expenses"), (B["rec"], "Sole Proprietor Records"), (B["fees"], "Services & Fees")],
    cta_h="Keep Your Expenses Deductible",
    cta_p="We review your payments against Section 21 and set up a banking routine that protects your deductions.",
    wa_text="Assalam o Alaikum, mera business zyada cash par chalta hai. Section 21 ke rules ke mutabiq review chahiye.",
)

POSTS = [FEESP, LHRP, WSP, CASHP]
