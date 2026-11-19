"""Form ATL-U series, posts 7-10."""
from atlu_common import *
from atlu_a import PEN_NOTE

# ───────────────────────────── 7. What you cannot buy / breach ─────────────────────────────
BUY = dict(
    slug=SL["buy"],
    svc=dict(h2="Check Your Six Months Before You Sign", intro="The undertaking is simple to furnish and easy to break by accident. Before we furnish Form ATL-U for anyone, we go through their family's property plans for the next six months, so the promise is one they can keep.",
             hook="Not sure whether your plans fit the undertaking?", fee=F_ALL, btn="Check my six months",
             items=["A short review of every property plan in the household: bookings, files, instalments, inheritance, gifts",
                    "A clear recommendation: Form ATL-U or the surcharge",
                    "Late return, wealth statement and the chosen ATL route filed",
                    "The six-month end date in writing",
                    "Help if a property issue comes up during the six months"],
             risks=["An instalment plan or booking you forgot about can count as acquiring property",
                    "A breach brings back the surcharge, usually in the middle of a deal",
                    "Holding property in a relative's name for your benefit is still a beneficial interest"]),
    title="Form ATL-U Undertaking: What You Cannot Buy for 6 Months",
    h1="The Form ATL-U Undertaking: What You Cannot Buy or Receive for Six Months, and What Happens If You Do",
    crumb="Form ATL-U: 6-Month Property Rule",
    description="The Form ATL-U promise in detail: plots, files, bookings, gifts, inheritance, benami property, vehicles, the six-month count and the cost of a breach.",
    keywords="form atl u property undertaking, atl-u six months property, atl undertaking breach, can i buy plot after form atl u, beneficial interest property fbr, section 182a(3) property",
    category="Form ATL-U", icon="⏳", read="12 min read",
    banner="Form ATL-U saves Rs 25,000 in exchange for one promise. Before you make it, know exactly what the promise covers.",
    tldr=("Under Section 182A(3) of the Income Tax Ordinance, an individual using Form ATL-U declares that he 'shall not purchase, acquire, or otherwise obtain ownership or "
          "beneficial interest in any property' for six months from the date of the undertaking. The words are wide: buying, acquiring by any other means and obtaining any "
          "ownership or beneficial interest are all covered, and the law does not define 'property' narrowly for this purpose. Plots, houses, flats, shops, allotment files and "
          "bookings are clearly within it; gifts, inheritance, vehicles and shares are not addressed expressly, so the careful approach is to treat them as covered until FBR "
          "clarifies. As notified in SRO 2097(I)/2026, a breach leads to withdrawal of the benefit from the date of breach after a hearing, and the surcharge rule then applies."),
    lead=("The undertaking takes a minute to furnish. Keeping it means thinking about every way property could come to you, or to someone holding it for you, over half a year. "
          "This guide walks through the situations our clients actually ask about."),
    body=f"""
{SERIES}

<h2 id="words">The Words That Bind You</h2>
<p>Section 182A(3) has four working parts:</p>
{table(["Words in the law", "What they cover"], [
    ["\"purchase\"", "Buying for a price, in cash or by instalments"],
    ["\"acquire\"", "Coming to own something by any route, not only by buying"],
    ["\"or otherwise obtain ownership\"", "A catch-all for any other way of becoming the owner"],
    ["\"or beneficial interest\"", "Property in another person's name that is held for your benefit"],
])}
<p>Then the object: "any property". The undertaking does not say "immovable property", even though Sections 236C and 236K, which deal with property transfers, do. Until FBR issues guidance, read "any property" in its ordinary, wide sense.</p>

<h2 id="clear">Clearly Covered</h2>
<ul>
<li><strong>Plots, houses, flats, shops and agricultural land</strong> bought in your name.</li>
<li><strong>Allotment files and bookings</strong> in housing schemes, including the first instalment of a plan.</li>
<li><strong>Transfer of a file into your name</strong> from another person.</li>
<li><strong>A share in jointly bought property</strong>: you are acquiring your share.</li>
<li><strong>Property in a spouse's or relative's name paid for by you and held for you.</strong> That is a beneficial interest.</li>
</ul>

<h2 id="grey">Grey Areas: Treat as Covered Until Clarified</h2>
{table(["Situation", "Why it is uncertain", "Safe course"], [
    ["Gift of a plot from a parent", "A gift is a way to 'obtain ownership', though not a purchase", "Delay the transfer until the six months end"],
    ["Inheritance on a death in the family", "Succession happens by law, not by your act", "Keep the record of the date and cause; seek advice before mutating into your name"],
    ["Buying a car or motorcycle", "'Any property' is not limited to land; vehicles are not mentioned", "If possible, wait; if not, consider the surcharge"],
    ["Buying shares or mutual fund units", "Same question as vehicles", "Wait, or keep the purchase small and seek advice"],
    ["Paying the next instalment of a plan booked before the undertaking", "You already hold the interest; the instalment may not be a new acquisition", "Discuss before signing; possession or transfer during the six months is riskier"],
])}
<p>These are honest uncertainties. The law does not answer them and the notified rules, as reported, do not either. We would rather you pay Rs 25,000 than lose it later in a dispute.</p>

<h2 id="allowed">Not Restricted</h2>
<ul>
<li><strong>Selling property you already own.</strong> See our guide on {a(B["sale"], "selling as a late filer")}.</li>
<li><strong>Renting property</strong> as a tenant. A tenancy is not ownership.</li>
<li><strong>Repairing or building on land you already own.</strong> You are not obtaining new ownership of land; take advice if the construction creates a separate unit for sale or transfer.</li>
<li><strong>Your adult family members' own purchases from their own funds,</strong> in their own names and for their own benefit.</li>
</ul>

<h2 id="count">Counting the Six Months</h2>
<p>The law says six months "commencing from the date of furnishing such undertaking". The date on the IRIS acknowledgement for Form ATL-U is your start date. Six months from 25 November 2026 run to 24 May 2027; do not book anything until the following day. The return's filing date and the date your name appears on the ATL are not the start date.</p>

<h2 id="breach">What a Breach Costs</h2>
<p>As notified, FBR can check against information from registries, financial institutions and other lawful sources. If a breach is found, you are given an electronic opportunity to explain. If it is established, the benefit is withdrawn from the date of breach and your ATL position follows the ordinary rule in Section 182A(1): you need to pay the surcharge to be included.</p>
<p>The real cost is the timing. A breach usually happens during a property purchase. If you are off the ATL at that moment, the buyer's advance tax under Section 236K is 10.5% to 18.5% by value instead of 1.25%. On a Rs 1 crore plot, that is Rs 1,050,000 instead of Rs 125,000.</p>

<h2 id="change-mind">If Your Plans Change</h2>
<p>Life changes. If a property opportunity appears in month three, do not proceed and hope. Talk to us first. Depending on the facts, the answer may be to wait out the six months, to pay the surcharge before the transaction so you are on the ATL on your own terms, or to structure the deal so that it completes after the end date.</p>

<h2 id="decide">A Quick Self-Check</h2>
<ol>
<li>Is any property, file or booking going to come into my name in six months?</li>
<li>Is anyone holding property for me, or buying with my money?</li>
<li>Am I expecting a gift or inheritance of property soon?</li>
<li>Do I need to buy a car in the next six months?</li>
</ol>
<p>Four honest "no" answers: Form ATL-U is likely right for you. Any "yes" or "maybe": talk it through, or read our {a(X["cmp"], "surcharge vs Form ATL-U comparison")}.</p>
""",
    faqs=[
        ("What does Form ATL-U stop me from buying?", "Section 182A(3) covers purchasing, acquiring or otherwise obtaining ownership or beneficial interest in any property for six months. Plots, houses, flats, shops, files and bookings are clearly covered."),
        ("Can I buy a car after signing Form ATL-U?", "The law says 'any property' and does not mention vehicles. Until FBR clarifies, the careful course is to wait or to pay the surcharge instead."),
        ("Does inheritance breach the undertaking?", "The law does not address it. Succession is not your act, but transferring the property into your name is a way of obtaining ownership. Seek advice before mutation within the six months."),
        ("Can my wife buy a plot while I use Form ATL-U?", "If she buys with her own money for herself, it is her purchase. If you fund it or she holds it for you, that is a beneficial interest and a breach."),
        ("When do the six months end?", "Six months from the date you furnished the undertaking, shown on the IRIS acknowledgement."),
        ("What happens if I breach the undertaking?", "As notified, after an electronic hearing the benefit is withdrawn from the date of breach, and the surcharge rule in Section 182A(1) applies."),
        ("Can I sell property during the six months?", "Yes. Selling is not one of the restricted acts."),
        ("Can I pay the surcharge later instead?", "Yes. If your plans change, paying the surcharge puts you on the ATL without depending on the undertaking. Do it before the purchase."),
    ],
    sources=[S_ITO, S_SRO, S_ATL],
    related=[(B["guide"], "Form ATL-U Complete Guide"), (X["cmp"], "Surcharge vs Form ATL-U"), (B["sale"], "Selling Property as a Late Filer")],
    cta_h="Make a Promise You Can Keep",
    cta_p="We check your six months, then file the route that fits.",
    wa_text="Assalam o Alaikum, Form ATL-U sign karne se pehle property ke baare mein mashwara chahiye.",
)

