"""Second depth pass for the Form ATL-U series."""
from atlu_common import a, table, B, X

EXTRA = {
"filer-fee-2026-pakistan-late-filer-cost": ("", [
    ("Is there a discount if I file several years together?", "Our pricing page offers a combined quote for multiple years. Message us with the years you need and we confirm the total before starting."),
]),

"late-filer-tax-on-property-sale-form-atl-u": (f"""
<h2 id="checklist">Seven Days Before the Transfer: A Checklist</h2>
<ol>
<li>Check your ATL status online or by SMS. If you are not on the list, do not go ahead on the planned date.</li>
<li>Confirm the gross consideration figure that will appear on the transfer papers; Section 236C applies to the gross amount.</li>
<li>Make sure your CNIC on the transfer papers matches the CNIC on IRIS, so the tax collected is credited to you.</li>
<li>Ask the society or registrar how the advance tax will be collected and get the challan copy afterwards.</li>
<li>Keep the purchase deed or allotment letter for the property you are selling; the gain is worked out from its cost.</li>
<li>Note the sale in your records for the Tax Year 2027 return.</li>
<li>Re-read your Form ATL-U end date before you discuss any new purchase with the buyer or a dealer.</li>
</ol>
""", [
    ("What if the transfer date comes before my name appears on the ATL?", "Section 236C will collect 11.5%. Either move the date, or pay the surcharge if that gets you on the list sooner for an urgent transfer."),
]),

"late-filer-tax-on-bank-profit-form-atl-u": (f"""
<h2 id="ask-bank">Questions to Ask Your Bank</h2>
<ul>
<li>"On what date did you last check my ATL status?" Banks check at payment, so a recent change may not show until the next payment.</li>
<li>"Can you give me a withholding tax certificate for July 2025 to June 2026?" You need it for the return.</li>
<li>"Is my CNIC correctly linked to every account and deposit?" A wrong CNIC means the tax may not appear against you on IRIS.</li>
<li>"When does my deposit next pay profit?" That tells you the deadline for getting onto the list.</li>
</ul>
<p>A bank cannot put you on the ATL or refund over-deducted tax; only FBR's list and your return do that. What the bank can do is apply the right rate once your name is there.</p>
""", [
    ("Can my bank refund the extra tax it deducted?", "No. The bank deposits the tax with FBR. You claim any excess through your return once you are on the ATL."),
]),

"form-atl-u-property-purchase-6-months-breach": (f"""
<h2 id="already">If You Think You Have Already Breached</h2>
<p>Do not ignore it and do not hide it. Three practical steps:</p>
<ol>
<li><strong>Write down the facts</strong>: what was acquired, on what date, in whose name and from whose money.</li>
<li><strong>Get advice on whether it is a breach at all.</strong> A family member's own purchase, or an instalment on an interest you already held, may not be.</li>
<li><strong>If it is a breach, consider the surcharge.</strong> The rules, as notified, withdraw the benefit from the date of breach and apply the ordinary rule, which is the surcharge. Being ready to show you understood and acted promptly is better than waiting for FBR to raise it.</li>
</ol>
<p>The electronic hearing the rules provide for is your chance to explain. Go into it with documents, not memories.</p>
""", [
    ("I booked a plot by mistake in month four. What now?", "Write down the facts and get advice. If it is a breach, the benefit is withdrawn from the breach date and the surcharge rule applies; acting early is better than waiting for FBR."),
]),

"form-atl-u-salaried-pensioners-late-return": (f"""
<h2 id="penalty-salaried">How the Penalty Works for a Salaried Person</h2>
<p>Section 182 sets the penalty as the higher of 0.1% of the tax payable for each day of default or Rs 1,000 for each day. For a salaried person with modest tax, the Rs 1,000 a day figure is usually the higher one. A minimum of Rs 10,000 applies where 75% or more of income is from salary, and the maximum is 200% of tax payable. The amount is then reduced by 75% if the return is filed within one month after the due date, 50% within two months and 25% within three.</p>
<p>"Tax payable" is defined in the Explanation to the entry as the higher of the tax on the assessed income for the year or the tax payable for the preceding year for which a return was duly filed. We work the actual figure out from your return and show it to you before filing.</p>

<h2 id="why-late">Why Salaried Returns Go Late, and How to Stop It</h2>
{table(["Reason", "Fix for next year"], [
    ["Employer certificate arrives late", "Ask HR in July; most payroll systems can issue it early"],
    ["Waiting for the deadline extension", "Do not count on one; file in August"],
    ["Wealth statement feels difficult", "Keep a one-page list of assets each June"],
    ["IRIS password lost", "Reset it in July, not on the last day"],
    ["Assuming tax deducted means no return", "The return is required regardless"],
])}

<h2 id="employer-tip">If Your Employer Deducted Too Little</h2>
<p>Payroll sometimes under-deducts, for example when bonuses come late in the year or when you had two employers. The return calculates the full tax on the year's salary; any shortfall is paid with the return before filing. Pay it through the PSID, keep the challan, and the return is complete. Underpayment is not a reason to delay: the penalty grows each day the return is late.</p>
""", [
    ("Is the Rs 10,000 minimum penalty reduced if I file within a month?", "The law reduces the amount of penalty by 75% for a return filed within one month after the due date. We work out the exact figure from your return before filing."),
]),

"form-atl-u-freelancers-traders-overseas": (f"""
<h2 id="remote">How We Work With You, Wherever You Are</h2>
<p>Most of our freelance, trader and overseas clients never visit the office. The process runs on WhatsApp and email:</p>
<ol>
<li>You send your CNIC, IRIS login status and a short description of your income.</li>
<li>We send a list of the exact documents needed for your case, with the fee in writing.</li>
<li>You upload statements and papers; we prepare the return and wealth statement.</li>
<li>We send a summary of the figures for your approval, including any tax and the penalty.</li>
<li>After approval and payment of any tax through PSID, we file, furnish Form ATL-U, and send you every acknowledgement.</li>
<li>After FBR's next ATL update, we confirm your status.</li>
</ol>
<p>We reply within office hours, Monday to Saturday 9:00 to 18:00, Friday until 12:30. For overseas clients in the Gulf, UK or North America, that usually means a reply the same working day.</p>
""", [
    ("Do I need to visit your office?", "No. Freelancers, traders and overseas clients can complete everything on WhatsApp and email."),
]),

"filer-kaise-bane-2026-form-atl-u": (f"""
<h2 id="hum-kaise">Hamare Saath Kaam Kaise Hota Hai</h2>
<ol>
<li>WhatsApp par CNIC aur apni aamdani ki mukhtasar tafseel bhejein.</li>
<li>Hum aap ko zaroori kaghzat ki list aur fees likh kar bhejte hain.</li>
<li>Return aur wealth statement tayyar karke figures aap ko dikhate hain.</li>
<li>Aap ki manzoori ke baad tax aur penalty ka PSID banta hai, aap bank ya app se jama karte hain.</li>
<li>Hum return file karte hain, Form ATL-U jama karte hain aur dono acknowledgements bhejte hain.</li>
<li>Agli ATL update ke baad status check karke aap ko batate hain.</li>
</ol>
<p>Hum office hours mein jawab dete hain: Peer se Hafta 9:00 se 18:00, Juma 12:30 tak. Itwaar chhutti.</p>
""", [
    ("Office aana zaroori hai?", "Nahi. Saara kaam WhatsApp aur email par ho jata hai, Pakistan mein kahin se bhi ya bahar se."),
]),
}
