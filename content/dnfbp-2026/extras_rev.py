"""Depth for the revision series (posts6). Same verified sections as posts6 (ITO amended to 30.06.2026)."""
from posts import a, table

EXTRA = {}

EXTRA["revised-return-tax-year-2026-60-days-pakistan"] = ("""
<h2 id="not-revision">When You Do Not Need a Revision</h2>
<ul>
<li><strong>You have not filed yet.</strong> A return filed for the first time after 31 October 2026 is a late return, not a revision; late filing has its own consequences under Sections 182 and 182A.</li>
<li><strong>The difference is a typing error with no effect on income, tax or wealth.</strong> Keep a note on file; a revision is not always worth it.</li>
<li><strong>FBR has already amended your assessment.</strong> Section 114(6)(c) bars a revised return that declares less than the income determined by such an order; respond to the order instead.</li>
</ul>

<h2 id="reasons">Writing the Reasons Properly</h2>
<p>Section 114(6)(b) requires the reasons, in writing and signed by you. Good reasons are short, specific and verifiable: "Profit of Rs 85,000 on a savings account at [bank] and the tax deducted on it were omitted; bank certificate attached." Vague reasons such as "some corrections" invite questions and do not show a bona fide omission, which is the test the Commissioner applies when approval is needed.</p>
""", [
    ("Is a return filed after 31 October 2026 a revised return?",
     "No. A first return filed after the due date is a late return. A revised return corrects a return you have already filed."),
    ("What should the written reasons say?",
     "Each change, why it was missed and the document that supports it, signed by you, as Section 114(6)(b) requires."),
])

EXTRA["revise-wealth-statement-last-5-years-pakistan"] = ("""
<h2 id="evidence">Evidence for Each Type of Correction</h2>
""" + table(["Correction", "Evidence that holds up"], [
    ["Property bought but not shown", "Sale deed, transfer letter or allotment, and bank records of payment"],
    ["Vehicle not shown", "Registration book, purchase receipt, bank or finance records"],
    ["Gift received", "Gift deed or declaration from the giver, with the giver's CNIC and the bank transfer"],
    ["Inheritance", "Succession certificate or mutation, and the deceased's last wealth statement if available"],
    ["Loan from a relative", "Written acknowledgement, the bank transfer, and repayment records"],
    ["Household spending overstated to force a balance", "Realistic spending supported by rent, school, utility and travel records"],
]) + """
<h2 id="questions">Questions Officers Usually Ask About Older Years</h2>
<ul>
<li>Where did the money for this asset come from, and was that source declared?</li>
<li>Why does this year's opening wealth differ from last year's closing wealth?</li>
<li>Why did household spending change sharply from one year to the next?</li>
<li>Who owns the asset registered in a family member's name?</li>
</ul>
<p>A revision that answers these questions in advance, with documents, is the strongest position you can be in.</p>
""", [
    ("What evidence do I need to add an old property?",
     "The sale deed, transfer letter or allotment, and bank records showing how it was paid for."),
    ("Can I correct household spending in an old statement?",
     "Yes, through a revised wealth statement under Section 116(3) before a 122(9) notice, with realistic figures you can support."),
])

EXTRA["revised-return-before-notice-penalty-relief-section-114-6a"] = ("""
<h2 id="voluntary">What Counts as "Voluntary"?</h2>
<p>Section 114(6A) gives full relief when the revised return is filed voluntarily, before a notice under Section 177 or 122(9). In practice, a revision filed on your own initiative, before any audit selection notice or show cause notice for that year, is the voluntary stage. Other letters, such as a notice asking you to file a return or a general information request, are not the notices named in the section; but once FBR has started asking about the same issue, act quickly, because the next step may be one of the named notices.</p>

<h2 id="audit-vs-122-9">Audit and 122(9) Notices in Brief</h2>
""" + table(["Notice", "What it is", "Effect on relief"], [
    ["Section 177", "Selection for audit of your income tax affairs", "Once received, the no-penalty stage has passed"],
    ["Section 122(9)", "Show cause notice before amending an assessment", "Revision after it requires 50% of leviable penalties"],
]) + """
<h2 id="documents">Documents to Assemble</h2>
<ul>
<li>The original return and wealth statement for each year affected.</li>
<li>Evidence of the omitted income or asset: bank statements, deeds, tenancy agreements, invoices.</li>
<li>Computation of the tax short paid and the default surcharge to the payment date.</li>
<li>Paid challans for the tax and surcharge.</li>
<li>Signed reasons for each revision.</li>
</ul>

<h2 id="mistakes">Mistakes That Lose the Relief</h2>
<ul>
<li>Filing the revised return but not paying the tax and surcharge with it.</li>
<li>Paying the tax but leaving out the default surcharge.</li>
<li>Waiting until an audit or show cause notice has been received.</li>
<li>Revising one year but leaving the same omission in later years.</li>
<li>Filing a revised return that misses a Section 114(6) condition, which makes it invalid.</li>
</ul>
""", [
    ("Does a notice asking me to file a return stop the no-penalty relief?",
     "Section 114(6A) names notices under Section 177 and Section 122(9). Other letters are not those notices, but act quickly once FBR is asking about the same issue."),
    ("Do I have to revise all affected years?",
     "Yes. Relief applies to each revised return; leaving the same omission in later years leaves those years exposed."),
    ("What makes a revised return invalid?",
     "Missing any condition in Section 114(6), such as written reasons or required approval, makes it an invalid return."),
])

