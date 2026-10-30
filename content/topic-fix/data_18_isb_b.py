"""Islamabad pages, part B: G, H, I, D and B sectors."""

PAGES = {}


def page(slug, lead, desc, body, faq):
    PAGES[f"blogs/tax-consultant-{slug}.html"] = {"lead": lead, "desc": desc, "body": body, "faq": faq}


page("g-5-islamabad",
     "G-5 holds much of Islamabad's state architecture, including the Diplomatic Enclave and major government buildings, along with staff housing and a few private residences. Our G-5 clients are local staff of missions and international organisations, government employees and their families.",
     "G-5 Islamabad tax help for local staff of embassies and international organisations and government employees: salary treatment, returns and refunds online.",
     """## Local Staff of Embassies and International Organisations

Pakistani nationals working for foreign missions and international bodies are often paid without tax deducted at source, because their employers do not act as withholding agents in the usual way. That does not make the salary exempt. In most cases the employee must declare the salary and pay tax directly, through advance tax instalments during the year and the balance with the return. Some organisations have specific arrangements, so the employment contract should be checked.

## Paying Tax Without an Employer Deducting It

Employees in this position should work out their expected tax at the start of the year and pay quarterly advance tax under section 147. Leaving the whole amount until September creates a large bill and default surcharge on missed instalments.

## Government Employees

Federal staff living in G-5 housing have tax deducted from salary, with official accommodation reflected in the salary certificate under the rules for perquisites.

## Getting Started

Mission and organisation staff should share their contract, monthly pay slips, any tax already paid and bank statements. Government employees need the salary certificate. We calculate the liability, set up advance tax payments where needed and file the return.""",
     [("Is my salary from an embassy taxable in Pakistan?",
       "For Pakistani nationals it generally is, even if the embassy does not deduct tax; you declare it and pay tax directly."),
      ("How do I pay tax if my employer does not deduct it?",
       "Through quarterly advance tax under section 147 and the balance with your annual return."),
      ("Is official government accommodation taxable?",
       "Accommodation and similar benefits are valued under the rules for perquisites and shown on the salary certificate.")])

page("g9-islamabad",
     "G-9 is a busy middle-class sector best known for Karachi Company, one of Islamabad's largest markets, with shops, training institutes and hostels around it. Our G-9 clients are shopkeepers, institute owners, hostel operators and residents.",
     "G-9 Islamabad tax help for Karachi Company shopkeepers, training institutes, hostels and residents: business returns, rent and ICT services tax online.",
     """## Karachi Company Shopkeepers

Garments, electronics, books and household goods are sold in G-9's main market, much of it in cash but increasingly through mobile wallets and cards. Purchase bills, monthly sales totals and electricity bills form the basis of a reliable return.

## Training Institutes and Academies

G-9 hosts many academies preparing students for competitive exams and language tests. Fee income is business income; payments to visiting teachers are expenses for the institute and income for the teachers. Some education and training services may fall under the ICT tax on services depending on the year's schedule and turnover.

## Hostels

Private hostels for students and job seekers operate from houses in G-9. Hostel income is business income when meals and services are provided, not just rent, and records of residents and monthly charges are needed.

## Getting Started

Shopkeepers should bring purchase records and bank statements; institutes their fee registers and teacher payments; hostel owners their residents' register and expenses. We prepare the return from these and explain each figure before submission.""",
     [("Is hostel income rent or business income?",
       "When meals and services are provided, it is generally business income; plain rent of a property is income from property."),
      ("Do teachers paid by a G-9 academy declare that income?",
       "Yes, as their own income, and the academy records the payments as expenses."),
      ("Are training institutes subject to ICT sales tax?",
       "It depends on the service and turnover under the year's ICT schedule; we check each institute.")])

