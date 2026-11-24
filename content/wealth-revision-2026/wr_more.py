"""Wealth statement revision series, posts 4-10 (facts checked 24 November 2026; see wr_common.py)."""
from wr_common import *

# 4 ---------------------------------------------------------------- sponsor parent
SPONSOR = post(
    slug=SL["sponsor"],
    title="Sponsor Parent's Wealth Statement for a Student Visa",
    h1="Funding a Child's Study Abroad? Checking and Revising the Sponsor Parent's Wealth Statement First",
    crumb="Sponsor Parent Wealth Statement",
    description="When a parent sponsors a student visa, the parent's FBR wealth statement is the one tested. Common errors, s.116 rules and how to revise before applying.",
    keywords="sponsor wealth statement student visa, parent sponsor fbr documents, father wealth statement student visa pakistan, sponsor tax return student visa, revise sponsor wealth statement",
    read="11 min read",
    banner="When the parent pays, the parent's papers carry the application. A sponsor's wealth statement that cannot support the fees is a weak link.",
    tldr=("When a parent funds study abroad, the money and its source are the parent's, so the parent's FBR return and wealth statement are the ones "
          "that matter. Section 116(1) asks every resident individual for assets and liabilities, including foreign ones, those of a dependent spouse, "
          "minor children and other dependents, assets transferred to others and total family expenditure. Fees sent abroad, an account opened for "
          "the student and money transferred to an adult child all belong in that picture. If the sponsor's statement leaves them out or records them "
          "wrongly, the sponsor revises under section 116(3), with a revised reconciliation and reasons, before any 122(9) notice and within five years."),
    lead=("Most student visa files from Pakistan are funded by a father, a mother or both. The student usually has little income of their own, so the "
          "officer looks through the student to the sponsor: who they are, what they earn, what they own, and whether paying tuition and living costs "
          "is realistic. In Pakistan the sponsor's financial story is recorded in their FBR return and wealth statement. This guide is for the parent: "
          "what to check in your own statement before your child applies, and how to correct it lawfully."),
    answers={
        "whose": "The sponsor's. If the parent pays, the parent's income, assets and their source are what the officer needs to believe.",
        "what": "Section 116(1): your assets and liabilities, those of dependents, assets transferred to others, and total family expenditure, with a reconciliation.",
        "errors": "Missing accounts, an asset sold to raise fees still shown, fees paid abroad missing from expenses, and transfers to the child not recorded.",
        "child": "A minor or dependent child's assets go in the parent's statement; an adult child who files separately records gifts from the parent in their own reconciliation.",
    },
    svc=svc("Sponsor Statement Review Before the Student Applies",
            "We check the sponsoring parent's return and wealth statement against the funds promised in the student's application, and revise where the record is wrong.",
            ["Compare the sponsor's bank papers and property sale deeds with the filed wealth statement",
             "Record fees, deposits and transfers for the student correctly",
             "Revise the wealth statement and reconciliation with written reasons",
             "Prepare or fix the student's own return if the student is an adult filer",
             "Summarise the corrected position in a short English note"],
            ["A sponsor whose declared income cannot plausibly fund the study weakens the application",
             "Selling a plot for fees without updating the statement leaves a gap FBR can question",
             "Money moved to the child's account without a record looks like undeclared income on one side"],
            "Paying for your child's studies abroad?"),
    wa_text="Assalam o Alaikum, bachay ke student visa ke liye sponsor (walid) ka wealth statement check karwana hai.",
    body=f"""
{SERIES("sponsor")}

<h2 id="whose">Whose Papers the Officer Actually Weighs</h2>
<p>Where someone else pays for a trip, the UK's supporting documents guide (updated 8 October 2026) asks for evidence of “what support is being provided”, “how this support is being provided” and that “the person supporting you has enough funds to adequately support themselves and their dependents”. That passage is written for visitors, but the logic is the same for any sponsored application: the sponsor's capacity is what is tested. Student visa rules differ by country; our guides for the {a(X["ukstu"], "UK student visa")} and the {a(X["f1"], "USA F-1")} list the documents each embassy expects. In every case, if the parent's FBR papers are in the file, they have to hold up.</p>

<h2 id="what">What the Sponsor's Wealth Statement Must Contain</h2>
<p>Section 116(1) of the Income Tax Ordinance 2001, as amended up to 30 June 2026, lists what a wealth statement gives particulars of. Section 116(2) makes every resident individual filing a return furnish it, with a wealth reconciliation statement, for that year.</p>
{table(["Clause", "What it covers", "Sponsor's angle"], [
    ["116(1)(a)", "Your total assets and liabilities, including foreign assets and foreign liabilities", "Every account the fees come from, any plot or shares sold, money already sent abroad"],
    ["116(1)(b)", "Assets and liabilities of your spouse, minor children and other dependents", "A dependent student's own account in Pakistan; a dependent spouse's assets (Explanation added 2024)"],
    ["116(1)(c)", "Assets transferred to any other person and the consideration", "A plot gifted or money transferred to an adult child"],
    ["116(1)(d)", "Total expenditure of you and your family and its details", "Tuition, housing deposits and travel paid in the year"],
    ["116(1)(e)", "The reconciliation statement of wealth", "Explains how net assets moved after fees were paid"],
])}

<h2 id="errors">The Errors We See Most in Sponsors' Statements</h2>
<ol>
<li><strong>The fee account is missing.</strong> Parents often open a separate account to collect funds for the student. If it is not in the statement, the balance the embassy sees is invisible to FBR. Our guide to {a(B["bank"], "bank balance revisions")} covers adding it.</li>
<li><strong>A plot sold for fees is still shown.</strong> The sale proceeds then appear in the bank with no source. See {a(B["prop"], "property revisions")}.</li>
<li><strong>Fees paid are not in expenditure.</strong> A parent who sent Rs 6,000,000 for tuition but shows Rs 900,000 of household expenses has a reconciliation that cannot be true.</li>
<li><strong>Money moved to the student is unrecorded.</strong> For a dependent child it stays inside the parent's statement. For an adult child who files separately, the parent shows the transfer and the child shows a gift from a relative.</li>
<li><strong>Money held abroad for the student.</strong> An account opened abroad in the parent's name is a foreign asset under section 116(1)(a), and may trigger section 116A; see {a(B["foreign"], "foreign assets")}.</li>
</ol>

<h2 id="child">Dependent Child or Adult Filer?</h2>
{table(["Student's position", "Where the student's money is recorded", "What the parent records"], [
    ["Minor, or a dependent adult with no return", "In the parent's wealth statement under 116(1)(b)", "The student's account as a dependent's asset; fees as family expenditure"],
    ["Adult who files their own return", "In the student's own wealth statement", "The transfer to the child under 116(1)(c); the child records a gift from a relative"],
])}
<p>A child is a relative under section 85(5), which covers descendants of the individual's grandparents. Under section 39(1)(la) a gift received from a relative is not treated as income from other sources, so a parent's gift does not create tax for the student, provided it is genuine and recorded. Sending it through a bank keeps the trail obvious; our guide to {a(B["gift"], "gifts and loans in the family")} covers the details.</p>

<h2 id="business">When the Sponsor Runs a Business</h2>
<p>A sponsoring parent who is a trader or shopkeeper usually funds fees from the business. In the wealth statement that shows as business capital going down, or drawings going up, in the year the fees were paid. If the business accounts show steady capital while Rs 5,000,000 of fees left the family, one of the two records is wrong. The fix is to record the drawings that actually funded the fees, so the business side and the personal side agree. Where the business income itself was understated, the return is the document to revise, not only the wealth statement.</p>

<h2 id="example">Example: Fees Raised by Selling a Plot</h2>
<p>Mr Ahmed, a Faisalabad trader, sold a 5 marla plot in April 2026 for Rs 9,000,000 to fund his daughter's master's in the UK. He paid Rs 4,200,000 of tuition and deposits by June and kept the rest in a new account. His TY2026 wealth statement still shows the plot at cost, omits the new account and shows Rs 1,400,000 of household expenses.</p>
{table(["Line", "Filed", "Revised", "Reason"], [
    ["Plot, 5 marla", "Rs 3,500,000 (cost)", "Removed", "Sold April 2026; sale consideration Rs 9,000,000 disclosed under 116(1)(c)"],
    ["New savings account", "Not shown", "Rs 4,800,000", "Account opened for fees; bank certificate"],
    ["Family expenditure", "Rs 1,400,000", "Rs 5,600,000", "Includes tuition and deposits Rs 4,200,000"],
])}
<p>The sale also produces a capital gain that belongs in the return, which is revised alongside. After the revision, the funds promised in the student's application have an FBR record: a plot sold, proceeds banked, fees paid.</p>

<h2 id="how">How the Sponsor Revises</h2>
<p>Section 116(3) allows the revision when an omission or wrong statement is discovered: a revised wealth statement, a revised wealth reconciliation and written reasons, filed under intimation to the Commissioner on IRIS, before receiving a section 122(9) notice for that year, and within five years of that year's return due date. The Commissioner may declare a revision void if it is not a bona fide correction, so every change should point to a document. Our {a(X["how"], "IRIS revision guide")} shows the screens.</p>
""",
    faqs=[
        ("Whose wealth statement matters for a sponsored student visa?",
         "The sponsor's. If a parent funds the study, the parent's income, assets and their source are what the officer needs to accept."),
        ("Should my child's bank account appear in my wealth statement?",
         "If the child is a minor or a dependent without their own return, yes, under section 116(1)(b). An adult child who files separately shows it in their own statement."),
        ("Are tuition fees part of the wealth statement?",
         "They are part of total expenditure under section 116(1)(d), so they belong in the reconciliation for the year they were paid."),
        ("Is money I give my child taxable for them?",
         "A gift from a relative is excluded from income under section 39(1)(la), and a child is a relative under section 85(5). Record it on both sides and send it through a bank."),
        ("I sold property to pay fees. What needs changing?",
         "Remove the property, record the sale consideration and the bank proceeds, and deal with any gain in the return."),
        ("How long do I have to revise?",
         "Until you receive a section 122(9) notice for that year, and never beyond five years from that year's return due date."),
    ],
    sources=[S_ITO, S_UKG, S_SBC, S_IRIS],
    related=[(X["ukstu"], "UK student visa FBR papers"), (X["f1"], "USA F-1 documents"), (B["gift"], "Gifts and loans in the family"), (X["svc"], "Wealth statement service")],
)

