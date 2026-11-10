"""Sole proprietorship series (6 posts). Facts checked 10 November 2026 against the Income Tax Ordinance 2001 (amended
up to 30.06.2026), the Sales Tax Act 1990 (amended up to 30.06.2026) and FBR's IRIS registration page."""
from posts import WA, a, table, S_IRIS

DATE = "2026-11-10"
DLONG = "10 November 2026"

S_ITO = ("FBR: Income Tax Ordinance, 2001 (amended up to 30.06.2026)", "https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf")
S_STA = ("FBR: Sales Tax Act, 1990 (amended up to 30.06.2026)", "https://download1.fbr.gov.pk/Docs/20267171373418951SalesTaxAct1990updatedupto30.06.2026.pdf")
S_181 = ("FBR: Change your personal details (Registration Form 181)", "https://www.fbr.gov.pk/change-your-personal-details/51147/71157")
S_PP181 = ("ProPakistani: Taxpayers face problems as FBR suspends key IRIS feature (5 August 2026)", "https://propakistani.pk/2026/08/05/taxpayers-face-problems-as-fbr-suspends-key-iris-feature/")
S_PRA = ("Punjab Revenue Authority", "https://pra.punjab.gov.pk/")
S_SRB = ("Sindh Revenue Board", "https://www.srb.gos.pk/")
S_KPRA = ("Khyber Pakhtunkhwa Revenue Authority", "https://kpra.gov.pk/")
S_EXC = ("Punjab Excise, Taxation and Narcotics Control Department", "https://excise.punjab.gov.pk/")

R_SLUG = "sole-proprietorship-registration-pakistan"
I_SLUG = "add-business-to-ntn-iris-sole-proprietor"
T_SLUG = "sole-proprietor-sales-tax-registration-strn-pakistan"
W_SLUG = "sole-proprietor-withholding-tax-duties-pakistan"
K_SLUG = "sole-proprietor-records-books-fbr-pakistan"
C_SLUG = "close-sole-proprietorship-remove-business-ntn-pakistan"
S = {k: "/blogs/" + v for k, v in dict(reg=R_SLUG, iris=I_SLUG, stx=T_SLUG, wht=W_SLUG, rec=K_SLUG, close=C_SLUG).items()}
X = {"ntn": "/ntn-registration", "strn": "/sales-tax-registration", "ret": "/blogs/sole-proprietor-tax-return-pakistan-2026",
     "secp": "/secp-vs-sole-proprietorship-pakistan", "rof": "/blogs/registrar-of-firms-vs-fbr-registration-partnership-lahore",
     "whtrates": "/blogs/withholding-tax-pakistan-2026", "notice": "/fbr-notice-defense", "pricing": "/pricing",
     "compare": "/blogs/sole-proprietorship-vs-partnership-vs-pvt-ltd-lahore", "filing": "/income-tax-filing"}
SERIES = (f'<p class="tf-primary"><strong>Sole proprietor series:</strong> {a(S["reg"], "registration")} &middot; {a(S["iris"], "adding a business on IRIS")} &middot; '
          f'{a(S["stx"], "sales tax (STRN)")} &middot; {a(S["wht"], "withholding duties")} &middot; {a(S["rec"], "records")} &middot; {a(S["close"], "closing a business")}</p>')


