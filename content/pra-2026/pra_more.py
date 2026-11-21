"""Extra sections and FAQs for the PRA series: worked cases and practical detail from the same official texts (checked 21 November 2026)."""
from pra_common import *

MORE = {
SL["proc"]: (f"""
<h2 id="timeline">A Realistic Timeline</h2>
{table(["Day", "What happens", "Basis"], [
    ["Day 0", "Documents collected; FBR profile checked and corrected", "PST-01 authorises PRA to take FBR particulars"],
    ["Day 0 or 1", "Application filed on PRA IRIS; codes confirmed; password received", "PRAL manual, part 2.1"],
    ["Day 0 or 1", "Provisional certificate of registration", "Rule 3(1)"],
    ["Within 48 working hours of review", "Status notified after a tax officer's review", "e-PRA login page"],
    ["Preferably within 30 days", "Final certificate in Form PST-03, or reasons for rejection", "Rules 3(2), 3(3)"],
])}
<p>The only part you fully control is day 0. A complete, correct file is what keeps the rest of the timeline short.</p>
""", [
    ("Do I have to visit a PRA office to register?", "No. Rule 3(1) allows the application electronically or manually, and the PRAL manual describes the full process online on PRA IRIS."),
    ("What does 'Registration Basis' mean on PRA IRIS?", "It is the drop-down where you choose voluntary registration or the notice/compulsory route; the notice route asks for the Notice Bar Code."),
]),
SL["docs"]: (f"""
<h2 id="cases">Three Common Cases</h2>
{table(["Applicant", "Identity", "Premises", "Extra"], [
    ["Consultant working from a rented office", "CNIC + NTN", "Rent agreement, landlord's CNIC, electricity bill", "One bank account certificate"],
    ["Salon owner with two outlets, one billing system", "CNIC + NTN", "Papers and electricity bill for each outlet", "Rule 2(2): one registration, both outlets listed"],
    ["Private limited agency", "Incorporation number + company NTN", "Office papers and electricity bill", "Directors' CNICs/NTNs (top ten), all company accounts"],
])}
<p>For a home-based business, Form PST-01 still asks for the place, how it is held and its electricity reference number. Use the same address you show on your FBR profile, or update FBR first.</p>
""", [
    ("Do I need photographs of the premises for PRA?", "Form PST-01 does not ask for photographs. It asks for the address, how the place is held, the electricity reference number, gas connection, phone and start date of each place."),
    ("Does PRA need a business bank account in the trade name?", "Form PST-01 asks for each bank account used in the business with its title; it does not say the title must be the trade name."),
    ("What if my FBR address is old?", "Update it with FBR first. PRA IRIS takes basic details from FBR and the Basic Information screen cannot be edited there."),
]),
SL["fee"]: (f"""
<h2 id="value">What Rs 5,000 Covers, Step by Step</h2>
<ol>
<li><strong>Intake on WhatsApp:</strong> we confirm your category (individual, AOP or company), your services and your places of business.</li>
<li><strong>FBR check:</strong> we compare your FBR profile with your documents, because PRA copies it and locks it.</li>
<li><strong>Form PST-01 preparation:</strong> principal service, other activities, each place with its electricity reference and possession, each bank account.</li>
<li><strong>Filing:</strong> on PRA IRIS, with you confirming the codes sent to your mobile and email.</li>
<li><strong>Provisional certificate:</strong> sent to you on filing (rule 3(1)).</li>
<li><strong>Follow-up:</strong> any verification query answered until the PST-03 certificate is issued (rule 3(2)).</li>
</ol>
<p>Work outside registration, such as a change of particulars later under rule 11 or de-registration under rule 5, is quoted separately as a fixed fee before work starts.</p>

<h2 id="pay">How Payment Works</h2>
<p>We confirm the fee on WhatsApp before any work starts. Nothing is payable to PRA for the registration itself, so there is no government challan in the process. If someone asks you to pay a "PRA registration fee", ask them to show the rule; rule 15 says there is none.</p>
""", [
    ("Is the Rs 5,000 refundable if PRA rejects my application?", "Rule 3(3) requires PRA to give reasons for any rejection. We go through the reasons with you, and any further work and its fee are confirmed before it starts."),
    ("Do I pay anything when my registration certificate is issued?", "No. Neither the provisional certificate nor Form PST-03 carries a fee (rule 15)."),
    ("Is NTN registration included in Rs 5,000?", "No. NTN registration is Rs 2,000 extra, and only if you do not already have an NTN."),
]),
SL["cert"]: (f"""
<h2 id="who-asks">Who Asks for the Certificate, and What They Need</h2>
{table(["Who asks", "What usually satisfies them", "Why"], [
    ["A corporate client paying your invoice", "Your registration number on the invoice and a profile inquiry result", "Section 25(5): reliance on PRA's list"],
    ["A tender committee", "The PST-03 certificate listing the service tendered for", "Rule 2(3): services shown on the certificate"],
    ["A bank opening a business account", "The certificate, or the provisional certificate while PST-03 is pending", "Rule 3"],
    ["A landlord or partner", "The certificate showing the business address", "Rule 11 keeps the address current"],
])}
<p>If the service being tendered for is not on your certificate, add it through a rule 11 change before you submit the tender.</p>
""", [
    ("Is the provisional certificate valid proof?", "It is issued under rule 3(1) on applying. The final proof of registration is the Form PST-03 certificate issued after verification."),
    ("Where do I find my PRA registration number?", "On the certificate issued under rule 3. For businesses registered automatically from FBR, rule 10 makes it P followed by the NTN."),
]),
SL["ver"]: (f"""
<h2 id="before-pay">A Checklist Before You Pay a Supplier's PRA Tax</h2>
<ol>
<li>Copy the registration number from the supplier's invoice (rule 2(5) requires it there).</li>
<li>Search it on the Taxpayer Profile Inquiry and compare the name with the invoice.</li>
<li>Confirm the supplier appears on the Active Taxpayer List (Sales Tax).</li>
<li>Save a screenshot with the date; section 25(5) protects reasonable reliance on PRA's list.</li>
<li>If the supplier is missing, ask for an explanation before paying the tax portion.</li>
</ol>
<p>Rule 8 is the reason for step 3: invoices issued during a suspension are not eligible for tax credit, adjustment or refund.</p>
""", [
    ("Can I verify a PRA payment receipt?", "Yes. The e-PRA page lists PSID/CPR verification for payment slip IDs and computerised payment receipts."),
    ("What if a supplier's number shows a different name?", "Rule 4 says only the registered person may use a registration or its number. Ask the supplier to explain before you rely on the invoice."),
]),
SL["who"]: (f"""
<h2 id="examples">Worked Examples</h2>
{table(["Business", "Section 25 question", "Likely route"], [
    ["Consultancy firm with an office in Lahore", "Is the consultancy a taxable service under the current schedules?", "If yes: register under s.25(1)(a)"],
    ["Karachi agency with a branch office in Lahore", "Is the service provided from a place of business in Punjab?", "Separate Punjab registration (rule 2(4))"],
    ["New service business not yet trading", "Is registration required yet?", "Voluntary registration if s.26 conditions are met"],
    ["Shop that only buys services from outside Punjab", "Is the service taxable by virtue of s.3(2)?", "Check s.25(3) recipient rule"],
])}
<p>Each answer turns on whether the service is taxable under the current Act and schedules, which change through Finance Acts. We check the current position on PRA's own texts before advising.</p>
""", [
    ("Does PRA registration depend on turnover?", "Section 25(1)(a) turns on providing a taxable service from a place of business in Punjab. Any other criteria are those PRA prescribes under section 25(2)."),
    ("Is a home-based service provider covered?", "Section 25(1)(a) speaks of an office or place of business in Punjab. Form PST-01 records the place, so a home used for the business is listed as the business place."),
]),
SL["comp"]: (f"""
<h2 id="prepare">What to Prepare for the Hearing</h2>
<ul>
<li><strong>The notice itself</strong>, with its date and bar code.</li>
<li><strong>A one-page description</strong> of what you charge for, to whom, and from which address.</li>
<li><strong>Proof of where you work from:</strong> ownership papers or rent agreement and an electricity bill.</li>
<li><strong>Your FBR record:</strong> NTN and recent returns, which also matter for section 26 conditions if you register voluntarily.</li>
<li><strong>Sample invoices or contracts</strong> showing the nature of the service.</li>
</ul>
<p>If the facts show you must register, the same documents complete Form PST-01 on the notice route, so nothing is wasted.</p>
""", [
    ("How long before the registration takes effect?", "Section 27(1) requires PRA to notify you not later than fifteen days before the day the compulsory registration takes effect."),
    ("Can an officer register me, or only PRA?", "Section 27(3) lets PRA authorise officers by Gazette notification to carry out compulsory registration functions."),
]),
SL["sole"]: (f"""
<h2 id="example">Example: A Lahore Salon Owner</h2>
<p>Sana runs a salon in her own name from a rented shop, with a second small outlet. Both use one booking and billing system. Her route:</p>
<ol>
<li>She already has an NTN, so we check her FBR profile and correct the address.</li>
<li>Category: individual, under her CNIC. Trade name: the salon's name, entered against both outlets.</li>
<li>Rule 2(2): one registration, because billing is centralised in Punjab; both outlets are listed.</li>
<li>Each outlet's rent agreement, landlord's CNIC and electricity reference number go on the form.</li>
<li>Her business bank account goes in the bank section.</li>
<li>Provisional certificate on filing; PST-03 after verification.</li>
</ol>
<p>Her cost: Rs 5,000 professional fee. PRA charges nothing.</p>
""", [
    ("Do I need a separate bank account for PRA?", "Form PST-01 asks for the bank accounts used in the business. It does not require a new account, but each business account must be listed."),
    ("Can a freelancer register with PRA as a sole proprietor?", "Yes, as an individual, if they provide a taxable service from a place of business in Punjab or register voluntarily under section 26."),
]),
SL["fbr"]: (f"""
<h2 id="example">Example: An Old FBR Registration</h2>
<p>A Lahore printing business registered with FBR years ago. The owner never saw a PRA letter, because the email on file was an old one. A search of the Taxpayer Profile Inquiry by P+NTN shows the business registered, but at its first address and without the design service it added later. The fix is one rule 11 change on Form PST-01: new address, the added service, and a current email and mobile. No new registration is needed.</p>
<p>The opposite case is common too: a newer business with an NTN that was never on FBR's sales tax side. It will not appear on PRA's list and applies on PRA IRIS using the option for persons who already have an NTN.</p>
""", [
    ("Will PRA use my FBR address?", "Form PST-01 authorises PRA to obtain your particulars from FBR, and PRA IRIS pre-fills basic details from FBR. Correct FBR first if it is out of date."),
    ("Can I have two PRA registrations, one automatic and one new?", "Rule 4 says a registration belongs only to the person registered. Check for a rule 10 registration before applying, so you do not create a second record."),
]),
SL["chg"]: (f"""
<h2 id="choose">Which Route Fits Your Situation</h2>
{table(["Situation", "Route", "Form or section"], [
    ["Moved office within Punjab", "Change of particulars", "PST-01, rule 11"],
    ["Moved to another PRA office's area", "Transfer of registration", "Rule 12(2)"],
    ["Added a service or branch", "Change of particulars", "PST-01, rules 2(3), 11"],
    ["Stopped providing taxable services", "De-registration", "PST-02, rule 5; s.29"],
    ["Business sold or merged", "Prior permission and notice; buyer registers", "Rule 14; s.20"],
    ["Received an inactivation notice", "Remedial action within the time given", "s.28(2)"],
    ["Registered compulsorily by mistake", "Cancellation ab initio", "Rule 13"],
])}
""", [
    ("Does de-registration clear my old tax liability?", "No. Rule 5 de-registers from the later of the date PRA specifies and the date outstanding tax is deposited, and rule 9 keeps undischarged liability alive."),
    ("Can PRA de-register me on its own?", "Yes. Section 29(1) lets PRA de-register a registered person, or a class of persons, not required to be registered under the Act."),
]),
}


