"""Extra sections for the gap series (depth to 2,000+ words). Facts checked 20 November 2026 against the ITO amended to 30.06.2026
(ss.111, 114(4)-(5), 137, 168-170, 182A, 205, 231AB) and the IRS W-8BEN instructions."""
from gap_common import *

MORE = {}

MORE[SL["adj"]] = f"""
<h2 id="refund">When Adjustable Tax Becomes a Refund</h2>
<p>Because Section 168 treats adjustable deductions as tax already paid, they can exceed the tax actually due. That happens often: a salaried person whose employer missed a zakat or pension adjustment, a retiree whose bank deducted tax on profit while other income is low, or a trader whose advance tax on electricity and vehicle tokens adds up to more than the year's liability. The excess is refundable, but Section 182A(1)(c) blocks refunds while you are off the Active Taxpayers List. Filing on time is therefore what turns a credit into cash.</p>
<p>Final tax works the opposite way. Section 169 says the tax deducted is the final liability on that income, so it can never produce a refund, even in a year when your total income is below the taxable threshold.</p>

<h2 id="return">Where Each Type Sits in the IRIS Return</h2>
{table(["Type", "Where it goes", "Effect on your bill"], [
    ["Adjustable deductions (e.g. salary, Section 236C, Section 231AB)", "Tax credits / adjustable withholding taxes", "Reduces the tax payable; excess refundable"],
    ["Final tax income (e.g. prize bonds)", "Final / fixed tax part of the return", "Tax already settled; no adjustment"],
    ["Separately taxed income (e.g. Section 7B profit on debt)", "Its own schedule, with the deduction credited", "Usually nil further tax"],
    ["Minimum tax", "Compared against the normal calculation", "You pay the higher of the two"],
])}
<p>Putting an item in the wrong part is the most common reason a return shows a demand that is not real, or a refund that FBR later reverses.</p>

<h2 id="filer-rates">Why the ATL Changes the Arithmetic</h2>
<p>Many adjustable and separate taxes are deducted at a higher rate from people off the ATL. Bank profit is taxed at 20% for a person on the list and 40% for others; the advance tax on selling property under Section 236C is 2.75% on the ATL against 11.5% off it. Even though most of these amounts are adjustable, the higher deduction ties up money until you file, and without the ATL a refund cannot be issued at all. Check where you stand with our <a href="{X["chk"]}">ATL status guide</a>.</p>
"""

MORE[SL["zak"]] = f"""
<h2 id="zakat-vs-donation">Zakat or Donation: Section 60 or Section 61?</h2>
{table(["Point", "Zakat (Section 60)", "Donation (Section 61)"], [
    ["Nature of relief", "Deductible allowance: reduces taxable income", "Tax credit: reduces tax at your average rate"],
    ["What qualifies", "Zakat paid under the Zakat and Ushr Ordinance 1980", "Donations to approved bodies and institutions named in the law"],
    ["Evidence", "Bank zakat certificate or receipt under the Zakat law", "Receipt from the approved recipient"],
    ["Unused amount", "Lost (Section 60(3))", "Limited by the Section 61 ceilings"],
])}
<p>Giving to a mosque, madrasa or relative as zakat is a religious duty, but for the income tax claim the question is whether it was paid under the Zakat law. If it was not, check whether the recipient is an approved body under Section 61; our <a href="{X["don"]}">donations guide</a> explains the credit. Claiming the same amount under both sections is not allowed.</p>

<h2 id="wealth">Zakat in Your Wealth Statement</h2>
<p>Zakat paid is money that leaves your wealth during the year. In the wealth statement it belongs among personal expenses and outflows, so that the opening wealth plus income minus outflows equals the closing wealth. If you leave it out, the statement shows wealth that has gone missing, which is exactly the kind of gap that leads to a Section 111 question about unexplained assets. Our <a href="{X["ws"]}">wealth statement guide</a> covers the reconciliation.</p>

<h2 id="timing">Timing Matters</h2>
<p>Section 60 allows zakat "paid by the person in the tax year". Banks usually deduct zakat on the first day of Ramadan, so the deduction falls in whichever tax year (1 July to 30 June) contains that date. Zakat paid directly counts in the year you actually paid it. A payment made after 30 June belongs to the next year's return, not the one you are filing.</p>
"""