REG = dict(
    slug=R_SLUG,
    title="Sole Proprietorship Registration Pakistan 2026: Full Guide",
    h1="Sole Proprietorship Registration in Pakistan 2026: What to Register, Where, and in What Order",
    crumb="Sole Proprietorship Registration",
    description="Start a sole proprietorship in Pakistan the right way: NTN under Section 181, adding the business on IRIS, when STRN and provincial registration apply.",
    keywords="sole proprietorship registration Pakistan, how to register sole proprietorship Pakistan, sole proprietor NTN, register business FBR 2026, sole proprietorship Lahore",
    category="Sole Proprietorship",
    icon="🏪",
    read="12 min read",
    banner="A sole proprietorship is the quickest way to start a business in Pakistan, but it is registered through the tax system, not through a separate business registry.",
    tldr=("A sole proprietorship is a business owned and run by one individual with no separate legal identity. There is no SECP-style registry for it; "
          "in practice it is recognised through income tax registration under Section 181 of the Income Tax Ordinance, where the owner's CNIC serves as the NTN. "
          "The steps are: register (or use) the owner's IRIS profile, add the business name and address to it, open a bank account in the business name, then "
          "check whether sales tax registration is compulsory under Section 14 of the Sales Tax Act and whether a provincial revenue authority or professional "
          "tax applies. Online sellers must now be registered before marketplaces or couriers can serve them."),
    lead=("Most small businesses in Pakistan, from shops and workshops to agencies and online stores, start as sole proprietorships. The setup is cheap and fast, "
          "but owners often register in the wrong order or miss a registration that later blocks a bank account or a marketplace payout. This guide sets out "
          "what the law actually requires, in the order that avoids rework."),
    body=f"""
{SERIES}

<h2 id="what-it-is">What a Sole Proprietorship Is in Law</h2>
<p>A sole proprietorship is not a separate legal person. The business and its owner are one taxpayer: profits are the owner's business income, taxed at individual rates, and the owner is personally responsible for the business's debts. That is the key difference from a private limited company registered with SECP, which is a separate person, and from a partnership or association of persons (AOP), which has two or more members. Our comparison of {a(X['compare'], 'sole proprietorship, partnership and private limited')} covers the choice in detail.</p>
<p>Because there is no separate legal person, there is no separate company-style register for a sole proprietorship. Partnerships can be registered with the provincial Registrar of Firms ({a(X['rof'], 'see our guide')}); companies are incorporated with SECP; a sole proprietorship is recognised through the owner's tax registration and the registrations its activity requires.</p>

<h2 id="registration-map">The Registration Map: What Applies to You</h2>
{table(["Registration", "Who needs it", "Legal basis", "Where"], [
    ["Income tax registration (NTN)", "Every taxpayer. For individuals with a CNIC, the CNIC is used as the NTN from tax year 2015.", "Income Tax Ordinance s.181(1) and (4)", "FBR IRIS"],
    ["Business details on the NTN", "Every sole proprietor, so returns, withholding and bank records show the business", "s.181 registration through Form 181 (modification)", "FBR IRIS"],
    ["Sales tax registration (STRN)", "Manufacturers (other than cottage industry), Tier-1 retailers, importers, wholesalers, dealers and distributors, exporters claiming refunds, and online sellers of goods", "Sales Tax Act s.14(1) and (1A)", "FBR IRIS"],
    ["Provincial sales tax on services", "Businesses providing taxable services in the province", "Provincial sales tax on services laws", "PRA, SRB, KPRA or BRA"],
    ["Professional tax", "Professionals and businesses in provinces that levy it", "Provincial law", "In Punjab, the Excise, Taxation and Narcotics Control Department"],
    ["Other licences", "Food, drugs, trade-specific activities", "Sector laws", "Relevant authority"],
])}

<h2 id="step-by-step">Step-by-Step: Setting Up in the Right Order</h2>
<ol>
<li><strong>Get your IRIS profile active.</strong> If you have never registered, create an IRIS account with your CNIC; the CNIC becomes your NTN. Our {a(X['ntn'], 'NTN registration service')} does this for you.</li>
<li><strong>Add the business to your registration.</strong> Enter the business name, address and nature of business through Form 181 on IRIS, so FBR records match your signboard, invoices and bank account. Our step-by-step guide to {a(S['iris'], 'adding a business to your NTN on IRIS')} explains the form and what to do if the online option is not working.</li>
<li><strong>Open the business bank account.</strong> Banks normally ask for proof of tax registration showing the business. Then add the bank account to your IRIS profile, since bank account details are one of the items Form 181 updates.</li>
<li><strong>Check sales tax.</strong> If your activity falls in a Section 14 category, registration is compulsory, and FBR can act against unregistered persons under Sections 14AC to 14AE. See our {a(S['stx'], 'STRN guide for sole proprietors')}.</li>
<li><strong>Check provincial registrations.</strong> Service businesses generally register with their province's revenue authority; professionals check professional tax.</li>
<li><strong>Set up records from day one.</strong> Section 174 requires records to be kept for six years. Our guide to {a(S['rec'], 'records FBR expects')} lists what to keep.</li>
</ol>

<h2 id="online-sellers">Selling Online: The 2025 Rules</h2>
<p>The Finance Act, 2025 added two rules that matter for online sole proprietors:</p>
<ul>
<li><strong>Income tax:</strong> Section 181(1) now expressly covers people selling digitally ordered goods or services from within Pakistan through an online marketplace or courier, and Section 181(1A) says a marketplace or courier must not let a vendor use its platform unless the vendor is registered.</li>
<li><strong>Sales tax:</strong> Section 14(1A) of the Sales Tax Act requires sellers of digitally ordered goods through a marketplace, website or app to register (cottage industry and retailers paying through electricity bills are excluded), and Section 14(1B) bars marketplaces and couriers from serving them without an NTN and, where required, a sales tax registration.</li>
</ul>
<p>In practice, a seller without registration can find a store or courier account blocked. Register before you launch.</p>

<h2 id="costs">What It Costs</h2>
<p>FBR charges no fee for an NTN or for adding a business on IRIS. Provincial registrations may have their own fees. If you want us to handle it, our published fees are Rs 2,000 for NTN registration (including ATL guidance) and Rs 3,000 for sales tax registration; see {a(X['pricing'], 'all prices')}.</p>

<h2 id="after-registration">What Comes After Registration</h2>
<ul>
<li><strong>Annual income tax return</strong> with business income and a wealth statement; see our {a(X['ret'], 'sole proprietor tax return guide')}.</li>
<li><strong>Withholding duties</strong> once you employ staff, rent premises above Rs 1.5 million a year, or your turnover reaches Rs 100 million; see our {a(S['wht'], 'withholding guide')}.</li>
<li><strong>Monthly sales tax returns</strong> if you hold an STRN.</li>
</ul>

<h2 id="mistakes">Common Mistakes</h2>
<ol>
<li><strong>Using a business name that does not appear on the NTN.</strong> Banks, marketplaces and customers' withholding statements then do not match your records.</li>
<li><strong>Registering for sales tax "just in case".</strong> An STRN brings monthly returns; register when the law requires it or when your buyers need it.</li>
<li><strong>Mixing personal and business money.</strong> It makes the wealth statement and the profit figure hard to defend.</li>
<li><strong>Opening a second business without updating IRIS.</strong> Every business and branch should be on the registration.</li>
</ol>

<h2 id="how-we-help">How Kamboh Associates Helps</h2>
<p>We set up sole proprietorships end to end over WhatsApp: IRIS registration, business details through Form 181, sales tax and provincial checks, and the first return. Replies within office hours.</p>
""",
    faqs=[
        ("Do I need to register a sole proprietorship with SECP?",
         "No. SECP incorporates companies. A sole proprietorship is not a separate legal person; it is recognised through the owner's income tax registration and any registrations its activity requires."),
        ("Is my CNIC my NTN as a sole proprietor?",
         "Yes. Under Section 181(4) of the Income Tax Ordinance, from tax year 2015 an individual's CNIC is used as the National Tax Number."),
        ("How do I add my business name to my NTN?",
         "Through Registration Form 181 (modification) on IRIS. FBR's page on changing details lists business address, business branches and bank account among the items it updates."),
        ("Does a sole proprietor need a sales tax number?",
         "Only if the business falls in a Section 14 category, such as a manufacturer that is not a cottage industry, a Tier-1 retailer, an importer, a wholesaler, dealer or distributor, or an online seller of goods. Services are usually registered with the provincial revenue authority instead."),
        ("Can I sell on Daraz or other marketplaces without an NTN?",
         "No. Since the Finance Act, 2025, marketplaces and couriers must not let unregistered vendors use their services for e-commerce transactions."),
        ("Is there a government fee for an NTN?",
         "FBR charges no fee for NTN registration on IRIS."),
        ("How is a sole proprietor taxed?",
         "Business profit is the owner's income, taxed at the rates for individuals with business income, through an annual return with a wealth statement."),
        ("When should a sole proprietor become a company?",
         "Usually when liability protection, outside investment or larger contracts matter more than simplicity. Our SECP versus sole proprietorship guide compares the two."),
    ],
    sources=[S_ITO, S_STA, S_181, S_IRIS, S_PRA, S_SRB, S_EXC],
    related=[(S['iris'], "Add a Business to Your NTN"), (S['stx'], "Sole Proprietor STRN"), (X['ret'], "Sole Proprietor Tax Return")],
    cta_h="Start Your Sole Proprietorship the Right Way",
    cta_p="NTN, business details on IRIS, sales tax and provincial checks, handled over WhatsApp.",
    wa_text="Assalam o Alaikum, mujhe sole proprietorship (business) registration karwani hai.",
)


