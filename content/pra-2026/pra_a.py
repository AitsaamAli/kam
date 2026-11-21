"""PRA series posts 1-5: process, documents, fee, certificate, verification."""
from pra_common import *

PROC = post(
    slug=SL["proc"],
    title="PRA Registration Process Online: Step by Step on PRA IRIS",
    h1="PRA Registration Process Online in Punjab: Every Step on PRA IRIS, Explained (2026)",
    crumb="PRA Registration Process",
    description="How to register with the Punjab Revenue Authority online: the New Registration screens on PRA IRIS, what each asks, OTPs, approval and the certificate.",
    keywords="pra registration process, pra registration online, how to register in pra, punjab revenue authority registration online, pra iris registration, new registration pra",
    read="11 min read",
    banner="PRA registration is free and fully online, but one wrong screen sends the application back. Here is each step in order.",
    tldr=("You register with the Punjab Revenue Authority on its IRIS portal by choosing New Registration, picking the basis (voluntary or on a notice), "
          "confirming one-time codes sent to your mobile and email, and completing the Basic Information, Address, Business, Utilities and Verification "
          "screens. Basic details are pulled from your FBR record and cannot be edited there, so an FBR NTN comes first. Rule 3 of the Registration Rules "
          "2012 gives you a provisional certificate at once and a final certificate (Form PST-03) after verification, preferably within thirty days. "
          "PRA charges no fee (rule 15)."),
    lead=("Most people who get stuck on PRA registration are not stuck on the law. They are stuck on a screen: a utility they did not have to hand, a "
          "business activity they could not find, or an address that FBR holds differently. This guide walks the PRA IRIS registration module in the "
          "order the official PRAL user manual describes it, and tells you what to prepare before each screen."),
    answers={
        "before": "Have an active FBR NTN, the mobile number and email you control, your business address, an electricity reference number and your bank account details ready.",
        "screens": "New Registration, verification codes, Basic Information, Address, Business, Utilities, a further details screen, then Verification and confirm.",
        "after": "Rule 3 gives a provisional certificate immediately; PRA verifies and issues Form PST-03, preferably within thirty days.",
        "mistakes": "Wrong principal activity, an address that does not match FBR, and a phone or email you cannot receive codes on cause most delays.",
    },
    svc=svc("Let Us File Your PRA Registration",
            "We prepare every screen before we submit, so the application goes in once, complete, and matches your FBR record.",
            ["Check your FBR NTN record first, so the pre-filled details are right",
             "Pick the correct principal service and any other activities",
             "Enter your business address, utility and bank details exactly",
             "Submit on PRA IRIS with you confirming the codes on your phone",
             "Follow up until the registration certificate is issued and send it to you"],
            ["A wrong principal activity can mean the wrong obligations from day one",
             "An address that differs from FBR's record holds up verification",
             "Registering under the wrong basis (voluntary vs notice) complicates a notice already issued"],
            "Need PRA registration without the trial and error?"),
    wa_text="Assalam o Alaikum, PRA registration karwani hai. CNIC aur business ki details bhej raha hoon.",
    body=f"""
{SERIES("proc")}

<h2 id="before">Before You Start: What PRA IRIS Will Ask For</h2>
<p>The PRA registration module runs on IRIS, the same system design FBR uses, and it is built on top of your FBR record. The official PRAL user manual (January 2024) says the information on the Basic Information screen is "pre-filled from the records fetched from FBR" and "cannot be edited". That one line decides your order of work: <strong>fix your FBR profile first</strong>, then register with PRA.</p>
<p>Form PST-01, the prescribed registration form appended to the 2012 Rules, shows what PRA wants to know about you. Read together with the IRIS screens, you need:</p>
<ul>
<li>An active NTN with FBR, and the CNIC of the individual (or the registration or incorporation number for a company or registered AOP)</li>
<li>A mobile number and an email address you can receive codes on today</li>
<li>Your business or mailing address, with province, district and city or tehsil</li>
<li>The services you provide, with one of them as your principal service</li>
<li>Each business place or branch: whether it is owned or rented (and the owner's CNIC or NTN if rented), its electricity reference number, whether a gas connection is installed, its phone and its start date</li>
<li>Each bank account used in the business: account number, title, bank, city and opening date</li>
</ul>
<p>Our {a(B["docs"], "documents checklist")} turns these fields into a list you can send to a client or collect yourself.</p>

<h2 id="screens">The Screens, In Order</h2>
<p>The manual describes the voluntary route screen by screen. Here is what each one does and what to watch for.</p>
<h3>1. New Registration</h3>
<p>On the PRA portal, click <strong>New Registration</strong>. Fill the starred fields. From the <strong>Registration Basis</strong> drop-down you choose one of two options: voluntary, or notice/compulsory. If PRA has already served you a notice, choose the notice option; the system then asks for the <strong>Notice Bar Code</strong> and verifies it. Then choose the <strong>Person</strong> type (individual, company or AOP), enter the captcha and submit.</p>
<h3>2. Verification codes</h3>
<p>A verification code goes to the mobile number and another to the email address you entered. Enter both, with the captcha, and click Next. If you are registering for someone else, they must be on the phone with you at this point.</p>
<h3>3. Basic Information</h3>
<p>This screen arrives filled from FBR and is locked. Two rules from the manual matter here: the "Withholding Agent" box is ticked automatically and cannot be changed for a company user, and the Business section becomes mandatory only if you tick <strong>Service Provider</strong>. Most applicants registering a service business tick it.</p>
<h3>4. Address</h3>
<p>Your address may already come from FBR's database; if not, add it with the "+" button, choose its type and save. At least one address must be selected (ticked) before you can move on.</p>
<h3>5. Business</h3>
<p>Add each business and its activities. The manual sets two hard rules: <strong>at least one activity must be marked Principal</strong>, and <strong>one business must be marked Primary Business</strong>. Pick addresses already saved or add new ones from this screen.</p>
<h3>6. Utilities</h3>
<p>Add the utility connections for the business place (Form PST-01 asks for the electricity reference number and whether gas is installed). Each entry is added with "+" and shows on a small dashboard.</p>
<h3>7. Further details and Verification</h3>
<p>One more screen asks for a link-type detail, added the same way. The last screen shows an <strong>undertaking</strong>; clicking Confirm means you declare the information authentic. The manual then says a <strong>password is sent to the registered email and mobile</strong>, and the registration process is complete on your side.</p>

<h2 id="after">What Happens After You Submit</h2>
<p>Rule 3 of the Registration and De-registration Rules 2012 sets the legal timetable:</p>
{table(["Stage", "What the rule says", "Rule"], [
    ["On applying", "The applicant is \"immediately\" issued a provisional certificate of registration", "3(1)"],
    ["Verification", "PRA may verify the particulars and the genuineness of documents", "3(2)"],
    ["Final certificate", "Issued in Form PST-03 with a registration number, \"preferably within thirty days\"", "3(2)"],
    ["Rejection", "Reasons given within thirty days of a complete application", "3(3)"],
])}
<p>The e-PRA login page adds a practical note: an application is reviewed by a tax officer and you are told the status "within 48 working hours". Read both together: you hear back quickly, and the final certificate follows verification. See our guide to the {a(B["cert"], "PST-03 certificate")} for what it shows and how to check it.</p>
<p>Two duties start with registration. Rule 2(5) requires you to show your registration number on invoices, bills, vouchers and letters to PRA. And section 25(4) lets PRA publish a list of registered persons on its website; under section 25(5) a customer may reasonably rely on that list, which is why being on it matters to clients who check.</p>

<h2 id="branches">One Registration or Several?</h2>
<p>Rule 2 answers the questions businesses ask most:</p>
<ul>
<li><strong>Several services:</strong> one application can list all of them, and the certificate shows all of them (rule 2(3)).</li>
<li><strong>Several premises:</strong> if billing or accounting is centralised in Punjab, you may take one registration (rule 2(2)). Each branch still goes on the form.</li>
<li><strong>Several provinces:</strong> a business providing services in Punjab and another province needs a <em>separate</em> Punjab registration for services rendered in Punjab (rule 2(4)). Our guide on {a(X["which"], "which provincial authority applies")} covers the other side.</li>
</ul>

<h2 id="mistakes">Mistakes That Hold Applications Up</h2>
<ol>
<li><strong>FBR details out of date.</strong> PRA pulls them and you cannot edit them there. Update your FBR profile first.</li>
<li><strong>No principal activity, or the wrong one.</strong> The system will not move on without one, and the wrong choice follows you.</li>
<li><strong>Codes going to an old number.</strong> The mobile and email must be live for both the codes and the password.</li>
<li><strong>Choosing voluntary when a notice exists.</strong> If PRA has served a notice, use the notice route and its bar code; see {a(B["comp"], "compulsory registration and e-Enrolment")}.</li>
<li><strong>Missing branch or bank details.</strong> Form PST-01 asks for every branch and every bank account. Leaving one out means a change application later under rule 11.</li>
</ol>
<p>If you already hold FBR sales tax registration, read {a(B["fbr"], "the P+NTN rule")} first: rule 10 may mean you are already registered with PRA.</p>
""",
    faqs=[
        ("Can I register with PRA without an NTN?", "PRA IRIS fills your Basic Information from FBR's records and that screen cannot be edited, so in practice you need an active FBR NTN before you start."),
        ("How long does PRA registration take?", "Rule 3 gives a provisional certificate immediately on applying and the final PST-03 certificate after verification, preferably within thirty days. The e-PRA page says status is notified within 48 working hours of review."),
        ("Is there a government fee for PRA registration?", "No. Rule 15 of the Registration and De-registration Rules 2012 says registration and de-registration are free of any fee or service charge."),
        ("Can one registration cover all my branches?", "Yes, if billing or accounting is centralised in Punjab (rule 2(2)). All branches are still listed in the application."),
        ("What if I also work in Sindh or KP?", "Rule 2(4) requires a separate registration for Punjab for services rendered in Punjab, alongside the other province's registration."),
        ("Who receives the password?", "The PRAL manual says the password is sent to the registered email address and mobile number once you confirm the undertaking."),
    ],
    sources=[S_RULES, S_MAN, S_LOGIN, S_ACT4, S_PRA],
    related=[(SVC, "PRA registration service"), (B["docs"], "PRA documents checklist"), (B["cert"], "PRA certificate (PST-03)")],
)