# 5 ---------------------------------------------------------------- refused on funds
REFUSED = post(
    slug=SL["refused"],
    title="Visa Refused Over Funds? Correcting Your Wealth Statement",
    h1="Visa Refused Over Funds or Their Source? Correcting Your Wealth Statement Before You Reapply",
    crumb="Visa Refused: Wealth Statement Fix",
    description="Visa refused because of funds or their source? How to read the refusal against your FBR wealth statement, what s.116(3) lets you correct, and how to explain it.",
    keywords="visa refused bank statement pakistan, visa refusal funds wealth statement, reapply visa after refusal fbr, visa rejected source of funds pakistan, correct wealth statement after visa refusal",
    read="11 min read",
    banner="A second application with the same unexplained numbers is likely to meet the same doubt. Fix the record first, then explain the change.",
    tldr=("If a visa was refused because the officer was not satisfied about your funds or where they came from, compare the refusal reasons with "
          "your FBR wealth statement before reapplying. Correct genuine errors under section 116(3), with a revised reconciliation and written "
          "reasons, as long as no section 122(9) notice has been received for that year and five years have not passed since its return due date. "
          "The embassy may still hold the earlier papers, so explain the revision in your cover letter. Never correct upwards to reach a number: "
          "section 111 taxes money that cannot be explained, and FBR can declare a revision void if it is not bona fide."),
    lead=("Refusal letters vary by country, but a common thread in finance-related refusals is doubt: about whether the money is really yours, whether "
          "it was earned or received lawfully, or whether it was placed in the account only for the application. A revised wealth statement cannot "
          "argue with an embassy. What it can do is remove a genuine contradiction between the FBR record and the bank papers, so the next "
          "application tells one consistent story. This guide shows how to work through the refusal, line by line."),
    answers={
        "read": "List each financial reason in the letter and find the document it refers to: a balance, a deposit, a salary, a property.",
        "map": "For each reason, check what the wealth statement and return say about the same money on the same date.",
        "fix": "Correct only real errors under section 116(3), with documents. Leave true figures alone even if they are smaller than you would like.",
        "explain": "The officer may compare old and new papers. A short cover note naming each revision and its evidence answers that.",
    },
    svc=svc("Refusal Review and FBR Record Correction",
            "We read the financial reasons in your refusal, trace each one to your FBR record, and correct only what is genuinely wrong, with a note you can attach to your next application.",
            ["Line-by-line review of the refusal's financial reasons against your return and wealth statement",
             "Identification of genuine omissions or wrong statements and their evidence",
             "Revised wealth statement and reconciliation filed on IRIS with reasons",
             "Advice on a revised return where income is involved",
             "A one-page English note explaining each change for your cover letter"],
            ["Reapplying with the same contradictions repeats the doubt that caused the refusal",
             "An upward revision without evidence creates a tax problem the visa never needed",
             "Old and new papers that differ without explanation look worse than either alone"],
            "Refused once and planning to reapply?"),
    wa_text="Assalam o Alaikum, visa refuse hua hai funds ki wajah se. Wealth statement check aur correct karwana hai.",
    body=f"""
{SERIES("refused")}

<h2 id="read">Step 1: Read the Refusal for Its Financial Reasons</h2>
<p>Separate the reasons in the letter into two groups. Some concern your purpose and ties: your job, your family, your travel history. A wealth statement does not change those. Others concern money: the balance was too low for the stay, a large deposit was unexplained, income on paper did not match the account, or the officer could not see where savings came from. Those are the reasons the FBR record can help with.</p>
<p>The official guidance explains why the source matters. The UK guide asks for “bank statements which detail the origin of the funds held” and says a decision maker may ask for additional information. Canada asks for at least six months of account history. The Schengen rules ask for sufficient means for the length of the stay. Each is a test of believability, not only of amount.</p>

<h2 id="map">Step 2: Map Each Reason to the FBR Record</h2>
{table(["Refusal concern", "Check in the FBR record", "Possible genuine error"], [
    ["Balance not credible against salary", "Declared income in the return; accounts in the wealth statement", "A second income source or an account omitted"],
    ["Large unexplained deposit", "Reconciliation for that year", "A plot sale, a gift from a relative or a loan never recorded"],
    ["Funds placed shortly before applying", "Liabilities in the wealth statement", "A loan shown as savings, or not shown at all"],
    ["Sponsor's capacity doubted", "The sponsor's return and statement", "Sponsor's assets or income understated; see " + a(B["sponsor"], "sponsor parents")],
    ["Ownership of assets unclear", "Property and vehicle entries", "Asset in a dependent's name left out, or a sold asset still shown"],
])}
<p>If the FBR record already agrees with the bank papers, there may be nothing to revise. The fix then lies in better documents for the embassy, not in the wealth statement.</p>

<h2 id="fix">Step 3: Correct Only What Is Genuinely Wrong</h2>
<p>Section 116(3) of the Income Tax Ordinance 2001 allows a revised wealth statement when you discover “any omission or wrong statement”. It must be filed with a revised wealth reconciliation and the reasons, under intimation to the Commissioner, before you receive a notice under section 122(9) for that tax year, and never more than five years after the return due date for that year.</p>
<p>The proviso is the reason to be strict with yourself: the Commissioner may declare a revision void, after a hearing, if it “is not for the purpose of correcting a bona fide omission or wrong statement”. And section 111 adds to income the value of money, investments or valuable articles whose source is not adequately explained. A refusal is a strong temptation to show more. The law turns that into tax.</p>
<p>The most common genuine corrections after a refusal are covered in detail elsewhere in this series: {a(B["bank"], "omitted bank accounts")}, {a(B["gift"], "gifts from relatives")}, {a(B["prop"], "property sold or bought")} and {a(B["cash"], "guessed cash figures")}.</p>

<h2 id="others">Check the Other Statements in the Family</h2>
<p>A refusal sometimes turns on someone else's papers: a spouse whose assets were cited as ties, a parent named as sponsor, a brother who sent the money. Each has their own return and wealth statement, and each should tell the same story about the same money. A gift that appears in your reconciliation should also leave the giver's statement, under section 116(1)(c), as an asset transferred. Reviewing the whole family's records together, before reapplying, removes contradictions that no single revision can.</p>

<h2 id="explain">Step 4: Explain the Change</h2>
<p>An embassy that refused you may keep the papers from the first application. If the new wealth statement differs, the difference itself needs an explanation. A short cover note works best:</p>
<ul>
<li>the tax year revised and the date of the revised IRIS acknowledgement;</li>
<li>each line changed, the old and new figure and the document behind it;</li>
<li>a sentence on why it was wrong, for example “the savings account opened in March 2026 was omitted in error”.</li>
</ul>
<p>Keep the tone factual. The purpose is to show that the record was corrected because it was wrong, not because the first application failed.</p>

<h2 id="example">Example: A Deposit Without a Recorded Source</h2>
<p>Bilal, a Gujranwala shopkeeper, was refused a visit visa. The officer noted a Rs 1,800,000 credit two months before the application and a declared income too low to explain the balance. The credit was genuine: Bilal's mother had sold gold she inherited and transferred the money to him by bank. His wealth statement recorded neither the gift nor the higher balance.</p>
{table(["Line", "Filed", "Revised", "Evidence"], [
    ["Bank balance, 30 June", "Rs 350,000", "Rs 2,150,000", "Bank certificate"],
    ["Gift from mother (reconciliation)", "Not shown", "Rs 1,800,000", "Transfer record; mother is a relative under s.85(5)"],
])}
<p>Bilal revised before any notice, attached the transfer record and a short note to his new application, and his file now shows a lawful, recorded source for the money that worried the officer. Whether the visa is granted remains the embassy's decision; the FBR record no longer contradicts the bank.</p>

<h2 id="when-not">When Not to Revise</h2>
<ul>
<li>When the figures are already true. A smaller, consistent statement is better than a larger, revised one without evidence.</li>
<li>When you have received a section 122(9) notice for that year. Revision is no longer open; respond to the notice instead, with our {a(X["notice"], "notice defence service")}.</li>
<li>When the money was borrowed only for the application. Show the loan as a liability or do not rely on the balance.</li>
</ul>
""",
    faqs=[
        ("Should I revise my wealth statement after a visa refusal?",
         "Only if the refusal points to money that your FBR record shows wrongly or not at all. If your figures are already true, improve the evidence for the embassy instead."),
        ("Will the embassy notice that my wealth statement changed?",
         "It may, if it kept your earlier papers. Explain each change in a short cover note with the document behind it."),
        ("Can I show a higher bank balance after a refusal?",
         "Only a balance that is genuinely yours on the date shown. Money you cannot explain is taxed under section 111, and FBR can declare a non-bona fide revision void."),
        ("Is there a time limit on revising?",
         "Yes. Before a section 122(9) notice for that year, and within five years of that year's return due date."),
        ("Does revising guarantee a visa?",
         "No. A visa decision rests with the embassy. Revising removes contradictions in your FBR record; it cannot change ties, purpose or travel history."),
        ("What if my sponsor's papers caused the refusal?",
         "Then the sponsor's return and wealth statement are the ones to review and, if wrong, revise."),
    ],
    sources=[S_ITO, S_UKG, S_CA, S_CAR, S_SBC, S_IRIS],
    related=[(B["visa"], "Revision before any visa"), (B["gift"], "Gifts from relatives"), (X["notice"], "FBR notice defence"), (X["svc"], "Wealth statement service")],
)

