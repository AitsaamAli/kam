"""Extra depth for DNFBP topic guides (FBR guidance, FAQs Feb 2023, FMU goAML guideline, SRO 950; checked 10 November 2026)."""
from posts import a, table, L

EXTRA = {}

EXTRA["real-estate-agent-dnfbp-registration-aml-pakistan"] = (f"""
<h2 id="overseas">Overseas Pakistani Buyers and Sellers</h2>
<p>Overseas Pakistanis are an important part of the property market, and FBR's CDD form provides for them: a non-resident is identified with a NICOP or POC, an alien registration card or a passport, and NADRA's online verification services can be used. Points that keep these deals clean:</p>
<ul>
<li>Where the overseas client acts through a power of attorney, identify both the client and the attorney, keep the attorney document, and ask why it is being used; FMU lists unexplained delegation through powers of attorney as a red flag.</li>
<li>Record how funds arrive: a foreign remittance through a bank is a clear trail; cash handed over locally on the client's behalf is not.</li>
<li>Check whether the client's country of residence is one FATF has called out; if so, apply enhanced due diligence.</li>
<li>Note the significant geographic distance between agent and client; FMU flags it when there is no clear reason.</li>
</ul>

<h2 id="companies">When the Buyer Is a Company or Trust</h2>
<p>A company buyer must be traced to the natural persons who own or control it. FBR's guidelines point to two registers under the Companies Act, 2017: the register of members (Section 119) and the register of ultimate beneficial owners (Section 123A). Ask for the incorporation certificate, memorandum and articles, an extract of the beneficial ownership register, and the CNICs of the people who control the company. If the owners cannot be identified, the guidance says the senior managing official is treated as the beneficial owner, but refusal to disclose owners is itself a red flag. For trusts, obtain the trust deed and registration and identify the trustees and beneficiaries.</p>

<h2 id="deal-file">What a Complete Deal File Looks Like</h2>
<ul>
<li>CDD form for the buyer and for the seller, signed and dated.</li>
<li>CNIC, NICOP, POC or passport copies, with NADRA verification where used.</li>
<li>Sanctions screening record for each party, their beneficial owners and any attorney.</li>
<li>Risk rating and, for higher risk, source-of-funds evidence and the approval.</li>
<li>Sale deed, transfer letter or agreement to sell.</li>
<li>Payment record: bank drafts, transfers or the cash register entry and CTR reference.</li>
<li>Any internal note of concerns raised and the decision taken (kept confidential).</li>
</ul>
<p>An inspector will usually pick a sample of deals and ask for exactly this file. If it exists for every deal, inspections are short.</p>
""", [
    ("How do I verify an overseas Pakistani buyer?",
     "Use the NICOP or POC, or a passport, and NADRA's verification services where available, record how funds arrive, and apply enhanced due diligence if the client is linked to a FATF-listed jurisdiction."),
    ("What documents do I need when a company buys property?",
     "The incorporation certificate, memorandum and articles, the register of ultimate beneficial owners, and CNICs of the natural persons who own or control the company."),
    ("What will an inspector ask for?",
     "Usually a sample of deal files with CDD forms, IDs, screening records, risk ratings, sale documents, payment records and any CTRs."),
])

