"""Sales tax, SME, partnership, minimum tax, property, CVT, professional tax, penalty and 7E pages."""

PAGES = {}

PAGES["blogs/sales-tax-return-filing-pakistan.html"] = {
    "replace": [("typically 18%, or 16%/13%/15% provincial for services)", "18% standard federal rate on goods; services are taxed by the provinces at their own rates)"),
                ("Rs. 10,000 or 0.1% of tax payable per day, whichever is higher (capped)",
                 "Penalty under section 33 with a minimum amount, rising if the default continues")],
    "body": """## Why Your Input Tax Can Be Disallowed

Most sales tax disputes start with input tax, not output tax. FBR's system compares the purchases you claim with the sales your suppliers declare in their own Annex-C. If a supplier files late, files a nil return or is not on the Sales Tax Active Taxpayers List, your claim on that invoice can be rejected even though you paid the tax.

| Reason input tax is refused | How to prevent it |
| Supplier did not declare the sale | Check the purchase annex before filing and follow up with the supplier |
| Payment above Rs 50,000 made in cash | Pay through banking channels, as required by section 73 |
| Item on the inadmissible list | Do not claim tax on blocked items such as certain vehicles and entertainment |
| Supplier blacklisted or suspended | Verify supplier status on FBR's online check before buying |

## The 90% Rule

Section 8B generally limits how much input tax a registered person can adjust in a month to a percentage of output tax, so most businesses pay at least some tax each month even when purchases are high. Unadjusted input tax is carried forward. Certain sectors and taxpayers are excluded, so check whether the limit applies to you before planning cash flow around full adjustment.

## Further Tax on Sales to Unregistered Buyers

When you sell to a buyer who is not registered for sales tax, further tax is charged on top of the normal rate in many cases. The buyer's registration status therefore changes your invoice. Collect your customers' NTN or STRN when opening their account, and keep the list updated.

## Our Monthly Routine for Clients

1. Collect sales invoices and purchase records by the 5th.
2. Reconcile suppliers' declared sales with your purchase annex.
3. Submit Annex-C by the 10th and the payment by the 15th.
4. File the return by the 18th and send the client a summary.

Monthly sales tax return filing is Rs 3,000 per month on our [pricing page](/pricing).""",
    "faq": [
        ("Why was my input tax claim rejected?",
         "Usually because the supplier did not declare the sale, is not on the Sales Tax Active Taxpayers List, or the payment was made in cash above the limit in section 73."),
        ("Can I adjust all my input tax every month?",
         "Not always. Section 8B generally caps monthly adjustment at a percentage of output tax; the balance is carried forward."),
    ],
}

PAGES["blogs/sme-tax-consultant-pakistan.html"] = {
    "replace": [('<div class="value">From Rs 7,000</div><div class="sub">Sole proprietor</div>', '<div class="value">From Rs 5,000</div><div class="sub">Sole proprietor</div>'),
                ('<div class="value">From Rs 2,000</div><div class="sub">Per month</div>', '<div class="value">From Rs 2,500</div><div class="sub">Per month</div>')],
    "faq_skip": ["What is the penalty for not filing monthly WHT in Pakistan?"],
    "body": """## Advance Tax: The Cash-Flow Item SMEs Forget

Growing businesses often pay their whole year's income tax in September and then struggle. Section 147 requires quarterly advance tax from businesses and individuals whose income crosses the threshold, based on the previous year's tax. The instalments fall due on 25 September, 25 December, 25 March and 15 June. Paying on time avoids default surcharge and spreads the cost across the year.

## When an SME Becomes a Withholding Agent

Once your business crosses certain turnover levels or becomes a company or AOP, you must deduct tax when you pay others, including salaries, rent, contractors and suppliers. You then deposit the tax and file withholding statements. Missing this is costly because FBR can disallow the expense and recover the tax you should have deducted.

| Payment | Withholding responsibility |
| Staff salaries above the taxable threshold | Deduct monthly under section 149 |
| Shop or office rent to a landlord | Deduct under section 155 if you are a prescribed person |
| Suppliers and contractors | Deduct under section 153 if you are a prescribed person |

## Structure Decisions at the SME Stage

Many SMEs start as sole proprietorships, later add a partner and then incorporate. Each change affects tax: an AOP files its own return, and a private limited company pays corporate tax and must keep audited accounts. Planning the move at a year end keeps records clean.

## What Our SME Package Covers

Monthly withholding statements (Rs 2,500 per month), monthly sales tax returns (Rs 3,000 per month), EOBI registration (Rs 8,000) and the annual return, as listed on our [pricing page](/pricing).""",
    "faq": [
        ("When is quarterly advance tax due?",
         "Under section 147, instalments are due on 25 September, 25 December, 25 March and 15 June for taxpayers whose income crosses the threshold."),
        ("Does an SME have to deduct tax from rent and supplier payments?",
         "If the business is a prescribed person under the law, it must deduct tax on these payments and file withholding statements."),
    ],
}

