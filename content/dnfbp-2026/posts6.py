"""Revision series (6 posts): revised returns and wealth statements. Facts checked 11 November 2026 against the Income Tax
Ordinance 2001 amended up to 30.06.2026: ss.111, 114(6), 114(6A), 114(6B), 116, 120, 122(2)-(4), 122(9), 170, 182, 205."""
from posts import WA, a, table, S_IRIS

DATE = "2026-11-11"
DLONG = "11 November 2026"

S_ITO = ("FBR: Income Tax Ordinance, 2001 (amended up to 30.06.2026)", "https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf")
S_FBR = ("Federal Board of Revenue", "https://www.fbr.gov.pk/")

SL = dict(r60="revised-return-tax-year-2026-60-days-pakistan", ws5="revise-wealth-statement-last-5-years-pakistan",
          ref="revised-return-claim-refund-missed-tax-credits-pakistan", miss="assets-missing-from-wealth-statement-pakistan",
          pen="revised-return-before-notice-penalty-relief-section-114-6a", sal="salaried-revised-return-tax-year-2026-pakistan")
B = {k: "/blogs/" + v for k, v in SL.items()}
X = {"rru": "/blogs/revised-tax-return-kab-kaise-file-karein-pakistan-2026", "rpd": "/blogs/post-deadline-revised-return-correcting-rushed-filing-pakistan",
     "wsr": "/blogs/wealth-statement-revise-kab-kaise-iris-pakistan-2026", "wsm": "/blogs/wealth-statement-mismatch-discovered-after-filing-pakistan",
     "rec": "/blogs/wealth-reconciliation-match-nahi-ho-rahi-fix-pakistan-2026", "wsg": "/blogs/wealth-statement-guide-pakistan-2026",
     "notice": "/fbr-notice-defense", "pricing": "/pricing", "refund": "/blogs/tax-refund-pakistan-2026", "sole_ws": "/blogs/sole-proprietor-wealth-statement-pakistan"}
SERIES = (f'<p class="tf-primary"><strong>Revision guides:</strong> {a(B["r60"], "TY2026 revised return (60 days)")} &middot; {a(B["ws5"], "wealth statements of the last 5 years")} &middot; '
          f'{a(B["pen"], "revising before a notice")} &middot; {a(B["ref"], "refunds and missed credits")} &middot; {a(B["miss"], "assets people leave out")} &middot; {a(B["sal"], "salaried revisions")}</p>')
FEE_REV = "Fixed fee for the revision confirmed before we start; wealth statement Rs 2,000 and salaried return Rs 3,500 as published."

PEN_TABLE = table(["When you revise", "What you pay with the revised return", "Section"], [
    ["Voluntarily, before any notice under Section 177 (audit) or 122(9)", "Tax short paid + default surcharge; no penalty is recovered", "114(6A)"],
    ["After the Commissioner points out tax during audit, or before a 122(9) notice is issued", "Tax + default surcharge + 25% of the leviable penalties", "114(6A), first proviso"],
    ["After a show cause notice under Section 122(9)", "Tax + default surcharge + 50% of the leviable penalties; the notice then abates", "114(6A), second proviso"],
])