EXTRA["revised-return-claim-refund-missed-tax-credits-pakistan"] = ("""
<h2 id="iris-statements">Reading Your Deduction Statements on IRIS</h2>
<p>Withholding agents report the tax they deduct or collect against your CNIC. On IRIS you can view these statements for each tax year. For each entry, note the section under which tax was deducted, the agent, the amount and the date, then check whether that section's tax is adjustable for you. Any adjustable amount missing from your return is a candidate for revision.</p>

<h2 id="after-application">After You Apply</h2>
<p>Under Section 170(3), once the Commissioner is satisfied that tax has been overpaid, the excess is first applied in reduction of any other tax due from you under the Ordinance, and the balance is refunded. Keep your contact details and bank account current on IRIS, since refunds and correspondence depend on them, and respond promptly to any request for documents.</p>

<h2 id="old-years">Revising an Old Year to Claim Credits</h2>
<p>For a year where more than 60 days have passed since filing, the revision needs the Commissioner's approval. Apply with your reasons and the certificates; if no written order is made within 60 days of your request, approval is deemed granted. Remember the separate three-year refund limit in Section 170: there is little value in revising a year for which the refund window has already closed.</p>

<h2 id="checklist">Refund Checklist</h2>
<ul>
<li>☐ Employer's tax certificate for the year.</li>
<li>☐ Bank tax certificates for profit and any other deductions.</li>
<li>☐ Utility, mobile and vehicle tax evidence where adjustable.</li>
<li>☐ Customers' withholding certificates, if you receive business income.</li>
<li>☐ Advance tax challans.</li>
<li>☐ IRIS deduction statements printed for the year.</li>
<li>☐ Revised return filed with reasons.</li>
<li>☐ Refund application filed within three years.</li>
</ul>

<h2 id="who-benefits">Who Most Often Has a Refund</h2>
<ul>
<li>Salaried people whose employer over-deducted, or who changed jobs mid-year.</li>
<li>Households and businesses with monthly electricity bills above Rs 30,000, where the tax on the excess is adjustable under Section 235(4)(b).</li>
<li>Pensioners and others with modest income but tax deducted at source.</li>
<li>Business owners whose customers deducted more tax than the final liability.</li>
</ul>
""", [
    ("Where can I see the tax deducted from me?",
     "On IRIS, where withholding agents' statements reported against your CNIC can be viewed for each tax year."),
    ("Will FBR adjust my refund against other tax?",
     "Yes. Under Section 170(3) the excess is first applied against other tax due from you; the balance is refunded."),
    ("Is it worth revising a very old year for a refund?",
     "Only if the three-year refund window in Section 170 is still open for that year; otherwise the refund is time-barred."),
    ("I changed jobs during the year. Could I have a refund?",
     "Possibly. Two employers each deducting tax without full information can over-deduct. Compare the total deducted with the tax on your total salary."),
])