def merge(p):
    body, faqs = MORE[p["slug"]]
    p = dict(p)
    p["body"] = p["body"].rstrip() + "\n" + body
    p["faqs"] = list(p["faqs"]) + faqs
    return p


S19 = f"""<p>Section 19 of the Act explains why careful buyers check. Where a registered person receiving a taxable service "is in the knowledge of or has reasonable grounds to suspect" that some or all of the tax on it "would go unpaid", the buyer and the provider "shall be jointly and severally liable" for the unpaid tax (s.19(1)). PRA may exempt persons or transactions from this by Gazette notification (s.19(2)). A buyer who checks PRA's list and keeps the result is in a far better position than one who ignored warning signs.</p>"""

MORE2 = {
SL["docs"]: ("", [
    ("Do I need my CNIC copy if PRA pulls details from FBR?", "Yes. Form PST-01 field 7 asks for the CNIC of an individual, and the codes and password go to the mobile and email you give, so keep the CNIC and live contact details ready."),
]),
SL["fee"]: (f"""
<h2 id="why-register">Why Clients Ask Their Suppliers to Register</h2>
<p>Many sole proprietors pay for PRA registration because a client asked for it. Section 19 of the Act explains the request: a registered buyer who knows or has reasonable grounds to suspect that the tax on a service will go unpaid can be held liable for it together with the supplier. Clients therefore prefer suppliers they can find on PRA's published list, as our {a(B["ver"], "verification guide")} explains.</p>
<p>So a registered supplier, visible on PRA's list, is easier for a client to work with. That is often the real return on a Rs 5,000 fee.</p>
""", []),
SL["cert"]: (f"""
<h2 id="joint">Why Your Clients Care: Joint Liability</h2>
<p>A client registered with PRA carries a risk when it pays an unregistered or doubtful supplier: under section 19, if it suspects the tax will go unpaid, it can share the liability. That is why finance teams ask for the certificate before the first payment.</p>
<p>Showing a valid certificate, a number that matches the Taxpayer Profile Inquiry, and a place on the Active Taxpayer List removes that doubt for your client.</p>
""", [
    ("Does my certificate show my branches?", "Form PST-01 lists every business place and rule 2(2) allows one registration for centrally billed branches. Any new branch is added through a rule 11 change."),
]),
SL["ver"]: (f"""
<h2 id="joint">Why Checking Protects You: Section 19</h2>
{S19}
<p>The two checks in this guide are the practical answer: run them before you pay, and keep the dated result with the invoice.</p>
""", []),
SL["sole"]: (f"""
<h2 id="first-invoice">Your First Invoice After Registration</h2>
<p>Section 18(2) of the Act sets when a service counts as provided for a tax period: when it is provided to the recipient, when an invoice is issued or due to be issued, or when payment is received, <strong>whichever is earlier</strong>. Section 18(1) links payment of the tax to the return for that period. For a new registrant that means two things: date your invoices accurately, and put your registration number on them from the first one (rule 2(5)).</p>
<h2 id="family">If the Owner Dies or the Business Passes On</h2>
<p>A sole proprietorship is tied to one person, so the Act covers what happens next. Section 21 makes the tax liability of a deceased registered person "the first charge on his estate in the hands of his successors". A family member who carries the business on should apply for a registration in their own name rather than use the late owner's number, which rule 4 does not allow.</p>
""", []),
SL["fbr"]: (f"""
<h2 id="charged">If You Charged PRA Tax Before Registering</h2>
<p>Some businesses add "PRA tax" to invoices before they are sure of their registration. Section 17 of the Act deals with this. Anyone who has collected tax "whether under misapprehension of any provision of this Act or otherwise" which was not payable, or more than was payable, and passed it on to the customer "shall pay the amount of tax or charge so collected to the Government" (s.17(1)). It is recoverable as an arrear (s.17(2)), and the burden of proving whether the tax was passed on lies on the person who collected it (s.17(3)).</p>
<p>The lesson is simple: confirm your PRA status first, then decide what your invoices show.</p>
<h2 id="time">When a Service Counts as Provided</h2>
<p>Section 18(2) treats a service as provided in the tax period in which it was provided, invoiced (or due to be invoiced) or paid for, whichever is earliest. If your registration takes effect partway through a project, this rule decides which invoices fall on which side.</p>
""", []),
SL["chg"]: (f"""
<h2 id="closing">Closing a Company or Firm: Who Stays Liable</h2>
<p>Three sections of Chapter III matter when a business ends rather than simply de-registers:</p>
<ul>
<li><strong>Deceased owner (s.21):</strong> the tax liability of a deceased registered person is the first charge on his estate in the hands of his successors.</li>
<li><strong>Bankruptcy (s.22):</strong> if the estate in bankruptcy continues the business, the tax liability passes to it and is paid before other creditors' claims.</li>
<li><strong>Wound-up company or enterprise (s.23):</strong> where tax cannot be recovered from a private company or business enterprise that is wound up, every owner, partner or director during the relevant period is jointly and severally liable.</li>
</ul>
<p>That is why we settle outstanding filings before applying on Form PST-02.</p>
""", []),
SL["comp"]: (f"""
<h2 id="past">What Happens to Past Periods</h2>
<p>Registration looks forward, but the Act also lets PRA look back. Under section 24, where an officer believes a registered person has not paid tax due or has paid short, the officer assesses the tax actually payable, with penalty and default surcharge under sections 48 and 49 (s.24(1)). Safeguards apply: a show cause notice must be given within five years of the end of the tax period (s.24(2)), and the order must be made within 120 days of that notice, ordinarily extendable by no more than 60 days (s.24(3)). Getting your registration and records in order early limits what can be looked back on.</p>
""", []),
SL["who"]: (f"""
<h2 id="excess">Do Not Charge PRA Tax Until You Know</h2>
<p>Section 17 makes anyone who collects tax that was not payable, or more than was payable, and passes it to the customer, pay that amount to the Government, recoverable as an arrear (s.17(1)-(2)). Settle the section 25 question first; then invoice accordingly.</p>
""", []),
SL["proc"]: ("", []),
}


