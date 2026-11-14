"""Extra depth for the sole proprietor series (facts: ITO 2001 amended to 30.06.2026; checked 10 November 2026)."""
from posts import a, table

R = "/blogs/sole-proprietorship-registration-pakistan"
I = "/blogs/add-business-to-ntn-iris-sole-proprietor"
ADV = "/blogs/sole-proprietor-advance-tax-pakistan"
W = "/blogs/sole-proprietor-withholding-tax-duties-pakistan"
REC = "/blogs/sole-proprietor-records-books-fbr-pakistan"
C = "/blogs/close-sole-proprietorship-remove-business-ntn-pakistan"
RET = "/blogs/sole-proprietor-tax-return-pakistan-2026"
NOTICE = "/fbr-notice-defense"

SLABS = table(["Taxable income (non-salaried individual, TY2027)", "Income tax"], [
    ["Up to Rs 600,000", "Nil"],
    ["Rs 600,001 to Rs 1,200,000", "15% of the amount above Rs 600,000"],
    ["Rs 1,200,001 to Rs 1,600,000", "Rs 90,000 + 20% of the amount above Rs 1,200,000"],
    ["Rs 1,600,001 to Rs 3,200,000", "Rs 170,000 + 30% of the amount above Rs 1,600,000"],
    ["Rs 3,200,001 to Rs 5,600,000", "Rs 650,000 + 40% of the amount above Rs 3,200,000"],
    ["Above Rs 5,600,000", "Rs 1,610,000 + 45% of the amount above Rs 5,600,000"],
])

EXTRA = {}