IRISP = dict(
    slug=I_SLUG,
    title="How to Add a Business to Your NTN on IRIS (Sole Proprietor)",
    h1="How to Add a Business to Your NTN on IRIS: Form 181 Guide for Sole Proprietors",
    crumb="Add Business to NTN",
    description="Add your business name, address, branches and bank account to your NTN on IRIS through Form 181, and what needs an RTO visit instead. Updated for 2026.",
    keywords="add business to NTN IRIS, Form 181 FBR, add business name NTN, sole proprietor IRIS business, modification of registration FBR, add bank account IRIS",
    category="Sole Proprietorship",
    icon="🧩",
    read="10 min read",
    banner="FBR lets you update business details yourself through Form 181 on IRIS, but some changes, such as discontinuing a business, still need a visit to your Regional Tax Office.",
    tldr=("A sole proprietor's business is added to the owner's existing NTN through Registration Form 181 (filed for modification) on IRIS. FBR's own page lists "
          "what this form can update: mobile number, personal address, business address, business branches, legal representative under Section 87, and bank "
          "account. Discontinuing a business, deregistration, change of jurisdiction, CNIC, email and POC updates need a visit to your Regional Tax Office (RTO) "
          "with documents. Tax practitioners reported problems with the online Form 181 facility in 2026, so check whether it is working before you plan around it."),
    lead=("Many people register an NTN as salaried individuals and later start a business, or open a second shop, without updating FBR. The return then shows "
          "business income from a business FBR does not know about, and bank or marketplace records do not match. This guide explains how to add a business "
          "properly and what to do when the online route is blocked."),
    body=f"""
{SERIES}

<h2 id="why">Why Your Business Must Be on Your NTN</h2>
<p>Section 181 of the Income Tax Ordinance requires every taxpayer to register in the prescribed form, and for individuals the CNIC is the NTN. A sole proprietorship has no separate NTN; its details sit on the owner's registration. Keeping them current matters because:</p>
<ul>
<li>Banks and payment processors match the business name and account to FBR records.</li>
<li>Customers who deduct withholding tax from your payments report it against your NTN, and you claim it in your return.</li>
<li>Online marketplaces and couriers must confirm vendors are registered (Section 181(1A)).</li>
<li>Notices and audits start from the registration data. Business income from an unregistered business invites questions.</li>
</ul>

<h2 id="what-181-changes">What Form 181 Can and Cannot Change</h2>
<p>FBR's page "Change your personal details" (checked {DLONG}) splits changes into two groups:</p>
{table(["Online through Form 181 (modification)", "Only by visiting your RTO with documents"], [
    ["Mobile number", "Discontinuance of business"],
    ["Personal or residential address", "Jurisdiction for income tax return assessment"],
    ["Business address", "Deregistration"],
    ["Addition of business branches", "Updating CNIC number"],
    ["Legal representative under Section 87", "Email"],
    ["Bank account", "Updating Pakistan Origin Card (POC)"],
])}

<h2 id="steps">Step-by-Step: Adding a Business on IRIS</h2>
<p>IRIS screens change from time to time; use these steps as a guide and follow the labels on screen.</p>
<ol>
<li><strong>Prepare the details:</strong> business name exactly as on your signboard and invoices, business address, the date the business started, nature of business, and the business bank account (if already opened).</li>
<li><strong>Log in to IRIS</strong> with your CNIC and password.</li>
<li><strong>Open the registration modification form</strong> (Form 181) for income tax.</li>
<li><strong>Add the business</strong> in the business section: name, start date and principal activity. Add each branch separately if you trade from more than one place.</li>
<li><strong>Add or update the business address</strong> and the bank account.</li>
<li><strong>Attach supporting documents</strong> where IRIS asks for them, such as a rent agreement or ownership proof for the premises and a utility bill.</li>
<li><strong>Submit</strong> and keep the acknowledgement. Check that the registration certificate shows the business once processed.</li>
</ol>

<h2 id="documents">Documents by Type of Premises</h2>
{table(["Premises", "Documents to keep ready"], [
    ["Rented shop or office", "Rent agreement in your name, landlord's CNIC copy, recent utility bill of the premises"],
    ["Owned premises", "Ownership document (registry, transfer letter or allotment) and a recent utility bill"],
    ["Family-owned premises used free of rent", "Owner's consent letter with CNIC copy, and a utility bill"],
    ["Home-based business", "Utility bill of the residence; describe the business activity accurately"],
    ["Online-only business", "Residential or correspondence address proof; the website or store link as the place of business"],
])}
<p>Mismatches between the address on IRIS, the utility bill and the bank's records are the most common reason an update is questioned. Use the same spelling of the business name and address everywhere.</p>

<h2 id="if-blocked">If the Online Form 181 Is Not Working</h2>
<p>In August 2026 ProPakistani reported that the Pakistan Tax Bar Association asked FBR to restore the "change in particulars" (Form 181) facility on IRIS, which had been suspended for sales tax registered persons, with users reporting problems for individuals too. If you cannot submit online:</p>
<ul>
<li>Keep screenshots of the error and the date you tried.</li>
<li>Visit or write to your Regional Tax Office with the documents, as FBR already requires for the changes in the right-hand column above.</li>
<li>Do not delay your return: declare the business income correctly in the return even while the registration update is pending, and keep proof that you tried to update.</li>
</ul>

<h2 id="special-cases">Special Cases</h2>
{table(["Situation", "What to do"], [
    ["Salaried person starting a side business", "Add the business through Form 181. Your return will then have salary and business income; keep them separate in your records."],
    ["Second shop or a branch in another city", "Add it as a business branch through Form 181."],
    ["Online store", "Add the business before opening marketplace or courier accounts, since they must check registration."],
    ["Business has stopped", "Discontinuance needs an RTO visit. See our guide to {a(S['close'], 'closing a sole proprietorship')}."],
    ["You also need sales tax registration", "Sales tax registration is a separate application on IRIS. See our {a(S['stx'], 'STRN guide')}."],
])}

<h2 id="after">After the Business Is Added</h2>
<ul>
<li>Use the same business name on invoices, the bank account and marketplace profiles.</li>
<li>Declare the business income and expenses in your next return; our {a(X['ret'], 'sole proprietor return guide')} explains the schedules.</li>
<li>Keep records from the start date for six years, as Section 174 requires.</li>
</ul>

<h2 id="how-we-help">How We Help</h2>
<p>We file Form 181 updates for clients, prepare the RTO application when the change cannot be made online, and make sure the business details match your bank and sales tax records. Replies within office hours.</p>
""".replace("{a(S['close'], 'closing a sole proprietorship')}", a(S['close'], 'closing a sole proprietorship')).replace("{a(S['stx'], 'STRN guide')}", a(S['stx'], 'STRN guide')),
    faqs=[
        ("Does a sole proprietorship get its own NTN?",
         "No. The business is added to the owner's registration, and for individuals the CNIC is the NTN under Section 181(4)."),
        ("Which form adds a business to my NTN?",
         "Registration Form 181, filed for modification, on IRIS. FBR lists business address, business branches and bank account among the details it updates."),
        ("Can I close a business online through Form 181?",
         "No. FBR's page says discontinuance of business and deregistration require a visit to your Regional Tax Office with relevant documents."),
        ("Can I change my email on IRIS myself?",
         "FBR's page lists email among the changes that require a visit to the RTO."),
        ("I have two shops. Do I need two NTNs?",
         "No. Add the second location as a business branch on your registration through Form 181."),
        ("What if Form 181 shows an error?",
         "Keep evidence of the error, contact or visit your RTO with documents, and declare the business correctly in your return in the meantime."),
        ("Should I add the business before opening a bank account?",
         "It helps. Banks usually check tax registration, and once the account is open you can add it to IRIS through Form 181."),
    ],
    sources=[S_181, S_ITO, S_IRIS, S_PP181],
    related=[(S['reg'], "Sole Proprietorship Registration"), (S['close'], "Closing a Sole Proprietorship"), (X['ntn'], "NTN Registration")],
    cta_h="Need Your Business Added to Your NTN?",
    cta_p="We file Form 181, or prepare your RTO application if the online route is blocked.",
    wa_text="Assalam o Alaikum, mujhe apne NTN mein business add karwana hai (Form 181).",
)


