"""Service, consultant, registration, vehicle, WHT, deadline and pensioner pages."""

PAGES = {}

PAGES["blogs/best-tax-consultant-near-me-pakistan.html"] = {
    "body": """## How to Check a Tax Consultant Before You Hire

Whether the consultant is down the street or in another city, a few checks separate a reliable firm from a risky one:

| Check | What a good answer looks like |
| Where is the return filed? | On FBR's IRIS portal under your own NTN, with the acknowledgement sent to you |
| How is tax paid? | Through a PSID payment slip in your name, never cash handed to the consultant |
| Who keeps your IRIS password? | You do; the consultant uses it only with your permission and you can change it after filing |
| Is the fee fixed in advance? | Yes, confirmed in writing before work starts |
| Can you see the draft? | Yes, before submission |

## Red Flags

- Promises of a refund before your documents have been reviewed.
- Requests to file under someone else's NTN or to inflate expenses.
- No written fee quote, or a fee that changes after filing.
- Reluctance to share the FBR acknowledgement.

## If You Prefer to Meet in Person

Most of our clients never visit, but clients in Lahore are welcome at our office: Shop No 34, Rizwan Block Market, opposite Rizwan Park, Awan Town, Lahore. Call 0328-4675162 first so the right consultant is available.

## What You Get from an Online Consultant

The work is the same as an office visit: document review, return preparation, wealth statement, submission and follow-up on any notice. The difference is that documents travel by WhatsApp or email and you approve the draft on your phone. Fees for each service are listed on our [pricing page](/pricing).""",
    "faq": [
        ("Should a consultant pay my tax for me in cash?",
         "No. Tax should be paid through a PSID payment slip generated in your name on IRIS, so the payment is linked to your NTN."),
        ("Where is the Kamboh Associates office?",
         "Shop No 34, Rizwan Block Market, opposite Rizwan Park, Awan Town, Lahore. Most clients are served online via WhatsApp 0328-4675162."),
    ],
}

PAGES["blogs/tax-on-inheritance-pakistan.html"] = {
    "body": """## Getting the Legal Paperwork in Order

Before an inherited asset can be put in your name, the legal heirs must be established. The documents depend on the asset:

| Asset | Typical document |
| Bank accounts and savings certificates | Succession certificate, issued in many districts through NADRA's succession facilitation units or the civil court |
| Agricultural or rural land | Inheritance mutation (intiqal) at the land record centre |
| Urban plot or house in a housing society | Society transfer to legal heirs on the basis of the succession or heirship documents |
| Shares and mutual funds | Transmission through the company or fund using the succession certificate |
| Vehicle | Transfer by the excise department on the basis of heirship documents |

## Transfers Among Heirs

Often one heir buys out the others' shares. That buy-out is a sale between the heirs, not part of the inheritance. Depending on the property, it can involve advance tax at registration and capital gains for the selling heirs. Keeping the inheritance step and the buy-out step clearly separate in the documents avoids treating the whole property as a sale.

## Cost and Holding Period for a Later Sale

When an inherited property is eventually sold, the cost and the holding period used for capital gains matter. The rules for inherited assets differ from ordinary purchases, so check them before agreeing a sale price. Keep the deceased's purchase documents if they exist, along with the date of death and the succession papers.

## The Deceased's Own Tax Affairs

Legal representatives are responsible for filing any outstanding return of the deceased and settling tax due from the estate before distribution. If the deceased was a filer, the final return covers income up to the date of death.""",
    "faq": [
        ("Is buying out my siblings' share of an inherited house taxed?",
         "The buy-out is a sale between heirs, separate from the inheritance, and can involve advance tax and capital gains for the selling heirs."),
        ("Who files the last return of a deceased person?",
         "The legal representatives file any outstanding return and settle tax due before distributing the estate."),
    ],
}