# ───────────────────────── Registration pillar ─────────────────────────
EXTRA["sole-proprietorship-registration-pakistan"] = (f"""
<h2 id="taxed">How a Sole Proprietor's Profit Is Taxed</h2>
<p>A sole proprietor's business profit is added to any other income and taxed at the rates for individuals whose income is not mainly salary. For tax year 2027 (1 July 2026 to 30 June 2027) the rates in the First Schedule are:</p>
{SLABS}
<p><strong>Worked example.</strong> A Lahore shop owner earns a business profit of Rs 2,400,000 in tax year 2027 and has no other income. Tax is Rs 170,000 plus 30% of Rs 800,000 (the amount above Rs 1,600,000), which is Rs 410,000. Adjustable tax deducted or collected during the year, for example tax on monthly electricity bills above Rs 30,000 (Section 235(4)(b)), is credited against it, and any balance is paid with the return. The figures are illustrative; the actual liability depends on the full return.</p>
<p>Because tax is charged on <em>profit</em>, not turnover, the records behind your expenses matter as much as the sales figures. Our {a(REC, 'records guide')} explains what FBR expects.</p>

<h2 id="structure">Is a Sole Proprietorship the Right Structure?</h2>
{table(["Question", "If the answer is yes", "Points to consider"], [
    ["Are you the only owner?", "A sole proprietorship fits", "Two or more owners means a partnership or AOP, or a company"],
    ["Is the business small or just starting?", "Low setup cost and simple compliance", "You can convert to a company later"],
    ["Do clients or lenders insist on a company?", "Consider a private limited company", "Some tenders and corporate clients prefer companies"],
    ["Is personal liability a concern?", "Consider a company", "A sole proprietor is personally liable for business debts"],
    ["Will profits be large?", "Compare rates before deciding", "Individuals and companies are taxed differently"],
])}
<p>For a fuller comparison, see our guide to {a('/secp-vs-sole-proprietorship-pakistan', 'SECP company versus sole proprietorship')}.</p>

<h2 id="name">Choosing and Protecting a Business Name</h2>
<p>There is no national register of sole proprietorship names, so registering the business name on IRIS does not stop someone else using it. If the name has value, consider a trademark application with IPO-Pakistan, the official intellectual property office. In any case:</p>
<ul>
<li>Use exactly the same spelling on IRIS, the bank account, the signboard, invoices and online profiles.</li>
<li>Avoid words that suggest a company or a regulated business (for example "Limited", "Bank" or "Insurance") when you are not one.</li>
<li>Check that the name is not already widely used in your trade and city, to avoid disputes later.</li>
</ul>

<h2 id="bank">Opening the Business Bank Account</h2>
<p>Banks set their own account-opening rules, but for a sole proprietorship they commonly ask for the owner's CNIC, proof of tax registration showing the business, proof of the business address, and a letter on the business letterhead describing the activity. Once the account is open, add it to your IRIS profile through Form 181 so FBR's records and the bank's match. Use the account for all business receipts and payments; mixing personal and business money makes the wealth statement and the profit figure harder to defend.</p>

<h2 id="first-year">Your First-Year Compliance Calendar</h2>
{table(["When", "What", "Why"], [
    ["Before you start trading", "IRIS registration, business added through Form 181, bank account linked", "Section 181 registration; bank and marketplace checks"],
    ["Every month", "Keep sales, purchase and expense records; pay any withholding tax you deducted", "Section 174 records; withholding duties"],
    ["Quarterly (if applicable)", "Advance tax by 15 September, December, March and June", "Section 147, once latest assessed income is Rs 1 million or more"],
    ["Quarterly (if applicable)", "Withholding statements by the 20th after each quarter", "Section 165, if you deducted tax"],
    ["By 30 September after the tax year", "Income tax return with wealth statement", "Section 118 due date for individuals, unless FBR extends it"],
])}
<p>Filing after the due date has a cost: under Section 182 the late-filing penalty is 0.1% of the tax payable for each day of default, up to 50%, with a minimum of Rs 40,000; and to be placed on the Active Taxpayers List after a late return, an individual pays a Rs 25,000 surcharge under Section 182A. A sole proprietor who files on time avoids both.</p>

<h2 id="checklist">Registration Checklist</h2>
<ul>
<li>☐ IRIS account active; CNIC serves as NTN.</li>
<li>☐ Business name, start date, address and nature of business added through Form 181.</li>
<li>☐ Each branch added separately.</li>
<li>☐ Business bank account opened and added to IRIS.</li>
<li>☐ Trade licences and provincial levies checked for your activity.</li>
<li>☐ Online stores: NTN in place before opening marketplace or courier accounts.</li>
<li>☐ Monthly record folder set up.</li>
<li>☐ Return date (30 September) and, if applicable, advance tax dates in your calendar.</li>
</ul>
""", [
    ("How much tax does a sole proprietor pay?",
     "For tax year 2027, non-salaried individuals pay nil up to Rs 600,000 of taxable income, then 15%, 20%, 30%, 40% and 45% in bands, reaching Rs 1,610,000 plus 45% above Rs 5,600,000."),
    ("When is a sole proprietor's tax return due?",
     "Under Section 118, an individual's return is normally due by 30 September following the end of the tax year, unless FBR extends the date."),
    ("Can I register my business name as a trademark?",
     "Yes. Registering the name on IRIS does not protect it; a trademark application with IPO-Pakistan does."),
    ("What does it cost to file late?",
     "Under Section 182, 0.1% of the tax payable per day of default, up to 50%, with a minimum of Rs 40,000; and an individual pays a Rs 25,000 surcharge under Section 182A to rejoin the Active Taxpayers List."),
])

