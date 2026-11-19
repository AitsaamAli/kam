"""Form ATL-U series, posts 1-3."""
from atlu_common import *

PEN_NOTE = ("Section 182 penalty, as it stands in the Ordinance amended up to 30 June 2026: the higher of 0.1% of tax payable per day "
            "or Rs 1,000 per day; minimum Rs 10,000 for an individual with 75% or more of income from salary and Rs 50,000 in other cases; "
            "maximum 200% of tax payable; reduced by 75%, 50% or 25% if the return is filed within one, two or three months after the due date.")

# ───────────────────────────── 1. Pillar guide ─────────────────────────────
GUIDE = dict(
    slug=SL["guide"],
    svc=dict(h2="Late Return Plus Form ATL-U, Filed for You", intro="If you are not planning to buy property in the next six months, Form ATL-U is usually the cheapest way back onto the Active Taxpayers List. We file the late return correctly, then furnish the undertaking and track your ATL status until your name appears.",
             hook="Missed 31 October 2026 and no property purchase planned?", fee=F_ALL, btn="File my return with Form ATL-U",
             items=["A quick check that you qualify: individual, return filed (or being filed) late, no property purchase planned for six months",
                    "Your Tax Year 2026 return and wealth statement prepared and filed on IRIS",
                    "Form ATL-U furnished on IRIS and the acknowledgement saved for your record",
                    "The exact date your six months end, in writing, so you know when you can buy again",
                    "An ATL status check after FBR's next update, with follow-up if your name does not appear"],
             risks=["Signing the undertaking with a property deal already in the pipeline can cost you the waiver and bring the surcharge back",
                    "A late return filed with mistakes still leaves you exposed to notices, even if you reach the ATL",
                    "Paying Rs 25,000 when the undertaking would have done the same job is money you do not get back"]),
    title="Form ATL-U 2026: ATL Without the Rs 25,000 Surcharge",
    h1="Form ATL-U 2026: How Late Filers Join the Active Taxpayers List Without Paying the Rs 25,000 Surcharge",
    crumb="Form ATL-U Guide 2026",
    description="Form ATL-U explained: who can use it, the six-month property undertaking, what it saves, what it does not cover, and how a late filer reaches the ATL.",
    keywords="form atl u, atl-u form, atl u fbr, form atl-u fbr 2026, atl without surcharge, section 182a(3) undertaking, sro 2097 2026",
    category="Form ATL-U", icon="📝", read="13 min read",
    banner="Filed your 2026 return after the deadline? If you will not buy property in the next six months, the law now gives you a way onto the ATL without the Rs 25,000 surcharge.",
    tldr=("Form ATL-U is the undertaking an individual furnishes under Section 182A(3) of the Income Tax Ordinance 2001, added by the Finance Act 2026. "
          "A person who files a return after the due date is kept off the Active Taxpayers List (ATL) for that year unless a surcharge is paid: Rs 25,000 for an individual, "
          "Rs 50,000 for an association of persons and Rs 100,000 for a company. Section 182A(3) lifts that condition for an individual who declares that he will not purchase, "
          "acquire or otherwise obtain ownership or beneficial interest in any property for six months from the date of the undertaking. FBR prescribed the form through "
          "SRO 2097(I)/2026 dated 10 November 2026. It is free to furnish, but it does not cancel the Section 182 late-filing penalty, and breaking the promise brings the surcharge rule back."),
    lead=("Until this year a late filer had one way back onto the ATL: pay the surcharge. When the Finance Act 2026 raised the individual surcharge from Rs 1,000 to Rs 25,000, "
          "it also added a second route for individuals. This guide explains that route from the law itself, who it suits, who it does not, and the mistakes that cost people the benefit."),
    body=f"""
{SERIES}

<h2 id="why-off-atl">Why a Late Return Keeps You Off the ATL</h2>
<p>The ATL is FBR's list of people who have filed their income tax return. Being on it is what makes you a "filer" in practice: banks, property registrars, motor vehicle authorities and companies paying dividends check it before deciding which withholding rate to apply.</p>
<p>Section 182A(1) says that a person who fails to file the return by the due date in Section 118, or by a date extended by the Board under Section 214A or by the Commissioner under Section 119, shall not be included in the ATL for the year for which the return was not filed on time. For Tax Year 2026 the extended date was 31 October 2026, so a return filed on 1 November 2026 or later is a late return.</p>
<p>The same section adds three more consequences for the late filer: the loss for that tax year cannot be carried forward under Part VIII of Chapter IV, no refund is issued while the person is not on the ATL, and that period does not count towards the additional payment for delayed refunds under Section 171.</p>

<h2 id="two-routes">The Two Routes Back</h2>
{table(["", "Route 1: Surcharge", "Route 2: Form ATL-U"], [
    ["Legal basis", "Proviso to Section 182A(1)(a)", "Section 182A(3), with Form ATL-U prescribed by SRO 2097(I)/2026"],
    ["Who can use it", "Individuals, AOPs and companies", "Individuals only"],
    ["Cost to you", "Rs 25,000 (individual), Rs 50,000 (AOP), Rs 100,000 (company)", "No payment to FBR for the undertaking itself"],
    ["Condition", "None after payment", "No purchase, acquisition or beneficial interest in any property for six months"],
    ["Risk", "None once paid", "If you breach the undertaking, the waiver is withdrawn and the surcharge rule applies again"],
])}
<p>For a full side-by-side discussion of the two routes, including the cases where paying is the better decision, see our {a(X["cmp"], "surcharge vs Form ATL-U comparison")}. This guide concentrates on how the undertaking itself works.</p>

<h2 id="law-text">What Section 182A(3) Actually Says</h2>
<blockquote><p>"The conditions of payment of surcharge mentioned in sub-section (1), shall not apply to an individual who furnishes an undertaking before the Commissioner by declaring that he shall not purchase, acquire, or otherwise obtain ownership or beneficial interest in any property for a period of six months commencing from the date of furnishing such undertaking in such form as may be prescribed."</p></blockquote>
<p>Five points sit inside that sentence, and each one matters:</p>
<ol>
<li><strong>Only an individual.</strong> An association of persons or a company cannot use it, even a small family firm. Their only route is the surcharge.</li>
<li><strong>It is an undertaking before the Commissioner.</strong> It is a formal declaration on the record, not a formality on a website. Treat it as you would a signed statement.</li>
<li><strong>Three verbs: purchase, acquire, or otherwise obtain.</strong> The law is not limited to buying. Acquiring by other means, and obtaining ownership in any other way, are also covered.</li>
<li><strong>Ownership or beneficial interest.</strong> Property held in someone else's name for your benefit is still caught.</li>
<li><strong>Six months from the date you furnish the undertaking.</strong> Not from the date of the return, and not from the date your name appears on the ATL.</li>
</ol>
<p>The phrase "in such form as may be prescribed" is why the route did not work in practice from 1 July 2026: there was no form. FBR issued draft rules in October 2026 and notified the final rules through SRO 2097(I)/2026 on 10 November 2026, adding Form ATL-U to the Income Tax Rules 2002 under rule 81B.</p>

<h2 id="who-fits">Who Form ATL-U Suits</h2>
<p>The undertaking is built for people whose next six months do not include a property deal. In our experience that is most late filers:</p>
<ul>
<li>Salaried employees who missed the deadline because the salary certificate came late or the deadline simply slipped by.</li>
<li>Pensioners and retired people whose main concern is the tax rate on bank profit and the ability to claim refunds.</li>
<li>Freelancers who need filer status for banking and remittance records rather than for a purchase.</li>
<li>Shopkeepers and sole proprietors who need the ATL for supplier and bank withholding rates.</li>
<li>People who are <em>selling</em> property soon. The undertaking restricts acquiring, not disposing; see our guide on {a(B["sale"], "selling property as a late filer")}.</li>
</ul>

<h2 id="who-not">Who Should Not Sign It</h2>
<ul>
<li>Anyone with a booking, token, file, or sale agreement for a plot, house, flat or shop that will complete within six months.</li>
<li>Anyone expecting to receive property in a way the law could treat as acquiring it, unless the transfer can wait six months.</li>
<li>An AOP or company: the law does not allow it.</li>
<li>Someone who is not sure. If you cannot say with confidence that no property will come to you in six months, the surcharge buys certainty.</li>
</ul>
<p>Our separate guide on {a(B["buy"], "what you cannot buy during the six months")} goes through plots, files, inheritance, gifts, joint ownership and vehicles in detail.</p>

<h2 id="what-saves">What It Saves, and What It Does Not</h2>
<p>Form ATL-U replaces one cost: the Rs 25,000 surcharge for an individual. Everything else about being a late filer stays:</p>
{table(["Item", "Removed by Form ATL-U?", "Why"], [
    ["Rs 25,000 ATL surcharge", "Yes", "Section 182A(3) disapplies the surcharge condition for an individual who gives the undertaking"],
    ["Section 182 late-filing penalty", "No", "It is a separate penalty for missing the due date"],
    ["Tax payable on the return", "No", "The undertaking does not change your income or tax"],
    ["Loss carry-forward for that year", "No", "Section 182A(1)(b) bars it for a late return, whatever the ATL route"],
])}
<p>{PEN_NOTE} That last reduction is worth acting on: a Tax Year 2026 return filed by 30 November 2026 is within one month of the extended due date.</p>

<h2 id="why-matters">Why Getting Back on the ATL Matters So Much</h2>
<p>Rule 1 of the Tenth Schedule increases withholding and collection rates by 100% for people not on the ATL, and some transactions carry their own higher rates. A few examples from the Ordinance amended up to 30 June 2026:</p>
{table(["Transaction", "On the ATL", "Not on the ATL"], [
    ["Profit on a bank deposit (s.151)", "20%", "20% increased by 100%"],
    ["Advance tax when selling immovable property (s.236C)", "2.75%", "11.5%"],
    ["Advance tax when buying immovable property (s.236K)", "1.25%", "10.5% to 18.5%, by value"],
    ["Advance tax on motor vehicle registration (s.231B)", "Normal rate", "Increased by 200%"],
])}
<p>Before 1 July 2026, rule 1A of the Tenth Schedule charged separate, higher rates to people on the ATL who had filed late. The Finance Act 2026 omitted rule 1A, so once you are on the ATL you are charged the ordinary filer rates. That is what makes the ATL route, whichever one you use, worth completing.</p>

<h2 id="process">How the Process Runs</h2>
<ol>
<li><strong>File the Tax Year 2026 return and wealth statement on IRIS.</strong> The undertaking is not a substitute for the return; it follows it.</li>
<li><strong>Pay any tax due</strong> on the return, and the Section 182 penalty if it is charged.</li>
<li><strong>Furnish Form ATL-U on IRIS.</strong> The form asks for your identity details, the tax year, the return filing details and the declaration. Our step-by-step guide covers {a(B["iris"], "the IRIS screens")}.</li>
<li><strong>Save the acknowledgement.</strong> The date on it is the start of your six months.</li>
<li><strong>Check the ATL</strong> after FBR's next update, using the {a(X["chk"], "online or SMS status check")}.</li>
</ol>

<h2 id="breach">If the Undertaking Is Broken</h2>
<p>As notified, the rules allow FBR to check property transactions against information from registries and other sources. If a breach is established after you are given a chance to explain, the benefit is withdrawn from the date of the breach and your ATL position is decided under the ordinary rules, which means the surcharge. In practice the cost of a breach is losing exactly what you saved, at the worst moment: in the middle of a property transaction where the higher non-ATL rates apply.</p>

<h2 id="mistakes">Five Mistakes We See</h2>
<ol>
<li>Furnishing the undertaking before the return is filed, then forgetting the return.</li>
<li>Counting six months from the return date instead of the undertaking date.</li>
<li>Assuming the late-filing penalty has gone too.</li>
<li>Signing while a spouse or family member is buying property that is partly funded by, or held for, the filer.</li>
<li>Using the route for an AOP or company.</li>
</ol>
""",
    faqs=[
        ("What is Form ATL-U?", "It is the form for the undertaking under Section 182A(3) of the Income Tax Ordinance, prescribed by SRO 2097(I)/2026. An individual who filed late declares that he will not obtain any property for six months and, in return, the ATL surcharge condition does not apply."),
        ("Is there any fee to FBR for Form ATL-U?", "No payment to FBR is required for the undertaking. Our professional fee for preparing and furnishing it is Rs 2,000, added to the return fee."),
        ("Can a company or AOP use Form ATL-U?", "No. Section 182A(3) applies only to an individual. A company pays Rs 100,000 and an AOP Rs 50,000 to be included in the ATL after a late return."),
        ("Does Form ATL-U remove the late-filing penalty?", "No. The Section 182 penalty for filing after the due date is separate. Filing within one month of the due date reduces it by 75% under the current text."),
        ("When do the six months start?", "From the date you furnish the undertaking. Keep the IRIS acknowledgement, which shows that date."),
        ("Can I sell property after signing Form ATL-U?", "The undertaking is about purchasing, acquiring or obtaining ownership or beneficial interest. Selling is not mentioned, and being on the ATL means the lower 2.75% rate under Section 236C."),
        ("What happens if I buy property within six months?", "As notified, the benefit is withdrawn from the date of breach after you are heard, and the ordinary rule applies: the surcharge must be paid to stay on the ATL."),
        ("Do I still need to file the return?", "Yes. The undertaking is for a person who files the return after the due date. It is not a substitute for the return."),
    ],
    sources=[S_ITO, S_SRO, S_ATL, S_IRIS],
    related=[(X["cmp"], "Surcharge vs Form ATL-U"), (B["iris"], "Submit Form ATL-U on IRIS"), (B["buy"], "What You Cannot Buy for 6 Months")],
    cta_h="Back on the ATL Without Paying Rs 25,000",
    cta_p="We file your late return, furnish Form ATL-U and track your ATL status.",
    wa_text="Assalam o Alaikum, maine 2026 ki return late file karni hai / ki hai. Form ATL-U ke zariye ATL mein aana hai.",
)