# ───────────────────────────── 8. Salaried & pensioners ─────────────────────────────
SAL = dict(
    slug=SL["sal"],
    svc=dict(h2="Your Salaried Return and Form ATL-U for Rs 5,500", intro="Send us your salary certificate and bank statements on WhatsApp. We prepare the return and wealth statement, show you the figures, file them, furnish Form ATL-U and confirm your ATL status.",
             hook="Salaried or pensioner and missed the deadline?", fee=F_SAL, btn="File my salaried return with ATL-U",
             items=["Return from your employer's certificate (Section 149) and bank tax certificates",
                    "Wealth statement with every account, plot and vehicle declared",
                    "Section 182 penalty worked out and shown before filing",
                    "Form ATL-U furnished and the acknowledgement sent",
                    "ATL status checked after FBR's next update"],
             risks=["Filing without the wealth statement leaves the return incomplete",
                    "Missing 30 November 2026 loses the 75% penalty reduction",
                    "Paying Rs 25,000 for the surcharge when Rs 2,000 for the undertaking would do"]),
    title="Form ATL-U for Salaried and Pensioners: Late Return Guide",
    h1="Late Return for Salaried Employees and Pensioners in 2026: Using Form ATL-U Instead of the Rs 25,000 Surcharge",
    crumb="Form ATL-U for Salaried",
    description="Salaried or pensioner and filed late? The penalty, the Rs 25,000 ATL surcharge, and how Form ATL-U puts you back on the ATL for Rs 5,500 all-in with us.",
    keywords="salaried late return 2026, salary return late filing penalty, how to become filer in pakistan for salaried person, pensioner late filer, form atl u salaried, salaried atl surcharge",
    category="Form ATL-U", icon="💼", read="11 min read",
    banner="Your tax was deducted from every salary slip, yet a late return still takes you off the ATL. Here is the quickest, cheapest way back.",
    tldr=("A salaried employee's tax is deducted by the employer under Section 149, but the return under Section 114 is still required, and a return filed after the due date "
          "keeps the person off the Active Taxpayers List under Section 182A(1). For Tax Year 2026 the extended due date was 31 October 2026. Off the ATL, bank profit, dividends, "
          "vehicle registration and property transactions attract higher withholding. To join the ATL after a late return, an individual pays a Rs 25,000 surcharge or furnishes "
          "Form ATL-U, promising not to obtain property for six months. The Section 182 penalty still applies, with a minimum of Rs 10,000 where at least 75% of income is salary, "
          "reduced by 75% if the return is filed by 30 November 2026."),
    lead=("Salaried people are the largest group of late filers, and usually for innocent reasons: the certificate arrived late, the deadline was extended twice and still slipped "
          "past, or they assumed the employer's deduction was enough. The law gives no exemption for good intentions, but it does give a cheaper route back."),
    body=f"""
{SERIES}

<h2 id="why-file">Why You Must File Even Though Tax Was Deducted</h2>
<p>Section 149 makes your employer deduct tax from salary every month. That deduction settles most or all of your tax, but it does not file your return. Section 114 still requires a return from every individual whose taxable income is above the exemption, and from others the Ordinance names. Only a filed return puts you on the ATL, and only the ATL gives you the filer rates at the bank and the registrar.</p>

<h2 id="consequences">What Happens When a Salaried Return Is Late</h2>
{table(["Consequence", "Section", "Effect on a salaried person"], [
    ["Not on the ATL for that year", "182A(1)(a)", "Higher deductions on bank profit, dividends, vehicle tax, property"],
    ["No refund while off the ATL", "182A(1)(c)", "Excess tax deducted by the employer cannot be refunded yet"],
    ["Late-filing penalty", "182", "Minimum Rs 10,000 where 75% or more of income is salary"],
])}
<p>The minimum penalty for salaried individuals is lower than the Rs 50,000 that applies to others, but it is still real money. {PEN_NOTE}</p>

<h2 id="routes">Your Two Routes Onto the ATL</h2>
{table(["", "Surcharge", "Form ATL-U"], [
    ["Paid to FBR", "Rs 25,000", "Nothing"],
    ["Our fee with the return", "Rs 3,500", "Rs 3,500 + Rs 2,000 = Rs 5,500"],
    ["Condition", "None", "No property obtained for six months"],
    ["Best for", "Anyone buying a plot, flat or house in six months", "Everyone else"],
])}

<h2 id="pensioners">Pensioners</h2>
<p>A pension is generally part of salary income, and many pensioners also earn profit on savings. For them, the ATL matters mostly at the bank: the 20% deduction on profit under Section 151 doubles to 40% when they are off the list. Our guide on {a(B["bank"], "late filer tax on bank profit")} shows the numbers. Few pensioners are buying property, so Form ATL-U usually fits.</p>
<p>Pensioners should check their wealth statement carefully. Commutation received on retirement, savings certificates and gifts to children all need to appear correctly, and the wealth statement must reconcile with the previous year's.</p>

<h2 id="docs">Documents for a Salaried Late Return</h2>
<ul>
<li>Salary certificate or annual tax deduction certificate from the employer for July 2025 to June 2026.</li>
<li>Bank tax deduction certificates for profit, and statements showing year-end balances.</li>
<li>Details of any property, vehicle, savings certificates, gold and cash held at 30 June 2026.</li>
<li>Utility and mobile phone tax certificates if you want those deductions credited.</li>
<li>Last year's wealth statement, if one was filed.</li>
</ul>

<h2 id="steps">The Steps, in Order</h2>
<ol>
<li>Prepare the Tax Year 2026 return from the certificates.</li>
<li>Prepare the wealth statement and reconcile it with last year's.</li>
<li>File both on IRIS and pay any balance tax.</li>
<li>Furnish Form ATL-U on IRIS and save the acknowledgement. Our {a(B["iris"], "IRIS step-by-step guide")} shows the screens.</li>
<li>Check the ATL after the next update and tell your bank once your name appears.</li>
</ol>

<h2 id="refund">If Your Employer Deducted Too Much</h2>
<p>A refund is possible where deductions exceed your tax, for example because a tax credit was not given through payroll. Section 182A(1)(c) holds refunds while you are off the ATL, so joining the ATL first is the practical step before any refund claim.</p>

<h2 id="employer">Does My Employer Need to Know?</h2>
<p>No. Form ATL-U is between you and FBR. Some employers ask staff for an ATL screenshot each year; once your name appears, a screenshot of the status check is enough.</p>

<h2 id="mistakes">Common Salaried Mistakes</h2>
<ul>
<li>Filing the return but skipping the wealth statement.</li>
<li>Declaring a different salary from the certificate.</li>
<li>Forgetting the bank account where salary is not paid.</li>
<li>Assuming the employer's tax deduction makes the return optional.</li>
</ul>
<p>Our {a(X["salr"], "salaried return guide")} covers the return itself in more depth.</p>
""",
    faqs=[
        ("Is the return required if my employer deducted tax?", "Yes. Section 149 deduction does not replace the Section 114 return, and only a filed return puts you on the ATL."),
        ("What is the late-filing penalty for a salaried person?", "The higher of 0.1% of tax payable or Rs 1,000 per day, with a minimum of Rs 10,000 where at least 75% of income is salary, reduced if filed within three months of the due date."),
        ("How much does a late salaried return with Form ATL-U cost with you?", "Rs 3,500 for the return plus Rs 2,000 for Form ATL-U, Rs 5,500 in total. FBR's penalty, if any, is paid separately."),
        ("Can pensioners use Form ATL-U?", "Yes. A pensioner is an individual, and the undertaking suits anyone not obtaining property for six months."),
        ("Will my employer be told about Form ATL-U?", "No. It is furnished on IRIS between you and FBR."),
        ("Can I claim a refund of excess salary tax after a late return?", "Yes, through the return, but Section 182A(1)(c) blocks refunds while you are off the ATL."),
        ("Do I need a wealth statement as a salaried person?", "In most cases yes. Section 116 requires it with the return for individuals in the cases it specifies, and it is checked against your records."),
        ("When is next year's salaried return due?", "30 September 2027 for Tax Year 2027, under Section 118, unless extended."),
    ],
    sources=[S_ITO, S_SRO, S_ATL, S_IRIS],
    related=[(X["salr"], "Salaried Tax Return Guide"), (B["bank"], "Late Filer Tax on Bank Profit"), (B["iris"], "Submit Form ATL-U on IRIS")],
    cta_h="Salaried Late Return + Form ATL-U: Rs 5,500",
    cta_p="Send your salary certificate on WhatsApp; we file and confirm your ATL status.",
    wa_text="Assalam o Alaikum, main salaried / pensioner hoon. Late return aur Form ATL-U (Rs 5,500) karwana hai.",
)