PAGES["blogs/affordable-tax-consultant-pakistan.html"] = {
    "body": """## Full Fee List for Common Services

| Service | Fee |
| Salaried individual return | Rs 3,500 |
| Freelancer or sole proprietor return | Rs 5,000 |
| NTN registration | Rs 2,000 |
| Wealth statement | Rs 2,000 |
| Overseas Pakistani return | Rs 6,000 |
| AOP return | Rs 8,000 |
| Sales tax registration (STRN) | Rs 3,000 |
| Monthly sales tax return | Rs 3,000 per month |
| Withholding statement | Rs 2,500 per month |
| FBR notice reply | From Rs 5,000 |
| Private limited company registration | From Rs 15,000 |

These match our [pricing page](/pricing), which is updated whenever fees change.

## When a Fee Is Higher Than the Base Price

A return can cost more than the starting fee when it involves several income sources at once, such as salary plus rent plus a business, multiple years being filed together, or a wealth statement that needs reconstruction because assets were never declared. We quote the exact fee after seeing your documents, before any work starts.

## Comparing Cost with the Saving

Filing is often cheaper than staying off the Active Taxpayers List. For example, the advance tax on buying a Rs 10 million property from 1 July 2026 is Rs 125,000 for an active filer and Rs 250,000 otherwise, a difference of Rs 125,000 on one transaction. A Rs 3,500 return pays for itself many times over.""",
    "faq": [
        ("How much does a freelancer return cost?",
         "Rs 5,000, the same as a sole proprietor return, as listed on the pricing page."),
        ("Why might my return cost more than Rs 3,500?",
         "Multiple income sources, several years filed together or a wealth statement that needs reconstruction take more work. The fee is confirmed before starting."),
    ],
}

PAGES["blogs/aop-tax-return-pakistan-2026.html"] = {
    "body": """## Filing the AOP Return on IRIS

1. Log in with the AOP's own NTN credentials, not a partner's.
2. Select the return of income for the AOP for the tax year.
3. Enter revenue, cost of sales and operating expenses from the firm's accounts.
4. Add back any salary, interest or commission paid to members, which are not expenses of the firm.
5. Claim tax deducted at source on the firm's receipts, such as contract payments and bank profit.
6. Show the divisible income and each member's share.
7. Pay any balance through a PSID and submit.

AOPs do not file a wealth statement themselves; each member files their own with their personal return.

## Members' Returns After the AOP Files

Each member declares their share of profit from the AOP in their personal return. Because the AOP has already paid tax, the share is exempt, but the figures must match the AOP return exactly. Filing the AOP first and the members' returns afterwards avoids mismatches.

## AOP as a Withholding Agent

An AOP above the prescribed turnover becomes a withholding agent. It must deduct tax on salaries, rent and supplier payments and file withholding statements, just like a company. Failure can lead to the expense being disallowed in the AOP's own return.

## Fees

AOP return filing is Rs 8,000 and members' returns are filed alongside, per our [pricing page](/pricing).""",
    "faq": [
        ("Does an AOP file a wealth statement?",
         "No. The AOP files its return; each member files a personal wealth statement with their own return."),
        ("Can an AOP deduct salaries paid to its members?",
         "No. Payments to members are treated as part of their profit share and are added back in the AOP's computation."),
    ],
}

PAGES["blogs/strn-registration-pakistan.html"] = {
    "replace": [("is a 7-digit number issued by FBR that", "is the registration number FBR issues that"),
                ("your 7-digit STRN", "your STRN"),
                ("Rs. 10,000 + 12% p.a. surcharge", "Penalty under section 33 plus default surcharge"),
                ("Default surcharge (KIBOR+3%)", "Default surcharge at a KIBOR-linked rate")],
    "body": """## Federal STRN or Provincial Registration?

Sales tax in Pakistan is split. FBR taxes goods; the provinces tax services. Many businesses need one, some need both.

| Business | Federal STRN (FBR) | Provincial registration |
| Manufacturer of goods | Yes | Only if it also provides taxable services |
| Importer or wholesaler of goods | Yes, subject to thresholds | Usually no |
| Software house or consultancy | Usually no | PRA, SRB, KPRA or BRA depending on location |
| Restaurant | Depends on structure | Yes, under the provincial law |
| Online seller of physical products | Yes, once it is a Tier-1 retailer or above thresholds | Possibly, for delivery or other services |

## The Sales Tax Active Taxpayers List

Sales tax has its own Active Taxpayers List, separate from the income tax list. A registered person who fails to file monthly returns drops off it, and buyers cannot claim input tax on purchases from someone who is not active. Staying on this list is therefore commercially important, not just a compliance detail.

## Suspension and Blacklisting

Under section 21, FBR can suspend or blacklist a registration where it suspects fake invoices, non-existent premises or non-filing. A suspended person cannot issue valid invoices until the matter is resolved. Responding quickly to the show-cause notice, with evidence of premises and genuine business, is the best way to restore it.

## Fees

STRN registration is Rs 3,000 and monthly sales tax return filing is Rs 3,000 per month on our [pricing page](/pricing).""",
    "faq": [
        ("Is there a separate Active Taxpayers List for sales tax?",
         "Yes. Sales tax has its own active list, and buyers cannot claim input tax on purchases from suppliers who are not active."),
        ("Can FBR suspend my STRN?",
         "Yes. Under section 21, registration can be suspended or blacklisted for suspected fake invoicing, non-existent premises or non-filing, after a notice."),
    ],
}

