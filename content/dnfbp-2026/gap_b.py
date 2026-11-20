"""Gap series posts 3-4: cash withdrawal tax; tax avoidance vs evasion."""
from gap_common import *

CASH = dict(
    slug=SL["cash"],
    svc=dict(h2="Stop Paying Tax Every Time You Withdraw Cash", intro="The cash withdrawal tax applies only to people off the Active Taxpayers List. We file your return, get you on the ATL, and claim the tax already deducted as a credit.",
             hook="Bank deducting 0.8% on your cash withdrawals?", fee=FEE_RET + " Late filers can rejoin the ATL with Form ATL-U for Rs 2,000.", btn="Get me on the ATL",
             items=["Your bank certificates checked for Section 231AB deductions",
                    "Return and wealth statement filed so you join the ATL",
                    "Form ATL-U or the surcharge route if your return is late",
                    "Section 231AB deductions claimed as an adjustable credit",
                    "A check that your bank applies the filer position after your name appears"],
             risks=["Each day's withdrawals above Rs 50,000 cost 0.8% while you are off the ATL",
                    "The deducted tax is only recovered through a filed return",
                    "Refunds are blocked while you are off the ATL"]),
    title="Cash Withdrawal Tax for Non-Filers in Pakistan 2026: 0.8%",
    h1="Cash Withdrawal Tax in Pakistan 2026: The 0.8% Charge on Non-Filers Under Section 231AB, and How to Stop It",
    crumb="Cash Withdrawal Tax 2026",
    description="Section 231AB: banks deduct 0.8% when a person off the ATL withdraws more than Rs 50,000 cash in a day. Filers pay nothing. How it works and how to recover it.",
    keywords="cash withdrawal tax, cash withdrawal tax for non filer 2026, cash withdrawal tax for filer, cash withdrawal tax in pakistan, atm cash withdrawal tax non filer, section 231ab, banking transaction tax pakistan",
    category="Tax Explainers", icon="🏧", read="10 min read",
    banner="If you are on the Active Taxpayers List, there is no tax on cash withdrawals. If you are not, every day above Rs 50,000 costs 0.8%.",
    tldr=("Section 231AB of the Income Tax Ordinance 2001 (inserted by the Finance Act 2023; rate raised from 0.6% to 0.8% by the Finance Act 2025) requires every "
          "banking company to deduct advance adjustable tax at 0.8% of cash withdrawals by a person whose name is not on the Active Taxpayers List, where the total cash "
          "withdrawn in a day exceeds Rs 50,000. The limit is the aggregate of all cash withdrawals in a single day. People on the ATL pay no cash withdrawal tax. "
          "The 100% increase in the Tenth Schedule does not apply to this deduction (rule 10(ga)). The tax is adjustable: a non-filer recovers it only by filing and "
          "claiming it as a credit, and refunds are issued only once on the ATL. The older cash withdrawal and banking transaction taxes in Sections 231A, 231AA and "
          "236P were omitted by the Finance Act 2021."),
    lead=("'Is there tax on cash withdrawal?' is one of the most searched tax questions in Pakistan, and the answer changed several times in the last few years. "
          "Here is the position as it stands in the Ordinance amended up to 30 June 2026, with the history that explains the confusion."),
    body=f"""
{SERIES("cash")}

<h2 id="law">What Section 231AB Says</h2>
<p>Every banking company shall deduct advance adjustable tax at the rate of 0.8% of the cash withdrawal from a person whose name is not appearing in the Active Taxpayers List, on the sum total of the payments for cash withdrawal in a day exceeding fifty thousand rupees. The Explanation adds that the Rs 50,000 is the aggregate of cash withdrawals in a single day.</p>
{table(["Point", "Rule"], [
    ["Who deducts", "The bank"],
    ["Who pays", "Only a person not on the Active Taxpayers List"],
    ["Rate", "0.8% of the cash withdrawn (Finance Act 2025; previously 0.6%)"],
    ["When", "Where total cash withdrawals in a day exceed Rs 50,000"],
    ["Nature", "Advance adjustable tax, credited in the return"],
    ["Tenth Schedule doubling", "Does not apply (Tenth Schedule rule 10(ga))"],
])}

<h2 id="filers">Do Filers Pay Cash Withdrawal Tax?</h2>
<p>No. Section 231AB applies only to persons whose names are not on the ATL. A person on the ATL can withdraw any amount of cash without this deduction. That is the whole difference, which is why getting on the list matters even for people with little or no taxable income.</p>

<h2 id="history">Why People Are Confused: The History</h2>
{table(["Provision", "What it did", "Status"], [
    ["Section 231A", "Tax on cash withdrawals above Rs 50,000 a day (non-ATL)", "Omitted by the Finance Act 2021"],
    ["Section 231AA", "Tax on banking instruments and transfers against cash", "Omitted by the Finance Act 2021"],
    ["Section 236P", "Tax on non-cash banking transactions (non-ATL)", "Omitted by the Finance Act 2021"],
    ["Section 231AB", "0.6% on non-ATL cash withdrawals above Rs 50,000 a day", "Inserted by the Finance Act 2023"],
    ["Section 231AB", "Rate raised to 0.8%", "Finance Act 2025"],
])}
<p>So for two years there was no cash withdrawal tax at all, then it returned for non-filers only. Articles written in that gap still circulate.</p>

<h2 id="examples">Worked Examples</h2>
{table(["Situation", "Tax deducted"], [
    ["Filer withdraws Rs 500,000 in a day", "Nil"],
    ["Non-filer withdraws Rs 40,000 in a day", "Nil (not above Rs 50,000)"],
    ["Non-filer withdraws Rs 30,000 twice on the same day (Rs 60,000)", "0.8% × Rs 60,000 = Rs 480"],
    ["Non-filer withdraws Rs 1,000,000 in a day", "0.8% × Rs 1,000,000 = Rs 8,000"],
])}
<p>A trader off the ATL who withdraws Rs 1 million in cash every week pays about Rs 8,000 a week, more than Rs 400,000 over a year, all for want of a filed return.</p>

<h2 id="recover">Recovering the Tax</h2>
<p>Because it is adjustable, tax deducted under Section 231AB is credited against your tax for the year under Section 168 when you file. If your total tax is lower than the credits, the excess is refundable, but Section 182A(1)(c) says no refund is issued while you are not on the ATL. The practical order is: file the return and wealth statement, join the ATL, then claim. If your return is late, an individual can join without the Rs 25,000 surcharge through <a href="{X["atlu"]}">Form ATL-U</a>.</p>

<h2 id="other-banking">Other Banking Taxes to Know</h2>
<ul>
<li><strong>Bank profit:</strong> 20% for people on the ATL, 40% for others. See the <a href="{X["bank"]}">bank profit tax calculator</a>.</li>
<li><strong>Online transfers and cheques:</strong> the older taxes on these were omitted in 2021; we found no current equivalent in the Ordinance.</li>
<li><strong>Section 114C(1)(d), a separate cap:</strong> the Fifteenth Schedule sets an annual cash withdrawal limit of Rs 100 million across all bank accounts held by an individual. Unlike the rest of Section 114C it covers any person, filer or not, but it applies only from a date the Federal Government notifies in the official Gazette (Section 114C(5)). See our <a href="{B["inel"]}">Section 114C guide</a>.</li>
</ul>

<h2 id="steps">How to Stop the Deduction</h2>
<ol>
<li>Check your ATL status with the <a href="{X["chk"]}">online or SMS check</a>.</li>
<li>If you are not on it, file the latest return and wealth statement.</li>
<li>If the return is late, use the surcharge or Form ATL-U route.</li>
<li>After FBR's next ATL update, your bank applies the filer position automatically at the next withdrawal.</li>
</ol>
""",
    faqs=[
        ("Is there a tax on cash withdrawal in Pakistan in 2026?", "Only for people not on the Active Taxpayers List. Section 231AB requires banks to deduct 0.8% where their cash withdrawals in a day exceed Rs 50,000."),
        ("Do filers pay cash withdrawal tax?", "No. Section 231AB applies only to persons whose names are not on the ATL."),
        ("What is the cash withdrawal tax rate for non-filers?", "0.8% of the cash withdrawn, since the Finance Act 2025 (previously 0.6%)."),
        ("Is the Rs 50,000 limit per transaction or per day?", "Per day: the Explanation says it is the aggregate of cash withdrawals in a single day."),
        ("Does the Tenth Schedule double the cash withdrawal tax?", "No. Rule 10(ga) of the Tenth Schedule excludes tax deducted under Section 231AB."),
        ("Can I get cash withdrawal tax back?", "It is adjustable: claim it in your return. Refunds are issued only once you are on the ATL."),
        ("Is there tax on ATM withdrawals?", "The same Section 231AB rule applies to cash withdrawals, whatever the channel, for persons off the ATL above Rs 50,000 a day."),
        ("Is there tax on online transfers?", "The older banking transaction taxes (Sections 231AA and 236P) were omitted in 2021; we found no current equivalent in the Ordinance."),
    ],
    sources=[S_ITO, S_ATL, S_FBR],
    related=[(X["atlu"], "Form ATL-U Guide"), (X["bank"], "Bank Profit Tax Calculator"), (B["inel"], "Ineligible Person Rules (114C)")],
    cta_h="Withdraw Cash Without the 0.8% Charge",
    cta_p="We file your return and get you on the ATL, then claim the tax already deducted.",
    wa_text="Assalam o Alaikum, bank cash withdrawal par tax kaat raha hai. ATL mein aana hai.",
)

