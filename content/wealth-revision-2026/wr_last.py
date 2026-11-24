"""Wealth statement revision series, posts 8-10: property, foreign assets, bank balances (facts checked 24 November 2026)."""
from wr_common import *

# 8 ---------------------------------------------------------------- property
PROP = post(
    slug=SL["prop"],
    title="Property Sold or Bought? Revising Your Wealth Statement",
    h1="Property Sold, Bought or Recorded at the Wrong Value: Revising Your Wealth Statement the Right Way (2026)",
    crumb="Property Wealth Statement Revision",
    description="Plot sold but still in your wealth statement, or bought at a lower declared value? Section 116(3) revision, s.111 risk, FBR value vs price, 236C and 236K.",
    keywords="property in wealth statement, plot sold wealth statement, revise wealth statement property, property value wealth statement pakistan, house purchase wealth statement correction",
    read="12 min read",
    banner="Property is the largest number in most wealth statements. When it is wrong, every other line has to bend to make the reconciliation agree.",
    tldr=("Property is often the line most out of date in a wealth statement: a plot sold years ago still listed, a house bought but missing, or a "
          "purchase recorded at the lower FBR value instead of the price actually paid. Section 116(1)(c) asks for assets transferred and the "
          "consideration received, and section 111 taxes an investment whose source is not adequately explained, so understating what you paid "
          "leaves the difference unexplained. Advance tax is a separate matter: 236K on the buyer is charged on FBR's fair market value under "
          "section 68, 236C on the seller on the sale price. Revise under section 116(3), with a revised reconciliation and reasons, before any "
          "122(9) notice and within five years."),
    lead=("Ask a Pakistani family to list what they own and property comes first. Ask them to match that list with their wealth statement and the "
          "gaps appear: the plot in Bahria Town sold in 2023 is still there, the inherited share in the village house is not, the new flat is at the "
          "DC rate rather than its real price. Each gap forces another figure, often cash or expenses, to absorb the difference. This guide shows "
          "how to correct property entries, what value to use, and what changes in the return at the same time."),
    answers={
        "value": "Record a purchase at what you actually paid, supported by the deed and payment trail; the FBR value is used for advance tax, not as your cost.",
        "sold": "Remove a sold property, record the sale consideration under section 116(1)(c) and the proceeds where they went, and report any gain in the return.",
        "tax": "236K on the buyer: 1.25% of FMV on the ATL. 236C on the seller: 2.75% of the sale price on the ATL; higher rates apply off the ATL.",
        "fix": "Section 116(3): revised statement, revised reconciliation and reasons, before a 122(9) notice and within five years of the return due date.",
    },
    svc=svc("Property Entries Corrected and Reconciled",
            "We list every property you and your dependents own or have sold, compare it with your filed statements year by year, and revise each one with its documents.",
            ["Year-by-year property schedule from deeds, allotment letters and payment records",
             "Correct cost on purchase and sale consideration on disposal",
             "Revised wealth statement and reconciliation with reasons",
             "Capital gain worked out and the return revised where needed",
             "Check of 236K and 236C deductions claimed against the documents"],
            ["Recording a purchase below the price paid leaves the difference unexplained under section 111",
             "A sold plot still on the statement hides where the sale money went",
             "Correcting only the latest year leaves earlier statements contradicting the deed dates"],
            "Property entries that no longer match your deeds?"),
    wa_text="Assalam o Alaikum, wealth statement mein property ki entry ghalat hai (sale/purchase). Revise karwani hai.",
    body=f"""
{SERIES("prop")}

<h2 id="value">Which Value Goes in the Wealth Statement</h2>
<p>Pakistani property has more than one value. FBR notifies values under section 68 of the Income Tax Ordinance for each area; in Lahore, for example, through S.R.O. 1722(I)/2024. Provincial authorities have their own valuation tables for stamp duty. And there is the price you actually paid. These numbers often differ widely.</p>
<p>The wealth statement exists to show what you own and to let the reconciliation explain how you paid for it. Section 111 is the reason the actual price matters: where a person “has made any investment” and does not adequately explain the source, the unexplained value is added to income. If you paid Rs 25,000,000 for a house and record Rs 14,000,000 because that is the FBR value, Rs 11,000,000 of real payment has no place in your statement. The money that paid it then sits unexplained elsewhere, or does not appear at all.</p>
{table(["Value", "What it is for", "Use it in the wealth statement?"], [
    ["Price actually paid, plus costs such as transfer fees", "Your investment in the asset", "Yes, supported by the deed and payment trail"],
    ["FBR value under section 68", "Advance tax such as 236K, and as a minimum for some purposes", "Not as a substitute for the price you paid"],
    ["Provincial valuation table", "Stamp duty and registration", "No"],
])}

<h2 id="sold">A Property You Have Sold</h2>
<p>Section 116(1)(c) asks for “any assets including foreign assets transferred by the person to any other person” during the period “and the consideration for the transfer”. So a sale is recorded in three places:</p>
<ol>
<li>the property is removed from closing assets in the year of sale;</li>
<li>the sale consideration is disclosed, and the proceeds appear where they went, a bank account, a new purchase or a loan repaid;</li>
<li>any capital gain is reported in the return for that year.</li>
</ol>
<p>Leaving a sold property on the statement for years is common. It overstates your assets, and it hides where the sale money went, which becomes a problem when that money later appears in a bank account or a new purchase.</p>

<h2 id="tax">Advance Tax and Gains: The Rates in Force</h2>
{table(["Tax", "On whom and on what", "Rate on the ATL", "Rate off the ATL"], [
    ["236K", "Buyer, on fair market value", "1.25%", "10.5% up to Rs 50m, 14.5% up to Rs 100m, 18.5% above"],
    ["236C", "Seller, on the sale price", "2.75%", "11.5%"],
    ["Capital gain, bought from 1 July 2024", "Seller, on the gain", "15%", "Slab rates, minimum 15%"],
    ["Capital gain, bought up to 30 June 2024", "Seller, by holding period", "Plot 0% after 6 years; constructed property after 4; flat after 2", "As per the Ordinance"],
])}
<p>Rates are those in the Income Tax Ordinance as amended up to 30 June 2026 (Division VIII and the Tenth Schedule). The advance tax actually collected appears on the registration papers, and the same figures should agree with what you claim in the return.</p>

<h2 id="fix">How the Revision Is Made</h2>
<p>Section 116(3) allows a revised wealth statement on discovering an omission or wrong statement: filed with a revised wealth reconciliation and written reasons, under intimation to the Commissioner, before a notice under section 122(9) for that year, and not later than five years from the return due date for that year. The Commissioner may declare a revision void if it does not correct a bona fide error. Deeds, allotment letters and bank payment records are what make a property revision bona fide.</p>
<p>Property revisions usually run across several years, because a sale or purchase in one year changes the opening position of every later one. Our guide to {a(X["five"], "revising five years")} explains the order. Where a gain or other income was not reported, the return is revised as well under section 114(6). Inherited property follows its own rules; see our {a(X["inherit"], "inherited property guide")}.</p>

<h2 id="example">Example: A Plot Sold and a House Bought</h2>
<p>Rehan, an Islamabad engineer, sold a plot bought in 2016 for Rs 3,000,000. He sold it in September 2025 for Rs 12,000,000 and bought a house in January 2026 for Rs 30,000,000, recorded on the deed at the FBR value of Rs 19,000,000. His TY2026 statement still lists the plot and shows the house at Rs 19,000,000.</p>
{table(["Line", "Filed", "Revised", "Reason"], [
    ["Plot, bought 2016", "Rs 3,000,000", "Removed", "Sold September 2025 for Rs 12,000,000, per sale deed"],
    ["House, bought January 2026", "Rs 19,000,000", "Rs 30,000,000", "Price paid per payment trail; FBR value used only for 236K"],
    ["Reconciliation", "Balanced through cash", "Sale proceeds Rs 12,000,000 and savings shown as the source", "Cash figure restated to actual"],
])}
<p>The plot was held for more than six years and bought before 1 July 2024, so under the holding-period table its gain is taxed at 0%; it is still reported in the return. The house now sits at its real cost, which also protects Rehan when he sells it: a cost recorded at Rs 19,000,000 would make his future gain look Rs 11,000,000 larger.</p>

<h2 id="dependents">Property in a Spouse's or Child's Name</h2>
<p>Section 116(1)(b) requires the assets of your spouse, minor children and other dependents. Since the Finance Act 2024, the Explanation limits a spouse's assets to cases where the spouse is dependent. A plot in a working wife's name belongs in her own statement; one in a minor son's name belongs in the parent's. If it was gifted, see our guide to {a(B["gift"], "gifts and loans in the family")}.</p>
""",
    faqs=[
        ("Should I show property at the FBR value or the price I paid?",
         "At what you actually paid, supported by the deed and payment trail. The FBR value under section 68 is used for advance tax such as 236K. Recording less than you paid leaves the difference unexplained under section 111."),
        ("I sold a plot years ago and it is still in my wealth statement. What now?",
         "Revise each affected year under section 116(3), within five years: remove the plot in the year of sale, disclose the consideration, show where the proceeds went, and report any gain in the return."),
        ("What advance tax applies when I buy property?",
         "Section 236K on the buyer: 1.25% of fair market value on the ATL; off the ATL 10.5% up to Rs 50m, 14.5% up to Rs 100m and 18.5% above."),
        ("What advance tax applies when I sell?",
         "Section 236C on the seller: 2.75% of the sale price on the ATL and 11.5% off it."),
        ("Is the gain on a plot held for many years taxable?",
         "For a plot bought up to 30 June 2024, the rate falls to 0% after six years of holding. For property bought from 1 July 2024, the gain is taxed at 15% for ATL filers."),
        ("Does a property in my wife's name go in my statement?",
         "Only if she is a dependent spouse; that is the Explanation to section 116(1)(b) added in 2024. Otherwise it belongs in her own wealth statement."),
    ],
    sources=[S_ITO, ("FBR: S.R.O. 1722(I)/2024, property values in Lahore under section 68", "https://download1.fbr.gov.pk/SROs/20241030Lahore1722.pdf"), S_IRIS],
    related=[(X["inherit"], "Inherited property in the return"), (X["five"], "Revising five years"), (B["gift"], "Gifts and loans"), (X["svc"], "Wealth statement service")],
)

