"""Third layer: closing gaps so each sole proprietor guide is complete."""
from posts import a, table

EXTRA = {}

EXTRA["add-business-to-ntn-iris-sole-proprietor"] = ("""
<h2 id="before-submit">Before You Press Submit</h2>
<ul>
<li>☐ Business name spelled exactly as on the bank account and signboard.</li>
<li>☐ Start date matches your first invoices or rent agreement.</li>
<li>☐ Every branch listed, each with its own address.</li>
<li>☐ Business bank account number entered correctly.</li>
<li>☐ Attachments legible and in the format IRIS accepts.</li>
<li>☐ Mobile number current, so verification codes and notices reach you.</li>
</ul>
""", [
    ("Why does IRIS ask for my mobile number to be current?",
     "Verification codes and some notices are sent to it, and mobile number is one of the details FBR lets you update through Form 181."),
])

EXTRA["sole-proprietor-advance-tax-pakistan"] = (f"""
<h2 id="aop-company">How This Differs for Partnerships and Companies</h2>
<p>The (A/4) - B formula is only for individuals. Where the taxpayer is an association of persons or a company, Section 147(4) uses a turnover-based formula, (A x B/C) - D, in which the quarter's turnover is applied to the ratio of last year's assessed tax to last year's turnover, less tax paid in the quarter. AOPs and companies also have their own estimate rules under Section 147(4A). If your sole proprietorship becomes a partnership or company, the advance tax calculation changes with it.</p>
<p>For partnerships, see our guide to {a('/blogs/aop-tax-return-pakistan-2026', 'AOP tax returns')}.</p>
""", [
    ("Do partnerships use the same advance tax formula as individuals?",
     "No. AOPs and companies use the turnover-based formula in Section 147(4), not the (A/4) - B formula for individuals."),
])

EXTRA["sole-proprietor-withholding-tax-duties-pakistan"] = (f"""
<h2 id="payee-status">Why the Payee's Status Matters</h2>
<p>The First Schedule usually sets two rates for the same payment: one for persons on the Active Taxpayers List and a higher one for persons who are not. If you apply the lower rate to a supplier who is not on the list, the difference is tax you failed to deduct, and under Section 161 you can be made personally liable for it. A two-minute check of each payee's status before payment, and a note of the date you checked, protects you. Re-check regularly, because the list changes, including after late filers rejoin it.</p>
<p>For individuals' own filer status, see our {a('/atl-pakistan-guide', 'Active Taxpayers List guide')}.</p>
""", [
    ("What if a supplier was not on the Active Taxpayers List but I deducted at the lower rate?",
     "The difference is tax you failed to deduct, for which you can be held personally liable under Section 161. Check status before each payment and keep a record of the check."),
])

EXTRA["sole-proprietor-records-books-fbr-pakistan"] = (f"""
<h2 id="monthly-summary">A Simple Monthly Summary Format</h2>
<p>A one-page summary each month, built from your folder, is enough for most sole proprietors and makes the annual return far quicker:</p>
{table(["Line", "Amount", "Source"], [
    ["Sales (cash)", "From daily summaries or POS", "Sales book"],
    ["Sales (bank and online)", "From bank and marketplace statements", "Bank and settlement reports"],
    ["Purchases of stock", "From supplier invoices", "Purchase file"],
    ["Rent", "From agreement and bank", "Expense file"],
    ["Salaries", "From payroll sheet", "Payroll file"],
    ["Utilities", "From bills", "Expense file"],
    ["Other expenses", "From receipts", "Expense file"],
    ["Tax deducted from you", "From certificates and statements", "Tax file"],
    ["Owner's drawings", "From bank and cash book", "Drawings record"],
])}
<p>Twelve of these summaries, plus a stock count at 30 June, give the figures for the profit and loss account, the balance sheet items in the wealth statement, and the tax credits in the return.</p>

<h2 id="year-file">What the Annual File Should Contain</h2>
<ul>
<li>Twelve monthly folders and summaries.</li>
<li>Stock count and valuation at the year end.</li>
<li>List of business assets with purchase documents.</li>
<li>Bank statements for the full year for every business account.</li>
<li>Withholding certificates received and, if applicable, tax you deducted and deposited.</li>
<li>Advance tax challans.</li>
<li>The filed return, wealth statement and acknowledgement.</li>
<li>Any notices received and the replies sent.</li>
</ul>

<h2 id="when-help">When to Bring in Help</h2>
<p>Many owners keep records well until the business grows. Signs it is time for help: you employ staff, your rent is over Rs 1.5 million a year, you have had a notice, your turnover is approaching Rs 100 million, or your monthly summary keeps slipping. At that point a small monthly fee costs less than one disallowed expense or one Section 182 penalty.</p>
""", [
    ("Is a monthly summary enough, or do I need full books?",
     "For many sole proprietors, a monthly summary built from organised invoices, receipts and bank statements is enough to prepare a defensible return, but the law requires the underlying records to be kept for six years."),
    ("What should I keep at the year end?",
     "A stock count and valuation at 30 June, a list of business assets, full-year bank statements, tax certificates, advance tax challans and the filed return."),
])

EXTRA["close-sole-proprietorship-remove-business-ntn-pakistan"] = (f"""
<h2 id="after-timeline">What Still Applies After You Close</h2>
{table(["Obligation", "Until when"], [
    ["Return for the year of closure, with wealth statement", "By 30 September after that tax year (Section 118), unless extended"],
    ["Withholding statement for the last quarter you deducted tax", "By the 20th of the month after that quarter (Section 165)"],
    ["Replies to notices about earlier years", "Until each matter is finally decided"],
    ["Keeping records", "Six years after the end of each tax year, longer if a case is pending (Section 174)"],
    ["Returns as an individual", "Every year you have taxable income or are otherwise required to file"],
])}

<h2 id="family-questions">Questions Families Often Ask</h2>
<p><strong>Can a son or daughter take over the shop under the parent's NTN?</strong> No. The NTN belongs to the parent. The child registers the business on their own profile, and the parent discontinues it on theirs.</p>
<p><strong>Can the business be moved into a partnership with relatives?</strong> Yes, but the partnership is a new taxpayer with its own registration and returns. The sole proprietorship is then discontinued on the original owner's registration.</p>
<p><strong>What about stock taken home for family use?</strong> Stock taken for personal use at closure is part of the closing position; record it, rather than leaving it unexplained.</p>
""", [
    ("Can my child continue my shop under my NTN?",
     "No. The child registers the business on their own profile, and you discontinue it on yours."),
    ("When is the final-year return due?",
     "By 30 September after the tax year in which the business closed, under Section 118, unless FBR extends the date."),
])
