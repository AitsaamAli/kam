"""Root-level digital business and freelancer guides.

Besides the shared filler, these pages claimed a "100% income tax exemption under SRO 1125(I)/2023" for IT
exports while also quoting the reduced 0.25% regime, and fixed 1%/2% remittance rates under section 231AA.
Neither could be verified, so the claims are reworded to the hedged position the project rules require.
"""

FIXES = [
    (r"the SRO 1125\(I\)/2023 export exemption", "the reduced tax treatment for IT exports"),
    (r"SRO 1125\(I\)/2023 IT export (?:tax )?exemption", "reduced tax treatment for IT exports"),
    (r"Under SRO 1125\(I\)/2023,? ", "Under the IT export rules, "),
    (r"under SRO 1125\(I\)/2023", "under the IT export rules"),
    (r"FBR's interpretation of SRO 1125", "FBR's interpretation of the IT export rules"),
    (r"for SRO 1125 IT export exemption", "for the IT export tax treatment"),
    (r"SRO 1125(?:\(I\)/2023)?", "the IT export rules"),
    (r'"Taxable but exempt" is the correct description for most Pakistani Upwork income\.',
     "Confirm the current treatment for your tax year before filing."),
    (r"is 100% income tax <strong>exempt</strong>", "is taxed through a reduced deduction on proceeds"),
    (r"making it 100% income tax exempt", "limiting the tax to a reduced deduction on proceeds"),
    (r"&mdash; 100% income tax exempt", "&mdash; taxed through a reduced deduction on proceeds"),
    (r"(are|is|be) 100% (?:income )?tax exempt", r"\1 taxed only through a reduced deduction on proceeds"),
    (r"(?:the |a )?100% income tax exemption", "the reduced IT export tax treatment"),
    (r"100% exempt from income tax", "taxed only through a reduced deduction on proceeds"),
    (r"(?:May qualify for )?100% IT export exemption", "May qualify for the reduced IT export treatment"),
    (r"is exempt from income tax\. Complete conditions", "is taxed under a reduced regime when the conditions are met. Typical conditions"),
    (r"you owe Rs\. 0 income tax on it", "your tax is limited to the reduced deduction on proceeds"),
    (r"Claim IT export exemption &mdash; Rs\. 0 tax", "Claim the IT export treatment &mdash; tax limited to the reduced deduction"),
    (r"ke thet 100% income tax exempt ho sakta hai", "ke tehet sirf kam shuda deduction par tax ho sakta hai"),
    (r"100% income tax exempt", "taxed through a reduced deduction on proceeds"),
    (r"IT [Ee]xport (?:[Tt]ax )?[Ee]xemption", "IT export tax treatment"),
    (r"it export exemption", "it export tax treatment"),
    (r"it-export-exemption", "it-export-tax-treatment"),
    (r" ?\(Section 231AA\)", ""),
    (r"under Section 231AA of the Income Tax Ordinance", "under the Income Tax Ordinance"),
    (r" under (?:Section |S\.)\s?231AA", ""),
    (r"deducts 1% WHT \(filer\) or 2% \(non-filer\)", "deducts tax at a rate that depends on your registration and filer status"),
    (r"deducts WHT at 1% \(filer\) or 2% \(non-filer\)", "deducts tax at a rate that depends on your registration and filer status"),
    (r"Bank deducts 1% WHT \(filer\) / 2% \(non-filer\)", "Bank deducts tax at the applicable rate"),
    (r"1% filer vs 2% non-filer on bank credits", "Lower deduction on bank credits for filers"),
    (r"\(1% filer vs 2% non-filer\)", "(lower for filers)"),
    (r"the 1% WHT rate applied", "the filer rate applied"),
    (r"Bank applies 1% rate", "Bank applies the filer rate"),
    (r"WHT From 2% → 1%", "Lower WHT as a filer"),
    (r"(?<![\w.])1% WHT on remittance receipt", "Lower filer rate on remittance receipt"),
    (r"(?<![\w.])2% WHT on remittance receipt", "Higher non-filer rate on remittance receipt"),
    (r"If you claim IT export tax treatment, this 1% WHT becomes a refundable credit",
     "How this deduction is treated depends on the IT export rules for the tax year"),
    (r"lower withholding tax rates \(1% vs 2%\)", "lower withholding tax rates"),
    (r" from 2% to 1%", ""),
    (r"</strong> 1% of amount received", "</strong> lower filer rate"),
    (r"</strong> 2% of amount received", "</strong> higher non-filer rate"),
    (r"you get 1% back instead of having 2% permanently deducted", "your deduction can be adjusted or refunded instead of being lost"),
    (r"Non-filers pay 2x the WHT rate", "Non-filers pay a higher rate"),
    (r"8-14\.5% WHT", "withholding at the rates for services"),
    (r">7% deducted at source", ">Filer rate deducted at source"),
    (r">14% deducted at source", ">Higher non-filer rate deducted at source"),
    (r"\(6% on services\)", "(at the rate for services)"),
    (r"SRA/SRBA \(Sindh/Balochistan\)", "SRB or BRA (Sindh/Balochistan)"),
    (r"charge 16% sales tax on invoices", "charge provincial sales tax (16% in Punjab, 15% in Sindh) on invoices"),
    (r"Rs\. 370/month employer contribution per employee", "employer contribution of 5% of the minimum wage per employee"),
    (r"20% on first \$500 with a client", "Upwork has changed its freelancer fee structure several times; check the fee shown on each contract"),
    (r"<li>\s*10% on \$500\.01 &ndash; \$10,000 with a client\s*</li>", ""),
    (r"ke thet", "ke tehet"),
    (r"<li>\s*5% on billings above \$10,000 with a client\s*</li>", ""),
]