# 9 ---------------------------------------------------------------- foreign assets
FOREIGN = post(
    slug=SL["foreign"],
    title="Foreign Assets Missing From Your Wealth Statement: Fix It",
    h1="Foreign Assets Left Out of Your Wealth Statement: Section 116, the 116A Statement and the Revision",
    crumb="Foreign Assets Revision",
    description="Foreign bank account or flat missing from your wealth statement? What ss.116(1), 116A and 111(2) say, the 2% penalty, and how to revise before FBR finds it.",
    keywords="foreign assets wealth statement, section 116a foreign income and assets statement, foreign bank account fbr, revise wealth statement foreign assets, overseas assets declaration pakistan",
    read="12 min read",
    banner="Foreign assets carry their own statement, their own penalty and their own timing rule. Disclosing them first is far cheaper than being found.",
    tldr=("Since the Finance Act 2024, section 116(1) expressly includes foreign assets and foreign liabilities in a wealth statement. A resident "
          "individual with foreign income of at least USD 10,000 or foreign assets worth at least USD 100,000 must also file a foreign income and "
          "assets statement under section 116A; the penalty for not doing so is 2% of the foreign income or of the value of the foreign assets for "
          "each year of default, and failing to comply with a 116A(2) notice is an offence under section 195A. Under section 111(2) unexplained "
          "foreign assets are taxed in the year before FBR discovers them. A resident who left a foreign account or property out can revise under "
          "section 116(3) before any 122(9) notice and within five years."),
    lead=("Many Pakistani families now hold something abroad: a savings account opened while working in the Gulf, a flat in Dubai bought with "
          "remittances, shares bought through a foreign broker, money kept abroad for a child's studies. A resident taxpayer is expected to show all "
          "of it. The common mistake is to treat the wealth statement as a Pakistan-only list. This guide sets out the rules for foreign assets in "
          "the Ordinance and the revision that brings a statement into line."),
    answers={
        "who": "Residents. Section 116(2) applies to resident individuals filing a return, and section 116A to resident individuals above its thresholds.",
        "116a": "Foreign income of USD 10,000 or more, or foreign assets of USD 100,000 or more, requires a separate foreign income and assets statement.",
        "penalty": "Section 182, row 1AAA: 2% of the foreign income or value of foreign assets for each year of default. Section 195A makes ignoring a 116A(2) notice an offence.",
        "timing": "Section 111(2)(ii): unexplained foreign assets are taxed in the tax year immediately before the year FBR discovers them.",
        "fix": "Revise the wealth statement under section 116(3) with a reconciliation explaining how the asset was funded, and file any 116A statement due.",
    },
    svc=svc("Foreign Assets Disclosed and Reconciled",
            "We list your foreign accounts, property and investments, check whether section 116A applies, and revise your wealth statements with a reconciliation that explains how each was funded.",
            ["Schedule of foreign accounts, property and investments with values in rupees",
             "Section 116A threshold check for each year",
             "Revised wealth statement and reconciliation, with reasons",
             "Foreign income and assets statement where due",
             "Residence check under section 82 if you have lived abroad"],
            ["Leaving foreign assets out risks the 2% per year penalty under row 1AAA",
             "Assets FBR discovers are taxed under section 111(2) in the year before discovery",
             "A non-resident who files as resident, or the reverse, starts from the wrong rules"],
            "Money or property abroad that FBR has never been told about?"),
    btn="Get my foreign assets disclosed",
    wa_text="Assalam o Alaikum, foreign account/property wealth statement mein show nahi hui. Revise karwana hai.",
    body=f"""
{SERIES("foreign")}

<h2 id="who">Resident or Non-Resident: Start Here</h2>
<p>The wealth statement and the foreign assets statement are obligations of residents. Section 116(2) requires “every resident taxpayer being an individual filing a return of income” to furnish a wealth statement and reconciliation; section 116A applies to “every resident taxpayer being an individual” above its thresholds. Under section 82, an individual is resident if in Pakistan for 183 days or more in the tax year, or, for a citizen, if not present in any other country for more than 182 days in the year or not a resident taxpayer of another country. If you have lived abroad, establish your status for each year first; it decides which rules apply.</p>

<h2 id="116">What Section 116 Requires</h2>
<p>The Finance Act 2024 rewrote section 116(1) to refer to “assets including foreign assets and liabilities including foreign liabilities”, for you and for your spouse, minor children and other dependents, and added “including foreign assets” to the assets you transferred. A foreign savings account, a property abroad, foreign shares or a loan from a foreign bank all belong in the wealth statement of a resident, converted into rupees.</p>

<h2 id="116a">The Separate Foreign Income and Assets Statement</h2>
<p>Section 116A, inserted by the Finance Act 2018, applies to a resident individual “having foreign income of not less than ten thousand United States dollars or having foreign assets with a value of not less than one hundred thousand United States dollars”. The statement gives:</p>
{table(["Clause", "Particulars"], [
    ["116A(1)(a)", "Total foreign assets and liabilities as on the last day of the tax year"],
    ["116A(1)(b)", "Foreign assets transferred to any other person during the year, and the consideration"],
    ["116A(1)(c)", "Complete particulars of foreign income and the expenditure incurred to earn it"],
])}
<p>Under section 116A(2), the Commissioner may serve a notice on a person he believes should have filed the statement but did not.</p>

<h2 id="penalty">Penalties and Timing</h2>
{table(["Provision", "What it says"], [
    ["Section 182, row 1AAA", "Failure to furnish the foreign assets and income statement by the due date: penalty of 2% of the foreign income or value of the foreign assets for each year of default"],
    ["Section 182, row 1AA", "Failure to furnish a wealth statement or wealth reconciliation statement: higher of 0.1% of taxable income per week or Rs 100,000"],
    ["Section 195A", "Non-compliance with a notice under section 116A(2) is an offence punishable on conviction"],
    ["Section 111(2)(ii)", "Unexplained investment, money or valuable article situated outside Pakistan is taxed in the tax year immediately preceding the year of discovery"],
])}
<p>The Explanation to section 111(2) adds a protection: where a foreign asset acquired in an earlier year is discovered and you explain its acquisition from sources of the year it was acquired, that explanation is not to be rejected on the ground that the source does not relate to the year in which the amount is charged. Keeping records of how the asset was funded, years of salary abroad, remittances, a sale, is what makes that protection work.</p>

<h2 id="fix">How to Revise</h2>
<ol>
<li><strong>List and value.</strong> Every foreign account, property and investment, with the value on 30 June of each year and the rupee conversion you use.</li>
<li><strong>Trace the funding.</strong> For each asset, the source: foreign salary taxed abroad, remittances, a sale in Pakistan, a gift from a relative. See {a(B["gift"], "gifts and loans")}.</li>
<li><strong>Revise under section 116(3).</strong> Revised wealth statement, revised reconciliation and written reasons, under intimation to the Commissioner, before any 122(9) notice for that year and within five years of its return due date.</li>
<li><strong>File section 116A where due.</strong> If a year's foreign income or assets cross the thresholds, the separate statement is needed too.</li>
<li><strong>Revise income if needed.</strong> Foreign income taxable for a resident and left out of the return calls for a revised return under section 114(6).</li>
</ol>

<h2 id="example">Example: A Dubai Account and Flat</h2>
<p>Kamran worked in Dubai until 2022 and has been resident in Lahore since. He holds a Dubai savings account of AED 90,000 and a studio flat bought in 2021 for AED 600,000, rented out. None of it is in his TY2025 or TY2026 statements.</p>
{table(["Item", "Filed", "Revised", "Notes"], [
    ["Dubai savings account", "Not shown", "Rupee value on 30 June each year", "Bank statement as evidence"],
    ["Dubai studio flat", "Not shown", "Cost converted at purchase", "Funded from salary earned while non-resident"],
    ["Foreign rental income", "Not shown", "Reported in the return", "Taxable for a resident; return revised"],
    ["Section 116A", "Not filed", "Filed for each year above the threshold", "The flat's value is above USD 100,000"],
])}
<p>Because the flat was bought from salary earned while Kamran was non-resident, the reconciliation explains it. Disclosing it himself, before any notice, avoids a later section 111(2) assessment and limits his exposure to the penalty rows that apply to the missed statements.</p>

<h2 id="visa">Foreign Assets and Visa Files</h2>
<p>A foreign account sometimes surfaces in a visa application before FBR ever hears of it, for example a statement from a Gulf bank shown to a UK or Schengen consulate. If the Pakistani wealth statement attached to the same file does not include it, the two documents contradict each other. Our guide to {a(B["visa"], "revising before a visa")} explains how to make the file consistent.</p>
""",
    faqs=[
        ("Do I need to show my foreign bank account in my wealth statement?",
         "Yes, if you are a resident. Section 116(1), as amended in 2024, expressly includes foreign assets and foreign liabilities."),
        ("When is the section 116A statement required?",
         "For a resident individual with foreign income of at least USD 10,000 or foreign assets worth at least USD 100,000."),
        ("What is the penalty for not filing the 116A statement?",
         "Section 182 row 1AAA: 2% of the foreign income or value of the foreign assets for each year of default. Not complying with a 116A(2) notice is an offence under section 195A."),
        ("In which year is an undisclosed foreign asset taxed?",
         "Under section 111(2)(ii), in the tax year immediately before the year FBR discovers it, unless its source is adequately explained."),
        ("I bought the asset while living abroad. Is that a defence?",
         "It is the explanation the law expects. The Explanation to section 111(2) says an explanation from sources of the acquisition year is not rejected only because it relates to an earlier year. Keep the records."),
        ("Do non-residents file a wealth statement?",
         "Section 116(2) and section 116A apply to residents. Check your residence under section 82 for each year first."),
    ],
    sources=[S_ITO, S_IRIS, S_FBR],
    related=[(X["missing"], "Assets missing from a statement"), (B["gift"], "Gifts and loans"), (X["five"], "Revising five years"), (X["svc"], "Wealth statement service")],
)

