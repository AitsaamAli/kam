"""Provincial, overseas, filing-process and freelancer guides that shared the same padded template."""

PAGES = {}

PAGES["blogs/kpk-income-tax-guide-2026.html"] = {
    "body": """## Three Tax Authorities a Peshawar Business May Deal With

A trader or service provider in Khyber Pakhtunkhwa can owe tax to three different bodies in the same year, and none of them shares your compliance record with the others:

| Authority | What it taxes | Typical KP taxpayer |
| FBR | Income tax, federal sales tax on goods, customs | Every filer, manufacturers, importers |
| KPRA | Sales tax on services under the province's own law | Consultants, contractors, restaurants, courier and IT firms |
| KP Excise and Taxation | Urban property tax, motor vehicle tax, professional tax | Property owners, vehicle owners, professionals |

Keeping all three current is what protects you. A clean FBR record does nothing if KPRA has you down as an unregistered contractor.

## Merged Districts: Check Before You Assume

Businesses in Khyber, Bajaur, Mohmand and the other merged districts received exemptions from several federal and provincial taxes after the 2018 merger. Those concessions came with end dates, and successive budgets have extended, narrowed or ended parts of them. A supplier in Bara or Landi Kotal selling into Peshawar should therefore check the current position for each tax separately before quoting prices, because buyers in settled districts may already be deducting tax on those purchases.

## Peshawar's Trading Markets

Karkhano Market, Board Bazaar and the wholesale markets of the old city run largely on cash and credit. For income tax, the problem is rarely the rate; it is proof. When a trader buys a plot in Hayatabad or a car, FBR sees the transaction and asks where the money came from. A basic year-end stock list and a cash book let us show business profit as the source rather than leaving it unexplained.

## Families with Members in the Gulf

A large share of KP households receive remittances from Saudi Arabia, the UAE and Qatar. The money itself is not the receiver's taxable income when it comes through banks, but the houses and land it pays for must appear in the wealth statement. Keep the bank advice for every transfer used to buy property.""",
    "faq": [
        ("Is KPRA registration needed if I already file with FBR?",
         "Yes, if you provide services that are taxable under Khyber Pakhtunkhwa's sales tax on services law. FBR filing and KPRA registration are separate obligations."),
        ("Are businesses in the merged districts still exempt?",
         "Some concessions applied after the merger, but they had time limits and have been changed in later budgets. Check the current status for each tax before relying on an exemption."),
        ("Does KP professional tax replace income tax?",
         "No. Professional tax is a small provincial levy on certain professions and businesses. Income tax with FBR still applies in full."),
    ],
}

PAGES["blogs/sindh-income-tax-guide-2026.html"] = {
    "replace": [("SRA (Sindh Revenue Authority)", "SRB (Sindh Revenue Board)"),
                ("Sindh Revenue Authority (SRA)", "Sindh Revenue Board (SRB)"),
                ("SRA", "SRB")],
    "body": """## Sindh-Only Levies Karachi Businesses Overlook

Apart from SRB sales tax on services, Sindh charges levies that have no equivalent in Punjab's tax calendar:

- **Sindh Infrastructure Cess** on goods entering or leaving the province through Karachi's ports, collected by the Excise, Taxation and Narcotics Control department. Importers see it alongside customs clearance.
- **Professional tax**, a fixed annual charge on many traders, professionals and companies, depending on the category.
- **Urban immovable property tax** on houses, flats and commercial units in Karachi, Hyderabad and other towns.
- **Sindh agricultural income tax** on farm income from land in the province.

None of these appear in your FBR return, and paying them does not reduce federal income tax.

## Karachi's Size Changes How FBR Works with You

Most large companies, banks and multinationals are handled by FBR's Large Taxpayers Office in Karachi, while individuals and smaller businesses fall under the Regional Tax Offices. If you supply services to a large Karachi company, it will deduct income tax from your invoices and also ask for your SRB registration, because it needs both to claim its own input tax and expenses. Not being registered often means losing the contract rather than just paying more tax.

## Hyderabad, Sukkur and Interior Sindh

Outside Karachi the mix shifts towards traders, rice and sugar businesses, transporters and landowners. Agricultural income is a provincial matter, but the rice mill, the transport company and the commission agent are federal income taxpayers. Many interior Sindh businesses also deal with SRB for the first time when a large buyer insists on registered suppliers.

## Practical Order of Registrations

For a new Sindh service business we usually recommend this order: NTN with FBR, SRB registration if the service is taxable, then professional tax enrolment. Doing it in this order means each registration uses the same business name and address, which avoids mismatches later.""",
    "faq": [
        ("Is SRB the same as FBR?",
         "No. The Sindh Revenue Board collects sales tax on services in Sindh. FBR collects federal income tax and sales tax on goods. Each needs its own registration and returns."),
        ("Does paying Sindh professional tax count as income tax?",
         "No. It is a separate provincial levy and does not reduce your federal income tax."),
        ("Who collects property tax in Karachi?",
         "Urban immovable property tax is collected by Sindh's Excise, Taxation and Narcotics Control department, separately from income tax."),
    ],
}