PAGES["blogs/partnership-firm-tax-pakistan.html"] = {
    "body": """## What Your Partnership Deed Should Cover

A written deed protects both the partners and the firm's tax position. At minimum it should state:

- names, CNICs and capital contribution of each partner;
- the profit and loss sharing ratio;
- whether partners draw a monthly amount and how it is treated;
- the bank account and who signs cheques;
- what happens when a partner retires, dies or a new partner joins.

Registering the deed with the provincial Registrar of Firms is optional for tax but helps when opening bank accounts, signing government contracts and enforcing the deed in court.

## Partner Salaries and Interest

Payments to partners, such as salary, interest on capital or commission, are generally not allowed as expenses of the AOP. They are treated as part of each partner's share of profit. Firms that deduct these payments in their accounts must add them back in the tax computation, otherwise the return understates profit.

## The Partner's Share in a Personal Return

A partner's share of the AOP's after-tax profit is exempt in the partner's own return, but it can still be taken into account when working out the rate on the partner's other income. A partner with salary or rent as well as a profit share therefore needs both figures in the personal return.

## Changes in Partnership

When a partner leaves or joins, the firm should update its deed, its FBR profile and its bank mandate. If the change is large enough to create a new firm, a new NTN may be needed. Profits up to the date of change should be settled under the old ratio.

## Fees

AOP return filing starts at Rs 8,000 on our [pricing page](/pricing), and individual partner returns can be filed alongside.""",
    "faq": [
        ("Can an AOP deduct salary paid to partners?",
         "Generally no. Salary, interest and commission paid to partners are treated as part of their profit share, not as expenses of the firm."),
        ("Is registering a partnership deed with the Registrar of Firms required?",
         "It is not required for tax, but a registered deed helps with banks, contracts and legal enforcement."),
    ],
}

PAGES["blogs/minimum-tax-turnover-pakistan.html"] = {
    "body": """## A Worked Example

Consider a trading company with turnover of Rs 200 million and a net profit of only Rs 3 million in a difficult year.

| Item | Amount |
| Turnover | Rs 200,000,000 |
| Minimum tax at an illustrative 1.25% | Rs 2,500,000 |
| Normal tax on Rs 3,000,000 profit at 29% | Rs 870,000 |
| Tax payable (higher of the two) | Rs 2,500,000 |
| Excess over normal tax available to carry forward | Rs 1,630,000 |

The rate used here is for illustration; the actual rate depends on the sector and the current First Schedule.

## Carrying the Excess Forward

The difference between minimum tax paid and normal tax can generally be carried forward for up to three tax years and adjusted against normal tax in a year when normal tax is higher than minimum tax. Track this balance year by year; it is easy to lose if returns are prepared by different people.

## What Counts as Turnover

Turnover usually means gross sales or gross receipts, excluding sales tax and federal excise duty, and after trade discounts shown on invoices. For service businesses it is gross fees. Getting the definition wrong in either direction, such as including sales tax or leaving out other receipts, changes the minimum tax directly.

## Minimum Tax Through Withholding

Section 113 is not the only minimum tax. Tax withheld on some transactions, such as certain imports or payments for goods, can itself be minimum tax under the relevant section. In those cases a loss does not lead to a refund of the deduction. Knowing which deductions are adjustable and which are minimum is essential before projecting a refund. Our detailed [section 113 guide](/blogs/minimum-tax-section-113-pakistan) covers the law clause by clause.""",
    "faq": [
        ("Can excess minimum tax be carried forward?",
         "Generally yes, for up to three tax years, and adjusted when normal tax exceeds minimum tax in a later year."),
        ("Does turnover include sales tax?",
         "No. Turnover for minimum tax generally excludes sales tax and federal excise duty."),
    ],
}