# ───────────────────────────── 1. TY2026 60 days ─────────────────────────────
R60 = dict(
    slug=SL["r60"],
    svc=dict(h2="Get Your TY2026 Revision Filed Inside the 60 Days", intro="The 60-day window is the easiest time to correct a return: no approval is needed. We check what needs correcting, prepare the reasons and the revised figures, and file before the window closes.",
             hook="Filed your 2026 return in a rush?", fee=FEE_REV, btn="Revise my 2026 return",
             items=["A line-by-line check of the return and wealth statement you filed", "The exact date your 60 days end", "Revised figures, revised reconciliation and written reasons prepared for your signature", "Filing on IRIS and the acknowledgement sent to you", "If the 60 days have passed, the approval request to the Commissioner"],
             risks=["After 60 days, revision needs the Commissioner's written approval", "A revised return that misses a condition is treated as invalid", "Leaving a known error until a notice arrives brings penalties"]),
    title="Revised Return Tax Year 2026: The 60-Day Window Explained",
    h1="Revised Return for Tax Year 2026: How the 60-Day Window Works, the Conditions, and What Happens After",
    crumb="TY2026 Revised Return (60 Days)",
    description="Found a mistake in your 2026 return? How Section 114(6) lets you revise within 60 days without approval, the conditions, deadlines and what comes next.",
    keywords="revised return 2026, revise income tax return within 60 days, section 114(6) revised return, revised return without commissioner approval, revise return after 31 October 2026",
    category="Return Revision",
    icon="🔁",
    read="12 min read",
    banner="Most Tax Year 2026 returns were filed close to the 31 October 2026 deadline. If yours has a mistake, the next 60 days are the simplest time to fix it.",
    tldr=("Under Section 114(6) of the Income Tax Ordinance (amended up to 30 June 2026), a person who discovers an omission or wrong statement in a filed return may "
          "file a revised return, with revised accounts where relevant and written, signed reasons. Commissioner approval is normally required, but not if the "
          "revised return is filed within 60 days of filing the original. A return filed on 31 October 2026 can therefore be revised without approval until about "
          "30 December 2026. After that, approval is deemed granted if the Commissioner does not decide within 60 days of the request, and must be granted for a bona "
          "fide omission. A revised return that misses a condition is treated as invalid."),
    lead=("The Tax Year 2026 deadline was extended twice and closed on 31 October 2026, and many returns went in during the last week. Rushed returns often leave out "
          "a bank account, a plot, a source of income or a tax credit. This guide explains exactly how the law lets you correct a 2026 return, why the next 60 days "
          "matter, and what to prepare."),
    body=f"""
{SERIES}

<h2 id="law">What Section 114(6) Says</h2>
<p>Any person who, having furnished a return, discovers an omission or wrong statement in it may file a revised return, subject to these conditions:</p>
{table(["Condition", "What it means in practice"], [
    ["(a) Revised accounts", "Business taxpayers attach revised accounts or revised audited accounts. The Commissioner may waive this if they are not necessary."],
    ["(b) Written reasons", "The reasons for revision, in writing and signed by the taxpayer, are filed with the revised return."],
    ["(ba) Commissioner's approval", "Written approval of the Commissioner is required, except in the cases below."],
    ["(c) Not below an order", "Taxable income declared must not be less (and loss not more) than income or loss determined by an order under Sections 121, 122, 122A, 129, 132, 133 or 221."],
])}
<p>If any condition is not met, the revised return is treated as an <strong>invalid return</strong>, as if it had not been filed. That is why the reasons, the figures and the timing all matter.</p>

<h2 id="sixty-days">The 60-Day Rule: When No Approval Is Needed</h2>
<p>The provisos to Section 114(6) remove the approval requirement in three situations:</p>
<ol>
<li><strong>Within 60 days of filing the return.</strong> A revised return filed within sixty days of filing the original does not need the Commissioner's approval.</li>
<li><strong>When the Commissioner does not decide in time.</strong> If you seek approval and the Commissioner makes no written order within 60 days of your request, approval is deemed granted.</li>
<li><strong>When you declare more income.</strong> If the revised taxable income is more than (or the loss less than) the amount assessed under Section 120, approval is deemed granted.</li>
</ol>
<p>The law also says the Commissioner <strong>shall</strong> grant approval for a bona fide omission or wrong statement. The mode and manner of seeking revision are prescribed by FBR, through IRIS.</p>

<h2 id="dates">Your 60-Day Deadline for Tax Year 2026</h2>
{table(["Original return filed on", "60 days end on (approximately)"], [
    ["30 September 2026", "29 November 2026"],
    ["15 October 2026", "14 December 2026"],
    ["25 October 2026", "24 December 2026"],
    ["31 October 2026", "30 December 2026"],
    ["Late, e.g. 20 November 2026", "19 January 2027"],
])}
<p>Count from the date shown on your IRIS acknowledgement. Do not leave the revision to the last day: IRIS can be slow near deadlines, and preparing a reconciliation that balances takes time.</p>

<h2 id="what-to-fix">Common Reasons to Revise a 2026 Return</h2>
<ul>
<li>A bank account, savings certificate or profit on debt left out.</li>
<li>A plot, house, vehicle or gold not shown in the wealth statement.</li>
<li>Rental, freelance or business income omitted.</li>
<li>Tax deducted at source not claimed, for example on electricity bills, mobile bills, vehicle tokens or bank cash withdrawals where adjustable.</li>
<li>A wealth reconciliation that does not balance, or household expenses understated.</li>
<li>Wrong figures carried from the employer's certificate or from last year's statement.</li>
</ul>
<p>For assets in particular, see our guide to {a(B['miss'], 'assets people leave out of wealth statements')}.</p>

<h2 id="what-happens">What Happens When the Revised Return Is Filed</h2>
<p>A complete return is treated as an assessment order under Section 120. When you file a valid revised return, Section 122(3) says the Commissioner is treated as having made an <strong>amended assessment</strong> of the income and tax set out in the revised return, and the revised return is taken to be an amended assessment order issued on the day it is filed. In plain terms, the revised return replaces the original as your assessment for the year.</p>
<p>The Commissioner can still amend an assessment later, within the time limits in Section 122(4): the later of five years from the end of the financial year in which the original assessment was issued, or one year from the end of the financial year of the amended assessment.</p>

<h2 id="tax-up-or-down">If the Revision Increases or Reduces Tax</h2>
<p><strong>Tax increases:</strong> pay the additional tax with the revision. Under Section 114(6A), a person who voluntarily files a revised return with the tax short paid and default surcharge, before receiving a notice under Section 177 or 122(9), pays no penalty. Our guide to {a(B['pen'], 'revising before a notice')} explains the penalty relief in detail.</p>
<p><strong>Tax reduces or a refund arises:</strong> the revised return can create a refund. Refund applications under Section 170 must be made within three years of the later of the assessment date or the date the tax was paid; see our guide to {a(B['ref'], 'claiming refunds and missed credits')}.</p>

<h2 id="wealth">Revising the Wealth Statement at the Same Time</h2>
<p>Most return revisions also change the wealth statement. Section 116(3) allows a revised wealth statement, with a revised reconciliation and the reasons, before you receive a notice under Section 122(9) for that year. The Commissioner can declare a revision void if it is not a bona fide correction. Revise both together so the figures agree.</p>

<h2 id="prepare">What to Prepare</h2>
<ol>
<li>The IRIS acknowledgement of the original return, to fix your 60-day date.</li>
<li>Documents for each change: bank certificates, property papers, salary or rent records, withholding certificates.</li>
<li>Revised figures for income, deductions, credits and the wealth statement.</li>
<li>A revised wealth reconciliation that balances.</li>
<li>A short, honest written reason for each change, signed by you.</li>
<li>Payment of any additional tax before submitting.</li>
</ol>

<h2 id="after-60">If Your 60 Days Have Already Passed</h2>
<p>You can still revise, but with the Commissioner's approval. Apply with your reasons; if no written order is made within 60 days of your request, approval is deemed granted. If you are increasing your income above the assessed figure, approval is deemed granted anyway. For older years and the five-year limits, see our guide to {a(B['ws5'], 'revising wealth statements of the last five years')}; for the general background in Roman Urdu, see {a(X['rru'], 'revised return kya hai')}.</p>
""",
    faqs=[
        ("Can I revise my 2026 income tax return?",
         "Yes. Section 114(6) allows a revised return when you discover an omission or wrong statement, with written reasons and, for businesses, revised accounts."),
        ("Do I need the Commissioner's approval to revise?",
         "Not if the revised return is filed within 60 days of filing the original return. After that, approval is needed, but it is deemed granted if the Commissioner does not decide within 60 days of your request."),
        ("I filed on 31 October 2026. Until when can I revise without approval?",
         "Within 60 days of filing, which is about 30 December 2026. Count from the date on your IRIS acknowledgement."),
        ("What happens if my revised return misses a condition?",
         "Section 114(6) says it is treated as an invalid return, as if it had not been filed."),
        ("Will a revised return trigger a penalty?",
         "Not if you file it voluntarily with any tax short paid and default surcharge before a notice under Section 177 or 122(9), under Section 114(6A)."),
        ("Does the revised return replace the original?",
         "Yes. Under Section 122(3) the revised return is treated as an amended assessment order issued on the day it is filed."),
        ("Should I revise my wealth statement too?",
         "Usually yes. Section 116(3) allows a revised wealth statement with a revised reconciliation and reasons before a notice under Section 122(9)."),
        ("Can a revision reduce my tax?",
         "Yes, if the original overstated income or missed credits. A refund can then be claimed within the time limit in Section 170."),
    ],
    sources=[S_ITO, S_IRIS, S_FBR],
    related=[(B["pen"], "Revise Before a Notice"), (B["ws5"], "Wealth Statements: Last 5 Years"), (X["rpd"], "Post-Deadline Revised Return")],
    cta_h="Fix Your 2026 Return While It's Simple",
    cta_p="Inside 60 days no approval is needed. We check, prepare and file the revision.",
    wa_text="Assalam o Alaikum, mujhe apni Tax Year 2026 ki return revise karwani hai (60 din ke andar).",
)