DOCS = post(
    slug=SL["docs"],
    title="PRA Registration Documents Required: Full Checklist (2026)",
    h1="PRA Registration Documents Required: The Complete Checklist From Form PST-01",
    crumb="PRA Registration Documents",
    description="Every document and detail PRA registration needs, taken from Form PST-01: CNIC, NTN, business address, premises, utility, bank account and services.",
    keywords="pra registration documents, pra registration documents required, pra registration requirements, documents for pra registration, pra registration form pst-01, punjab revenue authority registration documents",
    read="10 min read",
    banner="PRA does not publish a short list of documents. It publishes a form. This guide turns Form PST-01 into a checklist.",
    tldr=("PRA registration is driven by Form PST-01, the prescribed form under rule 3 of the Punjab Sales Tax on Services (Registration and "
          "De-registration) Rules 2012. It asks for your category (individual, company or AOP), CNIC or registration number, name, address, the services "
          "you provide and your principal service, phone and email, every business place (owned or rented, the owner's CNIC or NTN if rented, electricity "
          "reference number, gas connection, start date) and every business bank account. An individual also needs an active FBR NTN, because PRA IRIS "
          "takes your basic details from FBR."),
    lead=("Ask five people what PRA needs and you will get five lists. The reliable answer is the form itself. Form PST-01 is appended to the 2012 "
          "Registration Rules, and the PRA IRIS screens follow it field by field. This checklist is built from that form, so nothing on it is guesswork "
          "and nothing the form asks for is missing."),
    answers={
        "identity": "CNIC for an individual (passport for a non-resident), or the registration or incorporation number for a company or registered AOP, plus the FBR NTN.",
        "business": "The services you provide with one principal service, every business place, and how each place is held: owned, rented or other.",
        "premises": "For each place: electricity reference number, whether gas is installed, phone, start date, and the owner's CNIC or NTN if rented.",
        "bank": "Every bank account used in the business: number, title, bank, city and opening date.",
        "message": "Send one message with all items at once; partial sets cause back-and-forth and delay.",
    },
    svc=svc("Send Us the Documents, We Do the Rest",
            "We check every document against Form PST-01 before filing, so PRA's verification does not bounce it back.",
            ["A checklist matched to your category: individual, AOP or company",
             "A check of your FBR profile so the pre-filled details are right",
             "Branch, utility and bank details entered exactly as the form asks",
             "Filing on PRA IRIS and follow-up to the certificate"],
            ["A rented premises without the owner's CNIC or NTN stalls the application",
             "A missed bank account or branch means a change request later",
             "Details that differ from FBR's record cause verification queries"],
            "Collected the documents and want it filed correctly the first time?", "Send my documents"),
    wa_text="Assalam o Alaikum, PRA registration ke documents bhejne hain.",
    body=f"""
{SERIES("docs")}

<h2 id="identity">Identity and Category</h2>
<p>Form PST-01 opens with who you are. Section 4 of the form asks for your <strong>category</strong>: company, individual or AOP. Section 5 asks for the <strong>basis</strong>: as per law, voluntary registration, or compulsory registration. Section 6 asks for your <strong>status</strong>: resident or non-resident (and the country if non-resident). Then:</p>
{table(["Item", "Who needs it", "Form PST-01 field"], [
    ["CNIC (passport number for a non-resident)", "Individuals", "Field 7"],
    ["Registration or incorporation number", "Companies and registered AOPs", "Field 8"],
    ["Name of the registered person", "Everyone", "Field 9"],
    ["Directors, shareholders or partners (top ten, with NTN/CNIC/passport)", "Companies and AOPs", "Fields 16-18"],
    ["FBR NTN", "Everyone (PRA IRIS pulls basic details from FBR)", "Authorisation box, field 3"],
])}
<p>The form carries an authorisation: by applying you authorise PRA to obtain your registration particulars from FBR. That is why your <strong>FBR record must be current</strong> before you apply. If you have no NTN yet, start with {a(X["ntn"], "NTN registration")}.</p>

<h2 id="contact">Address, Phone and Email</h2>
<p>Field 10 asks for the registered office address for a company, or the mailing or business address for an individual or AOP, "for all correspondence". It is split into office, shop, house, flat or plot number; street, lane, plaza, floor or village; province; district; and city or tehsil. Fields 14 and 15 ask for phone, mobile and email.</p>
<p>The declaration at the end of the form says notices sent to that email or address are accepted as legal notice. So use an email someone reads. The PRA IRIS screens also send verification codes and your password to the mobile and email, which must be live on the day you apply.</p>

<h2 id="business">Services and Business Activity</h2>
<p>Field 11 lists types of service, field 12 asks for the <strong>principal service</strong>, and field 19 for other activities. The IRIS manual adds that at least one activity must be marked principal and one business marked primary. Before you apply, write down in one line what you charge clients for. That line decides the activity you choose.</p>
<p>If an agent files on your behalf under section 71, field 13 records the agent's CNIC or NTN, name and address. When we file for you, this is where our details go, with your consent.</p>

<h2 id="premises">Each Business Place</h2>
<p>Fields 20 to 25 repeat for every business, branch or outlet. For each one you need:</p>
<ul>
<li>The branch type (head office, showroom, godown, sub-office and so on), name and trade name</li>
<li>The full address</li>
<li><strong>Nature of possession</strong>: owned, rented or other, and the <strong>owner's CNIC, NTN or FTN</strong> if it is not yours</li>
<li>The <strong>electricity reference number</strong> and whether a <strong>gas connection</strong> is installed</li>
<li>The phone number and the date the business or branch started</li>
</ul>
<p>In practice, the documents that prove these are a recent electricity bill for each place (the reference number is on it), and the ownership papers or rent agreement with the landlord's CNIC.</p>

<h2 id="bank">Bank Accounts</h2>
<p>Fields 26 to 30 ask for every bank account used in the business: account number, account title, bank name, city and the date the account opened. A bank account maintenance certificate or the first page of a statement shows all of these.</p>

<h2 id="message">The Checklist to Send Us</h2>
<p>For a sole proprietor providing a service from one place, the whole set is usually:</p>
<ol>
<li>CNIC (front and back)</li>
<li>FBR NTN, or permission for us to register one ({a(X["pricing"], "Rs 2,000")})</li>
<li>A latest electricity bill of the business place</li>
<li>Rent agreement with the owner's CNIC, or ownership papers</li>
<li>Bank account maintenance certificate</li>
<li>One line on what services you provide, and since when</li>
<li>Your active mobile number and email</li>
</ol>
<p>Companies and AOPs add the incorporation or registration certificate and the directors' or partners' CNICs and NTNs. Several branches means items 3 and 4 for each branch. If you are not sure you must register at all, read {a(B["who"], "who must register with PRA")} first; sole proprietors should also see {a(B["sole"], "PRA registration for sole proprietors")}.</p>
""",
    faqs=[
        ("Which form is used for PRA registration?", "Form PST-01, prescribed by rule 3 of the Punjab Sales Tax on Services (Registration and De-registration) Rules 2012. The same form is used to report changes under rule 11."),
        ("Do I need a rent agreement for PRA registration?", "Form PST-01 asks whether each business place is owned, rented or other, and for the owner's CNIC, NTN or FTN where it is not yours, so a rent agreement with the landlord's CNIC is the usual proof."),
        ("Is an electricity bill required?", "The form asks for the electricity reference number of each business place and whether gas is installed. The reference number is printed on the bill."),
        ("Do I need to list every bank account?", "Form PST-01 asks for the total bank accounts and details of each one used in the business: number, title, bank, city and start date."),
        ("Can someone else file for me?", "Yes. Field 13 of Form PST-01 records an agent under section 71 with their CNIC or NTN, name and address."),
    ],
    sources=[S_RULES, S_MAN, S_ACT4, S_PRA],
    related=[(SVC, "PRA registration service"), (B["proc"], "PRA registration step by step"), (B["sole"], "PRA for sole proprietors")],
)

