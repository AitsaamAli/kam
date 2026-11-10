"""Depth for the second sole proprietor batch (posts5)."""
from posts import a, table

EXTRA = {}

EXTRA["sole-proprietor-tax-services-fees-pakistan"] = (table(["Business stage", "Typical services", "Published fees"], [
    ["Starting out", "Sole proprietorship registration; first return with wealth statement", "Rs 5,000 + Rs 5,000"],
    ["Growing (income above Rs 1 million, staff hired)", "Annual return; advance tax planning; salary withholding statements", "Rs 5,000 return; withholding Rs 3,000 a month"],
    ["Established (rent over Rs 1.5 million, turnover near Rs 100 million)", "Annual return; advance tax; withholding on salaries, rent and suppliers", "Return Rs 5,000; withholding Rs 3,000 a month"],
    ["Any stage, when a notice arrives", "Notice response", "From Rs 5,000"],
]).join(['<h2 id="stages">Which Services at Which Stage</h2>\n', """
<h2 id="return-includes">What Our Rs 5,000 Return Fee Includes</h2>
<ul>
<li>Review of your bank statements, sales records and expense documents for the year.</li>
<li>Business income computed with the expenses your records support.</li>
<li>Tax credits claimed for tax deducted from you and advance tax paid.</li>
<li>Draft figures shared with you for approval before filing.</li>
<li>Filing on IRIS and the acknowledgement sent to you.</li>
</ul>
<p>A separate, detailed wealth statement preparation is listed at Rs 2,000 on our pricing page. Where a business has unusual complexity, we tell you before starting.</p>
"""]), [
    ("Is the wealth statement included in the return fee?",
     "The return fee is Rs 5,000; detailed wealth statement preparation is listed separately at Rs 2,000 on our pricing page. We confirm the total before starting."),
    ("Do you offer yearly packages?",
     "We quote the services your business needs for the year, using the published fees, so you know the annual cost in advance."),
])

EXTRA["sole-proprietorship-registration-lahore"] = ("""
<h2 id="office-visit">What Happens When You Visit Our Office</h2>
<ol>
<li>We check your CNIC and whether an IRIS profile already exists.</li>
<li>We confirm the business details: name, start date, address, branches and activity.</li>
<li>We register or update your IRIS profile and add the business through Form 181.</li>
<li>We note what you still need: the bank account, trade licences or other registrations for your activity.</li>
<li>You leave with copies of what was filed and a list of the deadlines that apply to you.</li>
</ol>
<p>If the IRIS profile has problems, such as a mobile number or email that no longer works, we explain whether it can be fixed online or needs an RTO application, and prepare the application if needed.</p>

<h2 id="professional-tax">Professional Tax in Punjab</h2>
<p>Separately from federal income tax, Punjab levies professional tax, collected by the Excise, Taxation and Narcotics Control Department, which can be paid online. Whether and how much a business pays depends on the provincial rules for its category. Keep the paid receipt each year: licence renewals, tenders and some registrations ask for proof that it has been paid. Paying professional tax does not settle income tax, and vice versa.</p>

<h2 id="partnership-check">Sole Proprietorship or Partnership?</h2>
<p>Many Lahore businesses are run by relatives together. If two or more people share ownership and profits, the business is an association of persons, not a sole proprietorship, and it registers and files separately. Partnerships in Punjab can also register with the Registrar of Firms. Getting this right at the start avoids re-registering later; see our guide to the {rof}.</p>

<h2 id="online-lahore">Online Stores Run From Lahore</h2>
<p>Lahore has many home-based online stores. Because marketplaces and couriers must not serve unregistered vendors under Section 181(1A), register the business first, with the store name you will use, and use the same name and CNIC on the seller and courier accounts. Keep the monthly settlement and cash-on-delivery statements as your sales records.</p>
""".replace("{rof}", a("/blogs/registrar-of-firms-vs-fbr-registration-partnership-lahore", "Registrar of Firms and FBR registration for partnerships")), [
    ("Do Lahore businesses pay professional tax?",
     "Punjab levies professional tax through the Excise, Taxation and Narcotics Control Department, depending on the category of business or profession. It is separate from federal income tax."),
    ("Can you register my business the same day I visit?",
     "When the IRIS profile and documents are in order, the business can usually be added in the same visit. Problems with the profile may need extra steps."),
    ("Can I register an online store run from home in Lahore?",
     "Yes. Use your home address as the business address and register before opening marketplace and courier accounts."),
    ("Is there parking or easy access at your Awan Town office?",
     "Our office is in Rizwan Block Market, opposite Rizwan Park, Awan Town. Message us on WhatsApp before visiting and we will guide you and confirm the documents to bring."),
])