PAGES["blogs/token-tax-pakistan-2026.html"] = {
    "replace": [("Being an active filer reduces the Section 231B WHT by up to 50%.",
                 "Being on the Active Taxpayers List means the lower filer rate applies; non-filers pay a substantially higher amount.")],
    "drop": ["section 231b wht on vehicle purchase 2026", "become a filer before buying your vehicle"],
    "faq_skip": ["How much do filers save on vehicle registration in Pakistan?"],
    "body": """## Every Point Where Vehicle Tax Is Collected

| Stage | Tax | Collected by |
| First registration of a new car | Advance income tax under section 231B, by engine size or value | Excise department on behalf of FBR |
| Transfer to a new owner | Advance income tax on transfer under section 231B | Excise department |
| Every year | Provincial token tax, plus advance income tax under section 234 for private vehicles | Excise department |
| Leasing a vehicle | Advance tax collected by the leasing company | Bank or leasing company |

The income tax parts of these collections are adjustable against your annual liability if you file a return. The token tax itself is a provincial levy and is not credited against income tax.

## Why Filer Status Matters at Each Stage

Both the advance tax at registration and the annual tax with token are charged at higher rates for people not on the Active Taxpayers List. If you are planning to buy a car, file your return first and confirm your name appears on the list before the vehicle is registered.

## Paying Token Tax Online

Punjab, Sindh, Khyber Pakhtunkhwa and Islamabad offer online payment through their excise portals or banking apps. Some provinces also offer a lifetime token option for smaller cars, which removes the yearly payment. Keep the e-receipt; traffic police and future buyers may ask for it.

## Claiming the Advance Tax in Your Return

The excise receipt shows the income tax part separately from token tax. Enter that amount as tax collected in your return. Many vehicle owners never claim it and lose a credit every year.""",
    "faq": [
        ("Can I claim the tax paid with my car's token in my income tax return?",
         "The advance income tax collected under section 234 with the token can be claimed as a credit. The provincial token tax itself cannot."),
        ("Does filer status affect vehicle registration tax?",
         "Yes. Advance tax at registration and with the annual token is higher for people not on the Active Taxpayers List."),
    ],
}

PAGES["blogs/company-registration-pakistan-2026.html"] = {
    "replace": [("(starts from Rs. 1,500)", "(set by SECP's fee schedule according to authorised capital)"),
                ("<td>TDCP / District Council</td>", "<td>No separate registration; NTN with FBR</td>")],
    "drop": ["secp registration fees pakistan 2026"],
    "faq_skip": ["How much does it cost to register a company in Pakistan?"],
    "body": """## What Happens After Incorporation

The Certificate of Incorporation is the start, not the end. A new private limited company has ongoing SECP and FBR obligations:

| Obligation | Authority | Timing |
| Company NTN and IRIS profile | FBR | Immediately after incorporation |
| Bank account in the company's name | Bank | Before trading starts |
| Annual return (Form A) | SECP | After the annual general meeting each year |
| Changes in directors, address or shareholding | SECP | Within the period set for each form |
| Beneficial ownership record | SECP | Kept up to date and filed as required |
| Audited financial statements | SECP and FBR | Annually, as required by the Companies Act |
| Income tax return | FBR | By 31 December for a June year end |

## Tax Position of a New Company

Companies pay corporate income tax on profit, generally at 29%, with different treatment for some sectors and for small companies that meet the legal definition. Minimum tax on turnover can apply even in loss years. Dividends paid to shareholders are taxed again in their hands through withholding, which is why some owners prefer to start as a sole proprietor and incorporate later.

## Choosing Between SMC and Private Limited

A Single Member Company suits one owner who wants limited liability. If a second shareholder joins later, the SMC can convert to a private limited company. Starting as a private limited company with a family member as a nominal shareholder is common but creates real legal ownership, so it should be a deliberate choice.

## Fees

Private limited company registration starts at Rs 15,000 and corporate returns at Rs 18,000 on our [pricing page](/pricing). SECP's own fee is extra and depends on authorised capital.""",
    "faq": [
        ("What is the corporate tax rate in Pakistan?",
         "Companies are generally taxed at 29% on profit, with special treatment for certain sectors and qualifying small companies."),
        ("What must a company file with SECP each year?",
         "An annual return after the AGM, audited accounts as required, and forms for any changes in directors, address or shareholding."),
    ],
}

