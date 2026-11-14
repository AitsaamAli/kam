"""Second layer of depth for the sole proprietor series."""
from posts import a, table

ADV = "/blogs/sole-proprietor-advance-tax-pakistan"
W = "/blogs/sole-proprietor-withholding-tax-duties-pakistan"
REC = "/blogs/sole-proprietor-records-books-fbr-pakistan"
I = "/blogs/add-business-to-ntn-iris-sole-proprietor"

EXTRA = {}

EXTRA["sole-proprietorship-registration-pakistan"] = (f"""
<h2 id="online-detail">Online Sellers: Getting It Right From Day One</h2>
<p>Section 181(1A), added by the Finance Act, 2025, bars online marketplaces and couriers from letting an unregistered vendor use their platform for e-commerce. For a sole proprietor selling online, that means:</p>
<ol>
<li>Register on IRIS and add the online store as your business, with the store name you will use on the marketplace.</li>
<li>Use the same name and CNIC when opening marketplace seller and courier cash-on-delivery accounts.</li>
<li>Keep the marketplace settlement reports and courier statements every month; they are your sales records.</li>
<li>Declare the profit in your return as business income, claiming the platform fees and delivery charges you can support with statements.</li>
</ol>

<h2 id="from-job">Leaving a Job to Run the Business Full Time</h2>
<p>If you were salaried and now run the business full time, your registration stays the same; the change shows in your return. The year you leave will usually have both salary and business income. From the next year, only business income is declared, and because salary tax at source no longer covers you, check whether quarterly {a(ADV, 'advance tax')} will apply once your business income has been assessed at Rs 1 million or more.</p>
""", [
    ("Do I need a separate NTN for my online store?",
     "No. A sole proprietor's store is added as a business on the owner's registration, where the CNIC is the NTN."),
    ("I left my job to run my business. Does my registration change?",
     "No. The same registration continues; your return shows business income instead of, or alongside, salary for the year you switched."),
])

EXTRA["add-business-to-ntn-iris-sole-proprietor"] = (f"""
<h2 id="which-route">Form 181, New Registration or RTO? Choosing the Right Route</h2>
{table(["You want to…", "Route"], [
    ["Start your first business and you have never registered", "Register on IRIS first; your CNIC becomes your NTN. Then add the business."],
    ["Add a business to an existing registration", "Form 181 (modification) on IRIS"],
    ["Add a second shop or warehouse", "Form 181: add a business branch"],
    ["Change the business address within the same area", "Form 181"],
    ["Move the business to another city", "Visit the RTO: change of jurisdiction is on FBR's RTO-only list"],
    ["Update your email or CNIC", "Visit the RTO"],
    ["Stop the business", "Visit the RTO: discontinuance of business"],
])}

<h2 id="multiple">Several Businesses on One Registration</h2>
<p>A sole proprietor can run more than one business under one registration, for example a shop and an online store. All of them belong to the same taxpayer, so their profits are added together in one return. Keep separate records for each business so that income and expenses can be shown business by business if an officer asks, and use one bank account per business where practical. If one business makes a loss, it is set against the others under the rules for business losses, which is another reason clean records matter.</p>

<h2 id="moving-city">Moving Your Business to Another City</h2>
<p>Moving from, for example, Faisalabad to Lahore changes more than the address. Your income tax jurisdiction is linked to where you live and work, and FBR lists change of jurisdiction among the updates that need an RTO visit. Until it is changed, notices may still come from the old office. Apply early, keep the receipt, and update the business address and bank details once the jurisdiction is transferred.</p>

<h2 id="evidence">Evidence Officers Commonly Accept</h2>
<ul>
<li><strong>For the address:</strong> rent agreement or ownership document, and a recent utility bill in the name of the business or owner.</li>
<li><strong>For the activity:</strong> photographs of the premises or signboard, a sample invoice, or a link to the online store.</li>
<li><strong>For the start date:</strong> the first purchase invoices, the rent start date, or the bank account opening date.</li>
</ul>
<p>Keeping this small set of documents in one file makes Form 181, bank account opening and any later questions much easier.</p>
""", [
    ("Can I change my business city through Form 181?",
     "A move that changes your income tax jurisdiction needs an RTO visit; FBR lists change of jurisdiction among the RTO-only updates."),
    ("Can one person have two businesses on one NTN?",
     "Yes. Both businesses sit on the owner's registration and their profits are declared together, so keep separate records for each."),
    ("What evidence supports the business start date?",
     "First purchase invoices, the rent start date or the business bank account opening date are commonly used."),
])