def merge2(p):
    body, faqs = MORE2[p["slug"]]
    p = dict(p)
    p["body"] = p["body"].rstrip() + "\n" + body
    p["faqs"] = list(p["faqs"]) + faqs
    return p


FAQ3 = {
SL["docs"]: [
    ("What does a company need that an individual does not?", "Form PST-01 asks companies and registered AOPs for the registration or incorporation number and the top ten directors, shareholders or partners with their NTN, CNIC or passport number."),
],
SL["fee"]: [
    ("Does PRA charge for adding a branch or changing my address?", "Rule 15 covers registration and de-registration. Changes are made on Form PST-01 under rule 11; our fee for that work is a fixed fee confirmed before work starts."),
    ("Do I need to pay for the PRA verification services?", "The e-PRA page lists the Taxpayer Profile Inquiry and the Active Taxpayer List as online verification services; using them is part of the public portal."),
],
SL["cert"]: [
    ("What happens to my certificate if I sell the business?", "Rule 14 requires the Commissioner's prior permission for the sale, and the buyer must get a new registration or approved changes to the existing one."),
    ("Can my certificate be cancelled?", "Yes. Section 28 allows suspension and, after sixty days, cancellation; rule 6 allows suspension and cancellation for fraud or evasion after inquiry and a hearing."),
    ("Is the PRA certificate the same as an FBR STRN certificate?", "No. PRA registration is under the Punjab Sales Tax on Services Act 2012. Rule 10 gave existing FBR registrants a separate P+NTN registration with PRA."),
],
SL["ver"]: [
    ("Is the Active Taxpayer List the same as FBR's ATL?", "No. The PRA list is the Active Taxpayer List (Sales Tax) published by the Punjab Revenue Authority, separate from FBR's lists."),
    ("Can I search by CNIC for a sole proprietor?", "Yes. The Taxpayer Profile Inquiry accepts CNIC, which suits individuals and sole proprietors registered under their own CNIC."),
    ("How long can a suspension last before cancellation?", "Section 28(5)-(6): PRA may withdraw it within sixty days; after sixty days it may start proceedings, reinstate the registration or cancel it."),
],
SL["who"]: [
    ("Can PRA set extra criteria for registration?", "Yes. Section 25(1)(c) and 25(2) let PRA prescribe other criteria, conditions and restrictions by notification in the official Gazette."),
],
SL["comp"]: [
    ("Who receives the e-Enrolment codes?", "The PRAL manual says a verification SMS and code are sent to the mobile number and email entered on the e-Enrolment pop-up."),
    ("Can I choose the voluntary route after a notice?", "The PRA IRIS manual gives a separate Notice/Compulsory basis with the Notice Bar Code for a person who has received a notice; use that route."),
],
SL["sole"]: [
    ("Will my PRA registration show my own name or the shop name?", "The registered person is you, under your CNIC; Form PST-01 records the trade name against each business place."),
    ("What if I move my shop?", "Report the new address on Form PST-01 under rule 11; if the move takes you to another PRA office's area, rule 12 covers transfer of the registration."),
    ("Do I need PRA registration if I only work from home?", "Section 25(1)(a) asks whether you provide a taxable service from an office or place of business in Punjab. A home used for the business is listed as the business place on Form PST-01."),
],
SL["fbr"]: [
    ("How was I told about my automatic PRA registration?", "Rule 10 says by email, SMS, courier or post, with \"P\" as a prefix to your NTN."),
    ("Can PRA reject a change to an automatic registration?", "Yes. Rule 11 says PRA may approve or reject the requested change, preferably within thirty days of receiving it."),
],
SL["chg"]: [
    ("Can a cancelled PRA registration be restored?", "Rule 7 lets PRA revive a registration cancelled on an incorrect understanding of facts, on conditions and from a date it specifies."),
    ("Do I need permission to merge my business with another?", "Yes. Rule 14 requires the Commissioner's prior permission for a sale, and its explanation says sale includes merger."),
],
}