STX = dict(
    slug=T_SLUG,
    title="Sole Proprietor STRN: Who Must Register for Sales Tax",
    h1="Sales Tax Registration for Sole Proprietors: When an STRN Is Compulsory Under Section 14",
    crumb="Sole Proprietor STRN",
    description="Does your sole proprietorship need an STRN? Section 14 categories, the cottage industry and Tier-1 retailer tests (2026), online sellers, and FBR's powers.",
    keywords="sole proprietor sales tax registration, STRN for sole proprietor Pakistan, who must register for sales tax Pakistan, cottage industry sales tax, Tier-1 retailer definition 2026",
    category="Sole Proprietorship",
    icon="🧾",
    read="11 min read",
    banner="Sales tax registration is compulsory only for the categories in Section 14 of the Sales Tax Act. The Finance Act, 2026 changed the Tier-1 retailer test.",
    tldr=("Under Section 14 of the Sales Tax Act, 1990 (as amended up to 30 June 2026), a person making taxable supplies must register if they are a manufacturer "
          "other than a cottage industry, a retailer liable to pay sales tax (other than retailers paying through electricity bills), an importer, an exporter "
          "seeking refunds, a wholesaler, dealer or distributor, or a person required by another law. Online sellers of goods must also register under Section 14(1A). "
          "A cottage industry must meet all four tests, including annual turnover of no more than Rs 8 million. The Tier-1 retailer definition now includes "
          "retailers with turnover above Rs 200 million. Persons who should be registered but are not face bank account and property restrictions and, ultimately, "
          "sealing of premises."),
    lead=("Sole proprietors are often told either that every business needs a sales tax number or that small businesses never do. Neither is right. The answer "
          "depends on what you do and, for manufacturers and retailers, on a few precise tests in the law. This guide applies them to common sole proprietor "
          "businesses."),
    body=f"""
{SERIES}

<h2 id="section-14">The Section 14 Categories</h2>
<p>Section 14(1) requires every person making taxable supplies in Pakistan, including zero-rated supplies, in the course of a taxable activity, to register if they fall in any of these categories:</p>
{table(["Category", "Plain meaning", "Common sole proprietor examples"], [
    ["(a) Manufacturer not running a cottage industry", "Anyone who makes or processes goods, unless they meet every cottage industry condition", "Small factory, workshop with a commercial connection, food processing unit"],
    ["(b) Retailer liable to pay sales tax", "Mainly Tier-1 retailers; excludes retailers paying sales tax through electricity bills under s.3(9)", "Shop in an air-conditioned mall, chain outlet, high-turnover retailer"],
    ["(c) Importer", "Imports goods", "Importer of parts or consumer goods"],
    ["(d) Exporter wanting refunds", "Optional for exporters, but needed to claim sales tax refunds on zero-rated supplies", "Garment or handicraft exporter"],
    ["(e) Wholesaler, dealer or distributor", "Supplies goods in the trade chain", "Distributor of FMCG, building materials dealer"],
    ["(f) Required by another law", "Registration demanded by another federal or provincial law for a sales-tax-type levy", "Case by case"],
])}

<h2 id="cottage">The Cottage Industry Test</h2>
<p>Section 2(5AB) defines a cottage industry as a manufacturing concern that meets <strong>all</strong> of these conditions:</p>
<ol>
<li>No industrial gas or electricity connection.</li>
<li>Located in a residential area.</li>
<li>A total labour force of no more than ten workers.</li>
<li>Annual turnover from all supplies of no more than Rs 8 million.</li>
</ol>
<p>Fail any one, for example by taking an industrial electricity connection or moving to a commercial area, and the manufacturer must register.</p>

<h2 id="tier-1">The Tier-1 Retailer Test (Updated by the Finance Act, 2026)</h2>
<p>Section 2(43A), as amended up to 30 June 2026, defines a Tier-1 retailer as a retailer in any of these categories:</p>
<ul>
<li>A unit of a national or international chain of stores.</li>
<li>A retailer in an air-conditioned shopping mall, plaza or centre, excluding kiosks.</li>
<li>A retailer whose cumulative electricity bill for the previous twelve consecutive months exceeds Rs 1.2 million.</li>
<li>A wholesaler-cum-retailer with turnover above Rs 200 million engaged in bulk import and supply of consumer goods to retailers and consumers.</li>
<li>A retailer with turnover above Rs 200 million in the previous twelve months, by declaration or as worked back from tax deducted under Sections 236G or 236H of the Income Tax Ordinance (added in 2026).</li>
<li>Any other person or class prescribed by FBR.</li>
</ul>
<p>The 2026 changes removed some earlier categories and added the Rs 200 million turnover test. If you registered as Tier-1 under an older category, check whether you still fall within the definition before acting either way.</p>

<h2 id="online">Online Sellers</h2>
<p>Section 14(1A), added by the Finance Act, 2025, requires every person selling digitally ordered goods from within Pakistan through an online marketplace, website or app to register, except cottage industry and retailers paying through electricity bills. Section 14(1B) stops marketplaces and couriers from serving them unless they hold an NTN and, where Section 14(1A) applies, a sales tax registration.</p>

<h2 id="services">Services Are Usually Provincial</h2>
<p>Federal sales tax under the Sales Tax Act applies to goods. Most services are taxed by the provinces through the Punjab Revenue Authority, Sindh Revenue Board, Khyber Pakhtunkhwa Revenue Authority or Balochistan Revenue Authority. A consultant, salon, restaurant or agency run as a sole proprietorship checks its provincial registration, not an FBR STRN, for its services.</p>

<h2 id="quick-check">Quick Self-Check</h2>
{table(["Your business", "STRN compulsory?"], [
    ["Small home-based tailoring unit, 4 workers, no commercial connection, turnover Rs 3 million", "No, if all cottage industry conditions are met"],
    ["Same unit moves to a commercial market", "Yes, it is no longer in a residential area"],
    ["Mobile accessories shop in an air-conditioned plaza", "Yes, as a Tier-1 retailer (kiosks excluded)"],
    ["Corner shop paying sales tax through its electricity bill", "No, excluded from s.14(1)(b)"],
    ["Distributor of packaged foods", "Yes, as a distributor"],
    ["Online clothing store selling through a marketplace", "Yes, under s.14(1A), unless an exclusion applies"],
    ["Freelance designer", "Not under the Sales Tax Act; check provincial services rules"],
])}

<h2 id="consequences">What Happens If You Should Register but Do Not</h2>
<p>Sections 14AC to 14AE give FBR escalating powers against persons who make taxable supplies without the registration they need: restrictions on operating bank accounts, restrictions on transferring immovable property after a committee process that includes a chamber or trade association member, and finally sealing the business premises, seizing movable property or appointing a receiver.</p>

<h2 id="after">After Registration</h2>
<ul>
<li>File monthly sales tax returns, even for a nil month.</li>
<li>Issue tax invoices that meet Section 23.</li>
<li>Keep sales tax records for six years after the tax period (Section 24).</li>
<li>If the business later falls out of every category, de-registration under Section 21 is possible after a final return under Section 28. See our guide to {a(S['close'], 'closing a sole proprietorship')}.</li>
</ul>
<p>Our {a(X['strn'], 'sales tax registration service')} costs Rs 3,000, and monthly returns Rs 3,000 a month, as listed on our {a(X['pricing'], 'pricing page')}.</p>
""",
    faqs=[
        ("Is sales tax registration compulsory for every sole proprietor?",
         "No. It is compulsory only for the categories in Section 14 of the Sales Tax Act, such as manufacturers that are not cottage industries, liable retailers, importers, wholesalers, dealers, distributors and online sellers of goods."),
        ("What is the turnover limit for a cottage industry?",
         "Annual turnover from all supplies must not exceed Rs 8 million, and the unit must also have no industrial gas or electricity connection, be in a residential area and have no more than ten workers."),
        ("What changed in the Tier-1 retailer definition in 2026?",
         "The Finance Act, 2026 added retailers with turnover above Rs 200 million in the previous twelve months, set a Rs 200 million turnover condition for wholesaler-cum-retailers, and removed some earlier categories."),
        ("Is a shop in an air-conditioned plaza a Tier-1 retailer?",
         "Yes, a retailer operating in an air-conditioned shopping mall, plaza or centre is Tier-1, except kiosks."),
        ("Do online sellers need an STRN?",
         "Sellers of digitally ordered goods through a marketplace, website or app must register under Section 14(1A), except cottage industry and retailers paying through electricity bills."),
        ("Do service providers register with FBR for sales tax?",
         "Most services are taxed by provincial authorities such as PRA, SRB, KPRA and BRA, so service businesses usually register with the province."),
        ("What can FBR do if I should be registered but am not?",
         "Sections 14AC to 14AE allow restrictions on bank accounts and on transferring immovable property, and ultimately sealing premises, seizing movable property or appointing a receiver."),
        ("Can I cancel my STRN later?",
         "De-registration under Section 21 is possible for persons not required to be registered, after filing a final return under Section 28."),
    ],
    sources=[S_STA, S_IRIS, S_PRA, S_SRB, S_KPRA],
    related=[(S['reg'], "Sole Proprietorship Registration"), (X['strn'], "Sales Tax Registration Service"), (S['rec'], "Sole Proprietor Records")],
    cta_h="Not Sure If You Need an STRN?",
    cta_p="Tell us what you sell and where. We check Section 14 and register you only if the law requires it.",
    wa_text="Assalam o Alaikum, kya meri sole proprietorship ko sales tax registration (STRN) chahiye?",
)