EXTRA["sole-proprietor-advance-tax-pakistan"] = (f"""
<h2 id="paying">Paying an Instalment on IRIS</h2>
<ol>
<li>Log in to IRIS and open the payment section to create a payment slip (PSID).</li>
<li>Choose income tax, the advance tax section (147), the tax year and the period.</li>
<li>Enter the instalment amount worked out with the formula.</li>
<li>Generate the PSID and pay it through your bank's branch, internet banking or app before the 15th.</li>
<li>Download the paid challan (CPR) and file it with your records; you will claim it in your return.</li>
</ol>

<h2 id="cash-planning">Planning Cash for Instalments</h2>
<p>The 15th of September, December, March and June arrives inside the quarter, not after it. A simple way to avoid a shortfall is to move a fixed share of each month's takings to a separate account:</p>
{table(["If your annual instalments total", "Set aside each month"], [
    ["Rs 240,000", "Rs 20,000"],
    ["Rs 480,000", "Rs 40,000"],
    ["Rs 720,000", "Rs 60,000"],
    ["Rs 1,200,000", "Rs 100,000"],
])}

<h2 id="builders-detail">Builders and Developers: Project-by-Project</h2>
<p>Under Section 147(5C), a person whose business is constructing and disposing of buildings, or developing and selling plots, pays adjustable advance tax on a project-by-project basis at the rates in Part IIB of the First Schedule, in four equal instalments on the normal due dates. The project-based amount is adjustable against the final tax for the year, so the records for each project, including area and sale figures, need to be kept separately.</p>
""", [
    ("How do I pay advance tax?",
     "Create a PSID on IRIS for income tax under section 147 for the tax year and quarter, then pay it through your bank before the 15th and keep the paid challan."),
    ("Is advance tax paid on the 15th after the quarter ends?",
     "No. For individuals the due dates are 15 September, 15 December, 15 March and 15 June, inside each quarter."),
    ("Do builders calculate advance tax with the (A/4) - B formula?",
     "No. Under Section 147(5C), builders and developers pay project-by-project at the rates in Part IIB of the First Schedule, in four equal instalments."),
])

EXTRA["sole-proprietor-withholding-tax-duties-pakistan"] = (f"""
<h2 id="catch-up">Just Realised You Should Have Been Deducting? A 30-Day Plan</h2>
<ol>
<li><strong>Days 1 to 5:</strong> list every payment of the last year by type: salaries, rent, suppliers, services, contracts.</li>
<li><strong>Days 6 to 10:</strong> mark which ones fell under Sections 149, 153 or 155 based on the thresholds above.</li>
<li><strong>Days 11 to 20:</strong> start deducting correctly from the next payment; do not wait for the past to be settled.</li>
<li><strong>Days 21 to 30:</strong> take advice on the past periods: what tax was missed, which statements are outstanding, and how to file them.</li>
</ol>
<p>Correcting the practice quickly matters, because Section 161 liability and Section 182 penalties both grow with each missed period.</p>

<h2 id="three-taxes">Withholding, Advance Tax and Your Own Return: How They Fit</h2>
{table(["", "Withholding you deduct", "Advance tax you pay", "Your annual return"], [
    ["Whose tax is it?", "The payee's (employee, landlord, supplier)", "Yours", "Yours"],
    ["Law", "Sections 149, 153, 155", "Section 147", "Section 114"],
    ["When", "At the time of payment; statements quarterly", "15 Sep, Dec, Mar, Jun", "By 30 September after the tax year"],
    ["Where it ends up", "Credited in the payee's return", "Credited in your return", "Final computation of your tax"],
])}
<p>Mixing these up is common. Tax you deducted from others is never a credit in your own return.</p>

<h2 id="inspection-set">The Record Set an Officer Will Ask For</h2>
<ul>
<li>Payroll sheets and the tax calculation for each employee.</li>
<li>Rent agreements and proof of rent paid.</li>
<li>Supplier invoices with the deduction applied, and the supplier's NTN or CNIC.</li>
<li>Paid challans (CPRs) for every deposit.</li>
<li>Quarterly statements with their acknowledgements.</li>
<li>Copies of certificates issued to payees.</li>
</ul>
<p>Keep this set for six years, as Section 174 requires. Our {a(REC, 'records guide')} shows how to organise it.</p>
""", [
    ("Is tax I deducted from my landlord a credit in my own return?",
     "No. Tax you deduct belongs to the payee and is credited in their return. Only tax deducted from you is a credit in yours."),
    ("What should I do if I missed deductions in past months?",
     "Start deducting correctly from the next payment, then work out the past periods, missed tax and outstanding statements with advice, because liability and penalties grow with each period."),
    ("How long must withholding records be kept?",
     "Six years after the end of the tax year under Section 174, and longer if a proceeding is pending."),
])