EXTRA["jeweller-dnfbp-registration-aml-pakistan"] = (f"""
<h2 id="cash-policy">Writing a Cash Policy for the Shop</h2>
<p>The law sets the Rs 2 million line; a good shop policy sets its own lower internal line so staff act before it is crossed. A practical policy covers:</p>
<ol>
<li><strong>An internal trigger,</strong> for example taking a CNIC and completing the CDD form for any cash sale above an amount you choose below Rs 2 million, so that linked purchases are caught.</li>
<li><strong>Who may accept large cash:</strong> the owner or a named senior person only.</li>
<li><strong>How cash is recorded:</strong> every large cash receipt in the register with the customer's name and invoice number.</li>
<li><strong>When the CTR is filed:</strong> who files it on goAML and how the filing is recorded.</li>
<li><strong>When to refuse:</strong> a customer who will not give identification, or asks for no record to be kept.</li>
</ol>

<h2 id="screening">Screening Walk-In Customers Quickly</h2>
<p>FBR expects screening against the UN Security Council consolidated list and Pakistan's proscribed persons and organisations lists, which it makes available through its DNFBP mobile app and official links. At a busy counter, screening takes under a minute if it is a habit: type the name and CNIC, note the result on the CDD form, and move on. On a true match, freeze the funds without delay, refuse the transaction, file an STR and inform FBR immediately; on a possible match that you cannot resolve, do not complete the sale until it is resolved.</p>

<h2 id="inspection">What an Inspector Asks a Jeweller For</h2>
{table(["Request", "What to have ready"], [
    ["Registration", "FBR DNFBP registration details and goAML access"],
    ["Compliance officer", "Written appointment (or note that the sole owner is deemed officer)"],
    ["Policy and risk assessment", "Dated documents signed by the owner"],
    ["Large cash sales", "Cash register entries matched to CTRs and CDD forms"],
    ["Customer files", "CNIC copies, CDD forms, screening notes"],
    ["Training", "Dates, attendees and topics"],
])}

<h2 id="bullion">Bullion Dealers and Trade Purchases</h2>
<p>Bullion dealers often deal with other traders as well as the public. FBR's definition looks at cash transactions with a customer of Rs 2 million or more, so large cash trades with other dealers need the same identification, screening and CTR discipline as retail sales. Keep the counterparty's business details and NTN on file, and be alert to FMU's red flags around third-party payments and deliveries to people who are neither the buyer nor the payer.</p>
""", [
    ("Should my shop set a lower internal cash limit?",
     "It is good practice. An internal trigger below Rs 2 million for taking a CNIC and completing CDD helps staff catch linked purchases before the legal threshold is crossed."),
    ("What do I do on a possible sanctions match I cannot resolve?",
     "Do not complete the sale until it is resolved. On a confirmed match, freeze the funds, refuse the transaction, file an STR and inform FBR immediately."),
    ("Do trades with other dealers count?",
     "The test is a cash transaction with a customer of Rs 2 million or more, so large cash trades with other dealers need the same identification, screening and CTR discipline."),
])

EXTRA["goaml-registration-dnfbp-pakistan"] = (f"""
<h2 id="internal-workflow">From Concern to Report: An Internal Workflow</h2>
<ol>
<li><strong>Staff notice a red flag</strong> and record it on an internal concern form: who, what, when, and why it looked wrong.</li>
<li><strong>The compliance officer reviews</strong> the customer file, asks for any missing information, and decides whether there are grounds for suspicion.</li>
<li><strong>The decision is recorded,</strong> whether or not an STR is filed, with the reasons.</li>
<li><strong>If suspicion remains,</strong> the transaction is declined and the STR is filed promptly on goAML.</li>
<li><strong>Nothing is said to the customer</strong> about the concern or the report.</li>
</ol>
<p>This workflow is short enough for a two-person business and shows an inspector that suspicion is handled consistently.</p>

<h2 id="ctr-practice">CTRs in Practice</h2>
<p>A CTR is a threshold report: no suspicion is needed. To file one accurately you need, at the time of the transaction, the customer's identity details, the date, the amount of cash, and what it paid for. Capture these on the CDD form and in the cash register, then file the CTR on goAML and note the reference against the register entry. Keep the CTR record for at least ten years from filing.</p>

<h2 id="access">Keeping goAML Access Working</h2>
<ul>
<li><strong>When the admin leaves,</strong> arrange a new admin with FMU before the old login is lost; a business without a working login cannot report.</li>
<li><strong>Use an email the business controls,</strong> so password resets do not depend on a former employee.</li>
<li><strong>Limit who can see reports;</strong> confidentiality protects both the business and the customer process.</li>
<li><strong>Test the login</strong> every few months, not only when a report is due.</li>
</ul>

<h2 id="sector-notes">Notes by Sector</h2>
{table(["Sector", "Most common report", "Practical tip"], [
    ["Real estate agents", "CTRs for cash token and instalment payments; STRs for nominee and third-party purchases", "File the CTR reference in the deal file"],
    ["Jewellers and bullion dealers", "CTRs for cash sales and purchases of Rs 2 million or more", "Link each large cash register entry to its CTR"],
    ["Accountants and TCSPs", "STRs on formation or client-money services", "Record the concern before onboarding is completed"],
])}
""", [
    ("What details do I need to file a CTR?",
     "The customer's identity details, the date, the cash amount and what it paid for, captured on the CDD form and in the cash register at the time of the transaction."),
    ("What if our goAML admin leaves the business?",
     "Arrange a new admin with FMU before the old login is lost, and use an email address the business controls."),
    ("Should we record decisions not to file an STR?",
     "Yes. Recording the reasons for each decision shows an inspector that concerns are handled consistently."),
])