# wording fixes that depend on the replacements above having run
FIXES += [
    (r"which makes qualifying income taxed through a reduced deduction on proceeds\. This means you declare it, but your tax is limited to the reduced deduction on proceeds\. The exemption is a massive benefit that most Fiverr sellers don't even know they're entitled to\.",
     "which limits the tax on qualifying income to a reduced deduction on proceeds when the conditions are met. You still declare the income in your return."),
    (r"IT export tax treatment under the IT export rules applies to", "The IT export tax treatment applies to"),
    (r" \(zero tax due\)", ""),
    (r"making the income taxed through a reduced deduction on proceeds", "so the tax is limited to a reduced deduction on proceeds"),
    (r"to income tax ZERO hoga IT export tax treatment ke (?:thet|tehet)\. Bank 1% WHT kaatega jo refundable hai annual return mein\.",
     "to IT export tax treatment ke tehet tax kam shuda deduction tak mehdood ho sakta hai. Bank jo tax kaatega woh annual return mein dikhaya jata hai."),
    (r"apply 1% \(filer\) vs 2% \(non-filer\) WHT rate", "apply the lower filer WHT rate"),
    (r"claim IT export tax treatments", "claim IT export tax treatment"),
    (r"\(tax free if conditions met\)", "(reduced tax if conditions are met)"),
    (r"the bank deducts 1% WHT if you are a filer, or 2% if non-filer", "the bank deducts tax at a rate that is lower for filers"),
    (r"so you pay 1% WHT from day one", "so the lower filer rate applies as early as possible"),
    (r"Coaching income ka tax zero ya minimum karwao\.", "Coaching income ka tax sahi aur kam se kam qanooni tareeqe se."),
    (r"International clients ka tax zero karo\.", "International clients ki income ka sahi tax treatment."),
    (r"Banks 1% WHT deduct karte hain filers ke liye aur 2% non-filers ke liye", "Banks filers ke liye kam aur non-filers ke liye zyada rate par WHT deduct karte hain"),
    (r"triggers 1% WHT \(filer\) or 2% \(non-filer\)", "triggers withholding at a rate that is lower for filers"),
]

PAGES = {}


def page(body, faq, **extra):
    return {"body": body, "faq": faq, "regex": FIXES, **extra}


PAGES["amazon-fba-tax-pakistan.html"] = page("""## Which Slab Table Applies to FBA Profit

FBA profit is business income, so it is taxed at the slab rates for individuals with business income, which are higher than the salaried slabs and are revised in most budgets. Use the table for the tax year you are filing, not the year you started selling. If profits grow large, compare the slab tax with the 29% corporate rate plus dividend tax before incorporating.

## Inventory at Year End

Stock sitting in Amazon warehouses on 30 June is still your asset. Value it at cost in the wealth statement and deduct only the cost of units actually sold during the year from your income. Amazon's inventory reports by date make this straightforward.""",
    [("Is unsold FBA inventory declared in the wealth statement?",
      "Yes. Stock held in Amazon warehouses on 30 June is your asset and is shown at cost.")],
    drop=["income tax slab rates for fy 2025-26"])

