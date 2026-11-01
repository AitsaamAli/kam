"""Content for three posts on the passed 31 October 2026 return deadline (facts checked 1 November 2026)."""

WA = "https://wa.me/923284675162"

SRC_DAWN_EXT = ("Dawn: FBR extends deadline for filing income tax returns to Oct 31 (15 October 2026)", "https://www.dawn.com/news/2037394")
SRC_PROFIT_EXT = ("Profit: FBR extends tax return filing deadline to October 31, 2026", "https://profit.pakistantoday.com.pk/2026/10/15/fbr-extends-income-tax-return-filing-deadline-to-october-31-2")
SRC_FBR_182 = ("FBR: Income Tax Ordinance 2001, Section 182 (offences and penalties)", "https://www.fbr.gov.pk/section-182/152727")
SRC_BR_ATLU = ("Business Recorder: FBR waives surcharge for late filers pledging no property purchase (7 October 2026)", "https://www.brecorder.com/news/40443041/fbr-waives-surcharge-for-late-filers-pledging-no-property-purchase")
SRC_DAWN_ATLU = ("Dawn: FBR allows late returns without surcharge (7 October 2026)", "https://www.dawn.com/news/2035295")
SRC_PP_BAR = ("ProPakistani: Tax lawyers urge FBR to cancel Rs 25,000 surcharge on late filers", "https://propakistani.pk/2026/07/03/tax-lawyers-urge-fbr-to-cancel-rs-25000-surcharge-on-late-filers/")
SRC_FBR_ATL = ("FBR: Active Taxpayer List (Income Tax)", "https://www.fbr.gov.pk/categ/active-taxpayer-list-income-tax/51147/30859/71168")
SRC_IRIS = ("FBR IRIS portal", "https://iris.fbr.gov.pk/")

L = {  # internal links (tax site only)
    "main": "/blogs/income-tax-return-deadline-pakistan-2026",
    "penalty": "/blogs/late-filing-penalty-income-tax-pakistan",
    "surcharge": "/blogs/atl-surcharge-2026-pakistan",
    "n114": "/blogs/section-114-notice-lahore-response-guide",
    "wht": "/blogs/wht-rate-filer-non-filer-pakistan",
    "revised": "/blogs/revised-tax-return-kab-kaise-file-karein-pakistan-2026",
    "atlcheck": "/blogs/check-filer-status-atl-online-pakistan",
    "notice": "/blogs/fbr-notice-received-what-to-do-pakistan",
    "filing": "/income-tax-filing",
    "pricing": "/pricing",
    "defense": "/fbr-notice-defense",
}
A_SLUG = "tax-return-deadline-passed-31-october-2026-next-steps"
B_SLUG = "late-filer-atl-surcharge-or-form-atl-u-undertaking-2026"
C_SLUG = "tax-return-last-date-guzar-gayi-ab-kya-karein-2026"


def a(href, text):
    return f'<a href="{href}" style="color:#0D9488;font-weight:600;text-decoration:underline">{text}</a>'