PAGES["blogs/withholding-tax-rates-pakistan-2026.html"] = {
    "drop": ["complete wht rate table 2025 26"],
    "body": """## Withholding Rates We Can Confirm for 2026-27

Withholding rates change every budget, and many are set in detailed slabs by category. Below are figures we use for the current year. For anything not listed, we check FBR's Withholding Tax Regime Card for the tax year before advising.

| Transaction | Section | On the Active Taxpayers List | Not on the list |
| Buying immovable property (transfers from 1 July 2026) | 236K | 1.25% | 2.5% |
| Selling immovable property (transfers from 1 July 2026) | 236C | 2.75% | 5.5% |
| Prize bond winnings | 156 | 15% | 30% |
| Lottery and similar prizes | 156 | 20% | 40% |
| Online sales paid digitally (e-commerce collection) | E-commerce provisions | 1% | — |
| Online sales paid cash on delivery | E-commerce provisions | 2% | — |

## Adjustable, Minimum or Final?

Every deduction falls into one of three groups, and the group decides whether a refund is possible:

- **Adjustable** deductions are advance payments. If they exceed your tax, the excess can be refunded.
- **Minimum** tax deductions cannot be refunded even if your actual tax is lower, though higher actual tax is still payable.
- **Final** tax deductions settle the tax on that income completely; the income is not added to your other income.

The same payment can fall into different groups for different taxpayers, for example a company versus an individual.

## Where to Find the Official Rates

FBR publishes a Withholding Tax Regime Card after each Finance Act, listing sections, rates and the withholding agent for each transaction. It is the most reliable single source; social media tables are often a year out of date.

## Checking a Deduction on Your Account

Every deduction made against your CNIC or NTN appears in your IRIS profile and on the tax certificate from the withholding agent. Compare the two before filing so nothing is missed.""",
    "faq": [
        ("What is the advance tax on buying property in 2026-27?",
         "For transfers from 1 July 2026, 1.25% under section 236K for buyers on the Active Taxpayers List and 2.5% for others."),
        ("What is withholding tax on prize bond winnings?",
         "15% for persons on the Active Taxpayers List and 30% for others, collected as final tax."),
    ],
}

PAGES["blogs/sole-proprietor-tax-return-pakistan-2026.html"] = {
    "desc": "How a sole proprietor files an income tax return in Pakistan 2026: profit computation, records under section 174, separate business account and fees.",
    "replace": [("from Rs 7,000", "from Rs 5,000"), ("From Rs 7,000", "From Rs 5,000"), ("Rs 1,500", "Rs 2,000"),
                ("if last year liability exceeded Rs 100,000", "if your income crosses the threshold in section 147")],
    "drop": ["pricing"],
    "faq_skip": ["What income tax rate applies to sole proprietors in Pakistan 2026?"],
    "body": """## How a Sole Proprietor's Tax Is Worked Out

1. Start from total sales or fees for the year (1 July to 30 June).
2. Subtract the cost of goods sold, such as purchases adjusted for opening and closing stock.
3. Subtract business expenses: rent, salaries, utilities, transport, repairs and depreciation on business assets.
4. The result is business profit, which is added to any other income such as rent or salary.
5. Tax is calculated on the total using the slab rates for individuals with business income, which differ from the salaried slabs.
6. Tax deducted at source on sales, electricity bills and bank profit is subtracted.

## Records That Satisfy FBR

Section 174 requires taxpayers to keep records that support their return. For a small sole proprietor this means:

- a sales register or copies of invoices;
- purchase bills and supplier details;
- bank statements for the business account;
- salary sheets if staff are employed;
- a year-end stock list for traders.

Records should be kept for at least six years after the tax year.

## Separating Business and Personal Money

Using one bank account for both business and household spending is the most common reason sole proprietors struggle to explain their deposits. A separate business account, even a simple current account, makes the profit computation and the wealth statement much easier.

## Fees

Sole proprietor returns are Rs 5,000, NTN registration Rs 2,000 and monthly withholding statements Rs 2,500, per our [pricing page](/pricing).""",
    "faq": [
        ("Do sole proprietors use the salaried tax slabs?",
         "No. Individuals with business income use the non-salaried slab rates, which are different from the salaried slabs."),
        ("How long should a sole proprietor keep business records?",
         "At least six years after the end of the tax year, as required under section 174."),
    ],
}