WHT = dict(
    slug=W_SLUG,
    title="Withholding Tax Duties of a Sole Proprietor in Pakistan",
    h1="Withholding Tax Duties of a Sole Proprietor: When You Must Deduct, Deposit and File Statements",
    crumb="Sole Proprietor Withholding Duties",
    description="When a sole proprietor becomes a withholding agent: staff salaries, rent of Rs 1.5m+ a year, Rs 100m turnover (s.153), quarterly statements, penalties.",
    keywords="sole proprietor withholding agent Pakistan, section 153 prescribed person individual turnover 100 million, section 155 rent 1.5 million, section 165 quarterly statement, withholding duties business",
    category="Sole Proprietorship",
    icon="🧮",
    read="11 min read",
    banner="Withholding tax is not only something deducted from you. A growing sole proprietor can become legally responsible for deducting it from others.",
    tldr=("A sole proprietor must deduct tax when paying salary to employees (Section 149), when paying gross rent of Rs 1.5 million or more in a year (Section 155), "
          "and on payments for goods, services and contracts once turnover reaches Rs 100 million in any preceding tax year (Section 153). Tax deducted is "
          "reported in quarterly statements under Section 165, due by 20 April, 20 July, 20 October and 20 January. A person who fails to deduct or deposit is "
          "personally liable for the tax under Section 161, after being given an opportunity to be heard."),
    lead=("Many business owners know withholding tax only as the amount banks or customers deduct from them. As a business grows, the law turns the owner "
          "into a withholding agent too. This guide sets out the exact thresholds in the Income Tax Ordinance, as amended up to 30 June 2026, that make a sole "
          "proprietor responsible for deducting tax. Current rates are in our withholding tax guide, linked below."),
    body=f"""
{SERIES}

<h2 id="when">When a Sole Proprietor Becomes a Withholding Agent</h2>
{table(["Payment", "Duty applies when", "Section"], [
    ["Salary to employees", "You pay salary to any employee. The duty is on every person responsible for paying salary, with no size threshold.", "149"],
    ["Rent of immovable property", "You, as an individual or AOP, pay gross rent of Rs 1.5 million or more in a year", "155(3)(vib)"],
    ["Payments for goods, services and contracts", "Your turnover was Rs 100 million or more in any preceding tax year", "153(7)(i)(i)"],
    ["Same, through sales tax status", "You are registered under the Sales Tax Act with turnover of Rs 100 million or more in any preceding tax year", "153(7)(i)(j)"],
    ["Same, for builders", "You derive income from construction and sale of buildings", "153(7)(i)(k)"],
])}
<p>Other withholding provisions can also apply depending on the payment, such as commission or brokerage. Check each type of payment you make, not only the ones above.</p>

<h2 id="salary">Salary: The Duty Most Owners Miss</h2>
<p>Section 149 requires every person responsible for paying salary to deduct tax at the time of payment, at the employee's average rate on their estimated salary income for the year, adjusting for any tax already withheld under other heads and admissible credits. A shop with two salespeople earning below the taxable limit will compute nil, but the employer still needs the calculation and, where tax is due, must deduct and deposit it. Our {a(X['whtrates'], 'withholding tax guide')} gives the current rates.</p>

<h2 id="rent">Rent: The Rs 1.5 Million Threshold</h2>
<p>Section 155(3) makes individuals and associations of persons paying gross rent of Rs 1.5 million or more in a year prescribed persons who must deduct tax from rent. That is Rs 125,000 a month on average. A sole proprietor renting a shop, office or warehouse above that level deducts tax from the landlord's rent and deposits it.</p>

<h2 id="section-153">Section 153: The Rs 100 Million Turnover Test</h2>
<p>An individual with turnover of Rs 100 million or more in any of the preceding tax years is a "prescribed person" under Section 153(7). From then on, payments to suppliers for goods, to service providers and on contracts are subject to deduction at the rates in the Ordinance. The words "any of the preceding tax years" matter: one year above the threshold is enough, even if turnover falls later.</p>

<h2 id="deposit-and-statements">Depositing Tax and Filing Statements</h2>
<p>Tax deducted is deposited through a payment slip (PSID) generated on IRIS, within the time set by the Income Tax Rules. Section 165 then requires a quarterly statement of tax deducted, with each payee's name, CNIC or NTN, address and amounts:</p>
{table(["Quarter ending", "Statement due by"], [
    ["31 March", "20 April"],
    ["30 June", "20 July"],
    ["30 September", "20 October"],
    ["31 December", "20 January"],
])}
<p>Salary withholding also appears in the annual statement of salaries paid. Give employees and suppliers the deduction certificates they need for their own returns.</p>

<h2 id="consequences">What Happens If You Do Not Deduct</h2>
<p>Under Section 161, a person who fails to deduct tax as required, or deducts it but does not pay it to FBR, is <strong>personally liable to pay the amount of tax</strong>. Section 161(1A) requires that the person first be given an opportunity of being heard. Default surcharge and penalties can follow, and expenses paid without required deduction can be challenged when your own return is assessed. If a notice arrives, our {a(X['notice'], 'FBR notice defence service')} can prepare the reply.</p>

<h2 id="example">Worked Example</h2>
<p>A wholesaler in Faisalabad run as a sole proprietorship had turnover of Rs 115 million in tax year 2025, pays Rs 160,000 a month for a warehouse and employs six staff. From tax year 2026:</p>
<ul>
<li>Section 153 applies to payments to suppliers and service providers, because turnover crossed Rs 100 million in a preceding year.</li>
<li>Section 155 applies to the warehouse rent: Rs 1.92 million a year is above Rs 1.5 million.</li>
<li>Section 149 applies to the six salaries.</li>
<li>Quarterly Section 165 statements are due by the 20th of the month after each quarter.</li>
</ul>
<p>The figures are illustrative.</p>

<h2 id="checklist">Compliance Checklist</h2>
<ul>
<li>☐ List every recurring payment: salaries, rent, suppliers, services, commissions.</li>
<li>☐ Check each against the thresholds above.</li>
<li>☐ Set up monthly deduction and deposit, with PSIDs saved.</li>
<li>☐ Diary the four Section 165 due dates.</li>
<li>☐ Keep payee CNIC or NTN details on file.</li>
<li>☐ Keep deduction records for six years (Section 174).</li>
</ul>

<h2 id="how-we-help">How We Help</h2>
<p>We map a business's payments against the withholding rules, prepare deposits and quarterly statements, and reply to notices about missed deductions. Replies within office hours.</p>
""",
    faqs=[
        ("Does a small shop owner have to deduct tax from staff salaries?",
         "Section 149 puts the duty on every person paying salary. Where an employee's salary is below the taxable limit, the tax works out to nil, but the duty to calculate and, where due, deduct still applies."),
        ("At what turnover does a sole proprietor deduct tax from supplier payments?",
         "When the individual's turnover was Rs 100 million or more in any preceding tax year, under Section 153(7)."),
        ("When must a sole proprietor deduct tax from rent?",
         "When the individual pays gross rent of Rs 1.5 million or more in a year, under Section 155(3)."),
        ("When are withholding statements due?",
         "Quarterly under Section 165: by 20 April, 20 July, 20 October and 20 January for the quarters ending March, June, September and December."),
        ("What if I forgot to deduct tax?",
         "Under Section 161 you can be held personally liable for the tax you should have deducted, after an opportunity of being heard. Correct the practice now and take advice on the past payments."),
        ("If my turnover drops below Rs 100 million, does the Section 153 duty end?",
         "The test is turnover of Rs 100 million or more in any of the preceding tax years, so a past year above the threshold can still count."),
        ("Where do I find the withholding rates?",
         "In the First Schedule to the Income Tax Ordinance. Our withholding tax guide summarises the current rates."),
    ],
    sources=[S_ITO, S_IRIS],
    related=[(S['reg'], "Sole Proprietorship Registration"), (X['whtrates'], "Withholding Tax Rates 2026"), (S['rec'], "Sole Proprietor Records")],
    cta_h="Become Withholding-Compliant",
    cta_p="We check your payments, set up deposits and file quarterly statements on time.",
    wa_text="Assalam o Alaikum, mujhe apne business ke withholding tax (deduction aur quarterly statements) mein madad chahiye.",
)


