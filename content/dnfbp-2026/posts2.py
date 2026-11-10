"""DNFBP batch 2: goAML registration, accountants/TCSPs, AML compliance programme (facts checked 10 November 2026)."""
from posts import WA, L, a, table, S_FAQ23, S_950, S_REGS, S_GOAML, S_REDF, S_INTRO, S_IRIS

DATE = "2026-11-10"
DLONG = "10 November 2026"

S_GOAML_REG = ("FMU: Guidelines for Registration on goAML (DNFBPs)", "https://www.fmu.gov.pk/docs/2022/goAML-Registration-Guideline-DNFBPs.pdf")
S_FMU_FAC = ("FMU: goAML DNFBPs facilitation page", "https://www.fmu.gov.pk/dnfbps-facilitation/")
S_FMU_UG = ("FMU: goAML Web Users Guide (updated 2020)", "http://www.fmu.gov.pk/docs/Financial-Monitoring-Unit-FMU-goAML-Web-Users-Guide-Updated-2020.pdf")
S_ACC_GL = ("FBR: AML/CFT Guidelines for Accountants", "https://download1.fbr.gov.pk/Docs/202182168263117AMLCFTGuidelines_AccountantsupdatedJuly,2020.pdf")
S_ACC_RF = ("FMU: Red Flag Indicators for Accountants", "https://download1.fbr.gov.pk/Docs/202117141954216Red-Flag-Indicators-for-Accountants-final.pdf")
S_REA_SG = ("FBR: Short Guidance on AML/CFT Obligations for Real Estate Agents", "https://download1.fbr.gov.pk/Docs/2021915091332570ShortGuidanceForREAs.pdf")

G_SLUG = "goaml-registration-dnfbp-pakistan"
A_SLUG = "accountant-dnfbp-registration-aml-pakistan"
C_SLUG = "aml-cft-compliance-programme-dnfbp-pakistan"
L2 = {"goaml": "/blogs/" + G_SLUG, "acc": "/blogs/" + A_SLUG, "prog": "/blogs/" + C_SLUG,
      "company": "/secp-company-registration-guide-2026", "secp": "/blogs/company-registration-cost-pakistan-secp"}