page("g10-islamabad",
     "G-10 is a well-established residential sector with a busy markaz, schools and clinics, home to government employees, professionals and small business owners. Our G-10 clients include families, clinic and pharmacy owners and markaz traders.",
     "G-10 Islamabad tax help for government employees, clinics, pharmacies and markaz traders: returns, refunds, rent and wealth statements filed online.",
     """## Government Employees and Refunds

Many G-10 households include a federal employee whose tax is deducted monthly. Arrears of pay, received later for earlier years, can push monthly deductions up; such arrears may be taxed at the rate of the years they relate to if the option is chosen in the return. Checking this often produces a refund.

## Clinics and Pharmacies

G-10's clinics are run by general practitioners and specialists; pharmacies sit next to them. Doctors declare consultation fees as professional income; pharmacies declare trading profit from medicines and keep distributor invoices.

## Markaz Traders

Shops in G-10 Markaz file business returns and claim electricity bill tax. Larger outlets may face point-of-sale rules.

## Getting Started

Employees should share salary certificates, including any arrears statements; doctors their fee records; pharmacies their purchase invoices and stock list. We prepare returns and wealth statements together for households with more than one earner.""",
     [("Can pay arrears be taxed at earlier years' rates?",
       "There is an option to tax arrears at the rates of the years they relate to, which can reduce tax; it is chosen in the return."),
      ("How does a pharmacy calculate taxable income?",
       "Sales of medicines minus purchase cost and expenses, supported by distributor invoices and a stock list."),
      ("Do G-10 doctors declare fees from private patients?",
       "Yes, all consultation fees are professional income, whether or not tax was deducted.")])

page("g11-islamabad",
     "G-11 combines residential streets with a large markaz and the judicial complex nearby, attracting lawyers, government staff and business families. Our G-11 clients are professionals, shopkeepers and families buying or selling property.",
     "G-11 Islamabad tax help for lawyers, government staff, shopkeepers and property buyers: returns, advance tax on transfers and wealth statements online.",
     """## Lawyers Near the Courts

The judicial complex near G-11 brings legal practices to the sector. Lawyers receive fees from individuals without deduction and from institutions with deduction; all fees are income, and certificates are credits. Legal services may also attract ICT tax on services.

## Property Turnover in G-11

Houses and portions in G-11 change hands often. For transfers from 1 July 2026, buyers pay advance tax under section 236K at 1.25% if on the Active Taxpayers List and 2.5% otherwise, and sellers pay under section 236C at 2.75% or 5.5%. Islamabad's capital value tax and CDA charges apply in addition.

## Markaz Businesses

Shops and restaurants in G-11 Markaz file income tax returns; restaurants charge ICT sales tax on services.

## Getting Started

Before a property deal, check your status on the Active Taxpayers List; if you are not on it, file first. For returns, share your CNIC, income records and property papers on WhatsApp and we prepare the filing.""",
     [("What advance tax applies on buying a G-11 house?",
       "For transfers from 1 July 2026, 1.25% under section 236K for active filers and 2.5% for others, plus Islamabad charges."),
      ("Do lawyers in Islamabad charge sales tax?",
       "Legal services can be taxable under the ICT tax on services law depending on turnover."),
      ("Should I file before selling my house?",
       "Yes. Being on the Active Taxpayers List halves the seller's advance tax under section 236C.")])

page("g-12-islamabad",
     "G-12 is a developing sector on Islamabad's western side, where plots, new houses and older village settlements sit side by side. Our G-12 clients are plot owners, families building homes and residents of the older settlements.",
     "G-12 Islamabad tax help for plot owners, families building homes and long-time residents: property records, construction costs and filer status online.",
     """## Plots and Development Charges

Owners in developing sectors pay development charges and possession fees over time. Each payment adds to the cost of the plot in the wealth statement. Receipts from the authority or society should be kept, because they establish the cost for any future sale.

## Building a House

Construction is usually funded over several years from salary, savings, loans and family help. The wealth statement should show construction costs added to the house's value each year, along with the source of funds.

## Residents of Older Settlements

Families who owned land before the sector was developed may have received compensation or developed plots. Compensation and the land's history affect how a later sale is taxed, so the acquisition papers matter.

## Getting Started

Share the allotment letter, payment receipts, construction records and bank statements. We prepare the wealth statement so that every stage of the property's cost is accounted for.""",
     [("Do development charges increase my plot's cost?",
       "Yes. Development and possession charges paid are part of the cost shown in the wealth statement."),
      ("How do I show a house built over three years?",
       "Add each year's construction cost to the house's value, with the funding source in the reconciliation."),
      ("Is compensation for acquired land taxable?",
       "It depends on the nature of the land and the law at the time; agricultural land compensation is treated differently. We review the papers.")])