# 6 ---------------------------------------------------------------- cash in hand
CASH = post(
    slug=SL["cash"],
    title="Cash in Hand Wrong in Your Wealth Statement? How to Revise",
    h1="Cash in Hand Wrong in Your Wealth Statement: Why the Balancing Figure Causes Trouble and How to Correct It",
    crumb="Cash in Hand Revision",
    description="Cash in hand often ends up as a balancing figure in a wealth statement. Why that draws FBR questions under s.111, and how to revise it under s.116(3).",
    keywords="cash in hand wealth statement, cash in hand fbr, wealth statement cash correction, revise cash in hand wealth statement, cash at home wealth statement pakistan",
    read="11 min read",
    banner="Cash in hand is the line FBR can least verify and most often questions. A guessed figure carried for years compounds the problem.",
    tldr=("Cash in hand is often typed into a wealth statement as whatever figure makes the reconciliation balance. That makes it the weakest line in "
          "the statement: there is no bank record behind it, it often grows every year, and section 111 adds to income any money whose source is not "
          "adequately explained. If your cash figure is wrong, too high or too low, revise it under section 116(3) to the real amount, with a revised "
          "reconciliation that corrects the real cause of the gap, usually understated expenses or an omitted account. File before any 122(9) "
          "notice and within five years. A large cash balance also does little for a visa file, which relies on bank statements."),
    lead=("Ask anyone who has filed their own wealth statement in IRIS how they made the reconciliation agree, and many will say: by adjusting cash. "
          "The form wants opening net assets, plus income and receipts, less expenses, to equal closing net assets. Cash at home is the one figure "
          "no bank can contradict, so it absorbs whatever does not fit. Over a few years the result is a statement that says the family keeps Rs "
          "2,000,000 or Rs 5,000,000 in a cupboard. This guide explains why that is risky and how to unwind it."),
    answers={
        "why": "Because cash has no third-party record, an inflated or growing cash figure is the easiest line for FBR to question and the hardest for you to prove.",
        "law": "Section 111(1)(b) covers a person who is the owner of any money; unexplained money is added to income from other sources.",
        "fix": "Restate cash to the real figure and correct the real cause of the original gap: expenses, an omitted account or an unrecorded receipt.",
        "visa": "Embassies rely on bank statements; the UK asks for bank statements that detail the origin of funds, not cash at home.",
    },
    svc=svc("Cash Figure Correction, With the Real Cause Fixed",
            "We rebuild your reconciliation from bank records and real expenses, so cash in hand is a true figure rather than a balancing entry.",
            ["Rebuild opening and closing net assets from bank certificates and asset papers",
             "Estimate household expenses realistically from your actual spending pattern",
             "Find omitted accounts, receipts or liabilities that the cash figure was hiding",
             "Revise the wealth statement and reconciliation with reasons",
             "Check earlier years where the same cash figure was carried forward"],
            ["A cash figure that grows every year with no bank trail invites a section 111 question",
             "Cutting cash without fixing the cause leaves the reconciliation out of balance",
             "Correcting only the latest year leaves the earlier statements contradicting it"],
            "Cash in hand figure that nobody can explain?"),
    wa_text="Assalam o Alaikum, wealth statement mein cash in hand ghalat hai. Revise karwana hai.",
    body=f"""
{SERIES("cash")}

<h2 id="why">How Cash Becomes a Balancing Figure</h2>
<p>Section 116(1) of the Income Tax Ordinance requires a wealth statement to give your assets and liabilities, those of your dependents, assets transferred and your total expenditure, and clause (e) adds the reconciliation statement of wealth. The reconciliation is simple arithmetic: what you owned at the start of the year, plus what you earned and received, less what you spent, should equal what you own at the end. When a filer underestimates household expenses, forgets an account or leaves out a receipt, the arithmetic fails. Increasing cash is the quickest way to make it pass.</p>
{table(["What was actually wrong", "What the filer did", "What the statement now claims"], [
    ["Expenses understated by Rs 600,000", "Added Rs 600,000 to cash", "Rs 600,000 more cash at home than exists"],
    ["A savings account omitted", "Put the balance into cash", "Money held at home that is really in a bank"],
    ["A gift from a parent not recorded", "Reduced cash to balance", "Less cash than exists, with no record of the gift"],
])}
<p>Each version is a wrong statement under section 116(3), whichever way the cash figure moved.</p>

<h2 id="law">Why FBR Questions Cash</h2>
<p>Section 111(1)(b) applies where a person “is the owner of any money or valuable article” and offers no explanation of its nature and source, or an explanation the Commissioner does not find satisfactory. The amount is then included in income under “Income from Other Sources” to the extent it is not adequately explained. A bank balance comes with a statement that shows where it came from. Cash at home comes with nothing but your word.</p>
<p>Two other provisions often meet cash in practice. Section 39(3) treats a loan, advance, deposit or gift from a non-bank person as income from other sources unless it arrives by crossed cheque, banking channel or digital means from a person holding an NTN, with an exception in section 39(4) for advance payments for the sale of goods or supply of services. So “a relative gave me cash” and “a friend lent me cash” are explanations the law already treats with suspicion. Our guide to {a(B["gift"], "gifts and loans")} explains which family transfers are safe.</p>

<h2 id="fix">How to Correct the Cash Figure</h2>
<ol>
<li><strong>Count the real cash.</strong> What was actually at home and in your wallet on 30 June of that year, as best you can establish it.</li>
<li><strong>Find the real cause of the gap.</strong> Rebuild expenses from known costs: rent, school fees, utility bills, fuel, household spending, travel. Check for {a(B["bank"], "omitted bank accounts")} and receipts.</li>
<li><strong>Revise both.</strong> Restate cash to the real figure and correct the item that caused the gap, so the reconciliation balances honestly.</li>
<li><strong>File under section 116(3).</strong> Revised statement, revised reconciliation and written reasons, before any section 122(9) notice for that year and within five years of its return due date.</li>
<li><strong>Look at earlier years.</strong> A cash figure carried from year to year means the opening position of each year may be wrong too; our guide to {a(X["five"], "revising five years")} explains the sequence.</li>
</ol>
<p>The Commissioner may declare a revision void if it does not correct a bona fide error. A cash correction backed by a rebuilt expense schedule and bank certificates is a bona fide correction; a cash figure moved again only to balance is not.</p>

<h2 id="example">Example: Five Years of Rising Cash</h2>
<p>Saima, a Lahore pharmacist, filed her own statements from TY2022. Her cash in hand rose each year: Rs 400,000, Rs 900,000, Rs 1,500,000, Rs 2,100,000 and Rs 2,700,000 by TY2026. In reality she kept about Rs 50,000 at home. The difference came from household expenses she had entered at Rs 300,000 a year, when rent, school fees and running the house came to about Rs 900,000.</p>
{table(["Tax year", "Cash filed", "Cash revised", "Expenses filed", "Expenses revised"], [
    ["TY2024", "Rs 1,500,000", "Rs 50,000", "Rs 300,000", "Rs 880,000"],
    ["TY2025", "Rs 2,100,000", "Rs 50,000", "Rs 300,000", "Rs 900,000"],
    ["TY2026", "Rs 2,700,000", "Rs 50,000", "Rs 300,000", "Rs 900,000"],
])}
<p>Revising downward removes Rs 2,650,000 of cash that never existed and replaces it with real expenditure that her income easily covered. Nothing is hidden; the record simply becomes true. Because each year's closing position is the next year's opening position, the earlier years are revised in order, not just the latest.</p>

<h2 id="visa">Cash and Visa Applications</h2>
<p>Some applicants keep a high cash figure in the belief that it shows wealth to an embassy. The official guidance points the other way. The UK guide asks for “bank statements which detail the origin of the funds held”, and Canada asks for six months of account details and balances. Cash at home appears in neither. A large cash figure in the wealth statement that does not appear in any bank account is more likely to raise a question than answer one. Our guide to {a(B["visa"], "revising before a visa")} explains what a consistent visa file looks like.</p>

<h2 id="business">Business Owners: Cash in the Business vs at Home</h2>
<p>For a sole proprietor, cash in the till belongs in the business capital and its accounts, while cash at home is a personal asset. Mixing the two is a common reason the personal cash figure looks inflated. Where the business has books, the business cash balance should come from them, and only genuinely personal cash goes on the personal line.</p>
""",
    faqs=[
        ("Is it a problem to show a lot of cash in hand?",
         "It is the line FBR can least verify. Under section 111 money whose source is not adequately explained is added to income, so a large cash figure without a source is a risk."),
        ("My cash figure is just a balancing entry. Can I reduce it?",
         "Yes, by revising under section 116(3) to the real figure and correcting the real cause of the original gap, usually understated expenses or an omitted account."),
        ("Do I need to revise earlier years too?",
         "If the wrong figure was carried forward, the opening positions of later years are also wrong, so the years are usually revised in order, within the five-year limit."),
        ("Can cash received from a relative be shown?",
         "A gift from a relative is excluded from income by section 39(1)(la), but section 39(3) treats gifts and loans not received through a bank or digital channel from an NTN holder as income. Bank transfers avoid the question."),
        ("Does cash at home help my visa application?",
         "Not much. The official guidance we checked relies on bank statements and their origin, not on cash at home."),
        ("When can I no longer revise?",
         "After a section 122(9) notice for that tax year, or five years after its return due date."),
    ],
    sources=[S_ITO, S_UKG, S_CA, S_IRIS],
    related=[(X["recon"], "Reconciliation not matching"), (X["five"], "Revising five years"), (B["bank"], "Bank balance corrections"), (X["svc"], "Wealth statement service")],
)