# ─────────────────────────────── goAML ───────────────────────────────
GOAML = dict(
    slug=G_SLUG,
    svc={'h2': 'Let Us Register You on goAML', 'intro': 'goAML registration fails on small details: letterhead, phone formats, mismatched names. We prepare it so it goes through first time.', 'hook': 'Want goAML registration handled?', 'fee': 'Fixed fee, confirmed on WhatsApp before any work starts.', 'btn': 'Register me on goAML', 'items': ['Authority letter drafted on your letterhead', 'goAML form completed to match your FBR and NADRA records', 'Hard copy dispatch guidance and follow-up with FMU', 'Admin account set up with the right person', 'A one-page STR/CTR procedure for your staff'], 'risks': ['Without goAML access, a required STR or CTR cannot be filed on time', 'Shared or junior admin logins increase tipping-off risk']},
    title="goAML Registration for DNFBPs in Pakistan: Step-by-Step Guide",
    h1="goAML Registration for DNFBPs in Pakistan: Step-by-Step Guide to FMU's Reporting Portal",
    crumb="goAML Registration Guide",
    description="Register your property, jewellery or accounting business on FMU's goAML portal: every form field, the authority letter, admin rules and STR/CTR basics.",
    keywords="goAML registration Pakistan, goAML registration DNFBP, FMU goAML portal, goAML authority letter, how to file STR CTR goAML, goAML real estate jeweller",
    category="AML/CFT — goAML",
    icon="🧾",
    read="12 min read",
    banner="FBR registration does not register you on goAML. Every DNFBP needs a separate goAML account with the Financial Monitoring Unit before it can file an STR or CTR.",
    tldr=("goAML is the Financial Monitoring Unit's online portal for suspicious transaction reports (STRs) and currency transaction reports (CTRs). "
          "FBR's FAQs say every DNFBP must register on it, and that STRs go only to FMU, not to FBR. Registration is done at goamlweb.fmu.gov.pk using "
          "'Register New Organization': you enter the business details, then the details of a senior person who will be the goAML admin, attach a signed "
          "authority letter on your letterhead as a PDF, and send the hard copy of that letter to the Additional Director, FMU. FMU approves the request, "
          "after which the admin logs in with the email and password chosen at registration."),
    lead=("Many property dealers and jewellers register with FBR as a DNFBP and assume the job is done. It is not. Reports go to a different body, the "
          "Financial Monitoring Unit (FMU), through its own portal, goAML, and a business that has not registered there cannot report when it needs to. "
          "This guide follows FMU's own goAML registration guideline for DNFBPs field by field, then explains what happens after approval."),
    body=f"""
<p class="tf-primary"><strong>Main guide:</strong> who must register as a DNFBP and the duties that follow are in our {a(L['pillar'], 'DNFBP registration guide for Pakistan')}.</p>

<h2 id="what-is-goaml">What goAML Is and Why DNFBPs Need It</h2>
<p>goAML is the reporting system FMU uses to receive reports from banks and other reporting entities. For DNFBPs it has two uses: filing a <strong>Suspicious Transaction Report (STR)</strong> when you know or suspect that a transaction involves the proceeds of crime or terrorist financing, and filing a <strong>Currency Transaction Report (CTR)</strong> when a cash transaction with a customer is Rs 2 million or more.</p>
<p>FBR's February 2023 FAQs make three points clear. Each reporting entity must register on goAML to file STRs and CTRs. STRs are filed with FMU only, not with FBR. And an STR is filed promptly, as soon as the suspicion arises, not at the end of the year.</p>
{table(["", "FBR (DNFBP registration)", "FMU (goAML registration)"], [
    ["Purpose", "Supervision: registration, inspections, sanctions", "Receiving STRs and CTRs and analysing them"],
    ["Where", "FBR's IRIS portal", "goamlweb.fmu.gov.pk"],
    ["Login", "Your IRIS taxpayer login", "A separate goAML admin username (an email) and password"],
    ["Do you need both?", "Yes", "Yes"],
])}

<h2 id="before-you-start">Before You Start: What to Prepare</h2>
<ul>
<li><strong>Business NTN</strong>, or the owner's CNIC for a sole proprietorship.</li>
<li><strong>Business details:</strong> registered name, type of entity (sole proprietorship, partnership or AOP, company), full address and phone number.</li>
<li><strong>A contact person</strong> for the business, normally the owner, director or chief executive, with an email address.</li>
<li><strong>An admin user:</strong> FMU's guideline says the business administrator should be a senior official, preferably the head of compliance. For a small business this is usually the owner, who is also the AML/CFT compliance officer.</li>
<li><strong>The admin's details:</strong> name, date of birth, 13-digit CNIC, phone and address.</li>
<li><strong>An authority letter</strong> on your letterhead, signed by the head of compliance, scanned as a PDF. FMU publishes a specimen on its DNFBP facilitation page.</li>
</ul>

<h2 id="steps">Step-by-Step: Registering Your Business on goAML</h2>
<p>The steps below follow FMU's <em>Guidelines for Registration on goAML</em> for DNFBPs. Screen labels can change, so compare with FMU's own help page if something looks different.</p>
<ol>
<li><strong>Open the registration page.</strong> Go to goAML through FMU's website (fmu.gov.pk/goaml) and choose <strong>Register New Organization</strong>.</li>
<li><strong>Register as a reporting entity.</strong> Choose to register as a reporting entity.</li>
<li><strong>Choose your business type.</strong> For example, "Dealer of Precious Metals &amp; Stones (Jeweler)" or "Real Estate".</li>
<li><strong>Answer "Is financial?" with No.</strong> DNFBPs are not financial institutions.</li>
<li><strong>Enter the business name</strong>, for example "ABC Real Estate &amp; Builders".</li>
<li><strong>Enter the NTN</strong> of the business, or the owner's CNIC.</li>
<li><strong>Choose the entity type:</strong> partnership, proprietorship, association of persons or company.</li>
<li><strong>Add the contact person and their email.</strong></li>
<li><strong>Add the business phone number</strong> with country code 92 and without the leading zero, for example 321xxxxxxx for a mobile.</li>
<li><strong>Add the business address.</strong></li>
<li><strong>Fill in the admin user section</strong> (the "registering person"): username, which must be an email address, entered twice; password; title; first and last name; date of birth (DD/MM/YYYY); CNIC (13 digits, no dashes); phone number (92 code, no leading zero); and address, which may be the same as the business address.</li>
<li><strong>Attach the authority letter</strong> as a PDF and submit the form.</li>
<li><strong>Post the hard copy</strong> of the signed authority letter to the Additional Director, FMU.</li>
<li><strong>Wait for approval.</strong> FMU processes the request and notifies you. Once approved, the admin logs into the goAML production site with the username and password set at registration.</li>
</ol>

<h2 id="by-entity">What to Enter for Each Type of Business</h2>
{table(["Business type", "NTN field", "Letterhead and signatory", "Admin user"], [
    ["Sole proprietorship (e.g. a jewellery shop)", "Business NTN, or the owner's CNIC", "Shop letterhead, signed by the owner as head of compliance", "Usually the owner"],
    ["Partnership or AOP (e.g. a property agency run by partners)", "The AOP's NTN", "Firm letterhead, signed by the partner appointed as compliance officer", "The compliance partner"],
    ["Company (e.g. a builder or developer)", "The company's NTN", "Company letterhead, signed by the head of compliance", "A senior officer, preferably the head of compliance"],
])}
<p>Use the same business name and NTN that appear on your FBR record and DNFBP registration. Differences between the two are a common cause of questions from FMU or FBR later.</p>

<h2 id="admin-password">Admin Account and Password Rules</h2>
{table(["Item", "FMU's requirement or advice"], [
    ["Username", "Must be an email address. FMU recommends an official business email; a personal email such as Gmail is also accepted."],
    ["Password", "At least 8 characters, with at least one small letter, one capital letter, one number and one special character."],
    ["Who should be admin", "A senior person, preferably the head of compliance."],
    ["Phone numbers", "Country code 92 without 00 or +, and no leading 0."],
    ["CNIC", "13 digits without dashes."],
])}
<p>Treat the admin login like a bank login. Do not share it with staff who should not see reports. Tipping off a customer that a report has been made is an offence, and a shared password makes leaks more likely.</p>

<h2 id="mistakes">Common Reasons a goAML Request Is Delayed</h2>
<ul>
<li><strong>No hard copy sent.</strong> The guideline requires both the PDF upload and a posted original of the authority letter.</li>
<li><strong>Letter not on letterhead, or unsigned.</strong> The letter must be on the business's letterhead and signed by the head of compliance.</li>
<li><strong>Mismatched details.</strong> The NTN, business name and admin CNIC should match your FBR and NADRA records exactly.</li>
<li><strong>Phone numbers in the wrong format,</strong> with a leading zero or a + sign.</li>
<li><strong>A junior employee named as admin.</strong> FMU expects a senior official.</li>
</ul>

<h2 id="after-approval">After Approval: Filing STRs and CTRs</h2>
<p>Once logged in, reports are submitted through goAML's web forms. FMU's goAML Web Users Guide explains the screens. Some practical rules apply to every report:</p>
<ul>
<li><strong>STR:</strong> file promptly once you know, suspect or have reason to suspect that funds come from crime, are linked to terrorism, are meant to dodge reporting, or have no apparent lawful purpose. This includes attempted transactions that did not go ahead.</li>
<li><strong>CTR:</strong> file for any cash transaction with a customer of Rs 2 million or more. No suspicion is needed; it is a threshold report.</li>
<li><strong>Write a clear narrative</strong> in an STR: who, what, when, how much, and why it looked suspicious, with the red flags you saw. FMU's sector red flag lists help you describe the concern.</li>
<li><strong>Keep copies.</strong> FBR's FAQs require records of STRs and CTRs to be kept for at least ten years from filing.</li>
<li><strong>Do not tell the customer.</strong> Once the report is filed, your duty is done; any follow-up is for FMU or an investigating agency. FMU must keep the reporter's identity confidential under the AML Act.</li>
</ul>

<h2 id="str-narrative">What a Good STR Narrative Contains</h2>
<p>An STR is only as useful as its description. FMU does not ask for proof of a crime, only for the facts and the reasons for your suspicion. A practical checklist for the narrative:</p>
<ol>
<li><strong>Who:</strong> the customer, any person acting for them, and any third party who paid or received value, with identity details from your CDD file.</li>
<li><strong>What and when:</strong> the property, jewellery or service involved, dates, amounts and how each payment was made.</li>
<li><strong>Why it is suspicious:</strong> the specific red flags, in plain words, for example "buyer's stated salary does not support a Rs 4 crore cash purchase" or "payments split into several cash amounts below Rs 2 million over three days".</li>
<li><strong>What you did:</strong> questions you asked, documents requested or refused, and whether you declined the transaction.</li>
<li><strong>Supporting documents:</strong> attach copies from your CDD file where goAML allows.</li>
</ol>
<p>Avoid accusations and opinions about guilt. Describe what you saw and why it did not fit the customer's profile.</p>

<h2 id="help">Where to Get Help From FMU and FBR</h2>
{table(["Question about", "Contact"], [
    ["goAML registration or login", "goamlhelpdesk@fmu.gov.pk (as listed in FMU's DNFBP registration guideline)"],
    ["DNFBP registration with FBR, or AML/CFT duties", "help.dnfbp.fbr@gmail.com, helpline +92 51 9106606 (FBR FAQs, February 2023)"],
])}

<h2 id="how-we-help">How Kamboh Associates Helps</h2>
<p>We register businesses on goAML from start to finish: we prepare the authority letter on your letterhead, fill in the form with details matched to your FBR and NADRA records, and follow up until FMU approves. We also set up your FBR DNFBP registration and a short AML/CFT policy, so all three are consistent. See our guides for {a(L['rea'], 'real estate agents')}, {a(L['jew'], 'jewellers')} and {a(L2['acc'], 'accountants and company service providers')}. We reply on WhatsApp within office hours.</p>
""",
    faqs=[
        ("Is goAML registration the same as DNFBP registration with FBR?",
         "No. DNFBP registration is with FBR on IRIS. goAML registration is with the Financial Monitoring Unit and is needed to file STRs and CTRs. A DNFBP needs both."),
        ("Who should be the goAML admin for a small business?",
         "FMU's guideline says the admin should be a senior official, preferably the head of compliance. In a sole proprietorship that is usually the owner, who is also the AML/CFT compliance officer."),
        ("Can I use a Gmail address as the goAML username?",
         "Yes. FMU recommends an official business email, but its DNFBP registration guideline shows a Gmail address as an accepted example."),
        ("What is the goAML authority letter?",
         "A letter on the business's letterhead, signed by the head of compliance, authorising the admin user. It is uploaded as a PDF with the form, and the hard copy is posted to the Additional Director, FMU. FMU publishes a specimen."),
        ("What are the password rules for goAML?",
         "At least eight characters, including at least one small letter, one capital letter, one number and one special character."),
        ("Do I file STRs with FBR or FMU?",
         "With FMU through goAML only. FBR's FAQs say reporting entities are only required to file STRs with FMU."),
        ("When must a CTR be filed?",
         "When the business engages in a cash transaction with a customer worth Rs 2 million or more. It is a threshold report and no suspicion is needed."),
        ("Can I file an STR for a deal that did not happen?",
         "Yes. FBR's FAQs say an STR can be filed for an attempted transaction that raises suspicion."),
        ("How long should goAML reports be kept?",
         "Records of STRs and CTRs should be kept for at least ten years from the date of filing, according to FBR's 2023 FAQs."),
    ],
    sources=[S_GOAML_REG, S_FMU_FAC, S_FMU_UG, S_GOAML, S_FAQ23, S_REDF],
    related=[(L['pillar'], "DNFBP Registration Guide"), (L2['prog'], "AML/CFT Compliance Programme"), (L['rea'], "DNFBP Rules for Real Estate Agents")],
    cta_h="Need goAML Registration Done Right?",
    cta_p="Authority letter, form filling matched to your FBR records, and follow-up with FMU until approval.",
    wa_text="Assalam o Alaikum, mujhe goAML registration (FMU) mein madad chahiye.",
)


