"""Three DNFBP / AML-CFT guides (facts checked 9 November 2026 against FBR, FMU and SRO texts linked in each post)."""

WA = "https://wa.me/923284675162"

S_INTRO = ("FBR: Introduction to AML/CFT and DNFBPs", "https://www.fbr.gov.pk/introduction-aml-cft/152366/152367")
S_REGS = ("FBR: AML/CFT legislation, regulations and sector guidelines", "https://www.fbr.gov.pk/aml-cft-legislation-regulations/152366/152370")
S_FAQ23 = ("FBR Directorate General DNFBPs: Frequently Asked Questions (February 2023)", "https://download1.fbr.gov.pk/Docs/20233281432019788FrequentlyAskedQuestions(FAQs)-February2023.pdf")
S_950 = ("FBR: AML/CFT Sanctions Rules 2020, S.R.O. 950(I)/2020", "https://download1.fbr.gov.pk/Docs/202010151510533067AML-CFT-Sanction-Rules-2020-SRO-NO-950I-2020.pdf")
S_1497 = ("FBR: S.R.O. 1497(I)/2026, jurisdiction of DNFBP authorities (2 September 2026)", "https://download1.fbr.gov.pk/Docs/2026916149312406SRO1497-2026JurisdictionofDNFBPAuthorities.pdf")
S_REDF = ("FBR: Red flag indicators for DNFBPs", "https://www.fbr.gov.pk/red-flag-indicators-dnfbps/152366/152797")
S_GOAML = ("Financial Monitoring Unit: goAML reporting portal", "https://goamlweb.fmu.gov.pk/PRD/Home")
S_IRIS = ("FBR IRIS portal", "https://iris.fbr.gov.pk/")
S_REA_SG = ("FBR: Short Guidance on AML/CFT Obligations for Real Estate Agents (2021)", "https://download1.fbr.gov.pk/Docs/2021915091332570ShortGuidanceForREAs.pdf")
S_REA_GL = ("FBR: AML/CFT Guidelines for Real Estate Agents (updated July 2021)", "https://download1.fbr.gov.pk/Docs/2021821683014134AML-CFTRealEstateAgentsUpdatedJuly2021.pdf")
S_REA_RF = ("FMU: Red Flag Indicators for the Real Estate Sector", "https://download1.fbr.gov.pk/Docs/202117141328829Red-Flag-Indicators-for-Real-Estate-Sector.pdf")
S_DPMS_SG = ("FBR: Short Guidance for Dealers in Precious Metals and Stones", "https://download1.fbr.gov.pk/Docs/2022826883123108ShortGuidance-DPMS.pdf")
S_DPMS_GL = ("FBR: AML/CFT Guidelines for Dealers in Precious Metals and Stones (updated July 2021)", "https://download1.fbr.gov.pk/Docs/2021821683329217AML-CFT_DPMSUpdatedJuly,2021.pdf")
S_DPMS_RF = ("FMU: Red Flag Indicators for Jewelers and Precious Metals / Stones Dealers", "https://download1.fbr.gov.pk/Docs/202117141659214Red-Flag-Indicators-for-Jewelers-and-Precious-Stones-or-Metal-Dealers-Final.pdf")

P_SLUG = "dnfbp-registration-pakistan"
R_SLUG = "real-estate-agent-dnfbp-registration-aml-pakistan"
J_SLUG = "jeweller-dnfbp-registration-aml-pakistan"
L = {
    "pillar": "/blogs/" + P_SLUG, "rea": "/blogs/" + R_SLUG, "jew": "/blogs/" + J_SLUG,
    "ntn": "/ntn-registration", "stx": "/sales-tax-registration", "notice": "/fbr-notice-defense",
    "rea_tax": "/blogs/real-estate-agent-tax-pakistan", "dealers_lhr": "/blogs/tax-return-filing-property-dealers-lahore",
    "rea_lhr": "/blogs/tax-consultant-real-estate-agents-lahore", "dev": "/blogs/real-estate-developer-tax-pakistan",
    "236": "/blogs/property-transfer-tax-2026-27-pakistan-236c-236k", "gold": "/blogs/tax-on-gold-jewelry-pakistan",
    "atl": "/atl-pakistan-guide",
}


def a(href, text):
    return f'<a href="{href}" style="color:#0D9488;font-weight:600;text-decoration:underline">{text}</a>'


def ext(src):
    return f'<a href="{src[1]}" target="_blank" rel="noopener" style="color:#0D9488;font-weight:600">{src[0].split(": ", 1)[-1]}</a>'