MORE[SL["cash"]] = f"""
<h2 id="business">What It Means for Businesses and Traders</h2>
<p>Section 231AB applies to any "person" off the ATL, so it reaches individuals, associations of persons and companies alike. For a shop or distributor that draws cash daily to pay suppliers and staff, the cost compounds quickly:</p>
{table(["Daily cash drawn (off the ATL)", "Tax per day at 0.8%", "Over 300 working days"], [
    ["Rs 100,000", "Rs 800", "Rs 240,000"],
    ["Rs 250,000", "Rs 2,000", "Rs 600,000"],
    ["Rs 500,000", "Rs 4,000", "Rs 1,200,000"],
])}
<p>Every rupee of it is adjustable, but only for a business that files. For a sole proprietor, a return at the published fee of Rs 5,000 costs less than two days of this tax at Rs 250,000 a day.</p>

<h2 id="bank-side">How the Bank Applies It</h2>
<p>The deduction is the bank's legal duty, so a branch cannot waive it on request. Banks rely on FBR's Active Taxpayers List to decide who is a filer, and the list is updated by FBR, not by the bank. If you have just filed, keep the acknowledgement and check your status before a large withdrawal. Tax a bank deducts from you appears in your IRIS records and on the bank's tax certificate, which you use to claim the credit.</p>

<h2 id="dont">What Not to Do</h2>
<ul>
<li>Do not move business cash through relatives' accounts to avoid the deduction; it creates wealth statement gaps for everyone involved.</li>
<li>Do not assume an old article about "0.6%" is current; the Finance Act 2025 raised the rate to 0.8%.</li>
<li>Do not file a nil return just to get on the ATL if you have income; that trades a 0.8% deduction for a concealment problem. See <a href="{B["eva"]}">avoidance vs evasion</a>.</li>
</ul>
"""

MORE[SL["eva"]] = f"""
<h2 id="how-found">How Hidden Income Usually Comes to Light</h2>
<p>Section 111 is the provision most cases turn on. Where an amount is credited in a person's books, a person owns an investment, money or a valuable article, or has incurred expenditure, and offers no explanation of its nature and source, or an explanation the Commissioner does not find satisfactory, the amount is included in income under "Income from Other Sources" to the extent it is not adequately explained. The trigger is usually a mismatch: a property bought, a car registered or a foreign trip made that the declared income and wealth statement cannot support.</p>
<p>That is why a clean <a href="{X["ws"]}">wealth statement</a> is the best defence. When opening wealth, income, expenses and closing wealth reconcile, there is nothing unexplained. Our <a href="{X["wsr"]}">wealth reconciliation calculator</a> runs that check.</p>

<h2 id="checklist">A Planning Checklist That Stays Legal</h2>
{table(["Question", "If yes", "If no"], [
    ["Does the arrangement change who really owns or earns the money?", "Likely genuine", "Risk under Section 109"],
    ["Is every step documented (deed, bank transfer, agreement)?", "Defensible", "Expect questions"],
    ["Would you do it without the tax saving?", "Commercial purpose shown", "Main purpose may be tax"],
    ["Does your wealth statement still reconcile?", "Consistent", "Section 111 exposure"],
    ["Are you claiming a relief the Ordinance names?", "Planning", "Check before claiming"],
])}

<h2 id="penalty-math">The Cost of Getting It Wrong</h2>
<p>Take a trader who leaves Rs 2 million of sales out of a return and saves, say, Rs 300,000 of tax. If it is found, the tax is assessed, default surcharge runs on it under Section 205, and the concealment penalty under entry 12 of Section 182 is Rs 300,000 or Rs 100,000, whichever is higher. The revenue impact is under Rs 500,000, so Section 192A prosecution would not apply on these numbers; at a larger amount it would. Revising voluntarily before any audit or Section 122(9) notice, with the tax and surcharge paid, avoids the penalty entirely. Our <a href="{B["ds"]}">default surcharge guide</a> shows how the interest is worked out.</p>
"""