page("g-13-islamabad",
     "G-13 was developed largely for federal government employees through the employees' housing authority, and today combines houses, apartments and a busy markaz. Our G-13 clients are federal employees, apartment owners and markaz traders.",
     "G-13 Islamabad tax help for federal employee allottees, apartment owners and markaz traders: allotted plots, rent and returns, filed online.",
     """## Allottees of Government Housing Schemes

Federal employees who received plots or apartments through the housing authority pay for them in instalments. The amounts paid appear in the wealth statement as the asset's cost, and the allotment letter is the key document. Selling an allotted unit before or after possession has tax consequences that depend on the dates involved.

## Apartment Blocks

G-13's apartment blocks are often let to young families. Rent from individual tenants arrives without deduction, so owners pay tax with their returns.

## Markaz Traders

Shops and eateries in G-13 Markaz file business returns; eateries charge ICT sales tax on services where applicable.

## Getting Started

Federal employees should share the salary certificate, allotment letter and instalment receipts; landlords their tenancy agreements; traders their purchase and sales records. We prepare the return and wealth statement remotely.""",
     [("How do I show an apartment allotted by the housing authority?",
       "At the instalments paid so far, as an asset in the wealth statement, with the allotment letter as proof."),
      ("Is rent from a G-13 apartment taxable?",
       "Yes, and if the tenant does not deduct tax, you pay it with your return."),
      ("Can I sell my allotted unit?",
       "Usually yes, subject to the authority's rules; advance tax and capital gains apply based on the dates involved.")])

page("g13-islamabad",
     "Around G-13's main boulevards and markaz, small businesses, tuition centres and rented portions serve a young and growing population. This page focuses on business owners and tenants in G-13 rather than on allotment matters.",
     "G-13 Islamabad business and tenant tax help: markaz shops, tuition centres, rented portions and first returns for young professionals, done online.",
     """## Small Businesses on the Boulevards

Grocery chains' franchises, bakeries, mobile shops and salons line G-13's main roads. Owners file business returns, claim electricity bill tax and keep purchase records. Franchisees pay royalties to brand owners, which are business expenses supported by agreements.

## Tuition Centres

Coaching centres for school and university students are common. Fee registers and records of payments to teachers are the main documents for the centre's return.

## Young Professionals Renting Portions

Tenants in G-13 are often first-time filers working in Islamabad's offices. Their first return should include an opening wealth statement listing savings, vehicles and other assets.

## Getting Started

Business owners should share purchase and sales records and bank statements; tenants their salary certificates and bank statements. We file first returns with complete opening wealth statements so later years are simple.""",
     [("Are franchise royalties deductible?",
       "Yes, royalties paid under a franchise agreement are business expenses; tax may need to be deducted when paying them."),
      ("What should a first-time filer include in the wealth statement?",
       "All assets owned on 30 June, such as savings, vehicles, gold and any property, and any loans."),
      ("Do tuition centres need records of teacher payments?",
       "Yes, they are expenses for the centre and income for the teachers.")])

page("g14-islamabad",
     "G-14 is a newer sector developed through the federal employees' housing authority, where many allottees are still building or have only recently moved in. Our G-14 clients are allottees, families building homes and investors buying from original allottees.",
     "G-14 Islamabad tax help for allottees, families building homes and investors: allotment payments, construction costs and transfers, filed online.",
     """## Original Allottees

Allottees pay for plots in instalments and later pay possession and development charges. The wealth statement should show the cumulative amount paid each year. When the plot is transferred to a buyer, the allottee pays advance tax on the sale and any capital gains tax due.

## Buyers from Allottees

Investors who buy plots from original allottees pay advance tax under section 236K: for transfers from 1 July 2026, 1.25% if on the Active Taxpayers List and 2.5% otherwise, plus the authority's transfer fees. The purchase deed and the authority's transfer letter are the key records.

## Construction in Progress

Families building in G-14 add construction costs to the value of the house each year. Contracts with builders, and records of payments for materials, support the figures.

## Getting Started

Share the allotment or transfer letter, all payment receipts and construction records. We prepare a wealth statement that tracks the plot's cost from allotment to completion.""",
     [("What advance tax does a buyer pay on a G-14 plot?",
       "For transfers from 1 July 2026, 1.25% under section 236K for active filers and 2.5% for others."),
      ("Is selling an allotted plot taxable for the allottee?",
       "Advance tax is paid at transfer, and capital gains tax depends on the acquisition date and gain."),
      ("How do I record construction costs?",
       "Add each year's costs to the house's value in the wealth statement, supported by contracts and receipts.")])

