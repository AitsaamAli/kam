"""Wealth statement revision series, visa posts 1-5 (facts checked 24 November 2026; see wr_common.py)."""
from wr_common import *

# 1 ---------------------------------------------------------------- before a visa application (series hub)
VISA = post(
    slug=SL["visa"],
    title="Revise Your Wealth Statement Before a Visa Application",
    h1="Revising Your Wealth Statement Before a Visa Application: What to Fix, What Never to Touch (2026)",
    crumb="Wealth Statement Revision for Visa",
    description="Applying for a UK, Schengen or Canada visa? Which wealth statement errors to correct under section 116(3) first, the deadline, and why inflating cash backfires.",
    keywords="wealth statement revision for visa, revise wealth statement before visa, wealth statement for visa pakistan, fbr documents visa, wealth statement correction visa application",
    read="12 min read",
    banner="A wealth statement that does not match your bank statements raises more questions than one that shows less money. Fix it the lawful way, before you apply.",
    tldr=("Under section 116(3) of the Income Tax Ordinance you can revise a filed wealth statement when you discover an omission or wrong statement, "
          "with a revised wealth reconciliation and written reasons, at any time before you receive a notice under section 122(9) for that year and "
          "never later than five years from that year's return due date. Before a visa application, revise only to make the statement true: a missing "
          "bank account, a car or plot recorded at the wrong cost, a gift booked as income. Never revise to show more money than you have. FBR can "
          "declare a revision void if it is not a bona fide correction, and unexplained assets are taxed under section 111."),
    lead=("Visa officers do not read Pakistani tax law, but they read numbers. The UK guide asks for bank statements that “detail the origin of the "
          "funds held”; Canada asks for six months of account details; the Schengen rules ask for proof of sufficient means of subsistence. When the "
          "wealth statement you attach tells a different story from those bank papers, the officer has a reason to doubt both. This guide explains what "
          "the law lets you correct before you apply, how to do it so it stands up later with FBR, and the revisions people make that do lasting damage."),
    answers={
        "why": "Because the wealth statement is the one official record that explains where your money came from, and officers compare it with your bank papers.",
        "law": "Section 116(3): revised statement plus revised reconciliation plus written reasons, before a 122(9) notice and within five years of the return due date.",
        "fix": "Fix genuine errors: a missing account, wrong cost of an asset, a gift recorded as income, a dependent's asset left out.",
        "never": "Never add cash or assets you do not hold. The revision can be declared void and the extra amount taxed as unexplained income.",
        "timing": "Revise first, apply after, and keep the revised IRIS acknowledgement and your reasons letter together with the visa file.",
    },
    svc=svc("We Correct the Statement Before the Embassy Sees It",
            "We compare your filed wealth statement with the bank, property and salary papers you plan to give the embassy, list every mismatch, and revise only what is genuinely wrong.",
            ["Line-by-line check of the filed statement against bank certificates and property papers",
             "Revised wealth statement and revised wealth reconciliation on IRIS",
             "A written reasons note for each change, as section 116(3) requires",
             "Advice on whether the return also needs revising, and the conditions that apply",
             "A one-page summary in plain English you can keep with your visa documents"],
            ["Adding money you cannot trace invites a section 111 assessment later",
             "A revision without reasons or a matching reconciliation can be declared void",
             "Revising after a 122(9) notice is no longer allowed, so the error stays on record"],
            "Visa file ready but the wealth statement does not match?"),
    wa_text="Assalam o Alaikum, visa apply karna hai. Wealth statement revise karwana hai, IRIS copy bhej raha hoon.",
    body=f"""
{SERIES("visa")}

<h2 id="why">Why the Wealth Statement Matters to a Visa Officer</h2>
<p>None of the official visa pages we checked lists an FBR wealth statement as a mandatory document. What they ask for is proof that you can pay for the trip and that the money is genuinely yours:</p>
{table(["Country", "What the official guidance asks for", "Where the wealth statement fits"], [
    ["United Kingdom", "Financial documents showing funds, such as “bank statements which detail the origin of the funds held”, and proof of earnings (GOV.UK guide, updated 8 October 2026)", "It is the document that explains the origin of a large balance: a plot sold, a gift from a parent, business profit"],
    ["Canada", "“At least 6 months of account details, including balances”, plus an employer letter with current salary (IRCC, modified 16 November 2026)", "Balances that jump without a recorded source are what officers notice; the statement records that source"],
    ["Schengen states", "Documents showing “sufficient means of subsistence” for the stay (Visa Code, Article 14(1)(c))", "Property, savings and income declared to FBR support the claim that the means are lawful"],
])}
<p>So the wealth statement is supporting evidence. Its value depends on one thing: that it agrees with every other paper in the file. A Rs 4,200,000 balance on the bank statement and Rs 900,000 of declared cash and bank on the wealth statement is a gap the officer can see in a minute. Our country guides for the {a(X["uk"], "UK visitor visa")}, the {a(X["us"], "USA B1/B2")} and {a(X["au"], "Australia")} explain which FBR papers each embassy is usually given. This guide is about correcting the statement before you hand it over.</p>

<h2 id="law">What the Law Lets You Revise, and When</h2>
<p>Section 116(3) of the Income Tax Ordinance 2001, as amended up to 30 June 2026, is the only route to correct a filed wealth statement. Read in full, it sets five conditions:</p>
{table(["Condition", "What section 116(3) says"], [
    ["Trigger", "You “discover any omission or wrong statement” in a statement you have filed"],
    ["What you file", "A revised wealth statement “along with the revised wealth reconciliation and the reasons for filing” it"],
    ["How", "Under intimation to the Commissioner, in the prescribed form and manner (on IRIS)"],
    ["Deadline", "Before you receive a notice under section 122(9) for that tax year"],
    ["Outer limit", "Not after five years from the due date of the return for that tax year (Explanation added in 2020)"],
])}
<p>The proviso matters most for visa applicants. Where the Commissioner thinks a revision “is not for the purpose of correcting a bona fide omission or wrong statement”, he may declare it void by a written order, after giving you a hearing. A revision filed a week before a visa appointment that suddenly adds Rs 3,000,000 of cash at home is exactly the kind that invites that question.</p>
<p>A wealth statement revision does not change the income in your return. If the error is in income too, for example rent you never declared, the return must be revised under section 114(6), which has its own conditions; our guide to the {a(X["rev"], "revised return window")} covers those. The IRIS steps for the wealth statement itself are in our {a(X["how"], "revision how-to")}.</p>

<h2 id="fix">Errors Worth Fixing Before You Apply</h2>
<p>These are the corrections that make the statement true and the visa file consistent. Each has its own guide in this series.</p>
{table(["What went wrong", "Why it hurts the visa file", "The correction"], [
    ["A savings or foreign-currency account left out", "Bank statement shows an account FBR has never seen", a(B["bank"], "Add it at the 30 June balance")],
    ["Cash in hand typed as a round guess", "A large cash figure with no bank trail looks invented", a(B["cash"], "Correct to the real figure with its source")],
    ["A plot sold but still shown, or bought but missing", "Property papers and the statement disagree", a(B["prop"], "Record the sale or purchase at actual cost and price")],
    ["A parent's transfer booked as your income", "Inflates income you cannot show tax on", a(B["gift"], "Reclassify as a gift from a relative")],
    ["Money or property abroad not declared", "The officer may see the foreign account; FBR has no record", a(B["foreign"], "Declare it, and check section 116A")],
])}
<p>Two smaller corrections also come up often: a dependent spouse's assets missing (section 116(1)(b) requires the assets of a spouse, minor children and other dependents, and the Explanation added in 2024 limits the spouse's assets to a dependent spouse), and a car still shown after it was sold. Both are covered in our guide to {a(X["missing"], "assets missing from a wealth statement")}.</p>

<h2 id="never">Revisions That Do Lasting Damage</h2>
<p>The pressure before a visa appointment is to make the statement look richer. The Ordinance makes that expensive in three ways.</p>
<ul>
<li><strong>Section 111.</strong> If you own money, an investment or a valuable article and offer no explanation of its source, or an explanation the Commissioner finds unsatisfactory, its value is added to your income under “Income from Other Sources” to the extent it is not adequately explained. Cash added to impress an embassy is cash you must later explain to FBR.</li>
<li><strong>The void proviso.</strong> A revision that does not correct a bona fide error can be declared void, so the original statement stands and the revision itself becomes part of the record.</li>
<li><strong>The visa side.</strong> Canada's inadmissibility page lists misrepresentation, which “includes providing false information or withholding information”, and says an inadmissible person is “denied a visa”, refused entry or removed. The UK guide warns that a decision maker may ask for additional information, so a figure you cannot support can be questioned.</li>
</ul>
<p>The safe rule is short: revise to match the documents you have, never revise to create documents you do not have.</p>

<h2 id="example">A Worked Example</h2>
<p>Hamza, a salaried engineer in Lahore, plans a UK family visit. His TY2026 wealth statement shows Rs 650,000 in one bank account and Rs 300,000 cash. His real position on 30 June 2026 was Rs 650,000 in his salary account, Rs 1,150,000 in a savings account opened in March, and about Rs 40,000 cash. In April his father transferred Rs 1,000,000 to the savings account by bank transfer.</p>
{table(["Item", "Filed statement", "Revised statement", "Reason given"], [
    ["Salary account", "Rs 650,000", "Rs 650,000", "No change"],
    ["Savings account", "Not shown", "Rs 1,150,000", "Account omitted; balance per bank certificate"],
    ["Cash in hand", "Rs 300,000", "Rs 40,000", "Estimate replaced by actual"],
    ["Gift from father", "Not shown", "Rs 1,000,000 (reconciliation)", "Gift from a relative received by bank transfer"],
])}
<p>Net assets rise by Rs 890,000. The revised reconciliation shows the Rs 1,000,000 gift as an inflow and restates personal expenses to the real figure, so it balances without any invented income. Every figure now matches a bank document, and the gift is from a relative as defined in section 85(5), received through a banking channel. Hamza revises in November, before any notice, and only then books his appointment.</p>

<h2 id="timing">Timing and the Papers to Keep</h2>
<ol>
<li><strong>Collect first.</strong> Bank certificates of balance as on 30 June, property and vehicle papers, and transfer receipts for gifts.</li>
<li><strong>Revise next.</strong> File the revised statement and reconciliation on IRIS with the reasons, while no 122(9) notice exists for that year.</li>
<li><strong>Keep the trail.</strong> Save the revised acknowledgement and the reasons note. If an officer or FBR asks why two versions exist, the answer is on one page.</li>
<li><strong>Apply last.</strong> Bank statements you attach should be recent; the UK guide says not to use bank statements or letters issued more than a year before the application.</li>
</ol>
<p>If the year you need is older, our guide to revising the {a(X["five"], "last five years")} explains how far back the law allows you to go.</p>
""",
    faqs=[
        ("Can I revise my wealth statement just before a visa interview?",
         "Yes, if you are correcting a genuine omission or wrong statement and no section 122(9) notice has been received for that year. Do it before you apply, and keep the revised acknowledgement and reasons together."),
        ("Does the UK embassy require an FBR wealth statement?",
         "The GOV.UK supporting documents guide does not list it. It asks for financial documents such as bank statements that detail the origin of funds. A wealth statement can explain that origin, so it should agree with the bank statements."),
        ("Will a revised wealth statement look suspicious?",
         "A correction backed by bank certificates and a clear reasons note is normal. A last-minute revision that adds large cash with no source is what draws questions, from FBR and from an officer."),
        ("Do I also need to revise my income tax return?",
         "Only if the error affects income. A wealth statement correction alone is filed under section 116(3); a change in income needs a revised return under section 114(6), which has separate conditions."),
        ("How far back can I revise?",
         "The Explanation to section 116(3) bars revision after five years from the due date of the return for that tax year."),
        ("What does the revision cost?",
         "Wealth statement preparation is Rs 2,000 on our pricing page. A revision with a fresh reconciliation is a fixed fee we confirm after seeing your filed statement, before any work starts."),
    ],
    sources=[S_ITO, S_UKG, S_UKSV, S_CA, S_CAR, S_VC, S_IRIS],
    related=[(X["uk"], "UK visitor visa wealth statement"), (X["how"], "How to revise on IRIS"), (B["bank"], "Bank balance corrections"), (X["svc"], "Wealth statement service")],
)