def merge3(p):
    p = dict(p)
    p["faqs"] = list(p["faqs"]) + FAQ3.get(p["slug"], [])
    return p

FAQ3[SL["fee"]] += [("Who pays if I need PRA registration for several provinces' work?", "PRA registration covers services rendered in Punjab (rule 2(4)). Registration in another province is with that province's authority; our fee for it is confirmed before work starts.")]
FAQ3[SL["cert"]] += [("What if PRA rejects my application?", "Rule 3(3) requires PRA to tell you the reasons within thirty days of receiving a complete application, so you can correct and reapply.")]
FAQ3[SL["ver"]] += [("Does the Taxpayer Profile Inquiry work for companies?", "Yes. It accepts the registration or incorporation number, used for companies and registered AOPs, as well as PNTN."),
                    ("Can I download PRA's active list?", "Yes. The e-PRA page links the Active Taxpayer List (Sales Tax) for download from PRA's registration site.")]
FAQ3[SL["who"]] += [("Does registering voluntarily carry the same duties?", "Yes. A person registered under section 26 is a registered person, so duties such as showing the registration number on invoices (rule 2(5)) apply.")]
FAQ3[SL["comp"]] += [("Is there a fee for compulsory registration?", "No. Rule 15 makes registration free of any fee or service charge, whatever the basis.")]
FAQ3[SL["sole"]] += [("Can my wife or son run the business under my PRA number?", "Rule 4 says only the registered person may use the registration or its number. If someone else will own and run the business, they need their own registration.")]
FAQ3[SL["fbr"]] += [("I closed my FBR sales tax registration years ago. Am I still on PRA?", "Possibly. A rule 10 registration is a PRA registration; it ends through PRA's own de-registration process on Form PST-02 (rule 5), so check the Taxpayer Profile Inquiry."),
                    ("Does the P+NTN appear on my invoices?", "Rule 2(5) requires your registration number on invoices, bills and vouchers; for a rule 10 registration that number is your P+NTN."),
                    ("Should I correct FBR or PRA first?", "FBR first. PRA IRIS takes basic details from FBR and locks them, so a correct FBR profile makes any PRA application or change straightforward.")]