# ───────────────────────── Add business on IRIS ─────────────────────────
EXTRA["add-business-to-ntn-iris-sole-proprietor"] = (f"""
<h2 id="fields">The Business Details, One by One</h2>
{table(["Detail", "What to enter", "Common mistake"], [
    ["Business name", "The trading name exactly as on your signboard, invoices and bank account", "Abbreviations or spellings that differ from the bank account"],
    ["Start date", "The date you actually began trading", "Using the registration date when trading began earlier, which leaves earlier income unexplained"],
    ["Nature of business", "The principal activity, chosen from IRIS's list as closely as possible", "Choosing a vague or unrelated activity"],
    ["Business address", "The place where the business operates", "Using a home address for a shop elsewhere"],
    ["Branches", "Each additional place of business", "Leaving a second shop or warehouse off the registration"],
    ["Bank account", "Accounts used for business receipts and payments", "Listing only a personal account while business money runs elsewhere"],
])}

<h2 id="salaried-plus-business">Salaried and Running a Business: What Changes</h2>
<p>Many people add a business while still employed. Adding it to IRIS does not affect your employer's deductions, but your return changes in three ways:</p>
<ol>
<li><strong>Two heads of income.</strong> Salary stays under "Salary"; the business profit goes under "Income from business". Expenses of the business are claimed only against the business.</li>
<li><strong>Advance tax may start.</strong> Section 147 excludes salary taxed at source when applying the Rs 1 million test, but if your latest assessed business and other adjustable income reaches Rs 1 million, quarterly advance tax applies. See our {a(ADV, 'advance tax guide')}.</li>
<li><strong>Wealth statement reconciliation.</strong> Money put into the business and drawings taken out must be traceable through the wealth statement.</li>
</ol>

<h2 id="confirm">After Submitting: How to Confirm the Update</h2>
<ul>
<li>Check your IRIS registration details for the business name, address, branches and bank account.</li>
<li>Download the updated registration certificate where IRIS offers it, and keep it with your records; banks and marketplaces often ask for it.</li>
<li>If the status stays pending or the form is returned, read the reason in IRIS, correct the attachment or detail, and resubmit.</li>
<li>If nothing moves, take the acknowledgement and documents to your Regional Tax Office.</li>
</ul>

<h2 id="rto-visit">Preparing for an RTO Visit</h2>
<p>FBR's own page lists the changes that require a visit to your RTO: discontinuance of business, change of jurisdiction, deregistration, and updating CNIC, email or POC. For a smooth visit:</p>
<ul>
<li>Take your original CNIC and a copy, and a written application signed by you stating the change requested.</li>
<li>Bring documents that prove the change: a new rent agreement or ownership papers, a utility bill, or closure evidence.</li>
<li>Bring printouts of your IRIS profile and any error screens.</li>
<li>Ask for the application to be received or diarised, and keep the receipt.</li>
</ul>

<h2 id="legal-rep">When the Owner Dies: Legal Representative</h2>
<p>FBR's list of Form 181 updates includes the legal representative under Section 87. When a sole proprietor dies, the legal representative is liable for the tax the individual would have owed and for tax on the income of the estate, but only to the extent the estate can meet it (Section 87). Registering the legal representative on the deceased's profile allows pending returns and correspondence to be dealt with, and the business can then be continued by an heir under their own registration or closed.</p>

<h2 id="why-it-matters">Why an Outdated Registration Costs Money</h2>
<ul>
<li><strong>Notices.</strong> Income from a business FBR does not know about often triggers a notice asking you to explain it.</li>
<li><strong>Blocked payouts.</strong> Marketplaces and couriers must verify registration before serving vendors.</li>
<li><strong>Lost credits.</strong> Tax deducted by customers under a name or NTN that does not match can be harder to claim.</li>
<li><strong>Wrong office.</strong> An old address can leave notices going to the wrong place while deadlines run.</li>
</ul>
""", [
    ("Will adding a business change my employer's tax deduction?",
     "No. Your employer continues to deduct tax on salary. The business profit is declared separately in your return."),
    ("What start date should I enter for the business?",
     "The date you actually began trading. Entering a later date can leave earlier business income unexplained."),
    ("What happens to the business if the owner dies?",
     "The legal representative becomes liable for the deceased's tax, limited to what the estate can pay, under Section 87. The representative can be recorded on the profile through Form 181."),
    ("Do I need to visit the RTO to add a branch?",
     "No. Addition of business branches is one of the changes FBR lists for Form 181 online."),
])