# ─────────────────────────────── ACCOUNTANTS / TCSP ───────────────────────────────
ACC = dict(
    slug=A_SLUG,
    svc={'h2': 'Let Us Check Your Practice', 'intro': 'Most practices only need an hour to know whether they are in scope. If you are, we set up the registration and procedures without disrupting client work.', 'hook': 'Not sure if your practice is covered?', 'fee': 'Fixed fee, confirmed on WhatsApp before any work starts.', 'btn': 'Check my practice', 'items': ["A service-by-service check against FBR's 14 activities", 'A written note of the assessment for your file', 'DNFBP registration on IRIS and goAML, if in scope', 'A client CDD procedure for specified services', 'Engagement terms that require CDD documents at onboarding'], 'risks': ['There is no turnover threshold, and free services count', 'Company formation for clients is a specified service']},
    title="Accountants & Company Service Providers: DNFBP Rules Pakistan",
    h1="Accountants and Company Service Providers (Non-ICAP/ICMAP): DNFBP Registration and AML Rules in Pakistan",
    crumb="DNFBP for Accountants",
    description="Which accountant and company-formation services make you a DNFBP: FBR's 14 activities, what is not covered (tax, audit, bookkeeping) and the duties.",
    keywords="accountant DNFBP registration Pakistan, trust and company service provider DNFBP, non ICAP accountant AML FBR, company formation agent DNFBP, APDS survey accountants",
    category="AML/CFT — Accountants",
    icon="📒",
    read="12 min read",
    banner="Accountants who are not ICAP or ICMAP members become DNFBPs through the services they provide, not through their title or turnover. There is no minimum threshold.",
    tldr=("Under FBR's AML/CFT regime, sole practitioners, partners and employees of firms not regulated by ICAP or ICMAP are DNFBPs when they carry out "
          "any of 14 listed services: for example managing client money or accounts, forming companies or firms on a client's behalf, acting as or arranging "
          "a director, partner, trustee or nominee shareholder, or providing a registered or correspondence address. Tax advisory, statutory audit, internal audit "
          "and pure bookkeeping are not covered. There is no financial threshold, and free services count too. Covered firms must register with FBR, carry out "
          "CDD on the clients who receive those services, report STRs to FMU on goAML and keep records."),
    lead=("For accountants and company service providers, the hard question is not how to comply but whether the rules apply to them at all. FBR's "
          "February 2023 FAQs answer that in unusual detail, with service-by-service examples. This guide brings those answers together for practitioners, "
          "consultancy firms and corporate service providers who are not regulated by ICAP or ICMAP."),
    body=f"""
<p class="tf-primary"><strong>Main guide:</strong> for registration steps, penalties and the duties common to all DNFBPs, see our {a(L['pillar'], 'DNFBP registration guide for Pakistan')}.</p>

<h2 id="who">Who Counts as an "Accountant" for AML Purposes</h2>
<p>The AML Act, 2010 lists accountants as DNFBPs in Section 2(xii). FBR supervises those <strong>other than members regulated by the Institute of Chartered Accountants of Pakistan (ICAP) and the Institute of Cost and Management Accountants of Pakistan (ICMAP)</strong>; those institutes supervise their own members. FBR's definition covers sole practitioners, partners and professionals employed in firms when they carry out the listed activities. FBR's FAQs group these activities as "Accountant" or "Trust and Company Service Provider" (TCSP) services, together called specified services.</p>
<p>Two rules from the FAQs surprise many firms:</p>
<ul>
<li><strong>No threshold.</strong> Coverage depends only on the services provided. There is no turnover, fee or transaction limit (FAQ 19).</li>
<li><strong>Free work counts.</strong> A specified service provided without a fee still makes the firm a DNFBP (FAQ 20).</li>
</ul>

<h2 id="fourteen-activities">The 14 Activities That Bring You Into Scope</h2>
{table(["#", "Activity (FBR FAQs, question 2)"], [
    ["1", "Buying and selling real estate"],
    ["2", "Managing client money, securities or other assets"],
    ["3", "Managing bank, savings or securities accounts"],
    ["4", "Organising contributions for the creation, operation or management of companies"],
    ["5", "Creating, operating or managing companies, trusts or waqf"],
    ["6", "Acting as a formation agent of legal persons"],
    ["7", "Buying and selling business entities"],
    ["8", "Acting as a director or secretary of a company, or a partner of a partnership"],
    ["9", "Arranging for another person to act as a director, secretary or partner"],
    ["10", "Acting as a trustee of an express trust, or the equivalent for a waqf"],
    ["11", "Arranging for another person to act as such a trustee"],
    ["12", "Acting as a nominee shareholder for another person"],
    ["13", "Arranging for another person to act as a nominee shareholder"],
    ["14", "Providing a registered office, business address, or correspondence or administrative address for a company, partnership, trust or waqf"],
])}

<h2 id="covered-or-not">Covered or Not? FBR's Own Answers</h2>
<p>FBR's FAQs answer many borderline questions directly. The most useful, in one place:</p>
{table(["Service", "Specified service?", "FBR's reasoning"], [
    ["Registering a company with SECP for a client, or forming a partnership, firm or society", "<strong>Yes</strong>", "Acting as a formation agent; filing incorporation forms is a TCSP activity (FAQs 3 and 10)."],
    ["Filing annual returns and statutory forms (Form A, B, 29, 45) after incorporation", "No", "A routine regulatory requirement under the Companies Act, 2017 (FAQ 11)."],
    ["Authorising salary payments from the client's account to staff accounts", "<strong>Yes</strong>", "The accountant controls the flow of funds (FAQ 3)."],
    ["Preparing payroll vouchers that the client then pays", "No", "The client, not the accountant, controls the funds (FAQ 3)."],
    ["Joint signatory on a client's bank account", "Depends", "Covered if you have control over the flow of funds (FAQ 9)."],
    ["Providing a mailing address for a client's notices and bank statements", "<strong>Yes</strong>", "Providing a correspondence address is a TCSP service (FAQ 21)."],
    ["Incorporating a company through a nominee director", "<strong>Yes</strong>", "Falls within the TCSP definition (FAQ 16)."],
    ["Financial due diligence when a client buys or sells a business", "<strong>Yes</strong>", "Part of buying and selling business entities (FAQ 7)."],
    ["Bookkeeping only", "No", "Bookkeeping alone is not a specified service (FAQ 6)."],
    ["Outsourced trainees doing bookkeeping without authority", "No", "Covered only if the engagement gives authority over funds (FAQ 12)."],
    ["Statutory audit", "No", "Not within the Accountant or TCSP definition (FAQ 18)."],
    ["Internal audit", "No", "Not within the definitions (FAQ 23)."],
    ["Tax advisory", "No", "Not within the TCSP definition (FAQ 24)."],
    ["Certifying the SBP Foreign Royalty Payment Form, or receipt of subscription money for a rights issue", "No", "Not within the definitions (FAQs 13 and 22)."],
])}
<p><strong>"Arranging" has a narrow meaning.</strong> It applies, for example, where you supply a director yourself, choose them without going back to the client, and complete the appointment formalities. Normal headhunting or advertising for a candidate does not count, and neither does sharing a list of candidates when you have no say in the selection (FAQs 3 and 4).</p>
<p><strong>"Ordinary course of business"</strong> is a judgment call. FBR suggests asking whether the activity is normal, frequent, regular, involves significant money or resources, earns income, or is offered as a service to customers (FAQ 5).</p>

<h2 id="apds">The Accountant Population Determination Survey</h2>
<p>FBR's FAQs state that all practising accountants are required to submit the Accountant Population Determination Survey (APDS). FBR uses it to identify which practices provide specified services. Submitting the survey is separate from DNFBP registration. If your answers show you provide specified services, the full DNFBP duties apply.</p>

<h2 id="duties">What Changes for a Covered Firm</h2>
<ul>
<li><strong>Register with FBR</strong> as a DNFBP and on {a(L2['goaml'], 'goAML')} with FMU.</li>
<li><strong>Appoint a compliance officer</strong> from senior management. The role does not have to be standalone; the person can carry out other duties too (FAQ 29).</li>
<li><strong>CDD on the right clients.</strong> CDD is mandatory for existing and new clients who receive Accountant or TCSP services. For other services such as audit it is not mandatory, though FBR encourages it (FAQ 17).</li>
<li><strong>Enhanced due diligence for high-value engagements.</strong> Where you will manage significant assets or funds above a threshold set in your own AML policy, obtain more information and verification of source of funds or wealth, and senior management approval before onboarding (FAQ 8).</li>
<li><strong>Beneficial ownership.</strong> For companies, identify the natural persons who ultimately own or control the client, using the company's register of ultimate beneficial owners.</li>
<li><strong>Report STRs promptly</strong> to FMU on goAML as soon as suspicion arises, not at year end (FAQ 15).</li>
<li><strong>Keep records:</strong> CDD for at least five years, STR and CTR records for at least ten.</li>
</ul>

<h2 id="red-flags">Red Flags FMU Lists for Accountants</h2>
<ul>
<li>A corporate structure more complex than the business needs, or links to nominee shareholders, bearer shares or foreign shell companies.</li>
<li>A client who is secretive about the beneficial owner or the source of funds, or who provides fabricated records.</li>
<li>Assets abroad that are not declared in the client's tax return, or loans from unidentified parties.</li>
<li>A company dormant after incorporation that suddenly shows large activity, or high turnover with no physical presence or visible business.</li>
<li>An address shared by many other companies, suggesting a mailbox service, or the same directors and owners across many companies.</li>
<li>Payments to related companies with the same directors or owners, without a plausible reason.</li>
<li>Unusually high fees offered for routine work, or sudden last-minute changes in how payment is made.</li>
<li>Trusts or waqf set up in a way that hides ownership, or that hold the shares of a company.</li>
</ul>

<h2 id="examples">Four Practice Scenarios</h2>
{table(["Practice", "Services", "Position"], [
    ["A tax consultant in Lahore who files returns, prepares wealth statements and replies to notices", "Tax work only", "Not a DNFBP on these services. Keep a written note of the assessment."],
    ["The same consultant also registers private limited companies with SECP for clients", "Formation agent", "In scope. Register, appoint a compliance officer, and apply CDD to company-formation clients."],
    ["A bookkeeping firm that also lets a client use its office as the company's registered address", "Registered or correspondence address", "In scope because of the address service, even if bookkeeping alone is not."],
    ["A consultant who is joint signatory on a client's account and approves payments", "Control over the flow of funds", "In scope. CDD and EDD apply to that client, depending on the amounts managed."],
])}

<h2 id="practical">A Practical Approach for Small Practices</h2>
<ol>
<li><strong>List your services</strong> and mark each one against the table above.</li>
<li><strong>If none is a specified service,</strong> keep a short written note of that assessment and review it when you add services.</li>
<li><strong>If any is,</strong> register, appoint the compliance officer, and apply CDD to the clients who receive those services.</li>
<li><strong>Adopt engagement terms</strong> that ask for CDD documents at onboarding and allow you to decline work when information is refused.</li>
<li><strong>Train staff</strong> on red flags and tipping off.</li>
</ol>
<p>Company formation is the service that most often brings small practices into scope. If you {a(L2['company'], 'register companies with SECP')} for clients, treat it as a specified service.</p>

<h2 id="how-we-help">How Kamboh Associates Helps Practices</h2>
<p>We help practices map their services against FBR's list, register with FBR and on goAML where needed, and write a CDD procedure and AML/CFT policy sized for a small firm. Our {a(L2['prog'], 'AML/CFT compliance programme guide')} sets out what the policy should contain. We reply on WhatsApp within office hours.</p>
""",
    faqs=[
        ("Are all accountants in Pakistan DNFBPs?",
         "No. FBR supervises accountants not regulated by ICAP or ICMAP, and only when they provide one of the 14 listed services, such as managing client money, forming companies or providing a registered address."),
        ("Does tax return filing or tax advice make me a DNFBP?",
         "No. FBR's 2023 FAQs say tax advisory services do not fall within the Trust and Company Service Provider definition. You may still be covered if you also provide a listed service."),
        ("Is registering a company with SECP for a client covered?",
         "Yes. FBR's FAQs treat registering a company or forming a firm on a client's behalf as acting as a formation agent, which is a specified service."),
        ("Are annual SECP returns covered?",
         "No. Filing annual returns and statutory forms after incorporation is a routine requirement under the Companies Act, 2017 and is not a reporting activity, according to FBR's FAQs."),
        ("Is there a turnover threshold for accountants?",
         "No. FBR's FAQs say coverage is based on the services provided and there is no financial limit, threshold or benchmark."),
        ("If I do the service for free, am I still covered?",
         "Yes. FBR's FAQs say an entity providing these services without any fee is still classified as a DNFBP."),
        ("Is statutory audit or bookkeeping covered?",
         "No. Statutory audit, internal audit and pure bookkeeping are not specified services under FBR's FAQs."),
        ("What is the APDS?",
         "The Accountant Population Determination Survey. FBR's FAQs say all practising accountants are required to submit it."),
        ("Must I do CDD on all my clients?",
         "CDD is mandatory for clients who receive Accountant or Trust and Company Service Provider services. For other services, such as audit, it is not mandatory but FBR encourages it."),
    ],
    sources=[S_FAQ23, S_ACC_GL, S_ACC_RF, S_REGS, S_GOAML, S_950],
    related=[(L['pillar'], "DNFBP Registration Guide"), (L2['goaml'], "goAML Registration Guide"), (L2['prog'], "AML/CFT Compliance Programme")],
    cta_h="Not Sure if Your Practice Is a DNFBP?",
    cta_p="Send us your list of services. We map them against FBR's 14 activities and tell you what applies.",
    wa_text="Assalam o Alaikum, main accountant / consultant hoon. Kya meri practice DNFBP mein aati hai? Madad chahiye.",
)