FAQ3[SL["chg"]] += [("Do I still file while a de-registration application is pending?", "Your registration continues until PRA de-registers you from the date it specifies (rule 5); obligations of a registered person apply until then.")]

FAQ3[SL["cert"]] += [("Does the certificate expire?", "The 2012 Rules set no expiry date for the PST-03 certificate. A registration ends through de-registration (rule 5, section 29) or cancellation after suspension (section 28), so keep it active and your details current under rule 11.")]
FAQ3[SL["ver"]] += [("What should I do if my own registration shows old details?", "Apply for a change on Form PST-01 under rule 11. PRA approves or rejects the change, preferably within thirty days, and the inquiry then shows the new particulars.")]
FAQ3[SL["comp"]] += [("Can I ask for more time before the hearing?", "Section 27(2) guarantees advance notice and an opportunity of being heard in the manner PRA specifies. Ask the issuing officer in writing, quoting the notice, if you need time to gather documents.")]
FAQ3[SL["fbr"]] += [("Does rule 10 apply to businesses that registered with FBR recently?", "Rule 10 speaks of existing taxpayers already registered with FBR when the rules came into force. A business that registered later should check the Taxpayer Profile Inquiry and apply on PRA IRIS if it is not found.")]
FAQ3[SL["who"]] += [("Who decides whether my service is taxable?", "The Act and its schedules, as amended by Punjab Finance Acts. PRA publishes them; we check the current text on PRA's site before advising on your service.")]