FEE_P = post(
    slug=SL["fee"],
    title="PRA Registration Fee: What PRA Charges and What You Pay",
    h1="PRA Registration Fee in Punjab: Free Under Rule 15, and What a Consultant Costs (2026)",
    crumb="PRA Registration Fee",
    description="PRA charges no fee to register or de-register: rule 15 of the 2012 Rules. What you pay a consultant, what it covers, and our fixed Rs 5,000 fee.",
    keywords="pra registration fee, pra registration fees, punjab revenue authority registration fee, pra fee, pra registration cost, pra registration charges",
    read="9 min read",
    banner="PRA itself charges nothing for registration. Anyone quoting a 'government fee' for it is wrong.",
    tldr=("Rule 15 of the Punjab Sales Tax on Services (Registration and De-registration) Rules 2012 says: \"Registration and deregistration under these "
          "rules shall be free of any fee or service charge.\" So the Punjab Revenue Authority charges nothing to register you or to cancel your "
          "registration. Any amount you pay goes to the person who prepares and files the application for you. Kamboh Associates charges a fixed "
          "Rs 5,000 professional fee for PRA registration, published on our pricing page, plus Rs 2,000 for an FBR NTN if you do not have one."),
    lead=("\"How much is PRA registration?\" has two answers, and mixing them up costs people money. The government side is fixed by law at zero. The "
          "professional side is whatever the person filing for you charges. This guide separates the two, shows what a fair professional fee should "
          "cover, and explains our own fee line by line."),
    answers={
        "law": "Rule 15: registration and de-registration are free of any fee or service charge.",
        "consultant": "A consultant's fee pays for preparing, checking and filing the application, and for follow-up with PRA. It is not a PRA charge.",
        "ours": "Rs 5,000 fixed for PRA registration; Rs 2,000 extra only if you need an FBR NTN first.",
        "hidden": "There are no PRA charges to add; ask any consultant to put the full fee in writing before work starts.",
    },
    svc=svc("PRA Registration for a Fixed Rs 5,000",
            "One published fee, confirmed before we start, covering everything up to the certificate.",
            ["FBR profile check and NTN if needed (Rs 2,000 extra)",
             "Form PST-01 details prepared and checked against your documents",
             "Filing on PRA IRIS with you confirming the codes",
             "Follow-up until the certificate is issued"],
            ["Paying someone for a 'government fee' that does not exist",
             "A cheap filing with the wrong principal service, fixed later with a change request",
             "No follow-up, so a verification query goes unanswered"],
            "Want PRA registration at a fixed, published price?", "Book my PRA registration"),
    wa_text="Assalam o Alaikum, PRA registration ki fee Rs 5,000 wali service chahiye.",
    body=f"""
{SERIES("fee")}

<h2 id="law">What the Law Says: Zero</h2>
<p>The 2012 Registration and De-registration Rules close with a short rule that settles the question. Rule 15, headed "No fee for registration or deregistration", reads: <em>"Registration and deregistration under these rules shall be free of any fee or service charge."</em></p>
<p>That covers both ends. Applying in Form PST-01 costs nothing. Applying in Form PST-02 to be de-registered costs nothing. The IRIS registration module asks for no payment at any step. There is no PSID to generate for registration.</p>
{table(["Action", "PRA charge", "Authority"], [
    ["New registration (Form PST-01)", "Nil", "Rule 15"],
    ["De-registration (Form PST-02)", "Nil", "Rule 15"],
    ["Provisional certificate on applying", "Nil", "Rule 3(1) with rule 15"],
    ["Final certificate (Form PST-03)", "Nil", "Rule 3(2) with rule 15"],
])}

<h2 id="consultant">What a Consultant's Fee Pays For</h2>
<p>If PRA is free, why pay anyone? Because the work is not the fee, it is the form. A professional fee buys:</p>
<ul>
<li><strong>A correct FBR base.</strong> PRA IRIS copies your basic details from FBR and locks them. If your FBR profile is wrong, the PRA application is wrong.</li>
<li><strong>The right principal service.</strong> The activity you pick becomes part of your registration. Getting it wrong means a change application under rule 11 later.</li>
<li><strong>Complete branch and bank data.</strong> Form PST-01 asks for every place and every account, with utility references and the landlord's CNIC or NTN.</li>
<li><strong>Follow-up.</strong> Rule 3(2) allows PRA to verify before issuing the final certificate. Someone has to answer queries quickly.</li>
</ul>

<h2 id="ours">Our Fee, Line by Line</h2>
{table(["Service", "Fee", "When it applies"], [
    ["PRA registration (preparation, filing, follow-up to certificate)", "Rs 5,000", "Every PRA registration"],
    ["FBR NTN registration", "Rs 2,000", "Only if you have no NTN"],
    ["PRA registration charge", "Rs 0", "Never: rule 15"],
])}
<p>Both fees are on our {a(X["pricing"], "pricing page")} and are confirmed in writing on WhatsApp before we start. A sole proprietor with an NTN pays Rs 5,000 in total; one without an NTN pays Rs 7,000.</p>

<h2 id="compare">How to Compare Quotes</h2>
<p>Quotes for PRA registration vary widely. Before you choose, ask each provider four questions:</p>
<ol>
<li><strong>Is any part of this a government fee?</strong> The honest answer is no (rule 15).</li>
<li><strong>Does the fee include an NTN if I need one?</strong> Some quotes do, some add it.</li>
<li><strong>Do you follow up until the certificate is issued?</strong> A filing without follow-up is half a job.</li>
<li><strong>Is the fee fixed and written?</strong> Ours is published and confirmed before work starts.</li>
</ol>

<h2 id="hidden">Costs That Are Not a Registration Fee</h2>
<p>Registration is free, but being registered has consequences you should know before you apply. Rule 2(5) requires your registration number on every invoice and bill. Section 28 lets PRA suspend a registration for non-compliance, and rule 8 says invoices issued during a suspension cannot be used by your customers for tax credit or adjustment. Those are obligations, not fees, and they are why choosing the right registration from the start matters. Our guide to {a(B["chg"], "changes, suspension and de-registration")} explains them.</p>
""",
    faqs=[
        ("Does PRA charge a fee for registration?", "No. Rule 15 of the Punjab Sales Tax on Services (Registration and De-registration) Rules 2012 makes registration and de-registration free of any fee or service charge."),
        ("How much does Kamboh Associates charge for PRA registration?", "Rs 5,000 fixed, as published on our pricing page. If you need an FBR NTN first, that is Rs 2,000 more."),
        ("Is there a fee to cancel PRA registration?", "No. Rule 15 covers de-registration too. The application is made in Form PST-02 under rule 5."),
        ("Do I pay PRA for the registration certificate?", "No. The provisional certificate is issued on applying and the PST-03 certificate after verification, both free under rule 15."),
        ("Why do quotes for PRA registration differ so much?", "Because the only cost is the professional's time and what they include. Ask whether the NTN and follow-up to the certificate are included."),
    ],
    sources=[S_RULES, S_MAN, S_ACT4, S_PRA],
    related=[(SVC, "PRA registration service"), (X["pricing"], "Our published fees"), (B["proc"], "PRA registration step by step")],
)