PAGES["blogs/property-purchase-pakistan-dubai-pakistanis.html"] = {
    "replace": [('href="/income-tax-filing.html"', 'href="/income-tax-filing"')],
    "drop": ["filer vs non-filer withholding tax on property"],
    "faq_skip": ["How much tax do I pay on property purchase as a filer vs non-filer?"],
    "body": """## Current Advance Tax on Buying and Selling

For property transfers from 1 July 2026, the advance tax rates are:

| Transaction | Section | On the Active Taxpayers List | Not on the list |
| Buying | 236K | 1.25% | 2.5% |
| Selling | 236C | 2.75% | 5.5% |

On a Rs 20 million house, the buyer's advance tax is Rs 250,000 as an active filer and Rs 500,000 otherwise. Capital gains tax on a later sale is separate and depends on the holding period and the date the property was acquired.

## Proving the Money Came from Dubai

The UAE has no personal income tax on salary, so there is no UAE tax return to show. Your evidence is instead:

- salary certificates or an employment contract from your UAE employer;
- UAE bank statements showing salary credits and the outgoing transfer;
- the Pakistani bank's credit advice or encashment certificate for the funds received.

Send money through banks or a Roshan Digital Account rather than exchange houses that cannot provide a clean trail.

## Power of Attorney from the UAE

If you cannot travel, a special power of attorney limited to the specific property is safer than a general one. It is usually executed or attested through the Pakistani mission in the UAE and then used by your representative at registration. Make sure the deed is in your name, not the attorney's.

## After the Purchase

Declare the property in your wealth statement for the year of purchase, together with the advance tax paid as a credit. Section 7E deemed income applies to resident persons, so a genuinely non-resident owner is generally outside it, but your status should be checked each year you spend time in Pakistan.""",
    "faq": [
        ("What advance tax does an overseas buyer pay on a Pakistani property?",
         "For transfers from 1 July 2026, 1.25% under section 236K for buyers on the Active Taxpayers List and 2.5% for others."),
        ("How do I prove the source of funds from Dubai?",
         "Use UAE salary certificates and bank statements together with the Pakistani bank's credit advice or encashment certificate."),
    ],
}

PAGES["blogs/capital-value-tax-pakistan-2026.html"] = {
    "body": """## Valuing Foreign Assets for CVT

The tax is charged on value, so the valuation method decides the bill. Practical approaches we use:

| Asset | Valuation evidence |
| Foreign bank balance | Bank statement at 30 June, converted at the State Bank rate |
| Listed foreign shares | Year-end market price from the broker statement |
| Foreign property | Purchase deed and any recent valuation or council assessment |
| Foreign vehicle | Purchase invoice adjusted for age, or a dealer quote |

Keep the source of each valuation with your working papers. If FBR questions the figure, a documented method is far easier to defend than an estimate.

## Exchange Rates and Timing

Convert foreign values to rupees at the rate prescribed for the purpose, usually linked to the State Bank's rate on the relevant date. Sharp rupee movements can change CVT significantly from one year to the next even when the asset's foreign-currency value is unchanged.

## Who Is Typically Affected

- Residents who bought apartments in Dubai, London or elsewhere.
- Professionals holding foreign brokerage accounts or retirement funds.
- Returning expatriates whose foreign assets remain abroad after they become resident in Pakistan.

Returning expatriates should look at their residence status and the timing of any transfer of assets, because becoming resident brings foreign assets into both the wealth statement and CVT.

## Paying CVT

CVT is computed in the return and paid through a payment slip (PSID) generated on IRIS. Pay before submitting so the return shows no outstanding demand.""",
    "faq": [
        ("Which exchange rate is used for CVT?",
         "Foreign values are converted at the rate prescribed for the purpose, generally linked to the State Bank's rate on the relevant date."),
        ("Do returning expatriates pay CVT on assets left abroad?",
         "Once they become resident, foreign assets come into the wealth statement and can fall under CVT if above the threshold, so timing matters."),
    ],
}

PAGES["blogs/professional-tax-pakistan-2026.html"] = {
    "drop": ["professional tax rates by province 2026"],
    "faq_skip": ["Who must pay professional tax in Punjab?"],
    "body": """## Who Collects Professional Tax in Each Province

| Province | Collecting department | How it is paid |
| Punjab | Excise, Taxation and Narcotics Control Department | Online challan or designated banks |
| Sindh | Excise, Taxation and Narcotics Control Department | Online portal or designated banks |
| Khyber Pakhtunkhwa | Excise, Taxation and Narcotics Control Department | Designated banks and online services |
| Balochistan | Excise and Taxation Department | Designated banks |

Professional tax is fixed by each province's Finance Act in a schedule of categories, such as companies, traders, professionals, factories and certain employees. The amounts are modest and are revised from time to time, so we check the schedule for your category every year rather than relying on old lists.

## How It Differs from Income Tax

Professional tax is a flat annual levy based on your category or business size, not a percentage of profit. It does not replace federal income tax and is not credited against it. Where it relates to your business, it is generally treated as a business expense in the income tax return.

## Consequences of Not Paying

Unpaid professional tax can hold up business licence renewals, trade body memberships and certain government registrations. Provinces also run recovery drives and can charge additional amounts on arrears.

## What to Keep

Keep the paid challan for each year with your business records. It supports the expense in your income tax return and is often asked for when renewing licences or bidding for government work.""",
    "faq": [
        ("Who collects professional tax in Punjab?",
         "The Punjab Excise, Taxation and Narcotics Control Department collects professional tax under the provincial Finance Act schedule."),
    ],
}

