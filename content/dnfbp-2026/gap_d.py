"""Gap series posts 7-8: ineligible person under Section 114C; default surcharge under Section 205."""
from gap_common import *

INEL = dict(
    slug=SL["inel"],
    svc=dict(h2="Make Sure You Count as an Eligible Person", intro="Section 114C judges you on two things: a return for the previous tax year, and enough declared cash and liquid assets for the deal. We prepare both before you buy.",
             hook="Planning to buy a car, property or shares above the thresholds?", fee=FEE_RET + " Wealth statement Rs 2,000.", btn="Check my eligibility",
             items=["A check of last year's return and wealth statement against the purchase",
                    "Sufficient resources worked out at 130% of your declared cash-equivalent assets",
                    "Family resources (parents, spouse, dependent children) reviewed where the law allows",
                    "Sources of investment and expenditure statement, where it applies",
                    "Revision of the wealth statement before the deal, where an error exists"],
             risks=["An ineligible person's application is not accepted once the restriction is in force",
                    "Assets declared only after the purchase may raise Section 111 questions",
                    "A wealth statement that does not reconcile can be challenged"]),
    title="Ineligible Person Under Section 114C: Thresholds and Rules (2026)",
    h1="Ineligible Person Under Section 114C: Who Can Buy Cars, Property and Shares Above the Thresholds, and What 'Sufficient Resources' Means",
    crumb="Ineligible Person (114C)",
    description="Section 114C and the Fifteenth Schedule: limits on cars above Rs 7m, property above Rs 100m and investments above Rs 50m for ineligible persons, and when they apply.",
    keywords="114c income tax ordinance, ineligible person fbr, eligible person section 114c, fifteenth schedule income tax, sufficient resources 130 percent, non filer property purchase restriction, non filer car purchase ban",
    category="FBR Compliance", icon="🚫", read="12 min read",
    banner="Section 114C is law, but its restrictions start only from a date the Federal Government notifies. Get eligible before that happens.",
    tldr=("Section 114C of the Income Tax Ordinance 2001, with the Fifteenth Schedule (both inserted by the Finance Act 2025), stops an 'ineligible person' from "
          "booking, buying or registering a motor vehicle above Rs 7 million, registering or attesting transfer of immovable property above Rs 100 million fair "
          "market value, and holding securities or mutual fund investments above Rs 50 million. Separately, it sets an annual cash withdrawal limit of Rs 100 million "
          "across all bank accounts of an individual. An eligible person has filed a return for the tax year immediately before the transaction and has 'sufficient "
          "resources' (130% of declared cash and equivalent assets) for it, or has filed a sources of investment and expenditure statement. For an individual, "
          "eligibility includes immediate family members: parents, spouse and dependent children. Non-residents and public companies are outside the first three "
          "restrictions. Under Section 114C(5), the restrictions come into force only from a date the Federal Government notifies in the official Gazette."),
    lead=("Section 114C is the most talked-about change in the Finance Act 2025, and the most misunderstood. It is not a ban on non-filers buying anything; it is a "
          "test of whether your declared resources support a large purchase. Here is the full text, explained."),
    body=f"""
{SERIES("inel")}

<h2 id="status">Is Section 114C in Force?</h2>
<p>Section 114C(5) says all or any of the restrictions "shall come into force on such date as the Federal Government may, by notification in official Gazette, appoint", with any reductions or enhancements in the thresholds it considers appropriate. The section is part of the law, but the restrictions bite only from the notified date, and the notification may change the thresholds. Check whether a notification has been issued before relying on either position. The preparation below is worth doing either way, because it is the same work that keeps your wealth statement sound.</p>

<h2 id="thresholds">The Four Restrictions and Their Thresholds</h2>
{table(["Clause", "Transaction", "Value measured", "Threshold (Fifteenth Schedule)"], [
    ["114C(1)(a)", "Booking, purchase or registration of a motor vehicle", "Invoice value (local) or customs-assessed import value, including all taxes and duties", "Above Rs 7 million"],
    ["114C(1)(b)", "Registering, recording or attesting transfer of immovable property", "Fair market value under Section 2(22AA)", "Above Rs 100 million"],
    ["114C(1)(c)", "Investment in securities, debt securities, mutual fund units or money market instruments", "Acquisition cost; new investment in a financial year, excluding reinvestment", "Above Rs 50 million"],
    ["114C(1)(d)", "Cash withdrawal from bank accounts", "Annual total across all accounts of an individual", "Rs 100 million"],
])}
<p>Clauses (a) to (c) apply to ineligible persons. Clause (d) is worded differently: a bank shall not allow cash withdrawal from any account of <em>any person</em> above the threshold. Section 114C(2) excludes non-residents and public companies from the restrictions, except clause (d).</p>

<h2 id="eligible">Who Is an Eligible Person</h2>
<p>Section 114C(4)(a) defines an eligible person as one who has filed either:</p>
<ol>
<li>a return of income for the tax year immediately preceding the year of the transaction, and has sufficient resources in the wealth statement (individuals) or financial statements (companies and AOPs) for the transaction; or</li>
<li>a sources of investment and expenditure statement declaring sufficient resources and explaining them for that particular purchase or investment.</li>
</ol>
<p>For an individual, the proviso says the eligible person includes immediate family members, defined in Section 114C(4)(b) as parents, spouse and dependent children. An ineligible person is anyone who is not an eligible person.</p>

<h2 id="sufficient">What 'Sufficient Resources' Means: the 130% Rule</h2>
<p>Section 114C(4)(e) defines sufficient resources as 130% of the cash and equivalent assets declared in the sources of investment and expenditure statement or the latest wealth statement. Cash and equivalent assets include cash in local or foreign currency, the fair market value of gold, the net realisable value of stocks, bonds and receivables, and other cash-equivalent assets as prescribed. For a company or AOP, it is the cash and equivalent assets in the financial statements attached to the latest return.</p>
<p>The proviso adds that where the asset is bought by exchanging capital assets already declared, the disposal of those assets counts as cash equivalent to the extent of the value in the agreement.</p>
{table(["Declared cash and equivalents", "Sufficient resources (130%)", "Car at Rs 9 million?"], [
    ["Rs 5,000,000", "Rs 6,500,000", "Not enough on own resources"],
    ["Rs 7,000,000", "Rs 9,100,000", "Enough"],
    ["Rs 3,000,000 plus a declared plot sold for Rs 4,000,000 in exchange", "Rs 3,900,000 + Rs 4,000,000", "Check the exchange proviso"],
])}
<p>The examples show the arithmetic only; whether a particular exchange qualifies depends on the agreement and the declared asset.</p>

<h2 id="sie">The Sources of Investment and Expenditure Statement</h2>
<p>Section 114C(4)(d) describes it as a declaration filed on the Board's web portal specifying the sources of funds for the transaction. Section 114C(3) says this statement, and the sufficient resources in it, shall not be construed as the nature and source of income for the purposes of Section 111. In other words, it lets the transaction go ahead, but it does not by itself answer a later question about where the money came from.</p>

<h2 id="prepare">How to Prepare</h2>
<ol>
<li>File the return for the tax year before the purchase, on time, with a complete <a href="{X["ws"]}">wealth statement</a>.</li>
<li>Declare bank balances, gold and investments at the values the law uses.</li>
<li>Reconcile the wealth statement with income and expenses using the <a href="{X["wsr"]}">wealth reconciliation calculator</a>.</li>
<li>If something was left out, <a href="{X["rev"]}">revise before a notice</a>.</li>
<li>For a property deal, estimate the advance taxes with the <a href="{X["prop"]}">property transfer tax calculator</a>.</li>
</ol>

<h2 id="myths">Myths About Section 114C</h2>
<ul>
<li><strong>"Filers can buy anything."</strong> A return alone is not enough: 130% of your declared cash and equivalent assets must cover the transaction.</li>
<li><strong>"Non-filers cannot buy any car."</strong> Only cars above Rs 7 million are covered, and only once in force.</li>
<li><strong>"Overseas Pakistanis are blocked."</strong> Non-residents are outside clauses (a) to (c).</li>
<li><strong>"The cash cap is only for non-filers."</strong> Clause (d) applies to any person.</li>
</ul>
""",
    faqs=[
        ("What is Section 114C of the Income Tax Ordinance?", "A Finance Act 2025 provision restricting ineligible persons from vehicle purchases above Rs 7 million, property transfers above Rs 100 million and investments above Rs 50 million, plus an annual cash withdrawal cap of Rs 100 million for an individual."),
        ("Is Section 114C in force?", "Its restrictions apply from a date the Federal Government notifies in the official Gazette (Section 114C(5)). Check whether a notification has been issued."),
        ("Who is an eligible person under Section 114C?", "A person who filed a return for the preceding tax year with sufficient resources for the transaction, or filed a sources of investment and expenditure statement declaring sufficient resources."),
        ("What does sufficient resources mean?", "130% of cash and equivalent assets declared in the latest wealth statement or the sources of investment and expenditure statement."),
        ("Can my family's resources count?", "For an individual, the eligible person includes immediate family members: parents, spouse and dependent children."),
        ("Does Section 114C apply to overseas Pakistanis?", "Non-residents are excluded from the vehicle, property and investment restrictions, but not from the cash withdrawal cap."),
        ("Is there a cash withdrawal limit under Section 114C?", "Yes: Rs 100 million a year across all bank accounts of an individual, once notified. It applies to any person."),
        ("Does the sources of investment statement prove where the money came from?", "No. Section 114C(3) says it is not the nature and source of income for Section 111."),
    ],
    sources=[S_ITO, S_IRIS, S_FBR],
    related=[(X["ws"], "Wealth Statement Guide"), (X["wsr"], "Wealth Reconciliation Calculator"), (B["sim"], "Section 114B Enforcement")],
    cta_h="Be Eligible Before You Buy",
    cta_p="We file your return and wealth statement so your declared resources cover the purchase.",
    wa_text="Assalam o Alaikum, gaari/property khareedni hai. Section 114C eligibility check karni hai.",
)