CERT = post(
    slug=SL["cert"],
    title="PRA Registration Certificate (PST-03): How to Get and Check It",
    h1="PRA Registration Certificate: Provisional Certificate, Form PST-03 and How to Check It",
    crumb="PRA Registration Certificate",
    description="The PRA registration certificate explained: provisional certificate on applying, final Form PST-03 within thirty days, what it shows and how to verify it.",
    keywords="pra registration certificate, pra certificate, pra registration certificate download, pst-03 certificate, punjab revenue authority registration certificate, pra registration number",
    read="9 min read",
    banner="You get two certificates from PRA, not one. Know which one your client or bank is asking for.",
    tldr=("Under rule 3 of the Punjab Sales Tax on Services (Registration and De-registration) Rules 2012, an applicant is immediately issued a "
          "provisional certificate of registration. After any verification, PRA issues the certificate of registration in Form PST-03 with a specific "
          "registration number, preferably within thirty days; a rejection must be explained within thirty days. Where you provide several services, "
          "the certificate lists all of them (rule 2(3)). Your registration number must appear on your invoices and letters to PRA (rule 2(5))."),
    lead=("Clients, banks and tender committees ask for \"the PRA certificate\". There are in fact two documents, issued at different times, and a "
          "registration number that matters more than either. This guide explains each, what it proves, and how anyone can check it online."),
    answers={
        "two": "A provisional certificate is issued immediately on applying (rule 3(1)); the final certificate in Form PST-03 follows verification (rule 3(2)).",
        "shows": "The PST-03 certificate carries your specific registration number and, for several services, all of them (rule 2(3)).",
        "check": "Anyone can check registration through PRA's Taxpayer Profile Inquiry or the Active Taxpayer List on the e-PRA portal.",
        "use": "Show the registration number on every invoice, bill and voucher (rule 2(5)); never lend it (rule 4).",
    },
    svc=svc("Get Your PRA Certificate Without Delay",
            "We file a complete application so verification is quick, and we follow up until PST-03 is issued.",
            ["Complete Form PST-01 details so the certificate is right first time",
             "All your services listed so one certificate covers them",
             "Follow-up with PRA during verification",
             "Certificate sent to you, with a note on showing the number on invoices"],
            ["A certificate with the wrong services means a rule 11 change later",
             "Unanswered verification queries delay the final certificate",
             "Using another person's registration is barred by rule 4"],
            "Need a PRA certificate for a client or tender?", "Get my PRA certificate"),
    wa_text="Assalam o Alaikum, PRA registration certificate chahiye.",
    body=f"""
{SERIES("cert")}

<h2 id="two">Two Certificates, Two Moments</h2>
{table(["Document", "When", "Rule"], [
    ["Provisional certificate of registration", "\"Immediately\" on applying in Form PST-01", "3(1)"],
    ["Certificate of registration, Form PST-03", "After verification, \"preferably within thirty days\" of the application", "3(2)"],
    ["Written reasons for rejection", "Within thirty days of a complete application", "3(3)"],
])}
<p>Rule 3(2) explains the gap. PRA "may cause further verification or inquiry to ascertain the accuracy of information or particulars declared" and the "genuineness of the documents". Only "on completion of such verification or inquiry" does it register the applicant and issue PST-03 "with specific number of the applicant". In practice, the provisional certificate lets you show you have applied; PST-03 is the final proof.</p>
<p>The e-PRA login page states that an application is reviewed by a tax officer and the applicant is told its status within 48 working hours. That is the first response, not the end of verification.</p>

<h2 id="shows">What the Certificate Shows</h2>
<p>Form PST-03 is appended to the 2012 Rules under rule 3(2). Two rules shape its content:</p>
<ul>
<li><strong>All your services on one certificate.</strong> Rule 2(3): where a person provides more than one taxable service, a single application can mention all of them "and certificate of registration in such case shall indicate details of all taxable services provided by him".</li>
<li><strong>Your registration number.</strong> Rule 10 explains the format for businesses already registered with FBR: PRA assigns "P" as a prefix to the NTN (P+NTN). See {a(B["fbr"], "the P+NTN guide")}.</li>
</ul>

<h2 id="check">How Anyone Can Check a PRA Registration</h2>
<p>Section 25(4) of the Punjab Sales Tax on Services Act 2012 allows PRA to publish a list of registered persons on its website, and section 25(5) says it is reasonable for a person to believe another is registered if they are on that list. The e-PRA portal offers two public checks:</p>
<ul>
<li><strong>Active Taxpayer List (Sales Tax)</strong>: a downloadable list of active registered persons.</li>
<li><strong>Taxpayer Profile Inquiry</strong>: search by PNTN, CNIC, passport number or registration/incorporation number.</li>
</ul>
<p>Our {a(B["ver"], "verification guide")} walks through both and what each result means.</p>

<h2 id="use">Using the Certificate Correctly</h2>
<p>Rule 2(5) requires every registered person to "invariably and conspicuously mention his registration number" on invoices, bills, vouchers and similar documents, and in correspondence with PRA. Rule 4 adds that nobody except the person registered can use the registration or its number, and that a registration cannot be disposed of in any manner. Lending your number to a friend's business is not allowed.</p>
<p>If your name, address or other particulars change, the certificate must be updated through Form PST-01 under rule 11; PRA approves or rejects the change "preferably within thirty days".</p>

<h2 id="lost">If the Certificate Is Wrong or Missing</h2>
<ol>
<li><strong>Wrong particulars:</strong> apply for a change under rule 11.</li>
<li><strong>A service missing:</strong> the same rule 11 change adds it, so the certificate covers all services.</li>
<li><strong>No final certificate after thirty days:</strong> rule 3(3) requires reasons if PRA rejects; ask for the status through the portal or the helpline.</li>
<li><strong>Registration not showing in the inquiry:</strong> check whether it was suspended under section 28; suspension removes the name from the published list (section 28(4)).</li>
</ol>
""",
    faqs=[
        ("When do I get the PRA registration certificate?", "A provisional certificate is issued immediately on applying (rule 3(1)); the final Form PST-03 certificate follows verification, preferably within thirty days (rule 3(2))."),
        ("Does one certificate cover several services?", "Yes. Rule 2(3) allows one application for all your taxable services and the certificate shows all of them."),
        ("How can a client check my PRA registration?", "Through the Taxpayer Profile Inquiry (by PNTN, CNIC, passport or registration number) or the Active Taxpayer List on the e-PRA portal."),
        ("Do I have to print the number on invoices?", "Yes. Rule 2(5) requires the registration number on invoices, bills, vouchers and correspondence with PRA."),
        ("Can I let another business use my PRA number?", "No. Rule 4 says only the person registered can use the registration or its number, and it cannot be disposed of."),
    ],
    sources=[S_RULES, S_ACT4, S_LOGIN, S_ATL, S_PRA],
    related=[(SVC, "PRA registration service"), (B["ver"], "Verify a PRA registration"), (B["fbr"], "P+NTN for FBR-registered businesses")],
)