EXTRA["accountant-dnfbp-registration-aml-pakistan"] = (f"""
<h2 id="onboarding">Onboarding a Client for a Specified Service</h2>
<ol>
<li><strong>Identify the service:</strong> confirm which of the 14 activities you are being engaged for.</li>
<li><strong>Identify the client:</strong> CNIC for individuals; for companies, incorporation documents and the register of ultimate beneficial owners.</li>
<li><strong>Identify the beneficial owners</strong> and anyone acting on the client's behalf.</li>
<li><strong>Screen</strong> the client, beneficial owners and agents against the sanctions lists.</li>
<li><strong>Understand the purpose:</strong> why the company is being formed, why client money is being managed, what the address service is for.</li>
<li><strong>Rate the risk</strong> and, for higher risk or high-value engagements above your policy threshold, obtain source of funds or wealth and senior approval.</li>
<li><strong>Engage in writing,</strong> with terms that require CDD documents and allow you to withdraw if information is refused.</li>
</ol>

<h2 id="tcsp-risks">Where TCSP Services Are Most Exposed</h2>
<p>FMU's red flags for accountants highlight the situations most open to misuse:</p>
<ul>
<li><strong>Nominee arrangements:</strong> forming a company through a nominee director, or acting as or arranging a nominee shareholder, is a specified service, and nominee structures can hide the real owner.</li>
<li><strong>Registered address services:</strong> an address shared by many companies suggests a mailbox service, which FMU flags.</li>
<li><strong>Dormant then active companies:</strong> a company inactive after incorporation that suddenly shows large financial activity.</li>
<li><strong>Trusts and waqf:</strong> arrangements that obscure ownership or hold shares of a company.</li>
</ul>
<p>None of these services is prohibited; they require closer due diligence and a clear record of why the client needs them.</p>

<h2 id="assessment-note">Sample Note: Practice Not in Scope</h2>
<p>If your assessment shows you provide no specified services, keep a short dated note on file. For example:</p>
<blockquote style="border-left:3px solid #14B8A6;padding:8px 14px;margin:12px 0;background:#F8FAFC">Assessment of AML/CFT applicability, [date]. Services provided: tax returns, tax advisory, bookkeeping and statutory filings after incorporation. None of these is a specified service under FBR's AML/CFT Regulations (FBR FAQs, February 2023, questions 6, 11 and 24). The practice does not form companies, manage client funds, provide registered addresses or act as nominee or trustee. To be reviewed if services change. Signed: [partner].</blockquote>
<p>Review the note whenever you add a service. Company formation is the addition that most often changes the answer.</p>

<h2 id="mixed">Practices With Mixed Services</h2>
<p>Many practices do both: mostly tax and bookkeeping, plus a few company formations a year. FBR's FAQs say CDD is mandatory for clients receiving Accountant or TCSP services and encouraged for others. In practice, apply full CDD to every formation or client-money client, keep a lighter identification file for the rest, and register as a DNFBP because the specified services are part of your ordinary business.</p>
""", [
    ("Is acting as a nominee shareholder allowed?",
     "It is not prohibited, but acting as or arranging a nominee shareholder is a specified service under FBR's list, and nominee structures require close due diligence."),
    ("Should I keep a record if my practice is not in scope?",
     "Yes. A short, dated assessment note explaining why your services are outside the 14 activities is good practice and should be reviewed when services change."),
    ("Do I need full CDD for every client if I do a few company formations?",
     "CDD is mandatory for clients receiving specified services; for other clients FBR encourages it. Applying full CDD to formation clients and lighter identification to others is a practical approach."),
])

