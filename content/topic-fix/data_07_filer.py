"""Filer status, withholding, notices, slabs, exemptions, company and sales tax pages with long unique bodies."""

PAGES = {}

PAGES["blogs/corporate-tax-rate-pakistan-2026.html"] = {
    "body": """## Dividends: The Second Layer of Tax

Corporate tax is only part of the picture for owners. When a company distributes profit, it deducts withholding tax on the dividend under section 150, at a rate that is higher for shareholders not on the Active Taxpayers List. For an individual shareholder this deduction is generally the final tax on the dividend. Owners comparing a company with a sole proprietorship should therefore add corporate tax, super tax where applicable and dividend tax together before deciding.

## Accounting Year and Filing Date

Most companies use a 30 June year end and file by 31 December. A company can apply for a special tax year, for example to align with a foreign parent's calendar year, in which case its filing date shifts accordingly. Advance tax under section 147 is payable quarterly in either case.""",
    "faq": [
        ("Is dividend income taxed after the company pays corporate tax?",
         "Yes. The company deducts withholding tax on dividends under section 150, which is generally final tax for individual shareholders."),
    ],
}

PAGES["blogs/fbr-active-taxpayer-list-guide.html"] = {
    "drop": ["fbr iris portal — complete guide 2026", "common fbr iris issues and solutions", "fbr helpline and support"],
    "body": """## How Often the List Is Updated

FBR publishes the Active Taxpayers List for income tax once a year, on 1 March, based on returns filed for the previous tax year. Late filers who pay the ATL surcharge are added as their payments are processed, so their names can appear between the annual updates. If you filed and paid but do not appear after a reasonable time, a request through the IRIS facilitation channel usually resolves it.

## Checking Status Before a Transaction

| Method | How it works |
| FBR website ATL search | Enter CNIC or NTN to see current status |
| SMS service | Send ATL followed by your CNIC to FBR's short code |
| Tax Asaan app | Check status from your phone |

Banks, the excise department and property registrars check the list on the date of the transaction. Print or screenshot your status before a large transaction so you can show it if the counter staff see something different.

## Separate Lists for Sales Tax

Registered sales tax persons have their own Active Taxpayers List, based on monthly returns. A business can be active for income tax and inactive for sales tax, or the other way round.""",
    "faq": [
        ("When is the Active Taxpayers List updated?",
         "It is published each year on 1 March for the previous tax year's returns, and late filers who pay the surcharge are added as they are processed."),
        ("How can I check my ATL status by SMS?",
         "Send ATL followed by your CNIC to FBR's SMS short code, or use the Tax Asaan app or the online ATL search."),
    ],
}

PAGES["blogs/fbr-audit-pakistan-2026.html"] = {
    "faq_skip": ["What is the penalty if FBR finds unreported income in an audit?"],
    "body": """## Audit Outcomes and What Follows

An audit ends with one of three results: no change, an amended assessment with additional tax, or an amended assessment that also leads to penalty proceedings. Additional tax carries default surcharge from the original due date. If you disagree with the amended assessment, the appeal goes first to the Commissioner (Appeals) and then to the Appellate Tribunal Inland Revenue, with strict time limits for each step. Paying part of the disputed tax while appealing can sometimes help in obtaining a stay of recovery.""",
    "faq": [
        ("Can I appeal against an audit result?",
         "Yes. Appeals go to the Commissioner (Appeals) and then the Appellate Tribunal Inland Revenue, within the time limits set in the law."),
    ],
}