# ───────────────────────────── 2. IRIS step by step ─────────────────────────────
IRIS = dict(
    slug=SL["iris"],
    svc=dict(h2="We Submit Form ATL-U on IRIS for You", intro="IRIS is unforgiving: a wrong tax year or a missing acknowledgement number can mean the undertaking is not linked to your return. We check your IRIS profile, file the return if it is still pending, furnish Form ATL-U and send you the acknowledgement.",
             hook="Want Form ATL-U done today?", fee=F_ONLY, btn="Submit my Form ATL-U",
             items=["IRIS login recovery if your password or registered mobile has changed",
                    "A check that the Tax Year 2026 return is filed and its acknowledgement number is correct",
                    "Form ATL-U filled with your CNIC, tax year and return details, verified before submission",
                    "The acknowledgement PDF sent to you with the date your six months end",
                    "ATL status check after FBR's next update"],
             risks=["Selecting the wrong tax year links the undertaking to the wrong return",
                    "Submitting before the return is filed leaves nothing for the undertaking to attach to",
                    "Losing the acknowledgement makes it hard to prove the start date later"]),
    title="How to Submit Form ATL-U on IRIS: Step by Step (2026)",
    h1="How to Submit Form ATL-U on IRIS: A Step-by-Step Guide for Late Filers (2026)",
    crumb="Submit Form ATL-U on IRIS",
    description="Step-by-step: submitting Form ATL-U on FBR IRIS after a late 2026 return. What to prepare, each field, the acknowledgement and checking your ATL status.",
    keywords="how to submit form atl u, form atl u iris, atl-u iris steps, atl undertaking online, form atl u kaise submit karein, iris atl-u",
    category="Form ATL-U", icon="🖥️", read="12 min read",
    banner="Form ATL-U is furnished electronically on IRIS. Here is what to prepare, the order to do things in, and how to confirm it worked.",
    tldr=("Form ATL-U is furnished on FBR's IRIS portal after the late return has been filed. Prepare four things first: working IRIS login, the filed Tax Year 2026 return, "
          "its IRIS acknowledgement number and filing date, and certainty that you will not obtain any property for six months. The form, prescribed by SRO 2097(I)/2026 under "
          "rule 81B of the Income Tax Rules 2002, records your name, CNIC or NTN, tax year, return filing date, return acknowledgement number and the declaration. Once submitted, "
          "IRIS issues an acknowledgement; its date starts the six-month period under Section 182A(3). Your name should then appear on the ATL after FBR's next update."),
    lead=("Most people who come to us about Form ATL-U have already understood the idea. What they want is the practical sequence: what to open, what to fill, and how to know it worked. "
          "This guide follows that order, and flags the points where people go wrong."),
    body=f"""
{SERIES}

<h2 id="before">Before You Open IRIS: A Five-Point Check</h2>
<p>Do not start the form until each of these is true. Each one has stopped a client at some point.</p>
{table(["Check", "Why it matters", "How to confirm"], [
    ["You are an individual", "Section 182A(3) is limited to individuals", "Your IRIS registration type is Individual"],
    ["The Tax Year 2026 return is filed", "The undertaking relates to a return filed after the due date", "IRIS shows the return as Completed with an acknowledgement"],
    ["You have the return acknowledgement number and filing date", "The form asks for them", "Open the filed return or the acknowledgement PDF"],
    ["No property purchase, booking or transfer to you in the next six months", "That is the undertaking", "Ask yourself, and your family, honestly"],
    ["Mobile and email on IRIS are current", "Verification codes and notices go there", "Profile section on IRIS"],
])}

<h2 id="login">Step 1: Get Into IRIS</h2>
<p>Go to {a("https://iris.fbr.gov.pk/", "iris.fbr.gov.pk")} and log in with your CNIC and password. If the password is lost, use the reset option; the code goes to the mobile number and email registered with FBR. If you no longer have that number, the registered contact details must be changed first, which FBR handles through its own procedure, so allow time for it.</p>

<h2 id="return">Step 2: Make Sure the Late Return Is Complete</h2>
<p>Open the list of completed tasks and find the return for Tax Year 2026. Three things to verify:</p>
<ul>
<li>The status is Completed, not Draft. A draft is not a filed return.</li>
<li>The wealth statement for Tax Year 2026 has also been filed. A return without its wealth statement is an incomplete filing for an individual who must file one.</li>
<li>Any tax shown as payable on the return has been paid through a challan (PSID) and the payment reference is entered.</li>
</ul>
<p>If the return is still pending, file it first. Our {a(X["salr"], "salaried return guide")} and {a(X["free"], "freelancer return guide")} cover the return itself.</p>

<h2 id="form">Step 3: Open Form ATL-U</h2>
<p>FBR has added Form ATL-U to IRIS as an electronic form verified the same way as other IRIS submissions. Its exact menu location may change as FBR updates the portal, so if you cannot see it, use the IRIS search or the declaration/forms area rather than guessing. Do not use any paper or emailed version: the law requires the undertaking in the prescribed form, and IRIS is where it is furnished.</p>

<h2 id="fields">Step 4: Fill the Fields</h2>
{table(["Field", "What to enter", "Common mistake"], [
    ["Name", "Exactly as on your CNIC and IRIS profile", "A nickname or a different spelling"],
    ["CNIC / NTN", "Your 13-digit CNIC (for individuals this is the NTN)", "Entering a family member's CNIC"],
    ["Tax year", "2026 for the return due on 31 October 2026", "Selecting 2027, the current tax year"],
    ["Date of filing the return", "The date on the return acknowledgement", "The date you started the draft"],
    ["Return acknowledgement / reference number", "From the filed return", "The PSID of the tax payment instead"],
    ["Declaration", "Read it fully before confirming", "Ticking without reading the property clause"],
])}
<p>The declaration is the heart of the form. It records that you will not purchase, acquire or otherwise obtain ownership or beneficial interest in any property for six months from the date of the undertaking, and that you understand the benefit depends on keeping that promise.</p>

<h2 id="verify">Step 5: Verify and Submit</h2>
<p>IRIS asks for verification before submission, usually with your PIN or a code sent to your registered mobile and email. Submit only after re-reading the tax year and the return details: once furnished, the undertaking is on the record.</p>

<h2 id="ack">Step 6: Download and Keep the Acknowledgement</h2>
<p>IRIS issues an electronic acknowledgement. Download the PDF and keep it with your return acknowledgement. It is your proof of three things:</p>
<ul>
<li>That the undertaking was furnished, if your ATL status is ever questioned by a bank or registrar.</li>
<li>The date the six months began.</li>
<li>The date the six months end, which is when you can safely book or buy property again.</li>
</ul>
<p>Write the end date somewhere you will see it. People forget, and the most common breach we see is innocent: a plot booking in month five.</p>

<h2 id="atl-check">Step 7: Confirm Your ATL Status</h2>
<p>The ATL is updated periodically, not the minute you submit. After the next update, check your status online or by SMS, as explained in our {a(X["chk"], "ATL status check guide")}. If your name does not appear after an update, the usual reasons are:</p>
<ul>
<li>The return is not in Completed status, or the wealth statement is missing.</li>
<li>The undertaking was furnished against the wrong tax year.</li>
<li>The form was saved but not submitted.</li>
</ul>

<h2 id="timeline">A Realistic Timeline</h2>
{table(["Day", "What happens"], [
    ["Day 1", "Documents collected, return and wealth statement prepared"],
    ["Day 1-2", "Return filed on IRIS, tax paid, acknowledgement saved"],
    ["Day 2", "Form ATL-U furnished, acknowledgement saved, six-month end date noted"],
    ["After FBR's next ATL update", "Status checked online or by SMS"],
])}
<p>File sooner rather than later. Under the current text of Section 182, the late-filing penalty is reduced by 75% if the return is filed within one month after the due date, 50% within two months and 25% within three. For Tax Year 2026, one month after 31 October 2026 is 30 November 2026.</p>

<h2 id="if-not-showing">If Form ATL-U Is Not Visible on Your IRIS</h2>
<p>New forms are sometimes rolled out in stages. If the form is not visible, do not pay the surcharge in a panic unless you need ATL status for a transaction this week. File the return, keep it complete, and check again, or ask us to check the account. If you do need filer status immediately, for example for a property sale next week, paying the surcharge may be the faster route; our {a(X["cmp"], "comparison guide")} helps with that call.</p>
""",
    faqs=[
        ("Where is Form ATL-U on IRIS?", "It is an electronic form on IRIS. FBR can move menu items, so if you cannot find it, use the IRIS search or forms area, or ask us to check your account."),
        ("Can I submit Form ATL-U before filing my return?", "It relates to a return filed after the due date, and it asks for the return's filing date and acknowledgement number. File the return first."),
        ("Which tax year do I select?", "Tax Year 2026 for the return that was due on 31 October 2026."),
        ("Is there a challan or fee on IRIS for Form ATL-U?", "No payment is made to FBR for the undertaking. The Rs 25,000 surcharge is what the undertaking replaces."),
        ("How long until my name appears on the ATL?", "After FBR's next ATL update. Check online or by SMS after the update."),
        ("I lost the acknowledgement. Can I download it again?", "Yes, completed submissions remain in your IRIS account; download the acknowledgement again and keep a copy."),
        ("Can someone else submit Form ATL-U for me?", "A tax practitioner can prepare and submit it through your IRIS account with your authorisation. The undertaking remains yours, so read the declaration yourself."),
        ("What if I selected the wrong tax year?", "Contact us or your tax office promptly. An undertaking against the wrong year does not help with the late Tax Year 2026 return."),
    ],
    sources=[S_ITO, S_SRO, S_IRIS, S_ATL],
    related=[(B["guide"], "Form ATL-U Complete Guide"), (X["chk"], "Check ATL Status Online"), (B["fee"], "Filer Fee 2026")],
    cta_h="Form ATL-U Submitted Correctly, First Time",
    cta_p="We check your return, furnish the undertaking and send you the acknowledgement.",
    wa_text="Assalam o Alaikum, mujhe IRIS par Form ATL-U submit karwana hai.",
)