# ───────────────────────── Advance tax ─────────────────────────
EXTRA["sole-proprietor-advance-tax-pakistan"] = (f"""
<h2 id="full-year">A Full Year, Quarter by Quarter</h2>
<p>A sole proprietor's tax assessed for tax year 2026 was Rs 600,000, so A/4 is Rs 150,000 for each quarter of tax year 2027. Adjustable tax deducted at source in each quarter (B) varies:</p>
{table(["Quarter", "Due by", "A/4", "Adjustable tax deducted in quarter (B)", "Instalment (A/4 - B)"], [
    ["September", "15 Sep 2026", "Rs 150,000", "Rs 40,000", "Rs 110,000"],
    ["December", "15 Dec 2026", "Rs 150,000", "Rs 25,000", "Rs 125,000"],
    ["March", "15 Mar 2027", "Rs 150,000", "Rs 30,000", "Rs 120,000"],
    ["June", "15 Jun 2027", "Rs 150,000", "Rs 35,000", "Rs 115,000"],
    ["Total", "", "Rs 600,000", "Rs 130,000", "Rs 470,000"],
])}
<p>When the return for tax year 2027 is filed, the instalments and the tax deducted at source are both credited against the tax chargeable for that year. If they exceed it, the excess can be claimed back through the refund process; if they fall short, the balance is paid with the return. The figures are illustrative.</p>

<h2 id="what-counts-as-b">What Counts as "B"</h2>
<p>B is the tax paid in the quarter for which a credit is allowed under Section 168, other than tax deducted from salary under Section 149. In plain terms, it is <strong>adjustable</strong> tax deducted or collected from you during that quarter that you will claim as a credit in your return. Tax that is final, or is a minimum tax that cannot be credited, does not reduce the instalment. Keep the deduction certificates or statements for every amount you include in B, because the same amounts are claimed in the return.</p>

<h2 id="new-business">First Year in Business</h2>
<p>Section 147 applies to a taxpayer whose income was charged to tax for the latest tax year, and for individuals it bites only when that latest assessed taxable income (outside salary and final-tax income) is Rs 1 million or more. A brand-new business with no such assessed income does not have a formula amount to pay in its first year. Once the first return with business income is filed and the income is Rs 1 million or more, instalments start in the following year. Plan cash for it: the first year of instalments often arrives at the same time as the balance of tax for the previous year.</p>

<h2 id="estimate-example">Estimate Example: Using Section 147(6) Safely</h2>
<p>A trader's formula instalments for the year total Rs 480,000, but by January turnover has fallen sharply. The trader prepares an estimate showing turnover for the completed quarters, estimated turnover for the remaining quarters with reasons for the decline, supporting evidence for expenses, and a computation showing estimated tax of Rs 300,000. Having already paid Rs 240,000, the trader pays the remaining Rs 60,000 in equal instalments on the dates not yet passed.</p>
<p>The check that matters: if the tax finally chargeable turns out to be, say, Rs 360,000, the tax paid of Rs 300,000 is below 90% of it (Rs 324,000). Under Section 205(1B), default surcharge at 12% a year then applies to the Rs 24,000 shortfall. An estimate built on real records avoids that.</p>

<h2 id="mistakes">Common Advance Tax Mistakes</h2>
<ul>
<li>Counting salary tax in B; Section 147(4B) excludes it.</li>
<li>Paying the same amount every quarter without deducting adjustable tax actually suffered.</li>
<li>Filing a lower estimate without evidence or reasons.</li>
<li>Missing the 15th, which is in the last month of the quarter, not after it ends.</li>
<li>Not claiming instalments in the return because the PSIDs were not kept.</li>
</ul>
""", [
    ("Does a new business pay advance tax in its first year?",
     "Usually not. Section 147 depends on income charged to tax for the latest tax year, and for individuals applies when that latest assessed income is Rs 1 million or more."),
    ("What happens if my advance tax is more than my final tax?",
     "Instalments are credited against the tax chargeable in your return, and an excess can be claimed through the refund process."),
    ("What is the 90% rule for lower estimates?",
     "Under Section 205(1B), if tax paid on a lower estimate is less than 90% of the tax finally chargeable, default surcharge at 12% a year applies to the shortfall."),
    ("Which withholding taxes reduce my instalment?",
     "Only adjustable taxes for which credit is allowed under Section 168, other than salary tax. Final or minimum taxes do not reduce it."),
])