PAGES["blogs/fbr-audit-selection-criteria.html"] = {
    "drop": ["fbr iris portal — complete guide 2026", "common fbr iris issues and solutions", "fbr helpline and support"],
    "body": """## Random Ballot Versus Parametric Selection

FBR selects cases for audit in two main ways. Some are chosen through a computerised random ballot from all returns filed. Others are chosen on risk parameters: large differences between declared income and third-party data, sudden changes in profit margin, high refunds or repeated losses. Separately, the Commissioner can select a case for reasons recorded in writing. Being selected by ballot does not imply wrongdoing, but the response still needs the same care.

## Data FBR Matches Against Returns

| Data source | What it reveals |
| Banks | Large deposits, profit on deposits, cash withdrawals |
| Property registrars | Purchases and sales with values |
| Excise departments | Vehicle registrations and transfers |
| Electricity and gas companies | Commercial connections and high bills |
| Airlines and travel agents | Frequent foreign travel |
| Withholding statements | Payments received from companies and government |

## Reducing Risk Before You File

Reconcile your bank deposits with declared income, check that every withholding deduction shown in your IRIS profile appears in the return, and make sure the wealth statement explains every new asset. These three checks address most risk parameters.""",
    "faq": [
        ("Does selection in the random ballot mean FBR suspects me?",
         "No. The ballot is random, but you still need to respond fully with records supporting your return."),
    ],
}

PAGES["blogs/fbr-broadening-tax-base-pakistan.html"] = {
    "drop": ["consequences of not registering with fbr 2026"],
    "body": """## What Non-Registration Costs Today

For people outside the tax net, the cost now shows up in everyday transactions. For example, from 1 July 2026 the advance tax on buying property is 2.5% for persons not on the Active Taxpayers List against 1.25% for those on it, and the seller pays 5.5% instead of 2.75%. Prize bond winnings are taxed at 30% instead of 15%. Many other withholding rates are also higher for non-filers, and some purchases, such as certain vehicles and property above set values, have been restricted for them in recent budgets.

## Provisional Assessments for Non-Registrants

FBR has powers to register persons compulsorily and to issue provisional assessments based on the data it holds, such as bank deposits, property ownership and electricity bills. Responding by filing a proper return usually replaces the provisional figure with your actual income.""",
    "faq": [
        ("Can FBR register me without my application?",
         "Yes. FBR can register a person compulsorily on the basis of available data and may issue a provisional assessment until a return is filed."),
    ],
}

PAGES["blogs/fbr-registration-step-by-step.html"] = {
    "body": """## After Registration: First-Year Checklist

1. Download the NTN certificate from IRIS and keep it with your records.
2. Update your address, email and mobile number if anything changes.
3. Note the tax year in which your first return is due.
4. Link your bank accounts to your NTN by giving the bank your registration details, so tax deducted is credited to you.
5. File your first return and wealth statement by 30 September.

## Registering a Business Rather Than Yourself

A sole proprietor registers the business under their own CNIC-based NTN, adding the business name and address in the profile. An AOP or company receives its own NTN. Mixing these up, for example registering a partnership's business under one partner's personal NTN, causes problems with banks and withholding later.""",
    "faq": [
        ("Does a sole proprietor need a separate NTN for the business?",
         "No. A sole proprietor uses their own CNIC-based NTN and adds the business details to the profile. AOPs and companies get their own NTN."),
    ],
}

PAGES["blogs/fbr-section-122-notice-pakistan.html"] = {
    "drop": ["pricing"],
    "body": """## Time Limits on Amendment

An assessment can generally be amended under section 122 within five years from the end of the financial year in which the return was filed or deemed assessed. Notices issued outside this period can be challenged on that ground alone. Check the date of your original return before drafting any reply.

## Show-Cause Before Amendment

Before amending, the officer must issue a show-cause notice explaining the proposed changes and giving you a chance to respond. An order made without this opportunity is open to challenge. Your reply should address each point raised, attach evidence and ask for a hearing if the issues are complex.

Our [FBR notice service](/fbr-notice-defense) starts from Rs 5,000, with the exact fee depending on the issues involved.""",
    "faq": [
        ("How many years back can FBR amend an assessment under section 122?",
         "Generally within five years from the end of the financial year in which the return was filed or deemed assessed."),
    ],
}