MORE[SL["w8"]] = f"""
<h2 id="which-form">W-8BEN, W-8BEN-E or W-9?</h2>
{table(["Form", "Who uses it", "Typical Pakistani case"], [
    ["W-8BEN", "Non-US individual (beneficial owner)", "Freelancer, consultant or investor paid in their own name"],
    ["W-8BEN-E", "Non-US entity", "A Pakistani private limited company or other entity receiving the payment"],
    ["W-9", "US person (citizen or resident)", "A Pakistani who is also a US citizen or green card holder"],
])}
<p>If you are a US citizen as well as Pakistani, the W-8BEN is the wrong form however long you have lived in Pakistan; US citizens are US persons for tax purposes.</p>

<h2 id="platform-steps">Filling It on a Platform: Step by Step</h2>
<ol>
<li>Open the tax information section of the platform and choose "individual" and "not a US person".</li>
<li>Enter your legal name exactly as on your CNIC or passport.</li>
<li>Enter your permanent residence address in Pakistan, with city and postal code.</li>
<li>Enter your NTN in the foreign TIN field. For an individual, FBR uses the CNIC number as the NTN.</li>
<li>Answer the question on US activity honestly. If you performed no work while physically in the US, say so.</li>
<li>Skip the treaty claim unless you have US-source income it applies to.</li>
<li>Sign electronically, then download and keep a copy.</li>
</ol>

<h2 id="records">Keep the Pakistani Paper Trail Too</h2>
<p>The payer keeps your W-8BEN; FBR never sees it. What FBR does see are the remittances arriving in your Pakistani bank accounts. Keep the platform's annual earnings statement, the bank's foreign remittance records, and your W-8BEN together. If FBR asks how your wealth grew, those three documents answer it in one go. They also support the income figure in your <a href="{X["free"]}">freelancer return</a>.</p>
"""

MORE[SL["sim"]] = f"""
<h2 id="notice">The Section 114(4) Notice Comes First</h2>
<p>Under Section 114(4), the Commissioner may, by written notice, require a person who in the Commissioner's opinion is required to file a return for a tax year, but has not, to file it within thirty days of service, or a longer or shorter period stated in the notice or allowed by the Commissioner. Under Section 114(5), such a notice may cover one or more of the last five completed tax years. The notice usually arrives in the IRIS inbox and, for some people, by post or courier.</p>
{table(["Stage", "What happens", "What you should do"], [
    ["1", "Section 114(4) notice issued", "Read it, note the tax years and the compliance date"],
    ["2", "Compliance period runs (30 days or as stated)", "File the return, or reply that you were not liable, with evidence"],
    ["3", "Date passes with no return", "You become eligible for a Section 114B general order"],
    ["4", "General order issued", "File immediately and apply for restoration"],
    ["5", "Restoration ordered under Section 114B(3)", "Keep the order and the return acknowledgement"],
])}

<h2 id="not-liable">If You Were Never Liable</h2>
<p>Some notices go to people who did not have to file, for example someone whose only link to a trigger was a property later sold, or a widow or orphan covered by Section 115(3). Section 114B(3)(b) allows restoration where the Commissioner is satisfied the person was not liable. Reply to the notice in writing, explain why you were not required to file for each year named, and attach evidence such as a sale deed, transfer letter or CNIC of the deceased spouse. A reply is still a reply; ignoring the notice is what leads to the order.</p>

<h2 id="cost">What a Late Return Costs Compared With a Block</h2>
<p>People sometimes delay because they fear the penalty. The Section 182 late filing penalty is real, and is reduced to 75%, 50% or 25% if the return is filed within one, two or three months of the due date. But a blocked phone, a disconnected meter or a stopped trip costs more in a day than a filed return costs in fees. Estimate your exposure with the <a href="{X["pen"]}">late filing penalty calculator</a> and compare it with our published fee for a return.</p>
"""

MORE[SL["inel"]] = f"""
<h2 id="scenarios">Three Worked Scenarios</h2>
{table(["Situation", "How Section 114C reads", "Result once in force"], [
    ["Salaried filer, Rs 8 million car; latest wealth statement shows Rs 7 million in bank and savings", "130% × Rs 7 million = Rs 9.1 million, above Rs 8 million", "Eligible"],
    ["Non-filer, Rs 6.5 million car", "Below the Rs 7 million threshold", "Not restricted by 114C"],
    ["Housewife with no return buying a Rs 120 million house funded by her husband, a filer", "Eligible person includes the spouse of an individual who is eligible", "Depends on the husband's declared resources covering the deal"],
])}
<p>The third case shows why the family proviso matters, and also why documents matter: the funding should be traceable from the husband's declared resources, and the gift or transfer should appear in both wealth statements.</p>

<h2 id="fits">How 114C Fits With Other Non-Filer Rules</h2>
{table(["Rule", "What it does", "Status"], [
    ["Section 231AB", "0.8% tax on non-ATL cash withdrawals above Rs 50,000 a day", "In force"],
    ["Higher advance taxes off the ATL", "e.g. bank profit 40% instead of 20%", "In force"],
    ["Section 114B", "SIM, power, gas and travel action against people liable to file", "In force"],
    ["Section 114C", "Blocks large purchases by ineligible persons; annual cash cap", "From the notified date"],
])}
<p>Section 114C is different from the others. It looks not only at whether you filed, but at whether your declared resources support the purchase. A filer with an understated wealth statement can be ineligible; a careful filer is not. See our guides to <a href="{B["cash"]}">cash withdrawal tax</a> and <a href="{B["sim"]}">Section 114B</a>.</p>

<h2 id="timeline">When to Start</h2>
<p>Because eligibility depends on the return for the tax year immediately before the transaction, preparation has to start a year ahead. Someone planning to buy a house in the year to 30 June 2027 relies on the tax year 2026 return, due 31 October 2026. If that return is filed and the wealth statement shows the cash and liquid assets that will fund the purchase, the test is met when the notification comes.</p>
"""