# ───────────────────────── Withholding duties ─────────────────────────
EXTRA["sole-proprietor-withholding-tax-duties-pakistan"] = (f"""
<h2 id="penalties">Penalties for Late or Missing Statements</h2>
<p>Section 182 sets the penalty for failing to file a withholding statement under Section 165 by the due date:</p>
{table(["Situation", "Penalty"], [
    ["Tax was deducted and paid on time, and the statement is filed within 90 days of its due date", "Rs 50,000"],
    ["All other late or missing statements", "Rs 2,500 for each day of default, minimum Rs 10,000"],
    ["It is established that no tax had to be deducted in the period", "Minimum Rs 10,000"],
])}
<p>These penalties are separate from the Section 161 liability for tax not deducted or not paid. A single missed quarter can therefore cost more than a year of professional help.</p>

<h2 id="supplier-setup">Setting Up Supplier Withholding After Crossing Rs 100 Million</h2>
<ol>
<li><strong>Build a supplier list</strong> with each supplier's name, CNIC or NTN and whether they supply goods, services or work under a contract.</li>
<li><strong>Check each supplier's status</strong> on the Active Taxpayers List before payment, because rates for persons not on the list are higher under the First Schedule.</li>
<li><strong>Apply the right rate</strong> at the time of payment and pay the supplier the net amount.</li>
<li><strong>Deposit the tax</strong> through a PSID on IRIS within the time set by the rules.</li>
<li><strong>Issue certificates</strong> so suppliers can claim the tax in their returns.</li>
<li><strong>File the quarterly statement</strong> listing each payee and amount.</li>
</ol>
<p>Rates change through Finance Acts, so confirm them each year; our {a('/blogs/withholding-tax-pakistan-2026', 'withholding rates guide')} is updated for the current year.</p>

<h2 id="salary-workflow">Salary Withholding: A Monthly Routine</h2>
<ul>
<li>At the start of the year, estimate each employee's annual salary.</li>
<li>Work out the tax for the year at the salary rates, adjust for tax already deducted under other heads and any credits supported by documents, and spread it over the remaining months.</li>
<li>Deduct each month's share when paying salary, and recalculate when pay changes.</li>
<li>Deposit the tax and include it in the Section 165 statement for the quarter.</li>
<li>Give each employee a certificate of tax deducted for their own return.</li>
</ul>

<h2 id="rent-example">Rent Example</h2>
<p>A sole proprietor rents a showroom for Rs 140,000 a month. Annual rent is Rs 1,680,000, which is above the Rs 1.5 million threshold in Section 155(3), so the tenant is a prescribed person and must deduct tax from each rent payment at the rate applicable to the landlord, deposit it and report it. A tenant paying Rs 100,000 a month (Rs 1.2 million a year) is below the threshold and has no Section 155 duty as an individual. The figures are illustrative.</p>

<h2 id="situations">Quick Answers for Common Situations</h2>
{table(["Situation", "Withholding duty?"], [
    ["Shop with two employees on low salaries", "Yes, Section 149 applies to every employer; the tax may compute to nil"],
    ["Warehouse rent Rs 200,000 a month", "Yes, Section 155: annual rent exceeds Rs 1.5 million"],
    ["Turnover Rs 80 million in every past year", "No Section 153 duty as an individual on that test alone"],
    ["Turnover Rs 105 million in tax year 2024, Rs 90 million since", "Yes, Section 153 applies: the test is any preceding tax year"],
    ["Builder selling flats", "Yes, builders are prescribed persons under Section 153(7)"],
])}

<h2 id="certificates">Certificates Work Both Ways</h2>
<p>As your business grows, you will both deduct tax from others and have tax deducted from you. Keep the two separate: tax you deducted belongs in your statements and must be deposited; tax deducted from you is a credit in your own return and, if adjustable, can reduce your advance tax instalments.</p>
""", [
    ("What is the penalty for a late withholding statement?",
     "Rs 50,000 if the tax was already paid and the statement is filed within 90 days of the due date; otherwise Rs 2,500 per day of default, with a minimum of Rs 10,000, under Section 182."),
    ("Do I check my supplier's filer status before deducting tax?",
     "Yes. Rates for persons not on the Active Taxpayers List are higher, so check status at the time of payment."),
    ("Is withholding tax my own expense?",
     "No. You deduct it from the payment and deposit it on the payee's behalf. It becomes your liability only if you fail to deduct or deposit it."),
])