PAGES["blogs/filer-benefits-pakistan-2026.html"] = {
    "drop": ["filer vs non-filer — withholding tax rate comparison"],
    "replace": [("As a filer you pay Rs. 6 lakh in WHT. As a non-filer: Rs. 12 lakh — a Rs. 6 lakh difference on one transaction.",
                 "From 1 July 2026, as a filer you pay Rs. 2.5 lakh advance tax under section 236K. As a non-filer: Rs. 5 lakh — a Rs. 2.5 lakh difference on one transaction."),
                ("Rs. 8,000", "Rs. 5,000")],
    "faq_skip": ["What happens if I file late and miss the ATL for a year?"],
    "body": """## Filer and Non-Filer Rates We Can Confirm

| Transaction | On the Active Taxpayers List | Not on the list |
| Buying property (section 236K, transfers from 1 July 2026) | 1.25% | 2.5% |
| Selling property (section 236C, transfers from 1 July 2026) | 2.75% | 5.5% |
| Prize bond winnings (section 156) | 15% | 30% |
| Lottery and similar prizes (section 156) | 20% | 40% |

Many other withholding rates, such as those on bank profit, dividends and vehicle registration, also differ by filer status and are revised in each budget. We check the current rate for a specific transaction before advising.

## Getting on the List After Missing the Deadline

A late filer is added to the Active Taxpayers List after filing the return and paying the ATL surcharge, which has been Rs 1,000 for individuals, with higher amounts for AOPs and companies.""",
    "faq": [
        ("How much do I save on a Rs 1 crore property as a filer?",
         "For transfers from 1 July 2026, the buyer's advance tax is Rs 125,000 on the Active Taxpayers List against Rs 250,000 otherwise, a saving of Rs 125,000."),
    ],
}

PAGES["blogs/freelancer-ntn-filer-status-guide.html"] = {
    "drop": ["freelancer tax rates pakistan 2026", "how freelancers file tax return in guide", "pseb registration for freelancers"],
    "body": """## Keeping Filer Status Year After Year

Filer status is not permanent. Your name stays on the Active Taxpayers List only if you file every year by the due date. Freelancers often file once to open a bank account or travel, then forget. Set a reminder for August each year and keep a running folder of platform statements and bank certificates so the next return takes minutes.

## Filer Status and Your Bank

Banks check the Active Taxpayers List when deducting tax on profit and cash withdrawals, and many ask freelancers for proof of NTN when receiving regular foreign remittances. Give your bank your NTN and ask it to update your profile once you are on the list, so the lower rates apply from the next transaction.

For the full filing process, see our [freelancer tax guide](/blogs/tax-for-freelancers-guide-pakistan).""",
    "faq": [
        ("Do I stay a filer once I am on the ATL?",
         "Only if you file every year. The list is based on returns filed for the previous tax year."),
    ],
}

PAGES["blogs/tax-for-freelancers-guide-pakistan.html"] = {
    "replace": [("(progressive 5%-30%)", "(at the slab rates for individuals with business income)")],
    "body": """## Choosing How to Receive Payments

| Channel | Tax record it creates |
| Direct bank wire to a Pakistani account | Bank credit with remittance details and certificate of tax deducted |
| Payoneer or similar, withdrawn to a bank | Wallet statement plus bank credit on withdrawal |
| Exchange companies or informal channels | Weak record; avoid for business income |

A clear bank trail is the single most useful thing for a freelancer's return, because it ties every rupee to a foreign client.

## Freelancers with Local Clients Too

Many freelancers also work for Pakistani clients. That income is not export income and is taxed at normal rates, and the client may deduct tax when paying you. Keep the two streams separate in your records.""",
    "faq": [
        ("Is income from Pakistani clients taxed like foreign freelance income?",
         "No. Work for Pakistani clients is ordinary business income taxed at normal rates, and clients may deduct tax at source."),
    ],
}

PAGES["blogs/how-to-avoid-fbr-notice-pakistan.html"] = {
    "body": """## Respond, Do Not Ignore

If a notice does arrive, the worst response is silence. An unanswered notice usually leads to an order based only on FBR's information, which is harder and more expensive to undo through appeal. Note the compliance date, collect the documents asked for and reply on IRIS before the deadline, or request more time in writing if you need it.""",
    "faq": [
        ("What happens if I ignore an FBR notice?",
         "FBR can pass an order based only on the information it holds, which is harder to undo through appeal than replying on time."),
    ],
}