EXTRA["sole-proprietor-wealth-statement-pakistan"] = ("""
<h2 id="first-year">Your First Wealth Statement After Starting a Business</h2>
<p>In the first year, the money you put into the business usually comes from savings, a gift or a loan. The wealth statement should show where it came from: savings already declared in last year's statement, a gift with the giver's details, or a loan with the lender's details and terms. The business then appears as capital, and the source of that capital is visible. A first statement that shows business capital with no source is one of the most common reasons for questions.</p>

<h2 id="stock">Stock: Count It, Value It Consistently</h2>
<p>For trading businesses, stock is often the largest business asset. Count it at 30 June each year and value it on the same basis every year, the basis used in your business accounts. Stock that jumps or falls sharply without a reason in your sales or purchases will be questioned, and a low stock figure that later turns into high sales can suggest income was understated earlier.</p>

<h2 id="family-loans">Loans From Family and Friends</h2>
<p>Informal loans are common in small businesses. Record them properly: who lent, how much, when, and how it was paid, ideally through a bank. Show the loan as a liability while it is outstanding and its repayment in the reconciliation. A large inflow described only as a "loan from a relative", with no record, is weak evidence.</p>

<h2 id="cash-in-hand">Cash in Hand</h2>
<p>A large closing cash balance at home or in the shop invites questions. Keep business cash in the business bank account where possible, and make sure any cash shown at year end is consistent with your daily sales records and deposits.</p>
""", [
    ("How do I show money I put into a new business?",
     "Show it as capital in the business and make its source visible: savings from last year's statement, a gift with the giver's details, or a loan with the lender's details."),
    ("How should I value stock in the wealth statement?",
     "Count it at 30 June and value it on the same basis each year, the basis used in your business accounts."),
])

EXTRA["sole-proprietor-cash-payment-rules-section-21-pakistan"] = ("""
<h2 id="proof">Proving a Payment Went Through the Banking Channel</h2>
<ul>
<li>Keep the business bank statement showing the debit, with the payee's name where the bank shows it.</li>
<li>Keep the supplier's invoice and, where possible, a copy of their acknowledgement or bank receipt.</li>
<li>For card payments, keep the card statement and the receipt.</li>
<li>Note the invoice number in the transfer reference, so statement lines match invoices easily.</li>
</ul>

<h2 id="refuses">If a Supplier Refuses Bank Payment</h2>
<p>Some suppliers still insist on cash. If the amount under that expense head will stay well below Rs 250,000 for the year, the 21(l) rule does not bite. If it will not, the cost of the disallowance is part of the real price of that supplier. Compare it with a supplier who accepts bank payment and holds an NTN, which also avoids the 10% disallowance under 21(q).</p>

<h2 id="year-end">A Year-End Check Before 30 June</h2>
<ol>
<li>List each expense head and the total paid in cash so far.</li>
<li>Mark any head approaching Rs 250,000 and switch the rest of the year's payments to bank transfer.</li>
<li>List suppliers without an NTN and ask for it, or plan to move purchases.</li>
<li>Check invoices above Rs 200,000 collected in cash and ask regular customers to pay large invoices by bank.</li>
</ol>
""", [
    ("Do I need to change suppliers because of these rules?",
     "Not necessarily. Compare the tax cost of the disallowance with the price and convenience of a supplier who accepts bank payment and holds an NTN."),
    ("When should I review cash payments?",
     "Before 30 June, while there is still time to move payments to the bank and collect suppliers' NTNs for the year."),
])
