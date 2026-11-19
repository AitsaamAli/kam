"""Depth sections for the Form ATL-U series (merged by extras.py into the body before the service section)."""
from atlu_common import a, table, B, X

EXTRA = {
# ── IRIS ──
"form-atl-u-iris-submit-step-by-step": (f"""
<h2 id="troubleshoot">Troubleshooting: What Goes Wrong and the Fix</h2>
{table(["What you see", "Likely cause", "What to do"], [
    ["Cannot log in; code not received", "Mobile number or email on IRIS is old", "Update registered contact details through FBR's procedure before anything else"],
    ["Return shows as Draft", "It was saved but never submitted", "Open it, complete it, verify and submit; then note the new acknowledgement"],
    ["Form asks for an acknowledgement number you cannot find", "Looking at the tax payment instead of the return", "Open the completed return; the acknowledgement is on the return, not the challan"],
    ["Name not on the ATL after an update", "Wealth statement missing, wrong tax year, or form not submitted", "Check each in that order; most cases are one of these three"],
    ["Bank still deducts the higher rate", "The bank checked before your name appeared", "Show the bank your current status; later payments should change"],
])}

<h2 id="records">The File You Should Keep</h2>
<p>Keep a single folder, paper or digital, with these items for at least six years:</p>
<ul>
<li>The Tax Year 2026 return acknowledgement and the return itself.</li>
<li>The wealth statement and its reconciliation.</li>
<li>The PSID challans for tax and any penalty paid.</li>
<li>The Form ATL-U acknowledgement, with the six-month end date written on it.</li>
<li>A screenshot of your ATL status once your name appears.</li>
</ul>
<p>If a bank, a housing society or a registrar later questions your filer status for that year, this folder answers them in minutes.</p>

<h2 id="representative">Filing for a Parent or Spouse</h2>
<p>Many people handle IRIS for an elderly parent or a spouse. That is allowed in practice when you act with their permission, but remember whose undertaking it is. The declaration is made in the taxpayer's name; they are the one promising not to obtain property for six months. Explain the promise to them in plain words before you submit, and make sure no family property transfer into their name is planned. A parent who is about to receive a plot from a sibling's share of an inheritance, for example, may be better served by the surcharge.</p>

<h2 id="after-submit">After You Submit: The Next Six Months</h2>
<p>Set two reminders: one for the date FBR usually updates the ATL, to check your status, and one for the day after your six months end. Between those dates, if anyone in the family discusses buying or transferring property to you, pause and check before agreeing to anything. This is the stage where most innocent breaches happen.</p>
""", [
    ("Do I need a tax practitioner to submit Form ATL-U?", "No. Any individual can furnish it on IRIS. People use a consultant when the late return itself needs preparation, or when IRIS access is a problem."),
    ("Can I edit Form ATL-U after submitting?", "Treat a submitted undertaking as final. If you entered a wrong detail, contact us or your tax office promptly rather than submitting a second form without advice."),
]),

# ── Active late filer ──
"active-late-filer-meaning-form-atl-u-2026": (f"""
<h2 id="cases">Three Cases, Worked Through</h2>
<h3>Case 1: Filed on 5 November 2026, nothing else done</h3>
<p>The return is late, so under Section 182A(1)(a) the person is not on the ATL for Tax Year 2026. Any status check shows them as not active. Their bank deducts profit tax at the increased rate. Fix: Form ATL-U (if no property plans) or the surcharge.</p>
<h3>Case 2: Filed late, paid the Rs 25,000 surcharge</h3>
<p>The person is included in the ATL once FBR's list reflects the payment. Before 1 July 2026, rule 1A would have charged them separate rates as a late filer on the ATL; with rule 1A omitted, they now pay ordinary filer rates. The surcharge was the price of not having to keep a six-month promise.</p>
<h3>Case 3: Filed late, furnished Form ATL-U</h3>
<p>Same result as Case 2, without the Rs 25,000, as long as no property is obtained in the six months. If they breach, the benefit is withdrawn from the breach date and they are back to needing the surcharge.</p>

<h2 id="who-checks">Who Checks Your Status, and When</h2>
{table(["Who", "When they check", "What depends on it"], [
    ["Your bank", "Each time profit is paid", "Rate under Section 151"],
    ["Property registrar or housing society", "At registration or transfer", "Rates under Sections 236C and 236K"],
    ["Motor vehicle registering authority", "At registration", "Rate under Section 231B"],
    ["Companies and fund managers", "At dividend payment", "Rate on dividends"],
    ["Employers and other payers", "When deducting withholding tax", "Withholding rates covered by rule 1"],
])}
<p>Because each check happens at the time of the transaction, two people with identical returns can pay different amounts depending only on when their names reached the list. That is why we file the return and the ATL route on the same day.</p>

<h2 id="old-years">If Older Years Are Also Missing</h2>
<p>The ATL looks at the return for one tax year, but your wealth statement links every year to the one before. If Tax Years 2024 and 2025 were never filed, the 2026 wealth statement has nothing to reconcile from, and assets may look unexplained. It is usually better to file the missing years at the same time, carefully, rather than leave a gap that a later notice will find.</p>
""", [
    ("Is 'active late filer' an official FBR status?", "It came from rule 1A of the Tenth Schedule, which referred to persons on the ATL who had not filed by the due date. That rule was omitted by the Finance Act 2026."),
    ("Can I be active for one year and inactive for another?", "Yes. The ATL relates to a tax year. Filing one year late does not change your status for a year you filed on time, and vice versa."),
]),

# ── Filer fee ──
"filer-fee-2026-pakistan-late-filer-cost": (f"""
<h2 id="pay-penalty">How the Penalty Is Paid</h2>
<p>The Section 182 penalty is paid to FBR through a payment slip (PSID) generated on IRIS, the same way income tax is paid. It is not paid to us and it is not part of our fee. We work out the figure from your return before filing, show it to you, and generate the PSID for you to pay through your bank, mobile app or ATM. Keep the paid challan with your return papers.</p>

<h2 id="what-included">What Our Fee Covers, and What It Does Not</h2>
{table(["Included in our fee", "Not included"], [
    ["Preparing the return from your documents", "Tax payable on your income"],
    ["Preparing the wealth statement and reconciliation", "FBR's Section 182 penalty"],
    ["Filing both on IRIS", "The Rs 25,000 surcharge, if you choose that route"],
    ["Form ATL-U (Rs 2,000, if you choose that route)", "Earlier years' returns (quoted separately)"],
    ["ATL status check after FBR's next update", "Responding to notices on returns filed by others"],
])}

<h2 id="earlier-years">Filing Earlier Years at the Same Time</h2>
<p>If you have never filed, or skipped years, the cheapest moment to fix them is now. A wealth statement for 2026 that starts from nothing can make savings, property or a vehicle look unexplained. Filing the missing years in order lets each wealth statement reconcile with the one before. Each late year carries its own penalty question, so we look at the full picture and quote before starting. Our {a(X["ws"], "wealth statement guide")} explains how the reconciliation works.</p>

<h2 id="decision">A Two-Question Decision</h2>
<ol>
<li><strong>Are you an individual?</strong> If you are filing for an AOP or company, Form ATL-U is not available; the surcharge is Rs 50,000 or Rs 100,000.</li>
<li><strong>Will any property come to you in six months?</strong> If no, Form ATL-U costs Rs 2,000 with us instead of Rs 25,000 to FBR. If yes, or maybe, pay the surcharge.</li>
</ol>
<p>That is the whole decision. Everything else on the bill (tax, penalty, return fee) is the same either way.</p>

<h2 id="value">Why Not Just Stay a Non-Filer?</h2>
<p>Some people weigh these costs and decide to skip filing. The arithmetic rarely supports it. A non-filer pays increased withholding on every bank profit payment, dividend and vehicle registration, and 11.5% instead of 2.75% on any property sale. Section 114C of the Ordinance, added by the Finance Act 2025, also sets out restrictions on certain transactions by 'ineligible persons', which come into force from dates the Federal Government notifies. The direction of the law is clear: filing gets more valuable each year.</p>
""", [
    ("Do I pay the penalty to you or to FBR?", "To FBR, through a PSID challan. Our fee is separate and covers preparing and filing."),
    ("Is the Rs 2,000 for Form ATL-U paid to FBR?", "No. FBR charges nothing for the undertaking. Rs 2,000 is our fee for preparing and furnishing it."),
]),

# ── Property sale ──
"late-filer-tax-on-property-sale-form-atl-u": (f"""
<h2 id="example">A Worked Example</h2>
<p>Ahmed filed his Tax Year 2026 return on 12 November 2026, after the deadline. He has agreed to sell a house in Lahore for Rs 1.8 crore, with transfer planned for mid-January 2027. He has no plans to buy property before summer.</p>
{table(["Step", "Date", "Result"], [
    ["Return and wealth statement filed (house declared)", "12 November 2026", "Return complete, but Ahmed is not on the ATL"],
    ["Form ATL-U furnished on IRIS", "20 November 2026", "Six months run to 19 May 2027"],
    ["Name appears on the ATL", "After FBR's next update", "Filer rates now apply"],
    ["Transfer at the society or registrar", "Mid-January 2027", "Section 236C at 2.75%: Rs 495,000"],
])}
<p>Had Ahmed transferred while still off the ATL, Section 236C would have collected 11.5%: Rs 2,070,000. The difference, Rs 1,575,000, is far more than any fee or surcharge. His only discipline is not to put the sale money into another property before 20 May 2027.</p>

<h2 id="joint">Jointly Owned Property</h2>
<p>When two or more people sell a jointly owned property, each owner's share is a separate seller's share for advance tax, and each owner's own ATL status matters. A brother on the ATL and a sister off it may pay different rates on their halves. If any co-owner filed late, they should complete their own ATL route before the transfer. Form ATL-U is personal: one co-owner's undertaking does not cover another.</p>

<h2 id="poa">Selling Through a Power of Attorney</h2>
<p>Overseas owners often sell through an attorney in Pakistan. The tax is collected with reference to the owner, not the attorney, so it is the owner's ATL status that counts. The owner can file the return and furnish Form ATL-U on IRIS from abroad. Check the status before the attorney goes to the registrar.</p>

<h2 id="papers">What to Keep Ready for the Transfer</h2>
<ul>
<li>A screenshot of your ATL status on the day before transfer.</li>
<li>Your Form ATL-U acknowledgement, in case the official asks how a late filer appears on the list.</li>
<li>The Tax Year 2026 return acknowledgement.</li>
<li>Purchase documents, which you will need for the capital gain calculation in next year's return.</li>
</ul>
""", [
    ("Does each co-owner need their own Form ATL-U?", "Yes. The undertaking is personal to the individual who furnishes it. Each co-owner's ATL status decides the rate on their share."),
    ("Can an overseas owner selling through an attorney use Form ATL-U?", "Yes. The owner files the return and furnishes the form on IRIS from abroad; the owner's ATL status decides the rate."),
]),

# ── Bank profit ──
"late-filer-tax-on-bank-profit-form-atl-u": (f"""
<h2 id="pensioner-case">A Pensioner's Year, Worked Through</h2>
<p>Mrs Rehana, a retired teacher, holds Rs 3 million in a monthly-profit term deposit earning about Rs 25,000 a month. Her son filed her Tax Year 2026 return on 10 November 2026, after the deadline, and did nothing further.</p>
{table(["", "Off the ATL (40%)", "On the ATL (20%)"], [
    ["Monthly profit", "Rs 25,000", "Rs 25,000"],
    ["Tax deducted each month", "Rs 10,000", "Rs 5,000"],
    ["Paid to her each month", "Rs 15,000", "Rs 20,000"],
    ["Extra tax over six months", "Rs 30,000", "-"],
])}
<p>Six months off the list cost her Rs 30,000 in extra deductions, more than the Rs 25,000 surcharge and fifteen times our Rs 2,000 charge for Form ATL-U. She is not buying property, so the undertaking fits her exactly.</p>

<h2 id="certificate">Reading Your Bank's Tax Certificate</h2>
<p>Banks issue a withholding tax certificate for profit, usually on request or through internet banking. Check three things on it:</p>
<ul>
<li>The profit amount and the tax deducted for each period.</li>
<li>The rate: 20% means you were treated as on the ATL; 40% means you were not.</li>
<li>Your CNIC: if it is wrong, tax may not show against your name on IRIS.</li>
</ul>
<p>Use the certificate when preparing the return; the tax deducted is claimed there.</p>

<h2 id="timing">Monthly Profit vs Profit at Maturity</h2>
<p>For a savings account or monthly-profit deposit, each payment is a fresh check against the ATL, so the sooner you are on it, the sooner the rate drops. For a deposit that pays only at maturity, the check happens on the maturity date. If maturity is near, completing the ATL route before that date can decide the rate on a whole year's profit in one go.</p>

<h2 id="family">Accounts Held for Family Members</h2>
<p>Where a parent's savings are kept in a child's name or a joint account, the bank applies the ATL test according to its own records of the account holders. Make sure every person whose name is on the account and who has filed late completes their own ATL route. Form ATL-U is personal; one person's undertaking does not cover another.</p>
""", [
    ("Why does my bank certificate show 40%?", "You were not on the ATL when the profit was paid. Rule 1 of the Tenth Schedule increased the 20% rate by 100%."),
    ("If my deposit matures next month, should I hurry?", "Yes. The rate is decided on the payment date; being on the ATL by then applies 20% to the whole payment."),
]),

# ── What you cannot buy ──
"form-atl-u-property-purchase-6-months-breach": (f"""
<h2 id="household">Six Household Situations</h2>
{table(["Situation", "Fits Form ATL-U?", "Why"], [
    ["You plan to sell your plot and keep the money in the bank", "Yes", "Selling is not restricted"],
    ["Your father plans to gift you his house next month", "Risky", "A gift is a way to obtain ownership; delay it or pay the surcharge"],
    ["You paid the last instalment of a flat booked in 2023 and possession is due in March", "Risky", "Possession and transfer during the six months may be treated as acquiring; take advice"],
    ["Your adult son buys a car with his own salary", "Yes", "It is his purchase, from his money"],
    ["You give your brother money to buy a plot in his name 'for you'", "No", "That is a beneficial interest"],
    ["You will rent a new house for the family", "Yes", "A tenancy is not ownership"],
])}

<h2 id="evidence">Keep Evidence During the Six Months</h2>
<p>If a family member buys property during your six months, keep simple proof that it is theirs: their own bank transfer, their own name on every paper, and no payment from your account. If FBR's data ever links you to a transaction, this is what lets you explain it in the electronic hearing that the rules provide for before any withdrawal of the benefit.</p>

<h2 id="calendar">Mark the Calendar</h2>
<p>Write the end date on the acknowledgement, put it in your phone, and tell your spouse. The most common breach we hear about is a booking made on a property expo day in the fifth month, when the person had simply forgotten. A two-week buffer after the end date costs nothing and removes any argument about counting.</p>

<h2 id="vehicles-note">A Note on Vehicles</h2>
<p>Vehicles deserve a separate word because they are the commonest purchase. The Ordinance treats them in their own sections (231B for registration), and the undertaking does not mention them; but it does say "any property", and a car is property in ordinary language. Until FBR says otherwise, a car purchase in the six months is a risk we would not advise taking.</p>
""", [
    ("Can my family buy property while my undertaking runs?", "Yes, from their own money and for their own benefit. Keep evidence that the purchase is theirs."),
    ("Is a two-week buffer after six months necessary?", "Not legally, but it removes any dispute about how the six months are counted."),
]),

# ── Salaried ──
"form-atl-u-salaried-pensioners-late-return": (f"""
<h2 id="cases">Three Salaried Cases</h2>
<h3>Bilal, software engineer, Lahore</h3>
<p>Salary Rs 2.4 million; tax deducted by employer. Filed on 8 November 2026. No property plans; Rs 1.5 million in a savings account. Best route: Form ATL-U. With us: Rs 5,500, plus the Section 182 penalty to FBR, reduced by 75% because he filed within one month.</p>
<h3>Sana, bank officer, Karachi</h3>
<p>Salary Rs 3.6 million. Filed late. She is about to book an apartment in February 2027. Form ATL-U does not fit: booking is acquiring. Best route: the Rs 25,000 surcharge, so she is on the ATL and the buyer's rate under Section 236K is 1.25%, not 10.5% or more.</p>
<h3>Mr Aslam, retired, Faisalabad</h3>
<p>Pension plus profit on National Savings certificates. Filed late for the first time ever. No property plans. Best route: Form ATL-U, and a reminder for next July so it does not happen again.</p>

<h2 id="job-change">Changed Jobs During the Year?</h2>
<p>If you worked for two employers between July 2025 and June 2026, you need certificates from both. Each employer deducted tax on its own salary, often without knowing about the other, so the combined tax can be higher than what was deducted. The return brings both together; any shortfall is paid with the return. This is one of the commonest reasons salaried returns get delayed, and it is easy to fix.</p>

<h2 id="forget">Wealth Statement Items Salaried People Forget</h2>
<ul>
<li>A second bank account opened for savings or a committee.</li>
<li>Provident fund balances, where your employer reports them.</li>
<li>A motorcycle or car in your name, even if a family member uses it.</li>
<li>Gold received at a wedding.</li>
<li>Money lent to a relative, or owed to one.</li>
</ul>
<p>Each of these should be in the wealth statement at 30 June 2026. Leaving them out now and adding them later needs a revised statement, and our {a(X["r60"], "revision guide")} explains when that is possible.</p>
""", [
    ("I changed jobs during the year. Do I need both certificates?", "Yes. The return combines salary from both employers; any shortfall in tax is paid with the return."),
    ("I am booking a flat soon. Should I use Form ATL-U?", "No. Booking is acquiring property. Pay the surcharge so you are on the ATL for the purchase."),
]),

# ── Freelancers, traders, overseas ──
"form-atl-u-freelancers-traders-overseas": (f"""
<h2 id="cases">Three Cases</h2>
<h3>A graphic designer in Multan</h3>
<p>Receives about USD 1,500 a month from clients abroad through a bank. Filed Tax Year 2026 late. No property plans. Route: Form ATL-U. The return must match the remittances in the bank statements, and the wealth statement must show how savings grew. With us: Rs 7,000.</p>
<h3>A pharmacy owner in Gujranwala</h3>
<p>Runs the pharmacy as a sole proprietor. Filed late. Planning to buy the shop he rents in April 2027. Route: pay the surcharge. Form ATL-U would be breached by the purchase, and he needs the filer rate under Section 236K when he buys.</p>
<h3>An engineer in Riyadh</h3>
<p>Owns a plot in Islamabad and a house in Rawalpindi, files in Pakistan because of rent and a planned sale. Filed late. Selling the plot in February 2027; no purchase planned. Route: Form ATL-U from abroad on IRIS, so the sale is taxed at 2.75%. With us: Rs 8,000.</p>

<h2 id="records">Records Each Group Should Keep</h2>
{table(["Group", "Key records"], [
    ["Freelancer", "Bank statements showing foreign remittances, platform statements, invoices, any tax certificates from the bank"],
    ["Shopkeeper / sole proprietor", "Sales and purchase summaries, bank statements of the business account, rent agreement, utility bills and their tax certificates"],
    ["Overseas Pakistani", "Days in Pakistan during the tax year (for residence), rent agreements, property papers, Pakistani bank statements"],
])}

<h2 id="residence">A Note on Residence for Overseas Filers</h2>
<p>Your tax position in Pakistan depends heavily on whether you are resident for the tax year, which turns on the days you spent here and other tests in Section 82. A non-resident is taxed in Pakistan on Pakistan-source income; a resident on worldwide income. Get this right before filing, because it changes both the return and the wealth statement. It does not change your eligibility for Form ATL-U, which depends only on being an individual who filed late.</p>

<h2 id="next-year">Avoiding This Next Year</h2>
<p>Business and freelance returns take longer than salary returns because figures must be put together. Start in July, not September. The Tax Year 2027 due date under Section 118 is 30 September 2027, and an extension, if one comes, is never guaranteed.</p>
""", [
    ("Does residence status affect Form ATL-U?", "No. Eligibility depends on being an individual who filed after the due date. Residence affects what income goes in the return."),
    ("I plan to buy my rented shop. Should I use Form ATL-U?", "No. Buying the shop is acquiring property. Pay the surcharge so you are on the ATL when you buy."),
]),

# ── Roman Urdu ──
"filer-kaise-bane-2026-form-atl-u": (f"""
<h2 id="misalein">Teen Misalein</h2>
<h3>Usman, salaried, Lahore</h3>
<p>Return 7 November 2026 ko file ki, yani late. Agle 6 maah koi property nahi leni. Form ATL-U de kar Rs 25,000 bachaye. Hamari fees Rs 5,500, aur penalty mein 75% kami kyun ke 30 November se pehle file ki.</p>
<h3>Ayesha, freelancer, Islamabad</h3>
<p>Bahar ke clients se paisa aata hai. Return late. Bank profit par 40% kat raha tha. Form ATL-U ke baad ATL mein naam aaya to bank ne 20% kaatna shuru kiya. Hamari fees Rs 7,000.</p>
<h3>Tariq, dukandar, Sialkot</h3>
<p>Return late, lekin March 2027 mein plot lena hai. Form ATL-U un ke liye theek nahi, kyun ke plot lena "acquire" karna hai. Unhon ne Rs 25,000 surcharge diya taake plot khareedte waqt 1.25% wala rate lage.</p>

<h2 id="kaghzat">Zaroori Kaghzat</h2>
<ul>
<li>CNIC aur IRIS ka password (ya registered mobile number).</li>
<li>Salaried: employer ka salary certificate (July 2025 se June 2026).</li>
<li>Freelancer: bank statements jin mein bahar se aaya paisa nazar aaye.</li>
<li>Dukandar: saal bhar ki sale aur kharche ka khulasa, business account ki statement.</li>
<li>Sab ke liye: 30 June 2026 ko bank balance, plot, ghar, gaari, sona aur cash ki tafseel.</li>
<li>Bank aur bijli/mobile ke tax certificates, taake kata hua tax return mein credit ho.</li>
</ul>

<h2 id="property-bechna">Property Bechni Hai To?</h2>
<p>Form ATL-U sirf khareedne aur hasil karne par pabandi lagata hai, bechne par nahi. Is liye agar aap ne apna plot ya ghar bechna hai aur naya nahi lena, to Form ATL-U de kar ATL mein aa jayein aur 11.5% ke bajaye 2.75% advance tax dein. Rs 1 crore ki property par yeh farq Rs 875,000 banta hai. Tafseel hamari {a(B["sale"], "property sale guide")} mein.</p>

<h2 id="agla-saal">Agle Saal Yeh Masla Na Ho</h2>
<p>Tax Year 2027 ki return ki aakhri tareekh Section 118 ke mutabiq 30 September 2027 hai. Salaried log July ya August mein hi file kar lein, jaise hi employer certificate de. Waqt par file karne walon ke liye na surcharge hai, na undertaking, na penalty.</p>
""", [
    ("Kya main khud Form ATL-U jama kar sakta hoon?", "Haan, IRIS par koi bhi individual khud jama kar sakta hai. Log hamari madad tab lete hain jab return tayyar karni ho ya IRIS mein masla ho."),
    ("Biwi ke naam par plot le sakte hain?", "Agar paisa aap ka hai aur plot aap ke liye hai to yeh beneficial interest hai aur undertaking toot jati hai. Agar biwi apne paison se apne liye le to woh un ki khareed hai."),
]),
}