EVA = dict(
    slug=SL["eva"],
    svc=dict(h2="Pay Less Tax the Legal Way, With Records That Hold Up", intro="Legal tax planning uses the allowances and credits the Ordinance gives and keeps a clean paper trail. We review your income, claim every legitimate relief, and fix past errors before they become concealment.",
             hook="Want to reduce tax without crossing the line?", fee=FEE_FIX, btn="Plan my taxes legally",
             items=["A review of credits and allowances you are not claiming: zakat, donations, pension fund, tax credits",
                    "Correct treatment of final, separate and adjustable taxes",
                    "Wealth statement checked for gaps that look like hidden income",
                    "Voluntary revision under Section 114(6A) where an error exists",
                    "Notice handling if FBR questions a transaction (from Rs 5,000)"],
             risks=["Concealment carries a penalty of Rs 100,000 or the full tax evaded, whichever is higher",
                    "False verification can lead to prosecution under Section 192",
                    "A scheme whose main purpose is avoiding tax can be recharacterised under Section 109"]),
    title="Tax Avoidance vs Tax Evasion in Pakistan: Where the Line Is",
    h1="Tax Avoidance vs Tax Evasion in Pakistan: What Is Legal, What Is a Crime, and What FBR Can Do (2026)",
    crumb="Tax Avoidance vs Evasion",
    description="Legal planning, tax avoidance schemes and tax evasion compared under Pakistan's law: Section 109, concealment penalties, Sections 192 and 192A, and safe ways to pay less.",
    keywords="tax avoidance and tax evasion difference, tax avoidance vs tax evasion pakistan, tax evasion punishment in pakistan, how to pay less tax in pakistan legally, section 109 tax avoidance scheme, concealment of income penalty",
    category="Tax Explainers", icon="🧭", read="12 min read",
    banner="Paying less tax is legal. Hiding income is not. Pakistan's law draws three lines, not two.",
    tldr=("Pakistan's Income Tax Ordinance 2001 (FBR text amended up to 30 June 2026) recognises three zones. Legal tax planning uses the allowances, credits and rates "
          "the law gives, such as zakat (Section 60), pension fund contributions (Section 63) and filing on time to stay on the Active Taxpayers List. A 'tax avoidance "
          "scheme', defined in Section 109(2) as any transaction where one of the main purposes is avoiding or reducing tax, can be disregarded or recharacterised by "
          "the Commissioner. Tax evasion, meaning concealing income or giving inaccurate particulars, attracts a penalty of Rs 100,000 or the tax sought to be evaded, "
          "whichever is higher (Section 182, entry 12), and can be prosecuted: up to two years' imprisonment where the revenue impact is Rs 500,000 or more (Section "
          "192A), and up to three years or a fine of up to Rs 100,000 for a knowingly false verification (Section 192)."),
    lead=("Most people use 'avoidance' and 'evasion' interchangeably. The law does not. One is planning, one is a scheme FBR can unwind, and one is an offence. "
          "Knowing where your arrangements sit is the cheapest tax advice you will ever get."),
    body=f"""
{SERIES("eva")}

<h2 id="three-zones">Three Zones, Not Two</h2>
{table(["Zone", "What it is", "Legal consequence"], [
    ["Tax planning", "Using reliefs the law offers, as intended", "None: this is your right"],
    ["Tax avoidance scheme", "A transaction whose main purpose includes reducing tax, without real substance", "Can be recharacterised or disregarded (Section 109)"],
    ["Tax evasion", "Concealing income, claiming false deductions, false statements", "Penalty and possible prosecution (Sections 182, 192, 192A)"],
])}

<h2 id="planning">Legal Tax Planning: What the Ordinance Itself Offers</h2>
<ul>
<li><strong>Zakat:</strong> a deductible allowance under Section 60. See our <a href="{B["zak"]}">zakat guide</a>.</li>
<li><strong>Charitable donations:</strong> a tax credit under Section 61, explained in our <a href="{X["don"]}">donations guide</a>.</li>
<li><strong>Approved pension fund:</strong> a Section 63 tax credit on contributions up to 20% of taxable income.</li>
<li><strong>Being on the ATL:</strong> the single biggest saving for most people. Bank profit is taxed at 20% instead of 40%, property sale advance tax at 2.75% instead of 11.5%, and there is no cash withdrawal tax.</li>
<li><strong>Claiming every adjustable credit:</strong> see <a href="{B["adj"]}">adjustable vs final tax</a>.</li>
<li><strong>Choosing the right structure</strong> for a business, sole proprietorship, AOP or company, for real commercial reasons.</li>
</ul>

<h2 id="section-109">Tax Avoidance Schemes: Section 109</h2>
<p>Section 109(1) lets the Commissioner, in determining liability: recharacterise a transaction, or part of one, entered into as part of a tax avoidance scheme; disregard a transaction without substantial economic effect; recharacterise a transaction where the form does not reflect the substance; and, from tax year 2018, disregard an entity or corporate structure without economic or commercial substance or created as part of a tax avoidance scheme.</p>
<p>Section 109(2) defines a tax avoidance scheme as "any transaction where one of the main purposes of a person in entering into the transaction is the avoidance or reduction of any person's liability to tax". Section 109(3) adds that reduction includes avoidance or deferral of tax and an increase in a refund.</p>
<p>The test is not whether you saved tax, but whether the arrangement has real substance. Paper transfers to relatives, sham partnerships or loans that are never repaid are the typical targets.</p>

<h2 id="evasion">Tax Evasion: Concealment and Its Penalty</h2>
<p>Entry 12 of the Section 182 table covers a person who has concealed income or furnished inaccurate particulars of income, including suppressing income or claiming a deduction for expenditure not actually incurred. The penalty is Rs 100,000 or an amount equal to the tax the person sought to evade, whichever is higher. The entry also says no penalty is payable for the mere disallowance of a claim of exemption or of a declared expense, unless it is proved the person made the claim knowing it to be wrong. Honest mistakes are treated differently from deliberate ones.</p>

<h2 id="prosecution">When It Becomes a Crime</h2>
{table(["Section", "Offence", "Punishment"], [
    ["192", "Knowingly false statement in a verification in a return or document", "Fine up to Rs 100,000 or imprisonment up to three years, or both"],
    ["192A", "Concealment or inaccurate particulars with revenue impact of Rs 500,000 or more", "Imprisonment up to two years, or fine, or both"],
    ["199", "Knowingly and wilfully aiding, abetting or inducing another person to commit an offence", "Fine or imprisonment up to three years, or both"],
])}

<h2 id="grey">Grey Areas We Are Often Asked About</h2>
<ul>
<li><strong>Putting property in a spouse's name:</strong> legal if the spouse genuinely owns it and paid for it or received a documented gift; risky if it is a paper arrangement.</li>
<li><strong>Cash business sales not recorded:</strong> that is concealment, not planning.</li>
<li><strong>Splitting income among family members who do not work in the business:</strong> likely to be recharacterised.</li>
<li><strong>Using an approved pension fund to earn the Section 63 credit:</strong> planning, exactly as the law intends.</li>
</ul>

<h2 id="fix">If You Have Already Crossed the Line</h2>
<p>Voluntary correction is far cheaper than waiting. Under Section 114(6A), a revised return filed before an audit or Section 122(9) notice, with tax and default surcharge paid, carries no penalty; after the Commissioner points out tax, 25% of the leviable penalties applies; after a show cause notice, 50%. Our guide to <a href="{X["rev"]}">revising before a notice</a> explains the steps.</p>
""",
    faqs=[
        ("What is the difference between tax avoidance and tax evasion?", "Avoidance uses arrangements to reduce tax; where its main purpose is reducing tax without substance, Section 109 lets the Commissioner disregard or recharacterise it. Evasion is concealing income or giving false particulars, which carries penalties and can be prosecuted."),
        ("Is tax avoidance legal in Pakistan?", "Ordinary planning using reliefs the law offers is legal. A transaction that is a 'tax avoidance scheme' under Section 109(2) can be disregarded or recharacterised, though it is not by itself a crime."),
        ("What is the punishment for tax evasion in Pakistan?", "A penalty of Rs 100,000 or the tax sought to be evaded, whichever is higher (Section 182 entry 12); prosecution with up to two years' imprisonment where the revenue impact is Rs 500,000 or more (Section 192A)."),
        ("What is the penalty for a false statement in a return?", "Section 192: a fine up to Rs 100,000 or imprisonment up to three years, or both, if the person knows the statement is false."),
        ("Is a disallowed expense the same as concealment?", "No. Entry 12 says the mere disallowance of a claim does not attract the concealment penalty unless the claim was made knowing it to be wrong."),
        ("How can I legally pay less tax in Pakistan?", "Claim zakat, donations and pension credits, stay on the ATL, claim every adjustable credit, and structure your business for genuine commercial reasons."),
        ("Can I fix a past understatement without a penalty?", "Yes, by revising voluntarily before an audit or Section 122(9) notice and paying the tax and default surcharge (Section 114(6A))."),
        ("What is a tax avoidance scheme?", "Section 109(2): any transaction where one of the main purposes of entering into it is avoiding or reducing any person's tax liability."),
    ],
    sources=[S_ITO, S_IRIS, S_FBR],
    related=[(X["rev"], "Revise Before a Notice"), (B["zak"], "Zakat Deduction"), (X["notice"], "FBR Notice Defence")],
    cta_h="Plan Legally, Sleep Soundly",
    cta_p="We claim every relief the law gives and fix past errors before they become concealment.",
    wa_text="Assalam o Alaikum, legal tareeqe se tax kam karna hai aur purani ghalti theek karni hai.",
)