PAGES["creator-economy-tax-pakistan.html"] = page("""## Mixed Income Is the Norm for Creators

Most Pakistani creators earn from several sources at once: AdSense, brand deals with local companies, affiliate commissions and digital product sales. Each has a different tax point. Local brand payments usually have tax deducted by the brand; foreign platform payouts arrive through banks with their own deduction; product sales may need provincial or federal sales tax registration once they grow. Keep one spreadsheet with a column per source and match each month to your bank statement.""",
    [("Do creators pay the same tax on local brand deals and AdSense?",
      "No. Local brand payments are taxed as service income with tax deducted by the brand, while foreign payouts follow the rules for foreign receipts and IT exports.")])

PAGES["crypto-tax-rules-pakistan-2026.html"] = page("""## Keeping a Crypto Ledger

Because exchanges do not issue Pakistani tax certificates, your own records are the evidence. For each transaction note the date, the coin, quantity, price in rupees on that date, the wallet or exchange used and what the transaction was: purchase, sale, swap, payment received or transfer between your own wallets. Transfers between your own wallets are not sales, but they must be traceable so a later disposal can be matched to its cost.""",
    [("Is moving crypto between my own wallets a taxable sale?",
      "No, but record it so that later sales can be matched to their original cost.")])

PAGES["digital-agency-compliance-pakistan.html"] = page("""## Agency Growth Stages and Registrations

| Stage | Registrations usually needed |
| Freelancer working alone | NTN and annual return |
| Small team billing foreign clients | NTN, PSEB registration, withholding on staff salaries |
| Billing Pakistani companies | Provincial sales tax registration (PRA, SRB, KPRA or BRA) |
| Hiring 5+ staff or seeking investment | Consider a private limited company, EOBI registration |

Planning each step before it is needed avoids back-dated registrations and penalties.""",
    [("When does a digital agency need provincial sales tax registration?",
      "When it provides taxable services, such as advertising or IT services, to clients in Pakistan above the provincial threshold.")])

PAGES["dropshipping-tax-pakistan.html"] = page("""## How Dropshipping Profit Is Taxed

Dropshipping profit is business income taxed at the slab rates for individuals with business income, or at the corporate rate if you trade through a company. The slab table is revised in most budgets, so use the one for the tax year you are filing. Because dropshipping sells physical goods rather than IT services, the reduced regime for IT exports does not normally apply.

## Advertising Spend Is Your Biggest Deduction

Facebook, Google and TikTok ad spend is usually the largest expense in a dropshipping store. Download monthly ad invoices from each platform and keep the card or bank statement showing payment. Without invoices, ad spend is the first expense FBR disallows.""",
    [("Can dropshippers deduct Facebook ad spend?",
      "Yes, as a business expense, supported by the platform's invoices and the payment record.")],
    drop=["income tax rates for dropshipping profit"])

PAGES["fiverr-tax-guide-pakistan.html"] = page("""## Keeping Fiverr Records Audit-Ready

Download the Fiverr earnings report for each tax year (1 July to 30 June), the Payoneer or bank withdrawal statement, and the bank's certificate of tax deducted. Together these three documents show the full path from order to rupees. Keep them for at least six years. If a buyer requests an invoice, issue it in your own name with your NTN so the record matches your return.""",
    [("Which Fiverr documents should I keep for FBR?",
      "The yearly earnings report, the Payoneer or bank withdrawal statement and the bank's certificate of tax deducted, kept for at least six years.")])

PAGES["freelancer-ntn-registration-pakistan.html"] = page("""## After You Get Your NTN

Registration alone does not put you on the Active Taxpayers List. You must file a return for the tax year. If you register in, say, January, file the return for the tax year that ended the previous 30 June if you had income then, and the current year's return by the next 30 September. Then give your bank your NTN so the lower filer rates apply to future receipts.""",
    [("Does getting an NTN make me a filer?",
      "No. You appear on the Active Taxpayers List only after filing a return for the relevant tax year.")])