# 2 ---------------------------------------------------------------- Schengen
SCHENGEN = post(
    slug=SL["schengen"],
    title="Schengen Visa: Revising Your Wealth Statement First",
    h1="Schengen Visa From Pakistan: Revising Your FBR Wealth Statement So It Matches Your Means of Subsistence",
    crumb="Schengen Visa Wealth Statement",
    description="Schengen visa from Pakistan? How means of subsistence is judged under the Visa Code and Borders Code, and how to correct your FBR wealth statement to match.",
    keywords="schengen visa wealth statement, schengen visa fbr documents, means of subsistence schengen pakistan, wealth statement revision schengen, europe visa tax return pakistan",
    read="11 min read",
    banner="Schengen states judge your funds against the length of your stay. A wealth statement that contradicts your bank papers weakens the whole file.",
    tldr=("Article 14(1)(c) of the EU Visa Code asks Schengen applicants for documents showing sufficient means of subsistence for the stay, and "
          "Article 6(4) of the Schengen Borders Code assesses those means by the length and purpose of the stay against average budget board and "
          "lodging costs in the state you visit. The FBR wealth statement is not a named requirement, but it is often in the file as proof that your "
          "assets are lawful and declared. If it disagrees with your bank statements or property papers, revise it under section 116(3) before you "
          "apply: real figures, a revised reconciliation and written reasons, before any section 122(9) notice for that year."),
    lead=("Pakistani applicants for Germany, Italy, Spain, France and the other Schengen states usually build a financial file of bank statements, "
          "a salary letter or business papers, and FBR documents. The EU rules do not tell you which Pakistani document to use; they tell the consulate "
          "what it must be satisfied about. Knowing that test explains which wealth statement errors matter and which do not, and how to correct the "
          "ones that do without creating a tax problem at home."),
    answers={
        "rule": "Visa Code Article 14(1)(c): documents showing sufficient means of subsistence for the stay and the return, or the ability to acquire them lawfully.",
        "assess": "Borders Code Article 6(4): means are judged by duration and purpose of stay, against average budget board and lodging prices, times the number of days.",
        "fbr": "The wealth statement shows the means are lawful and declared; it must agree with the bank and property papers in the same file.",
        "fix": "Correct omitted accounts, wrong balances, unrecorded gifts and stale property entries, with a revised reconciliation and reasons.",
        "sponsor": "If a host or relative sponsors you, the Borders Code accepts sponsorship declarations as possible evidence; the sponsor's own papers then matter too.",
    },
    svc=svc("Schengen File Check and Wealth Statement Revision",
            "We read your Schengen financial file the way a consulate does: duration of stay against funds, and every FBR figure against the bank papers.",
            ["Compare your bank statements, salary or business papers with the filed wealth statement",
             "Revise the wealth statement and reconciliation on IRIS where a figure is genuinely wrong",
             "Write the reasons note for each change",
             "Check a sponsoring relative's wealth statement if their funds support your trip",
             "Return a short English summary of the corrected figures for your file"],
            ["Topping up the balance just before applying, with no recorded source, invites questions on both sides",
             "A revised statement that does not reconcile can be declared void by FBR",
             "Mismatched figures across documents weaken an otherwise strong application"],
            "Schengen appointment booked and the FBR papers do not match?"),
    wa_text="Assalam o Alaikum, Schengen visa ke liye wealth statement check aur revise karwana hai.",
    body=f"""
{SERIES("schengen")}

<h2 id="rule">What the EU Rules Actually Ask For</h2>
<p>Two EU regulations set the financial test for a short-stay Schengen visa. The Visa Code, Regulation (EC) No 810/2009, says in Article 14(1)(c) that an applicant must present “documents indicating that the applicant possesses sufficient means of subsistence both for the duration of the intended stay” and for the return or transit, or that he is in a position to acquire such means lawfully. Article 14(3) points to a non-exhaustive list of supporting documents in Annex II, and Article 14(5a), added in 2019, lets the Commission adopt a harmonised list for each country.</p>
<p>The Visa Code does not name an FBR return or wealth statement. Pakistani applicants include them because they show that the money in the bank was earned or received lawfully and declared at home. Our country guides for {a(X["germany"], "Germany")} and {a(X["spain"], "Spain")} cover the wider FBR paperwork; this guide deals with correcting the wealth statement inside that file.</p>

<h2 id="assess">How Means of Subsistence Is Judged</h2>
<p>Article 6(4) of the Schengen Borders Code, Regulation (EU) 2016/399, explains the test: “Means of subsistence shall be assessed in accordance with the duration and the purpose of the stay and by reference to average prices in the Member State(s) concerned for board and lodging in budget accommodation, multiplied by the number of days stayed.” Reference amounts are set by each Member State and notified to the Commission.</p>
<p>Three practical consequences follow for a Pakistani file:</p>
<ul>
<li><strong>Length of stay drives the figure.</strong> A 30-day trip needs more than a 10-day one at the same daily reference amount, so the balance you show should fit the itinerary.</li>
<li><strong>Several forms of evidence count.</strong> Article 6(4) says cash, travellers' cheques and credit cards may be evidence, and that sponsorship declarations or a host's guarantee letter may also constitute evidence of sufficient means.</li>
<li><strong>Consistency is the real test.</strong> A balance that fits the stay but appears from nowhere a fortnight before the application is weaker than a smaller one with a history.</li>
</ul>

<h2 id="fbr">Where the Wealth Statement Helps, and Where It Hurts</h2>
{table(["Situation in the file", "What a consistent wealth statement shows", "What an inconsistent one suggests"], [
    ["Rs 2,500,000 balance in a savings account", "The account and its 30 June balance, with salary and savings building it up", "An account missing from FBR records, so the funds look new or undeclared"],
    ["Recent large credit from a parent", "A gift from a relative recorded in the reconciliation", "Income or a loan nobody can explain"],
    ["Property papers to show ties to Pakistan", "The plot at its cost, held for years", "A plot that FBR has never been told about"],
    ["Business owner with irregular income", "Business capital and drawings that match the bank flow", "Cash figures that do not agree with deposits"],
])}
<p>The wealth statement shows assets on 30 June of the tax year, while the bank statements you attach usually cover the last few months. They will not be identical, and that is normal. What matters is that the 30 June position is true and that later movements in the bank statement have an obvious source.</p>

<h2 id="fix">Correcting the Statement Under Section 116(3)</h2>
<p>If you find an error, section 116(3) of the Income Tax Ordinance lets you file a revised wealth statement with a revised wealth reconciliation and the reasons for revision, under intimation to the Commissioner, before receiving a notice under section 122(9) for that year, and within five years of that year's return due date. For a Schengen file the usual corrections are:</p>
<ol>
<li><strong>A missing account.</strong> Add it at the bank's certified 30 June balance; see our guide to {a(B["bank"], "bank balance corrections")}.</li>
<li><strong>A parent's or sibling's transfer.</strong> Record it as a gift from a relative in the reconciliation, not as your income; see {a(B["gift"], "gifts and loans")}.</li>
<li><strong>A guessed cash figure.</strong> Replace it with the real amount; see {a(B["cash"], "cash in hand")}.</li>
<li><strong>A plot or car sold or bought.</strong> Update it at actual cost or sale price; see {a(B["prop"], "property revisions")}.</li>
</ol>
<p>The proviso to section 116(3) allows the Commissioner to declare a revision void, after a hearing, if it does not correct a bona fide error. A correction backed by a bank certificate passes that test easily. A revision that adds funds to reach a consulate's reference amount does not.</p>

<h2 id="example">Example: A Twelve-Day Trip to Italy</h2>
<p>Ayesha, a Lahore teacher, applies for a twelve-day tourist visa. Her bank statement shows Rs 1,600,000 at the end of October, built from salary and a Rs 700,000 transfer from her brother in May. Her TY2026 wealth statement shows Rs 300,000 in the bank and no gift.</p>
{table(["Line", "Filed", "Revised", "Evidence"], [
    ["Bank balance on 30 June 2026", "Rs 300,000", "Rs 1,180,000", "Bank certificate of balance"],
    ["Gift from brother (reconciliation)", "Not shown", "Rs 700,000", "Bank transfer record; brother is a relative under s.85(5)"],
    ["Personal expenses", "Rs 480,000", "Rs 300,000", "The earlier figure was a balancing entry, not her spending"],
])}
<p>After the revision, the reconciliation explains the Rs 880,000 rise, and the balance in her October statement follows naturally from the 30 June figure plus four months of salary. The revision is filed before any notice, with reasons, and the consulate file now tells one story.</p>

<h2 id="sponsor">When a Relative Sponsors the Trip</h2>
<p>Many Pakistani applicants travel on a parent's or spouse's funds. The Borders Code accepts sponsorship declarations as possible evidence of means. In that case it is the sponsor's papers that carry weight, and the sponsor's wealth statement must support the money they are giving. Our guide for {a(B["sponsor"], "sponsor parents")} explains how a sponsoring parent checks and corrects their own statement.</p>
""",
    faqs=[
        ("Is an FBR wealth statement required for a Schengen visa?",
         "The Visa Code does not name it. Article 14(1)(c) asks for documents showing sufficient means of subsistence. Pakistani applicants often add the FBR return and wealth statement to show those means are lawful and declared."),
        ("How much money do I need to show for Schengen?",
         "Each Member State sets its own reference amount. Under Borders Code Article 6(4) means are judged by the duration and purpose of the stay, against average budget board and lodging prices multiplied by the number of days."),
        ("My bank balance today is higher than in my wealth statement. Is that a problem?",
         "Not by itself. The wealth statement shows 30 June; the bank statement shows recent months. It becomes a problem only if the 30 June figure is wrong or the later rise has no source."),
        ("Can I add my brother's gift to my wealth statement?",
         "Yes, as a gift from a relative in the reconciliation, if it was genuinely received. A brother is a relative under section 85(5). Receiving it by bank transfer keeps the record clean."),
        ("When is it too late to revise?",
         "After you receive a section 122(9) notice for that tax year, or five years after that year's return due date."),
        ("Can you check my whole Schengen file?",
         "We check the FBR side: the return, wealth statement and how they match your bank papers. Visa decisions rest with the consulate."),
    ],
    sources=[S_VC, S_SBC, S_ITO, S_IRIS],
    related=[(B["visa"], "Revision before any visa"), (X["germany"], "Germany visa FBR papers"), (B["sponsor"], "Sponsor parents"), (X["svc"], "Wealth statement service")],
)