PAGES["blogs/balochistan-income-tax-guide-2026.html"] = {
    "body": """## Hub and Lasbela: The Sindh–Balochistan Boundary Problem

Many factories in the Hub industrial area are run from offices in Karachi. The plant sits in Balochistan, the head office and bank accounts sit in Sindh, and services are bought from both sides. This creates a recurring question: which province's service tax applies, SRB or BRA? The answer depends on where the service is provided or consumed under each province's law, and getting it wrong can mean paying tax to one authority and receiving a demand from the other.

> For Hub-based manufacturers, we map each service contract, from security and catering to transport and maintenance, to the province that taxes it before invoices are raised.

## Quetta's Economy and Its Tax Profile

Quetta's taxpayers are mainly traders, transporters, government employees, contractors and fruit growers. Some typical issues:

| Taxpayer | Typical issue |
| Fruit orchard owners in Pishin and Mastung | Agricultural income is provincial, but sale proceeds still need to fit the wealth statement |
| Government employees | Salary tax deducted every month, often with a refund unclaimed |
| Construction contractors | Income tax deducted from bills, plus BRA tax on construction services where applicable |
| Coal mine lessees and contractors | Royalties and provincial levies on top of income tax |

## Mining and Minerals

Coal, marble and chromite operations in Balochistan pay royalties to the province under mining concessions. Royalty is a cost, not an income tax. The mining company still files an income tax return with FBR, and payments to contractors that haul and process minerals are subject to withholding. Keeping lease documents and royalty receipts together makes the return and any audit easier.

## Working with Us from Balochistan

Clients in Quetta, Hub, Turbat and Gwadar work with us remotely. Send documents on WhatsApp, and we register you, prepare returns and handle BRA and FBR correspondence without you travelling.""",
    "faq": [
        ("Which province taxes services at a Hub factory run from Karachi?",
         "It depends on where each service is rendered or consumed under the Sindh and Balochistan laws. Each contract should be checked, because both SRB and BRA can claim tax on cross-border services."),
        ("Is mineral royalty the same as income tax?",
         "No. Royalty is paid to the province under the mining lease and is a business expense. Income tax is still due to FBR on the profit."),
        ("Do Quetta government employees need to file returns?",
         "Filing is how they get on the Active Taxpayers List and claim any excess salary tax as a refund, so most should file every year."),
    ],
}

PAGES["blogs/azad-kashmir-tax-guide-2026.html"] = {
    "replace": [("AJK provincial income tax is administered separately by the AJK Revenue Authority.",
                 "Income sourced within AJK is taxed under AJK's own law and administered by AJK's own revenue authorities, not by FBR.")],
    "body": """## Mirpur and the British-Pakistani Connection

A large share of the British-Pakistani community traces its roots to Mirpur, Kotli and Bhimber. That creates a specific set of questions we see every year:

- **UK residents who own houses in Mirpur** and want to know whether the rent is taxable in AJK, in the UK, or both.
- **Family members in AJK receiving money from the UK** to build or maintain homes.
- **Returning families** who move back after decades abroad and need to start filing in Pakistan for the first time.

For UK residents, income from AJK property is normally reportable in the UK as foreign income, with credit given for tax paid locally where the rules allow. The AJK side depends on AJK's own rental income rules. Both sides need a record of the rent received.

## Property Bought Outside AJK

AJK families often buy plots in Islamabad, Rawalpindi or Lahore. Those transactions happen under federal law: advance tax is collected at registration, and filer status decides the rate. An AJK resident with no federal income may still find that filing a federal return is worthwhile simply to get on the Active Taxpayers List before a large purchase in Punjab or Islamabad.

## Hydropower and Construction Contracts

Hydropower projects on the Jhelum and Neelum rivers and road building across the region bring contractors from all over Pakistan. A Lahore-registered contractor working in AJK may face deductions under AJK rules on its AJK contracts while filing with FBR on the rest. Keeping separate contract-wise records for AJK and non-AJK work makes both filings defensible.

## Getting the Split Right

We start every AJK file by listing each income source and where it legally arises, then decide which authority it belongs to. That one exercise prevents most double-taxation and undeclared-income problems.""",
    "faq": [
        ("Do I pay FBR tax on rent from my house in Mirpur?",
         "Income arising in AJK is generally taxed under AJK's own law, not FBR. If you live in the UK, the rent is usually reportable there too, with relief for local tax where the rules allow."),
        ("Can an AJK resident become a filer on FBR's Active Taxpayers List?",
         "Yes. AJK residents can register and file with FBR, which lowers withholding on property and bank transactions in Pakistan's federal territory and provinces."),
        ("Who taxes a contractor's work on an AJK hydropower project?",
         "Contracts performed in AJK can attract AJK withholding, while the contractor's other income is taxed by FBR. Separate contract-wise records keep both filings correct."),
    ],
}