PAGES["freelancer-wealth-statement-guide.html"] = page("""## Foreign Balances and Equipment

Freelancers often forget two items. First, balances held abroad on 30 June, such as Payoneer, Wise or PayPal wallets, are assets and must be declared, converted at the applicable rate. Second, work equipment bought from freelance income, including laptops, cameras and phones, belongs in the wealth statement at cost. Both are easy to explain when declared and suspicious when they appear later without a record.""",
    [("Do I declare my Payoneer balance in the wealth statement?",
      "Yes. Foreign wallet balances on 30 June are assets and are declared at the converted rupee value.")])

PAGES["influencer-tax-guide-pakistan.html"] = page("""## Contracts with Brands

A short written agreement with each brand protects both sides. It should state the fee, deliverables, payment date, whether the fee includes provincial sales tax, and that the brand will issue a tax deduction certificate. Influencers who skip this step often find that tax was deducted at the higher non-filer rate or not reported against their CNIC at all.""",
    [("Why should I sign a contract with a brand for a sponsored post?",
      "It fixes the fee, deliverables and tax treatment, and ensures you receive a tax deduction certificate in your name.")])

PAGES["nft-tax-pakistan-2026.html"] = page("""## Valuing NFT Income in Rupees

NFT sales and royalties are usually paid in cryptocurrency. For tax purposes, convert each receipt to rupees at the market value on the date received and keep a screenshot or exchange record of that price. Later movement in the coin's value is a separate gain or loss when you sell or convert it, not part of the original NFT income.""",
    [("How do I convert NFT income paid in ETH to rupees?",
      "Use the market value on the date you received it, with a record of the price, and treat later changes in the coin's value separately.")])

PAGES["online-coaching-business-tax-pakistan.html"] = page("""## Pakistani and Foreign Clients Together

Coaches often have both. Income from Pakistani clients is ordinary business income, and corporate clients may deduct tax when paying. Income from foreign clients received through banks follows the rules for foreign receipts. Invoice each client separately and keep the two streams apart in your records, because the tax treatment and the documents needed differ.""",
    [("Is coaching income from Pakistani clients taxed differently?",
      "Yes. It is ordinary business income, and corporate clients may deduct tax at source, while foreign receipts follow different rules.")])

PAGES["online-course-creator-tax-pakistan.html"] = page("""## Platform Payouts and Records

Udemy, Teachable and similar platforms issue monthly payout statements that show gross sales, platform share, refunds and the net paid to you. Keep these with the matching bank credits. Refunds and chargebacks reduce your income only in the period they are deducted, so the statements are needed to show the correct figure for each tax year.""",
    [("Do course refunds reduce my taxable income?",
      "Yes, in the period the platform deducts them, as shown in its payout statements.")])

PAGES["remote-worker-tax-guide-pakistan.html"] = page("""## Employment Contract Wording Matters

Whether you are treated as a foreign employee or an independent contractor depends on your contract and how you are paid. An employment contract with a foreign company, payslips and fixed monthly salary point to salary income; invoices, variable payments and multiple clients point to business income. The classification affects which slab table applies and what records FBR expects, so keep the contract with your tax papers.""",
    [("Am I a remote employee or a contractor for tax?",
      "It depends on your contract and payment pattern: payslips and fixed salary suggest employment; invoices and multiple clients suggest business income.")])

PAGES["saas-company-tax-pakistan.html"] = page("""## Recognising Annual Subscriptions

Many SaaS businesses sell annual plans paid upfront. For accounts prepared on the accrual basis, revenue is spread over the months of service, so a plan sold in May belongs mostly to the next tax year. Small founders using cash-basis records should be consistent from year to year. Whichever method you use, state it clearly in your accounts and apply it every year.""",
    [("How is an annual SaaS subscription paid upfront treated?",
      "On an accrual basis it is spread over the months of service; whatever method you use should be applied consistently each year.")])

PAGES["shopify-business-registration-pakistan.html"] = page("""## Selling to Pakistani Customers Through Couriers

When Pakistani customers pay cash on delivery, the courier collects the money and remits it to you, and since the 2025-26 budget tax is collected on these online sales: 1% on digital payments and 2% on cash on delivery. These amounts are advance payments. Keep the courier's and payment gateway's statements to claim them in your return.""",
    [("Is tax deducted on Shopify cash-on-delivery orders in Pakistan?",
      "Yes. Since the 2025-26 budget, tax is collected on online sales: 1% on digital payments and 2% on cash on delivery, adjustable in your return.")])