PAGES["blogs/how-to-become-active-filer-pakistan-2026.html"] = {
    "replace": [("Filing your return late (penalty: Rs. 1,000/day, max Rs. 50,000)", "Filing your return late (a penalty may follow under section 182)"),
                ("Paying the ATL surcharge under Section 182A (Rs. 1,000 for individuals, Rs. 20,000 for companies)",
                 "Paying the ATL surcharge (Rs. 1,000 for individuals, higher for AOPs and companies)"),
                ("to get reinstated on the active list under Section 182A.", "to get reinstated on the active list.")],
    "body": """## Common Reasons a New Filer Does Not Appear on the List

- The return was saved as a draft and never submitted with the PIN.
- The return was filed for the wrong tax year.
- A late return was filed but the ATL surcharge was not paid.
- The CNIC on the bank or registrar's system does not match the IRIS profile.

Check the acknowledgement for the correct tax year and confirm the surcharge payment if you filed late.""",
    "faq": [
        ("I filed my return but I am not on the ATL. Why?",
         "Common reasons are an unsubmitted draft, the wrong tax year, an unpaid ATL surcharge for a late return, or a mismatch in CNIC details."),
    ],
}

PAGES["blogs/how-to-download-ntn-certificate-fbr.html"] = {
    "drop": ["pricing"],
    "body": """## Where the NTN Certificate Is Used

| Situation | Why the certificate is asked for |
| Opening a business bank account | Proof of tax registration |
| Registering as a supplier with a company or government department | Vendor registration |
| Applying for STRN or provincial sales tax registration | Base registration |
| Visa applications | Together with returns, as proof of tax compliance |
| Import or export registration | Needed for customs and trade bodies |

Keep a PDF copy on your phone and update it whenever your address or business details change, because many counterparties check that the certificate details match their records.

NTN registration is Rs 2,000 on our [pricing page](/pricing).""",
    "faq": [
        ("Do I need a new NTN certificate after changing my address?",
         "Update the profile on IRIS and download a fresh certificate, since banks and buyers check that the details match."),
    ],
}

PAGES["blogs/how-to-reset-fbr-iris-password.html"] = {
    "drop": ["iris recovery by kamboh associates"],
    "body": """## Keeping Your IRIS Account Safe

- Use a password you do not use anywhere else.
- Keep your registered mobile number and email address current; you need them for every reset.
- Do not share your password with anyone you do not trust to file for you, and change it after a consultant has filed.
- Log out after using IRIS on a shared computer.

## If Someone Else Changed Your Details

If your registered email or mobile number was changed without your consent, contact FBR's helpline and visit a Regional Tax Office with your CNIC to have the profile restored. Ask for written confirmation once the details are corrected.""",
    "faq": [
        ("What should I do if my IRIS mobile number was changed without permission?",
         "Contact FBR's helpline and visit a Regional Tax Office with your CNIC to restore the profile, and keep written confirmation."),
    ],
}

PAGES["blogs/income-tax-exemptions-pakistan-2026.html"] = {
    "replace": [("Freelancers receiving foreign remittance via banking channel: 0.25% final WHT on remittance (no income tax return liability if remittance is the only income)",
                 "Freelancers exporting IT services through banking channels: reduced tax on proceeds when the conditions are met; a return is still needed to declare the income and stay on the Active Taxpayers List"),
                ("Gratuity received from an approved gratuity fund is exempt up to Rs. 300,000 per year per the Second Schedule. Excess above Rs. 300,000 is taxable as salary income.",
                 "Gratuity from an approved gratuity fund is generally exempt; gratuity from other schemes is exempt only up to limits in the Second Schedule, with the rest taxable as salary."),
                ("15% (filer) or 25% (", "15% (filer) or 30% (")],
    "faq_skip": ["Is freelancer income from Upwork/Fiverr tax-free in Pakistan?"],
    "body": """## Exempt Income Still Belongs in the Return

Exempt income is declared, not ignored. IRIS has separate fields for exempt income, final-tax income and normal income. Declaring exempt amounts lets the wealth reconciliation balance, because money from exempt sources, such as agricultural income, a government pension or an inheritance, often pays for the assets in your wealth statement.""",
    "faq": [
        ("Do I need to show exempt income in my return?",
         "Yes. Exempt income is entered in its own fields so that the wealth reconciliation shows where your money came from."),
    ],
}