# 10 --------------------------------------------------------------- bank balances
BANK = post(
    slug=SL["bank"],
    title="Bank Balance Wrong in Your Wealth Statement? How to Revise",
    h1="Bank Balances That Do Not Match Your Wealth Statement: Omitted Accounts, Wrong Dates and the Fix",
    crumb="Bank Balance Revision",
    description="Bank balance in your wealth statement differs from the bank certificate, or an account is missing? Why it happens, what s.116 requires and how to revise.",
    keywords="bank balance wealth statement, bank account missing wealth statement, wealth statement bank certificate, revise bank balance fbr, wealth statement bank mismatch pakistan",
    read="11 min read",
    banner="FBR can see bank data. A balance your statement does not show is the easiest mismatch for anyone, FBR or an embassy, to spot.",
    tldr=("A wealth statement should show the balance of every account you and your dependents hold, in Pakistan and abroad, on the last day of the "
          "tax year, 30 June. Mismatches come from accounts forgotten or opened mid-year, balances taken on the wrong date, joint accounts entered in "
          "full or not at all, and profit credited after the balance was copied. Each is a wrong statement under section 116(3) and can be revised "
          "with a revised reconciliation and reasons, before any section 122(9) notice and within five years of the return due date. Use the bank's "
          "certificate of balance as on 30 June; it is the document that settles the figure."),
    lead=("Bank balances look like the simplest line in a wealth statement, and they cause a surprising share of the corrections we make. Filers copy a "
          "balance from a mobile app on the day they file, forget the account their employer opened for them, leave out a savings certificate "
          "account, or enter a joint account twice. Because banks report to FBR and embassies read bank statements, a wrong balance is the mismatch "
          "most likely to be noticed. This guide covers the common causes and the revision."),
    answers={
        "date": "The balance on 30 June, the last day of the tax year, taken from a bank certificate, not the balance on the day you file.",
        "which": "Every account of yours and of dependents under section 116(1)(b), including foreign-currency and foreign accounts.",
        "joint": "Show the part that is genuinely yours and explain the rest; entering a joint account in full in two statements double-counts it.",
        "fix": "Section 116(3): revised statement, revised reconciliation and reasons, before a 122(9) notice and within five years.",
    },
    svc=svc("Every Account, at the Right Date",
            "We collect bank certificates for every account you and your dependents hold, compare them with your filed statements, and revise where a balance or account is wrong.",
            ["List of every account, including dormant, foreign-currency and investment accounts",
             "Bank certificates of balance as on 30 June for each year needed",
             "Revised wealth statement and reconciliation with reasons",
             "Profit on bank deposits checked against the tax deducted",
             "Matching note for your visa file if you are applying abroad"],
            ["A missing account is the mismatch FBR's data and an embassy's bank review both reveal",
             "A balance on the wrong date makes the reconciliation wrong for two years at once",
             "Fixing the balance without fixing the reconciliation leaves the statement unbalanced"],
            "Bank balance or account your statement does not match?"),
    wa_text="Assalam o Alaikum, wealth statement mein bank balance/account ghalat hai. Revise karwana hai.",
    body=f"""
{SERIES("bank")}

<h2 id="date">The Right Date: 30 June</h2>
<p>The wealth statement filed with a return under section 116(2) describes your position at the end of the tax year, which in Pakistan runs from 1 July to 30 June. Section 116A uses the same anchor for foreign assets, “as on the last day of the tax year”. The figure for each account is therefore its balance on 30 June. Banks issue a certificate of balance for a stated date on request, and that certificate is the cleanest evidence.</p>
<p>The most common error is using the balance on the day of filing, which may be months later. That one mistake makes two years wrong: the closing balance of one year and the opening balance of the next.</p>

<h2 id="which">Which Accounts Belong in the Statement</h2>
{table(["Account", "In the statement?", "Note"], [
    ["Salary and current accounts", "Yes", "Including accounts opened by an employer"],
    ["Savings and term deposit accounts", "Yes", "Including deposits that matured after 30 June"],
    ["Foreign-currency accounts in Pakistan", "Yes", "Converted to rupees at 30 June"],
    ["Accounts abroad", "Yes, for a resident", "Section 116(1) includes foreign assets; see " + a(B["foreign"], "foreign assets")],
    ["A dependent's account", "Yes, under 116(1)(b)", "Minor children; a spouse only if dependent"],
    ["Business account of a sole proprietor", "Yes, within business capital", "Not entered again as a personal account"],
    ["Dormant accounts", "Yes", "A small balance still counts"],
])}

<h2 id="causes">Why Balances Go Wrong</h2>
<ol>
<li><strong>Wrong date.</strong> Balance taken on the filing day, not on 30 June.</li>
<li><strong>Forgotten account.</strong> A second bank, a digital bank account, or an account opened in the middle of the year.</li>
<li><strong>Joint account entered twice.</strong> Husband and wife both enter the full balance, or neither does.</li>
<li><strong>Profit missing.</strong> Profit credited on 30 June itself left out, which also means the income in the return is incomplete.</li>
<li><strong>Business and personal mixed.</strong> A proprietor's business account entered as a personal account and again inside capital.</li>
</ol>
<p>Profit on bank deposits is taxed at source at 20% for persons on the Active Taxpayers List and 40% for others, so a missing account often also means profit and tax deducted that the return does not show.</p>

<h2 id="liabilities">Bank Loans, Financing and Closed Accounts</h2>
<p>The bank side of a wealth statement has liabilities too. Section 116(1)(a) covers your “total assets including foreign assets and liabilities including foreign liabilities”, so the amount outstanding on 30 June on a car financing facility, a house finance, a personal loan or a running finance line belongs in the statement, from the bank's statement of outstanding balance for that date. Leaving a loan out makes the asset it paid for look unexplained: a car worth Rs 6,000,000 bought with Rs 4,500,000 of bank financing needs that liability recorded, or the reconciliation must find Rs 4,500,000 from somewhere else.</p>
<p>Credit cards are a smaller case of the same rule: an unpaid card balance on 30 June is a liability, although the UK guide notes that credit card statements are not evidence of funds for a visa.</p>
<p>Accounts closed during the year still matter. An account open on 30 June of the previous year was in last year's closing assets; if it was closed in March, its balance moved somewhere, to another account, a purchase or spending, and the reconciliation should show where. A closed account that simply disappears from one year to the next is a gap.</p>
{table(["Bank item on 30 June", "Where it goes", "Evidence"], [
    ["Car or house financing outstanding", "Liability", "Bank statement of outstanding principal"],
    ["Running finance used", "Liability", "Facility statement"],
    ["Unpaid credit card balance", "Liability", "Card statement"],
    ["Account closed during the year", "Not in closing assets; movement explained in the reconciliation", "Closing letter or final statement"],
])}

<h2 id="fix">Revising the Statement</h2>
<p>Section 116(3) allows a revised wealth statement when you discover any omission or wrong statement. File it with the revised wealth reconciliation and the reasons, under intimation to the Commissioner, before receiving a notice under section 122(9) for that tax year, and within five years of the return due date. Because a balance at 30 June is both a closing and an opening figure, check the next year too.</p>
<p>A higher balance must be explained in the reconciliation: income, a gift from a relative, a sale. A lower one may reveal that an earlier balancing entry, usually {a(B["cash"], "cash in hand")}, was covering the gap. Our guide to {a(X["recon"], "a reconciliation that will not match")} helps when the figures still do not agree.</p>

<h2 id="example">Example: Three Accounts, One Entered</h2>
<p>Nadia, a Multan doctor, entered one account in her TY2026 statement: Rs 820,000 in her salary account, the balance on the day she filed in October. On 30 June 2026 she actually held:</p>
{table(["Account", "Filed", "Balance on 30 June 2026 (certificate)"], [
    ["Salary account", "Rs 820,000", "Rs 610,000"],
    ["Savings account, second bank", "Not shown", "Rs 1,940,000"],
    ["Dollar account", "Not shown", "USD 4,000, converted at 30 June"],
])}
<p>Her revision uses the certificates, adds the two missing accounts, and corrects the reconciliation: the savings account was built from salary over three years, so the opening balances of TY2025 and TY2026 also need checking. The profit on the savings account, and the tax deducted on it, go into the return.</p>

<h2 id="visa">Bank Balances and Visa Files</h2>
<p>An embassy sees your bank statements directly. The UK guide asks for bank statements that “detail the origin of the funds held” and says statements issued more than a year before the application should not be used; Canada asks for six months of account details. An account on your bank statement that is missing from your FBR wealth statement is a contradiction in your own file. Our guide to {a(B["visa"], "revising before a visa")} covers the whole file.</p>
""",
    faqs=[
        ("Which date's bank balance goes in the wealth statement?",
         "The balance on 30 June, the last day of the tax year, ideally from a bank certificate of balance for that date."),
        ("Do I need to show a dormant account?",
         "Yes. Every account is an asset, whatever its balance."),
        ("How do I show a joint account?",
         "Show the part that is genuinely yours and explain the rest. Entering the full balance in two people's statements counts it twice."),
        ("Is my foreign-currency account part of the statement?",
         "Yes, converted to rupees at 30 June. An account abroad is also included for a resident; it may trigger section 116A."),
        ("I left out an account. Is it too late?",
         "You can revise under section 116(3) until you receive a 122(9) notice for that year, and within five years of its return due date."),
        ("What tax applies to profit on my bank account?",
         "Profit on bank deposits is taxed at source at 20% for ATL filers and 40% for others."),
    ],
    sources=[S_ITO, S_UKG, S_CA, S_IRIS],
    related=[(X["recon"], "Reconciliation not matching"), (B["cash"], "Cash in hand corrections"), (B["foreign"], "Foreign assets"), (X["svc"], "Wealth statement service")],
)