PAGES["blogs/income-tax-2025-budget-changes.html"] = {
    "body": """## Where Budget 2025-26 Changes Showed Up in Practice

Rather than repeating figures that later budgets have revised, it is more useful to see which parts of a taxpayer's life the 2025-26 Finance Act touched:

| Area | What changed in nature | Who felt it |
| Salary slabs | Rates on several middle-income bands were adjusted | Salaried employees and payroll departments |
| Withholding on bank profit | The rate on profit from deposits and savings was revisited | Savers and pensioners |
| E-commerce | Tax collection on online sales through banks, gateways and couriers, 1% on digital payments and 2% on cash on delivery | Online sellers and marketplaces |
| Non-filer restrictions | Further limits on what non-filers can buy or open | People not on the Active Taxpayers List |
| Property | Withholding on purchase and sale was revised | Buyers, sellers and builders |

## The E-Commerce Change Was the Most Practical

For many small sellers, the new collection on online payments was the first time tax appeared on their sales at all. The amount withheld by the bank, payment gateway or courier is an advance payment. Sellers who file a return can claim it against their liability; those who do not file simply lose it.

## How Property Rules Moved Again in 2026-27

The property withholding introduced or revised in 2025-26 did not last long. For transfers from 1 July 2026, buyers pay advance tax under section 236K at 1.25% if on the Active Taxpayers List and 2.5% otherwise, while sellers pay under section 236C at 2.75% or 5.5%. This is a good example of why a budget article must always be read together with the latest Finance Act.

## A Simple Post-Budget Routine

1. Read the Finance Act summary FBR publishes after the budget, not just news headlines.
2. Note which of your income streams or transactions are affected.
3. Update payroll, pricing or invoicing systems from 1 July.
4. Keep a dated copy of the rates you applied, in case of a later audit.""",
    "faq": [
        ("Did the 2025-26 budget change e-commerce taxation?",
         "Yes. It introduced tax collection on online sales through banks, payment gateways and couriers, 1% on digital payments and 2% on cash-on-delivery orders, adjustable for sellers who file returns."),
        ("Are the 2025-26 property rates still in force?",
         "No. For transfers from 1 July 2026, the buyer's rate under 236K is 1.25% for filers and 2.5% for non-filers, and the seller's rate under 236C is 2.75% or 5.5%."),
        ("Where do I find the official list of changes?",
         "FBR publishes explanatory circulars after each Finance Act. These are more reliable than social media summaries."),
    ],
}