PAGES["blogs/income-tax-exemptions-salaried-pakistan.html"] = {
    "drop": ["salaried person tax slabs pakistan 2026"],
    "body": """## Which Slabs Apply to Your Salary

Salaried individuals are taxed on a separate, lower schedule than individuals with business income. The bands are revised in most budgets: for example, the Finance Act 2025 cut the rate on the Rs 600,001 to Rs 1,200,000 band from 5% to 1% for tax year 2026. Because employers recalculate deductions every July, check that your payroll uses the current year's slabs; our [income tax slab guide](/blogs/income-tax-slab-pakistan-2026) explains how to read them.

## Allowances and the Salary Certificate

The salary certificate your employer issues after 30 June shows gross salary, exempt allowances, taxable perquisites and tax deducted. Compare it with your payslips before filing. If the employer treated a component incorrectly, ask for a corrected certificate rather than adjusting figures yourself in the return.""",
    "faq": [
        ("Are salaried slabs the same as business slabs?",
         "No. Salaried individuals have a separate, lower schedule of rates than individuals with business income."),
    ],
}

PAGES["blogs/income-tax-return-filing-pakistan.html"] = {
    "drop": ["income tax slabs pakistan 2026 salaried individuals"],
    "replace": [("Late filing incurs a penalty of Rs. 1,000 per day (minimum Rs. 10,000) and removal from Active Taxpayer List (ATL).",
                 "Late filing can lead to a penalty under section 182, and a late filer reaches the Active Taxpayer List (ATL) only after paying the ATL surcharge.")],
    "faq_skip": ["What happens if I don't file my income tax return in Pakistan?"],
    "body": """## Which Tax Rates Apply

Rates depend on the type of income: salaried individuals, individuals with business income, rent, and final-tax income such as prize bonds each have their own schedule. Our [income tax slab guide](/blogs/income-tax-slab-pakistan-2026) sets out the slab tables and how they changed between tax years. When income comes from more than one source, each part is taxed under its own rules and then combined in the return.""",
    "faq": [
        ("What happens if I do not file my return?",
         "You stay off the Active Taxpayers List, pay higher withholding on many transactions, and may receive notices, penalties and assessments based on FBR's data."),
    ],
}

PAGES["blogs/income-tax-slab-pakistan-2026.html"] = {
    "replace": [("— Tax Year 2026</h2>", "— Tax Year 2025 Rates</h2>"),
                ("from 2.5% up to 35%", "up to 35%"),
                ("Gratuity up to Rs. 300,000 (approved gratuity fund)", "Gratuity from an approved fund, within Second Schedule limits")],
    "faq_skip": ["What tax slab applies to freelancers in Pakistan?"],
    "body": """## What Changed for Tax Year 2026

The slab tables above show the rates set by the Finance Act 2024 for tax year 2025. The Finance Act 2025 revised them for tax year 2026 (1 July 2025 to 30 June 2026). The best-known change for salaried taxpayers was the cut on the Rs 600,001 to Rs 1,200,000 band from 5% to 1%, with reductions on several higher bands as well. Before filing your return due on 30 September 2026, confirm the full tax year 2026 table on FBR's website or with us, because using the older table will overstate the tax on most salaries.

## Reading a Slab Table Correctly

Each band shows a fixed amount plus a percentage of income above the band's lower limit. Tax is not charged at the top rate on your whole income. Find the band your total taxable income falls into, take the fixed amount and add the percentage on the excess.""",
    "faq": [
        ("Are the tax year 2025 slabs used for returns due in September 2026?",
         "No. Returns due on 30 September 2026 are for tax year 2026, which uses the revised slabs from the Finance Act 2025."),
        ("How do freelancers find the right slab?",
         "Freelancers usually have business income and use the non-salaried slabs, unless their IT export income is taxed under the reduced regime on proceeds."),
    ],
}