# ───────────────────────────── 2. Last 5 years ─────────────────────────────
WS5 = dict(
    slug=SL["ws5"],
    svc=dict(h2="Let Us Review Your Last Five Wealth Statements", intro="Older years are where unexplained gaps hide. We review each year's statement against the next, find the breaks, and correct them in the right order before FBR asks.",
             hook="Worried about wealth statements from earlier years?", fee="Review fee confirmed before we start; each wealth statement Rs 2,000 as published.", btn="Review my last 5 years",
             items=["A year-by-year check that each closing figure matches the next opening figure", "A list of assets, loans and gifts missing in any year", "Revised statements and reconciliations, prepared oldest year first", "Advice on whether a return revision is also needed for each year", "Replies if a notice has already arrived"],
             risks=["Unexplained assets can be taxed as income under Section 111", "Once a 122(9) notice arrives, a voluntary wealth statement revision is no longer available", "Penalties rise if tax is pointed out first"]),
    title="Revise Wealth Statements of the Last 5 Years (TY2021–TY2026)",
    h1="Revising Wealth Statements of the Last Five Years: What You Can Still Correct, and Why It Matters Now",
    crumb="Wealth Statements: Last 5 Years",
    description="How far back you can correct wealth statements and returns: the five-year limit in Section 122, Section 116(3) revisions, and fixing years in order.",
    keywords="revise wealth statement previous years, wealth statement last 5 years Pakistan, section 116(3) revised wealth statement, section 122 five years amendment, correct old wealth statement FBR",
    category="Wealth Statement",
    icon="🗓️",
    read="12 min read",
    banner="An error in one year's wealth statement carries into every year after it. Correcting the chain before FBR asks is far cheaper than explaining it afterwards.",
    tldr=("Section 116(3) lets an individual file a revised wealth statement, with a revised reconciliation and reasons, at any time before receiving a notice under "
          "Section 122(9) for that year. FBR's own power to amend an assessment is limited by Section 122(2) to five years from the end of the financial year in which "
          "the assessment was issued or treated as issued, which is when the return was filed. In practice, years from about Tax Year 2021 onwards are still open in "
          "2026–27, and a gap in any of them can be questioned as unexplained income or assets under Section 111. Fix the years in order, oldest first, so each "
          "closing figure becomes the next year's opening figure."),
    lead=("FBR increasingly compares wealth statements with property, vehicle, bank and travel data. A plot bought in 2021 but never declared, or a loan from a "
          "relative never recorded, does not stay in 2021: it breaks every reconciliation after it. This guide explains how far back you can still correct, what "
          "the law allows, and the order to do it in."),
    body=f"""
{SERIES}

<h2 id="why-chain">Why Wealth Statements Form a Chain</h2>
<p>Each year's wealth statement opens with the previous year's closing net wealth. If an asset is missing in Tax Year 2022, then the 2022 closing figure is wrong, the 2023 opening figure is wrong, and the reconciliation in every later year either fails or has been forced to balance with an unrealistic expense or income figure. Correcting only the latest year rarely works; the chain must be fixed from the year the error started.</p>

<h2 id="how-far">How Far Back Can FBR Look, and You Correct?</h2>
<p>A filed return is treated as an assessment order under Section 120 on the day it is filed. Under Section 122(2), the Commissioner cannot amend that assessment after <strong>five years from the end of the financial year</strong> in which it was issued or treated as issued.</p>
{table(["Tax year", "Return typically filed in", "Financial year ends", "Five-year amendment limit ends (approx.)"], [
    ["2020", "Late 2020", "30 June 2021", "30 June 2026 (passed)"],
    ["2021", "Late 2021", "30 June 2022", "30 June 2027"],
    ["2022", "Late 2022", "30 June 2023", "30 June 2028"],
    ["2023", "Late 2023", "30 June 2024", "30 June 2029"],
    ["2024", "Late 2024", "30 June 2025", "30 June 2030"],
    ["2025", "Late 2025", "30 June 2026", "30 June 2031"],
    ["2026", "Late 2026", "30 June 2027", "30 June 2032"],
])}
<p>Dates depend on when each return was actually filed; a return filed after 30 June of the following year moves the limit by a year. Where an assessment has been amended, Section 122(4) allows further amendment within the later of five years from the original assessment year-end or one year from the amended assessment year-end. So, as of late 2026, roughly Tax Years 2021 to 2026 are the years that matter.</p>

<h2 id="wealth-revision">Revising a Wealth Statement: Section 116(3)</h2>
{table(["Rule", "Detail"], [
    ["Who", "A person who has filed a wealth statement and discovers an omission or wrong statement"],
    ["What to file", "A revised wealth statement, a revised wealth reconciliation, and the reasons for revision, under intimation to the Commissioner in the prescribed form"],
    ["Deadline", "Any time before receipt of a notice under Section 122(9) for that tax year"],
    ["Safeguard", "The Commissioner may declare the revision void by written order if it is not to correct a bona fide omission or wrong statement"],
])}
<p>There is no 60-day limit for wealth statement revision; the cut-off is the 122(9) notice. That is the key reason to act early.</p>

<h2 id="return-too">When the Return Must Be Revised Too</h2>
<p>If the wealth statement change only reflects something already explained, such as an asset bought from declared savings but entered under the wrong head, revising the wealth statement may be enough. If the change reveals income that was not declared, such as rent from the omitted property, the return for that year also needs revision under Section 114(6), with the tax and default surcharge. For years where more than 60 days have passed since filing, return revision needs the Commissioner's approval, which is deemed granted if no order is made within 60 days of the request, or if the revision increases declared income.</p>

<h2 id="order">The Right Order to Fix Several Years</h2>
<ol>
<li><strong>Find the first break.</strong> Compare each year's closing statement with the next year's opening statement, and each reconciliation with income and spending.</li>
<li><strong>Collect the evidence for that year:</strong> purchase documents, bank statements, gift or loan records.</li>
<li><strong>Revise the earliest affected year</strong> (wealth statement, and return if income changes).</li>
<li><strong>Carry the corrected closing figure forward</strong> and revise each later year in turn.</li>
<li><strong>Pay any tax and default surcharge</strong> with the revised returns before any notice arrives.</li>
<li><strong>Keep a file</strong> of each revision, its reasons and evidence, for at least six years under Section 174.</li>
</ol>

<h2 id="example">Example: A Plot Left Out in 2022</h2>
<p>An individual bought a plot in Tax Year 2022 for Rs 4,000,000 from savings that were already declared, but did not list the plot. Savings in the 2022 statement were reduced, so the reconciliation balanced only by showing Rs 4,000,000 of household expenses that never happened. Every later statement then omits the plot. The fix: revise the 2022 wealth statement to show the plot and correct expenses, then revise 2023 to 2026 so the plot appears each year. No return revision is needed if no income arose from the plot; if it was rented out, the rent must be declared through revised returns. The figures are illustrative.</p>

<h2 id="risk">What Happens If You Leave It</h2>
<p>Under Section 111, where a person owns money, an investment or a valuable article, or has incurred expenditure, and offers no explanation, or an explanation the Commissioner finds unsatisfactory, the amount can be included in income as income from other sources. Once a 122(9) notice arrives, the voluntary route under Section 116(3) is closed for that year, and penalties under Section 114(6A) rise to 50% of those leviable if a return is revised after the show cause notice. See our guide to {a(B['pen'], 'revising before a notice')}.</p>
<p>For the latest year, our guide to {a(X['wsm'], 'wealth statement mismatches discovered after filing')} covers the correction window, and our {a(X['rec'], 'reconciliation fix guide')} (Roman Urdu) explains how to make a reconciliation balance.</p>
""",
    faqs=[
        ("How many years back can FBR amend my assessment?",
         "Under Section 122(2), not after five years from the end of the financial year in which the assessment was issued or treated as issued, usually when the return was filed."),
        ("Until when can I revise an old wealth statement?",
         "Under Section 116(3), any time before you receive a notice under Section 122(9) for that tax year."),
        ("Is there a 60-day limit for revising a wealth statement?",
         "No. The 60-day rule applies to return revision without approval. Wealth statement revision is available until a 122(9) notice for that year."),
        ("Do I have to revise every year after the error?",
         "Usually yes, because each year's closing wealth is the next year's opening wealth. Fix the earliest year first and carry the figures forward."),
        ("Does revising a wealth statement mean paying more tax?",
         "Not always. If the change only corrects how already declared money was used, no tax may arise. If it reveals undeclared income, the return must be revised and the tax paid."),
        ("Can FBR reject my revised wealth statement?",
         "The Commissioner can declare it void by written order if it is not to correct a bona fide omission or wrong statement."),
        ("What if I already received a notice?",
         "The voluntary route under Section 116(3) is closed for that year; reply to the notice and consider the options in Section 114(6A)."),
        ("Which years matter most in 2026?",
         "Roughly Tax Years 2021 to 2026, depending on when each return was filed."),
    ],
    sources=[S_ITO, S_IRIS],
    related=[(B["miss"], "Assets People Leave Out"), (B["pen"], "Revise Before a Notice"), (X["wsm"], "Wealth Mismatch After Filing")],
    cta_h="Fix the Chain Before FBR Asks",
    cta_p="We review five years of statements and correct them in the right order.",
    wa_text="Assalam o Alaikum, mujhe pichhle 5 saal ki wealth statements check aur revise karwani hain.",
)