PAGES["blogs/late-filing-penalty-income-tax-pakistan.html"] = {
    "desc": "Late income tax return penalty in Pakistan 2026: how section 182 penalty orders arrive, default surcharge vs ATL surcharge, and evidence that reduces it.",
    "body": """## How a Penalty Actually Reaches You

IRIS does not deduct a penalty when you submit a late return. The process normally runs like this:

1. A notice is issued asking why the return was late or why a penalty should not be imposed.
2. You reply, ideally with evidence of the reason for the delay.
3. The officer passes an order imposing, reducing or dropping the penalty.
4. If you disagree, you can appeal to the Commissioner (Appeals) and then to the Appellate Tribunal Inland Revenue.

A clear, documented reply at step 2 resolves most cases without an appeal.

## Penalty Versus Default Surcharge

These are often confused:

| Charge | What triggers it | How it is calculated |
| Penalty under section 182 | Late or missing return, among other defaults | Set out in the penalty table, with minimum amounts |
| Default surcharge under section 205 | Tax paid after its due date | A rate linked to KIBOR, for the period of delay |
| ATL surcharge | Getting on the Active Taxpayers List after a late return | A fixed amount by taxpayer type |

A late return with tax still unpaid can attract all three, so paying the tax first limits the surcharge.

## Evidence That Supports a Reduction

- Hospital records or a death certificate for the period.
- Screenshots or FBR announcements showing IRIS problems near the deadline.
- Proof that documents from an employer or bank arrived late.
- Travel records showing you were abroad without access.

Our [FBR notice service](/fbr-notice-defense) prepares these replies from Rs 5,000.""",
    "faq": [
        ("Is the late filing penalty charged automatically by IRIS?",
         "No. It is normally imposed through a notice and an order after the return is filed late, and you can reply before the order is made."),
        ("What is the difference between a penalty and default surcharge?",
         "The penalty is for the late return; default surcharge under section 205 is charged on tax paid late, for the period of delay."),
    ],
}

PAGES["blogs/section-7e-tax-pakistan.html"] = {
    "body": """## Common Exemptions in the Section

Section 7E applies to resident persons and lists several categories that are excluded. In summary, these include:

| Category | Why it is excluded |
| One self-owned house used as residence | Personal residence relief |
| Property used for your own business | Already part of business income |
| Property let out on rent where rent is taxed | Actual rent is taxed instead |
| Agricultural land where farm income is taxed by the province | Provincial tax applies |
| Property acquired in the year on which advance tax under 236K was paid | First-year relief |
| Total property value within the aggregate limit set in the section | Small holdings excluded |

The aggregate limit was Rs 25 million when the section was introduced. Some exemptions have conditions, so check each property individually.

## Valuation Under 7E

Fair market value is generally taken from the FBR valuation table for the area, not the price you paid or a market estimate. In cities where valuation tables were revised upward, 7E liability rose even though nothing else changed. Keep a copy of the valuation table entry you used.

## Court Challenges

Section 7E has been challenged in several High Courts since it was introduced, and decisions have not been uniform across provinces. Some taxpayers obtained relief; others did not. The safe course is to declare 7E correctly in your return, pay where it applies, and take advice if you want to rely on a court decision, because the outcome can depend on your jurisdiction and the case.

## Paying 7E Before a Sale

When a property is sold, the 7E position for earlier years is often checked at registration. Clearing past years in advance avoids delays at the registrar's office.""",
    "faq": [
        ("Does section 7E apply to non-residents?",
         "Section 7E applies to resident persons. A genuinely non-resident owner is generally outside it, but residence must be checked each year."),
        ("Is 7E calculated on purchase price or FBR value?",
         "It is generally based on the fair market value under the FBR valuation table for the area, not the purchase price."),
    ],
}
