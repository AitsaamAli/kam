"""Gap series posts 1-2: adjustable vs final tax; zakat deduction."""
from gap_common import *

ADJ = dict(
    slug=SL["adj"],
    svc=dict(h2="Get Every Rupee of Adjustable Tax Credited", intro="Most people lose money not to tax rates but to tax they already paid and never claimed. We collect every certificate, separate adjustable from final tax, and make sure each credit lands in your return.",
             hook="Paid tax at the bank, on bills or on property and not sure it counted?", fee=FEE_RET, btn="Check my tax credits",
             items=["A list of every withholding and advance tax you paid in the year, from IRIS and your certificates",
                    "Each item classified: adjustable credit, final tax, or separately taxed block",
                    "Credits claimed in the return so you pay only the balance, or claim a refund",
                    "Wealth statement reconciled with the income those taxes relate to",
                    "A note of the documents to keep for each credit"],
             risks=["Unclaimed adjustable tax is simply lost money",
                    "Claiming final tax as a credit invites a correction and a demand",
                    "Mixing final-tax income into normal income can push you into a higher band"]),
    title="Adjustable vs Final Tax in Pakistan: The Difference Explained",
    h1="Adjustable Tax vs Final Tax vs Minimum Tax in Pakistan: What Each Means for Your Return (2026)",
    crumb="Adjustable vs Final Tax",
    description="Adjustable tax is a credit against your yearly tax; final tax settles that income for good. Sections 168 and 169 explained with examples and how to claim.",
    keywords="adjustable tax vs final tax, difference between adjustable tax and final tax, adjustable tax fbr, adjustable taxes in pakistan, final tax regime pakistan, minimum tax and final tax, section 168 section 169",
    category="Tax Explainers", icon="⚖️", read="12 min read",
    banner="Every withholding tax in Pakistan is one of two kinds. Knowing which one decides whether you get it back.",
    tldr=("Under Section 168 of the Income Tax Ordinance 2001 (FBR text amended up to 30 June 2026), tax deducted or collected from you is treated as tax you paid "
          "and is allowed as a credit against the tax due on your taxable income for that year: this is adjustable tax. Section 169 sets out the cases where tax "
          "deducted is a final tax on the income it relates to, for example prize bond winnings under Section 156(3) and the Section 154A export deduction. "
          "Final-tax income is not added to your other income, no expense or deductible allowance can reduce it, and the tax cannot be refunded or set against other "
          "tax. Minimum tax sits between the two: it is the least you will pay on that income even if your normal calculation is lower."),
    lead=("'Adjustable' and 'final' are the two words that decide what happens to the tax a bank, employer, registrar or utility company takes from you. Mix them up "
          "and you either lose money you were owed or claim a credit FBR will reverse. This guide explains both from the law, with the everyday examples that matter."),
    body=f"""
{SERIES("adj")}

<h2 id="adjustable">What Adjustable Tax Means</h2>
<p>Section 168(1) says two things about any tax collected or deducted from you under the withholding provisions: the amount deducted is treated as income you received, and the amount is treated as tax you paid. Section 168(2) then allows you a tax credit for it in computing the tax due on your taxable income for the year in which it was collected or deducted.</p>
<p>In plain terms, adjustable tax is an advance payment. When you file, your total tax for the year is worked out first, and every adjustable deduction is subtracted from it. If the deductions are more than the tax, the difference is refundable, subject to the refund rules and to being on the Active Taxpayers List (Section 182A(1)(c) blocks refunds while you are off it).</p>
{table(["Common adjustable taxes", "Section", "Where you meet it"], [
    ["Tax on salary", "149", "Deducted by the employer every month"],
    ["Advance tax on selling property", "236C", "Collected by the registrar or society at transfer"],
    ["Advance tax on buying property", "236K", "Collected from the buyer at transfer"],
    ["Advance tax on cash withdrawal (off the ATL)", "231AB", "Deducted by the bank above Rs 50,000 a day"],
    ["Advance tax on vehicle registration", "231B", "Collected by the Excise department"],
    ["Quarterly advance tax", "147", "Paid by you during the year"],
])}

<h2 id="final">What Final Tax Means</h2>
<p>Section 169 applies where the tax required to be deducted is a final tax under the provisions it lists. These include sub-section (3) of Section 156 (prizes and winnings), sub-section (2) of Section 154A (export proceeds), Section 152A and Section 156A, among others. Where Section 169 applies, sub-section (2) sets four consequences:</p>
<ol>
<li>The income is not chargeable to tax under any head in computing your taxable income.</li>
<li>No deduction is allowed for any expenditure incurred in earning it.</li>
<li>The income is not reduced by any deductible allowance, such as zakat, or by setting off a loss.</li>
<li>The tax deducted is not reduced by any tax credit.</li>
</ol>
<p>The result is that final-tax income lives in its own box. It does not push your other income into a higher band, but the tax on it is also never refunded, whatever your circumstances.</p>

<h2 id="separate">Separately Taxed Income: The Middle Ground</h2>
<p>Some income is neither fully adjustable nor a Section 169 final tax, but is taxed separately from your other income. The best-known example is profit on debt. Section 7B taxes an individual's profit on debt up to Rs 5 million separately, at the rate in Division IIIA of the First Schedule (20% for bank deposits, 15% in other cases such as National Savings). Because the rate matches what the bank deducts, the deduction is usually the whole tax, but the profit is still reported in the return and the deduction is credited against that Section 7B tax.</p>

<h2 id="minimum">Minimum Tax: A Floor, Not a Ceiling</h2>
<p>Minimum tax means the tax on a particular receipt cannot fall below a set amount, even if your normal calculation would give less. Section 113, for example, sets a minimum tax on turnover for certain persons; our guide to <a href="{X["min"]}">minimum tax under Section 113</a> covers it. The practical point for most individuals is simple: a minimum-tax deduction is not refunded even if your income turns out lower, but it may still count towards your total if your normal tax is higher.</p>

<h2 id="table">The Three Side by Side</h2>
{table(["", "Adjustable", "Final (Section 169)", "Minimum"], [
    ["Added to your other income?", "Yes", "No", "Depends on the provision"],
    ["Expenses deductible against it?", "Yes, where the head allows", "No", "Depends"],
    ["Zakat or other allowances reduce it?", "Yes", "No", "Depends"],
    ["Refund if over-deducted?", "Yes, through the return", "No", "No, below the minimum"],
    ["Example", "Salary tax, property advance tax", "Prize bond winnings", "Turnover tax under Section 113"],
])}

<h2 id="examples">Five Everyday Examples</h2>
<ul>
<li><strong>Salary:</strong> your employer deducts tax monthly under Section 149. It is adjustable: if a credit was missed through payroll, the return corrects it.</li>
<li><strong>Bank profit:</strong> deducted under Section 151 and taxed separately under Section 7B up to Rs 5 million. File so the deduction stays at 20%; off the ATL it is 40%. See the <a href="{X["bank"]}">bank profit tax calculator</a>.</li>
<li><strong>Selling a plot:</strong> the 2.75% (on the ATL) collected under Section 236C is adjustable against the tax on your gain.</li>
<li><strong>Prize bond prize:</strong> 15% under Section 156, final under Section 169. Nothing to adjust; declare it so your wealth statement reconciles.</li>
<li><strong>Freelance export proceeds:</strong> the bank deducts under Section 154A (0.25% for PSEB-registered IT exporters, 1% otherwise), which Section 169 lists as final tax under sub-section (2) of Section 154A.</li>
</ul>

<h2 id="claim">How to Claim Adjustable Tax</h2>
<ol>
<li>Collect certificates: salary, bank, utility, vehicle, property transfer and any other withholding.</li>
<li>Compare them with the tax shown in IRIS for your CNIC; most banks and payers report directly.</li>
<li>Enter each adjustable amount against the right section in the return.</li>
<li>Keep final-tax income in its own place in the return; do not mix it into taxable income.</li>
<li>Pay any balance by PSID, or claim the refund once you are on the ATL.</li>
</ol>

<h2 id="mistakes">Mistakes That Cost Money</h2>
<ul>
<li>Forgetting the property advance tax from a sale when computing the tax on the gain.</li>
<li>Adding prize bond winnings to salary and paying slab tax on money already taxed finally.</li>
<li>Assuming a non-filer's higher deductions are refundable while still off the ATL.</li>
<li>Not filing at all, so adjustable credits are never claimed.</li>
</ul>
""",
    faqs=[
        ("What is the difference between adjustable tax and final tax?", "Adjustable tax (Section 168) is credited against your tax for the year and can be refunded if it exceeds that tax. Final tax (Section 169) settles the income on its own: it is not added to other income, not reduced by deductions or credits, and not refunded."),
        ("Is tax on salary adjustable or final?", "Adjustable. The tax your employer deducts under Section 149 is credited against your total tax in the return."),
        ("Is prize bond tax final?", "Yes. Tax deducted under Section 156(3) is a final tax under Section 169."),
        ("Is bank profit tax final?", "For individuals, Section 7B taxes profit on debt up to Rs 5 million separately at the Division IIIA rate, so the 20% deduction is usually the whole tax; it is reported and credited in the return."),
        ("Can I get adjustable tax back?", "Yes, if it exceeds your tax for the year, through the return and a refund claim. Refunds are not issued while you are off the ATL."),
        ("Does zakat reduce final-tax income?", "No. Section 169(2)(c) says final-tax income is not reduced by any deductible allowance, including zakat."),
        ("Is advance tax on property adjustable?", "Yes. Tax collected under Sections 236C and 236K is credited against your tax for the year."),
        ("What is minimum tax?", "A floor: the tax on that income or turnover cannot be less than the set amount, and it is not refunded below it."),
    ],
    sources=[S_ITO, S_IRIS, S_FBR],
    related=[(X["min"], "Minimum Tax Section 113"), (X["bank"], "Bank Profit Tax Calculator"), (B["zak"], "Zakat Deduction")],
    cta_h="Don't Leave Tax Credits Unclaimed",
    cta_p="We separate adjustable and final tax and claim every credit in your return.",
    wa_text="Assalam o Alaikum, mera adjustable tax credit sahi claim karwana hai.",
)