def table(head, rows):
    h = "".join(f"<th>{x}</th>" for x in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div style="overflow-x:auto;-webkit-overflow-scrolling:touch"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


# ─────────────────────────────── PILLAR ───────────────────────────────
PILLAR = dict(
    slug=P_SLUG,
    title="DNFBP Registration in Pakistan 2026: Complete FBR Guide",
    h1="DNFBP Registration in Pakistan 2026: Who Must Register With FBR and What Comes After",
    crumb="DNFBP Registration Guide",
    description="Who counts as a DNFBP, how FBR registration works, and the AML duties that follow: CDD, screening, STR/CTR on goAML, records and penalties up to Rs 100m.",
    keywords="DNFBP registration Pakistan, FBR DNFBP registration, DNFBP registration 2026, AML CFT compliance Pakistan, DNFBP real estate jeweller accountant, goAML registration",
    category="AML/CFT — DNFBPs",
    icon="🛡️",
    read="14 min read",
    banner="Real estate agents, builders, jewellers and non-ICAP/ICMAP accountants are supervised by FBR for anti-money laundering. Registration is the first step, not the last.",
    tldr=("DNFBP means Designated Non-Financial Businesses and Professions. Under the Anti-Money Laundering Act, 2010 and FBR's AML/CFT Regulations "
          "(S.R.O. 924(I)/2020), FBR supervises three groups: real estate agents (including builders and developers when they deal in property), dealers in precious "
          "metals and stones who take cash of Rs 2 million or more in a transaction, and accountants not regulated by ICAP or ICMAP when they carry out listed activities. "
          "These businesses must register with FBR, appoint a compliance officer, check customers (CDD), screen them against sanctions lists, report suspicious and "
          "large cash transactions to the Financial Monitoring Unit on goAML, and keep records for 5 to 10 years. The Sanctions Rules allow penalties of up to "
          "Rs 100 million per violation."),
    lead=("Most property dealers and jewellers in Pakistan already know about NTN, income tax returns and the Active Taxpayers List. DNFBP registration is a separate "
          "regime with a different purpose: it is about preventing money laundering and terrorist financing, not collecting tax. This guide explains, from FBR's own "
          "regulations, FAQs and sector guidance, who is covered, how registration works, the duties that start the day you register, and how FBR enforces them."),
    body=f"""
<h2 id="what-is-dnfbp">What a DNFBP Is, in Plain Terms</h2>
<p>Banks have long been required to know their customers and report suspicious transactions. Money launderers responded by moving value through businesses that handle large sums outside the banking system: property deals, gold and jewellery, and professionals who set up companies or manage client money. The Financial Action Task Force (FATF) calls these businesses <strong>Designated Non-Financial Businesses and Professions</strong>, and Pakistan brought them into its anti-money laundering law to meet FATF standards.</p>
<p>The legal base is Section 2(xii)(a), (b) and (c) of the Anti-Money Laundering Act, 2010 (AMLA). FBR is the AML/CFT regulatory authority for these three categories, and it issued the <strong>FBR AML/CFT Regulations for DNFBPs</strong> through S.R.O. 924(I)/2020 on 29 September 2020. A Directorate General of DNFBPs inside FBR handles registration, supervision, inspections and sanctions. Other DNFBPs, such as lawyers and chartered accountants, are supervised by their own bodies, not by FBR.</p>

<h2 id="who-must-register">Who Must Register With FBR</h2>
<p>The test is the <em>activity</em>, not the label on your shop. FBR's February 2023 FAQs and its sector guidance define each group as follows:</p>
{table(["Category", "You are a DNFBP when you…", "Not covered (examples)"], [
    ["<strong>Real estate agents (REAs)</strong>", "Execute the purchase or sale of real property, take part in a real estate transaction in that capacity, or carry on professional activity for a property transfer. FBR's short guidance says this includes <strong>builders, real estate developers, brokers and property dealers</strong>.", "Someone selling their own house once, with no business of dealing in property."],
    ["<strong>Dealers in precious metals and stones (DPMS)</strong>", "Deal in bullion, jewellery, gold, platinum, diamonds, precious or semi-precious stones or pearls <strong>and</strong> engage in a <strong>cash transaction of Rs 2 million or more</strong> with a customer.", "A jeweller whose cash dealings with every customer always stay below Rs 2 million (but see the warning on split payments below)."],
    ["<strong>Accountants (non-ICAP / ICMAP)</strong>", "Sole practitioners, partners or employees of firms who buy or sell real estate for clients, manage client money, securities or accounts, organise contributions for companies, create or manage companies, trusts or waqf, or act as formation agents, among 14 activities listed by FBR.", "Members regulated by ICAP or ICMAP (supervised by their institutes). Ordinary tax return and tax advisory work is not one of the listed activities."],
])}
<p><strong>A warning on thresholds.</strong> The Rs 2 million cash test for jewellers is per transaction with a customer, but FMU's red flags treat a series of smaller payments that add up to a large amount as suspicious in itself. Splitting a sale to stay under the limit does not take a business out of the regime; it creates a reporting problem.</p>
<p>For sector detail, read our guides for {a(L['rea'], 'real estate agents and property dealers')} and {a(L['jew'], 'jewellers and gold dealers')}.</p>

<h2 id="registration">How DNFBP Registration Works</h2>
<p>The FBR AML/CFT Regulations (S.R.O. 924(I)/2020) require every DNFBP to be registered with FBR and to give FBR whatever information it needs to register the business and keep the registration up to date, <strong>including the criminal record of senior management and beneficial owners</strong>. Registration is done online on FBR's IRIS portal, where the business uses its existing taxpayer login. A practical sequence:</p>
<ol>
<li><strong>Get your tax registration in order.</strong> You need an NTN and IRIS login for the individual, firm (AOP) or company that runs the business. If you do not have one, start with {a(L['ntn'], 'NTN registration')}.</li>
<li><strong>Identify who must be declared.</strong> The owner or partners, directors, and any natural person who ultimately owns or controls the business (the beneficial owner), plus the person you will appoint as compliance officer.</li>
<li><strong>Collect documents.</strong> CNICs of owners, partners or directors; business address and contact details; the registration documents of the firm or company where applicable; and character or criminal-record certificates for senior management and beneficial owners, since the Regulations require that information.</li>
<li><strong>Complete the DNFBP registration in IRIS</strong> for your category (real estate agent, dealer in precious metals and stones, or accountant) and submit it with the attachments. Menu names in IRIS change from time to time; if the option is hard to find, the DNFBP helpline below can guide you.</li>
<li><strong>Register on goAML separately.</strong> Reports go to the Financial Monitoring Unit (FMU), not FBR, through goAML. FBR's FAQs say every reporting entity must register on goAML to file STRs and CTRs. Do this straight after FBR registration, before you need to file anything.</li>
<li><strong>Keep the registration current.</strong> Inform FBR when owners, partners, directors, the compliance officer or the business address change.</li>
</ol>
<p>Which FBR office supervises you depends on where the business operates. Under S.R.O. 1497(I)/2026 dated 2 September 2026, the Directorate General has all-Pakistan jurisdiction, with Directors at Islamabad, Karachi, Lahore and Quetta. The Lahore Directorate, for example, covers businesses within the jurisdiction of RTO-I and RTO-II Lahore, CTO Lahore, LTO Lahore and Multan, and the RTOs of Sialkot, Gujranwala, Faisalabad, Sargodha, Multan, Sahiwal and Bahawalpur.</p>

<h2 id="obligations">The Eight Duties That Start After Registration</h2>
{table(["Duty", "What FBR expects", "Legal reference"], [
    ["1. Risk assessment", "Assess the money laundering, terrorist financing and proliferation financing risks you face from customers, areas, products and delivery channels, using Pakistan's National Risk Assessment.", "Reg. 4(1), S.R.O. 924(I)/2020"],
    ["2. Policies and controls", "Written policies, controls and procedures to manage those risks; enhanced measures for higher risks, simplified measures only for lower risks and never when there is suspicion.", "Reg. 4(2)"],
    ["3. Compliance officer", "A senior management person as AML/CFT compliance officer, with contact details shared with FBR. A sole proprietor with no employees is deemed the compliance officer.", "Reg. 7(1); AMLA s.7G; FBR Condition No. 3 (2022)"],
    ["4. Customer due diligence (CDD)", "Identify and verify each customer and beneficial owner, the purpose of the relationship and, for higher-risk customers, the source of funds and wealth.", "AMLA s.7A(1); Reg. 8(1)"],
    ["5. Sanctions screening", "Screen customers, their beneficial owners and agents against UN Security Council and domestic proscribed lists. On a true match: freeze, refuse, file an STR and tell FBR immediately.", "AMLA; FBR TFS guidance"],
    ["6. STR and CTR reporting", "Suspicious transaction reports (including attempted transactions) and currency transaction reports for cash of Rs 2 million or more, filed with FMU on goAML.", "AMLA s.7"],
    ["7. Record keeping", "CDD and relationship records for at least 5 years; STR and CTR records for at least 10 years from filing.", "FBR FAQs Q54"],
    ["8. Staff screening, training and audit", "Screen staff when hiring, train them regularly, and have an independent check of the system.", "Reg. 7(1)"],
])}

<h2 id="cdd">Customer Due Diligence: What to Collect</h2>
<p>FBR's sector guidance sets out a CDD form and lists the information for each type of customer:</p>
<ul>
<li><strong>Individuals:</strong> full name, date of birth, residential address, CNIC, NICOP, POC or passport number, whether they act for themselves or someone else, purpose of the relationship, beneficial ownership and, for higher-risk customers and PEPs, the source of wealth or funds. Verification can use the CNIC, NADRA verification services, utility bills, bank statements, tax documents or salary slips.</li>
<li><strong>Companies and other legal persons:</strong> name, registration number, taxpayer number, business address, nature of business, ownership and control structure, and the natural persons who ultimately own or control it, verified from the incorporation certificate, memorandum and articles, FBR documents and the company's register of ultimate beneficial owners.</li>
</ul>
<p>How often to review a customer depends on risk. FBR's FAQs give a guide: at least once a year for high-risk customers, every two years for medium risk and every three years for low risk, or sooner when something changes. You may rely on another regulated party's CDD in limited cases, but you stay responsible for it.</p>

<h2 id="high-risk">Higher-Risk Customers and Enhanced Due Diligence</h2>
<p>Enhanced due diligence (EDD) means more questions, better evidence and senior management approval before you start or continue the relationship. FBR's guidance points to these as higher risk:</p>
<ul>
<li><strong>Politically exposed persons (PEPs)</strong>, meaning people who hold or held a prominent public function in Pakistan, abroad or in an international organisation, and their family members and close associates.</li>
<li>Customers whose beneficial owner is unclear because of a complex ownership chain.</li>
<li>Links to countries that FATF has listed for countermeasures or enhanced due diligence.</li>
<li>Unknown NGOs, or NGOs exposed to terrorist financing abuse.</li>
<li>Customers in high-risk businesses, or with adverse media reports.</li>
</ul>
<p>Source-of-wealth evidence can include a bank statement showing where funds came from, a sale deed for a property sold earlier, a wealth statement, inheritance papers, or audited accounts of a business.</p>

<h2 id="reporting">STR and CTR on goAML</h2>
{table(["Report", "When to file", "Points to remember"], [
    ["<strong>STR</strong> (Suspicious Transaction Report)", "Promptly, when you know, suspect or have reason to suspect that funds come from crime, are linked to terrorism, are meant to evade reporting, or have no apparent lawful purpose.", "Covers attempted transactions too. File with FMU only, not FBR. Decline the business where suspicion arises."],
    ["<strong>CTR</strong> (Currency Transaction Report)", "When a customer transaction involves cash equal to Rs 2 million or more.", "Threshold based: no suspicion needed. Keep the record for 10 years."],
])}
<p><strong>Tipping off is an offence.</strong> Owners, officers and staff must not tell the customer, directly or indirectly, that a report has been or will be filed. Once you file an STR, your role is complete; any investigation is for FMU or the investigating agency, and FMU must keep the reporter's identity confidential under AMLA.</p>

<h2 id="penalties">Inspections and Penalties</h2>
<p>FBR's DNFBP teams inspect registered businesses for compliance. The AML/CFT Sanctions Rules, 2020 (S.R.O. 950(I)/2020) set out what FBR may do when it finds a breach:</p>
<ul>
<li>A monetary penalty of <strong>up to Rs 100 million per violation</strong>, worked out on a risk-based penalty scale.</li>
<li>Conditions, limits or restrictions on the business, or de-registration.</li>
<li>A warning, suspension or removal of a person in management.</li>
<li>A censure or reprimand, or directions such as a remedial plan with a deadline.</li>
</ul>
<p>A sanction must be given by written notice that states the violation and your right of appeal. Significant sanctions are published quarterly, with the name of the business, which can hurt a property or jewellery business more than the fine itself. Unpaid penalties can lead to further sanctions.</p>

<h2 id="checklist">A 30-Day Compliance Checklist After Registration</h2>
<ol>
<li><strong>Week 1:</strong> appoint the compliance officer and share their details with FBR. Register on goAML.</li>
<li><strong>Week 1–2:</strong> write a short risk assessment for your business: who your customers are, where they come from, how they pay, and which deals carry more risk.</li>
<li><strong>Week 2:</strong> adopt an AML/CFT policy covering CDD, EDD, screening, reporting, record keeping and training. Keep it practical and specific to your business.</li>
<li><strong>Week 3:</strong> start using a CDD form for every customer, and set up sanctions screening using the lists FBR points to, including its DNFBP mobile app.</li>
<li><strong>Week 4:</strong> train your staff, set up a file or folder system that keeps records for the required period, and diary the next review.</li>
</ol>

<h2 id="tax-link">How DNFBP Rules Sit Alongside Your Tax Duties</h2>
<p>DNFBP registration does not replace your income tax return, and a tax return does not register you as a DNFBP. The two systems do meet, though: the CDD you collect, the source of funds you record and the cash you receive should match what appears in your own return and wealth statement. Property dealers should also understand the advance tax on property under {a(L['236'], 'Sections 236C and 236K')}, and jewellers the rules in our guide to {a(L['gold'], 'tax on gold and jewellery')}.</p>

<h2 id="how-we-help">How Kamboh Associates Can Help</h2>
<ul>
<li>Check whether your business falls in a DNFBP category, and in which one.</li>
<li>Prepare and file the DNFBP registration on IRIS, and register you on goAML.</li>
<li>Draft a risk assessment, an AML/CFT policy and a CDD form fitted to your business.</li>
<li>Prepare a reply if you receive a DNFBP notice or an inspection letter, alongside your regular tax work.</li>
</ul>
<p>We work over WhatsApp or at our office in Awan Town, Lahore, and reply within office hours.</p>
""",
    faqs=[
        ("What does DNFBP stand for?",
         "Designated Non-Financial Businesses and Professions. In Pakistan, FBR supervises three of them for anti-money laundering: real estate agents (including builders and developers when dealing in property), dealers in precious metals and stones, and accountants not regulated by ICAP or ICMAP."),
        ("Is DNFBP registration the same as NTN or sales tax registration?",
         "No. NTN and sales tax registration are for tax. DNFBP registration is under the Anti-Money Laundering Act, 2010 and FBR's AML/CFT Regulations, and brings duties such as customer due diligence and reporting to FMU. You normally need an NTN and IRIS login first."),
        ("Does a jeweller have to register if most sales are below Rs 2 million?",
         "A jeweller is a DNFBP when it engages in a cash transaction of Rs 2 million or more with a customer. If that ever happens, or could happen, register. Breaking one sale into smaller cash payments is itself a red flag for FMU."),
        ("Are builders and developers DNFBPs?",
         "Yes, when they deal in property. FBR's short guidance for real estate agents states that the category includes builders, real estate developers, brokers and property dealers when they execute the purchase or sale of real property."),
        ("Do tax consultants have to register as DNFBPs?",
         "Not for tax work alone. Non-ICAP/ICMAP accountants are DNFBPs only when they carry out listed activities such as managing client money, forming or managing companies or trusts, or buying and selling property for clients. Ordinary tax returns and tax advice are not on the list."),
        ("Who can be the AML/CFT compliance officer?",
         "A person in senior management, such as the sole proprietor, CEO, managing partner, or a partner or employee with enough knowledge and authority. A sole proprietor with no employees is deemed to be the compliance officer."),
        ("Where are STRs and CTRs filed?",
         "With the Financial Monitoring Unit on its goAML portal (goamlweb.fmu.gov.pk), not with FBR. Each DNFBP must register on goAML first."),
        ("How long must DNFBP records be kept?",
         "Customer due diligence and relationship records for at least five years, and records of STRs and CTRs for at least ten years from the date of filing, according to FBR's 2023 FAQs."),
        ("What is the penalty for not complying?",
         "Under the AML/CFT Sanctions Rules, 2020, FBR may impose a monetary penalty of up to Rs 100 million per violation on a risk-based scale, along with restrictions, de-registration or action against management. Significant sanctions are published every quarter."),
    ],
    sources=[S_INTRO, S_REGS, S_FAQ23, S_950, S_1497, S_REA_SG, S_DPMS_SG, S_REDF, S_GOAML, S_IRIS],
    related=[(L['rea'], "DNFBP Rules for Real Estate Agents"), (L['jew'], "DNFBP Rules for Jewellers"), (L['ntn'], "NTN Registration")],
    cta_h="Need DNFBP Registration or an AML Policy?",
    cta_p="We check your category, file the IRIS registration, set up goAML and draft the policy and CDD form.",
    wa_text="Assalam o Alaikum, mujhe DNFBP registration (FBR AML/CFT) ke bare mein madad chahiye.",
)


# ─────────────────────────────── REAL ESTATE ───────────────────────────────
REA = dict(
    slug=R_SLUG,
    title="Real Estate Agent DNFBP Registration & AML Rules Pakistan",
    h1="Real Estate Agents and Property Dealers: DNFBP Registration and AML Rules in Pakistan",
    crumb="DNFBP for Real Estate Agents",
    description="DNFBP rules for estate agents, property dealers, builders and developers: FBR registration, buyer and seller CDD, red flags, cash CTRs and records.",
    keywords="real estate agent DNFBP registration, property dealer DNFBP FBR, AML rules real estate Pakistan, builder developer DNFBP, estate agent CDD form Pakistan",
    category="AML/CFT — Real Estate",
    icon="🏘️",
    read="12 min read",
    banner="Property dealers, brokers, builders and developers who execute property purchases or sales fall under FBR's AML/CFT regime, in addition to their tax obligations.",
    tldr=("FBR treats real estate agents as DNFBPs when they execute or take part in the purchase or sale of real property, and its guidance names builders, developers, "
          "brokers and property dealers. Each must register with FBR, appoint a compliance officer, carry out CDD on the buyer and seller, screen them against sanctions "
          "lists, report suspicious deals (including deals that fall through) and cash of Rs 2 million or more to FMU on goAML, and keep the CNICs, sale deed, bank "
          "draft and CDD form on file for at least five years."),
    lead=("Large property deals can move a lot of value in one transaction, which is why the real estate trade was among the sectors FBR "
          "brought under AML supervision when its DNFBP regulations took effect in 2020. This guide is written for estate agents, property dealers, builders and developers. It covers what FBR's real estate guidelines and "
          "FMU's red flags actually ask of you in a deal, step by step. For the general rules that apply to every DNFBP, see our "
          "DNFBP registration guide."),
    body=f"""
<p class="tf-primary"><strong>Main guide:</strong> for the full list of DNFBP categories, the registration process and penalties, see our {a(L['pillar'], 'DNFBP registration guide for Pakistan')}.</p>

<h2 id="who-is-covered">Which Property Businesses Are Covered</h2>
<p>FBR's February 2023 FAQs describe a real estate agent as a DNFBP when an individual or business (i) executes a purchase and sale of real property, (ii) participates in a real estate transaction in that capacity, or (iii) carries on professional activity to bring about a property transfer. FBR's short guidance for real estate agents goes further and says the category <strong>includes builders, real estate developers and property brokers and dealers</strong>.</p>
{table(["Business", "Covered?", "Why"], [
    ["Property dealer or estate agency arranging sales and purchases", "Yes", "Core real estate agent activity."],
    ["Builder or developer selling plots, houses, flats or shops in its own project", "Yes", "FBR's guidance names builders and developers."],
    ["Broker or sub-dealer earning commission on a deal", "Yes", "Takes part in the transaction in a professional capacity."],
    ["Agent who only arranges rentals", "Check your activities", "The FBR definition is about purchase, sale and transfer; if you also handle any sale, you are covered."],
    ["Individual selling their own home once", "No", "Not a business of dealing in property."],
])}
<p>If you are covered, registration, a compliance officer and goAML registration come first. Our {a(L['pillar'], 'main guide')} explains each step.</p>

<h2 id="deal-workflow">AML Steps in a Typical Property Deal</h2>
<p>Here is how FBR's requirements fit into the way a sale actually runs, from first enquiry to the transfer:</p>
<ol>
<li><strong>Enquiry and token.</strong> Before you accept the token money (bayana), identify both the buyer and the seller: CNIC (or NICOP, POC or passport for overseas Pakistanis and foreigners), address, and whether each is acting for themselves or for someone else.</li>
<li><strong>Screen both parties.</strong> Check the names, and any company owners or attorneys, against the UN Security Council consolidated list and Pakistan's proscribed persons and organisations lists. FBR's DNFBP mobile app gives access to these lists.</li>
<li><strong>Rate the risk.</strong> Note whether either party is a PEP, uses a company or trust, lives abroad in a high-risk jurisdiction, or pays in an unusual way. Higher risk means enhanced due diligence.</li>
<li><strong>Ask about the money.</strong> For higher-risk buyers, record where the funds come from: bank account, sale of another property (sale deed), inheritance, business income or savings shown in a wealth statement.</li>
<li><strong>Watch the payment trail.</strong> Record how each payment is made. Cash of Rs 2 million or more in a transaction triggers a CTR to FMU, whether or not anything seems wrong.</li>
<li><strong>Before the transfer.</strong> If anything in the deal raises suspicion, decline it and file an STR. You must file even if the buyer walks away, because attempted transactions are reportable.</li>
<li><strong>After completion.</strong> File the CNICs of the seller and buyer, the sale deed or transfer letter, the bank draft or payment record and the CDD form. Keep them for at least five years after the relationship ends, and keep STR and CTR records for ten years.</li>
</ol>

<h2 id="cdd-documents">CDD Documents for Buyers and Sellers</h2>
{table(["Party", "Identify", "Verify with"], [
    ["Resident individual", "Name, date of birth, address, CNIC, acting for self or another, purpose", "CNIC, NADRA verification, recent utility bill"],
    ["Overseas Pakistani or foreigner", "Same, plus country of residence", "NICOP or POC, passport, alien registration card"],
    ["Company buyer or seller", "Name, registration and taxpayer number, address, nature of business, ownership and control, beneficial owners", "Incorporation certificate, memorandum and articles, FBR documents, register of ultimate beneficial owners"],
    ["Attorney or representative", "Identity of the attorney and of the person they act for", "CNIC of both, the power of attorney"],
    ["High-risk or PEP buyer", "Source of funds and wealth; senior management approval", "Bank statements, previous sale deed, wealth statement, inheritance papers, audited accounts"],
])}

<h2 id="red-flags">Red Flags FMU Lists for the Property Sector</h2>
<p>FMU's red flag indicators for real estate say that one flag alone may not mean money laundering, but a combination, read with the client's profile, may. The ones most often seen in Pakistani deals:</p>
<ul>
<li><strong>Means do not match the deal.</strong> The buyer's or seller's known income or business does not fit the price of the property.</li>
<li><strong>Nominees and benami-style purchases.</strong> Property bought in the name of an associate or relative other than a spouse or child, or for a minor or someone without the means, or for a PEP.</li>
<li><strong>Hidden principal.</strong> The client acts on someone else's instructions without saying who, insists on an intermediary for every step, or uses a power of attorney without a clear reason.</li>
<li><strong>Price out of line.</strong> A sale, by the developer or a sub-sale, far above or below the market value.</li>
<li><strong>Cash pressure.</strong> Payments made in many cash amounts straight into a project account, or a seller who insists on large payments in cash.</li>
<li><strong>Third-party money.</strong> The initial deposit paid by cheque from a third party other than a spouse or parent, or funding from an offshore bank in a high-risk jurisdiction.</li>
<li><strong>Speed and indifference.</strong> Several properties bought or sold in a short period with little interest in location or price, a buyer who never inspects the property, or a deal rushed without reason.</li>
<li><strong>Threshold awareness.</strong> A client who is unusually interested in the reporting limits or AML rules.</li>
<li><strong>Construction that does not add up.</strong> A sale of vacant land and then of a completed building recorded faster than construction could normally take.</li>
</ul>

<h2 id="scenarios">Four Deal Scenarios and What to Do</h2>
<p>These illustrations show how the rules apply in situations agents see every week. The names and amounts are invented.</p>
{table(["Scenario", "What stands out", "What the agent should do"], [
    ["A salaried buyer in Johar Town pays for a Rs 1.5 crore house by bank transfer from their own account, with a home loan for part of it.", "Payment trail is clear and matches the buyer's profile.", "Standard CDD for buyer and seller, sanctions screening, keep the file. No report needed unless something else arises."],
    ["A buyer pays Rs 35 lakh of the token and first instalment in cash at the office.", "Cash of Rs 2 million or more.", "File a CTR on goAML. Record the buyer's CNIC and how the cash was paid. A CTR does not mean the buyer is suspected; it is a threshold report."],
    ["A young relative with no visible income is named as buyer of a commercial plot, while an older family member negotiates and pays.", "Nominee purchase and a hidden principal, both on FMU's list.", "Identify the person paying as well as the named buyer, and ask about the source of funds. If the answers do not hold up, decline and file an STR, without telling the parties."],
    ["An overseas buyer wants to buy three files in a society within a week, does not visit, and asks whether deals above a certain amount are reported.", "Speed, indifference to the property, and interest in reporting limits.", "Apply enhanced due diligence, including source of funds and senior management approval. If suspicion remains, do not proceed and file an STR, even if the deal never completes."],
])}

<h2 id="builders">Extra Points for Builders and Developers</h2>
<p>A developer often deals with the same buyer over months or years through booking, instalments and possession, so the relationship needs ongoing monitoring, not one check at booking. Update the CDD when a buyer's profile changes, for example when they move abroad or become a PEP. Treat transfers of files or allotments before possession with care: the FMU red flags mention sub-sales at prices far from market value, and a file that changes hands several times can hide who really paid. Instalments paid in cash at the project office need the same CTR checks as any other cash.</p>
<p>The tax side of a project is separate; see our guide to {a(L['dev'], 'tax for real estate developers')}.</p>

<h2 id="mistakes">Five Mistakes Property Businesses Make</h2>
<ol>
<li><strong>Collecting only the buyer's CNIC.</strong> The seller is also your customer under FBR's guidance, and FBR expects the seller's CNIC on file.</li>
<li><strong>Doing CDD after the token.</strong> Once money changes hands it is harder to walk away. Identify and screen first.</li>
<li><strong>Telling a client about a report.</strong> Telling a client a deal "has been reported" or "will be reported" is tipping off, which is an offence.</li>
<li><strong>Keeping records in WhatsApp chats only.</strong> Records must be retrievable for five to ten years. Keep a file or folder per deal.</li>
<li><strong>Thinking the registrar or society does it for you.</strong> Transfer authorities have their own role in a transfer, but your duties as a registered agent still apply to the deals you handle.</li>
</ol>

<h2 id="tax">Your Tax Position Is a Separate Matter</h2>
<p>AML compliance does not cover your income tax. Commission income must be declared in your return, and buyers and sellers face advance tax under {a(L['236'], 'Sections 236C and 236K')}. See our guide to {a(L['rea_tax'], 'tax for real estate agents')} and, for Lahore dealers, our page on {a(L['dealers_lhr'], 'tax returns for property dealers')}.</p>

<h2 id="how-we-help">How We Help Property Businesses</h2>
<p>Kamboh Associates registers estate agents, property dealers and developers as DNFBPs on IRIS, sets up goAML, and prepares a short AML/CFT policy, risk assessment and a buyer-and-seller CDD form your staff can actually use. We also handle the agency's income tax return, so the figures in both systems match. We reply on WhatsApp within office hours.</p>
""",
    faqs=[
        ("Do property dealers have to register with FBR as DNFBPs?",
         "Yes. FBR treats real estate agents, including property dealers, brokers, builders and developers, as DNFBPs when they execute or take part in the purchase or sale of real property. They must register with FBR and follow the AML/CFT Regulations."),
        ("Whose CNIC must an estate agent keep, the buyer's or the seller's?",
         "Both. FBR's short guidance for real estate agents lists the CNIC of the seller and purchaser, the sale deed, the bank draft and the CDD form as records to keep."),
        ("When must an estate agent file a CTR?",
         "When the agent engages in a cash transaction with a customer worth Rs 2 million or more. The CTR goes to the Financial Monitoring Unit on goAML."),
        ("Must I report a deal that did not go through?",
         "If it raised suspicion, yes. FBR's FAQs say an STR can be filed for an attempted transaction, and the agent should decline the business."),
        ("Is a builder selling its own flats a DNFBP?",
         "Yes. FBR's short guidance for real estate agents says the category includes builders and real estate developers when they execute property sales."),
        ("How long should property deal records be kept?",
         "CDD and transaction records for at least five years after the relationship ends, and STR and CTR records for at least ten years from filing."),
        ("Can I tell my client that I reported the deal?",
         "No. Telling a client, directly or indirectly, that an STR or CTR has been filed is tipping off, which is an offence under the AML law."),
        ("Is a buyer purchasing in a relative's name a red flag?",
         "It can be. FMU lists purchases in the name of an associate or relative other than a spouse or child, or for a minor or someone without the means, as a red flag. Ask questions and record the answers; file an STR if suspicion remains."),
        ("Which FBR office supervises a property dealer in Lahore?",
         "Under S.R.O. 1497(I)/2026, the Director (DNFBPs) Lahore covers businesses within RTO-I and RTO-II Lahore, CTO and LTO Lahore, and several other Punjab regions, with Additional Directors handling specific areas."),
    ],
    sources=[S_REA_SG, S_REA_GL, S_REA_RF, S_FAQ23, S_950, S_1497, S_GOAML, S_REGS],
    related=[(L['pillar'], "DNFBP Registration Guide"), (L['jew'], "DNFBP Rules for Jewellers"), (L['rea_tax'], "Tax for Real Estate Agents")],
    cta_h="Property Business? Get DNFBP-Compliant",
    cta_p="IRIS registration, goAML setup, a buyer-and-seller CDD form and an AML policy fitted to your agency or project.",
    wa_text="Assalam o Alaikum, main property dealer / builder hoon. DNFBP registration aur AML compliance mein madad chahiye.",
)


# ─────────────────────────────── JEWELLERS ───────────────────────────────
JEW = dict(
    slug=J_SLUG,
    title="Jeweller DNFBP Registration & AML Compliance Pakistan",
    h1="Jewellers and Gold Dealers: DNFBP Registration and AML Compliance in Pakistan",
    crumb="DNFBP for Jewellers",
    description="When a jeweller, bullion or gemstone dealer becomes a DNFBP: the Rs 2 million cash rule, CDD at the counter, FMU red flags, goAML reports and records.",
    keywords="jeweller DNFBP registration, gold dealer AML Pakistan, DNFBP Rs 2 million cash jeweller, sarafa DNFBP FBR, precious metals dealer goAML CTR",
    category="AML/CFT — Jewellers",
    icon="💍",
    read="11 min read",
    banner="A jeweller or bullion dealer becomes a DNFBP under FBR's AML regime on any cash transaction with a customer of Rs 2 million or more.",
    tldr=("Dealers in precious metals and stones, including jewellers, sarafa and bullion dealers and gemstone traders, are DNFBPs when they engage in a cash transaction "
          "with a customer of Rs 2 million or more. Once in scope they must register with FBR, appoint a compliance officer, identify and screen customers, report "
          "every cash transaction of Rs 2 million or more to FMU as a CTR, report suspicious or attempted transactions as STRs on goAML, and keep records for 5 to 10 years. "
          "Splitting a sale into smaller cash payments is a red flag, not a way out."),
    lead=("Gold holds value, is easy to carry and is often bought in cash, which is why FATF and Pakistan's AML law treat jewellers and bullion dealers as a high-attention "
          "sector. This guide is written for jewellers, sarafa and bullion traders and gemstone dealers. It explains, from FBR's DPMS guidance and FMU's red flags, when you "
          "come under the regime and what to do at the counter. For the rules that apply to every DNFBP, see our DNFBP registration guide."),
    body=f"""
<p class="tf-primary"><strong>Main guide:</strong> for the registration process, compliance officer rules and penalties for all DNFBPs, see our {a(L['pillar'], 'DNFBP registration guide for Pakistan')}.</p>

<h2 id="who-is-covered">When a Jeweller Becomes a DNFBP</h2>
<p>FBR's short guidance defines dealers in precious metals and stones (DPMS) as bullion dealers and anyone selling jewellery, precious stones and metals, including all articles made wholly or mainly of gold or platinum, diamonds, precious or semi-precious stones and pearls, whether set, mounted or strung. Such a dealer is a DNFBP <strong>when it engages in a cash transaction with a customer of Rs 2 million or more</strong>.</p>
{table(["Situation", "Within the regime?"], [
    ["A customer pays Rs 2.4 million in cash for a bridal set", "Yes. The business is a DNFBP and a CTR is due."],
    ["A customer pays Rs 3 million by bank transfer", "The cash test is not met for this sale, but CDD is still good practice and suspicion must still be reported once you are registered."],
    ["A customer buys Rs 1.8 million in cash, then returns the next day for Rs 900,000 more", "Treat with care. FMU lists many smaller transactions adding up to a large total as a red flag."],
    ["A bullion dealer buys gold from the public for cash above Rs 2 million", "Yes. The rule is about cash transactions with customers, not only sales."],
    ["A shop never takes Rs 2 million or more in cash from any customer", "Not a DNFBP on this test, but keep the rule and a written cash policy in place."],
])}
<p>In practice, most established jewellers and sarafa dealers in large markets do handle cash of this size at least occasionally, especially during the wedding season. Register before the first such sale, not after.</p>

<h2 id="counter">CDD at the Counter: A Practical Routine</h2>
<ol>
<li><strong>Before taking cash of Rs 2 million or more,</strong> take the customer's CNIC (NICOP, POC or passport for overseas customers) and record their name, date of birth, address and the purpose of the purchase.</li>
<li><strong>Ask whether they are buying for themselves.</strong> If someone else is paying or will receive the jewellery, identify that person too.</li>
<li><strong>Screen the names</strong> against the UN Security Council and domestic proscribed lists, which FBR makes available through its DNFBP mobile app and official links.</li>
<li><strong>Consider risk.</strong> A PEP, a customer from a high-risk country, or one with negative news needs enhanced due diligence: source of funds, more detail, and approval from senior management.</li>
<li><strong>Record the payment</strong> by method and amount, and issue a proper invoice.</li>
<li><strong>File the CTR</strong> on goAML for the cash transaction, and an STR if anything is suspicious. Do not tell the customer.</li>
<li><strong>File the paperwork:</strong> CNIC copy, CDD form and invoice. Keep them for at least five years, and keep STR and CTR records for ten years.</li>
</ol>

<h2 id="old-gold">Buying Old Gold and Exchanges</h2>
<p>Much of a jeweller's business is buying old gold or exchanging it for new pieces. When you pay a customer cash of Rs 2 million or more for gold, the cash test applies in the same way. Record where the seller says the gold came from, such as inheritance or an earlier purchase with a receipt, and be careful when someone sells large quantities often without a clear explanation. Where an exchange is settled partly in cash, record the cash portion.</p>

<h2 id="red-flags">Red Flags FMU Lists for Jewellers</h2>
<p>FMU's red flag indicators for jewellers and dealers in precious metals and stones include the following. One flag alone may not prove anything; several together, read with the customer's profile, may justify an STR.</p>
{table(["Area", "Red flag"], [
    ["Customer profile", "The customer's economic profile does not fit the value of the purchase, or the source of funds is unclear."],
    ["Indifference to the goods", "The customer shows no interest in the value, size or colour of the stone, metal or piece."],
    ["Secrecy", "The customer asks you not to keep normal records, refuses to give due diligence information, or uses false or forged identity documents."],
    ["Thresholds", "The customer is unusually concerned with the reporting limit or your AML policy."],
    ["Payments", "Large amounts of cash, traveller's cheques, cashier's cheques or prize bonds, or a cheque marked as payment for something else."],
    ["Splitting", "Many purchases over a short period, each small, adding up to a large total."],
    ["Third parties", "Payment from someone who does not own the funds, or delivery to someone who is neither the buyer nor the payer, without a legitimate reason."],
    ["Geography and news", "Links to FATF high-risk jurisdictions, negative news, a sanctions list match, or a PEP linked to crime."],
])}

<h2 id="examples">Worked Examples at the Counter</h2>
<p>The examples below are invented, but they reflect common situations in sarafa markets.</p>
{table(["Customer", "Transaction", "Action"], [
    ["A father buying a bridal set for his daughter", "Rs 26 lakh, paid in cash", "The business is in scope. Take both CNICs (payer and bride, if she is the buyer), complete the CDD form, screen names, file a CTR on goAML and keep the record for ten years."],
    ["A regular customer buying gold bars", "Rs 18 lakh in cash on Monday, Rs 15 lakh in cash on Thursday", "Two payments of the same kind, close together, totalling Rs 33 lakh. Consider whether they are one purchase split in two. Record CDD, and file an STR if the split looks deliberate."],
    ["A walk-in customer selling old jewellery", "Rs 22 lakh paid by the shop in cash", "A cash transaction above the threshold. Identify the seller, record where they say the gold came from, screen, file a CTR."],
    ["A business buyer paying by cheque", "Rs 40 lakh, cheque from a company account marked for \"office supplies\"", "Not a cash transaction, but a cheque marked as payment for something else is a red flag. Ask questions, record the answers and consider an STR."],
])}

<h2 id="wedding-season">Wedding Season and Family Purchases</h2>
<p>Bridal purchases are the most common reason a jeweller crosses the threshold. A family member paying for a set is normal; FBR's guidance only asks that you identify who is paying and who is buying when they are different people. Record both CNICs on the CDD form. What turns a family purchase into a red flag is a payer with no visible connection to the buyer, a payer whose means clearly do not match, or pressure to keep the sale off the books.</p>

<h2 id="records-system">A Simple Record System for a Jewellery Shop</h2>
<ul>
<li>One CDD form per qualifying customer, kept with a CNIC copy and the invoice.</li>
<li>A cash register or ledger that shows the customer and the cash amount for each large sale, so CTRs can be traced.</li>
<li>A file or folder for goAML submissions, kept for ten years.</li>
<li>A written note of staff training dates and the topics covered.</li>
<li>A yearly review of your risk assessment, done sooner if your business changes.</li>
</ul>

<h2 id="mistakes">Mistakes That Lead to Penalties</h2>
<ol>
<li><strong>Waiting for FBR to tell you to register.</strong> The duty comes from the law and the regulations, not from a letter.</li>
<li><strong>Breaking an invoice into smaller amounts.</strong> It does not avoid the regime, and it is exactly the pattern FMU looks for.</li>
<li><strong>Taking cash without a CNIC</strong> because the customer is a regular. Familiarity is not due diligence.</li>
<li><strong>Not registering on goAML</strong> until a report is due, then missing the filing.</li>
<li><strong>Telling a customer a report will be made.</strong> That is tipping off, which is an offence.</li>
</ol>
<p>Under the AML/CFT Sanctions Rules, 2020, penalties can reach Rs 100 million per violation, and significant sanctions are published with the business name.</p>

<h2 id="tax">Tax Is Separate</h2>
<p>AML rules do not change your income tax or sales tax position. For income tax, sales tax and the tax treatment of gold held by individuals, see our guide to {a(L['gold'], 'tax on gold and jewellery in Pakistan')}, and our {a(L['stx'], 'sales tax registration')} service if your buyers ask for an STRN.</p>

<h2 id="how-we-help">How We Help Jewellers</h2>
<p>Kamboh Associates registers jewellers, sarafa and bullion dealers on IRIS as DNFBPs, sets up goAML access, and prepares a counter-ready CDD form, a cash policy and an AML/CFT policy that fit a shop's real working day. We also file the business's income tax return so that both records agree. We reply on WhatsApp within office hours.</p>
""",
    faqs=[
        ("Is every jeweller a DNFBP?",
         "No. A dealer in precious metals and stones is a DNFBP when it engages in a cash transaction with a customer of Rs 2 million or more. Most established jewellers handle such cash at least occasionally, so most should register."),
        ("Does the Rs 2 million limit apply to card or bank payments?",
         "The DNFBP test for jewellers is about cash transactions. Payments by bank transfer or card do not trigger it, but once registered you must still report suspicion in any transaction."),
        ("What if a customer pays Rs 2 million in two cash instalments?",
         "Be careful. FMU lists several smaller transactions that add up to a substantial total as a red flag. Identify the customer, consider whether the payments are linked, and file an STR if you suspect they were split to avoid reporting."),
        ("Does buying old gold for cash count?",
         "Yes. The rule refers to cash transactions with customers, so paying Rs 2 million or more in cash for gold brings you into the regime in the same way as selling."),
        ("Where does a jeweller file a CTR?",
         "With the Financial Monitoring Unit on its goAML portal. The jeweller must register on goAML before filing."),
        ("Which records must a jeweller keep?",
         "The customer's CNIC and CDD form for every qualifying transaction, kept at least five years, and records of STRs and CTRs kept at least ten years from filing."),
        ("Is a sole-owner jewellery shop required to have a compliance officer?",
         "Yes. If there are no employees, FBR's Condition No. 3 (2022) treats the sole proprietor as the AML/CFT compliance officer."),
        ("Can a jeweller refuse a sale?",
         "Yes. FBR's guidance says that where there is suspicion, the business relationship or transaction should be turned down and an STR filed. If the customer matches a sanctions list, freeze the funds, refuse the transaction and inform FBR immediately."),
        ("Are gemstone and diamond traders covered too?",
         "Yes. FBR's definition covers diamonds, precious and semi-precious stones and pearls, and articles set with them, as well as gold and platinum."),
    ],
    sources=[S_DPMS_SG, S_DPMS_GL, S_DPMS_RF, S_FAQ23, S_950, S_GOAML, S_REGS],
    related=[(L['pillar'], "DNFBP Registration Guide"), (L['rea'], "DNFBP Rules for Real Estate Agents"), (L['gold'], "Tax on Gold and Jewellery")],
    cta_h="Jeweller or Bullion Dealer? Set Up AML Compliance",
    cta_p="IRIS DNFBP registration, goAML setup, a counter-ready CDD form and a cash policy for your shop.",
    wa_text="Assalam o Alaikum, main jeweller / sarafa dealer hoon. DNFBP registration aur AML compliance mein madad chahiye.",
)

POSTS = [PILLAR, REA, JEW]