REC = dict(
    slug=K_SLUG,
    title="Sole Proprietor Records: What FBR Expects You to Keep",
    h1="Sole Proprietor Records and Books in Pakistan: What FBR Expects You to Keep, and for How Long",
    crumb="Sole Proprietor Records",
    description="Records a sole proprietor must keep for income tax and sales tax: six-year retention, receipts that protect deductions, invoices and a simple filing system.",
    keywords="sole proprietor records Pakistan, section 174 records six years, books of accounts small business Pakistan, sales tax records section 24, FBR audit records",
    category="Sole Proprietorship",
    icon="🗂️",
    read="10 min read",
    banner="Records are what turn a return into a defensible return. The law requires six years of them, and longer if a case is pending.",
    tldr=("Section 174 of the Income Tax Ordinance requires every taxpayer to keep the accounts, documents and records prescribed, in Pakistan, for six years after "
          "the end of the tax year they relate to, and until any pending proceeding is finally decided. The Commissioner can disallow or reduce a deduction if you "
          "cannot produce a receipt or other evidence without reasonable cause. Sales tax registered persons keep their sales tax records for six years after the "
          "tax period under Section 24 of the Sales Tax Act. For income, assets or expenses covered by Section 111(2)(ii), the time limit does not apply."),
    lead=("Most disputes between small businesses and FBR are not about the law but about evidence. A sole proprietor who can show where each rupee came from and "
          "went usually wins; one who cannot often loses deductions even for genuine expenses. This guide explains what the law requires and how to keep records "
          "in a way that is simple enough to actually do."),
    body=f"""
{SERIES}

<h2 id="law">What the Law Requires</h2>
{table(["Rule", "What it says", "Source"], [
    ["Keep prescribed records in Pakistan", "Every taxpayer maintains in Pakistan the accounts, documents and records prescribed, unless the Commissioner authorises otherwise.", "ITO s.174(1)"],
    ["Evidence for deductions", "A deduction can be disallowed or reduced if, without reasonable cause, you cannot provide a receipt or other record or evidence. 'Deduction' includes any amount debited to trading, manufacturing, receipts and expenses, or profit and loss account.", "ITO s.174(2) and (4)"],
    ["Six years", "Keep records for six years after the end of the tax year, and until any pending proceeding (assessment, appeal, revision, reference, petition, prosecution or ADR) is finally decided.", "ITO s.174(3)"],
    ["No time limit in some cases", "The six-year limit does not apply to records about income, assets, expenses or transactions covered by s.111(2)(ii).", "ITO s.174(3) proviso"],
    ["Electronic systems", "FBR may require a person or class to install and use a prescribed electronic resource to record transactions.", "ITO s.174(5)"],
    ["Sales tax records", "Registered persons keep sales tax records and documents for six years after the tax period, or until proceedings are finalised.", "STA s.24"],
])}

<h2 id="what-to-keep">What a Sole Proprietor Should Keep</h2>
{table(["Record", "Why it matters"], [
    ["Sales invoices or cash memos, and a daily sales summary", "Supports the turnover in your return and, if registered, your sales tax returns."],
    ["Purchase invoices and supplier bills", "Supports cost of sales; without them, purchases can be disallowed."],
    ["Expense receipts: rent, utilities, salaries, transport, repairs", "Each is a 'deduction' under s.174(4) and needs evidence."],
    ["Bank statements for business accounts", "The bank trail is the first thing an officer checks against declared income."],
    ["Withholding certificates and deposit slips", "Tax deducted from you is a credit only if you can prove it; tax you deducted from others must match your statements."],
    ["Stock records", "Opening and closing stock drive the profit figure for trading and manufacturing businesses."],
    ["Asset purchase documents", "Support depreciation and the wealth statement."],
    ["Rent agreement, utility connections, licences", "Support the business address and the nature of business."],
    ["Copies of returns, wealth statements and notices", "Needed for revisions, refunds and replies."],
])}

<h2 id="system">A Simple System That Works</h2>
<ol>
<li><strong>Separate bank account</strong> for the business, used for every business receipt and payment where possible.</li>
<li><strong>One folder per month</strong>, physical or digital, with sales, purchases, expenses and bank statement.</li>
<li><strong>Scan or photograph receipts</strong> the day you get them. Paper fades.</li>
<li><strong>Monthly summary</strong> of sales, purchases, expenses and drawings. It takes an hour and makes the annual return straightforward.</li>
<li><strong>Annual archive</strong> labelled by tax year, kept for at least six years after the year ends.</li>
</ol>

<h2 id="by-business">Key Records by Type of Business</h2>
{table(["Business", "Records that carry the most weight"], [
    ["Retail shop", "Daily sales summary or POS reports, purchase bills from suppliers, stock count at year end, electricity bills (relevant to Tier-1 tests)"],
    ["Small manufacturer", "Raw material purchases, production and stock registers, wage records, utility connections (relevant to the cottage industry test)"],
    ["Service business or freelancer", "Client invoices or contracts, bank receipts, foreign remittance records where relevant"],
    ["Online seller", "Marketplace settlement reports, courier cash-on-delivery statements, refunds and returns records"],
    ["Wholesaler or distributor", "Sales and purchase invoices, delivery challans, withholding certificates from buyers, sales tax returns if registered"],
])}

<h2 id="cash">Cash Payments and Drawings</h2>
<p>Cash is where small businesses lose most arguments. Pay suppliers and staff through the bank where you can, record cash expenses on the day with the payee's name, and record the owner's drawings separately from business expenses. Money you take out for household spending is not a business expense, and it must line up with your wealth statement.</p>

<h2 id="audit">When Records Are Asked For</h2>
<p>Officers usually ask for records through a notice: to explain income, to support a deduction, or as part of an audit. Reply on time, provide what is asked in an organised form, and keep a copy of what you submitted. Our {a(X['notice'], 'FBR notice defence service')} prepares replies where the records are complex.</p>

<h2 id="mistakes">Common Record-Keeping Mistakes</h2>
<ul>
<li>Throwing records away after five years. The income tax period is six years, and longer while a case is pending.</li>
<li>Keeping only bank statements, not the invoices behind them.</li>
<li>Running business payments through a family member's account.</li>
<li>Claiming round-figure expenses with no receipts.</li>
</ul>

<h2 id="how-we-help">How We Help</h2>
<p>We set up simple monthly record systems for sole proprietors, prepare the annual accounts and {a(X['ret'], 'tax return')}, and organise records when a notice arrives. Replies within office hours.</p>
""",
    faqs=[
        ("How long must a sole proprietor keep records?",
         "Six years after the end of the tax year under Section 174(3), and until any pending proceeding is finally decided."),
        ("What happens if I cannot produce a receipt for an expense?",
         "Under Section 174(2), the Commissioner may disallow or reduce the deduction if you cannot provide a receipt or other evidence without reasonable cause."),
        ("Do I need to keep sales tax records separately?",
         "Registered persons keep sales tax records for six years after the tax period under Section 24 of the Sales Tax Act. The same documents often serve both taxes."),
        ("Can I keep records digitally?",
         "Digital copies are practical, but the law requires records to be maintained in Pakistan and producible when asked. FBR can also require specific electronic systems under Section 174(5)."),
        ("Are bank statements enough?",
         "Usually not. Bank statements show money moving; invoices, receipts and contracts show what it was for."),
        ("Does the six-year limit always apply?",
         "No. It does not apply to records of income, assets, expenses or transactions covered by Section 111(2)(ii), and records must be kept while proceedings are pending."),
    ],
    sources=[S_ITO, S_STA],
    related=[(S['reg'], "Sole Proprietorship Registration"), (X['ret'], "Sole Proprietor Tax Return"), (S['wht'], "Withholding Duties")],
    cta_h="Get Your Books in Order",
    cta_p="A simple monthly record system and an annual return that your records can defend.",
    wa_text="Assalam o Alaikum, mujhe apne business ke records aur accounts set up karwane hain.",
)