ZAK = dict(
    slug=SL["zak"],
    svc=dict(h2="Zakat and Every Allowance Claimed Correctly", intro="Zakat reduces your taxable income only if it is claimed properly and supported. We check the zakat you paid, claim it under Section 60, and make sure it does not collide with final-tax income.",
             hook="Paid zakat this year and want it counted in your tax?", fee=FEE_RET, btn="Claim my zakat deduction",
             items=["Zakat paid in the tax year identified from bank and other certificates",
                    "Section 60 allowance claimed against the right income",
                    "Check that it is not claimed against final-tax income",
                    "Charitable donations checked separately for the Section 61 credit",
                    "Return and wealth statement filed with the supporting documents listed"],
             risks=["An allowance that exceeds your income is lost; it cannot be carried forward",
                    "Claiming zakat without a certificate invites the claim being disallowed",
                    "Confusing zakat (an allowance) with donations (a credit) under-claims one or both"]),
    title="Zakat Deduction in Income Tax: Section 60 Explained (2026)",
    h1="Zakat Deduction in Pakistan's Income Tax: How Section 60 Reduces Your Taxable Income (2026)",
    crumb="Zakat Deduction (Section 60)",
    description="Zakat paid under the Zakat and Ushr Ordinance reduces taxable income under Section 60. Who can claim, limits, final-tax income and the documents FBR expects.",
    keywords="zakat deduction income tax, zakat deduction for tax, zakat income tax deduction pakistan, section 60 zakat, zakat deductible allowance fbr, zakat certificate for tax return",
    category="Tax Explainers", icon="🕌", read="11 min read",
    banner="Zakat you have paid is not just an obligation met; under the tax law it also reduces the income you are taxed on.",
    tldr=("Section 60 of the Income Tax Ordinance 2001 (FBR text amended up to 30 June 2026) entitles a person to a deductible allowance for any zakat paid in the "
          "tax year under the Zakat and Ushr Ordinance, 1980. A deductible allowance reduces taxable income, so the saving equals the zakat multiplied by your "
          "marginal tax rate. It does not apply to zakat already taken into account under Section 40(2), it cannot reduce income taxed under the final tax regime "
          "(Section 169), and any part that cannot be used in the year is lost: it is not refunded, carried forward or carried back (Section 60(3)). Keep the "
          "certificate of zakat deducted or paid."),
    lead=("Every Ramadan banks deduct zakat from eligible savings accounts, and many people also pay zakat directly. Few claim it in their tax return, and those who "
          "do sometimes claim it in the wrong place. Here is exactly what the law allows, and how much it is worth."),
    body=f"""
{SERIES("zak")}

<h2 id="law">What Section 60 Says</h2>
<p>Section 60(1): a person is entitled to a deductible allowance for the amount of any zakat paid by the person in a tax year under the Zakat and Ushr Ordinance, 1980. Section 60(2): this does not apply to zakat taken into account under Section 40(2). Section 60(3): any allowance, or part of an allowance, that cannot be deducted under Section 9 for the year is not refunded, carried forward to a later year or carried back to an earlier one.</p>
<p>Three points follow. The zakat must be paid in the tax year (1 July to 30 June). It must be zakat under the Zakat and Ushr Ordinance. And the allowance is use-it-or-lose-it.</p>

<h2 id="allowance">An Allowance, Not a Credit</h2>
<p>A deductible allowance is subtracted from your total income to arrive at taxable income (Section 9). It is different from a tax credit, which is subtracted from the tax itself. The difference matters for how much you save:</p>
{table(["", "Zakat (Section 60)", "Charitable donation (Section 61)"], [
    ["Type", "Deductible allowance", "Tax credit"],
    ["Reduces", "Taxable income", "Tax payable"],
    ["Saving", "Zakat × your marginal rate", "Worked out by the Section 61 formula"],
    ["Guide", "This page", f"<a href=\"{X['don']}\">Charitable donations</a>"],
])}
<p>Example: if your income falls in a band taxed at 11% at the margin, Rs 100,000 of zakat reduces your taxable income by Rs 100,000 and your tax by about Rs 11,000. In a 25% band, the same zakat saves about Rs 25,000.</p>

<h2 id="final-tax">The Final-Tax Trap</h2>
<p>Section 169(2)(c)(i) says income taxed under the final tax regime is not reduced by any deductible allowance under Part IX of Chapter III, which is where Section 60 sits. So zakat cannot be claimed against, for example, prize bond winnings or export proceeds taxed finally under Section 154A. If most of your income is final-tax income, much of the zakat allowance may simply have nothing to reduce, and Section 60(3) means the unused part is lost.</p>

<h2 id="who">Who Benefits Most</h2>
<ul>
<li>Salaried people whose tax is deducted at normal slab rates: zakat lowers taxable income and can produce a refund of salary tax already deducted.</li>
<li>Business individuals and sole proprietors taxed at normal rates.</li>
<li>Landlords and others with income taxed at normal rates.</li>
</ul>
<p>It helps least where income is mainly taxed separately or finally, such as profit on debt under Section 7B or export proceeds under Section 154A.</p>

<h2 id="bank-zakat">Zakat Deducted by Your Bank</h2>
<p>Banks deduct zakat from eligible accounts under the Zakat and Ushr Ordinance and issue a certificate of the amount. That certificate is the simplest evidence for your claim. If you pay zakat directly, keep a receipt or record that shows it was paid under the Zakat law; payments that do not meet that description are better treated as donations and checked under Section 61.</p>

<h2 id="claim">How to Claim It in IRIS</h2>
<ol>
<li>Get the zakat certificate from each bank, and receipts for any other zakat paid in the tax year.</li>
<li>In the return, enter the amount under the zakat deductible allowance.</li>
<li>Check that the income it reduces is normal taxable income, not final-tax income.</li>
<li>Show the zakat as an outflow in your wealth reconciliation, so the statement balances.</li>
</ol>
<p>Our <a href="{X["wsr"]}">wealth reconciliation calculator</a> helps check the last step.</p>

<h2 id="example">Worked Example</h2>
<p>A salaried teacher has taxable salary of Rs 1.8 million. Her bank deducted Rs 40,000 zakat in Ramadan, and she paid Rs 60,000 directly under the Zakat law with receipts. Total zakat: Rs 100,000. Her taxable income becomes Rs 1.7 million. If her marginal rate is 11%, her tax falls by about Rs 11,000, and because her employer deducted tax on the full salary, the difference becomes a refund once she files and is on the ATL.</p>

<h2 id="mistakes">Common Mistakes</h2>
<ul>
<li>Claiming zakat paid outside the tax year.</li>
<li>Claiming it against final-tax income.</li>
<li>Treating general charity as zakat; it may qualify as a donation instead.</li>
<li>Not keeping the bank certificate or receipts.</li>
</ul>
""",
    faqs=[
        ("Is zakat deductible from income tax in Pakistan?", "Yes. Section 60 gives a deductible allowance for zakat paid in the tax year under the Zakat and Ushr Ordinance, 1980."),
        ("Does zakat reduce tax or taxable income?", "Taxable income. It is a deductible allowance, so the saving equals the zakat times your marginal rate."),
        ("Can unused zakat be carried forward?", "No. Section 60(3) says any part that cannot be deducted is not refunded, carried forward or carried back."),
        ("Can zakat reduce final-tax income?", "No. Section 169(2)(c) bars deductible allowances against final-tax income."),
        ("What document do I need?", "The bank's zakat deduction certificate, or receipts showing zakat paid under the Zakat law."),
        ("Is zakat the same as a charitable donation for tax?", "No. Zakat is an allowance under Section 60; donations may give a tax credit under Section 61."),
        ("Can a salaried person get a refund from zakat?", "Yes, if salary tax was deducted on the full salary, the lower taxable income can produce a refund after filing, once you are on the ATL."),
        ("Which tax year does bank zakat belong to?", "The tax year in which it was deducted; Ramadan deductions fall in the July-June year in which they occur."),
    ],
    sources=[S_ITO, S_IRIS, S_FBR],
    related=[(X["don"], "Charitable Donation Tax Credit"), (B["adj"], "Adjustable vs Final Tax"), (X["wsr"], "Wealth Reconciliation Calculator")],
    cta_h="Claim the Zakat You Already Paid",
    cta_p="We include zakat and every other allowance correctly in your return.",
    wa_text="Assalam o Alaikum, maine zakat di hai, income tax return mein claim karni hai.",
)