PAGES["blogs/minimum-tax-section-113-pakistan.html"] = {
    "drop": ["who does minimum tax apply to?"],
    "replace": [("1.5%", "1.25%"), ("Rs. 750,000", "Rs. 625,000")],
    "body": """## Who Section 113 Covers

| Taxpayer | Position |
| Resident companies | Covered |
| AOPs above the turnover threshold | Covered |
| Individuals with business turnover above the threshold | Covered |
| Specific sectors such as distributors, oil marketing and some retailers | Covered at sector-specific rates |
| Persons exempted under the Second Schedule or special zones | Excluded, subject to conditions |

The general rate is 1.25% of turnover, with lower or different rates for specified sectors in the First Schedule. The thresholds and sector rates change with budgets, so check them for each tax year.""",
    "faq": [
        ("What is the general minimum tax rate under section 113?",
         "The general rate is 1.25% of turnover, with different rates for specified sectors under the First Schedule."),
    ],
}

PAGES["blogs/non-filer-consequences-pakistan-2026.html"] = {
    "drop": ["financial consequences — higher withholding tax rates", "legal penalties for non-filing"],
    "replace": [("double WHT (6% vs 3%) — a Rs. 50 lakh plot costs Rs. 3 lakh extra in WHT alone",
                 "double advance tax (2.5% vs 1.25% for transfers from 1 July 2026) — a Rs. 50 lakh plot costs Rs. 62,500 extra in advance tax alone"),
                ("charges triple the registration tax", "charges a much higher advance tax"),
                ("From Rs. 15,000", "From Rs. 5,000")],
    "faq_skip": ["If I file now for previous years, will FBR penalize me?"],
    "body": """## Higher Withholding in Numbers

| Transaction | On the Active Taxpayers List | Not on the list |
| Buying property (236K, from 1 July 2026) | 1.25% | 2.5% |
| Selling property (236C, from 1 July 2026) | 2.75% | 5.5% |
| Prize bond winnings | 15% | 30% |
| Lottery and similar prizes | 20% | 40% |

Rates on bank profit, dividends, vehicles and cash withdrawals also differ by status and change in each budget.

## Legal Exposure

A person who does not file when required can face a penalty under section 182, a best-judgment assessment of income under section 121 based on FBR's data, and in serious cases of wilful concealment, prosecution. Filing late stops these from growing and is almost always better than continuing not to file.""",
    "faq": [
        ("Will FBR penalise me if I file past years now?",
         "A late-filing penalty may be imposed under section 182, but filing late stops further exposure, restores your ATL status after the surcharge, and prevents a best-judgment assessment."),
    ],
}

PAGES["blogs/private-limited-company-tax-return-pakistan.html"] = {
    "drop": ["pricing", "penalties for late filing by a private limited company"],
    "replace": [("From Rs 20,000", "From Rs 18,000")],
    "body": """## If a Company Return Is Late

A company that misses its filing date can face a penalty under section 182 and default surcharge on any unpaid tax under section 205, at a KIBOR-linked rate. The penalty is imposed through an order after a notice, so a documented reason for the delay can be put forward. Directors should also remember that SECP filings, such as the annual return and audited accounts, have their own deadlines and penalties.

## Fees

Corporate returns start from Rs 18,000, NTN registration is Rs 2,000 and withholding statements are Rs 2,500 per month on our [pricing page](/pricing).""",
    "faq": [
        ("Is a company late-filing penalty automatic?",
         "It is imposed through a notice and an order under section 182, giving the company a chance to explain the delay."),
    ],
}