CLOSE = dict(
    slug=C_SLUG,
    title="Close a Sole Proprietorship: Remove Business From NTN",
    h1="Closing or Changing a Sole Proprietorship: Removing a Business From Your NTN and Ending Sales Tax Registration",
    crumb="Close a Sole Proprietorship",
    description="Closing a sole proprietorship: discontinuance at your RTO, sales tax de-registration and final return, the last income tax return, and records to keep.",
    keywords="close sole proprietorship Pakistan, remove business from NTN, discontinuance of business FBR, STRN deregistration section 21, final sales tax return section 28",
    category="Sole Proprietorship",
    icon="🔚",
    read="9 min read",
    banner="Stopping trading does not end your tax obligations. A business has to be formally discontinued with FBR, and any sales tax registration closed properly.",
    tldr=("FBR's guidance says discontinuance of business and deregistration cannot be done through the online Form 181; you visit your Regional Tax Office with "
          "relevant documents. If you hold an STRN, de-registration is under Section 21 of the Sales Tax Act, and Section 28 requires a final sales tax return "
          "before de-registration. Your income tax return for the year the business closes must still be filed, with the closing stock, assets and bank balances "
          "reflected in the wealth statement. Records must be kept for six years after the relevant tax year, under Section 174 and Section 24."),
    lead=("Owners who stop trading often simply close the shop and stop filing. Monthly sales tax returns then go unfiled, notices follow, and the NTN still shows a "
          "business that no longer exists. Closing properly takes a few steps and avoids years of follow-up."),
    body=f"""
{SERIES}

<h2 id="before">Before You Close: Decide What Is Changing</h2>
{table(["Situation", "What to do"], [
    ["The business has stopped for good", "Discontinue it with FBR at your RTO, de-register sales tax if registered, file final returns."],
    ["You are moving to a new address", "Update the business address through Form 181 on IRIS; no closure needed."],
    ["One branch closes, others continue", "Update the branches on your registration; the business continues."],
    ["You are converting to a company", "The new company registers separately; the sole proprietorship is then discontinued. See {link_secp}."],
    ["You are changing the line of business", "Update the nature of business and check whether sales tax obligations change."],
])}

<h2 id="income-tax">Step 1: Discontinue the Business for Income Tax</h2>
<p>FBR's page on changing registration details lists <strong>discontinuance of business</strong> and <strong>deregistration</strong> among changes that require a visit to your Regional Tax Office with the relevant documents, rather than the online Form 181. Prepare:</p>
<ul>
<li>A written application stating the business name, NTN (CNIC) and date trading stopped.</li>
<li>Evidence of closure, such as the end of the rent agreement, disconnection of commercial utilities, or closure of the business bank account.</li>
<li>Copies of the last filed returns.</li>
</ul>
<p>Your personal NTN continues. You remain an individual taxpayer; only the business is removed.</p>

<h2 id="sales-tax">Step 2: End Sales Tax Registration (If You Have an STRN)</h2>
<ol>
<li><strong>Check you are no longer required to be registered.</strong> Section 21(1) allows FBR, subject to the rules, to de-register persons not required to be registered.</li>
<li><strong>File any outstanding monthly returns</strong>, including nil returns.</li>
<li><strong>File the final return.</strong> Section 28 requires a person applying for de-registration to furnish a final return in the form, manner and time the Commissioner directs.</li>
<li><strong>Settle sales tax on remaining stock and assets</strong> as the final return requires, and pay any balance.</li>
<li><strong>Keep the de-registration order</strong> with your records.</li>
</ol>
<p>Until de-registration is complete, monthly returns remain due, and a gap of unfiled returns can lead to penalties and to the registration being suspended rather than closed.</p>

<h2 id="final-return">Step 3: The Last Income Tax Return</h2>
<p>The business's income up to the date of closure is declared in your normal annual return for that tax year. Points to get right:</p>
<ul>
<li>Closing stock sold, taken for personal use or written off.</li>
<li>Business assets sold or kept, with any gain declared.</li>
<li>Money withdrawn from the business shown correctly in the wealth statement reconciliation.</li>
<li>Withholding certificates for tax deducted from you up to closure, claimed as credits.</li>
<li>If you were a withholding agent, final quarterly statements filed (see our {{link_wht}}).</li>
</ul>

<h2 id="records">Step 4: Keep the Records</h2>
<p>Closing the business does not shorten record-keeping duties. Income tax records are kept for six years after the end of the tax year under Section 174, and sales tax records for six years after the tax period under Section 24, longer if any proceeding is pending. Store the closure documents with them.</p>

<h2 id="timeline">Example Timeline</h2>
{table(["When", "Step"], [
    ["Week before closing", "Count and value stock; decide what is sold, kept or written off. Settle supplier and staff dues."],
    ["Closing date", "Stop trading; issue final invoices; note the date in writing."],
    ["Within the month", "File the monthly sales tax return; apply for de-registration and file the final return as directed."],
    ["Next few weeks", "Visit the RTO with the discontinuance application and closure evidence."],
    ["After tax is settled", "Close the business bank account."],
    ["Return season", "File the income tax return for the year, with the closing position in the wealth statement."],
])}
<p>The order matters: closing the bank account before final returns are filed and tax paid makes the last steps harder.</p>

<h2 id="mistakes">Mistakes to Avoid</h2>
<ul>
<li>Stopping sales tax returns without de-registration.</li>
<li>Closing the bank account before final returns are filed and tax paid.</li>
<li>Leaving the business on the NTN, so FBR still expects business income.</li>
<li>Discarding records once the shop is shut.</li>
</ul>

<h2 id="how-we-help">How We Help</h2>
<p>We prepare RTO discontinuance applications, final sales tax returns and de-registration, and the last income tax return with a reconciled wealth statement. Replies within office hours.</p>
""".replace("{link_secp}", a(X['secp'], 'our SECP versus sole proprietorship guide')).replace("{link_wht}", a(S['wht'], 'withholding guide')),
    faqs=[
        ("Can I remove my business from my NTN online?",
         "No. FBR's guidance says discontinuance of business and deregistration require a visit to your Regional Tax Office with relevant documents."),
        ("Does closing my business cancel my NTN?",
         "No. Your CNIC remains your NTN as an individual. Only the business is discontinued."),
        ("How do I cancel my STRN?",
         "De-registration is under Section 21 of the Sales Tax Act for persons not required to be registered, and Section 28 requires a final return before de-registration."),
        ("Do I still file sales tax returns after closing the shop?",
         "Yes, until de-registration is complete. Unfiled returns can lead to penalties."),
        ("Do I need to file an income tax return for the year I closed?",
         "Yes. Income up to the closure date is declared in your annual return, and the wealth statement must reflect the closing position."),
        ("How long should I keep the closed business's records?",
         "Six years after the relevant tax year or tax period, under Section 174 of the Income Tax Ordinance and Section 24 of the Sales Tax Act, and longer if proceedings are pending."),
    ],
    sources=[S_181, S_STA, S_ITO, S_IRIS],
    related=[(S['iris'], "Add a Business to Your NTN"), (S['stx'], "Sole Proprietor STRN"), (S['rec'], "Sole Proprietor Records")],
    cta_h="Closing a Business? Do It Once, Properly",
    cta_p="RTO discontinuance, STRN de-registration with final return, and your last income tax return.",
    wa_text="Assalam o Alaikum, mujhe apna business band karna hai, NTN se remove aur STRN cancel karwana hai.",
)

POSTS = [REG, IRISP, STX, WHT, REC, CLOSE]