DS = dict(
    slug=SL["ds"],
    svc=dict(h2="Stop the Surcharge Clock", intro="Default surcharge runs every day tax stays unpaid. We work out what is due, pay it correctly, and challenge surcharge on demands that should not stand.",
             hook="Notice showing default surcharge on top of tax?", fee=FEE_NOT, btn="Check my surcharge",
             items=["Calculation of the surcharge period and rate for each amount",
                    "Check of whether an exception (Section 129 proviso) applies",
                    "Refund of surcharge where the underlying tax is reduced (Section 205(2))",
                    "Payment challans prepared correctly in IRIS",
                    "Reply or appeal where the demand is wrong"],
             risks=["Surcharge keeps running until payment, not until the notice",
                    "Unpaid surcharge is assessed and recovered as if it were tax",
                    "Withholding agents also face personal liability under Section 161"]),
    title="Default Surcharge FBR Section 205: Rate and Calculation 2026",
    h1="Default Surcharge Under Section 205: The Rate, the Formula, and How to Calculate It (2026)",
    crumb="Default Surcharge (Section 205)",
    description="Section 205 default surcharge: the higher of 12% or KIBOR plus 3% a year on unpaid tax, 12% on advance tax and withholding defaults, with the formula and worked examples.",
    keywords="default surcharge fbr, default surcharge calculation, default surcharge formula, section 205 income tax ordinance, default surcharge rate 2026, default surcharge on late payment of tax, kibor plus 3 default surcharge",
    category="Tax Explainers", icon="⏱️", read="11 min read",
    banner="Default surcharge is interest on late tax. It runs per day, and it is calculated per amount.",
    tldr=("Section 205 of the Income Tax Ordinance 2001 (FBR text amended up to 30 June 2026) charges default surcharge on tax, penalties and amounts under "
          "Sections 140 and 141 not paid by the due date, at the higher of 12% or KIBOR plus 3% a year, from the due date to the date of payment (Section 205(1), "
          "rate set by the Finance Act 2024). Advance tax under Section 147 not paid carries 12% a year until paid or the return due date, whichever is earlier "
          "(Section 205(1A)); an underestimate below 90% carries 12% a year from 1 April (Section 205(1B)). A withholding agent who fails to collect, deduct or "
          "deposit tax pays 12% a year from the date it should have been collected or deducted (Section 205(3)). Surcharge is refunded to the extent the underlying "
          "amount is held not payable (Section 205(2)), and it is assessed and recovered as if it were tax. Formula: amount × rate × days ÷ 365."),
    lead=("Default surcharge is the interest FBR charges on money paid late. It is not a penalty, and it is not optional. People search for 'the default surcharge "
          "formula' because notices rarely show the working. Here it is, section by section, with examples you can check against your own notice."),
    body=f"""
{SERIES("ds")}

<h2 id="what">What Default Surcharge Is</h2>
<p>Part XII of Chapter X of the Ordinance is headed "Default Surcharge". Until 2010 it was called "additional tax"; the Finance Act 2010 renamed it. It compensates the Government for the time value of money paid late. It is separate from penalties under Section 182, so a late payer can owe both.</p>

<h2 id="rates">The Four Default Surcharge Rules</h2>
{table(["Sub-section", "What was unpaid", "Rate", "Period"], [
    ["205(1)", "Any tax (other than s.147 advance tax and the surcharge itself), any penalty, or amounts under s.140 or s.141", "Higher of 12% or KIBOR + 3% a year", "Due date to date of payment"],
    ["205(1A)", "Advance tax under s.147 not paid", "12% a year", "Due date to date paid or the return due date, whichever is earlier"],
    ["205(1B)", "Estimate under s.147(4A) or (6) not paid, or paid tax below 90% of the tax chargeable", "12% a year", "1 April to the assessment date or 30 June following, whichever is earlier"],
    ["205(3)", "Withholding or collection agent failing to collect, deduct or deposit tax", "12% a year", "Date tax should have been collected or deducted to date paid to the Commissioner"],
])}

<h2 id="due">When Is Tax 'Due'?</h2>
<p>Under Section 137(1), tax payable on taxable income for a tax year, including minimum tax under Section 113 and 113A, is due on the due date for filing the return for that year. For tax year 2026, that is 31 October 2026. Tax payable under an assessment or other order is due on the date in the notice under Section 137(2). Default surcharge under Section 205(1) is counted from these dates.</p>

<h2 id="formula">The Formula</h2>
<p><strong>Default surcharge = unpaid amount × annual rate × number of days late ÷ 365</strong></p>
<p>Count days from the due date to the date of payment. Calculate each unpaid amount separately if they fell due on different dates. Under Section 205(1), compare 12% with KIBOR plus 3% for the period and use the higher. We do not quote a KIBOR figure here because it changes; use the rate published for the relevant period.</p>

<h2 id="examples">Worked Examples (at 12%)</h2>
{table(["Situation", "Working", "Default surcharge"], [
    ["Rs 100,000 return tax paid 73 days late", "100,000 × 12% × 73 ÷ 365", "Rs 2,400"],
    ["Rs 500,000 assessed tax paid 180 days after the notice date", "500,000 × 12% × 180 ÷ 365", "Rs 29,589"],
    ["Rs 50,000 penalty paid 30 days late", "50,000 × 12% × 30 ÷ 365", "Rs 493"],
    ["Employer deposits Rs 200,000 withheld tax 45 days late", "200,000 × 12% × 45 ÷ 365", "Rs 2,959"],
])}
<p>If KIBOR plus 3% exceeds 12% for a Section 205(1) amount, recompute with the higher rate. Sections 205(1A), (1B) and (3) use a flat 12%.</p>

<h2 id="advance">Advance Tax Instalments</h2>
<p>Under Section 147, certain taxpayers pay advance tax in quarterly instalments. Missing an instalment triggers Section 205(1A), but only until the instalment is paid or the return falls due, whichever comes first; after that, any tax still unpaid falls due with the return under Section 137(1). Underestimating the year's tax to pay less than 90% triggers Section 205(1B). Our <a href="{X["adv"]}">advance tax instalment calculator</a> helps you plan the instalments.</p>

<h2 id="withholding">Withholding Agents and Section 161</h2>
<p>Employers, banks and businesses that must deduct or collect tax carry two separate exposures. Under Section 161, a person who fails to collect or deduct tax, or collects it and fails to pay it, is personally liable to pay the tax. Under Section 205(3), default surcharge at 12% a year runs from the date the tax should have been collected or deducted until it is paid to the Commissioner. The proviso to Section 205(3) relieves surcharge for the period after a Section 161 order if the person pays by the date in the Section 137(2) notice and does not appeal.</p>

<h2 id="relief">Exceptions and Refunds</h2>
<ul>
<li><strong>Appeal effect relief:</strong> under the proviso to Section 205(1), a person who pays tax due under an order of the Commissioner (Appeals) under Section 129 by the date in the Section 137(2) notice, and does not appeal further under Section 131, does not pay surcharge for the period from the due date under the order appealed against to that payment.</li>
<li><strong>Refund:</strong> Section 205(2) refunds surcharge to the extent the tax, penalty or other amount is held not payable.</li>
<li><strong>Revised returns:</strong> voluntary revision before an audit or Section 122(9) notice avoids penalties under Section 114(6A), but tax and default surcharge must still be paid. See <a href="{X["rev"]}">revising before a notice</a>.</li>
</ul>

<h2 id="assess">How FBR Recovers It</h2>
<p>Section 205(5) says the Commissioner assesses default surcharge as if it were tax, and Section 205(6) applies the appeal and recovery provisions to it in the same way. An unpaid surcharge demand can therefore be recovered by the same means as unpaid tax, and it can be appealed in the same way.</p>

<h2 id="tips">Practical Tips</h2>
<ul>
<li>Pay the tax first; surcharge stops the day you pay.</li>
<li>Keep the payment challan (CPR) dates; they decide the number of days.</li>
<li>Check that a notice uses the right sub-section; advance tax defaults are capped at the return due date.</li>
<li>If the underlying tax is reduced on appeal, claim the surcharge back under Section 205(2).</li>
</ul>
""",
    faqs=[
        ("What is the default surcharge rate in Pakistan in 2026?", "Under Section 205(1), the higher of 12% or KIBOR plus 3% a year on unpaid tax, penalties and Section 140/141 amounts. Advance tax and withholding defaults carry 12% a year."),
        ("How is default surcharge calculated?", "Unpaid amount × annual rate × days late ÷ 365, counted from the due date to the date of payment."),
        ("Is default surcharge a penalty?", "No. It is a separate charge for late payment. A late payer can owe both a Section 182 penalty and default surcharge."),
        ("Does default surcharge apply to advance tax?", "Yes, at 12% a year under Section 205(1A), until paid or the return due date, whichever is earlier."),
        ("What is the default surcharge for withholding agents?", "12% a year under Section 205(3), from the date the tax should have been collected or deducted to the date paid to the Commissioner."),
        ("Can default surcharge be refunded?", "Yes, to the extent the underlying tax, penalty or amount is held not payable (Section 205(2))."),
        ("What was default surcharge called earlier?", "Additional tax. The Finance Act 2010 renamed it default surcharge."),
        ("Can I appeal against default surcharge?", "Yes. Section 205(6) applies the appeal provisions to a default surcharge assessment as if it were tax."),
    ],
    sources=[S_ITO, S_IRIS, S_FBR],
    related=[(X["adv"], "Advance Tax Instalment Calculator"), (X["pen"], "Late Filing Penalty Calculator"), (X["notice"], "FBR Notice Defence")],
    cta_h="Surcharge on Your Notice? Let Us Check It",
    cta_p="We recalculate the surcharge, pay what is due and challenge what is not.",
    wa_text="Assalam o Alaikum, FBR notice mein default surcharge aya hai. Check karwana hai.",
)