MORE[SL["ds"]] = f"""
<h2 id="vs-penalty">Default Surcharge vs Penalty vs ATL Surcharge</h2>
{table(["Charge", "Section", "Triggered by", "How it is worked out"], [
    ["Default surcharge", "205", "Paying tax, penalty or other amounts late", "Rate × amount × days"],
    ["Late filing penalty", "182", "Filing the return late", "Higher of 0.1% of tax payable or Rs 1,000 a day, with minimums and a cap"],
    ["ATL surcharge", "182A", "Filing late and wanting to join the ATL", "Rs 25,000 individual, Rs 50,000 AOP, Rs 100,000 company"],
    ["Concealment penalty", "182 (entry 12)", "Concealing income", "Higher of Rs 100,000 or the tax sought to be evaded"],
])}
<p>A person who files late and pays late can face the first three together. The <a href="{X["pen"]}">late filing penalty calculator</a> and the <a href="{X["atlroute"]}">ATL route calculator</a> cover the other two.</p>

<h2 id="dates">Counting the Days: A Dated Example</h2>
<p>A sole proprietor's tax year 2026 return shows Rs 240,000 payable. The due date was 31 October 2026. The return is filed on time, but the tax is paid on 15 January 2027.</p>
<ul>
<li>Days late: 1 November to 15 January = 76 days.</li>
<li>Default surcharge at 12%: 240,000 × 12% × 76 ÷ 365 = Rs 5,996.</li>
<li>If KIBOR plus 3% for the period was higher than 12%, Section 205(1) uses that rate instead.</li>
</ul>
<p>Paying in two parts? Work each part separately: the part paid earlier stops accruing on the day it is paid.</p>

<h2 id="instalment-example">An Advance Tax Example</h2>
<p>A company due to pay a Rs 1,000,000 quarterly instalment under Section 147 pays it 60 days late. Under Section 205(1A): 1,000,000 × 12% × 60 ÷ 365 = Rs 19,726. The surcharge stops at the date of payment or the return due date, whichever is earlier; it does not keep running into the next year on the same instalment.</p>
"""

DESC = {
    SL["zak"]: None,
    SL["cash"]: "Section 231AB: banks deduct 0.8% when a person off the ATL withdraws over Rs 50,000 cash in a day. Filers pay nothing. Rules, examples and recovery.",
    SL["eva"]: "Tax planning, avoidance schemes and evasion under Pakistani law: Section 109, the concealment penalty, Sections 192 and 192A, and safe ways to pay less.",
    SL["w8"]: "Form W-8BEN for freelancers in Pakistan: why US payers ask for it, each line explained, your NTN as foreign TIN, the treaty part, and your FBR tax.",
    SL["sim"]: "Section 114B lets FBR block SIMs, cut power and gas, and limit travel for people liable to file but not on the ATL. Conditions and how to restore.",
    SL["inel"]: "Section 114C: ineligible persons barred from cars above Rs 7m, property above Rs 100m and investments above Rs 50m once notified. Rules explained.",
    SL["ds"]: "Section 205 default surcharge: the higher of 12% or KIBOR plus 3% a year on unpaid tax, 12% on advance tax and withholding, with formula and examples.",
}
TITLE = {SL["inel"]: "Ineligible Person Section 114C: Thresholds and Rules 2026"}