EXTRA["aml-cft-compliance-programme-dnfbp-pakistan"] = (f"""
<h2 id="matrix">A Simple Customer Risk-Rating Matrix</h2>
<p>Score each factor 1 (low), 2 (medium) or 3 (high) and add them up. Your policy decides the cut-offs; an example:</p>
{table(["Factor", "1 (low)", "2 (medium)", "3 (high)"], [
    ["Customer type", "Known local individual", "New customer, company with clear owners", "PEP, complex ownership, adverse news"],
    ["Geography", "Local", "Elsewhere in Pakistan or a low-risk country", "Linked to a FATF-listed jurisdiction"],
    ["Payment", "Bank transfer from own account", "Partly cash below threshold", "Large cash, third-party payer"],
    ["Service or product", "Low value, routine", "Higher value", "Plot files, bullion, formation with nominees"],
])}
<p>For example: a total of 4 to 6 could mean standard CDD, 7 to 9 additional checks, and 10 to 12 enhanced due diligence with senior approval. Record the score on the CDD form so the reason for each level of checks is visible.</p>

<h2 id="training-plan">A Training Plan for a Small Business</h2>
{table(["When", "Who", "Topics"], [
    ["On joining", "Every customer-facing employee", "What the business must do, CDD form, red flags, tipping off"],
    ["Every six months", "All staff dealing with customers or money", "Sector red flags, recent cases, any policy changes"],
    ["Yearly", "Compliance officer", "FBR and FMU updates, sanctions list changes, inspection findings"],
    ["After any incident", "Staff involved", "What happened and what changes"],
])}
<p>Record the date, attendees and topics each time. Training that is not recorded is hard to prove.</p>

<h2 id="calendar">An Annual Compliance Calendar</h2>
<ul>
<li><strong>Monthly:</strong> check CDD forms are complete for every customer in scope; match large cash entries to CTRs.</li>
<li><strong>Quarterly:</strong> re-screen existing customers against updated lists; review the internal concern log.</li>
<li><strong>Every six months:</strong> staff refresher training.</li>
<li><strong>Yearly:</strong> review and re-date the risk assessment and policy; carry out the independent review; confirm FBR registration and goAML access are current.</li>
</ul>

<h2 id="reasonable-steps">Showing "Reasonable Steps"</h2>
<p>Rule 4(2) of the Sanctions Rules is the reason documentation matters: a regulator that is satisfied you took all reasonable steps and exercised due diligence may not impose a sanction. What counts as reasonable is judged from evidence, so keep the dated risk assessment, signed policy, completed CDD forms, screening records, training records and independent review findings together, where they can be produced on request.</p>
""", [
    ("How do I decide which customers need enhanced due diligence?",
     "Use a simple scoring matrix across customer type, geography, payment method and service, with cut-offs set in your policy, and apply enhanced due diligence with senior approval to the highest scores."),
    ("How often should staff be trained?",
     "On joining and then at regular intervals, for example every six months, with records of dates, attendees and topics."),
])