PAGES["blogs/income-tax-second-schedule-pakistan.html"] = {
    "body": """## How the Second Schedule Is Organised

The Second Schedule is divided into parts, and the part a clause sits in tells you what kind of relief it gives:

| Part | Type of relief | Practical effect |
| Part I | Exemption from total income | The income is left out of tax altogether |
| Part II | Reduced rates of tax | The income is taxed, but at a lower rate |
| Part III | Reduction in tax liability | Tax is calculated normally, then reduced by a percentage or amount |
| Part IV | Exemption from specific provisions | Usually relief from a particular withholding or other section, not from tax itself |

Knowing the part matters because a Part IV clause that waives withholding does not make the income exempt. Many taxpayers misread these clauses and leave taxable income out of their return.

## Exemption Certificates Versus Schedule Exemptions

Some reliefs work automatically through the return, while others require an exemption certificate from the Commissioner under section 159 before a withholding agent will stop deducting tax. If a clause relieves you from withholding but your bank or buyer keeps deducting, the remedy is usually a certificate, not a refund claim at year end. Our [exemption certificate service](/tax-exemption-certificate) handles these applications.

## Typical Clauses Individuals Ask About

- Pension received by retired government employees.
- Profit on certain savings instruments held by specific groups.
- Reduction in tax for full-time teachers and researchers in recognised institutions.
- Income of approved funds and non-profit organisations.

Each clause has conditions, such as who qualifies, what records are needed and whether the relief has been withdrawn or limited in a later Finance Act.

## Reading a Clause Properly

When checking a clause, read the whole entry including provisos, note the tax year from which it applies, and look for any later omission. Clauses are frequently added with a sunset date. Using an omitted clause in a return is one of the commonest reasons for an amended assessment.""",
    "faq": [
        ("What is the difference between Part I and Part IV of the Second Schedule?",
         "Part I exempts income from tax altogether. Part IV gives relief from specific provisions, often withholding, without making the income itself exempt."),
        ("Do I need a certificate to use a Second Schedule exemption?",
         "Some reliefs apply directly in the return, but stopping withholding at source often needs an exemption certificate under section 159."),
        ("Can a Second Schedule clause expire?",
         "Yes. Many clauses carry sunset dates or are withdrawn by later Finance Acts, so always check the current text for your tax year."),
    ],
}

PAGES["blogs/export-income-tax-pakistan-2026.html"] = {
    "replace": [
        ("typically qualifies for concessional final-tax treatment under the export income regime, rather than being taxed at standard progressive rates — but only if",
         "has income tax collected by the bank at the time of realisation under the export regime, and how that deduction is treated, as final tax or as minimum tax under the normal regime, has changed in recent budgets — but the export treatment applies only if"),
        ("The concessional tax treatment on export income is conditional on", "The export tax treatment is conditional on"),
        ("risk losing the preferential rate on that portion of income and being assessed at standard rates instead.",
         "risk losing the export treatment on that portion of income."),
    ],
    "body": """## From Final Tax to Minimum Tax

For many years the tax deducted from export proceeds was the exporter's final income tax, so exporters filed a simple statement and kept no profit computation. Budget changes since 2024 moved commercial exporters of goods towards the normal tax regime, where the deduction on proceeds works as a minimum tax and the return must show actual profit and expenses. The difference is significant: an exporter with a loss still pays the minimum, while a highly profitable exporter may owe more than was deducted.

> Exporters who still keep only bank realisation papers and no expense records are the most exposed to this change. Start keeping purchase, salary and overhead records from the first month of the tax year.

## Export Facilitation Scheme and Sales Tax

The Export Facilitation Scheme replaced older schemes such as DTRE and manufacturing bond arrangements. It lets approved exporters import or locally buy inputs without paying duty and sales tax upfront, against an authorisation and a later reconciliation of how inputs were used. Exporters outside the scheme pay sales tax on inputs and claim refunds, which depends on registered suppliers and accurate invoices.

## Indirect Exporters

Units that supply goods to an exporter rather than shipping abroad themselves are called indirect exporters. Tax may be deducted on their sales to the exporter, and their position under the export regime depends on the documentation linking their supply to the final export. Keeping the exporter's purchase order and the inland letter of credit or contract helps prove the link.

## Records We Ask Exporters to Keep

- Electronic form E and bank realisation certificate for each shipment.
- Commercial invoice, packing list and bill of lading or airway bill.
- Purchase invoices and sales tax returns.
- Payroll records and overheads, now needed for profit computation.""",
    "faq": [
        ("Is tax deducted on export proceeds still final?",
         "For many exporters of goods it now works as a minimum tax under the normal regime, so the return must show actual profit. IT exports have their own rules. We confirm the treatment for each tax year."),
        ("What replaced the DTRE scheme?",
         "The Export Facilitation Scheme now covers duty- and tax-free inputs for approved exporters, subject to authorisation and later reconciliation."),
        ("Who is an indirect exporter?",
         "A business that supplies goods to an exporter rather than exporting directly. Its tax treatment depends on documents linking its sale to the final export."),
    ],
}