# ───────────────────────── Records ─────────────────────────
EXTRA["sole-proprietor-records-books-fbr-pakistan"] = (f"""
<h2 id="penalties">What Poor Records Can Cost</h2>
{table(["Failure", "Penalty under Section 182"], [
    ["Failing to maintain records required under the Ordinance or rules", "Rs 10,000 or 5% of the tax on income, whichever is higher"],
    ["Failing to produce records in an audit (Section 177): first notice", "Rs 100,000"],
    ["Second notice", "Rs 200,000"],
    ["Third notice", "Rs 300,000"],
])}
<p>On top of penalties, Section 174(2) lets the Commissioner disallow or reduce expenses you cannot support, which increases taxable income and the tax on it. Records are the cheapest protection a small business has.</p>

<h2 id="how-long">How Long, in Practice</h2>
{table(["Tax year", "Year ends", "Keep records at least until"], [
    ["2024", "30 June 2024", "30 June 2030"],
    ["2025", "30 June 2025", "30 June 2031"],
    ["2026", "30 June 2026", "30 June 2032"],
    ["2027", "30 June 2027", "30 June 2033"],
])}
<p>If an assessment, appeal, reference, petition, prosecution or ADR proceeding is pending for a year, keep that year's records until it is finally decided, whatever the date above.</p>

<h2 id="month-end">A Month-End Routine in Ten Steps</h2>
<ol>
<li>Download the business bank statement.</li>
<li>Match each deposit to a sale or other receipt.</li>
<li>Match each payment to a bill, salary sheet or receipt.</li>
<li>Record cash sales from the daily summaries.</li>
<li>Record cash expenses with the payee's name and purpose.</li>
<li>Separate the owner's drawings from business expenses.</li>
<li>File withholding certificates received from customers.</li>
<li>File proof of tax you deducted and deposited, if any.</li>
<li>Note stock purchases and any large stock movements.</li>
<li>Store the month's folder, physical or digital, under the tax year.</li>
</ol>

<h2 id="digital">Keeping Records Digitally</h2>
<p>Photographs and scans are practical, but they must be legible and retrievable for the whole retention period. Use one folder per tax year and month, name files consistently (date, party, amount), and keep a backup in a second place. Remember that Section 174(1) requires records to be maintained in Pakistan, and Section 174(5) allows FBR to require specified electronic systems for some persons or classes; if your business is notified, the prescribed system takes priority over your own method.</p>

<h2 id="wealth">Records Behind the Wealth Statement</h2>
<p>The wealth statement compares what you owned at the start and end of the year with your income and spending. For a sole proprietor, the business records feed it directly: closing stock, business bank balances, receivables, payables and business assets all appear in it. If business records are incomplete, the reconciliation does not balance, which is one of the most common triggers for notices.</p>
""", [
    ("What is the penalty for not keeping records?",
     "Under Section 182, Rs 10,000 or 5% of the tax on income, whichever is higher, for failing to maintain records required under the Ordinance or rules."),
    ("What happens if I do not produce records in an audit?",
     "Under Section 182, penalties of Rs 100,000, Rs 200,000 and Rs 300,000 apply for failing to produce records on the first, second and third notices under Section 177."),
    ("Until when must I keep tax year 2026 records?",
     "At least until 30 June 2032, six years after the tax year ended on 30 June 2026, and longer if a proceeding is pending."),
    ("Do business records affect my wealth statement?",
     "Yes. Stock, business bank balances, receivables, payables and assets from the business all feed into the wealth statement reconciliation."),
])