page("g15-islamabad",
     "G-15 lies on Islamabad's outer edge near the motorway and the new airport road, with a mix of developed plots, new homes and land still awaiting development. Our G-15 clients are plot owners, investors and families moving out from the city centre.",
     "G-15 Islamabad tax help for plot owners, investors and families moving in: property cost records, transfers and filer status for the outer sectors.",
     """## Investors Holding Plots

G-15 plots are often held as investments while the area develops. Holding a vacant plot can bring section 7E into play if the owner's total property value is above the aggregate limit and no exemption applies. Owners should review this every year.

## Families Moving Out from the Centre

Families who sell a house in an older sector and buy or build in G-15 should document both transactions. The sale proceeds explain the new purchase in the wealth statement, and the sale itself attracts advance tax and possibly capital gains tax.

## Access to the New Airport and Motorway

G-15's location makes it attractive to people working at the airport and in logistics. Their salaries are declared normally, and any allowances for location or shifts are shown on salary certificates.

## Getting Started

Share the plot's allotment or purchase papers, payment receipts, and details of any property sold to fund the move. We prepare the wealth statement so that both the sale and the purchase are explained.""",
     [("Does section 7E apply to my vacant G-15 plot?",
       "It can, if your total property value exceeds the limit and no exemption applies; review it each year."),
      ("How do I show a house sale used to buy in G-15?",
       "Declare the sale and its proceeds, then the new purchase funded by them, in the same year's wealth statement."),
      ("Do airport employees declare shift allowances?",
       "Allowances are part of salary and treated according to the rules for each allowance on the salary certificate.")])

page("h13-islamabad",
     "H-13 lies near the university belt in the H sectors and the Kashmir Highway, with student housing, private hostels and growing residential areas. Our H-13 clients are hostel operators, landlords, university staff and students who have started earning.",
     "H-13 Islamabad tax help for hostel operators, landlords, university staff and earning students: business and rental income and first returns online.",
     """## Hostels and Student Housing

Students of nearby universities rent rooms and beds in H-13. Hostel operators who provide meals, cleaning and utilities run a business, and their income is the charges collected less running costs. Simple monthly records of residents and payments are enough.

## Landlords

Owners who let whole houses or portions to hostel operators receive rent, which is income from property, while the operator's profit is business income. Clear tenancy agreements separate the two.

## University Staff

Faculty and staff of the nearby universities have salary tax deducted. Visiting faculty, research grants and consulting add other income streams to declare.

## Students Who Start Earning

Students freelancing or tutoring can register and file early. A small first return establishes a record for bank accounts and future visas.

## Getting Started

Share your CNIC and the relevant records: residents' register for hostels, tenancy agreements for landlords, salary certificates for staff, and platform statements for students.""",
     [("Is running a student hostel business income?",
       "Yes, when meals and services are provided; plain letting of a house is income from property."),
      ("Do research grants count as income?",
       "Payments for research work or consulting are generally income; grants with specific conditions should be reviewed case by case."),
      ("Should students who freelance file returns?",
       "Yes, once they earn; filing early builds a record and gives access to filer rates.")])

page("h-15-islamabad",
     "H-15 is a newer sector on Islamabad's southern side, where cooperative societies and developers have been bringing plots and homes to market. Our H-15 clients are society members, plot investors and families building their first homes.",
     "H-15 Islamabad tax help for society members, plot investors and first-home builders: membership payments, transfers and wealth statements online.",
     """## Cooperative Society Membership

Many H-15 plots are held through society membership, paid in instalments. The membership and payments are an asset in the wealth statement until a plot is allotted. If membership is sold, the gain is taxable, and the society's transfer record is the proof.

## Plot Investors

Buying and selling files and plots is common in developing sectors. Occasional sales of investment property are capital transactions; frequent buying and selling can be treated as a business. Records of each deal and the intention behind it matter.

## First-Time Builders

Families building their first home in H-15 should keep contracts and receipts for construction, and record loans from banks or relatives in the wealth statement.

## Getting Started

Share the society membership or allotment documents, payment receipts and construction records on WhatsApp. We prepare a wealth statement that tracks each payment and explains how it was funded.""",
     [("Is a society membership an asset for tax purposes?",
       "Yes. Payments for membership are shown in the wealth statement until a plot is allotted."),
      ("Can frequent plot trading be treated as a business?",
       "Yes, if buying and selling is regular and organised; occasional sales are usually capital transactions."),
      ("How do I show a loan from my brother for construction?",
       "As a liability in the wealth statement, supported by a written acknowledgement and bank transfers.")])