# ───────────────────────────── 9. Freelancers, traders, overseas ─────────────────────────────
FREE = dict(
    slug=SL["free"],
    svc=dict(h2="Late Return and Form ATL-U for Freelancers, Traders and Overseas Filers", intro="Business and foreign-income returns need more care than salary returns: income, expenses, remittances and the wealth statement must agree. We prepare them properly, then furnish Form ATL-U so you avoid the surcharge.",
             hook="Freelancer, shopkeeper or overseas and filed late?", fee=f"{F_FREE} Sole proprietor: Rs 7,000. Overseas: Rs 8,000.", btn="File my return with Form ATL-U",
             items=["Income worked out from remittance records, sales records or foreign income details",
                    "Wealth statement reconciled with last year's and with your bank balances",
                    "Return filed on IRIS, with the penalty shown before filing",
                    "Form ATL-U furnished and the acknowledgement sent",
                    "ATL status checked and a reminder for the Tax Year 2027 deadline"],
             risks=["Remittances or sales that do not match the return attract questions",
                    "An AOP or company cannot use Form ATL-U; mislabelling the business causes trouble",
                    "Non-residents selling property here pay 11.5% if off the ATL"]),
    title="Form ATL-U for Freelancers, Traders and Overseas Filers",
    h1="Form ATL-U for Freelancers, Shopkeepers, Sole Proprietors and Overseas Pakistanis: Late Return Without the Rs 25,000 Surcharge",
    crumb="Form ATL-U: Freelancers & Traders",
    description="Freelancer, sole proprietor or overseas Pakistani who filed late? Who can use Form ATL-U, who cannot (AOPs, companies), and what each group should check.",
    keywords="how to become filer in pakistan for overseas, freelancer late return atl, sole proprietor atl surcharge, shopkeeper late filer, form atl u freelancer, overseas pakistani atl surcharge",
    category="Form ATL-U", icon="🌍", read="12 min read",
    banner="Business owners, freelancers and overseas Pakistanis each face the late-return problem differently. Here is how Form ATL-U applies to each.",
    tldr=("Form ATL-U, under Section 182A(3), is available to any individual who files the return after the due date and undertakes not to obtain ownership or beneficial "
          "interest in any property for six months. That includes freelancers, sole proprietors (who are individuals carrying on business in their own name) and overseas "
          "Pakistanis who file in Pakistan. It is not available to an association of persons or a company, which must pay Rs 50,000 or Rs 100,000 to join the ATL after a "
          "late return. For individuals who are not salaried, the Section 182 minimum penalty is Rs 50,000, reduced by 75% if the Tax Year 2026 return is filed by 30 November 2026."),
    lead=("For a freelancer the ATL affects bank profit and remittance accounts; for a shopkeeper it affects what suppliers and banks deduct; for an overseas Pakistani it affects "
          "property sales and bank profit at home. The fix is the same law, but the return behind it differs a lot. Here is what each group needs to know."),
    body=f"""
{SERIES}

<h2 id="who">Individual or Not? The First Question</h2>
{table(["How you work", "Taxed as", "Form ATL-U?", "Surcharge if late"], [
    ["Freelancer on Upwork, Fiverr or direct clients", "Individual", "Yes", "Rs 25,000"],
    ["Shop or service business in your own name (sole proprietor)", "Individual", "Yes", "Rs 25,000"],
    ["Overseas Pakistani filing in Pakistan", "Individual", "Yes", "Rs 25,000"],
    ["Partnership or family firm registered as an AOP", "Association of persons", "No", "Rs 50,000"],
    ["Private limited or SMC company", "Company", "No", "Rs 100,000"],
])}
<p>Section 182A(3) begins "shall not apply to an individual". A partnership's partners are individuals, but the firm's return is the AOP's, and its ATL status is the AOP's. The undertaking cannot be given for the firm.</p>

<h2 id="freelancers">Freelancers</h2>
<p>Most freelancers do not buy property within months of filing, which makes Form ATL-U a natural fit. What needs care is the return:</p>
<ul>
<li>Foreign remittances received through banks, Payoneer-linked accounts or exchange companies should match the income declared.</li>
<li>Withholding on export proceeds, where your bank deducted it, is credited in the return.</li>
<li>If you are registered with PSEB, the treatment of your IT export income depends on the rules that apply for the year; we check this rather than assume.</li>
<li>The wealth statement must explain how bank balances grew.</li>
</ul>
<p>Our {a(X["free"], "freelancer tax return guide")} covers the return itself.</p>

<h2 id="traders">Shopkeepers and Sole Proprietors</h2>
<p>A sole proprietor is an individual doing business in their own name, so the undertaking is available. Three cautions:</p>
<ul>
<li><strong>Buying a shop or godown for the business</strong> within six months is acquiring property. If expansion is planned, pay the surcharge.</li>
<li><strong>Business assets</strong> like stock and equipment are part of running the business. The law's wide words ("any property") leave some doubt about major fixed-asset purchases; discuss them before signing.</li>
<li><strong>Section 182 minimum penalty</strong> for non-salaried individuals is Rs 50,000, before the time-based reduction. {PEN_NOTE}</li>
</ul>

<h2 id="overseas">Overseas Pakistanis</h2>
<p>Whether you must file depends on your residence status and Pakistan-source income. Many non-residents file because they own property here, earn rent or profit here, or plan to sell. If you filed the Tax Year 2026 return late, you face the same Section 182A consequences as a resident.</p>
<p>The biggest stake is usually a property sale. Section 236C collects 2.75% from a seller on the ATL and 11.5% from one off it. On a Rs 2 crore house, that is Rs 550,000 against Rs 2,300,000. An overseas seller who is not buying in Pakistan in the next six months can furnish Form ATL-U and sell at the filer rate. Our guide on {a(B["sale"], "selling property as a late filer")} explains the timing.</p>
<p>Form ATL-U is furnished on IRIS, so it can be done from abroad. Our {a(X["ovs"], "overseas Pakistani tax return guide")} covers residence and filing.</p>

<h2 id="side-by-side">Costs for Each Group With Us</h2>
{table(["Group", "Return fee", "Form ATL-U", "Total", "Instead of surcharge"], [
    ["Freelancer", "Rs 5,000", "Rs 2,000", "Rs 7,000", "Rs 30,000"],
    ["Sole proprietor", "Rs 5,000", "Rs 2,000", "Rs 7,000", "Rs 30,000"],
    ["Overseas Pakistani", "Rs 6,000", "Rs 2,000", "Rs 8,000", "Rs 31,000"],
])}
<p>FBR's Section 182 penalty, if any, is paid to FBR in either case.</p>

<h2 id="aop">If You Are an AOP or Company</h2>
<p>There is no undertaking route. The firm or company pays the surcharge to be included in the ATL after a late return, and the Section 182 penalty applies. If the business is really run by one person and registered as an AOP by mistake, that is a registration question to sort out for future years; it cannot be fixed by signing Form ATL-U now.</p>

<h2 id="steps">Steps for All Three Groups</h2>
<ol>
<li>Gather income records: remittances, sales, rent, profit.</li>
<li>Prepare the Tax Year 2026 return and wealth statement.</li>
<li>File on IRIS; pay tax and any penalty.</li>
<li>Furnish Form ATL-U; save the acknowledgement. See {a(B["iris"], "the IRIS steps")}.</li>
<li>Check the ATL after the next update.</li>
</ol>
""",
    faqs=[
        ("Can a freelancer use Form ATL-U?", "Yes. A freelancer is an individual, and the undertaking is open to individuals who filed late and will not obtain property for six months."),
        ("Can a sole proprietor use Form ATL-U?", "Yes. A sole proprietor is an individual. Buying a shop or other property for the business within six months would breach the undertaking."),
        ("Can a partnership firm use Form ATL-U?", "No. An AOP must pay Rs 50,000 to be included in the ATL after a late return."),
        ("Can overseas Pakistanis use Form ATL-U?", "Yes, if they file in Pakistan as individuals. It is furnished on IRIS, so it can be done from abroad."),
        ("What is the late-filing penalty for a freelancer?", "The higher of 0.1% of tax payable or Rs 1,000 per day, minimum Rs 50,000 for non-salaried individuals, reduced by 75% if filed within one month of the due date."),
        ("Does Form ATL-U help an overseas seller of property?", "Yes. If you are not buying in the next six months, it puts you on the ATL so that 2.75% applies under Section 236C instead of 11.5%."),
        ("Can I buy business equipment during the six months?", "The law says 'any property'. Routine stock is part of the business; for major fixed assets, take advice before signing."),
        ("How much do you charge?", "Freelancer or sole proprietor Rs 7,000 and overseas Rs 8,000, each including Rs 2,000 for Form ATL-U."),
    ],
    sources=[S_ITO, S_SRO, S_ATL, S_IRIS],
    related=[(X["free"], "Freelancer Tax Return 2026"), (X["ovs"], "Overseas Pakistani Tax Return"), (B["sale"], "Selling Property as a Late Filer")],
    cta_h="Business or Foreign Income? File It Right, Skip the Surcharge",
    cta_p="Freelancers and traders Rs 7,000, overseas Rs 8,000, Form ATL-U included.",
    wa_text="Assalam o Alaikum, main freelancer / dukandar / overseas hoon. Late return aur Form ATL-U karwana hai.",
)