def table(head, rows):
    h = "".join(f"<th>{x}</th>" for x in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div style="overflow-x:auto;-webkit-overflow-scrolling:touch"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


# ─────────────────────────────── POST A ───────────────────────────────
POST_A = dict(
    slug=A_SLUG,
    title="Tax Return Deadline Passed (31 Oct 2026): What to Do Now",
    h1="The 31 October 2026 Tax Return Deadline Has Passed: Your Next Steps",
    crumb="31 October Deadline Passed",
    description="The Tax Year 2026 return deadline closed on 31 October 2026. What a late return costs under Section 182, how to rejoin the ATL, and a 7-day filing plan.",
    keywords="tax return deadline passed 31 October 2026, file tax return after 31 October 2026, late tax return Pakistan 2026, FBR late filing penalty section 182",
    category="Deadline Passed — Tax Year 2026",
    icon="⏰",
    read="12 min read",
    banner="The extended deadline for Tax Year 2026 returns closed at the end of 31 October 2026. You can still file, and the sooner you file, the less a late return costs.",
    tldr=("FBR's extended deadline for Tax Year 2026 income tax returns ended on 31 October 2026. As of 1 November 2026 FBR had not announced another extension. "
          "You can still file through IRIS, but the return now counts as late. That has three practical effects: a Section 182 penalty can be imposed, "
          "you stay off the Active Taxpayers List (ATL) until you pay the Section 182A surcharge (Rs 25,000 for individuals), and non-filer withholding rates "
          "apply to you in the meantime. Filing quickly limits all three."),
    lead=("For most individuals and associations of persons, the last date to file the Tax Year 2026 income tax return was 31 October 2026. "
          "FBR had already moved it twice, from 30 September to 15 October and then to 31 October. If your return is still not filed, this guide explains "
          "exactly where you stand from 1 November, what filing late will cost in rupees, and the order in which to fix it."),
    body=f"""
<p class="tf-primary"><strong>Main guide:</strong> for dates, forms and who must file, see our {a(L['main'], 'income tax return deadline guide for 2026')}.</p>

<h2 id="what-closed">What Closed on 31 October 2026</h2>
<p>On 15 October 2026 FBR used its power under Section 214A of the Income Tax Ordinance, 2001 to extend the filing date to 31 October 2026. The notification covered persons whose returns were due on 30 September 2026 and whose date had already been moved to 15 October. In practice, that means salaried individuals, business individuals, freelancers, landlords and AOPs filing for Tax Year 2026 (the year from 1 July 2025 to 30 June 2026).</p>
<p>FBR gave two reasons: requests from trade bodies and tax bar associations, and a filing season slowed by new return forms, extra disclosures, wealth statement reconciliation and IRIS problems. Interest was high. Dawn reported 6.71 million returns filed by 14 October, against 4.99 million at the same point a year earlier.</p>
<p>Companies with a 30 June year-end are not part of this deadline. Their return is normally due by 31 December, so this guide does not apply to them.</p>

<h2 id="still-file">Can You Still File After 31 October?</h2>
<p>Yes. IRIS keeps accepting Tax Year 2026 returns after the due date. A late return is still a valid return: it records your income, the tax already deducted from you, and your wealth statement. What changes is the status attached to it. Your return is now a late return, and three consequences follow.</p>
<p>Two common hopes no longer help. An extension application under Section 119 has to reach the Commissioner before the due date, so it cannot rescue a return that is already late. And waiting for a backdated general extension is a gamble. FBR has not announced one, and every day you wait adds to the penalty formula below.</p>

<h2 id="what-changes">What Changes for You From 1 November</h2>
{table(["Consequence", "What it means", "How to limit it"], [
    ["Section 182 penalty", "A penalty for filing after the due date can be imposed by order. It is calculated per day of delay, with a minimum amount.", "File as early as possible. Every day counts in the formula."],
    ["Off the Active Taxpayers List", "Under Section 182A, a late filer is not placed on the ATL just by filing. A surcharge must be paid first.", "Pay the surcharge (Rs 25,000 for individuals) or use the Form ATL-U undertaking route if it is available in IRIS."],
    ["Non-filer withholding rates", "While you are off the ATL, banks, property registrars and vehicle registration authorities can deduct tax at non-filer rates.", "Get back on the ATL before any large transaction."],
    ["Notices", "Persons who do not file can receive a Section 114(4) notice. If that is ignored, an assessment can be made on the information FBR holds.", "File before a notice arrives, and never ignore one that does."],
])}

<h2 id="penalty">How the Section 182 Penalty Is Worked Out</h2>
<p>The penalty for not filing by the due date appears as entry 1 of the table in Section 182. As published on FBR's website (checked 1 November 2026), it works like this:</p>
<ul>
<li><strong>Daily rate:</strong> 0.1% of the tax payable for that tax year, for each day of default.</li>
<li><strong>Ceiling:</strong> no more than 50% of the tax payable.</li>
<li><strong>Floor:</strong> if the figure works out below Rs 40,000, or no tax is payable at all, the penalty is Rs 40,000.</li>
<li><strong>Salaried relief:</strong> if at least 75% of your income is from salary and that salary income is below Rs 5 million, the minimum is Rs 5,000 instead of Rs 40,000.</li>
</ul>
<p>"Tax payable" here means the tax chargeable on your taxable income for the year. It is not just the balance left after deductions. A salaried person whose employer deducted every rupee still has tax payable for this calculation.</p>
<p>The worked examples below count days from 1 November 2026. The tax figures are illustrations, not real cases.</p>
{table(["Profile", "Tax payable (TY2026)", "Filed on", "Days late", "0.1% × days", "Penalty under the formula"], [
    ["Salaried, salary Rs 3 million, no other income", "Rs 180,000", "30 Nov 2026", "30", "Rs 5,400", "Rs 5,400 (above the Rs 5,000 floor)"],
    ["Same salaried person, waits longer", "Rs 180,000", "31 Jan 2027", "92", "Rs 16,560", "Rs 16,560"],
    ["Shopkeeper", "Rs 150,000", "30 Nov 2026", "30", "Rs 4,500", "Rs 40,000 (floor applies)"],
    ["Freelancer or consultant", "Rs 900,000", "31 Jan 2027", "92", "Rs 82,800", "Rs 82,800 (below the 50% ceiling)"],
    ["Business individual with a loss year", "Nil", "Any date", "—", "—", "Rs 40,000"],
])}
<p>Two points matter more than the arithmetic. First, the penalty is imposed by an order of the tax officer, normally after a notice that gives you a chance to explain. It is not a fee IRIS adds when you press submit. If you had a genuine, documented reason for the delay, that reply is where it belongs, and an order you disagree with can be appealed to the Commissioner (Appeals). Second, the business floor of Rs 40,000 means that for small businesses, a few days of delay already costs as much as several months. Do not let the penalty become an excuse to keep waiting.</p>
<p>For a longer treatment of penalty rules across returns, statements and notices, read our {a(L['penalty'], 'guide to late filing penalties')}.</p>

<h2 id="atl">Getting Back on the Active Taxpayers List</h2>
<p>For most people, ATL status matters more than the penalty, because it sets the tax rate on bank cash withdrawals, property transfers and vehicle registration. Section 182A, as amended by the Finance Act 2026, keeps late filers off the ATL until they pay a surcharge:</p>
{table(["Taxpayer", "Surcharge to join the ATL after the due date", "Before 1 July 2026"], [
    ["Individual", "Rs 25,000", "Rs 1,000"],
    ["Association of persons", "Rs 50,000", "Rs 10,000"],
    ["Company", "Rs 100,000", "Rs 20,000"],
])}
<p>For individuals there may be a second route. On 6 October 2026 FBR published draft rules for a Form ATL-U undertaking: you skip the surcharge and in return promise not to acquire any property for six months. At the time of writing, the reports we found describe this as a draft. Check IRIS when you file. We compare both routes in detail in {a('/blogs/' + B_SLUG, 'our guide to the ATL surcharge and Form ATL-U')}.</p>
<p>The surcharge and the Section 182 penalty are separate. Paying one does not settle the other.</p>

<h2 id="seven-day-plan">A 7-Day Plan to File Your Late Return Properly</h2>
<ol>
<li><strong>Day 1. Check your position.</strong> Log in to IRIS. Confirm whether a Tax Year 2026 return is saved as a draft or not started, and note any notices in your inbox. Check your current ATL status.</li>
<li><strong>Day 1–2. Collect documents.</strong> Salaried: salary certificate or the employer's annual tax deduction statement. Everyone: bank statements and withholding certificates for 1 July 2025 to 30 June 2026. Business: sales, purchase and expense records. Freelancers: remittance records.</li>
<li><strong>Day 2–3. Rebuild the wealth statement.</strong> Start from last year's closing figures. Add assets bought and money received, subtract spending, and make sure the reconciliation balances. Most rushed returns go wrong here.</li>
<li><strong>Day 3–4. Pay any balance tax first.</strong> If your return shows tax still payable, pay it through a payment slip (PSID) before submitting, so the return is not filed with an unpaid demand.</li>
<li><strong>Day 4–5. Review and submit.</strong> Check every figure against the documents, submit the return and wealth statement together, and save the acknowledgement.</li>
<li><strong>Day 5–6. Decide the ATL route.</strong> Pay the Section 182A surcharge, or use the undertaking if it is available and fits your plans.</li>
<li><strong>Day 7. Confirm.</strong> Check that your ATL status has updated before you rely on it for a transaction. Keep copies of everything in case a penalty notice arrives later.</li>
</ol>

<h2 id="mistakes">Mistakes That Make a Late Return Worse</h2>
<ul>
<li><strong>Filing a "quick" return with a guessed wealth statement.</strong> A rushed reconciliation is one of the most common reasons for later notices. Revising it later is possible, but it is slower than doing it right the first time (see {a(L['revised'], 'how revised returns work')}).</li>
<li><strong>Leaving out income to keep the tax low.</strong> FBR matches returns against bank, property and withholding data. Understating income turns a late-filing problem into a concealment problem.</li>
<li><strong>Ignoring a Section 114(4) notice.</strong> Once a notice arrives, the response has a deadline of its own. Our {a(L['n114'], 'Section 114 notice guide')} explains how to answer one.</li>
<li><strong>Assuming the surcharge cancels the penalty.</strong> It does not. They are two different provisions with two different purposes.</li>
<li><strong>Waiting for a large transaction to force the issue.</strong> Discovering at the property registrar that you are off the ATL costs far more than the surcharge.</li>
</ul>

<h2 id="previous-years">If You Also Missed Earlier Years</h2>
<p>Some people find, while filing Tax Year 2026, that Tax Year 2025 or earlier returns were never filed either. Each missing year is a separate return with its own penalty position. The wealth statements also have to connect year to year. File the oldest missing year first, so each closing wealth figure becomes the next year's opening figure. Filing only the latest year with an opening position that FBR cannot trace is how notices start.</p>

<h2 id="how-we-help">How Kamboh Associates Files Late Returns</h2>
<p>Late returns are a large part of our work every November. We work entirely over WhatsApp, or at our office in Awan Town, Lahore:</p>
<ul>
<li>We review your IRIS profile and documents and tell you within one working day what is missing.</li>
<li>We prepare the return and a wealth statement that reconciles, and share the figures with you for approval before filing.</li>
<li>We file through IRIS and guide you through the ATL surcharge or undertaking.</li>
<li>If a Section 182 penalty notice or a Section 114 notice arrives later, we draft the reply.</li>
</ul>
<p>Our fees are the same published fees as for on-time returns: salaried returns from Rs 3,500, freelancer and sole proprietor returns from Rs 5,000, AOP returns from Rs 8,000, and overseas Pakistani returns from Rs 6,000. Penalties and surcharges are paid to FBR, not to us. See the full {a(L['pricing'], 'pricing page')} or our {a(L['filing'], 'income tax return filing service')}.</p>

<div class="highlight-box"><p><strong>Missed 31 October?</strong> Send your CNIC and documents on WhatsApp to <strong><a href="{WA}" style="color:#14B8A6;font-weight:600">0328-4675162</a></strong>. We will tell you what your late return involves before you pay anything.</p></div>
""",
    faqs=[
        ("Was the Tax Year 2026 return deadline extended beyond 31 October 2026?",
         "As of 1 November 2026, FBR had not announced any extension beyond 31 October 2026. The date had already been moved twice: from 30 September to 15 October, and then to 31 October under Section 214A. Check FBR's official website or X account for any later notification."),
        ("Can I still file my income tax return in November 2026?",
         "Yes. IRIS accepts Tax Year 2026 returns after the due date. The return is treated as late, so a Section 182 penalty can be imposed, and you join the Active Taxpayers List only after paying the Section 182A surcharge or using the undertaking route if available."),
        ("What is the minimum late filing penalty for a salaried person?",
         "Under Section 182 as published by FBR, the minimum is Rs 5,000 if at least 75% of your income is from salary and that salary income is below Rs 5 million. Otherwise the minimum is Rs 40,000. Above the minimum, the penalty is 0.1% of tax payable per day of delay, capped at 50% of the tax payable."),
        ("Does the penalty apply if my employer already deducted all my tax?",
         "It can. The formula uses tax payable, meaning the tax chargeable on your taxable income for the year, not the unpaid balance. The salaried minimum of Rs 5,000 applies to most salaried people below Rs 5 million in salary."),
        ("Is the Rs 25,000 ATL surcharge the same as the late filing penalty?",
         "No. The Rs 25,000 surcharge for individuals is paid under Section 182A to be placed on the Active Taxpayers List after a late return. The Section 182 penalty is a separate penalty for the delay itself and is imposed by order."),
        ("Can I apply for an extension now that the deadline has passed?",
         "An extension application under Section 119 must be made to the Commissioner before the due date, so it does not help once the return is already late. The practical step now is to file as soon as possible."),
        ("Do companies have to file by 31 October 2026?",
         "No. The 31 October 2026 date covered persons whose returns were due on 30 September, mainly individuals and AOPs. Companies with a 30 June year-end normally file by 31 December."),
        ("How quickly can Kamboh Associates file a late return?",
         "Once we have complete documents, most salaried and freelancer returns are prepared and shared for approval within one to two working days. Business returns with full records take longer, depending on the volume of transactions."),
    ],
    sources=[SRC_DAWN_EXT, SRC_PROFIT_EXT, SRC_FBR_182, SRC_BR_ATLU, SRC_PP_BAR, SRC_IRIS],
    related=[(L['main'], "Income Tax Return Deadline Pakistan 2026"), ('/blogs/' + B_SLUG, "ATL Surcharge or Form ATL-U?"), ('/blogs/' + C_SLUG, "Last Date Guzar Gayi? (Roman Urdu)")],
    cta_h="Missed the 31 October Deadline? File Your Return This Week",
    cta_p="Fixed, published fees. Return and wealth statement prepared and shared for your approval before filing.",
    wa_text="My income tax return for Tax Year 2026 is late (missed 31 October). Please help me file it.",
)

# ─────────────────────────────── POST B ───────────────────────────────
POST_B = dict(
    slug=B_SLUG,
    title="ATL Surcharge Rs 25,000 or Form ATL-U? Late Filer's Guide",
    h1="Late Filer in 2026? Rs 25,000 ATL Surcharge or the Form ATL-U Undertaking",
    crumb="ATL Surcharge or Form ATL-U",
    description="Filed after 31 October 2026? Compare the Rs 25,000 Section 182A ATL surcharge with the draft Form ATL-U property undertaking and pick the right route.",
    keywords="Form ATL-U, ATL surcharge 25000, late filer ATL 2026, section 182A surcharge, join ATL without surcharge",
    category="Active Taxpayer List",
    icon="🧾",
    read="10 min read",
    banner="Filing after the deadline does not put you on the Active Taxpayers List. Individuals have two possible routes back: a Rs 25,000 surcharge, or a six-month property undertaking (draft rule).",
    tldr=("After the 31 October 2026 deadline, filing a return alone does not put you on the Active Taxpayers List. Under Section 182A, individuals pay a Rs 25,000 surcharge "
          "(AOPs Rs 50,000, companies Rs 100,000). In October 2026 FBR published a draft Form ATL-U: an individual who promises not to acquire any property for six months "
          "could join the ATL without the surcharge. Pay the surcharge if any property deal is possible within six months. Consider the undertaking only if it is live in IRIS "
          "and you are certain no property will come to you in that period."),
    lead=("Every November, the same question arrives on our WhatsApp from people who filed late: \"My return is submitted, so why am I still not on the ATL?\" "
          "In 2026 the answer comes with a bigger price tag than before, along with a possible way to avoid it. This guide sets out both routes, who each one suits, "
          "and the risks in the fine print."),
    body=f"""
<p class="tf-primary"><strong>Main guide:</strong> for the full surcharge rules, read our {a(L['surcharge'], 'ATL surcharge 2026 guide')}.</p>

<h2 id="why-not-on-atl">Why a Late Return Does Not Put You on the ATL</h2>
<p>The Active Taxpayers List is the list banks, property registrars and vehicle registration authorities check before choosing which withholding rate to apply. On-time filers appear on it once their return is processed. Section 182A treats late filers differently. A person who files after the due date (31 October 2026 for most Tax Year 2026 returns) is included only after paying a surcharge. Your return can be complete and accepted while you still show as inactive.</p>

<h2 id="route-one">Route 1: Pay the Section 182A Surcharge</h2>
<p>The Finance Act 2026 raised the surcharge from 1 July 2026:</p>
{table(["Taxpayer", "Surcharge now", "Before 1 July 2026", "Increase"], [
    ["Individual", "Rs 25,000", "Rs 1,000", "25 times"],
    ["Association of persons", "Rs 50,000", "Rs 10,000", "5 times"],
    ["Company", "Rs 100,000", "Rs 20,000", "5 times"],
])}
<p>Once you pay, your status updates and nothing else is required of you. There are no conditions on what you buy or sell afterwards. The increase has been controversial. The Pakistan Tax Bar Association asked FBR to withdraw the higher amount for Tax Year 2025 returns, arguing it cannot apply retrospectively. For Tax Year 2026 returns filed after 31 October 2026, the higher amount is the current rule.</p>

<h2 id="route-two">Route 2: The Form ATL-U Undertaking (Draft)</h2>
<p>On 6 October 2026, FBR published draft amendments to Rule 81B of the Income Tax Rules, 2002, through SRO 1691(I)/2026, and invited comments within seven days. As reported by Dawn and Business Recorder, the draft would let an individual who files the latest return after the due date join the ATL without the surcharge by submitting Form ATL-U through IRIS. The form records your name, CNIC or NTN, tax year, filing date and return acknowledgement number.</p>
<p>The undertaking has three parts:</p>
<ul>
<li><strong>The promise:</strong> you will not purchase, acquire or otherwise obtain ownership or beneficial interest in <em>any</em> property for six months.</li>
<li><strong>The clock:</strong> the six months run from the date on the IRIS electronic acknowledgement for Form ATL-U.</li>
<li><strong>The consequence:</strong> FBR can verify compliance with registries, authorities and financial institutions. If a breach is established after a hearing, the surcharge-free benefit is withdrawn from the date of the breach.</li>
</ul>
<p><strong>Status check:</strong> the reports we found up to 1 November 2026 describe this as a draft, and we have not seen a final notification. If Form ATL-U is not available in IRIS when you file, Route 1 is the only route.</p>

<h2 id="compare">Side-by-Side Comparison</h2>
{table(["Question", "Rs 25,000 surcharge", "Form ATL-U undertaking"], [
    ["Who can use it", "Individuals, AOPs and companies (at their own rates)", "Individuals only, under the draft"],
    ["Cash cost", "Rs 25,000 for an individual", "None"],
    ["Conditions afterwards", "None", "No property acquired for six months"],
    ["Legal status (1 Nov 2026)", "In force under Section 182A", "Draft rule; check IRIS"],
    ["Risk if your plans change", "None", "Benefit withdrawn from the date of breach"],
    ["Effect on the Section 182 penalty", "None. The penalty is separate.", "None. The penalty is separate."],
])}

<h2 id="choose">Which Route Fits Your Situation</h2>
<p><strong>Pay the surcharge if:</strong></p>
<ul>
<li>You are buying, booking or might inherit property, a plot file or a share in property in the next six months. The draft wording "any property" is broad, so do not assume it covers only land or houses.</li>
<li>You are partway through a property transaction, such as an instalment plan, a transfer in progress or a family settlement.</li>
<li>You want certainty, and Rs 25,000 is small next to the withholding difference on a single transaction.</li>
</ul>
<p><strong>The undertaking may suit you if:</strong></p>
<ul>
<li>Form ATL-U is actually live in IRIS when you file.</li>
<li>You are, for example, a salaried employee or a freelancer who needs filer rates mainly for banking, and you are certain nothing of this kind will happen in the next six months.</li>
<li>You keep a written note of the acknowledgement date, so you know exactly when the six months end.</li>
</ul>
<p><strong>Not an option:</strong> AOPs and companies. The draft applies only to individuals, so they pay Rs 50,000 or Rs 100,000.</p>

<h2 id="situations">Situations to Think Through Before You Sign</h2>
<p>An undertaking is a promise to FBR, and the draft attaches a real consequence to breaking it. Before choosing it, go through the next six months honestly. These are the situations we ask clients about:</p>
<ul>
<li><strong>An instalment plan already running.</strong> If you are paying instalments on a plot, flat or file in a housing scheme, a transfer, allotment or possession letter could fall inside the six months. That can look like acquiring an interest in property. Pay the surcharge.</li>
<li><strong>Family transfers and inheritance.</strong> A gift from a parent, or a share in inherited property being transferred to heirs, is still a change in ownership. If a family settlement is underway, do not give the undertaking without advice on whether it would count.</li>
<li><strong>Balloting and new bookings.</strong> Booking a unit in a new project, or winning a balloting draw, can create a beneficial interest even before full payment. Anyone planning to apply for a scheme should take Route 1.</li>
<li><strong>Vehicles and other assets.</strong> The draft wording, as reported, says "any property" without listing types. Until the final rule defines it, the cautious reading is that the promise may reach further than land and houses. Plan accordingly, and check the final wording before you rely on a narrower reading.</li>
</ul>
<p>If you are unsure about even one of these, Rs 25,000 buys certainty. A broken undertaking takes back the benefit and draws attention to your file, so it can cost more.</p>

<h2 id="numbers">Why the Surcharge Is Often Worth Paying</h2>
<p>The real comparison is not Rs 25,000 against zero. It is Rs 25,000 against what being off the ATL costs you on your actual transactions. Property transfers, vehicle registration and some banking transactions carry much higher withholding for persons not on the ATL. On one property deal, that difference can be many times the surcharge. Our {a(L['wht'], 'filer and non-filer withholding rates guide')} has the current rates. If even one such transaction is likely, pay the surcharge.</p>

<h2 id="steps">Steps After Filing Your Late Return</h2>
<ol>
<li>File the Tax Year 2026 return and wealth statement in IRIS and save the acknowledgement.</li>
<li>Choose your route. For the surcharge, generate the payment slip (PSID) for the Section 182A surcharge and pay it through your bank or banking app. For the undertaking, submit Form ATL-U in IRIS, if it is available, and save its acknowledgement.</li>
<li>Allow time for processing, then check your status online or by SMS (see our {a(L['atlcheck'], 'ATL status check guide')}).</li>
<li>Keep the payment receipt or the undertaking acknowledgement with your tax records.</li>
</ol>

<h2 id="penalty-reminder">The Penalty Still Applies</h2>
<p>Neither route settles the Section 182 penalty for filing late. That penalty can still be imposed by order. It is 0.1% of tax payable per day, with a minimum of Rs 40,000, or Rs 5,000 for most salaried individuals below Rs 5 million in salary. We explain the calculation with examples in {a('/blogs/' + A_SLUG, 'our guide to what happens after the 31 October deadline')}.</p>

<h2 id="how-we-help">How We Help Late Filers With ATL Status</h2>
<p>When we file a late return for you, we also go through the ATL decision with you. We ask about any property, plot or vehicle plans in the next six months, check what IRIS offers on the day, and make sure the surcharge or undertaking is filed against the right tax year. Return fees start at Rs 3,500 for salaried individuals and Rs 5,000 for freelancers and sole proprietors. The surcharge itself is paid to FBR. See our {a(L['filing'], 'return filing service')} for details.</p>

<div class="highlight-box"><p><strong>Not sure which route is safe for you?</strong> WhatsApp <strong><a href="{WA}" style="color:#14B8A6;font-weight:600">0328-4675162</a></strong> with your plans for the next six months, and we will tell you which route fits before you file.</p></div>
""",
    faqs=[
        ("What is Form ATL-U?",
         "Form ATL-U is an undertaking proposed by FBR in draft rules published on 6 October 2026. An individual who files late promises not to acquire any property for six months and, in return, joins the Active Taxpayers List without paying the Section 182A surcharge."),
        ("Is Form ATL-U available in IRIS now?",
         "The reports we found up to 1 November 2026 describe Form ATL-U as a draft. Whether it is usable depends on FBR finalising the rule and enabling the form in IRIS, so check IRIS on the day you file."),
        ("How much is the ATL surcharge for late filers in 2026?",
         "From 1 July 2026 under the Finance Act 2026, the Section 182A surcharge is Rs 25,000 for individuals, Rs 50,000 for associations of persons, and Rs 100,000 for companies."),
        ("What counts as property under the ATL-U undertaking?",
         "The draft wording, as reported, covers purchasing, acquiring or otherwise obtaining ownership or beneficial interest in any property. That is broad. Until the final rule is published, do not assume it is limited to houses or land."),
        ("What happens if I break the six-month undertaking?",
         "Under the draft, FBR can verify compliance using records from registries, authorities and financial institutions. If a breach is established after a hearing, the surcharge-free ATL benefit is withdrawn from the date of the breach."),
        ("Can an AOP or company use Form ATL-U?",
         "No. The draft applies to individuals only. AOPs pay Rs 50,000 and companies pay Rs 100,000 to be placed on the Active Taxpayers List after a late return."),
        ("Does paying the surcharge remove the late filing penalty?",
         "No. The surcharge only restores ATL status. The Section 182 penalty for filing after the due date is a separate matter and can still be imposed by order."),
        ("How do I check whether I am back on the ATL?",
         "Check FBR's online ATL search with your CNIC or NTN, or send an SMS with ATL, a space and your CNIC to 9966. Allow some processing time after paying or submitting the undertaking."),
    ],
    sources=[SRC_BR_ATLU, SRC_DAWN_ATLU, SRC_PP_BAR, SRC_FBR_182, SRC_FBR_ATL],
    related=[(L['surcharge'], "FBR ATL Surcharge 2026"), ('/blogs/' + A_SLUG, "31 October Deadline Passed: Next Steps"), ('/blogs/' + C_SLUG, "Last Date Guzar Gayi? (Roman Urdu)")],
    cta_h="Filed Late? Get Back on the ATL the Right Way",
    cta_p="We file your late return and help you choose between the surcharge and the undertaking.",
    wa_text="I filed (or need to file) my Tax Year 2026 return late and need help getting back on the ATL.",
)

# ─────────────────────────────── POST C (Roman Urdu) ───────────────────────────────
POST_C = dict(
    slug=C_SLUG,
    title="Tax Return Ki Last Date Guzar Gayi? Ab Kya Karein (2026)",
    h1="Tax Return Ki Last Date (31 October 2026) Guzar Gayi — Ab Return Kaise File Karein",
    crumb="Last Date Guzar Gayi",
    description="Tax return ki last date 31 October 2026 guzar gayi? Late return ab bhi file ho sakti hai. Steps, documents, jurmana aur ATL surcharge ki Roman Urdu guide.",
    keywords="tax return last date guzar gayi, late tax return kaise file karein, 31 October ke baad return, FBR jurmana late return, ATL surcharge 25000",
    category="Roman Urdu Guide",
    icon="📝",
    read="11 min read",
    banner="Tax Year 2026 ki return ki last date 31 October 2026 thi. Return ab bhi file ho sakti hai, magar jitni der karenge, nuqsan utna barhta jayega.",
    tldr=("Tax return ki last date guzar gayi hai, magar return ab bhi IRIS par file ho sakti hai. Late return par Section 182 ke tehat jurmana lag sakta hai "
          "(zyada tar salaried logon ke liye kam az kam Rs 5,000, baqi ke liye Rs 40,000). ATL mein wapis aane ke liye Rs 25,000 surcharge dena hoga, ya agar IRIS mein "
          "Form ATL-U maujood ho to 6 mahine property na lene ka wada karna hoga. Sab se pehle documents ikatthe karein, wealth statement theek banayein aur jaldi file karein."),
    lead=("Bohat se log 1 November ki subah ye soch kar pareshan hote hain: \"Last date nikal gayi, ab kya hoga?\" Pehli baat: ghabrane ki zaroorat nahi, "
          "return ab bhi file ho sakti hai. Doosri baat: ab har din ki der ka asar hai. Is guide mein hum asaan Roman Urdu mein batayenge ke late return kaise file karein, "
          "kaun se kaghzaat chahiye, kitna kharcha aa sakta hai aur kaun si ghaltiyon se bachna hai."),
    body=f"""
<p class="tf-primary"><strong>English guide:</strong> poori tafseel aur jurmane ki misalein hamari English guide mein hain: {a('/blogs/' + A_SLUG, 'what to do after the 31 October deadline')}.</p>

<h2 id="kya-hua">Last Date Kaun Si Thi Aur Ab Kya Badla?</h2>
<p>Tax Year 2026 (1 July 2025 se 30 June 2026 tak ki aamdani) ki return pehle 30 September tak file honi thi. FBR ne pehle ise 15 October aur phir Section 214A ke tehat 31 October 2026 tak barhaya. Ye date salaried, karobari afraad, freelancers, kiraye ki aamdani walon aur AOPs ke liye thi. Companies ki date alag hoti hai.</p>
<p>1 November 2026 tak FBR ne mazeed kisi extension ka elaan nahi kiya tha. Is liye ab jo return file hogi wo "late return" kehlayegi. Late return bhi poori tarah valid return hai. Farq sirf itna hai ke iske saath teen cheezein judi hain: jurmana, ATL se bahar rehna aur non-filer wali katautiyan.</p>

<h2 id="kaghzaat">Pehla Kaam: Apne Kaghzaat Ikatthe Karein</h2>
<p>Late return mein sab se zyada waqt kaghzaat dhoondne mein lagta hai. Apni category dekh kar ye cheezein tayyar karein:</p>
{table(["Aap kaun hain", "Zaroori kaghzaat"], [
    ["Salaried (naukri pesha)", "CNIC, salary certificate ya employer ki annual tax deduction statement, 1 July 2025 se 30 June 2026 tak ki bank statements"],
    ["Dukandar ya karobari", "Upar wali cheezein, saath sales aur purchase ka record, kharchon ki details, aur suppliers ya buyers ki taraf se kati hui tax ki slips"],
    ["Freelancer (Upwork, Fiverr waghera)", "Bank statements, foreign remittance ka record (PRC ya bank ka certificate), platform ki earning report"],
    ["Kiraye ki aamdani", "Kirayanama, saal bhar mein mila kiraya, aur tenant ki taraf se kata hua tax (agar kata ho)"],
    ["Overseas Pakistani", "CNIC ya NICOP, Pakistan mein aamdani aur assets ka record, safar ki dates (residency check karne ke liye)"],
])}
<p>Wealth statement ke liye ye bhi chahiye: pichle saal ki wealth statement, saal mein khareeda ya becha gaya plot, gaari, sona ya shares, aur loans ki details.</p>

<h2 id="steps">IRIS Par Late Return File Karne Ka Tareeqa</h2>
<ol>
<li><strong>Login karein:</strong> iris.fbr.gov.pk par apne CNIC aur password se login karein. Password bhool gaye hon to "Forgot Password" se registered mobile aur email par code mangwa lein.</li>
<li><strong>Sahi form kholein:</strong> Declaration mein Tax Year 2026 ka Return of Income (Section 114) form chunein. Agar draft pehle se save hai to wahi kholein, naya na banayein.</li>
<li><strong>Aamdani bharein:</strong> salary, karobar, kiraya ya foreign income, jo bhi ho, apni sahi category mein likhein. Andaze se figures na bharein.</li>
<li><strong>Kati hui tax darj karein:</strong> employer, bank, mobile company aur bijli ke bill par kati hui advance tax ki details darj karein. Ye aap ke tax mein se minus hoti hai.</li>
<li><strong>Wealth statement banayein:</strong> 30 June 2026 tak ke assets aur liabilities likhein, aur reconciliation check karein ke figures aapas mein milti hain.</li>
<li><strong>Baqi tax jama karwayein:</strong> agar form mein tax baqi aa raha hai to pehle payment slip (PSID) bana kar bank ya app se jama karwayein, phir submit karein.</li>
<li><strong>Submit karke acknowledgement save karein:</strong> return aur wealth statement dono submit karein aur acknowledgement ka PDF sambhal kar rakhein.</li>
</ol>
<p>Ek mashwara: agar aap ne pichle saal ki wealth statement nahi bhari thi, ya is saal koi bara asset khareeda hai, to pehle kisi tajurbakar consultant se figures check karwa lein. Notices aksar yahin se shuru hote hain.</p>

<h2 id="jurmana">Late Return Par Kitna Jurmana Lag Sakta Hai?</h2>
<p>FBR ki website par Section 182 ka jo text maujood hai (1 November 2026 ko check kiya), uske mutabiq:</p>
<ul>
<li>Har din ki der par saal ke tax payable ka 0.1%.</li>
<li>Zyada se zyada tax payable ka 50%.</li>
<li>Kam az kam Rs 40,000, chahe tax zero ho.</li>
<li>Agar aap ki 75% ya zyada aamdani salary se hai aur salary Rs 50 lakh se kam hai, to kam az kam jurmana Rs 5,000 hai.</li>
</ul>
<p>Yaad rakhein ke ye jurmana IRIS submit karte waqt khud nahi kat-ta. Tax officer notice bhej kar order ke zariye lagata hai, aur aap ko apni wajah batane ka mauqa milta hai. Agar der ki koi asal aur saabit wajah thi, jaise IRIS ka masla jiska screenshot aap ke paas ho, to wo jawab mein likhi ja sakti hai. Mazeed misalein hamari {a(L['penalty'], 'late filing penalty guide')} mein hain.</p>

<h2 id="atl">ATL Mein Wapis Kaise Aayen?</h2>
<p>Late return file karne se aap khud ba khud Active Taxpayers List (ATL) mein nahi aate. Finance Act 2026 ke baad Section 182A ka surcharge ye hai:</p>
{table(["Kaun", "Surcharge"], [
    ["Individual (fard)", "Rs 25,000"],
    ["AOP (partnership)", "Rs 50,000"],
    ["Company", "Rs 100,000"],
])}
<p>Individuals ke liye FBR ne October 2026 mein ek draft rule (Form ATL-U) bhi jari kiya tha. Is mein aap 6 mahine tak koi property na lene ka wada karte hain aur surcharge nahi dena parta. 1 November 2026 tak ki khabron mein ye draft hi tha, is liye file karte waqt IRIS mein check karein ke ye form maujood hai ya nahi. Dono raston ka mukammal muqabla hamari {a('/blogs/' + B_SLUG, 'ATL surcharge ya Form ATL-U guide')} mein hai.</p>
<p>ATL status check karne ke liye 9966 par SMS karein: ATL, phir space, phir apna 13 hindson wala CNIC.</p>

<h2 id="ghaltiyan">Late Return Mein Ye 6 Ghaltiyan Na Karein</h2>
<ul>
<li><strong>Jaldi mein wealth statement andaze se bharna.</strong> Baad mein revise karna parta hai (dekhein {a(L['revised'], 'revised return kab aur kaise file hoti hai')}).</li>
<li><strong>Aamdani kam dikhana taake tax kam aaye.</strong> FBR ke paas bank, property aur katautiyon ka data hota hai. Is se masla aur bara ho jata hai.</li>
<li><strong>Agle extension ke intezar mein baithe rehna.</strong> FBR ne koi elaan nahi kiya, aur jurmane ka hisab har din barhta hai.</li>
<li><strong>Kisi aur ke IRIS account se ya ghalat CNIC par return file karna.</strong> Har shakhs ki return uske apne CNIC par aur uski apni aamdani ke mutabiq honi chahiye.</li>
<li><strong>Notice aaye to nazar-andaz karna.</strong> Section 114(4) ke notice ka jawab na diya jaye to FBR apne data par assessment kar sakta hai. Hamari {a(L['n114'], 'Section 114 notice guide')} dekhein.</li>
<li><strong>Ye samajhna ke surcharge dene se jurmana khatam ho gaya.</strong> Surcharge sirf ATL ke liye hai. Jurmana alag cheez hai.</li>
</ul>

<h2 id="sawalat">WhatsApp Par Aane Wale Aam Sawalat</h2>
<p><strong>"Main ne pichle saal bhi return nahi bhari, ab kya karun?"</strong> Pehle purane saal ki return bharein, phir is saal ki. Is tarah wealth statement ki opening aur closing figures aapas mein judi rehti hain.</p>
<p><strong>"Mera tax to employer ne kaat liya tha, phir bhi return zaroori hai?"</strong> Ji haan. Return bharne ki zimmedari alag hai, aur jurmane ke hisab mein "tax payable" poora saal ka tax hai, sirf baqi raqam nahi.</p>
<p><strong>"Main Lahore se bahar hoon, kya online ho sakta hai?"</strong> Ji haan. Hum poora kaam WhatsApp par karte hain. Aap documents bhejein, hum figures aap ko dikha kar aap ki manzoori ke baad file karte hain.</p>

<h2 id="hamari-madad">Kamboh Associates Aap Ki Late Return Kaise File Karta Hai</h2>
<p>November mein hamare paas sab se zyada kaam late returns ka hota hai. Hamara tareeqa seedha hai:</p>
<ol>
<li>Aap WhatsApp par CNIC aur maujood documents bhejein. Hum ek working day mein bata dete hain ke kya kami hai.</li>
<li>Hum return aur reconcile hui wealth statement tayyar karke aap ko figures dikhate hain.</li>
<li>Aap ki manzoori ke baad hum IRIS par file karte hain aur ATL ke surcharge ya undertaking mein rehnumai karte hain.</li>
<li>Baad mein jurmane ya Section 114 ka notice aaye to uska jawab bhi hum tayyar karte hain.</li>
</ol>
<p>Hamari fees wahi hain jo time par return ki hoti hain: salaried return Rs 3,500 se, freelancer aur dukandar ki return Rs 5,000 se, AOP Rs 8,000 se aur overseas Pakistani Rs 6,000 se. Jurmana ya surcharge FBR ko jata hai, hamein nahi. Tafseel {a(L['pricing'], 'pricing page')} par dekhein. Hamara daftar Awan Town, Lahore mein hai.</p>

<div class="highlight-box"><p><strong>Last date guzar gayi?</strong> Abhi WhatsApp karein: <strong><a href="{WA}" style="color:#14B8A6;font-weight:600">0328-4675162</a></strong>. Documents bhejein, hum bata denge ke aap ki late return mein kya kya shamil hai.</p></div>
""",
    faqs=[
        ("Kya 31 October 2026 ke baad bhi tax return file ho sakti hai?",
         "Ji haan. IRIS par Tax Year 2026 ki return ab bhi file ho sakti hai. Ye late return kehlayegi, is liye Section 182 ka jurmana lag sakta hai aur ATL mein aane ke liye surcharge dena hoga ya Form ATL-U ka rasta, agar maujood ho, istemal karna hoga."),
        ("Late return par kam az kam jurmana kitna hai?",
         "FBR ki website par maujood Section 182 ke mutabiq kam az kam jurmana Rs 40,000 hai. Agar 75% ya zyada aamdani salary se ho aur salary Rs 50 lakh se kam ho to kam az kam Rs 5,000 hai. Is se upar har din tax payable ka 0.1% lagta hai, zyada se zyada 50% tak."),
        ("Kya FBR ne last date dobara barhai hai?",
         "1 November 2026 tak FBR ne 31 October ke baad koi extension announce nahi ki thi. Kisi nayi khabar ke liye FBR ki official website ya X account dekhein."),
        ("ATL mein wapis aane ke liye kitne paise dene honge?",
         "Late return ke baad individual ko Section 182A ke tehat Rs 25,000 surcharge dena hota hai, AOP ko Rs 50,000 aur company ko Rs 100,000. Individuals ke liye Form ATL-U ka draft rule bhi hai jis mein 6 mahine property na lene ka wada karna hota hai."),
        ("Agar mera tax employer ne poora kaat liya tha to kya phir bhi jurmana lagega?",
         "Lag sakta hai, kyunke jurmane ka hisab saal ke poore tax payable par hota hai. Magar zyada tar salaried logon ke liye, jin ki salary Rs 50 lakh se kam hai, kam az kam jurmana Rs 5,000 hai."),
        ("Late return file karne mein kitne din lagte hain?",
         "Agar saare documents mukammal hon to salaried aur freelancer ki return aam tor par ek se do working days mein tayyar ho kar manzoori ke liye bhej di jati hai. Karobari return mein record ke hisab se zyada waqt lagta hai."),
        ("Kya main ghar baithe late return file karwa sakta hoon?",
         "Ji haan. Kamboh Associates poora kaam WhatsApp par karta hai. Aap documents bhejte hain, hum return aur wealth statement tayyar karke dikhate hain, aur aap ki manzoori ke baad IRIS par file karte hain."),
        ("ATL status kaise check karein?",
         "9966 par SMS bhejein jis mein ATL likh kar space dein aur apna 13 hindson wala CNIC likhein. FBR ki website par online ATL search bhi maujood hai. Surcharge ya undertaking ke baad status update hone mein kuch waqt lag sakta hai."),
    ],
    sources=[SRC_DAWN_EXT, SRC_FBR_182, SRC_BR_ATLU, SRC_FBR_ATL, SRC_IRIS],
    related=[('/blogs/' + A_SLUG, "31 October Deadline Passed: Next Steps"), ('/blogs/' + B_SLUG, "ATL Surcharge or Form ATL-U?"), (L['revised'], "Revised Return Kab Aur Kaise")],
    cta_h="Last Date Guzar Gayi? Return Isi Hafte File Karwayein",
    cta_p="Fixed fees, WhatsApp par poora kaam, figures aap ki manzoori ke baad file.",
    wa_text="Assalam o Alaikum, meri Tax Year 2026 ki return late ho gayi hai (31 October guzar gaya). File karwani hai.",
)

POSTS = [POST_A, POST_B, POST_C]