# ─────────────────────────────── COMPLIANCE PROGRAMME ───────────────────────────────
PROG = dict(
    slug=C_SLUG,
    svc={'h2': 'Get an Inspection-Ready Programme', 'intro': 'A programme that exists only as a downloaded template will not survive an inspection. We write one that matches how your business actually works, and test it.', 'hook': 'Want your AML programme written for you?', 'fee': 'Fixed fee, confirmed on WhatsApp before any work starts.', 'btn': 'Build my AML programme', 'items': ['Risk assessment for your customers, areas, services and payment methods', 'An AML/CFT policy your staff can follow', 'CDD and EDD forms, screening log and internal reporting form', 'Training notes and a training record', 'A pre-inspection review against the checklist above'], 'risks': ['FBR weighs whether you took reasonable steps before deciding a sanction', 'A missing programme is itself a breach']},
    title="AML/CFT Compliance Programme for DNFBPs: Policy & Checklist",
    h1="AML/CFT Compliance Programme for DNFBPs in Pakistan: Risk Assessment, Policy and Inspection Checklist",
    crumb="AML/CFT Compliance Programme",
    description="Build the AML/CFT programme FBR expects from a DNFBP: risk assessment, written policy, CDD, screening, training, audit and an inspection checklist.",
    keywords="AML CFT compliance programme DNFBP, AML policy for real estate agents Pakistan, DNFBP risk assessment template, FBR DNFBP inspection checklist, AML policy jeweller Pakistan",
    category="AML/CFT — Compliance",
    icon="📋",
    read="13 min read",
    banner="Registration only puts you on FBR's list. Inspections test whether your AML/CFT programme exists on paper and works in practice.",
    tldr=("A DNFBP's AML/CFT programme has five parts that FBR's regulations require: a written risk assessment (Reg. 4(1)), policies, controls and procedures "
          "that match that risk (Reg. 4(2)), a senior compliance officer, staff screening and ongoing training, and an independent audit function (Reg. 7(1)). "
          "Around these sit day-to-day CDD, sanctions screening, reporting to FMU and record keeping. The Sanctions Rules allow penalties of up to Rs 100 million "
          "per violation, but they also say FBR may not impose a sanction where the business took all reasonable steps and exercised all due diligence to comply. "
          "A documented, working programme is the strongest protection a DNFBP has."),
    lead=("Small property agencies, jewellers and practices often ask what an AML programme actually looks like for a business of their size. FBR does not "
          "expect a bank's compliance department, but it does expect specific documents and habits that can be shown to an inspector. This guide sets out each "
          "part, what to write, and a checklist to test whether you are ready."),
    body=f"""
<p class="tf-primary"><strong>Main guide:</strong> for who must register and the full list of DNFBP duties, see our {a(L['pillar'], 'DNFBP registration guide for Pakistan')}.</p>

<h2 id="why">Why a Written Programme Matters</h2>
<p>The AML/CFT Sanctions Rules, 2020 (S.R.O. 950(I)/2020) let FBR impose penalties of up to Rs 100 million per violation, restrictions, de-registration and action against managers. Yet Rule 4(2) also says the regulator <strong>may not impose a sanction if it is satisfied that the reporting entity took all reasonable steps and exercised all due diligence</strong> to ensure that the requirement would be complied with. When FBR does decide a penalty, Rule 4(3) tells it to weigh, among other factors, the gravity and duration of the breach, your compliance history, your financial strength, any profit gained, the remedial steps you took, and whether the breach was negligent or wilful.</p>
<p>In other words, a business that can show a sensible risk assessment, a policy that staff actually follow, and records that prove it, stands in a very different position from one that registered and did nothing else.</p>

<h2 id="five-parts">The Five Parts FBR's Regulations Require</h2>
{table(["Part", "What it means", "Source"], [
    ["1. Risk assessment", "Identify, assess and understand your ML, TF and PF risks by customer, country or area, product or service, and delivery channel.", "Reg. 4(1), S.R.O. 924(I)/2020"],
    ["2. Policies, controls and procedures", "Written rules that manage those risks: enhanced measures for higher risks, simplified only for lower risks, and never simplified where there is suspicion.", "Reg. 4(2)"],
    ["3. Compliance officer", "A senior management person responsible for AML/CFT, whose details are shared with FBR.", "Reg. 7(1); AMLA s.7G"],
    ["4. Staff screening and training", "Check integrity when hiring, and train staff on an ongoing basis.", "Reg. 7(1)"],
    ["5. Independent audit", "An independent check that the system works.", "Reg. 7(1)"],
])}

<h2 id="risk-assessment">Part 1: The Risk Assessment</h2>
<p>FBR's FAQs ask DNFBPs to consider the nature, size and complexity of the business, the products and services offered, how they are delivered, the types of customers, the countries involved, FBR's guidance, and any new technologies that might favour anonymity. Pakistan's National Risk Assessment is the starting reference. A simple, defensible format is a one-page table:</p>
{table(["Risk factor", "Questions to answer", "Example rating"], [
    ["Customers", "Who are they? Any PEPs, companies with complex ownership, NGOs, or customers with adverse news?", "Medium: mostly local individuals, a few company buyers"],
    ["Geography", "Do customers or funds come from abroad? Any FATF-listed jurisdictions?", "Low to medium: some overseas Pakistani buyers"],
    ["Products and services", "Which of your services move or hold value? High-value items, files, plots, formation services?", "High: plot files traded before possession"],
    ["Payments and channels", "How much cash? Third-party payments? Clients you never meet in person?", "High: cash token payments are common"],
    ["Overall", "Combine the above and note what controls reduce each risk.", "Medium-high, with EDD for cash and third-party payments"],
])}
<p>Review the assessment at least once a year, and sooner if your business changes. Keep each dated version.</p>

<h2 id="policy">Part 2: What the Written Policy Should Cover</h2>
<ol>
<li><strong>Scope and responsibility:</strong> which services are covered and who the compliance officer is.</li>
<li><strong>Customer acceptance:</strong> who you will not take on, for example customers who refuse identification or match a sanctions list.</li>
<li><strong>CDD procedure:</strong> what to collect from individuals and companies, how to verify it, and when beneficial ownership must be identified.</li>
<li><strong>Risk rating:</strong> how customers are rated low, medium or high, and what triggers enhanced due diligence.</li>
<li><strong>EDD procedure:</strong> source of funds and wealth, and senior management approval for high-risk customers and PEPs.</li>
<li><strong>Ongoing monitoring:</strong> review cycles that match risk. FBR's FAQs suggest at least once a year for high risk, every two years for medium and every three years for low, or sooner when something changes.</li>
<li><strong>Sanctions screening:</strong> which lists, when to screen (onboarding and when lists are updated), and what to do on a match: freeze, refuse, file an STR and inform FBR immediately.</li>
<li><strong>Reporting:</strong> how staff raise concerns internally, how the compliance officer decides, and how STRs and CTRs are filed on {a(L2['goaml'], 'goAML')}.</li>
<li><strong>Tipping off:</strong> a clear rule that no one tells a customer about a report.</li>
<li><strong>Record keeping:</strong> CDD for at least five years after the relationship ends; STR and CTR records for at least ten years from filing.</li>
<li><strong>Training and audit:</strong> how often, by whom, and how it is recorded.</li>
</ol>
<p>Keep the policy short enough that staff read it. A clear eight-page document that matches your real workflow is better than a long template copied from a bank.</p>

<h2 id="procedures">Turning the Policy Into Daily Procedures</h2>
{table(["Moment", "Procedure", "Evidence to keep"], [
    ["New customer", "Collect CDD, verify identity, identify beneficial owner, screen against sanctions lists, assign a risk rating", "CDD form, CNIC copy, screening result, risk rating"],
    ["High-risk customer", "Obtain source of funds or wealth and senior management approval", "Supporting documents and the signed approval"],
    ["Cash of Rs 2 million or more", "File a CTR on goAML", "CTR acknowledgement"],
    ["Something looks wrong", "Staff tell the compliance officer, who decides on an STR; decline the transaction where suspicion remains", "Internal note, STR acknowledgement (kept confidential)"],
    ["Customer profile changes", "Update CDD, for example when a customer becomes a PEP or moves abroad", "Updated CDD form"],
    ["Sanctions list updated", "Re-screen existing customers", "Screening log"],
])}

<h2 id="officer-training-audit">Parts 3 to 5: Officer, Training and Independent Audit</h2>
<p><strong>Compliance officer.</strong> FBR's FAQs define senior management to include the sole proprietor, the CEO, the managing partner or chief operating officer, or a partner or employee with enough knowledge of the business's risks and enough authority to act. The officer may have other duties. A sole proprietor with no employees is deemed to be the compliance officer.</p>
<p><strong>Staff screening and training.</strong> Check references and identity when hiring staff who deal with customers or money. Train them when they join and at regular intervals, using FMU's red flags for your sector, and record dates, topics and attendees.</p>
<p><strong>Independent audit.</strong> The regulations require an independent audit function to test the system. For a small business this can be a periodic review by someone outside the day-to-day process, such as an external adviser, who samples customer files, checks screening and reporting, and writes up findings and fixes.</p>

<h2 id="inspection-checklist">Inspection Readiness Checklist</h2>
<p>Use this list to check whether you could show FBR a working programme today:</p>
<ul>
<li>☐ FBR DNFBP registration is current, with correct owner, partner or director details.</li>
<li>☐ goAML registration is approved and the admin can log in.</li>
<li>☐ The compliance officer is named in writing and their details are with FBR.</li>
<li>☐ A dated risk assessment exists and was reviewed in the last 12 months.</li>
<li>☐ A written AML/CFT policy is approved and signed by the owner or senior management.</li>
<li>☐ Every in-scope customer file has a CDD form, ID copy, screening record and risk rating.</li>
<li>☐ High-risk files show source-of-funds evidence and senior approval.</li>
<li>☐ Cash transactions of Rs 2 million or more are matched to CTRs.</li>
<li>☐ There is an internal log of concerns raised and the decision on each, kept confidential.</li>
<li>☐ Training records show who was trained, when and on what.</li>
<li>☐ An independent review has been done, with findings followed up.</li>
<li>☐ Records go back at least five years (CDD) and ten years (STR and CTR), or to the date you registered.</li>
</ul>

<h2 id="if-sanctioned">If FBR Proposes a Sanction</h2>
<p>Rule 7 of the Sanctions Rules requires a written notice stating the proposed sanction, the violations behind it, your right to appeal and how to appeal. Rule 8 gives the right of appeal to a senior person in the regulator who did not take part in the original decision, and requires the regulator to publish an appeal procedure, including the time allowed to file. The appeal decision must be made within 180 days. Significant sanctions are published every quarter, so a quick, well-documented response matters. Our {a(L['notice'], 'FBR notice defence service')} prepares replies to notices of this kind.</p>

<h2 id="how-we-help">How Kamboh Associates Helps</h2>
<p>We write risk assessments, AML/CFT policies, CDD forms and training notes for {a(L['rea'], 'real estate agents')}, {a(L['jew'], 'jewellers')} and {a(L2['acc'], 'accountants')}, sized for the way each business actually works. We can also carry out a pre-inspection review against the checklist above and help with FBR and goAML registration. We reply on WhatsApp within office hours.</p>
""",
    faqs=[
        ("What must a DNFBP AML/CFT programme include?",
         "Under FBR's AML/CFT Regulations: a risk assessment, policies, controls and procedures matched to that risk, a senior compliance officer, staff screening and ongoing training, and an independent audit function, plus CDD, sanctions screening, reporting to FMU and record keeping."),
        ("Does a small property agency or jewellery shop need a written policy?",
         "Yes. The regulations require policies, controls and procedures for every DNFBP. They can be short and practical, but they should be written down and followed."),
        ("How often should the risk assessment be updated?",
         "Review it at least once a year and whenever the business changes significantly, keeping each dated version as evidence."),
        ("How often should customers be reviewed?",
         "FBR's FAQs give a guide: at least once a year for high-risk customers, every two years for medium risk and every three years for low risk, or sooner when something changes."),
        ("Can a sole proprietor be the compliance officer?",
         "Yes. A sole proprietor counts as senior management, and where there are no employees FBR deems the sole proprietor to be the compliance officer. The role can be combined with other duties."),
        ("What is an independent audit for a small DNFBP?",
         "A periodic check of the AML system by someone outside the day-to-day process, such as an external adviser, who tests customer files, screening and reporting and records findings."),
        ("Can FBR waive a penalty if we tried to comply?",
         "The Sanctions Rules say FBR may not impose a sanction if it is satisfied that the business took all reasonable steps and exercised all due diligence to comply. A documented programme is how you show that."),
        ("What is the maximum penalty for AML breaches by a DNFBP?",
         "Up to Rs 100 million per violation under the AML/CFT Sanctions Rules, 2020, on a risk-based scale, along with other possible sanctions such as restrictions or de-registration."),
        ("Can I appeal an FBR AML sanction?",
         "Yes. The Sanctions Rules give a right of appeal to a senior person in the regulator who was not part of the original decision, and the decision on the appeal must be made within 180 days."),
    ],
    sources=[S_REGS, S_950, S_FAQ23, S_REA_SG, S_INTRO, S_GOAML, S_REDF],
    related=[(L['pillar'], "DNFBP Registration Guide"), (L2['goaml'], "goAML Registration Guide"), (L2['acc'], "DNFBP Rules for Accountants")],
    cta_h="Get an Inspection-Ready AML Programme",
    cta_p="Risk assessment, policy, CDD forms and staff training notes written for your business, plus a pre-inspection review.",
    wa_text="Assalam o Alaikum, mujhe DNFBP ke liye AML/CFT policy aur compliance programme banwana hai.",
)

POSTS = [GOAML, ACC, PROG]