page("i8-islamabad",
     "I-8 is a popular residential sector with a lively markaz, clinics, schools and offices, close to Faizabad and the Islamabad Expressway. Our I-8 clients are families, doctors, small business owners and landlords.",
     "I-8 Islamabad tax help for families, doctors, small businesses and landlords: returns, professional income, rent and wealth statements filed online.",
     """## Doctors and Clinics

I-8 Markaz and the surrounding streets have many clinics, laboratories and dental practices. Fees from patients are professional income, and payments from panels or hospitals often have tax deducted. Laboratories with equipment and staff should keep records of these costs.

## Landlords Near the Expressway

Houses and portions in I-8 are let to families and to offices. Rent is declared each year; office tenants may deduct tax.

## Small Businesses

Retailers, salons and cafes in I-8 Markaz file business returns. Cafes and salons may need registration for ICT sales tax on services.

## Families

Households with salaried members, rental income and savings should file together so that gifts, joint assets and shared expenses agree across all their statements.

## Getting Started

Share CNICs, salary certificates, practice records, tenancy agreements and bank statements on WhatsApp. We prepare returns for each earning member and review them together before submission.""",
     [("Do laboratory owners claim equipment costs?",
       "Yes, through depreciation on equipment and as running expenses, supported by invoices."),
      ("Is rent from an office tenant in I-8 taxed at source?",
       "Office tenants who are prescribed persons deduct tax from rent; you claim it in your return."),
      ("Do salons in Islamabad charge sales tax on services?",
       "Beauty and similar services can be taxable under the ICT law depending on turnover.")])

page("i10-islamabad",
     "I-10 sits beside Islamabad's industrial area in I-9 and I-10, with residential streets, a busy markaz and workshops and factories nearby. Our I-10 clients are factory and workshop owners, traders and the workers who live in the sector.",
     "I-10 Islamabad tax help for industrial-area factories, workshops, traders and workers: sales tax, withholding, returns and refunds, handled online.",
     """## Industrial Area Units

Islamabad's industrial area in I-9 and I-10 hosts food processing, printing, steel, furniture and pharmaceutical units. Manufacturers generally need sales tax registration and monthly returns, deduct tax from staff and suppliers, and claim input tax only on invoices from active registered suppliers.

## Workshops and Service Units

Automobile workshops, printing presses and fabrication units provide services and may fall under the ICT tax on services. Customers that are companies may deduct income tax on payments.

## Traders

I-10 Markaz traders supply both residents and industrial customers. Sales to registered businesses may require proper invoices.

## Workers

Workers living in I-10 can file to claim refunds of excess salary tax and to join the Active Taxpayers List.

## Getting Started

Manufacturers should share their sales tax returns, supplier list and payroll; workshops their job cards and customer invoices; workers their salary certificates. We set up monthly and annual filings as needed.""",
     [("Do I-9 and I-10 manufacturers need sales tax registration?",
       "Manufacturers are generally required to register for federal sales tax, with limited exceptions."),
      ("Do automobile workshops charge ICT sales tax?",
       "Repair and maintenance services can be taxable under the ICT law depending on turnover."),
      ("Can industrial workers claim refunds?",
       "Yes, if tax deducted from salary exceeds their liability, by filing a return.")])