# ───────────────────────────── 3. Penalty relief 114(6A) ─────────────────────────────
PEN = dict(
    slug=SL["pen"],
    svc=dict(h2="Act Before the Notice Does", intro="The difference between a voluntary revision and one after a show cause notice can be half the leviable penalties. We work out what is short, prepare the revision, and file it while relief is at its best.",
             hook="Know your return is wrong but no notice yet?", fee="Fixed fee confirmed before we start; notice response from Rs 5,000 as published.", btn="Revise before a notice",
             items=["A confidential review of what was left out and the tax short paid", "Default surcharge worked out to the date of payment", "Revised return, wealth statement and reasons prepared", "Filing and payment before any audit or 122(9) notice", "If a notice has already arrived, the reply and settlement options"],
             risks=["After audit findings, 25% of the leviable penalties is added", "After a 122(9) show cause notice, 50% of the leviable penalties is added", "Unexplained assets can be taxed in full under Section 111"]),
    title="Revise Before a Notice: Penalty Relief Under Section 114(6A)",
    h1="Revising Your Return Before FBR Sends a Notice: How Section 114(6A) Removes or Reduces Penalties",
    crumb="Revise Before a Notice (114(6A))",
    description="Section 114(6A): revise before an audit or 122(9) notice and pay no penalty; 25% after audit findings, 50% after a show cause notice. Worked examples.",
    keywords="section 114(6A) revised return penalty, revise return before notice no penalty, 122(9) show cause notice revised return, FBR voluntary disclosure revised return, default surcharge revised return",
    category="Return Revision",
    icon="🛡️",
    read="11 min read",
    banner="Under Section 114(6A), the timing of a revised return decides the penalty: none if you act first, a quarter after audit findings, half after a show cause notice.",
    tldr=("Section 114(6A) of the Income Tax Ordinance gives a strong reason to correct a return early. If a taxpayer voluntarily files a revised return with the tax "
          "short paid and default surcharge before receiving a notice under Section 177 (audit) or Section 122(9), no penalty is recovered. If the tax is pointed out "
          "by the Commissioner during audit or before a 122(9) notice, the taxpayer pays the tax, default surcharge and 25% of the leviable penalties. After a show "
          "cause notice under Section 122(9), it is the tax, default surcharge and 50% of the penalties, and the notice then abates. Separately, Section 114(6B) lets "
          "a taxpayer who accepts a settlement from FBR's algorithmic settlement mechanism revise without approval and without separate penalty or surcharge."),
    lead=("Many people know their return has a problem, an undeclared property, rent or bank profit, but wait to see whether FBR notices. The law makes waiting "
          "expensive. This guide explains the three stages in Section 114(6A), what you pay at each, and how to use the voluntary stage while it is still open."),
    body=f"""
{SERIES}

<h2 id="three-stages">The Three Stages and What Each Costs</h2>
{PEN_TABLE}
<p>"Leviable penalties" means the penalties that could be imposed under the Ordinance for the default, for example for concealment or for incorrect particulars. The relief is applied to those amounts, which is why the stage you are at changes the total so much.</p>

<h2 id="stage-one">Stage One: Voluntary Revision</h2>
<p>To qualify for full penalty relief you must:</p>
<ol>
<li>File the revised return <strong>voluntarily</strong>, whenever the error comes to your notice.</li>
<li>Deposit the <strong>tax short paid</strong>, or the tax sought to be evaded, with the revised return.</li>
<li>Deposit the <strong>default surcharge</strong> on that tax.</li>
<li>Do it <strong>before</strong> you receive a notice under Section 177 or Section 122(9).</li>
</ol>
<p>The revised return must still meet the conditions in Section 114(6): written reasons, revised accounts where relevant, and Commissioner approval unless you are within 60 days of filing, approval is deemed granted, or your declared income is increasing. Because you are increasing income, the approval is deemed granted under the proviso for income above the Section 120 assessment.</p>

<h2 id="default-surcharge">Working Out Default Surcharge</h2>
<p>Default surcharge under Section 205 runs on tax not paid by its due date, at the rate set in that section (for most taxes, the higher of 12% a year or KIBOR plus 3%), for the period of default. Calculate it to the day you pay, and pay it with the tax, because Section 114(6A) relief depends on both being deposited.</p>

<h2 id="example">Worked Example</h2>
<p>A taxpayer failed to declare rental income of Rs 1,200,000 in Tax Year 2025, giving tax short paid of Rs 180,000 (illustrative). Consider three paths:</p>
{table(["Path", "Pays", "Note"], [
    ["Revises voluntarily in November 2026", "Rs 180,000 tax + default surcharge", "No penalty recovered"],
    ["Revises after the officer points it out in audit", "Rs 180,000 + default surcharge + 25% of leviable penalties", "Relief reduced"],
    ["Revises after a 122(9) show cause notice", "Rs 180,000 + default surcharge + 50% of leviable penalties", "Notice abates"],
    ["Does nothing", "Tax as assessed, default surcharge and the full penalties, plus the time and cost of proceedings", "Worst outcome"],
])}

<h2 id="algorithmic">Section 114(6B): FBR's Algorithmic Settlement Offers</h2>
<p>If FBR's algorithmic settlement mechanism offers you a settlement and you accept it, Section 114(6B) lets you file a revised return without the Commissioner's approval. You pay the tax determined by the mechanism, no separate penalty or default surcharge is payable, and the return must be accompanied by the documents required under Section 114(6). Check any such offer carefully against your records before accepting.</p>

<h2 id="wealth">Wealth Statements in the Same Exercise</h2>
<p>A revision that adds income almost always changes the wealth statement. Section 116(3) allows a revised wealth statement with a revised reconciliation and reasons before a 122(9) notice for that year. File both together so they tell the same story.</p>

<h2 id="unexplained">Why Waiting Is Riskier for Assets</h2>
<p>Undeclared property, vehicles or bank balances are not only an income problem. Under Section 111, money, investments or valuable articles with no satisfactory explanation of their source can be included in income as income from other sources. Declaring them voluntarily, with an explanation of where the money came from, keeps control of the explanation with you.</p>

<h2 id="steps">A Safe Sequence</h2>
<ol>
<li>List what was left out, by year, with documents.</li>
<li>Recompute the tax for each affected year and the default surcharge to the planned payment date.</li>
<li>Prepare revised returns, revised wealth statements and written reasons.</li>
<li>Pay the tax and surcharge.</li>
<li>File the revisions on IRIS and keep the acknowledgements and payment proof.</li>
</ol>
<p>For the 60-day window on the latest return, see our {a(B['r60'], 'Tax Year 2026 revision guide')}; for older years, see {a(B['ws5'], 'revising the last five years')}.</p>
""",
    faqs=[
        ("Is there a penalty if I revise my return voluntarily?",
         "No, if you file the revised return with the tax short paid and default surcharge before receiving a notice under Section 177 or 122(9), under Section 114(6A)."),
        ("What if the error is found during an audit?",
         "If you deposit the tax pointed out during audit, or before a 122(9) notice, you pay the tax, default surcharge and 25% of the leviable penalties."),
        ("What if I already received a 122(9) show cause notice?",
         "You can still revise, paying the tax, default surcharge and 50% of the leviable penalties; the show cause notice then abates."),
        ("Do I need the Commissioner's approval to revise and pay more tax?",
         "Approval is deemed granted when the revised taxable income is more than the amount assessed under Section 120, and is not needed within 60 days of the original filing."),
        ("What is the algorithmic settlement mechanism?",
         "Under Section 114(6B), if you accept a settlement offered by FBR's algorithmic mechanism, you can revise without approval and pay the tax determined, with no separate penalty or default surcharge."),
        ("Does default surcharge still apply on a voluntary revision?",
         "Yes. Section 114(6A) relief requires the tax and the default surcharge to be deposited with the revised return."),
        ("Should I revise my wealth statement as well?",
         "Usually yes. Section 116(3) allows a revised wealth statement before a 122(9) notice for that year."),
    ],
    sources=[S_ITO, S_IRIS],
    related=[(B["r60"], "TY2026 Revised Return"), (B["ws5"], "Wealth Statements: Last 5 Years"), (X["notice"], "FBR Notice Defence")],
    cta_h="The Cheapest Time to Fix It Is Now",
    cta_p="Revise before a notice and no penalty is recovered. We prepare it confidentially.",
    wa_text="Assalam o Alaikum, meri return mein kuch cheezein reh gayi hain. Notice aane se pehle revise karwani hai.",
)