PAGES["stripe-income-tax-pakistan.html"] = page("""## Currency and Timing of Stripe Payouts

Stripe pays out in batches, often several days after a customer pays, and an overseas LLC account adds a further transfer to Pakistan. For your Pakistani return, record income when it is earned or received according to your method, and convert at the rate on the relevant date. Keep Stripe's monthly payout reports alongside the LLC and Pakistani bank statements so each rupee can be traced to customer payments.""",
    [("Which documents prove Stripe income for FBR?",
      "Stripe's monthly payout reports, the LLC or foreign bank statements, and the Pakistani bank credits for the transfers home.")])

PAGES["subscription-business-tax-pakistan.html"] = page("""## Churn, Refunds and Failed Payments

Subscription revenue is rarely the same as the amount charged. Refunds, failed renewals and chargebacks reduce what you actually earn. Use your billing platform's reports to show net revenue for each month and keep them with the bank statements. This also explains why bank credits differ from the headline subscription numbers.""",
    [("Why do my bank credits differ from my subscription revenue?",
      "Refunds, failed payments, chargebacks and platform fees reduce the amount paid out; billing reports explain the difference.")])

PAGES["tax-for-ai-agencies-pakistan.html"] = page("""## Paying for AI Tools from Pakistan

AI agencies pay for API usage, model subscriptions and cloud hosting in dollars, usually by card. Banks may apply advance tax on foreign card payments, which is adjustable if you file. Download the monthly invoices from each provider; API usage invoices are often only available inside the provider's dashboard and disappear after a period.""",
    [("Can an AI agency deduct API and cloud costs?",
      "Yes, as business expenses, supported by the providers' invoices and card or bank statements.")])

PAGES["tax-for-automation-businesses-pakistan.html"] = page("""## Retainers Versus Project Fees

Automation agencies often combine one-off build fees with monthly maintenance retainers. Invoice them separately. Build fees are earned when the project is delivered; retainers are earned month by month. Separate invoices make it easy to show the right income in each tax year and to explain recurring bank credits from the same client.""",
    [("Should automation build fees and retainers be invoiced separately?",
      "Yes. It shows clearly when each type of income was earned and explains recurring payments.")])

PAGES["tax-on-international-clients-pakistan.html"] = page("""## Contracts and Invoices for Foreign Clients

Every foreign engagement should have a contract or accepted proposal, and each payment should match an invoice that shows your name, NTN, the client's name and country, the service and the amount in foreign currency. Banks increasingly ask for invoices before crediting foreign receipts, and FBR uses the same documents to accept the receipt as export income.""",
    [("What should an invoice to a foreign client show?",
      "Your name and NTN, the client's name and country, the service, the date and the amount in foreign currency.")])

PAGES["uae-remote-job-tax-pakistan.html"] = page("""## Moving Between Dubai and Pakistan During the Year

People who split the year between the UAE and Pakistan must count days carefully, because residence is decided per tax year (1 July to 30 June), not per calendar year. Keep a simple log of entry and exit dates with passport stamps or airline records. A few days either side of the threshold can change whether your UAE salary is taxable in Pakistan.""",
    [("How do I prove days spent outside Pakistan?",
      "Keep passport stamps, airline tickets or an immigration travel history covering the tax year.")])

PAGES["upwork-tax-guide-pakistan.html"] = page("""## Upwork Fees and Your Income Figure

Upwork's freelancer fee has changed several times, and the current fee is shown on each contract and in your transaction history. Declare either the gross billing with fees as an expense, or the net amount after fees, but use the same method every year. Upwork's annual earnings report and transaction history are the best evidence for either approach.""",
    [("Should I declare Upwork income before or after fees?",
      "Either gross with fees as an expense or net after fees, as long as you use the same method every year and keep the transaction history.")],
    faq_skip=["What is the Upwork service fee and is it deductible?"])

PAGES["wise-business-account-tax-pakistan.html"] = page("""## Wise Balances and Conversions

Money held in Wise in dollars, pounds or euros on 30 June is a foreign asset for the wealth statement. Conversions inside Wise from one currency to another are not income, but the rupee value of the balance changes with exchange rates. Download the Wise statement for 30 June each year and keep it with your return.""",
    [("Is my Wise balance on 30 June declared in the wealth statement?",
      "Yes. Foreign currency held in Wise on 30 June is an asset, declared at its rupee value.")])