page("i-13-islamabad",
     "I-13 is a developing sector along the Islamabad side of the twin-city border, where plots, new homes and small markets are filling in. Our I-13 clients are plot owners, families building homes and small traders setting up in the new markets.",
     "I-13 Islamabad tax help for plot owners, home builders and new traders: property cost records, first business returns and filer status, done online.",
     """## Plot Owners Awaiting Development

Owners in I-13 often pay development and possession charges over years. Each payment adds to the plot's cost. Keeping every receipt avoids disputes later about the cost when the plot is sold.

## Building Homes

Families building homes should add construction costs each year to the house's value and show the funding source, whether savings, loans or help from relatives.

## Traders Opening Shops

New shops in I-13's markets should register from the start and keep records of initial investment in stock, fixtures and rent deposits, which are assets in the wealth statement.

## Commuters to Rawalpindi and Islamabad

Many residents work in either city. Salary tax is deducted by employers; filing claims refunds and keeps them on the Active Taxpayers List.

## Getting Started

Share the plot's papers, payment receipts, construction records or business start-up costs and bank statements. We prepare a clear wealth statement and return.""",
     [("Are security deposits for a shop an asset?",
       "Yes, refundable deposits are assets in the wealth statement until they are returned."),
      ("Should a new shop register from the first day?",
       "Yes, so that start-up costs, stock and early sales are recorded from the beginning."),
      ("Do I declare development charges paid for my plot?",
       "Yes, they add to the plot's cost in the wealth statement.")])

page("i14-islamabad",
     "I-14 is part of Islamabad's newer I-series belt, with residential plots, apartments under construction and access to the Expressway and Kashmir Highway. Our I-14 clients are apartment buyers, plot owners and young families.",
     "I-14 Islamabad tax help for apartment buyers, plot owners and young families: instalment payments, property records and first returns filed online.",
     """## Apartments Bought Off-Plan

Developers in the I-series sectors sell apartments on booking and instalments. Each instalment is part of the buyer's investment and should appear in the wealth statement as an advance for property until possession, then as the apartment at full cost.

## Young Families

Couples buying their first home often combine savings, a bank loan and help from parents. Each source should be recorded: the loan as a liability, the gift in both parents' and children's wealth statements.

## Plot Owners

Owners holding plots for future construction should track development charges and consider section 7E if their total property value is above the limit.

## Getting Started

Share the booking letter, payment schedule, receipts and loan documents. We prepare returns that show the investment correctly from booking to possession.""",
     [("How do I declare an off-plan apartment?",
       "As an advance for property at the instalments paid, until possession, then as the apartment at full cost."),
      ("Is a home loan shown in the wealth statement?",
       "Yes, the outstanding balance is a liability on 30 June each year."),
      ("Do gifts from parents need to be recorded?",
       "Yes, in both the parents' and the children's wealth statements, preferably through bank transfers.")])

page("i-16-islamabad",
     "I-16 is one of Islamabad's youngest sectors, on the city's south-western edge, where development is still under way and most activity revolves around plots and construction. Our I-16 clients are allottees, investors and construction contractors.",
     "I-16 Islamabad tax help for allottees, investors and construction contractors: plot costs, contract income and filer status in a developing sector.",
     """## Allottees and Investors

I-16 plots are mostly held for future development. Payments for allotment, development and possession build up the plot's cost. Investors who buy from allottees should keep the transfer letter and payment records.

## Construction Contractors

Contractors building homes and infrastructure in the new sectors receive payments from developers, authorities and households. Developers and government bodies deduct tax on payments. A contract register with amounts received and tax deducted is the foundation of the contractor's return.

## Suppliers of Building Materials

Brick, sand, steel and cement suppliers serving the new sectors deal in large volumes. Sales to companies may have tax deducted; purchase invoices and delivery records support profit.

## Getting Started

Allottees and investors should share allotment and payment papers; contractors their contracts and payment advices; suppliers their purchase and sales records. We prepare the returns and keep a running property or contract schedule.""",
     [("Is tax deducted from contractor payments in new sectors adjustable?",
       "For most contractors it is adjustable against their final liability, depending on the contract and the year's rules."),
      ("What records should a building materials supplier keep?",
       "Purchase invoices, delivery records and sales invoices, especially for sales to companies."),
      ("When do I declare an I-16 plot?",
       "From the first payment, as an asset at the amount paid, increasing as further charges are paid.")])