EXTRA["sole-proprietor-records-books-fbr-pakistan"] = (f"""
<h2 id="evidence-by-expense">Good Evidence for Each Type of Expense</h2>
{table(["Expense", "Evidence that holds up", "Weak evidence"], [
    ["Rent", "Rent agreement, bank transfers to the landlord, withholding proof if applicable", "Cash with no receipt"],
    ["Salaries", "Payroll sheet, bank transfers or signed salary receipts, employee CNICs", "A single annual total with no names"],
    ["Electricity, gas, phone", "Bills in the business or owner's name for the business premises", "Bills for the owner's home claimed as business"],
    ["Stock purchases", "Supplier invoices, delivery notes, bank payments", "Handwritten slips with no supplier details"],
    ["Transport and delivery", "Courier statements, fuel bills linked to business vehicles, freight receipts", "Round monthly figures"],
    ["Repairs and maintenance", "Invoices describing the work and premises", "Undated cash receipts"],
    ["Marketing and online fees", "Platform invoices, ad account statements", "Screenshots without amounts or dates"],
])}

<h2 id="cash-sales">Making Cash Sales Credible</h2>
<p>Cash businesses are usually questioned on whether all sales were declared. The answer is a consistent trail: a daily sales summary or POS report, regular bank deposits that match it, and stock records showing purchases moving into sales. A shop that deposits takings irregularly, or keeps no daily figure, has little to show when an officer estimates sales from other information.</p>

<h2 id="lost">If Records Are Lost or Damaged</h2>
<ol>
<li>Record what happened and when, with any police report or insurance claim for theft or fire.</li>
<li>Rebuild what you can from bank statements, supplier ledgers, marketplace reports and copies held by your accountant.</li>
<li>Ask suppliers and customers for copies of invoices.</li>
<li>Keep a note of what could not be recovered and why; Section 174(2) allows deductions to be disallowed only where you cannot provide evidence <em>without reasonable cause</em>.</li>
</ol>

<h2 id="other-records">Records for Advance Tax and Withholding</h2>
<p>Keep advance tax PSIDs and paid challans with the tax year they relate to, so they can be claimed in the return. If you deduct tax from others, keep the payroll calculations, rent agreements, supplier details, deposit challans and quarterly statements as a separate set; see our {a(W, 'withholding guide')} for the full list.</p>
""", [
    ("What evidence works best for rent?",
     "A rent agreement, bank transfers to the landlord and, where you deducted tax, the deposit challan."),
    ("What if my records were destroyed?",
     "Document the event, rebuild what you can from bank statements and third-party copies, and keep a note of what was lost; Section 174(2) allows disallowance only where evidence is missing without reasonable cause."),
    ("How do I support cash sales?",
     "Keep daily sales summaries or POS reports, deposit takings regularly so bank deposits match, and keep stock records."),
])

EXTRA["close-sole-proprietorship-remove-business-ntn-pakistan"] = (f"""
<h2 id="settling">Settling With Employees, Landlord and Suppliers</h2>
<ul>
<li><strong>Employees:</strong> pay final salaries and dues, deduct tax under Section 149 on the final payments where due, and give each employee a certificate of tax deducted.</li>
<li><strong>Landlord:</strong> if annual rent was Rs 1.5 million or more, deduct and deposit tax on the last rent payments under Section 155, and keep proof the premises were handed back.</li>
<li><strong>Suppliers:</strong> if you were a prescribed person under Section 153, apply withholding to final payments as usual.</li>
<li><strong>Statements:</strong> file the Section 165 statement for the last quarter in which you deducted tax. Missing it attracts the Section 182 penalty even after closure.</li>
</ul>

<h2 id="credits">Do Not Lose Your Credits</h2>
<p>Adjustable tax deducted by customers from your payments, and adjustable tax collected up to closure (for example on monthly electricity bills above Rs 30,000 under Section 235(4)(b)), are credits in your final return. Collect the certificates before you lose touch with customers, and download the statements available on IRIS. If credits and advance tax paid exceed the tax for the year, the excess can be claimed through the refund process.</p>

<h2 id="online-close">Closing an Online Store</h2>
<p>Marketplace and courier accounts are linked to your NTN. Settle pending orders and returns, download all settlement and cash-on-delivery statements for the year, and close or deactivate the seller and courier accounts. Those statements are the sales record for your final return.</p>

<h2 id="restart">Restarting Later</h2>
<p>If you start trading again, add the new or restarted business to your registration through Form 181, as explained in our guide to {a(I, 'adding a business on IRIS')}. Your earlier records still need to be kept for the full six years.</p>

<h2 id="full-checklist">Closure Checklist</h2>
<ul>
<li>☐ Closing date fixed and recorded.</li>
<li>☐ Stock counted and valued; decision on sale, personal use or write-off recorded.</li>
<li>☐ Employees, landlord and suppliers settled; final withholding deducted and deposited.</li>
<li>☐ Last Section 165 statement filed, if applicable.</li>
<li>☐ Withholding certificates collected from customers.</li>
<li>☐ Online store and courier accounts settled and statements downloaded.</li>
<li>☐ RTO application for discontinuance submitted, receipt kept.</li>
<li>☐ Business bank account closed after tax is settled.</li>
<li>☐ Final-year return and wealth statement filed by 30 September.</li>
<li>☐ Records archived for six years.</li>
</ul>
""", [
    ("Do I need to file withholding statements after closing?",
     "Yes, for the last quarter in which you deducted tax. Missing it attracts a Section 182 penalty even after the business has closed."),
    ("What happens to tax customers deducted from me before closure?",
     "It is a credit in your final return; collect the certificates before you lose contact with customers."),
    ("Can I restart the business later?",
     "Yes. Add it again through Form 181 when you restart, and keep the earlier records for the full six years."),
])