PAGES["blogs/sales-tax-registration-guide-pakistan.html"] = {
    "body": """## After the STRN Is Issued

The first month after registration matters most. Set up invoice numbering that includes your STRN and the buyer's details, register your business bank account in the sales tax profile, and file the first monthly return even if you made no sales. Missing the first return is a common reason new registrations are suspended.""",
    "faq": [
        ("Do I file a sales tax return in my first month even without sales?",
         "Yes. A return is due every month from registration, including nil returns when there were no sales."),
    ],
}

PAGES["blogs/sales-tax-return-filing-pakistan-2026.html"] = {
    "drop": ["sales tax rates pakistan 2026"],
    "faq_skip": ["What is the standard sales tax rate in Pakistan 2026?"],
    "body": """## Rates in Brief

The standard federal sales tax rate on goods is 18%. Some goods carry reduced rates or are exempt under the Sixth and Eighth Schedules to the Sales Tax Act, and exports are zero-rated. These schedules change in almost every budget, so we check the item's current treatment by its tariff heading before invoicing. Services are taxed separately by the provinces.""",
    "faq": [
        ("What is the standard sales tax rate on goods in 2026?",
         "18%, with reduced rates and exemptions for specific goods under the Sales Tax Act schedules, and zero-rating for exports."),
    ],
}

PAGES["blogs/tax-planning-tips-pakistan-2026.html"] = {
    "replace": [("A property sold before 1 year: 15% CGT. Same property after 6 years: 0% CGT. If you are planning to sell, holding slightly longer can eliminate CGT entirely on plots (6 years) and constructed property (4 years).",
                 "For property acquired between July 2022 and June 2024, the rate falls each year of holding and reaches nil after six years, so timing a sale can matter. Property acquired from July 2024 is generally taxed at a flat rate, so holding longer no longer reduces the rate.")],
    "body": """## Planning Around Filer Status

The simplest plan is to be on the Active Taxpayers List before any large transaction. From 1 July 2026, a Rs 2 crore property purchase carries advance tax of Rs 250,000 for a filer and Rs 500,000 for a non-filer. File by 30 September and confirm your status before signing.""",
    "faq": [
        ("Does holding property longer still reduce capital gains tax?",
         "Only for property acquired before July 2024. Property acquired from July 2024 is generally taxed at a flat rate regardless of holding period."),
    ],
}

PAGES["blogs/tax-refund-pakistan-2026.html"] = {
    "body": """## Refund Claims Have a Time Limit

A refund must generally be claimed within the period set in the law after the tax year or the date the tax was paid, whichever is later. Old excess deductions that were never claimed can be lost. If you have several years of salary or bank deductions that exceeded your liability, file the missing returns and claims together before the limit passes.""",
    "faq": [
        ("Is there a deadline for claiming an income tax refund?",
         "Yes. Refunds must be claimed within the period set in the law, so old unclaimed excess deductions can be lost."),
    ],
}

PAGES["blogs/types-of-fbr-notices-pakistan.html"] = {
    "body": """## Reading a Notice Before Replying

Every notice states the section it is issued under, the tax year, the information required and the compliance date. Start with these four points. The section tells you what kind of proceeding it is: section 114 asks for a return, 116 for a wealth statement, 122 proposes amending an assessment, 176 asks for information, 177 starts an audit and 111 questions the source of an amount. The reply should answer exactly what was asked, with documents, and be filed through IRIS before the compliance date.""",
    "faq": [
        ("What should I check first in an FBR notice?",
         "The section, the tax year, the information requested and the compliance date. These decide what the reply must contain and when it is due."),
    ],
}

PAGES["blogs/wealth-statement-guide-pakistan-2026.html"] = {
    "body": """## Liabilities Count Too

The wealth statement also lists what you owe: bank loans, car financing, credit card balances and personal loans from relatives. A liability explains how an asset was paid for when income alone does not. A personal loan should be supported by a written acknowledgement and, ideally, a bank transfer, because cash loans from relatives are a common point of challenge.""",
    "faq": [
        ("Should I show a loan from a relative in my wealth statement?",
         "Yes, as a liability, supported by a written acknowledgement and preferably a bank transfer record."),
    ],
}

