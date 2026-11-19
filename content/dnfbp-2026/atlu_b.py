"""Form ATL-U series, posts 4-6."""
from atlu_common import *
from atlu_a import PEN_NOTE

# ───────────────────────────── 4. Filer fee 2026 ─────────────────────────────
FEE = dict(
    slug=SL["fee"],
    svc=dict(h2="One Fixed Price: Return Plus Form ATL-U", intro="You know the full cost before we start. The return fee is the one published on our pricing page; Form ATL-U adds Rs 2,000. FBR's own penalty, if any, is calculated and shown to you before filing, and you pay it directly to FBR.",
             hook="Want the full cost before you decide?", fee=F_ALL, btn="Tell me my total cost",
             items=["Your exact professional fee from the published price list, in writing",
                    "Your Section 182 penalty worked out from your return, before filing",
                    "A side-by-side of surcharge vs Form ATL-U for your situation",
                    "Return, wealth statement and Form ATL-U filed on IRIS",
                    "ATL status checked after FBR's next update"],
             risks=["Paying an agent's 'filer fee' that quietly includes a surcharge you did not need",
                    "Filing only a bare return to save money, then facing a notice over the wealth statement",
                    "Waiting past 30 November 2026 and losing the 75% penalty reduction"]),
    title="Filer Fee 2026: What a Late Filer Really Pays in Pakistan",
    h1="Filer Fee 2026 in Pakistan: The Real Cost of Becoming a Filer After the Deadline, Line by Line",
    crumb="Filer Fee 2026",
    description="There is no single 'filer fee'. The real 2026 cost for a late filer, line by line: return, penalty, Rs 25,000 surcharge or Form ATL-U, and our fees.",
    keywords="filer fee 2026, filer fees in pakistan 2026, non filer to filer fee, atl fee fbr 2026, atl surcharge fee, late filer fee 2026, filer fee after deadline",
    category="Form ATL-U", icon="💰", read="11 min read",
    banner="People ask 'how much is the filer fee?' The honest answer is that FBR charges no fee for being a filer. Here is what a late filer actually pays in 2026, and how to cut it.",
    tldr=("FBR does not charge any fee to become a filer. Filing a return on IRIS is free. A person becomes a filer in practice by appearing on the Active Taxpayers List, "
          "which requires a return filed for the relevant tax year. Costs arise only in three places: the tax on your income, if any; the Section 182 penalty if the return "
          "is late; and, for a late filer, the Section 182A surcharge of Rs 25,000 (individual), Rs 50,000 (AOP) or Rs 100,000 (company) to be included in the ATL. An "
          "individual who will not obtain property for six months can replace the surcharge with Form ATL-U, which costs nothing at FBR. Professional fees, where you use a "
          "consultant, are separate: ours are published."),
    lead=("'Filer fee' is one of the most searched tax phrases in Pakistan, and also one of the most misunderstood. Some agents quote a single number that hides what is "
          "inside it. This guide breaks the cost into its real parts, using the law as it stands after the Finance Act 2026, so you can see what you must pay and what you can avoid."),
    body=f"""
{SERIES}

<h2 id="no-fee">FBR Charges No Fee to Become a Filer</h2>
<p>There is no "filer registration fee" in the Income Tax Ordinance. NTN registration on IRIS is free for an individual, and so is filing a return. The word "filer" is shorthand for a person on the Active Taxpayers List, and the only way onto that list is a filed return. Anyone quoting a fixed "filer fee" is quoting their own service charge, possibly with FBR amounts folded in.</p>

<h2 id="parts">The Five Possible Cost Lines</h2>
{table(["Cost line", "Paid to", "When it applies", "Can it be avoided?"], [
    ["Income tax on the return", "FBR", "If your income is above the exemption or tax was under-deducted", "No; it is your tax"],
    ["Section 182 late-filing penalty", "FBR", "Return filed after the due date", "Reduced by filing early (see below)"],
    ["Section 182A ATL surcharge", "FBR", "Late filer who wants to be on the ATL", "Yes for an individual, through Form ATL-U"],
    ["Wealth statement", "Nobody, if you prepare it", "Required with an individual's return in most cases", "It is part of a complete return"],
    ["Professional fee", "Your consultant", "If you use one", "Optional, but a wrong return costs more"],
])}

<h2 id="surcharge">The Surcharge Line in Detail</h2>
<p>The proviso to Section 182A(1)(a), as amended by the Finance Act 2026, says a person who files after the due date is included in the ATL on paying a surcharge of:</p>
{table(["Person", "Surcharge before Finance Act 2026", "Surcharge from 1 July 2026"], [
    ["Individual", "Rs 1,000", "Rs 25,000"],
    ["Association of persons", "Rs 10,000", "Rs 50,000"],
    ["Company", "Rs 20,000", "Rs 100,000"],
])}
<p>For an individual, a twenty-five-fold increase turned the surcharge from a nuisance into a real decision. That is why the same Finance Act added Section 182A(3), the undertaking that FBR has now put into Form ATL-U.</p>

<h2 id="penalty">The Penalty Line in Detail</h2>
<p>{PEN_NOTE}</p>
<p>The reductions are time-sensitive. For Tax Year 2026 the extended due date was 31 October 2026, so:</p>
{table(["Return filed by", "Reduction in penalty"], [
    ["30 November 2026 (within one month)", "75%"],
    ["31 December 2026 (within two months)", "50%"],
    ["31 January 2027 (within three months)", "25%"],
    ["After that", "None"],
])}
<p>Our {a(X["calc"], "late-filing penalty calculator")} gives an estimate; we confirm the figure from your actual return before filing.</p>

<h2 id="scenarios">Three Real-World Totals</h2>
<p>These use our published fees and leave out tax and penalty, which depend on each return.</p>
{table(["Situation", "Surcharge route", "Form ATL-U route", "Saving"], [
    ["Salaried employee, late, no property plans", "Rs 3,500 fee + Rs 25,000 to FBR = Rs 28,500", "Rs 3,500 + Rs 2,000 = Rs 5,500", "Rs 23,000"],
    ["Freelancer, late, no property plans", "Rs 5,000 + Rs 25,000 = Rs 30,000", "Rs 5,000 + Rs 2,000 = Rs 7,000", "Rs 23,000"],
    ["Overseas Pakistani, late, selling a plot", "Rs 6,000 + Rs 25,000 = Rs 31,000", "Rs 6,000 + Rs 2,000 = Rs 8,000", "Rs 23,000"],
])}
<p>The saving is the same Rs 23,000 in every case because the undertaking replaces the Rs 25,000 surcharge and our charge for preparing it is Rs 2,000. The question is not the money but whether you can honestly keep the six-month promise.</p>

<h2 id="hidden">Costs People Forget</h2>
<ul>
<li><strong>Doubled withholding while you wait.</strong> Every month off the ATL, a bank deducts tax on profit at the increased rate. That money comes back only through a refund claim, and Section 182A(1)(c) blocks refunds while you are off the ATL.</li>
<li><strong>Earlier years.</strong> If earlier returns are missing, the wealth statement for 2026 may not reconcile. Fixing that later costs more than doing it now.</li>
<li><strong>Breaking the undertaking.</strong> If you buy property within six months, the waiver is withdrawn and the surcharge rule applies. Pick the route that fits your real plans.</li>
</ul>

<h2 id="agents">How to Read an Agent's Quote</h2>
<p>Ask for every quote in lines: professional fee, FBR penalty, FBR surcharge (if any). Ask whether the surcharge is included and whether you qualify for Form ATL-U instead. Ask for the IRIS acknowledgement of everything filed in your name. A consultant who cannot separate these lines is asking you to trust a number you cannot check.</p>

<h2 id="non-filer">Non-Filer to Filer: The Full Path</h2>
<ol>
<li>NTN on IRIS, if you have never registered: free at FBR (our fee Rs 2,000 if you want it done).</li>
<li>Tax Year 2026 return and wealth statement.</li>
<li>Tax and any penalty paid.</li>
<li>Form ATL-U (no property for six months) or surcharge.</li>
<li>ATL checked after the next update.</li>
</ol>
""",
    faqs=[
        ("What is the filer fee in Pakistan in 2026?", "FBR charges no fee to become a filer. Late filers may owe the Section 182 penalty and, to join the ATL, a surcharge of Rs 25,000 (individual) unless they use Form ATL-U."),
        ("What is the non-filer to filer fee?", "There is no FBR fee for it. You file the return; if it is late, the penalty and the ATL route (surcharge or Form ATL-U) apply."),
        ("Is the ATL surcharge the same as the late-filing penalty?", "No. The penalty is under Section 182 for missing the due date; the surcharge is under Section 182A for inclusion in the ATL after a late return."),
        ("How much is the ATL fee for an individual in 2026?", "The surcharge is Rs 25,000 from 1 July 2026, up from Rs 1,000. An individual who furnishes Form ATL-U does not pay it."),
        ("How much do you charge for Form ATL-U?", "Rs 2,000 for preparing and furnishing it, added to the published return fee: Rs 5,500 total for a salaried return."),
        ("Can I reduce the late-filing penalty?", "Yes, by filing quickly. Under the current text it falls by 75% if the return is filed within one month after the due date, 50% within two months and 25% within three."),
        ("Is NTN registration free?", "Yes, at FBR. We charge Rs 2,000 if you want us to register you."),
        ("Do I pay the surcharge and Form ATL-U both?", "No. They are alternative routes; the undertaking replaces the surcharge for an individual."),
    ],
    sources=[S_ITO, S_SRO, S_ATL, S_IRIS],
    related=[(X["calc"], "Late Filing Penalty Calculator"), (B["guide"], "Form ATL-U Complete Guide"), (X["pricing"], "Our Published Fees")],
    cta_h="Know Your Full Cost Before You File",
    cta_p="Published fees, your penalty worked out, and the cheapest ATL route that fits.",
    wa_text="Assalam o Alaikum, 2026 ki return late hai. Total kitna kharcha ayega (fee, penalty, ATL)?",
)