page("d-12-islamabad",
     "D-12 lies at the foot of the Margalla Hills on the western side of the city, with newer houses, green surroundings and a developing markaz. Our D-12 clients are families who have built or bought homes here and professionals working from home.",
     "D-12 Islamabad tax help for homeowners and professionals working from home: property records, rent, freelance income and wealth statements online.",
     """## Homeowners in a Newer Sector

Many D-12 homes were built in the last decade. The cost of land, construction and later improvements should all be reflected in the wealth statement. These records also matter for any future sale, because capital gains depend on cost.

## Professionals Working from Home

D-12's quieter setting attracts consultants and remote workers. Foreign income, consulting fees and expenses for a home office should be documented and declared.

## Letting Part of a House

Some owners let an annexe or upper portion. Rent is taxable and declared each year.

## Getting Started

Share the purchase or construction records for your house, your income documents and bank statements. We prepare a complete return and keep a property file that will be ready if you ever sell.""",
     [("Should I keep construction receipts after the house is finished?",
       "Yes. They establish the house's cost for the wealth statement and for capital gains if it is sold."),
      ("Can I claim home office costs as a consultant?",
       "A reasonable share of costs used for work can be claimed if supported by records."),
      ("Is rent from an annexe taxable?",
       "Yes, rent from any part of a house is income from property.")])

page("d12-islamabad",
     "This page covers D-12 from a plot investor's and builder's perspective: buying, developing and selling plots in a sector where demand has grown with new construction. Our clients here are investors, small builders and plot sellers.",
     "D-12 Islamabad plot investors and small builders: buying and selling plots, building homes for sale, advance tax and capital gains, filed online.",
     """## Buying Plots in D-12

Buyers pay advance tax under section 236K at registration: for transfers from 1 July 2026, 1.25% for persons on the Active Taxpayers List and 2.5% for others, plus CDA transfer charges. The purchase should be funded from declared income or savings.

## Building Homes to Sell

Small builders who buy a plot, build a house and sell it are running a business. Their profit is the sale price less land and construction costs and is taxed as business income, not as a capital gain. Separate records for each project are essential.

## Selling Investment Plots

Investors who sell a plot held for some time pay advance tax under section 236C and capital gains tax based on when the plot was acquired. Plots acquired from July 2024 are generally taxed at a flat rate for active filers.

## Getting Started

Share purchase deeds, CDA transfer letters, construction contracts and sale agreements. We work out the correct treatment for each plot or project and prepare the return.""",
     [("Is building and selling houses taxed as capital gains?",
       "No, building homes for sale is a business, and profit is taxed as business income."),
      ("What advance tax applies when buying a D-12 plot?",
       "For transfers from 1 July 2026, 1.25% under section 236K for active filers and 2.5% for others."),
      ("How is a plot bought after July 2024 taxed on sale?",
       "Generally at a flat capital gains rate for active filers, regardless of holding period.")])

page("d-13-islamabad",
     "D-13 is a developing sector next to D-12 at the edge of the Margalla Hills, where plot owners are waiting for development and early residents are starting to build. Our D-13 clients are plot owners and families planning construction.",
     "D-13 Islamabad tax help for plot owners and families planning to build: development charges, section 7E and funding records for construction.",
     """## Waiting for Development

D-13 owners often hold plots for years before building. During this time, payments for development charges add to cost, and owners with several properties should check section 7E each year.

## Planning Construction

Before construction begins, families should plan how it will be funded and documented. Savings, sale of other property, bank loans and gifts each need a clear record. Contracts with builders specifying payment stages make annual reporting easy.

## Selling Before Building

Some owners sell before development completes. Advance tax applies at transfer, and capital gains depend on the acquisition date. The original allotment or purchase documents are needed.

## Getting Started

Share your plot papers and payment receipts. If you are planning construction, tell us how it will be funded and we will show you how it should appear in your wealth statements over the coming years.""",
     [("Should I consider section 7E for my D-13 plot?",
       "Yes, if your total property value is above the aggregate limit and no exemption applies."),
      ("How should construction be funded on paper?",
       "From declared income, savings, documented loans or gifts, each recorded in the wealth statement."),
      ("Is selling my plot before development taxable?",
       "Yes; advance tax applies at transfer and capital gains depend on when you acquired it.")])