PAGES["blogs/wht-on-dividends-pakistan-2026.html"] = {
    "drop": ["withholding tax rates pakistan 2026", "how to claim wht credit"],
    "body": """## Dividends from Mutual Funds and REITs

Dividends from mutual funds and real estate investment trusts are also subject to withholding under section 150, but the rate can differ from that on ordinary company dividends, depending on the type of fund and how much of its income comes from capital gains or debt. Check the tax shown on each dividend advice rather than assuming the standard company rate.

## Where Dividends Go in the Return

Dividend income taxed as final tax is entered in the final-tax section of the return, together with the tax deducted. It does not change your tax on other income, but it does count in the wealth reconciliation as money received during the year.""",
    "faq": [
        ("Are mutual fund dividends taxed at the same rate as company dividends?",
         "Not always. The rate under section 150 can depend on the type of fund and the source of its income."),
    ],
}

PAGES["blogs/wht-rate-filer-non-filer-pakistan.html"] = {
    "drop": ["the real annual cost of being a non-filer", "withholding tax rates pakistan 2026"],
    "body": """## The Annual Cost of Being a Non-Filer

Consider a family that, in one year, buys a Rs 1 crore house and wins Rs 500,000 on a prize bond. For transfers from 1 July 2026:

| Transaction | On the Active Taxpayers List | Not on the list |
| Advance tax on the house (236K) | Rs 125,000 | Rs 250,000 |
| Tax on the prize bond win | Rs 75,000 | Rs 150,000 |
| Total | Rs 200,000 | Rs 400,000 |

The non-filer pays Rs 200,000 more on just two transactions, before counting higher deductions on bank profit, dividends and vehicle registration. Because a non-filer does not file, much of that extra is also never adjusted or refunded.""",
    "faq": [
        ("How much more does a non-filer pay on a Rs 1 crore house?",
         "For transfers from 1 July 2026, Rs 250,000 in advance tax under section 236K against Rs 125,000 for a person on the Active Taxpayers List."),
    ],
}

PAGES["blogs/withholding-agent-responsibilities-pakistan.html"] = {
    "drop": ["withholding tax rates pakistan 2026", "how to claim wht credit"],
    "body": """## Issuing Certificates to Payees

A withholding agent must give each payee a certificate of tax deducted, showing the amount paid, the tax deducted and the date of deposit. Payees need these to claim credit in their returns, and FBR matches the certificates with the agent's withholding statements. Late or missing certificates are a common source of disputes with suppliers and employees.

## Keeping the Agent's Own Records

- Payment vouchers showing gross amount, tax deducted and net paid.
- Copies of PSIDs and bank confirmation of each deposit.
- Payees' NTN or CNIC and their status on the Active Taxpayers List on the payment date.
- Filed withholding statements and their acknowledgements.

Monthly withholding statements are Rs 2,500 per month on our [pricing page](/pricing).""",
    "faq": [
        ("Must a withholding agent give certificates to payees?",
         "Yes. Each payee should receive a certificate showing the payment, tax deducted and deposit date, so they can claim the credit."),
    ],
}

PAGES["blogs/withholding-tax-agent-registration-pakistan.html"] = {
    "drop": ["common wht rates for businesses 2026", "pricing"],
    "faq_skip": ["When must I deduct WHT on service payments?"],
    "body": """## Finding the Right Rate for Each Payment

Rates for services, goods, contracts and rent are set in the First Schedule and differ by the payee's status, the type of payee and the nature of the payment. They also change with each budget. Before setting up your payment system, take the rates from FBR's Withholding Tax Regime Card for the current tax year and check each supplier's status on the Active Taxpayers List on the payment date.

## Fees

Monthly withholding statement filing is Rs 2,500 per month on our [pricing page](/pricing).""",
    "faq": [
        ("Where can a business find current withholding rates?",
         "In FBR's Withholding Tax Regime Card for the tax year, which lists sections, rates and responsibilities after each Finance Act."),
    ],
}