PAGES["blogs/income-tax-return-deadline-pakistan-2026.html"] = {
    "desc": "Income tax return last date in Pakistan for tax year 2026: 30 September for individuals and AOPs, 31 December for companies, plus advance tax dates.",
    "replace": [("Missing this deadline results in automatic penalties.", "Missing it can lead to a penalty, the ATL surcharge and higher withholding.")],
    "drop": ["tax return deadlines pakistan 2026", "what happens if you miss the 30 september deadline?", "pricing"],
    "faq_skip": ["Can I file my return after 30 September 2026?", "What is the penalty for not filing at all in Pakistan?"],
    "body": """## Key Federal Tax Dates for Tax Year 2026

| Obligation | Due date |
| Return and wealth statement for individuals and AOPs | 30 September 2026 |
| Return for companies with a 30 June year end | 31 December 2026 |
| Advance tax instalments under section 147 | 25 September, 25 December, 25 March and 15 June |
| Monthly sales tax payment and return | 15th and 18th of the following month |
| Salary withholding deposit by employers | Within the time set after deduction each month |

Companies with a special tax year file within the period after their year end set in section 118.

## Planning the Filing Month

IRIS slows down in the last week of September every year as millions of returns are submitted. A practical calendar:

- **July:** collect salary, bank and property tax certificates for the year that ended 30 June.
- **August:** prepare the return and wealth statement; resolve missing documents.
- **First half of September:** submit and download the acknowledgement.
- **After filing:** check that your name appears on the Active Taxpayers List when it is next updated.

## If You Cannot Meet the Date

An individual extension can be requested under section 119, but only before the due date. If the deadline has already passed, file as soon as possible and pay the ATL surcharge. Our [late filing guide](/blogs/income-tax-return-late-filing-pakistan) explains the consequences.

## Fees

Salaried returns are Rs 3,500, sole proprietor and freelancer returns Rs 5,000, AOP returns Rs 8,000 and corporate returns from Rs 18,000, per our [pricing page](/pricing).""",
    "faq": [
        ("When are company returns due?",
         "Companies with a 30 June year end file by 31 December. Companies with a special tax year follow the period in section 118."),
        ("When are advance tax instalments due?",
         "On 25 September, 25 December, 25 March and 15 June for taxpayers liable under section 147."),
    ],
}

PAGES["blogs/online-tax-consultant-pakistan.html"] = {
    "replace": [("Exporters needing WHT compliance and DTRE guidance", "Exporters needing WHT compliance and Export Facilitation Scheme guidance")],
    "drop": ["transparent online pricing"],
    "faq_skip": ["What documents do I need to share for online tax filing?"],
    "body": """## How We Protect Your Information

Working online means your documents travel by WhatsApp or email, so we follow simple rules:

- We never ask for your bank login, card PIN or one-time banking passwords.
- Your IRIS password is used only to file your return; you can change it after filing.
- The IRIS submission PIN is sent to your own mobile number, so nothing is submitted without you.
- Documents are used only for your filing and are not shared with third parties.

## Documents by Type of Taxpayer

| Taxpayer | Documents |
| Salaried | CNIC, salary certificate with tax deducted, bank statement |
| Freelancer | CNIC, platform earnings report, bank statements, remittance tax certificates |
| Business owner | CNIC, sales and purchase summary, bank statements, electricity bills |
| Landlord | CNIC, tenancy agreements, rent receipts, tax certificates from tenants |
| Overseas Pakistani | CNIC or NICOP, travel history, Pakistani bank statements, property papers |

## Verifying the Filing Yourself

After we file, you receive the FBR acknowledgement. You can also check FBR's Active Taxpayers List online with your CNIC once the list is updated, and log in to IRIS to see the submitted return.

## Fees

Fees for each service are listed on our [pricing page](/pricing): Rs 3,500 for salaried returns, Rs 5,000 for freelancers and sole proprietors, and Rs 2,000 for NTN registration.""",
    "faq": [
        ("Do you need my bank password to file my return?",
         "No. We only need statements. Never share banking passwords, card PINs or banking one-time codes with anyone."),
        ("What documents does a freelancer send for online filing?",
         "CNIC, platform earnings report, bank statements and the bank's certificates of tax deducted on foreign remittances."),
    ],
}