VER = post(
    slug=SL["ver"],
    title="PRA NTN Verification: Taxpayer Profile Inquiry and Active List",
    h1="PRA NTN Verification and Taxpayer Profile Inquiry: How to Check a PRA Registration (2026)",
    crumb="PRA Verification",
    description="Check any PRA registration: Taxpayer Profile Inquiry by PNTN, CNIC or passport, the Active Taxpayer List, and what an inactive or missing result means.",
    keywords="pra ntn verification, pra ntn inquiry, pra taxpayer profile inquiry, pra registration check, pra registration verification, pra active taxpayer list, pntn",
    read="9 min read",
    banner="Before you pay a supplier's PRA tax, or rely on your own registration, check it on PRA's own system.",
    tldr=("The e-PRA portal lists public online verification services: a Taxpayer Profile Inquiry that searches by PNTN, CNIC, passport number or "
          "registration/incorporation number, and a downloadable Active Taxpayer List (Sales Tax). Section 25(4) of the Punjab Sales Tax on Services Act "
          "2012 allows PRA to publish the list of registered persons, and section 25(5) makes it reasonable to rely on it. A suspended registration is "
          "removed from the published list (section 28(4)), so a missing name can mean suspension, not just non-registration."),
    lead=("A PRA registration number on an invoice proves nothing by itself. What proves it is PRA's own record. This guide shows the two checks "
          "anyone can run, how to read each result, and what to do when your own registration does not show."),
    answers={
        "pntn": "PNTN is the PRA number for businesses already registered with FBR: rule 10 assigns \"P\" as a prefix to the NTN.",
        "inquiry": "Search by PNTN, CNIC, passport number or registration/incorporation number on the e-PRA portal.",
        "list": "Download the Active Taxpayer List (Sales Tax) from PRA's registration site and search the name or number.",
        "results": "Found and active: registered. Missing: never registered, or suspended (section 28(4) removes suspended names).",
        "own": "If your own name is missing, check for a suspension notice and act within sixty days (section 28(5)).",
    },
    svc=svc("Not Showing on PRA? We Sort It Out",
            "Whether you need a new registration or your existing one is missing from PRA's list, we find out why and fix it.",
            ["Check your status on the Taxpayer Profile Inquiry and the Active List",
             "Trace a suspension notice and the remedial action it asks for",
             "New registration if you were never registered",
             "Change of particulars if the record shows old details"],
            ["Customers may stop relying on an unlisted registration (section 25(5))",
             "Invoices issued while suspended do not give customers tax credit (rule 8)",
             "After sixty days a suspension can lead to cancellation (section 28(6))"],
            "Your PRA registration missing or never done?", "Check my PRA status"),
    wa_text="Assalam o Alaikum, PRA registration ka status check karwana hai.",
    body=f"""
{SERIES("ver")}

<h2 id="pntn">PNTN: The Number You Search By</h2>
<p>Rule 10 of the Registration and De-registration Rules 2012 says that taxpayers already registered with FBR were registered with PRA automatically and were told by email, SMS, courier or post, "assigning them 'P' as prefix to NTN (P+NTN)". That P+NTN is what the portal calls <strong>PNTN</strong>. For anyone registered fresh through PRA IRIS, the registration number appears on the certificate issued under rule 3.</p>

<h2 id="inquiry">Check 1: Taxpayer Profile Inquiry</h2>
<p>The e-PRA login page lists "Taxpayer Profile Inquiry" under its online verification services. It accepts four kinds of search:</p>
{table(["Search by", "Use it when"], [
    ["PNTN", "You have the P+NTN from an invoice or certificate"],
    ["CNIC", "Checking an individual or sole proprietor"],
    ["Passport No.", "Checking a non-resident individual"],
    ["Reg./Inc. No.", "Checking a company or registered AOP"],
])}
<p>Search, then read the name, status and registration details against the invoice or document in front of you. A different name for the same number is a warning sign: rule 4 says only the registered person can use a registration or its number.</p>

<h2 id="list">Check 2: The Active Taxpayer List (Sales Tax)</h2>
<p>The same page links the <strong>Active Taxpayer List (Sales Tax)</strong> for download from PRA's registration site. Section 25(4) of the Act allows PRA to publish a list of registered persons, and section 25(5) says: "It shall be reasonable for a person to believe that another person is registered under this Act if that other person is on the list placed on the website of the Authority." For a business paying a supplier, that is the legal basis for relying on the list.</p>

<h2 id="results">Reading the Result</h2>
{table(["Result", "What it usually means", "Law"], [
    ["Found, active", "Registered and on PRA's published list", "s.25(4)-(5)"],
    ["Not found at all", "Never registered with PRA, or a typing error in the search", "s.25"],
    ["Was listed, now missing", "Possibly suspended: suspension is effected by removing the name from the list", "s.28(4)"],
    ["Different name on the number", "Possible misuse of a registration", "Rule 4"],
])}

<h2 id="own">If Your Own Registration Is Missing</h2>
<p>Section 28 sets out a process, not a sudden switch-off. PRA first may "temporarily inactivate" a registration if it is satisfied the person is not entitled to be registered or has not complied with the Act or rules (s.28(1)). It must give notice with reasons and the remedial action needed (s.28(2)). If the response is not satisfactory, it may suspend, and suspension removes the name from the published list (s.28(3)-(4)).</p>
<ul>
<li><strong>Within sixty days</strong> of suspension, PRA may withdraw it if satisfied with your remedial action (s.28(5)).</li>
<li><strong>After sixty days</strong>, PRA may start proceedings, reinstate the registration, or cancel it (s.28(6)).</li>
<li>Cancellation needs an enquiry, investigation or audit, and never removes your other obligations (s.28(7)).</li>
</ul>
<p>Rule 8 shows why speed matters: invoices issued during a suspension are not eligible for tax credit, adjustment or refund. Your customers will notice. Read more in our guide to {a(B["chg"], "suspension and de-registration")}.</p>

<h2 id="other">Other Checks on the Same Page</h2>
<p>The e-PRA page also lists PSID/CPR verification (to check a payment slip or receipt) and Collecting Agent Invoice Verification. For help, it gives the helpline UAN 042-111-000-772 (9 am to 5 pm, Monday to Friday) and eSupport@pra.punjab.gov.pk.</p>
""",
    faqs=[
        ("What is PNTN in PRA?", "It is the PRA number of a business already registered with FBR: rule 10 of the 2012 Rules assigns \"P\" as a prefix to the NTN."),
        ("How do I check if a business is registered with PRA?", "Use the Taxpayer Profile Inquiry on the e-PRA portal (search by PNTN, CNIC, passport or registration number) or download the Active Taxpayer List (Sales Tax)."),
        ("Can I rely on PRA's list when paying a supplier?", "Section 25(5) of the Act says it is reasonable to believe a person is registered if they are on the list on PRA's website."),
        ("Why would a registered business disappear from the list?", "Suspension under section 28 is effected by removing the name from the published list (s.28(4))."),
        ("What is the PRA helpline?", "The e-PRA page gives UAN 042-111-000-772, 9 am to 5 pm, Monday to Friday, and eSupport@pra.punjab.gov.pk."),
    ],
    sources=[S_LOGIN, S_ATL, S_ACT4, S_RULES, S_PRA],
    related=[(SVC, "PRA registration service"), (B["cert"], "PRA certificate (PST-03)"), (B["chg"], "Suspension and de-registration")],
)