# ───────────────────────────── 4. Refund / credits ─────────────────────────────
REF = dict(
    slug=SL["ref"],
    svc=dict(h2="Recover the Tax You Overpaid", intro="Most people who overpay never claim it. We find the credits you missed, revise the return, and apply for the refund within the time limit.",
             hook="Paid more tax than you owe?", fee="Refund claim 10% of the refund, as published; revision fee confirmed before we start.", btn="Check my refund",
             items=["A check of every withholding certificate and statement on IRIS against your return", "Revised return claiming the missed credits", "The refund application within the Section 170 time limit", "Follow-up until the refund is processed or adjusted"],
             risks=["Refund applications are time-barred after three years under Section 170", "Credits not claimed in the return are lost"]),
    title="Revised Return to Claim a Refund or Missed Tax Credits (2026)",
    h1="Using a Revised Return to Claim Missed Tax Credits and a Refund: What the Law Allows and the Time Limits",
    crumb="Refunds & Missed Credits",
    description="Missed adjustable tax in your return? How to revise to claim it, how Section 170 refunds work, the three-year limit, and the documents you need.",
    keywords="revised return refund Pakistan, claim missed tax credit revised return, section 170 refund time limit, adjustable withholding tax claim return, FBR refund application 2026",
    category="Return Revision",
    icon="💰",
    read="10 min read",
    banner="Tax deducted from you during the year is often adjustable. If it was not claimed in your return, a revision can bring it back, within the law's time limits.",
    tldr=("If your return did not claim adjustable tax deducted or collected from you during the year, or overstated income, you may have overpaid. Section 114(6) "
          "allows a revised return to correct it (without approval within 60 days of filing). Section 170 then lets a taxpayer who has paid tax in excess of the "
          "amount properly chargeable apply for a refund, in the prescribed form, within three years of the later of the date the assessment order was issued (or "
          "treated as issued) or the date the tax was paid. The Commissioner first applies any excess against other tax due before refunding the balance."),
    lead=("Banks, utility companies, vehicle registration offices and employers deduct or collect tax at source throughout the year. Some of it is adjustable, meaning "
          "it counts towards your final tax. When those credits are left out of a return, the result is tax paid twice. This guide explains how to recover it."),
    body=f"""
{SERIES}

<h2 id="adjustable">Adjustable vs. Final: The Key Difference</h2>
<p>Tax deducted at source falls into two broad groups. <strong>Adjustable</strong> tax is a payment towards your final liability and is claimed as a credit in your return. <strong>Final</strong> or minimum tax discharges the liability on that income and cannot be claimed back as a credit. Whether a particular deduction is adjustable depends on the section under which it was deducted and your status; the IRIS statement and the deduction certificate show the section.</p>

<h2 id="common-missed">Credits People Commonly Miss</h2>
{table(["Source", "Where to find the evidence"], [
    ["Tax on salary deducted by the employer", "Employer's certificate; IRIS statement"],
    ["Tax deducted on bank profit, where adjustable for your income level", "Bank's annual tax certificate"],
    ["Tax collected on electricity and mobile bills, where adjustable", "Bills and IRIS statements"],
    ["Tax collected on vehicle registration or token tax, where adjustable", "Registration and token receipts"],
    ["Tax deducted by customers or clients on your receipts", "Their withholding certificates; IRIS statement"],
    ["Advance tax paid in instalments", "Paid challans (CPRs)"],
])}
<p>IRIS shows many of the deductions reported against your CNIC. Compare that list with the credits in your filed return line by line.</p>

<h2 id="revise">Step 1: Revise the Return</h2>
<p>Under Section 114(6), you may revise when you discover an omission or wrong statement. Within 60 days of filing the original return, no approval is needed; after that, the Commissioner's approval is required, deemed granted if no order is made within 60 days of the request, and to be granted for a bona fide omission. Attach written reasons, such as "adjustable tax deducted on electricity bills under the relevant section was not claimed", and the supporting certificates.</p>

<h2 id="refund">Step 2: Apply for the Refund</h2>
{table(["Rule (Section 170)", "Detail"], [
    ["Who can apply", "A taxpayer who has paid tax in excess of the amount properly chargeable"],
    ["How", "In the prescribed form, verified in the prescribed manner"],
    ["Time limit", "Within three years of the later of: the date the Commissioner issued (or is treated as issuing) the assessment order for that year, or the date the tax was paid"],
    ["What happens", "The Commissioner applies the excess against other tax due from you, then refunds any balance"],
])}

<h2 id="example">Example</h2>
<p>A salaried individual's Tax Year 2026 return showed tax chargeable of Rs 250,000 and claimed the employer's deduction of Rs 250,000. Missing from the return: adjustable tax of Rs 40,000 collected on the year's electricity bills and Rs 15,000 deducted on bank profit that was adjustable at that income level. A revised return within 60 days claims Rs 55,000 of additional credits, showing an excess of Rs 55,000, and a refund application follows. The figures are illustrative.</p>

<h2 id="older">Older Years</h2>
<p>Section 170's three-year limit runs from the later of the assessment date or the payment date. A return filed in late 2023 for Tax Year 2023 is treated as an assessment on the filing date, so a refund application for that year would need to be made by late 2026. Older years may already be time-barred. Revising a return for an old year solely to claim credits needs the Commissioner's approval because the 60 days have long passed.</p>

<h2 id="pitfalls">Pitfalls</h2>
<ul>
<li>Claiming final tax as a credit. It will be disallowed.</li>
<li>Claiming a deduction certified to someone else's CNIC.</li>
<li>Claiming credits without the certificate or statement to prove them.</li>
<li>Letting the three-year limit run out.</li>
<li>Forgetting that the excess may first be adjusted against other tax you owe.</li>
</ul>
<p>Our {a(X['refund'], 'tax refund guide')} explains the refund process more broadly.</p>
""",
    faqs=[
        ("Can I revise my return to claim tax credits I missed?",
         "Yes. Section 114(6) allows a revised return to correct an omission. Within 60 days of filing no approval is needed."),
        ("What is the time limit for a refund application?",
         "Under Section 170, three years from the later of the date the assessment order was issued or treated as issued, or the date the tax was paid."),
        ("Can every tax deducted from me be claimed?",
         "No. Only adjustable tax is a credit. Final or minimum tax discharges the liability on that income and cannot be claimed back."),
        ("How do I find what was deducted from me?",
         "Check the deduction statements on IRIS against your CNIC and collect certificates from the bank, employer or other withholding agents."),
        ("Will FBR pay the refund in cash?",
         "The Commissioner first applies the excess against any other tax due from you and then refunds the balance."),
        ("What do you charge to claim a refund?",
         "Our published fee for a refund claim is 10% of the refund; any revision fee is confirmed before we start."),
    ],
    sources=[S_ITO, S_IRIS],
    related=[(B["r60"], "TY2026 Revised Return"), (X["refund"], "Tax Refund Guide"), (B["sal"], "Salaried Revised Return")],
    cta_h="Don't Leave Your Refund With FBR",
    cta_p="We find missed credits, revise the return and claim the refund in time.",
    wa_text="Assalam o Alaikum, lagta hai maine zyada tax diya hai. Refund aur missed credits check karwane hain.",
)