PAGES["blogs/best-tax-consultant-pakistan.html"] = {
    "replace": [("Business return from Rs. 7,000. NTN registration Rs. 2,000. Sales tax registration Rs. 5,000.",
                 "Freelancer and sole proprietor return from Rs. 5,000. NTN registration Rs. 2,000. Sales tax registration Rs. 3,000.")],
    "faq_skip": ["What is the fee for income tax return filing in Pakistan?"],
    "body": """## What Makes a Consultant the Right Fit for You

"Best" depends on what you need. A salaried employee, an exporter and a family with property disputes need different strengths:

| Your situation | What to look for |
| Salaried with a refund due | Speed, correct claim of deductions and credits |
| Freelancer or IT exporter | Knowledge of foreign remittance treatment and PSEB registration |
| Shop or trading business | Practical bookkeeping help and sales tax experience |
| Landlord or property investor | Advance tax, capital gains and section 7E experience |
| Overseas Pakistani | Residency rules and remote handling |
| Received an FBR notice | Experience drafting replies and appearing in hearings |

## Questions Worth Asking

- Will you explain each figure in the return before filing?
- Who handles my file if my usual contact is unavailable?
- What happens if a notice arrives after filing?
- Is the fee fixed, and what would make it change?

## How We Work

Kamboh Associates has served clients since 2008 from Lahore, mostly online. Every return is reviewed before submission, you approve the draft, and you receive the FBR acknowledgement. Our office is at Shop No 34, Rizwan Block Market, opposite Rizwan Park, Awan Town, Lahore, and fees are published on our [pricing page](/pricing).""",
    "faq": [
        ("How much does Kamboh Associates charge for a return?",
         "Rs 3,500 for salaried individuals, Rs 5,000 for freelancers and sole proprietors, and Rs 6,000 for overseas Pakistanis, as listed on the pricing page."),
    ],
}

PAGES["blogs/tax-filing-pensioners-pakistan.html"] = {
    "desc": "Income tax for pensioners in Pakistan 2026: exempt government pension and commutation, taxed bank profit, wealth statement after retirement and filing.",
    "replace": [("Exempt up to Rs 300,000 for private sector; fully exempt for government servants",
                 "Generally exempt for government servants and from approved funds; other gratuity is exempt only up to Second Schedule limits"),
                ("if you own property worth over Rs 5 million, have a bank account with significant balance, or own a vehicle.",
                 "if you meet any of the filing conditions in section 114, for example owning certain property or a larger vehicle, and filing is the only way to stay on the Active Taxpayers List.")],
    "drop": ["pricing"],
    "faq_skip": ["Is gratuity received on retirement taxable in Pakistan?"],
    "body": """## Commutation, Arrears and Family Pension

Pension rarely arrives as one simple monthly figure. The common parts are treated as follows:

| Payment | Usual treatment |
| Monthly government pension | Exempt |
| Commuted portion of government pension | Exempt |
| Family pension received by a widow or dependants of a government servant | Exempt |
| Private sector pension from an approved scheme | Exempt within the limits in the Second Schedule |
| Pension arrears paid in a later year | Same treatment as the pension it relates to |

## Bank Profit Is Where Pensioners Pay Tax

Many retirees put their commutation into savings accounts or certificates. Profit on these is taxed through withholding. Being on the Active Taxpayers List keeps the deduction at the lower rate, which is often the main financial reason for a retiree to file. Keep the annual tax deduction certificates from the bank or National Savings centre and enter them in the return.

## Wealth Statement After Retirement

Retirement often changes the wealth statement significantly: commutation money comes in, a house may be built or bought, and gifts are made to children. Record each of these so the reconciliation balances. A gift to a child should appear in both the pensioner's and the child's wealth statements.

## Fees

A pension return is Rs 3,500 and a wealth statement Rs 2,000, per our [pricing page](/pricing). Elderly clients can send documents through a family member on WhatsApp 0328-4675162.""",
    "faq": [
        ("Is the commuted portion of government pension taxable?",
         "No. Commutation of government pension is exempt, as is the monthly pension and family pension for dependants."),
        ("Why should a pensioner with exempt pension file a return?",
         "To stay on the Active Taxpayers List, which keeps withholding on bank profit and property transactions at the lower rate."),
    ],
}