# ───────────────────────────── 10. Roman Urdu ─────────────────────────────
RU = dict(
    slug=SL["ru"],
    svc=dict(h2="Hum Aap Ki Late Return Aur Form ATL-U File Karte Hain", intro="WhatsApp par apna CNIC aur aamdani ki tafseel bhejein. Hum return aur wealth statement tayyar karte hain, aap figures dekh kar approve karte hain, phir hum file karke Form ATL-U jama karte hain aur ATL status check karte hain.",
             hook="Deadline guzar gayi aur property nahi khareedni?", fee="Salaried Rs 3,500 + Form ATL-U Rs 2,000 = Rs 5,500. Freelancer ya dukandar Rs 7,000. Overseas Rs 8,000. FBR ki penalty, agar bane, alag se FBR ko jama hoti hai.", btn="Mujhe filer banna hai",
             items=["Pehle check: aap individual hain aur 6 maah property nahi khareedni",
                    "Tax Year 2026 ki return aur wealth statement IRIS par file",
                    "Penalty ka hisaab file karne se pehle aap ko bataya jata hai",
                    "Form ATL-U jama, acknowledgement aap ko bheja jata hai",
                    "Agli ATL update ke baad status check"],
             risks=["Rs 25,000 surcharge dena jab Rs 2,000 mein kaam ho sakta tha",
                    "30 November 2026 ke baad file karne se 75% penalty kami khatam",
                    "6 maah ke andar plot book karne se riayat wapas aur surcharge lagu"]),
    title="Filer Kaise Banein 2026: Form ATL-U, Bina Rs 25,000",
    h1="Filer Kaise Banein 2026: Late Return Ke Baad Form ATL-U Se Bina Rs 25,000 Surcharge ATL Mein Naam",
    crumb="Filer Kaise Banein 2026",
    description="Filer kaise banein 2026 mein? Late return ke baad Rs 25,000 surcharge ya Form ATL-U: kaun use kar sakta hai, 6 maah ki shart, penalty aur fees.",
    keywords="filer kaise bane 2026, filer kaise bane pakistan, tax filer kaise bane, online filer kaise bane, form atl u urdu, atl surcharge 25000 urdu, late filer kya kare",
    category="Form ATL-U", icon="🧾", read="12 min read",
    banner="Return ki aakhri tareekh 31 October 2026 guzar gayi? Agar agle 6 maah property nahi khareedni to Rs 25,000 diye baghair filer ban sakte hain.",
    tldr=("Filer banne ke liye FBR koi fees nahi leta. Filer ka matlab hai Active Taxpayers List (ATL) mein naam, aur yeh naam return file karne se aata hai. Lekin Section 182A "
          "ke mutabiq jo shakhs return deadline ke baad file kare, woh us saal ATL mein nahi aata jab tak surcharge na de: individual Rs 25,000, AOP Rs 50,000, company Rs 100,000. "
          "Finance Act 2026 ne Section 182A(3) shamil kiya: individual agar undertaking de ke 6 maah tak koi property nahi khareedega ya hasil nahi karega, to surcharge ki shart "
          "lagu nahi hoti. FBR ne 10 November 2026 ko SRO 2097(I)/2026 ke zariye is ka form, Form ATL-U, jari kiya. Late-filing penalty phir bhi alag se lagti hai."),
    lead=("Har saal deadline ke baad hazaron log yahi poochte hain: ab filer kaise banein? Is saal jawab badal gaya hai, kyun ke surcharge Rs 1,000 se Rs 25,000 ho gaya aur saath "
          "hi aik naya, sasta raasta bhi aa gaya. Yeh guide qanoon ki buniyad par, aasan zubaan mein, poora tareeqa batati hai."),
    body=f"""
{SERIES}

<h2 id="filer-matlab">Filer Ka Asal Matlab</h2>
<p>"Filer" koi certificate nahi. Bank, property registrar aur gaari ki registration wale yeh dekhte hain ke aap ka naam FBR ki Active Taxpayers List mein hai ya nahi. Naam hai to kam tax katta hai, nahi hai to Tenth Schedule ke rule 1 ke mutabiq zyada tar withholding rates 100% barh jate hain.</p>
{table(["Kaam", "ATL mein naam", "ATL mein naam nahi"], [
    ["Bank profit par tax (s.151)", "20%", "100% izafa, yani 40%"],
    ["Property bechne par advance tax (s.236C)", "2.75%", "11.5%"],
    ["Property khareedne par advance tax (s.236K)", "1.25%", "10.5% se 18.5%"],
    ["Gaari ki registration par tax (s.231B)", "Aam rate", "200% izafa"],
])}

<h2 id="late-masla">Late Return Ka Masla</h2>
<p>Tax Year 2026 ki return ki aakhri tareekh barha kar 31 October 2026 ki gayi thi. Is ke baad file karne wala "late filer" hai. Section 182A(1) kehta hai ke aisa shakhs us saal ke ATL mein shamil nahi hoga. Saath mein:</p>
<ul>
<li>Jab tak ATL se bahar hai, refund nahi milta (182A(1)(c)).</li>
<li>Us saal ka nuqsan agle saalon mein carry forward nahi hota (182A(1)(b)).</li>
<li>Late filing ki penalty Section 182 ke tehat alag se lagti hai.</li>
</ul>

<h2 id="do-raaste">ATL Mein Aane Ke Do Raaste</h2>
{table(["", "Raasta 1: Surcharge", "Raasta 2: Form ATL-U"], [
    ["Qanoon", "Section 182A(1)(a) ka proviso", "Section 182A(3) + SRO 2097(I)/2026"],
    ["Kaun use kar sakta hai", "Individual, AOP, company", "Sirf individual"],
    ["FBR ko kitna", "Rs 25,000 (individual)", "Kuch nahi"],
    ["Shart", "Koi nahi", "6 maah tak koi property nahi khareedni ya hasil nahi karni"],
])}

<h2 id="qanoon">Qanoon Kya Kehta Hai</h2>
<p>Section 182A(3) ka khulasa: surcharge ki shart us individual par lagu nahi hogi jo Commissioner ke saamne undertaking de ke woh undertaking ki tareekh se 6 maah tak kisi property ko "purchase, acquire, or otherwise obtain ownership or beneficial interest" nahi karega. Yani na khareedna, na kisi aur tareeqe se maalik banna, aur na kisi doosre ke naam par apne faide ke liye property rakhna.</p>
<p>Yeh shart 1 July 2026 se qanoon mein thi lekin form na hone ki wajah se kaam nahi kar rahi thi. 10 November 2026 ko FBR ne Income Tax Rules 2002 ke rule 81B mein tarmeem karke Form ATL-U jari kiya.</p>

<h2 id="kis-ke-liye">Form ATL-U Kis Ke Liye Theek Hai</h2>
<ul>
<li>Naukri pesha log aur pensioners jinhon ne deadline miss ki. Tafseel hamari {a(B["sal"], "salaried guide")} mein hai.</li>
<li>Freelancers, dukandar aur sole proprietors; dekhein {a(B["free"], "yeh guide")}.</li>
<li>Bahar rehne wale Pakistani jo yahan property bechna chahte hain.</li>
<li>Woh log jin ke bank profit par double tax kat raha hai; dekhein {a(B["bank"], "bank profit guide")}.</li>
</ul>

<h2 id="kis-ke-liye-nahi">Kis Ke Liye Nahi</h2>
<ul>
<li>Jis ne agle 6 maah mein plot, ghar, flat, dukaan ya file leni hai.</li>
<li>AOP ya company: qanoon sirf individual ki baat karta hai.</li>
<li>Jise yaqeen nahi. Gaari, gift ya wirasat ke sawalon par hamari {a(B["buy"], "6 maah wali guide")} parhein.</li>
</ul>

<h2 id="tareeqa">Tareeqa: Qadam Ba Qadam</h2>
<ol>
<li><strong>IRIS par login</strong> karein. Password bhool gaye hain to reset karein.</li>
<li><strong>Tax Year 2026 ki return aur wealth statement</strong> file karein. Draft nahi, Completed status zaroori hai.</li>
<li><strong>Tax aur penalty</strong> (agar bane) PSID challan se jama karein.</li>
<li><strong>Form ATL-U</strong> IRIS par bharein: naam, CNIC, tax year 2026, return ki tareekh aur acknowledgement number, phir declaration. Screens ki tafseel hamari {a(B["iris"], "IRIS guide")} mein hai.</li>
<li><strong>Acknowledgement</strong> download karke sambhal lein. Is ki tareekh se 6 maah gine jayenge.</li>
<li><strong>ATL status</strong> agli update ke baad check karein: {a(X["chk"], "online ya SMS se")}.</li>
</ol>

<h2 id="penalty">Penalty Kitni Hai</h2>
<p>30 June 2026 tak amended Ordinance ke mutabiq Section 182 ki penalty yeh hai: har din ke liye tax payable ka 0.1% ya Rs 1,000, jo zyada ho. Kam az kam Rs 10,000 agar aamdani ka 75% ya zyada salary se ho, warna Rs 50,000. Zyada se zyada tax payable ka 200%. Aur agar return deadline ke 1, 2 ya 3 maah ke andar file ho to penalty 75%, 50% ya 25% kam ho jati hai.</p>
<p>Is ka matlab: <strong>30 November 2026 tak</strong> return file karne par penalty mein 75% kami milti hai. Der na karein.</p>

<h2 id="kharcha">Kul Kharcha: Misaal</h2>
{table(["Aap kaun hain", "Surcharge wala raasta", "Form ATL-U wala raasta"], [
    ["Salaried / pensioner", "Rs 3,500 + Rs 25,000 = Rs 28,500", "Rs 3,500 + Rs 2,000 = Rs 5,500"],
    ["Freelancer / dukandar", "Rs 5,000 + Rs 25,000 = Rs 30,000", "Rs 5,000 + Rs 2,000 = Rs 7,000"],
    ["Overseas Pakistani", "Rs 6,000 + Rs 25,000 = Rs 31,000", "Rs 6,000 + Rs 2,000 = Rs 8,000"],
])}
<p>Yeh hamari published fees hain; FBR ki penalty in ke ilawa hai. Poori tafseel {a(B["fee"], "filer fee 2026 guide")} mein.</p>

<h2 id="ghaltiyan">Aam Ghaltiyan</h2>
<ul>
<li>Sirf return file karke samajhna ke ATL mein naam aa jayega.</li>
<li>6 maah return ki tareekh se ginna, jab ke yeh undertaking ki tareekh se shuru hote hain.</li>
<li>Yeh samajhna ke Form ATL-U se penalty bhi maaf ho gayi.</li>
<li>6 maah ke andar biwi ya bhai ke naam par apne paison se plot lena. Yeh "beneficial interest" hai.</li>
</ul>
""",
    faqs=[
        ("Filer banne ki fees kitni hai?", "FBR filer banne ki koi fees nahi leta. Late return par penalty aur ATL ke liye Rs 25,000 surcharge ya Form ATL-U ka raasta hai."),
        ("Form ATL-U kya hai?", "Section 182A(3) ke tehat undertaking ka form, jo SRO 2097(I)/2026 se jari hua. Individual 6 maah property na lene ka wada karta hai aur surcharge ke baghair ATL mein aata hai."),
        ("Kya company ya AOP Form ATL-U de sakti hai?", "Nahi. Yeh sirf individual ke liye hai. AOP Rs 50,000 aur company Rs 100,000 surcharge deti hai."),
        ("6 maah kab se shuru hote hain?", "Undertaking jama karne ki tareekh se, jo IRIS acknowledgement par likhi hoti hai."),
        ("Kya Form ATL-U ke baad property bech sakte hain?", "Haan. Pabandi khareedne ya hasil karne par hai, bechne par nahi."),
        ("Agar 6 maah mein plot le liya to kya hoga?", "Notify kiye gaye rules ke mutabiq sunwai ke baad breach ki tareekh se riayat wapas ho jati hai aur surcharge wala qanoon lagu hota hai."),
        ("Penalty kab kam hoti hai?", "Deadline ke 1 maah ke andar file karne par 75%, 2 maah mein 50%, 3 maah mein 25% kami. Tax Year 2026 ke liye 30 November 2026 tak 75%."),
        ("Aap kitni fees lete hain?", "Salaried return Rs 3,500 + Form ATL-U Rs 2,000 = Rs 5,500. Freelancer ya dukandar Rs 7,000, overseas Rs 8,000."),
    ],
    sources=[S_ITO, S_SRO, S_ATL, S_IRIS],
    related=[(B["guide"], "Form ATL-U Complete Guide (English)"), (B["fee"], "Filer Fee 2026"), (X["chk"], "ATL Status Check")],
    cta_h="Bina Rs 25,000 Filer Banein",
    cta_p="Late return aur Form ATL-U hum file karte hain, ATL status bhi check karte hain.",
    wa_text="Assalam o Alaikum, mujhe filer banna hai. Return late hai, Form ATL-U ke zariye ATL mein aana hai.",
)