MORE[SL["zak"]] += f"""
<h2 id="business">Business Owners, AOPs and Companies</h2>
<p>Section 60(1) gives the allowance to "a person" for zakat paid "by the person". Under the Ordinance a person includes an individual, an association of persons and a company, so the allowance is not limited to salaried individuals. Two conditions follow from the wording. The zakat must be paid by the same person who claims it: zakat a business owner pays personally is claimed in the owner's return, not the firm's, and zakat paid by a company is claimed by the company. And it must be paid under the Zakat and Ushr Ordinance 1980.</p>
<p>Section 60(2) adds one exclusion: zakat already taken into account under Section 40(2), the provision on deductions against income from other sources, cannot be claimed again under Section 60. The same amount is never deducted twice.</p>

<h2 id="checklist">A Checklist Before You Claim</h2>
{table(["Check", "Why it matters"], [
    ["Was it paid under the Zakat and Ushr Ordinance 1980?", "Only that zakat qualifies under Section 60(1)"],
    ["Was it paid in this tax year (1 July to 30 June)?", "The allowance is for zakat paid in the tax year"],
    ["Did the same person pay and claim it?", "The allowance belongs to the person who paid"],
    ["Is there enough normal taxable income to absorb it?", "Unused allowance is lost under Section 60(3)"],
    ["Is it already deducted under Section 40(2)?", "No double deduction (Section 60(2))"],
    ["Do you hold the bank certificate or receipt?", "Evidence if FBR asks"],
    ["Is it shown as an outflow in the wealth statement?", "Keeps the reconciliation clean"],
])}
"""

MORE[SL["cash"]] += f"""
<h2 id="overseas">Overseas Pakistanis and Non-Residents</h2>
<p>Section 231AB does not exempt non-residents. The test is only whether the person's name appears on the Active Taxpayers List. An overseas Pakistani who keeps a resident account in Pakistan, is not on the ATL, and withdraws more than Rs 50,000 in cash in a day will have 0.8% deducted. Many overseas Pakistanis file a return precisely to stay on the ATL; our published fee for an overseas Pakistani return is Rs 6,000. Note that Section 114C, if and when notified, treats non-residents differently: they are outside its vehicle, property and investment restrictions but not its cash withdrawal cap.</p>

<h2 id="quick-calc">Work It Out Yourself</h2>
<p><strong>Tax = total cash withdrawn in the day × 0.8%</strong>, if the day's total exceeds Rs 50,000 and you are not on the ATL. The tax is on the whole day's total, not only the part above Rs 50,000: the section applies the rate to "the cash withdrawal" once the day's sum total crosses the limit. Add up withdrawals from the counter, cheques encashed and ATM withdrawals made in a day when you check.</p>
<p>Over a year, add up the deductions shown on your bank's tax certificate. That total is the credit you claim when you file.</p>
"""

MORE[SL["eva"]] += f"""
<h2 id="abetment">Advisers, Family Members and Abetment</h2>
<p>Section 199 makes it an offence to knowingly and wilfully aid, abet, assist, incite or induce another person to commit an offence under the Ordinance, punishable with a fine or imprisonment up to three years, or both. That covers anyone who knowingly helps build a false return or a sham arrangement, including an adviser, an accountant or a relative who lends their name. Section 200 also reaches the principal officers and directors of a company or AOP where the entity commits an offence. A good adviser protects you by refusing to do what would put both of you at risk.</p>
"""

MORE[SL["sim"]] += f"""
<h2 id="prevent">How to Make Sure It Never Happens</h2>
<ul>
<li><strong>Keep your IRIS contact details current.</strong> Notices go to the email, mobile and address on your record.</li>
<li><strong>File by the due date every year.</strong> For tax year 2026 that was 31 October 2026; a timely return keeps you on the ATL.</li>
<li><strong>Answer every notice</strong>, even when you believe you were not liable. A written reply with evidence is what Section 114B(3)(b) relies on.</li>
<li><strong>Check the ATL after filing.</strong> FBR updates the list; your name should appear after the next update.</li>
</ul>
"""

MORE[SL["inel"]] += f"""
<h2 id="companies">Companies and AOPs</h2>
<p>For a company or an association of persons, the eligibility test uses the financial statements attached to the return for the latest tax year instead of a wealth statement: sufficient resources are 130% of the cash and equivalent assets shown there. Public companies are outside the vehicle, property and investment restrictions altogether under Section 114C(2). A private company planning a large purchase should therefore make sure its last audited accounts, filed with the return, show the liquid resources the purchase will draw on.</p>
"""