# ───────────────────────── Close ─────────────────────────
EXTRA["close-sole-proprietorship-remove-business-ntn-pakistan"] = (f"""
<h2 id="sell-instead">Selling the Business Instead of Closing It</h2>
<p>Sometimes the better option is to sell the business as a going concern: stock, fixtures, goodwill and the right to the premises. A sole proprietorship is not a separate legal person, so the buyer acquires the assets, not "the business" itself. The buyer registers the business under their own NTN, and you discontinue it on yours. Any gain on assets sold is declared in your return for that year, and the sale price and what it covers should be set out in a written agreement that you keep with your records.</p>

<h2 id="death">When the Owner Has Died</h2>
<p>Under Section 87, the legal representative of a deceased individual is liable for the tax the individual would have owed and for tax on the income of the estate, limited to what the estate can pay. FBR's list of Form 181 updates includes recording the legal representative. In practice, the family:</p>
<ol>
<li>records the legal representative on the deceased's IRIS profile;</li>
<li>files any outstanding returns up to the date of death;</li>
<li>decides whether an heir continues the business under their own registration or the business is closed; and</li>
<li>applies to the RTO for discontinuance on the deceased's registration once affairs are settled.</li>
</ol>

<h2 id="pending">Closing While a Notice or Case Is Pending</h2>
<p>Closing a business does not end a pending assessment, audit or appeal. Respond to notices on time, and keep the records for every year involved until the proceeding is finally decided, as Section 174(3) requires. If you cannot attend to them, appoint someone to represent you. Our {a(NOTICE, 'notice defence service')} handles replies for closed businesses too.</p>

<h2 id="wealth-example">The Wealth Statement on Closure: Example</h2>
<p>A trader closes on 31 March 2027. On that date the business had stock of Rs 900,000, a bank balance of Rs 450,000 and furniture worth Rs 150,000. The trader sells the stock for Rs 1,000,000, transfers the furniture to personal use, and closes the business bank account into a personal account. In the tax year 2027 return:</p>
<ul>
<li>The profit up to closure, including the stock sale, is declared as business income.</li>
<li>The business bank balance disappears and the personal bank balance rises by the transferred amount.</li>
<li>The furniture moves from business assets to personal assets.</li>
<li>The reconciliation shows how the money moved, so the wealth statement balances.</li>
</ul>
<p>The figures are illustrative.</p>

<h2 id="dormant">Dormant Is Not Closed</h2>
<p>A business that has stopped trading but has not been discontinued with FBR remains on your registration. Returns continue to be expected, and nil activity still needs to be declared. If you are sure you will not restart, discontinue it formally; if you might restart within a few months, keep filing and keep the records.</p>

<h2 id="pack">Document Pack for the RTO</h2>
<ul>
<li>Written application stating your name, CNIC, business name and the date trading stopped.</li>
<li>Copy of your CNIC.</li>
<li>Evidence of closure: end of the rent agreement or premises handed back, commercial utility disconnection, bank account closure letter.</li>
<li>Copies of the last returns filed.</li>
<li>Any sale agreement if the business assets were sold.</li>
</ul>

<h2 id="after-closure">After Closure</h2>
<p>Your personal registration continues. If you have other income, keep filing as an individual; a return filed late costs 0.1% of tax payable per day under Section 182, with a minimum of Rs 40,000. If you start a new business later, add it to your registration through Form 181 as described in our guide to {a(I, 'adding a business on IRIS')}.</p>
""", [
    ("Can I sell my sole proprietorship?",
     "You can sell its assets, such as stock, fixtures and goodwill. The buyer registers the business under their own NTN, and you discontinue it on yours and declare any gain."),
    ("What happens to the business when the owner dies?",
     "The legal representative is liable for the deceased's tax up to what the estate can pay (Section 87), is recorded on the profile, and the business is continued by an heir under their own registration or closed."),
    ("Can I close my business while a notice is pending?",
     "You can stop trading, but the notice or case continues. Respond on time and keep the records until it is finally decided."),
    ("Is a dormant business the same as a closed one?",
     "No. Until it is discontinued with FBR, it remains on your registration and returns are still expected."),
    ("Do I still file returns after closing the business?",
     "Yes, for the year of closure, and as an individual afterwards if you have taxable income or are otherwise required to file."),
])