PAGES["blogs/how-to-file-nil-return-pakistan.html"] = {
    "body": """## Step-by-Step: Filing a Nil Return on IRIS

1. Log in to IRIS with your CNIC and password. If you have forgotten it, reset it through the registered email and mobile number.
2. Open **Declaration** and choose the return of income form for the correct tax year. Make sure it is the year that ended on 30 June, not the current one.
3. Leave income fields at zero only where there genuinely was no income. Bank profit, rent or freelance receipts, however small, must be entered.
4. Enter any tax already deducted, such as tax on bank profit or a mobile phone bill, so it is recorded as a credit.
5. Complete the wealth statement if you hold assets such as a bank account, vehicle, gold or a plot. A nil income return can still have a full wealth statement.
6. Calculate, verify the figures, and submit with the PIN sent to your mobile number.
7. Download the acknowledgement and keep it with the year's papers.

## When a Nil Return Is the Wrong Choice

| Situation | Correct return |
| Student with no income and no assets | Nil return |
| Housewife with a bank account funded by her husband | Nil income, but a wealth statement showing the account and gifts received |
| Person whose employer deducted salary tax | Normal salaried return, not nil |
| Dormant business that still had bank profit | Return showing the bank profit |

## Why a Nil Return Still Matters

Filing on time keeps you on the Active Taxpayers List without the late-filing surcharge. That status lowers withholding on future bank, vehicle and property transactions, and an unbroken filing history helps with visas and loans.

If you are unsure which category you fall into, our [income tax return service](/income-tax-return-pakistan) starts with a quick review of your situation.""",
    "faq": [
        ("Do I need a wealth statement with a nil return?",
         "If you own assets such as a bank account, vehicle, gold or property, the wealth statement should be completed even when income is nil."),
        ("Can I file a nil return if my employer deducted tax?",
         "No. Salary with tax deducted is income and must be declared in a normal return, which also lets you claim the deducted tax."),
        ("Does a nil return put me on the Active Taxpayers List?",
         "Yes, if filed by the due date. A late nil return also qualifies after the late-filing surcharge is paid."),
    ],
}

PAGES["blogs/income-tax-return-late-filing-pakistan.html"] = {
    "replace": [("trigger a Rs. 1,000/month penalty under Section 182 plus loss of Active Taxpayer List status until the surcharge is paid and the return processed.",
                 "can attract a penalty under Section 182, and a late filer only appears on the Active Taxpayer List after paying the late-filing surcharge.")],
    "body": """## What Actually Happens After You Miss 30 September

Three separate consequences follow a late return, and it helps to treat them separately:

| Consequence | Legal basis | What you can do |
| Not on the Active Taxpayers List | Section 181A | File the return and pay the ATL surcharge to be included |
| Penalty for late return | Section 182 | Usually charged through an order, which can be contested if there was a reasonable cause |
| Higher withholding meanwhile | Various withholding sections | Deductions at non-filer rates continue until you appear on the list |

## The ATL Surcharge

A return filed after the due date does not put you on the Active Taxpayers List automatically. You also pay a fixed surcharge, which for individuals has been Rs 1,000, with higher amounts for associations of persons and companies. Once the surcharge is paid and the return is accepted, your name is added at the next update of the list.

## Penalty Orders and Reasonable Cause

The late-filing penalty is not charged by IRIS automatically on submission. It normally arrives later, through a notice and an order. If the delay had a genuine reason, such as illness, a death in the family or a documented IRIS outage, a reply with evidence can reduce or remove the penalty. We draft these replies through our [FBR notice service](/fbr-notice-defense).

## Applying for an Extension Before the Deadline

If you know you will miss the deadline, section 119 allows an application to the Commissioner for more time, filed before the due date with a reason. An extension granted this way avoids the late status completely, which is better than paying the surcharge afterwards.

## Late Return Checklist

- Gather salary certificates, bank certificates of tax deducted and property papers.
- File the return and wealth statement on IRIS.
- Pay the ATL surcharge through a payment slip (PSID).
- Keep copies of everything in case a penalty notice arrives.""",
    "faq": [
        ("How much is the ATL surcharge for a late return?",
         "For individuals it has been Rs 1,000, with higher amounts for AOPs and companies. It is paid separately from any penalty."),
        ("Can I avoid the late-filing penalty?",
         "Applying for an extension under section 119 before the deadline is the cleanest route. After the deadline, a reasonable cause supported by evidence can help contest a penalty order."),
        ("Will a late return still put me on the Active Taxpayers List?",
         "Yes, once the return is filed and the surcharge is paid, your name is added at the next list update."),
    ],
}