page("d-17-islamabad",
     "D-17 lies along the road towards Taxila and the western outskirts of Islamabad, with private housing schemes, farmhouses and roadside businesses. Our D-17 clients are scheme investors, farmhouse owners and business owners along the main road.",
     "D-17 Islamabad tax help for housing scheme investors, farmhouse owners and roadside businesses: property records, rent and business returns online.",
     """## Housing Scheme Investors

Private schemes in the D-17 area sell plots and files on instalments. Investors should check that a scheme is approved before buying and should keep every receipt. Files are assets in the wealth statement at the amount paid.

## Farmhouses

Farmhouses on the city's outskirts may be used as residences, let for events or used for agriculture. Event rentals are taxable income; genuine agricultural income is taxed by the province and declared as exempt in the federal return.

## Roadside Businesses

Restaurants, fuel stations and workshops along the main road serve travellers. Restaurants and workshops may fall under sales tax on services; fuel stations deal with petroleum products and have specific margins and records.

## Getting Started

Share purchase receipts for plots or files, farmhouse letting records, or business records. We prepare the return and advise on the treatment of each income stream.""",
     [("Is renting a farmhouse for events taxable?",
       "Yes, event rentals are taxable income and should be declared."),
      ("Should I check a scheme's approval before buying a file?",
       "Yes. Unapproved schemes carry legal risk, and the purchase still needs to be declared."),
      ("How do fuel station owners calculate profit?",
       "From sales and purchases of fuel at the applicable margins, plus other income, minus running costs.")])

page("b-16-islamabad",
     "The B-16 zone on the city's western side, along the road to Fateh Jang and the new airport, is an area of private housing schemes, farmland and new development. Our B-16 clients are investors, farmland owners and residents of the new schemes.",
     "B-16 Islamabad tax help for scheme investors, farmland owners and new residents near the new airport road: property, agriculture and filer status.",
     """## Farmland Owners

Agricultural land in this zone is taxed for agricultural income by the province, and declared as exempt income in the federal return. When farmland is sold to developers, the sale is a capital transaction that may attract advance tax and capital gains, depending on the land's status and the law at the time.

## Investors in New Schemes

New schemes near the airport road attract investors buying files and plots. Payments are assets in the wealth statement; sales of files are taxable gains.

## Residents Moving to the Area

Families moving to new schemes in B-16 and B-17 often sell property elsewhere. Documenting the sale and the purchase together explains the funding.

## Getting Started

Share your land record, scheme booking or allotment papers and payment receipts. We prepare the return and advise on how a land sale or purchase should be shown.""",
     [("Is selling farmland to a developer taxable?",
       "It can attract advance tax and capital gains depending on the land's status and dates; we review each case."),
      ("Do I declare agricultural income in the federal return?",
       "Yes, as exempt income, because it is taxed by the province."),
      ("How do I show a file in a new scheme?",
       "As an asset at the amount paid, increasing with each instalment.")])

page("b-18-islamabad",
     "B-18 lies further along the western growth corridor towards the new airport, where land is being converted from farms to housing schemes. Our B-18 clients are landowners selling to developers, early investors and local business owners.",
     "B-18 Islamabad tax help for landowners selling to developers, early investors and local businesses: land sales, agriculture and property records.",
     """## Landowners Dealing with Developers

When developers acquire farmland, landowners may receive cash, developed plots or a mix. Each form of payment has tax consequences. Plots received in exchange are new assets whose cost is linked to the land given up, and the agreement's wording matters.

## Early Investors

Investors who bought land early in the corridor's growth hold assets whose value has risen sharply. Their acquisition dates and costs determine the capital gains on sale.

## Local Businesses

Shops, workshops and transporters serving construction in the area keep business records and claim tax deducted by corporate customers.

## Getting Started

Landowners should share land records and any agreement with a developer before signing; investors their purchase papers; businesses their records. We advise on the correct treatment and prepare the returns.""",
     [("What if a developer pays me in plots instead of cash?",
       "The plots received are new assets and the land given up is treated as disposed of; the agreement's wording affects the tax."),
      ("How are early land investments taxed on sale?",
       "Capital gains depend on the acquisition date and cost; advance tax applies at transfer."),
      ("Can construction suppliers claim tax deducted by developers?",
       "Yes, as credits in their annual returns.")])