# 7 ---------------------------------------------------------------- gifts and loans
GIFT = post(
    slug=SL["gift"],
    title="Gifts and Loans From Family: Fixing Your Wealth Statement",
    h1="Gifts and Loans From Family Recorded Wrongly in Your Wealth Statement: The Rules and the Correction",
    crumb="Gift and Loan Revision",
    description="A parent's gift booked as income, or a loan from a friend left out? What ss.39(1)(la), 39(3) and 85(5) say, and how to revise your wealth statement correctly.",
    keywords="gift in wealth statement, gift from father wealth statement, loan from relative wealth statement, section 39(3) gift loan, revise wealth statement gift pakistan",
    read="11 min read",
    banner="The same Rs 1,000,000 can be tax-free, taxable income or a liability, depending on who gave it, how, and on what terms. Record it the right way.",
    tldr=("Section 39(1)(la) treats property or money received without consideration or as a gift as income from other sources, except a gift from a "
          "relative as defined in section 85(5): ancestors, descendants of grandparents, adopted children, and spouses, of you or your spouse. Section "
          "39(3) separately treats a loan, advance, deposit or gift from a non-bank person as income unless it arrives by crossed cheque, banking "
          "channel or digital means from a person holding an NTN. So a parent's bank transfer is a gift in the reconciliation, a loan is a liability, "
          "and neither is your income. If yours were recorded wrongly, revise under section 116(3) before any 122(9) notice and within five years."),
    lead=("Pakistani families move money between each other constantly: a father helps with a house, a brother abroad sends money, a cousin lends "
          "for a wedding. On a wealth statement each of these has one correct place. Put a parent's gift into income and you overstate what you "
          "earned. Leave a loan out and your assets look unexplained. Accept cash from a friend and section 39(3) may make it income. This guide "
          "sets out the rules from the Ordinance and the revision that fixes a wrong entry."),
    answers={
        "relative": "Section 85(5): ancestors, descendants of the grandparents, adopted children, of you or your spouse, and the spouses of all of them.",
        "gift": "A gift from a relative is excluded from section 39(1)(la). A gift from anyone else is income from other sources.",
        "channel": "Section 39(3): a non-bank loan, advance, deposit or gift not received by crossed cheque, banking channel or digital means from an NTN holder is income.",
        "fix": "Move the gift out of income into the reconciliation, add any loan as a liability, and file the revision with reasons.",
    },
    svc=svc("Family Money Recorded the Right Way",
            "We classify each family transfer as a gift, a loan or income under the Ordinance, and revise your statement and reconciliation so each sits in its proper place.",
            ["Review each transfer from family and friends in the year",
             "Check who gave it, how it arrived and on what terms",
             "Reclassify gifts from relatives, add loans as liabilities",
             "Revise the wealth statement, reconciliation and, if needed, the return",
             "Advise on recording future family transfers so they need no fixing"],
            ["A parent's gift shown as income can mean tax on money that was never taxable",
             "A loan left out makes your assets look unexplained under section 111",
             "Cash gifts and loans from non-relatives can be treated as income under section 39"],
            "Family money that your wealth statement shows wrongly?"),
    wa_text="Assalam o Alaikum, family se mila gift/loan wealth statement mein sahi show karwana hai.",
    body=f"""
{SERIES("gift")}

<h2 id="relative">Who Counts as a Relative</h2>
<p>Section 85(5)(i) of the Income Tax Ordinance 2001, as amended up to 30 June 2026, defines a relative of an individual as:</p>
<ul>
<li>(a) an ancestor, a descendant of any of the grandparents, or an adopted child, of the individual or of the individual's spouse; or</li>
<li>(b) a spouse of the individual or of any person in (a).</li>
</ul>
<p>In practice that covers parents and grandparents, children and grandchildren, brothers and sisters, uncles, aunts and cousins (all descendants of your grandparents), the same people on your spouse's side, and their spouses. A friend, a business partner or an employer is not a relative. Section 39(1)(la) was amended by the Finance Act 2021 to use this definition; it previously listed grandparents, parents, spouse, brother, sister, son or daughter.</p>

<h2 id="gift">When a Gift Is Income</h2>
<p>Section 39(1)(la) includes in “Income from Other Sources” any amount or fair market value of property received without consideration or as a gift, other than a gift from a relative as defined in section 85(5). So:</p>
{table(["Transfer", "Treatment under s.39(1)(la)", "Where it goes in your statement"], [
    ["Rs 1,500,000 from your father", "Not income: gift from a relative", "Reconciliation, as a gift received"],
    ["Rs 800,000 from your sister abroad", "Not income: gift from a relative", "Reconciliation, as a gift received"],
    ["Rs 500,000 from a family friend", "Income from other sources", "Income in the return, with tax"],
    ["A car from an employer for free", "Income at its fair market value", "Income, and the car as an asset"],
])}
<p>Our general guide to {a(X["gift"], "gift tax in Pakistan")} covers gifts of property and the donor's side. This guide is about correcting the recipient's wealth statement.</p>

<h2 id="channel">The Banking Channel Rule in Section 39(3)</h2>
<p>Section 39(3) applies to “any amount received as a loan, advance, deposit for issuance of shares or gift” from a person who is not a bank or financial institution. Unless it is received by a crossed cheque drawn on a bank, through a banking channel, or through digital means, from a person holding a National Tax Number, it is treated as income from other sources in the year received. Section 39(4) excludes advance payments for the sale of goods or supply of services.</p>
<p>Read together, the two provisions mean a gift from a relative is safest when it comes by bank transfer from a relative who holds an NTN, and that a loan from anyone should arrive through a bank and be recorded as a liability. Cash handed over at a family gathering is exactly what section 39(3) was written for.</p>

<h2 id="errors">Common Wrong Entries</h2>
{table(["What happened", "What was filed", "The correct entry"], [
    ["Father paid Rs 2,000,000 towards your flat", "Shown as your income", "Gift from a relative in the reconciliation; flat at full cost"],
    ["Brother lent Rs 1,000,000, to be repaid", "Not shown at all", "Liability of Rs 1,000,000 in the wealth statement"],
    ["Mother's gift recorded as a loan", "Liability that will never be repaid", "Gift in the reconciliation; liability removed"],
    ["Friend's Rs 300,000 in cash", "Not shown", "Disclosed; treated as income if s.39(3) applies"],
])}

<h2 id="giving">The Giver's Side of the Same Gift</h2>
<p>Every gift has two statements. Section 116(1)(c) asks the giver for “any assets including foreign assets transferred” to another person during the period and the consideration for the transfer. A father who transfers Rs 2,000,000 to his son should show it leaving his own statement, as a transfer with no consideration, in the same tax year in which the son records it as received. When only one side records the gift, the father's assets look higher than they are and the son's receipt has no matching source. If you are both giver and receiver in a family, revise both statements together.</p>

<h2 id="fix">Making the Correction</h2>
<p>Section 116(3) lets you revise a filed wealth statement on discovering an omission or wrong statement: a revised statement, a revised wealth reconciliation and the reasons, under intimation to the Commissioner, before receiving a section 122(9) notice for that year, and not after five years from its return due date. Where the correction changes income, for example a gift wrongly shown as income, the return is also revised under section 114(6), which has its own conditions; see our {a(X["rev"], "revised return guide")}.</p>
<p>Keep the evidence with the revision: bank transfer records, the relative's CNIC and NTN where available, and for a loan, a short written note of the terms and any repayments.</p>

<h2 id="example">Example: Help With a House</h2>
<p>Usman, a Karachi banker, bought a house in TY2026 for Rs 18,000,000. His father paid Rs 5,000,000 by bank transfer and his cousin lent Rs 2,000,000, repayable over three years. Usman's statement showed the house at Rs 11,000,000 (only his own contribution), no loan, and a balancing entry in cash.</p>
{table(["Line", "Filed", "Revised", "Reason"], [
    ["House", "Rs 11,000,000", "Rs 18,000,000", "Full cost per sale deed"],
    ["Loan from cousin", "Not shown", "Rs 2,000,000 liability", "Loan by bank transfer; written terms"],
    ["Gift from father", "Not shown", "Rs 5,000,000 in reconciliation", "Relative under s.85(5); bank transfer"],
])}
<p>The revision raises assets by Rs 7,000,000 and explains every rupee: Rs 5,000,000 gift and Rs 2,000,000 loan. The house is now in the statement at what it really cost, which matters again when it is sold; see our {a(B["prop"], "property revision guide")}.</p>

<h2 id="visa">Family Money in a Visa File</h2>
<p>A recent gift from a parent is one of the most common reasons a Pakistani applicant's balance jumps. Recorded as a gift from a relative, with the transfer behind it, it is an ordinary, explainable source. Unrecorded, it is the “large unexplained deposit” that worries officers. See {a(B["visa"], "revising before a visa")}.</p>
""",
    faqs=[
        ("Is a gift from my father taxable?",
         "No. Section 39(1)(la) excludes gifts from a relative as defined in section 85(5), which includes parents. Record it as a gift in the reconciliation, ideally received by bank transfer."),
        ("Is my cousin a relative for gift purposes?",
         "Yes. Section 85(5) includes descendants of your grandparents, which covers cousins, and the same relatives on your spouse's side."),
        ("Is a gift from a friend taxable?",
         "Yes. A gift from someone who is not a relative is income from other sources under section 39(1)(la)."),
        ("How should a loan from a relative be shown?",
         "As a liability in your wealth statement, received through a bank. Under section 39(3) a non-bank loan not received by crossed cheque, banking channel or digital means from an NTN holder is treated as income."),
        ("I showed a gift as income. Can I fix it?",
         "Yes. Revise the wealth statement under section 116(3) and the return under section 114(6), subject to their conditions."),
        ("What proof should I keep?",
         "The bank transfer record, the giver's CNIC and NTN where available, and for a loan, its written terms and repayments."),
    ],
    sources=[S_ITO, S_IRIS, S_FBR],
    related=[(X["gift"], "Gift tax in Pakistan"), (B["prop"], "Property revisions"), (X["rev"], "Revised return window"), (X["svc"], "Wealth statement service")],
)