# ───────────────────────────── 5. Missing assets ─────────────────────────────
MISS = dict(
    slug=SL["miss"],
    svc=dict(h2="Let Us Find What Your Statement Is Missing", intro="We compare your wealth statement with the records FBR is likely to hold and add what is missing, with the source of funds explained.",
             hook="Not sure your wealth statement is complete?", fee="Wealth statement Rs 2,000 as published; revision of earlier years quoted before we start.", btn="Check my wealth statement",
             items=["An asset-by-asset review against bank, property and vehicle records", "Revised wealth statement and reconciliation that balance", "The source of each newly added asset documented", "Earlier years corrected in order where the asset goes back further"],
             risks=["Unexplained assets can be added to income under Section 111", "The voluntary route closes once a 122(9) notice arrives"]),
    title="Assets Missing From Your Wealth Statement: How to Add Them",
    h1="Assets Commonly Missing From Wealth Statements in Pakistan, and How to Add Them Correctly",
    crumb="Assets Left Out of Wealth Statements",
    description="The assets most often left out of wealth statements, from plots and cars to gold, cash, loans given and foreign accounts, and how to add them correctly.",
    keywords="assets missing wealth statement, add property to wealth statement, gold in wealth statement Pakistan, foreign assets wealth statement, loan given wealth statement, section 116 assets",
    category="Wealth Statement",
    icon="🔍",
    read="11 min read",
    banner="Section 116 requires all assets and liabilities, including foreign ones, and those of dependents. Most problems come from a few assets people simply forget.",
    tldr=("Section 116 requires a wealth statement to show the person's total assets and liabilities, including foreign assets and liabilities, the assets of a "
          "dependent spouse, minor children and other dependents, assets transferred to others during the year with the consideration, and personal expenditure. "
          "The assets most often left out are plots and files, vehicles, gold, cash, bank and savings accounts, prize bonds and certificates, loans given, business "
          "capital and foreign accounts. Missing assets can be added by a revised wealth statement under Section 116(3) before a 122(9) notice; unexplained assets can "
          "otherwise be taxed under Section 111."),
    lead=("A wealth statement does not need to be complicated, but it must be complete. FBR increasingly receives information from banks, property registrars, "
          "vehicle registration authorities and other sources. This guide goes asset by asset through what people commonly leave out, how to value it, and how to "
          "add it properly."),
    body=f"""
{SERIES}

<h2 id="what-law">What Section 116 Requires</h2>
<ul>
<li>Your total <strong>assets and liabilities</strong>, including foreign assets and liabilities, as on the date specified (30 June for the annual statement).</li>
<li>Assets and liabilities of your <strong>spouse, minor children and other dependents</strong>; a spouse's assets only if the spouse is dependent.</li>
<li><strong>Assets transferred</strong> by you to any other person during the period, and the consideration received.</li>
<li>Your <strong>personal expenditure</strong> and that of your dependents.</li>
<li>The <strong>wealth reconciliation statement</strong>.</li>
</ul>

<h2 id="checklist">The Assets Most Often Left Out</h2>
{table(["Asset", "Why it gets missed", "How to show it"], [
    ["Plots, files and allotments (including instalment plans)", "Not yet transferred or still being paid", "At cost paid to date, with the remaining instalments shown as a commitment where relevant"],
    ["House or flat in a family member's name but paid by you", "Treated as 'family property'", "If you paid for it and own it, it is yours; if it was a gift to someone else, show the transfer"],
    ["Vehicles", "Registered in another name, or 'open letter'", "Show vehicles you own at cost, with the registration details"],
    ["Gold and jewellery", "Received at marriage or inherited", "Show the weight and value; explain the source (gift, inheritance)"],
    ["Cash at home or in the business", "Seen as everyday money", "Show the closing cash realistically and consistently with your records"],
    ["Bank and savings accounts, including dormant ones", "Small or forgotten accounts", "Show every account with its 30 June balance"],
    ["Prize bonds, savings certificates, shares, mutual funds", "Treated as savings, not assets", "Show at cost with identifying details"],
    ["Loans given to relatives or friends", "Informal, not documented", "Show as a receivable, with the borrower's name"],
    ["Business capital", "Kept 'separate' from personal wealth", "A sole proprietor's business assets less liabilities are personal wealth"],
    ["Foreign bank accounts and property", "Thought to be outside Pakistan's scope", "The law specifically includes foreign assets and liabilities"],
])}
<p>Sole proprietors should also read our guide to {a(X['sole_ws'], 'the sole proprietor wealth statement')}.</p>

<h2 id="liabilities">Liabilities People Forget</h2>
<ul>
<li>Bank loans, car financing and credit card balances.</li>
<li>Loans from relatives, which should be documented.</li>
<li>Advances received against a sale not yet completed.</li>
</ul>
<p>Forgetting a liability overstates your wealth and can create an apparent gap that you then have to explain.</p>

<h2 id="source">Adding an Asset Means Explaining Its Source</h2>
<p>Every asset added must be explained by money that was already declared or by a new, documented source: savings in an earlier statement, a gift (with the giver's details), inheritance (with succession documents), a loan (with the lender's details), or income. If the source is income that was not declared, the return for that year must also be revised and the tax paid. Under Section 111, an asset with no satisfactory explanation of its source can be included in income as income from other sources.</p>

<h2 id="when-acquired">When Was It Acquired?</h2>
<p>If the asset was acquired in an earlier year, the correction usually starts in that year and carries forward, because each closing statement is the next opening statement. FBR can amend assessments for up to five years under Section 122(2), so the years from about Tax Year 2021 onwards are the ones to review. See our guide to {a(B['ws5'], 'revising the last five years')}.</p>

<h2 id="how">How to Add a Missing Asset</h2>
<ol>
<li>Identify the year the asset was acquired and its cost.</li>
<li>Collect evidence: purchase deed, transfer letter, payment records, gift or inheritance papers.</li>
<li>Revise the wealth statement for that year under Section 116(3), with a revised reconciliation and written reasons, before any 122(9) notice for that year.</li>
<li>Revise later years so the asset appears each year until disposed of.</li>
<li>If income arose from it (rent, profit), revise the return for those years too.</li>
</ol>
<p>For the most recent year, our guide to {a(B['r60'], 'the Tax Year 2026 revision window')} explains the 60-day rule for returns.</p>
""",
    faqs=[
        ("Do I need to show my wife's assets in my wealth statement?",
         "Only if she is dependent on you. Assets of a dependent spouse, minor children and other dependents are included."),
        ("Do foreign bank accounts go in the wealth statement?",
         "Yes. Section 116 expressly includes foreign assets and foreign liabilities."),
        ("How do I show a plot I am still paying instalments on?",
         "Show it at the amount paid to date, and keep the allotment and payment records."),
        ("Should gold received at marriage be shown?",
         "Yes, with its weight, value and source, such as a gift or inheritance."),
        ("Do loans I gave to relatives count?",
         "Yes. Money lent is an asset (a receivable) and should be shown with the borrower's name."),
        ("What happens if I add an asset I cannot explain?",
         "Under Section 111, an asset whose source is not satisfactorily explained can be included in income as income from other sources."),
        ("Can I add a missing asset without revising the return?",
         "Yes, if it was bought from already declared money. If its source was undeclared income, the return must also be revised."),
    ],
    sources=[S_ITO, S_IRIS],
    related=[(B["ws5"], "Wealth Statements: Last 5 Years"), (X["wsg"], "Wealth Statement Guide"), (X["sole_ws"], "Sole Proprietor Wealth Statement")],
    cta_h="Make Your Wealth Statement Complete",
    cta_p="We add what is missing, explain the source, and correct earlier years in order.",
    wa_text="Assalam o Alaikum, meri wealth statement mein kuch assets reh gaye hain. Add aur revise karwane hain.",
)