# ───────────────────────────── 3. Active late filer ─────────────────────────────
ALF = dict(
    slug=SL["alf"],
    svc=dict(h2="Turn \"Late\" or \"Inactive\" Into Active", intro="Whatever your status shows, the fix starts with the missing or late return. We look at your IRIS record, file what is outstanding, choose the right ATL route and confirm the status once FBR updates the list.",
             hook="ATL shows inactive or late for you?", fee=F_ALL, btn="Make me an active filer",
             items=["A reading of your IRIS record: which years are filed, late or missing",
                    "The Tax Year 2026 return and wealth statement filed",
                    "Form ATL-U, if you are not buying property in the next six months, or the surcharge if you are",
                    "A status check after the next ATL update",
                    "A reminder before 30 September 2027 so next year's return is on time"],
             risks=["Reading the status wrongly and paying the surcharge when the undertaking would have worked",
                    "Filing the return without the wealth statement, which keeps problems open",
                    "Leaving the status as is and paying double withholding for months"]),
    title="Active Late Filer Meaning 2026: Status, Rates, Form ATL-U",
    h1="Active Late Filer, Inactive Filer and ATL Status in 2026: What They Mean and How Form ATL-U Changes the Picture",
    crumb="Active Late Filer Meaning",
    description="What 'active late filer' and 'inactive filer' mean on the FBR ATL in 2026, why the old late-filer rates ended, and how Form ATL-U gets you active again.",
    keywords="active late filer means, atl status active late filer, active late filer tax rate, inactive filer fbr, how to become active filer from inactive, how to become active filer from late filer",
    category="Form ATL-U", icon="🔎", read="12 min read",
    banner="Checked your status and saw a word you did not expect? Here is what the ATL status terms mean in 2026 and what to do about each one.",
    tldr=("The Active Taxpayers List (ATL) shows whether you have filed the return that the list relates to. 'Active' means you are on it; 'inactive' generally means FBR does not "
          "have a return from you for that year, so you are not on the list. The term 'active late filer' came from rule 1A of the Tenth Schedule, which from 1 July 2024 charged "
          "higher withholding rates to people on the ATL who had filed after the due date. The Finance Act 2026 omitted rule 1A, so from 1 July 2026 there is no separate rate for "
          "late filers who are on the ATL. A late filer reaches the ATL either by paying the Section 182A surcharge (Rs 25,000 for an individual) or, as an individual, by furnishing "
          "Form ATL-U and not obtaining property for six months."),
    lead=("Searches for 'active late filer meaning' jump every year after the deadline, because people see the phrase on a bank form or a status check and assume it is a penalty. "
          "The phrase has a history, and in 2026 its meaning changed. Here is the plain explanation, with the law behind it."),
    body=f"""
{SERIES}

<h2 id="terms">The Status Terms in Plain Words</h2>
{table(["Status you see", "What it means", "What to do"], [
    ["Active", "Your name is on the current ATL", "Nothing, except file next year's return on time"],
    ["Inactive / not found", "FBR does not have a return from you for the year the list relates to, or you filed late and have not completed an ATL route", "File the missing return, then use the surcharge or Form ATL-U"],
    ["Active late filer (bank or registrar wording)", "On the ATL, but the return was filed after the due date", "Since 1 July 2026, no separate rate applies; check the bank applied ordinary filer rates"],
])}
<p>Different banks and registrars use slightly different words on their own screens. The legal question is always the same: is the person "appearing in the active taxpayers' list"? That is the phrase the Tenth Schedule uses.</p>

<h2 id="history">Where "Active Late Filer" Came From</h2>
<p>From 1 July 2024, the Finance Act 2024 inserted rule 1A into the Tenth Schedule. It applied to "persons appearing on the active taxpayers' list who have not filed the return by the due date" and gave them their own rates for certain transactions, most visibly advance tax under Section 236C on selling property, which was higher than the ordinary filer rate. Banks and property dealers started calling these people "active late filers", and the term stuck.</p>
<p>The Finance Act 2026 omitted rule 1A. In the Ordinance amended up to 30 June 2026, the rule appears only in a footnote recording what was omitted. The practical result from 1 July 2026:</p>
<ul>
<li>If you are on the ATL, you are charged the ordinary filer rates, whether you filed on time or late.</li>
<li>If you are not on the ATL, rule 1 of the Tenth Schedule applies: rates increased by 100%, and higher specific rates on some transactions.</li>
</ul>
<p>So in 2026 the question that matters is no longer "on time or late", it is "on the ATL or not".</p>

<h2 id="late-not-on">Late Filer Not Yet on the ATL</h2>
<p>Section 182A(1)(a) keeps a late filer off the ATL for the year of the late return unless the proviso is satisfied: payment of Rs 25,000 for an individual, Rs 50,000 for an AOP, or Rs 100,000 for a company. Section 182A(3) adds a second door for individuals only: the undertaking in Form ATL-U not to obtain ownership or beneficial interest in any property for six months.</p>
<p>Until one of those is done, three more consequences apply under Section 182A(1): no refund is issued while you are not on the ATL, the period does not count for additional payment on delayed refunds, and a loss for the late year cannot be carried forward.</p>

<h2 id="cost">What Staying Inactive Costs</h2>
{table(["Transaction", "On the ATL", "Not on the ATL"], [
    ["Bank profit (s.151)", "20%", "Increased by 100% under Tenth Schedule rule 1"],
    ["Selling immovable property (s.236C)", "2.75%", "11.5%"],
    ["Buying immovable property (s.236K)", "1.25%", "10.5% up to Rs 50m, 14.5% up to Rs 100m, 18.5% above"],
    ["Motor vehicle registration (s.231B)", "Normal rate", "Increased by 200%"],
    ["Other withholding taxes covered by rule 1", "Normal rate", "Increased by 100%"],
])}
<p>For someone with Rs 2 million in a savings account earning 10% a year, the profit is Rs 200,000. At the filer rate the bank deducts Rs 40,000; at the doubled rate it deducts Rs 80,000. The Rs 40,000 difference alone is more than the surcharge, and Form ATL-U removes it without the surcharge.</p>

<h2 id="become-active">How to Become Active From Inactive</h2>
<ol>
<li><strong>Find out which year is missing.</strong> The ATL relates to a specific tax year; for the list issued in 2027 that is Tax Year 2026.</li>
<li><strong>File that return and the wealth statement.</strong> If earlier years are also missing, discuss them before filing so that the wealth statements reconcile.</li>
<li><strong>Choose the ATL route.</strong> No property purchase planned for six months: Form ATL-U. A purchase planned: the surcharge.</li>
<li><strong>Wait for the next ATL update and check.</strong> Use the {a(X["chk"], "online or SMS check")}.</li>
</ol>

<h2 id="choose">Choosing the Route in Ten Seconds</h2>
{table(["Your next six months", "Best route"], [
    ["No property purchase, booking or transfer to you", "Form ATL-U"],
    ["Selling property only", "Form ATL-U usually fits; selling is not restricted"],
    ["Buying a plot, house, flat or shop", "Pay the surcharge"],
    ["You run the business as an AOP or company", "Surcharge (Form ATL-U is for individuals only)"],
    ["Not sure", "Talk it through before signing anything"],
])}

<h2 id="penalty">The Late-Filing Penalty Is a Separate Question</h2>
<p>Becoming active does not settle the Section 182 penalty. {PEN_NOTE} The one-month reduction is the reason to file now: a Tax Year 2026 return filed by 30 November 2026 qualifies.</p>

<h2 id="next-year">Staying Active Next Year</h2>
<p>The Tax Year 2027 return is due on 30 September 2027 under Section 118, unless extended. File on time and none of this applies: no surcharge, no undertaking, no penalty. Salaried people can usually file in July or August as soon as the employer's certificate is ready.</p>
""",
    faqs=[
        ("What does active late filer mean?", "It describes a person on the ATL who filed the return after the due date. Rule 1A of the Tenth Schedule used to charge such people higher rates; the Finance Act 2026 omitted it, so from 1 July 2026 they pay ordinary filer rates."),
        ("What does inactive filer mean?", "Your name is not on the current ATL, usually because the return for the relevant year is missing or was filed late without the surcharge or Form ATL-U."),
        ("How do I become active from inactive?", "File the missing return and wealth statement, then either pay the surcharge or, as an individual not obtaining property for six months, furnish Form ATL-U."),
        ("Do active late filers still pay higher tax on property?", "Not from 1 July 2026. The separate rates in rule 1A were omitted by the Finance Act 2026; a person on the ATL pays 2.75% under Section 236C when selling."),
        ("Is the late-filing penalty removed once I am active?", "No. The Section 182 penalty is separate from ATL status."),
        ("Can a bank still deduct the higher rate after I become active?", "Banks apply the rate according to the ATL on the date of the transaction. After your name appears, ask the bank to apply the filer rate going forward."),
        ("How long does Form ATL-U keep me active?", "Your ATL inclusion relates to the tax year. The six-month promise is the condition; breaking it brings back the surcharge rule."),
        ("Which return decides my status in 2027?", "The ATL issued in 2027 relates to Tax Year 2026, the return that was due on 31 October 2026."),
    ],
    sources=[S_ITO, S_ATL, S_SRO, S_IRIS],
    related=[(B["guide"], "Form ATL-U Complete Guide"), (X["chk"], "Check ATL Status"), (B["bank"], "Late Filer Tax on Bank Profit")],
    cta_h="Become an Active Filer Again",
    cta_p="We file the missing return and put you back on the ATL by the cheapest route that fits.",
    wa_text="Assalam o Alaikum, mera ATL status inactive / late filer dikha raha hai. Active filer banna hai.",
)