# ───────────────────────────── 5. Property sale ─────────────────────────────
SALE = dict(
    slug=SL["sale"],
    svc=dict(h2="Selling Soon? Get on the ATL Before the Transfer", intro="Timing is everything in a sale. We file the late return, furnish Form ATL-U, confirm your name is on the ATL and only then tell you it is safe to proceed with the transfer at the filer rate.",
             hook="Selling property while off the ATL?", fee=F_ALL, btn="Get me on the ATL before my sale",
             items=["A check of your ATL status today and the date your sale is likely to register",
                    "Late Tax Year 2026 return and wealth statement filed, showing the property correctly",
                    "Form ATL-U furnished, so the Rs 25,000 surcharge is not needed",
                    "Confirmation once your name is on the ATL, before the transfer",
                    "Guidance on capital gain on the sale for next year's return"],
             risks=["Transferring before your name appears means 11.5% instead of 2.75%",
                    "Using the sale money to book another property within six months breaches the undertaking",
                    "Leaving the property out of the wealth statement creates a mismatch the registrar's data can expose"]),
    title="Late Filer Tax on Property Sale 2026: 2.75% or 11.5%?",
    h1="Late Filer Tax on Property Sale in 2026: Why the Rate Is 2.75% or 11.5%, and How Form ATL-U Gets You the Lower One",
    crumb="Late Filer Property Sale Tax",
    description="Selling property after filing late? The Section 236C rate is 2.75% on the ATL and 11.5% off it. How Form ATL-U puts sellers on the ATL without Rs 25,000.",
    keywords="late filer tax on property sale, non filer tax on property sale 2026, late filer property sale tax, 236c tax rate 2026 late filer, sell property without atl, form atl u property sale",
    category="Form ATL-U", icon="🏠", read="12 min read",
    banner="On a Rs 1 crore sale, the advance tax is Rs 275,000 if you are on the ATL and Rs 1,150,000 if you are not. Late filers who are only selling can usually close that gap with Form ATL-U.",
    tldr=("When immovable property is sold, Section 236C requires advance tax to be collected from the seller at registration or transfer. Under Division X of Part IV of the "
          "First Schedule, as substituted by the Finance Act 2026, the rate for a person on the Active Taxpayers List is 2.75% of the gross consideration. The Tenth Schedule sets "
          "11.5% for a person not on the ATL. A late filer is off the ATL until the surcharge is paid or, for an individual, Form ATL-U is furnished. The undertaking restricts "
          "purchasing, acquiring or obtaining ownership or beneficial interest in property for six months; it says nothing against selling. A seller with no purchase planned can "
          "therefore join the ATL without the Rs 25,000 surcharge and sell at 2.75%."),
    lead=("Most late filers who call us in November have one urgent question: 'My property transfer is next month. How much tax will I pay?' The answer depends almost entirely on "
          "whether your name is on the ATL on the day of transfer. Here is the law, the numbers, and the order of steps that protects you."),
    body=f"""
{SERIES}

<h2 id="rates">The Rates in the Law</h2>
{table(["Seller's status", "Section 236C rate", "Where it comes from"], [
    ["On the ATL", "2.75% of gross consideration", "First Schedule, Part IV, Division X (Finance Act 2026)"],
    ["Not on the ATL", "11.5% of gross consideration", "Tenth Schedule, rule 1, third proviso table"],
])}
<p>Two changes in the Finance Act 2026 matter for sellers. First, Division X now has a single 2.75% rate for filers, replacing the earlier slab table of 4.5%, 5% and 5.5% by value. Second, rule 1A of the Tenth Schedule, which charged separate higher rates to people who were on the ATL but had filed late, was omitted. A late filer who reaches the ATL is now charged exactly what an on-time filer pays.</p>

<h2 id="numbers">What the Difference Looks Like</h2>
{table(["Sale value", "Advance tax at 2.75%", "Advance tax at 11.5%", "Extra paid off the ATL"], [
    ["Rs 50 lakh", "Rs 137,500", "Rs 575,000", "Rs 437,500"],
    ["Rs 1 crore", "Rs 275,000", "Rs 1,150,000", "Rs 875,000"],
    ["Rs 2.5 crore", "Rs 687,500", "Rs 2,875,000", "Rs 2,187,500"],
])}
<p>Against those numbers, Rs 25,000 for the surcharge looks small, and many sellers pay it out of fear. If you are not buying anything in the next six months, there is no need: Form ATL-U achieves the same ATL inclusion.</p>

<h2 id="why-allowed">Why Selling Is Compatible With Form ATL-U</h2>
<p>Section 182A(3) asks an individual to declare that he "shall not purchase, acquire, or otherwise obtain ownership or beneficial interest in any property" for six months. Each verb is about something coming <em>to</em> you. Disposing of property you already own is not among them. The undertaking was designed for exactly the person who needs ATL status without buying.</p>
<p>The risk is what happens to the sale money. If it goes into a new plot, a booking, a file or a flat within six months, the undertaking is broken. Plan the reinvestment for after the six months, or pay the surcharge instead.</p>

<h2 id="order">The Order of Steps That Protects You</h2>
<ol>
<li><strong>Check your status now</strong> with the {a(X["chk"], "online or SMS check")}.</li>
<li><strong>File the Tax Year 2026 return and wealth statement.</strong> The property you are selling should already be in the wealth statement at its cost.</li>
<li><strong>Furnish Form ATL-U</strong> and keep the acknowledgement.</li>
<li><strong>Wait for your name to appear on the ATL.</strong> The rate is applied according to the list at the time of transfer.</li>
<li><strong>Proceed with the transfer.</strong> Ask for the challan showing tax at 2.75%.</li>
</ol>
<p>If the buyer is pushing for a date earlier than the next ATL update, you have two choices: move the date, or pay the surcharge and accept the cost for certainty. We help you weigh that on the day.</p>

<h2 id="tax-credit">Is the 236C Tax Final?</h2>
<p>Advance tax under Section 236C is adjustable against your tax on the capital gain for the year of sale, not a final tax in itself. That is another reason to be on the ATL: Section 182A(1)(c) blocks refunds while a person is not on the ATL, so excess tax collected at the higher rate can stay locked. The capital gain itself is reported in the return for the tax year in which the sale happens, the Tax Year 2027 return for a sale now.</p>

<h2 id="overseas">Overseas Sellers</h2>
<p>Non-resident Pakistanis who own property here face the same Section 236C rates. If you have not filed, or filed late, the same two routes apply. Our {a(B["free"], "guide for freelancers, traders and overseas Pakistanis")} covers the overseas angle, including filing from abroad.</p>

<h2 id="buyer-side">What About the Buyer?</h2>
<p>The buyer pays advance tax under Section 236K: 1.25% on the ATL, and 10.5%, 14.5% or 18.5% by value off it. If you are the buyer and a late filer, Form ATL-U is not for you: buying is what it forbids. Pay the surcharge, or use our {a(X["cmp"], "comparison guide")} to think it through.</p>

<h2 id="mistakes">Mistakes Sellers Make</h2>
<ul>
<li>Filing the return but not the ATL route, then discovering at the registrar that they are still off the list.</li>
<li>Assuming 'active late filer' rates still apply. Rule 1A is gone since 1 July 2026.</li>
<li>Selling one property and booking another within the six months.</li>
<li>Omitting the property from the wealth statement and creating a mismatch with the registrar's records.</li>
</ul>
<p>Our main guide on {a(X["sale"], "tax on property sale in Pakistan")} covers gains, holding periods and the buyer's side in more depth.</p>
""",
    faqs=[
        ("What is the tax on property sale for a late filer in 2026?", "It depends on the ATL. On the ATL, Section 236C collects 2.75%; off it, 11.5%. Rule 1A, which set separate rates for late filers on the ATL, was omitted by the Finance Act 2026."),
        ("Can I sell property after furnishing Form ATL-U?", "The undertaking forbids purchasing, acquiring or obtaining ownership or beneficial interest in property for six months. Selling is not among those, so a sale does not breach it."),
        ("Do I need to pay Rs 25,000 to sell at the filer rate?", "Not if you are an individual who can keep the six-month undertaking. Form ATL-U replaces the surcharge."),
        ("When is the rate decided?", "At the time of transfer, according to whether you appear on the ATL. Make sure your name is on the list before the transfer date."),
        ("Is the 236C advance tax final?", "No. It is adjustable against tax on the capital gain in the return for the year of sale."),
        ("Can I reinvest the sale proceeds in a new plot?", "Not within the six months if you used Form ATL-U. That would be acquiring property. Wait, or pay the surcharge instead."),
        ("What did 'active late filer' sellers pay before?", "From 1 July 2024 to 30 June 2026, rule 1A of the Tenth Schedule charged them separate higher rates. That rule no longer applies."),
        ("Does the buyer's status affect my tax?", "No. The seller pays 236C based on the seller's status; the buyer pays 236K based on the buyer's."),
    ],
    sources=[S_ITO, S_SRO, S_ATL, S_IRIS],
    related=[(X["sale"], "Tax on Property Sale 2026"), (B["buy"], "What You Cannot Buy for 6 Months"), (B["guide"], "Form ATL-U Complete Guide")],
    cta_h="Sell at 2.75%, Not 11.5%",
    cta_p="We get you on the ATL with Form ATL-U before your transfer date.",
    wa_text="Assalam o Alaikum, main property bechne wala hoon aur late filer hoon. Form ATL-U ke zariye ATL mein aana hai.",
)