# 3 ---------------------------------------------------------------- Canada
CANADA = post(
    slug=SL["canada"],
    title="Canada Visitor Visa: Wealth Statement Revision Guide",
    h1="Canada Visitor Visa From Pakistan: Making Your Wealth Statement Agree With Six Months of Bank Records",
    crumb="Canada Visitor Visa Wealth Statement",
    description="Canada visitor visa from Pakistan: IRCC asks for 6 months of bank details. How to correct your FBR wealth statement under s.116(3) so balances agree.",
    keywords="canada visitor visa wealth statement, canada visa bank statement pakistan, ircc proof of funds pakistan, wealth statement revision canada visa, canada trv fbr documents",
    read="11 min read",
    banner="IRCC reads six months of balances. Large credits without a recorded source are the first thing a wealth statement should explain.",
    tldr=("IRCC's visitor visa page asks for a bank account statement with “at least 6 months of account details, including balances”, in your "
          "name and address, and an employer letter with your current salary dated no earlier than three months before you apply. Your FBR wealth "
          "statement is not on that list, but applicants often add it, and it should explain where the money in those six months came from. If an "
          "account, a gift or a property sale is missing or wrong, revise the statement under section 116(3) before applying. IRCC lists "
          "misrepresentation, including false or withheld information, as a reason to be refused a visa."),
    lead=("A Canadian visitor visa file from Pakistan is usually decided on two questions: can you pay for the trip, and will you come back. The money "
          "question is answered mostly by your bank statement. When the bank statement shows a large deposit or a balance that does not fit your "
          "salary, an FBR wealth statement that records the source, a plot sold, a parent's gift, business profit, can help. One that contradicts "
          "the bank statement does the opposite. Here is how to line them up lawfully."),
    answers={
        "ircc": "A bank account statement with at least six months of account details and balances, proof it is your account, and an employer letter with current salary.",
        "deposits": "IRCC's page does not mention large deposits; the six-month history is what shows them. A recorded source in the wealth statement is the clean answer.",
        "fix": "Revise omitted accounts, unrecorded gifts, sold or bought property and guessed cash, with a revised reconciliation and reasons.",
        "risk": "IRCC treats false or withheld information as misrepresentation, a ground for refusal. Revise only to make the statement true.",
    },
    svc=svc("Canada Visa: FBR Papers That Match Your Bank Records",
            "We line up six months of your bank statement against the wealth statement and reconciliation, and correct the FBR side where it is genuinely wrong.",
            ["Mark every large credit in your six-month bank statement and find its source",
             "Check that each source is recorded in the wealth statement or reconciliation",
             "Revise the statement and reconciliation on IRIS with written reasons",
             "Advise on a revised return where income is also affected",
             "Give you a short English note of what changed and why"],
            ["A deposit with no recorded source is the question an officer is most likely to ask",
             "Showing borrowed money as your own savings is misrepresentation on the visa side",
             "A revision without matching reconciliation can be declared void by FBR"],
            "Canada visitor visa and a bank statement that needs explaining?"),
    wa_text="Assalam o Alaikum, Canada visitor visa ke liye wealth statement aur bank statement match karwana hai.",
    body=f"""
{SERIES("canada")}

<h2 id="ircc">What IRCC Asks For</h2>
<p>The IRCC page “Apply for a visitor visa” (modified 16 November 2026) lists a bank account statement among the documents you might need, because it “can help us understand if you have enough money to support yourself during your stay in Canada.” It should show:</p>
{table(["Item on the IRCC page", "What it means for a Pakistani applicant"], [
    ["Bank name and contact", "A statement on bank letterhead or a stamped printout"],
    ["Proof it is your account", "Your name and address on the statement"],
    ["At least 6 months of account details, including balances", "Every credit and debit in that period is visible to the officer"],
    ["Employer letter with current salary, dated no earlier than 3 months before you apply", "Salary credits in the statement should match this letter"],
])}
<p>The eligibility page (modified 28 August 2026) adds that you must “have enough money for your stay”, and that the amount depends on how long you stay and whether you stay in a hotel or with friends or relatives. Tax returns and wealth statements are not named on these pages. If you are applying for permanent residence rather than a visit, our {a(X["canpr"], "Canada PR guide")} covers that route.</p>

<h2 id="deposits">Why Six Months of History Changes the Picture</h2>
<p>A single balance certificate hides how the money arrived. Six months of transactions do not. A teacher earning Rs 120,000 a month whose balance rises from Rs 400,000 to Rs 2,900,000 in May will be asked, in effect, where Rs 2,500,000 came from. IRCC's page says nothing about large deposits as such, but the six-month history makes them visible.</p>
<p>The FBR wealth statement is where that answer is recorded in Pakistan. If the money came from a plot sold in May, the TY2026 statement (30 June 2026) should show the plot gone and the sale proceeds in the bank. If it came from a father, the reconciliation should show a gift from a relative. If it is a loan from a friend, it is a liability, not savings, and should be shown as one.</p>

<h2 id="fix">The Corrections That Usually Come Up</h2>
{table(["Bank statement shows", "Wealth statement shows", "Correction under s.116(3)"], [
    ["A second account with savings", "Only the salary account", "Add the account at its 30 June balance"],
    ["Rs 2,500,000 credit from a property buyer", "The plot still held", "Remove the plot, record the sale proceeds and any gain; see " + a(B["prop"], "property revisions")],
    ["Monthly transfers from a parent abroad", "Nothing in the reconciliation", "Record gifts from a relative; check " + a(B["foreign"], "foreign assets") + " if the parent's money sits abroad in your name"],
    ["A friend's Rs 800,000 credited for a few weeks", "Nothing", "Show the loan as a liability, or do not rely on that balance at all"],
])}
<p>Section 116(3) of the Income Tax Ordinance requires the revised statement, a revised wealth reconciliation and written reasons, filed under intimation to the Commissioner before any section 122(9) notice for that year and within five years of that year's return due date. Our {a(X["how"], "IRIS revision guide")} walks through the screens.</p>

<h2 id="salary">Salary Credits, the Employer Letter and the Return</h2>
<p>IRCC asks for an employer letter that includes your current salary and is dated no earlier than three months before you apply. The officer can then compare three figures: the salary in the letter, the monthly salary credits in your six-month bank statement, and the income in your FBR return. They will rarely match to the rupee, because the letter shows gross pay and the bank shows pay after tax and deductions. They should still be plainly consistent. A return declaring Rs 900,000 a year next to a letter showing Rs 250,000 a month is a gap the wealth statement cannot explain; it points to an income figure in the return that needs a revised return under section 114(6), not just a revised wealth statement. Our {a(X["rev"], "revised return guide")} explains those conditions.</p>

<h2 id="borrowed">Borrowed Balances: The Mistake to Avoid</h2>
<p>A common Pakistani practice is to park a relative's or friend's money in the applicant's account before a visa application and return it afterwards. Section 39(3) of the Ordinance already treats a loan, advance, deposit or gift received from a non-bank person otherwise than by crossed cheque, banking channel or digital means from a person holding an NTN as income from other sources, so cash parked this way can become taxable income at home. On the visa side, IRCC's inadmissibility page lists misrepresentation, which “includes providing false information or withholding information”, and says a person found inadmissible is denied a visa or refused entry. Presenting a loan as your savings fits that description.</p>
<p>The honest version is usually stronger: your own balance, plus a declared sponsor or host where one exists. IRCC's page itself notes that staying with friends or relatives changes how much money you need.</p>

<h2 id="example">Example: A Retired Couple Visiting Their Son</h2>
<p>Mr and Mrs Qureshi, retired in Rawalpindi, plan a six-week visit to their son in Toronto. Their joint bank statement shows a Rs 3,200,000 credit in February 2026 from the sale of a shop, and pension credits each month. Mr Qureshi's TY2026 wealth statement still lists the shop at its old cost and shows only Rs 450,000 in the bank.</p>
{table(["Line", "Filed", "Revised", "Reason"], [
    ["Shop, Saddar", "Rs 1,100,000 (cost)", "Removed", "Sold February 2026, sale deed attached"],
    ["Bank balance, 30 June 2026", "Rs 450,000", "Rs 3,310,000", "Sale proceeds and pension, bank certificate"],
    ["Reconciliation: sale proceeds", "Not shown", "Rs 3,200,000 received", "Against cost Rs 1,100,000; gain dealt with in the return"],
])}
<p>Because the sale also creates a capital gain, the return needs attention too, not only the wealth statement. Once both are right, the February credit on the bank statement has an FBR record behind it, and the six-week stay is clearly affordable.</p>
""",
    faqs=[
        ("Does IRCC ask for my FBR tax return or wealth statement?",
         "The visitor visa page we checked lists a bank account statement and an employer letter, not FBR documents. Applicants often add FBR papers to show where funds came from; they should agree with the bank statement."),
        ("How many months of bank statements does Canada want?",
         "IRCC's page says at least six months of account details, including balances."),
        ("A large deposit appears in my bank statement. What should I do?",
         "Make sure its source is recorded: a property sale, a gift from a relative, or business income. If your wealth statement omits it, revise under section 116(3) before applying."),
        ("Can a relative put money in my account for the visa?",
         "Presenting someone else's money as your savings is risky on both sides: IRCC treats false information as misrepresentation, and section 39(3) can tax some unrecorded loans and gifts as income."),
        ("Is there a deadline for revising?",
         "Yes. Before you receive a section 122(9) notice for that tax year, and never more than five years after that year's return due date."),
        ("What if the property sale also needs to be in my return?",
         "Then the return is revised as well, under section 114(6) and its conditions. We check both and tell you before filing."),
    ],
    sources=[S_CA, S_CAE, S_CAR, S_ITO, S_IRIS],
    related=[(B["visa"], "Revision before any visa"), (X["canpr"], "Canada PR FBR guide"), (B["prop"], "Property sale revisions"), (X["svc"], "Wealth statement service")],
)