EXTRA["assets-missing-from-wealth-statement-pakistan"] = ("""
<h2 id="valuation">How to Value Assets Consistently</h2>
<p>Use the same basis every year so the statement can be followed from one year to the next. For most assets, that means the cost you actually paid, adjusted for additions such as construction or improvements, and for disposals. Do not inflate or deflate values to make a reconciliation balance; a value that jumps without a transaction is itself a question.</p>

<h2 id="inherited">Inherited Assets</h2>
<p>An inherited share in a house, land or gold is your asset from the date of inheritance. Show your share, keep the succession certificate or mutation, and explain the inflow in the reconciliation as inheritance. If the property earns rent, your share of the rent is your income.</p>

<h2 id="gifts">Gifts Within the Family</h2>
<p>Gifts are a common explanation for new assets, and a common source of questions. Record the giver's name and CNIC, the date and amount, and how it was given, ideally by bank transfer. The giver's own wealth statement should show the gift going out, as Section 116(1)(c) requires assets transferred to others, and the consideration, to be shown.</p>

<h2 id="joint">Jointly Owned Assets</h2>
<p>Where an asset is owned jointly, for example a plot bought by two brothers, each shows his own share at his share of the cost, and each explains the source of his own contribution. Showing the full value in one statement and nothing in the other is a frequent error.</p>

<h2 id="disposed">Assets Sold or Given Away During the Year</h2>
<p>An asset disposed of during the year disappears from the closing statement, but the disposal must be visible: the sale proceeds appear as an inflow in the reconciliation, and any gain may be taxable. Assets transferred to another person must be shown with the consideration received.</p>
""", [
    ("How should I value assets in the wealth statement?",
     "Use a consistent basis each year, usually the cost actually paid plus improvements, and do not adjust values to force a reconciliation."),
    ("How do I show an inherited property?",
     "Show your share from the date of inheritance, keep the succession or mutation papers, and record the inheritance in the reconciliation."),
    ("How do I show a plot owned jointly with my brother?",
     "Each owner shows his own share at his share of the cost and explains the source of his own contribution."),
    ("What if I sold an asset during the year?",
     "Remove it from the closing statement and show the sale proceeds as an inflow in the reconciliation; any gain may be taxable."),
])

EXTRA["salaried-revised-return-tax-year-2026-pakistan"] = ("""
<h2 id="two-employers">Two Employers in One Year</h2>
<p>If you changed jobs during Tax Year 2026, each employer deducted tax on the salary it paid, often without knowing about the other. The return must combine both salaries, and the tax on the total may differ from the sum of the two deductions. Collect both certificates; if tax was under-deducted, pay the balance with the revision; if over-deducted, claim the excess.</p>

<h2 id="example">A Salaried Reconciliation, Done Properly</h2>
""" + table(["Line", "Amount (illustrative)"], [
    ["Opening net wealth (from the 2025 statement)", "Rs 3,200,000"],
    ["Add take-home salary for the year", "Rs 2,600,000"],
    ["Add bank profit (net)", "Rs 90,000"],
    ["Add gift from parents (bank transfer)", "Rs 300,000"],
    ["Less household spending (rent, school, utilities, food, travel)", "(Rs 1,900,000)"],
    ["Expected closing net wealth", "Rs 4,290,000"],
]) + """
<p>The closing statement must then add up to Rs 4,290,000: for example, bank balances, a car bought during the year at its cost, and gold. If the car was left out, the closing statement would show less wealth than expected, which is usually "fixed" by inflating spending. Showing the car, and spending at its real level, makes the reconciliation honest and balanced.</p>

<h2 id="spouse">Working Spouses</h2>
<p>If your spouse has their own income, they file their own return and wealth statement. Their assets are not included in yours unless they are your dependent. Decide clearly who owns what, especially for jointly bought property and gold, and keep both statements consistent.</p>

<h2 id="allowances">Allowances and Benefits</h2>
<p>Allowances and benefits provided by the employer are generally part of salary and appear on the certificate. Check that the return shows them as the employer reported them; if a benefit was left off the certificate, ask the employer to correct it rather than adjusting the return on your own.</p>
""", [
    ("I had two employers this year. What should I check?",
     "Combine both salaries and both tax deductions. The tax on the total may differ from the two deductions added together; pay any shortfall or claim any excess."),
    ("Does my working wife's income go in my return?",
     "No. A spouse with their own income files their own return and wealth statement; their assets go in yours only if they are dependent."),
    ("How do I set household spending realistically?",
     "Build it from rent, school fees, utilities, food, travel and other regular costs you can support with records."),
    ("Should I adjust my return if a benefit is missing from my certificate?",
     "Ask your employer to correct the certificate first, so your return and the employer's statement agree."),
])