# ───────────────────────────── 6. Salaried ─────────────────────────────
SAL = dict(
    slug=SL["sal"],
    svc=dict(h2="Let Us Revise Your Salaried Return", intro="Salaried returns look simple, but most errors sit in the wealth statement and the credits. We check both and revise within the 60-day window where possible.",
             hook="Salaried and unsure your 2026 return is right?", fee="Salaried return Rs 3,500 as published; revision fee confirmed before we start.", btn="Revise my salaried return",
             items=["Salary, allowances and tax checked against the employer's certificate", "Other income added: bank profit, rent, freelance, pension", "Every adjustable credit claimed", "Wealth statement and reconciliation corrected", "Filing on IRIS within the 60-day window where possible"],
             risks=["Undeclared side income can lead to notices and penalties", "Missed credits mean tax paid twice"]),
    title="Salaried Revised Return Tax Year 2026: Common Fixes",
    h1="Revised Return for Salaried People, Tax Year 2026: The Errors We See Most and How to Correct Them",
    crumb="Salaried Revised Return 2026",
    description="Salaried and need to fix your 2026 return? Common errors, from employer certificates to side income and wealth statements, and how to revise in 60 days.",
    keywords="salaried revised return 2026, revise salary tax return Pakistan, employer tax certificate mismatch, salaried wealth statement revise, salaried person bank profit return",
    category="Return Revision",
    icon="💼",
    read="10 min read",
    banner="Salaried returns are not as simple as they look. Most errors sit in other income, tax credits and the wealth statement, and all can be revised.",
    tldr=("A salaried person's Tax Year 2026 return can be revised under Section 114(6) when an omission or wrong statement is discovered, without the Commissioner's "
          "approval if filed within 60 days of the original. The most common errors are figures that do not match the employer's certificate, bank profit or rent "
          "left out, freelance or side income omitted, adjustable credits not claimed, and wealth statements that do not reconcile with take-home pay and household "
          "spending. If the revision increases tax, filing voluntarily with the tax and default surcharge before a notice means no penalty under Section 114(6A)."),
    lead=("Salaried people are often told their tax is 'already deducted', so the return does not matter. The deduction covers the salary, but the return also "
          "covers other income, credits and a wealth statement, and that is where problems start. This guide lists the errors we correct most often in salaried "
          "returns and how to fix each."),
    body=f"""
{SERIES}

<h2 id="errors">The Errors We See Most</h2>
{table(["Error", "Why it matters", "Fix"], [
    ["Salary or tax differs from the employer's certificate", "FBR receives the employer's statement; mismatches attract questions", "Use the certificate figures; ask HR to correct the certificate if it is wrong"],
    ["Bank profit left out", "Banks report profit and tax deducted", "Declare it and claim the tax deducted where adjustable"],
    ["Rent from a property left out", "Property and rent data can be matched", "Declare the rent and the tax deducted by the tenant, if any"],
    ["Freelance or side income omitted", "Foreign remittances and platform payments leave a bank trail", "Declare it under the correct head"],
    ["Adjustable credits not claimed", "Tax paid twice", "Claim with certificates; see the refund guide"],
    ["Wealth reconciliation forced to balance", "Unrealistic household spending is a common trigger", "Rebuild it from take-home pay and real spending"],
    ["Spouse's or children's assets mishandled", "Dependents' assets must be included", "Include dependents' assets; a spouse only if dependent"],
])}

<h2 id="certificate">Matching the Employer's Certificate</h2>
<p>Your employer deducts tax under Section 149 and reports it. The return should show gross salary, taxable allowances and the tax deducted exactly as on the certificate. If the certificate itself is wrong, for example a bonus missing or tax under-deducted, ask the employer to correct it before you revise, so the figures match FBR's records.</p>

<h2 id="other-income">Other Income Salaried People Forget</h2>
<ul>
<li><strong>Profit on bank deposits and savings certificates.</strong> Declare it; the tax deducted may be final or adjustable depending on the rules for your level of income.</li>
<li><strong>Rent</strong> from a house, portion or shop.</li>
<li><strong>Freelance, consultancy or tutoring income</strong> received alongside the job.</li>
<li><strong>Capital gains</strong> on property, shares or mutual funds sold during the year.</li>
<li><strong>Pension or income from a previous employer</strong> in the same year.</li>
</ul>

<h2 id="wealth">The Salaried Wealth Statement</h2>
<p>For most salaried people the reconciliation is simple: opening wealth plus take-home salary, plus any other income and inflows, less household spending, equals closing wealth. Problems arise when a car, plot or gold is bought but not shown, or when household spending is set unrealistically to make the numbers fit. Correct the assets and set spending to a realistic figure supported by your actual life: rent, school fees, utilities, travel. Our guide to {a(B['miss'], 'assets people leave out')} lists what to check.</p>

<h2 id="how">How to Revise, Step by Step</h2>
<ol>
<li>Check the filing date on your IRIS acknowledgement; within 60 days, no approval is needed.</li>
<li>Collect the employer's certificate, bank certificates, rent records and any other income documents.</li>
<li>Correct income, credits and the wealth statement; prepare the revised reconciliation.</li>
<li>Write short, signed reasons for each change.</li>
<li>Pay any additional tax with default surcharge before filing.</li>
<li>File the revised return and wealth statement on IRIS; keep the acknowledgements.</li>
</ol>

<h2 id="increase-or-refund">If Tax Goes Up, or Down</h2>
<p>If tax increases, filing the revision voluntarily with the tax and default surcharge before any notice under Section 177 or 122(9) means no penalty is recovered, under Section 114(6A). If tax goes down because credits were missed, a refund can be claimed under Section 170 within three years; see our guide to {a(B['ref'], 'refunds and missed credits')}.</p>

<h2 id="late">If You Have Missed the 60 Days</h2>
<p>Revision needs the Commissioner's approval, which is deemed granted if no written order is made within 60 days of your request, or if the revision increases your declared income. For a broader view of post-deadline corrections, see our guide to {a(X['rpd'], 'correcting a rushed filing after the deadline')}.</p>
""",
    faqs=[
        ("My employer deducted all my tax. Do I still need to revise a wrong return?",
         "Yes. The return also covers other income, credits and your wealth statement. An error in any of them can be corrected by a revised return under Section 114(6)."),
        ("My employer's certificate is wrong. What should I do?",
         "Ask the employer to correct it first, so your revised return matches the figures FBR receives."),
        ("Do I need to declare bank profit if tax was deducted?",
         "Yes. Declare the profit and the tax deducted; whether that tax is final or adjustable depends on the rules for your level of income."),
        ("I forgot to show the car I bought. Do I need to revise?",
         "Yes, revise the wealth statement to show it and explain how it was paid for. If the money came from undeclared income, revise the return too."),
        ("How long do I have to revise without approval?",
         "Sixty days from the date you filed the original return."),
        ("What does a salaried return cost with you?",
         "Our published fee for a salaried return is Rs 3,500; any revision fee is confirmed before we start."),
    ],
    sources=[S_ITO, S_IRIS],
    related=[(B["r60"], "TY2026 Revised Return"), (B["ref"], "Refunds & Missed Credits"), (B["miss"], "Assets People Leave Out")],
    cta_h="Salaried? Get Your Return Right",
    cta_p="We check the certificate, other income, credits and the wealth statement, then revise.",
    wa_text="Assalam o Alaikum, main salaried hoon. Meri 2026 ki return mein ghalti hai, revise karwani hai.",
)

POSTS = [R60, WS5, PEN, REF, MISS, SAL]