# ───────────────────────────── 6. Bank profit ─────────────────────────────
BANK = dict(
    slug=SL["bank"],
    svc=dict(h2="Stop the Double Deduction on Your Bank Profit", intro="Every month off the ATL, your bank takes more. We file the late return and wealth statement, furnish Form ATL-U, confirm your ATL status and, where tax was over-deducted, claim it in your return.",
             hook="Bank deducting double tax on your profit?", fee=F_ALL, btn="Fix my bank profit tax",
             items=["Your bank tax certificates reviewed for the rate actually deducted",
                    "Tax Year 2026 return and wealth statement filed, with all accounts declared",
                    "Form ATL-U furnished, so no Rs 25,000 surcharge",
                    "ATL status confirmed and a note for your bank to apply the filer rate",
                    "Excess deductions claimed through the return once you are on the ATL"],
             risks=["Each profit payment while off the ATL is taxed at the increased rate",
                    "Refunds are blocked under Section 182A(1)(c) until you are on the ATL",
                    "Leaving an account out of the wealth statement creates a mismatch with bank data"]),
    title="Late Filer Tax on Bank Profit: 20% or 40%? Form ATL-U Fix",
    h1="Late Filer Tax on Bank Profit in 2026: Why Your Bank May Be Deducting Double, and How Form ATL-U Stops It",
    crumb="Late Filer Bank Profit Tax",
    description="Off the ATL after a late return? Bank profit tax under s.151 rises from 20% to 40%. How Form ATL-U restores the filer rate for savers and pensioners.",
    keywords="late filer tax on bank profit, non filer tax on bank profit 2026, bank profit tax late filer, section 151 rate non atl, form atl u bank profit, pensioner late filer bank tax",
    category="Form ATL-U", icon="🏦", read="11 min read",
    banner="Savers and pensioners feel a late return first in their bank statement. Here is why the deduction doubles and how to bring it back to 20% without paying Rs 25,000.",
    tldr=("Section 151 requires a bank to deduct tax on profit paid on an account or deposit. Division IA of Part III of the First Schedule sets the rate at 20%. Rule 1 of "
          "the Tenth Schedule increases withholding rates by 100% for a person not on the Active Taxpayers List, so the bank deducts 40%. A person who filed the Tax Year 2026 "
          "return after the due date stays off the ATL until the Section 182A surcharge is paid or, for an individual, Form ATL-U is furnished. Savers who are not buying property "
          "in the next six months can use the undertaking and return to the 20% rate without paying the Rs 25,000 surcharge. Refunds of excess deductions are blocked while off the ATL."),
    lead=("For a pensioner living on profit from a savings certificate or term deposit, the difference between 20% and 40% is the difference between a manageable deduction "
          "and a painful one. The fix is the same as for every late filer, but the urgency is higher because every profit payment counts."),
    body=f"""
{SERIES}

<h2 id="how-rate">How the Bank Decides the Rate</h2>
<p>When a bank pays profit, it checks whether the account holder appears on the ATL. If yes, it deducts at 20% under Division IA. If not, rule 1 of the Tenth Schedule applies: "the rate of tax required to be deducted or collected... shall be increased by hundred percent." The specific row that once set a separate 35% non-filer rate for Section 151 was omitted by the Finance Act 2025, so the general 100% increase now governs: 20% becomes 40%.</p>
<p>The check happens at each payment. A deposit that pays profit monthly is checked every month; a term deposit that pays at maturity is checked at maturity. That makes the date your name reaches the ATL matter.</p>

<h2 id="numbers">What It Costs You</h2>
{table(["Annual profit", "Deducted at 20%", "Deducted at 40%", "Extra deducted"], [
    ["Rs 100,000", "Rs 20,000", "Rs 40,000", "Rs 20,000"],
    ["Rs 300,000", "Rs 60,000", "Rs 120,000", "Rs 60,000"],
    ["Rs 600,000", "Rs 120,000", "Rs 240,000", "Rs 120,000"],
])}
<p>On Rs 300,000 a year of profit, about Rs 5,000 extra goes every month. In about five months the extra deduction equals the whole Rs 25,000 surcharge, and with Form ATL-U you avoid both.</p>

<h2 id="late">Why a Late Filer Is Treated Like a Non-Filer</h2>
<p>Section 182A(1)(a) keeps a person who files after the due date off the ATL for that year. The bank does not see "late filer"; it sees a name that is not on the list. Until the surcharge is paid or Form ATL-U is furnished, the doubled rate applies even though the return is filed.</p>

<h2 id="refund">Can You Get the Extra Back?</h2>
<p>Tax deducted under Section 151 from an individual's bank profit falls under Section 7B, which taxes an individual's profit on debt up to Rs 5 million separately from other income. Tax deducted above your actual liability is claimed through the return. Two limits apply:</p>
<ul>
<li>Section 182A(1)(c): no refund is issued while you are not on the ATL.</li>
<li>Section 182A(1)(d): the period off the ATL is not counted for the additional payment for delayed refunds under Section 171.</li>
</ul>
<p>Joining the ATL quickly protects both the rate going forward and your ability to recover what was over-deducted. Our {a(X["bank"], "bank profit tax guide")} covers how Section 7B and the rates work for filers.</p>

<h2 id="pensioners">Pensioners and Widows</h2>
<p>Many people living on profit have no other income and assume they do not need to file. If profit is your main income and tax has been deducted, filing and being on the ATL is what keeps the deduction at 20%. Form ATL-U is well suited to this group: few pensioners are buying property, and the undertaking replaces the Rs 25,000 surcharge.</p>
<p>A pension itself is treated under the salary head in many cases, and our {a(B["sal"], "Form ATL-U guide for salaried people and pensioners")} covers that side.</p>

<h2 id="steps">Steps to Return to the 20% Rate</h2>
<ol>
<li>Collect the tax deduction certificates from each bank for July 2025 to June 2026.</li>
<li>File the Tax Year 2026 return, declaring every account in the wealth statement.</li>
<li>Furnish Form ATL-U and keep the acknowledgement.</li>
<li>Check the ATL after the next update, then inform your bank branch so later payments use the filer rate.</li>
<li>Review the next certificate to confirm the rate changed.</li>
</ol>

<h2 id="other">Other Deductions That Double</h2>
<p>Rule 1 is general. Dividends, some contract and service payments, and other withholding and collection taxes in the Ordinance also rise by 100% for people off the ATL. Motor vehicle registration tax under Section 231B rises by 200%. If you receive dividends from shares or mutual funds, the same fix applies.</p>

<h2 id="penalty">The Late-Filing Penalty</h2>
<p>{PEN_NOTE} For a person with little tax payable, the minimum is usually the figure that applies, and the reduction for filing within one month of the due date (by 30 November 2026) cuts it significantly.</p>

<h2 id="future">Next Year</h2>
<p>File the Tax Year 2027 return by 30 September 2027, or by any extended date, and your name stays on the ATL without any route at all.</p>
""",
    faqs=[
        ("What is the tax on bank profit for a late filer?", "A late filer who has not used the surcharge or Form ATL-U is off the ATL, so the 20% rate under Section 151 is increased by 100% to 40% under rule 1 of the Tenth Schedule."),
        ("How do I get back to 20%?", "Get on the ATL: file the late return and either pay the Rs 25,000 surcharge or, as an individual not obtaining property for six months, furnish Form ATL-U."),
        ("Will the bank refund the extra deduction?", "The bank does not refund it. You claim the excess through your return, and Section 182A(1)(c) blocks refunds while you are off the ATL."),
        ("Is Form ATL-U suitable for pensioners?", "Usually yes. Pensioners rarely buy property within six months, and the undertaking replaces the surcharge."),
        ("How quickly does the rate change?", "The bank applies the rate according to the ATL on the payment date. After your name appears, inform the bank so later payments use 20%."),
        ("Does this apply to National Savings certificates?", "Profit on debt under Section 151 includes profit on National Savings schemes, and the ATL test applies the same way."),
        ("Is the late-filing penalty removed by Form ATL-U?", "No. The Section 182 penalty remains; filing within one month of the due date reduces it by 75%."),
        ("Are dividends also affected?", "Yes. Rule 1 of the Tenth Schedule increases withholding rates generally, including on dividends, for people off the ATL."),
    ],
    sources=[S_ITO, S_SRO, S_ATL, S_IRIS],
    related=[(X["bank"], "Tax on Bank Profit 2026"), (B["alf"], "Active Late Filer Meaning"), (B["sal"], "Form ATL-U for Salaried and Pensioners")],
    cta_h="Back to 20% on Your Bank Profit",
    cta_p="Late return, Form ATL-U and an ATL check, so the double deduction stops.",
    wa_text="Assalam o Alaikum, bank meri profit par double tax kaat raha hai. Late return aur Form ATL-U karwana hai.",
)
