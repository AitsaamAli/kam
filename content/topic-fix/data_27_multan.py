"""Multan city and area pages."""

PAGES = {}


def page(slug, lead, desc, body, faq, kind="tax-consultant"):
    PAGES[f"blogs/{kind}-{slug}.html"] = {"lead": lead, "desc": desc, "body": body, "faq": faq}


page("multan",
     "Multan, the commercial centre of southern Punjab, lives on cotton, mangoes, grain and the trade that moves them, alongside a large population of government employees, doctors and shrine-linked businesses. Tax questions here often start with agriculture and end with trading and property.",
     "Multan tax consultant for cotton ginners, mango and grain traders, landowners, doctors and families: FBR returns, PRA services tax and property, online.",
     """## Agriculture and Trade Side by Side

Many Multan families own farmland in the surrounding districts and run trading businesses in the city. Agricultural income is taxed by the Punjab government and is declared as exempt in the federal return, while trading profit is taxed by FBR. Keeping the two apart in bank accounts and records prevents agricultural receipts from looking like unexplained business income, and vice versa.

## Cotton and Ginning

Ginning factories around Multan buy seed cotton at harvest and sell lint to mills and seed to oil expellers. They deal with large seasonal cash flows, sales tax on lint and deductions by mills. Weight and quality records for each lot are as important as invoices.

## Mangoes and Fruit Exports

Orchard owners sell mangoes to contractors or exporters. Orchard income is agricultural, but exporters and fruit contractors who buy, pack and sell earn business income. Export proceeds are received through banks with tax deducted.

## Doctors and Hospitals

Nishtar Hospital and many private hospitals make Multan a medical centre for the south. Doctors declare salaries and private practice income together.

## Getting Started

Share your land records, ginning or trading records, or salary and practice records. We prepare returns and PRA filings remotely.""",
     [("Is mango orchard income taxed by FBR?",
       "Orchard income from your own land is agricultural and taxed by the province; buying and exporting fruit is business income taxed by FBR."),
      ("Do Multan ginners pay sales tax?",
       "Sales of cotton lint are generally subject to sales tax, so ginners usually register."),
      ("Why keep farm and business money in separate accounts?",
       "It shows clearly which receipts are exempt agricultural income and which are taxable business income.")])

page("multan",
     "Multan residents register for an NTN when they start trading, join the ginning or fruit export business, take government contracts or prepare to buy property. Registration is online through IRIS, followed by sales tax or PRA registration where the business needs it.",
     "NTN registration in Multan for traders, ginners, fruit exporters and contractors: IRIS steps, documents and follow-on sales tax or PRA registration.",
     """## Who Registers in Multan

- **Ginners and cotton traders** who need sales tax registration to sell to mills.
- **Fruit contractors and exporters** dealing with banks and foreign buyers.
- **Contractors** working for government departments in the south.
- **Freelancers and students** at Multan's universities earning from abroad.

## Registration Steps

1. Register on IRIS with CNIC, your own mobile number and email.
2. Verify the codes.
3. Enter address and income source; add business details where relevant.
4. Submit and download the NTN certificate.

## Seasonal Businesses

Ginning and mango export are seasonal. Register well before the season so bank accounts, sales tax registration and export documentation are ready when trade begins.

## PRA for Services

Service businesses in Multan register with the Punjab Revenue Authority after obtaining an NTN.

## Getting Started

Send your CNIC and business details on WhatsApp. NTN registration is Rs 2,000 on our [pricing page](/pricing).""",
     [("When should a ginner register?",
       "Before the cotton season starts, so sales tax registration and banking are in place when buying begins."),
      ("Do fruit exporters need an NTN?",
       "Yes, exporters need an NTN and proper export documentation; banks deduct tax on proceeds."),
      ("Does an NTN put me on the Active Taxpayers List?",
       "No, only after you file a return.")],
     kind="ntn-registration")

page("cantt-multan",
     "Multan Cantonment houses military establishments, officers' residences and a commercial area under the cantonment board. Our Multan Cantt clients are officers, retired personnel, civilian staff and cantonment businesses.",
     "Multan Cantt tax help for officers, retired personnel, civilian staff and cantonment businesses: salary, pension, allotted plots and returns online.",
     """## Officers and Allotted Plots

Officers posted to Multan often hold plots allotted through defence schemes, sometimes in Multan's own defence housing. These are shown at the amounts paid. Officers' salaries are taxed at source.

## Retired Personnel

Many retired officers settle in Multan, often with agricultural land in nearby districts. Pension is exempt, agricultural income is declared as exempt, and rent and profit are taxable.

## Cantonment Businesses

Shops, restaurants and service providers in the cantonment's markets file FBR returns and register with PRA for taxable services.

## Cantonment Property

The cantonment board collects property tax and manages transfers.

## Getting Started

Share salary or pension statements, allotment letters, land records or business records. We prepare the returns.""",
     [("Is agricultural income of retired officers taxable by FBR?",
       "No, it is taxed by the province and declared as exempt income in the federal return."),
      ("Who collects property tax in Multan Cantt?",
       "The cantonment board."),
      ("Do cantonment restaurants file with PRA?",
       "Yes, restaurant services are generally taxable under the Punjab law.")])

page("chungi-no-9-multan",
     "Chungi No. 9 is one of Multan's busiest junctions, surrounded by markets, workshops, transport offices and dense residential streets. Our clients here are traders, transporters, workshop owners and families.",
     "Chungi No. 9 Multan tax help for traders, transporters, workshops and families around the junction: records, vehicle tax credits and returns online.",
     """## Traders Around the Junction

Shops selling auto parts, hardware and household goods serve the city and travellers. Purchase invoices, sales records and electricity bills support returns.

## Transport Offices

Goods and passenger transport offices near the junction book cargo and seats. Fleet owners earn freight and fares; agents earn commission. Advance tax paid with vehicle tax is adjustable.

## Workshops

Auto workshops provide repairs, which may be taxable under the Punjab law depending on turnover. Job cards and parts invoices support income.

## Families

Households file salaried returns and declare any rent from shops or portions.

## Getting Started

Share purchase records, trip or booking records, job cards or salary certificates. We prepare the returns.""",
     [("Are booking agents taxed on full fares?",
       "No, only on their commission."),
      ("Do auto workshops in Multan register with PRA?",
       "Repair services can be taxable under the Punjab law once turnover crosses the threshold."),
      ("Can transporters claim tax paid with vehicle tax?",
       "Yes, it is adjustable in the annual return.")])

page("garden-town-multan",
     "Garden Town in Multan is a planned residential area with family houses, schools and nearby markets, popular with professionals and business families. Our Garden Town clients are families, doctors, teachers and landlords.",
     "Garden Town Multan tax help for families, doctors, teachers and landlords: salary and professional income, rent and wealth statements filed online.",
     """## Professional Families

Doctors at Nishtar and private hospitals, university teachers and bank officers live in Garden Town. Salaries are taxed at source; private practice, tuition and consulting are declared separately.

## Landlords

Houses and portions let to families and offices produce rent, declared each year; office tenants may deduct tax.

## Families with Farmland

Many Garden Town families own agricultural land nearby. Agricultural income is declared as exempt; its records explain assets bought with farm income.

## Property Purchases

Houses in Garden Town change hands at substantial prices. Filing before a purchase lowers the advance tax.

## Getting Started

Share salary certificates, practice records, tenancy agreements and land records. We prepare returns for the household.""",
     [("Do university teachers in Multan get tax reductions?",
       "Full-time teachers and researchers at recognised institutions have had a reduction under the Second Schedule; we check the year's rules."),
      ("How does farm income help explain assets?",
       "Declared as exempt income, it shows the source of funds for property or vehicles."),
      ("Does filing lower advance tax on buying a house?",
       "Yes, persons on the Active Taxpayers List pay a lower rate under section 236K.")])

page("multan-garden-town-multan",
     "This page looks at Multan's Garden Town area from the perspective of its commercial strip and small businesses, rather than its residents: clinics, pharmacies, academies and shops that serve the neighbourhood.",
     "Multan Garden Town businesses: clinics, pharmacies, academies and shops on the commercial strip, with PRA, records and returns filed online.",
     """## Clinics and Laboratories

Clinics and diagnostic labs along Garden Town's commercial roads earn fees from patients and panels. Laboratories invest in equipment, depreciated over time, and employ technicians whose salaries may require tax deduction.

## Pharmacies

Pharmacies keep distributor invoices and stock records; profit is the margin on medicines sold.

## Academies

Coaching academies preparing students for entry tests charge fees and pay teachers per course. Fee registers and teacher payment records support their returns.

## Shops

Bakeries, grocery stores and boutiques keep purchase and sales records and claim electricity bill tax.

## Getting Started

Share fee records, invoices, stock lists and bank statements. We prepare the returns.""",
     [("How do labs claim equipment costs?",
       "Through depreciation over the equipment's useful life, with invoices as support."),
      ("How are academy teachers' payments recorded?",
       "As expenses for the academy and income for the teachers."),
      ("Do pharmacies need stock records?",
       "Yes, stock and purchase invoices determine the cost of medicines sold.")])

page("gulgasht-multan",
     "Gulgasht Colony is Multan's best-known upscale residential area, home to business families, landowners, senior professionals and many of the city's restaurants and boutiques along Bosan Road. Our Gulgasht clients are business and landowning families, professionals and commercial landlords.",
     "Gulgasht Multan tax help for landowning and business families, professionals and Bosan Road businesses: returns, rent, property and wealth statements.",
     """## Landowning Families

Many Gulgasht families own large agricultural holdings in southern Punjab. Agricultural income is declared as exempt in the federal return, but income from businesses, rent and investments is taxable. Lifestyle spending should be consistent with total declared income, both exempt and taxable.

## Business Owners

Ginners, traders and industrialists live in Gulgasht. Personal returns should reconcile with business drawings and dividends.

## Bosan Road Businesses

Restaurants, cafes and boutiques along Bosan Road charge PRA tax on services where applicable and file FBR returns.

## Commercial Landlords

Buildings let to banks, brands and restaurants produce rent with tax deducted by corporate tenants.

## Getting Started

Share land records, business accounts, tenancy agreements and bank statements. We prepare returns for each family member together.""",
     [("Can large agricultural income explain an expensive lifestyle?",
       "Yes, if properly declared as exempt income with land and sale records; undeclared, it cannot."),
      ("Do Bosan Road restaurants pay PRA tax?",
       "Restaurant services are generally taxable under the Punjab law."),
      ("Is rent from a bank tenant taxed at source?",
       "Yes, banks deduct tax from rent.")])

page("low-income-scheme-multan",
     "Multan's low-income housing schemes were built to give working families affordable homes, and today house labourers, drivers, small shopkeepers and government workers. Our clients here are first-time filers and small businesses.",
     "Multan low-income housing scheme tax help for working families and small shopkeepers: simple returns, NTN and Active Taxpayers List status online.",
     """## Families in Affordable Housing

Houses allotted or bought in these schemes are often the family's only property. They belong in the wealth statement at cost, including instalments paid to the authority.

## Small Shopkeepers

Corner shops and repair stalls serve the scheme. Simple purchase and sales records are enough for a return.

## Workers

Drivers, labourers and security guards usually earn below the taxable threshold but benefit from filing through lower filer rates.

## Help from Relatives

Money from relatives abroad or in other cities, if it funds a house or vehicle, should be recorded with bank transfers.

## Getting Started

Send your CNIC, bank statement and house documents on WhatsApp 0328-4675162. We prepare a simple return.""",
     [("Do I need to file if my income is low?",
       "Not always, but filing gives access to lower filer rates and builds a record."),
      ("How do I show a house bought on instalments?",
       "At the amounts paid, as an asset in the wealth statement."),
      ("What does a simple return cost?",
       "A salaried return is Rs 3,500 on our pricing page.")])

page("new-multan",
     "New Multan is a large residential area with blocks of houses, schools, mosques and markets, home to government employees, teachers and small business families. Our New Multan clients are salaried families, teachers and shopkeepers.",
     "New Multan tax help for government employees, teachers and shopkeepers: salaried returns, refunds, rent and simple business records online.",
     """## Government Employees and Teachers

Provincial and federal employees and school teachers form a large part of New Multan's population. Their salary tax is deducted, and many are owed refunds from arrears or over-deduction.

## Shopkeepers

Neighbourhood shops keep purchase records and monthly sales and claim tax paid on electricity bills.

## Portions Let to Families

Families let upper portions to tenants. Rent is declared each year.

## Families with Farmland

Some families own small farms nearby; agricultural income is declared as exempt.

## Getting Started

Share salary certificates, shop records, tenancy agreements and land records. We prepare returns for each earner.""",
     [("Can teachers in New Multan claim refunds?",
       "Yes, if tax deducted exceeds their liability."),
      ("Is rent from an upper portion taxable?",
       "Yes, rent is declared each year."),
      ("Do I declare a small family farm?",
       "Yes, the land is an asset and its income is declared as exempt agricultural income.")])

page("shah-rukn-e-alam-multan",
     "Shah Rukn-e-Alam Colony, named after the shrine that dominates Multan's skyline, is a residential area with markets, workshops and families involved in the old city's trades. Our clients here are traders, artisans and families.",
     "Shah Rukn-e-Alam Colony Multan tax help for traders, artisans and families: records, returns and filer status for small businesses, online.",
     """## Artisans and Crafts

Multan's crafts, including blue pottery, camel-skin lamps and embroidered textiles, are made by artisans in and around the old city. Artisans selling to shops or exporters earn business income from sales after materials.

## Traders Serving Visitors

Shops near the shrine sell souvenirs, sweets and religious items, with peaks during urs and religious occasions. Daily records of sales are important.

## Families

Households combine income from trades, jobs and remittances. Each earner files, and assets are declared.

## Exporting Crafts

Artisans and dealers selling crafts abroad receive proceeds through banks, with tax deducted under the export rules.

## Getting Started

Share sales records, material invoices or salary certificates. We prepare the returns.""",
     [("How are Multani craft artisans taxed?",
       "On business income from sales after material and other costs."),
      ("Do souvenir shops near the shrine need daily records?",
       "Yes, because sales peak around religious events and vary widely."),
      ("Is tax deducted on craft exports?",
       "Banks deduct tax on export proceeds under the export rules.")])

page("vehari-road-multan",
     "Vehari Road leads east out of Multan towards Vehari, lined with ginning factories, oil mills, warehouses and transport businesses that serve the cotton belt. Our Vehari Road clients are ginners, oil millers, warehouse owners and transporters.",
     "Vehari Road Multan tax help for ginners, oil mills, warehouses and transporters: sales tax, seasonal cash flows, records and returns, filed online.",
     """## Ginning Factories

Ginners along Vehari Road buy seed cotton from farmers and middlemen and sell lint to spinning mills. Sales tax on lint, deductions by mills and seasonal cash purchases make careful records essential: purchase slips with weights, lint bale numbers and invoices.

## Oil Mills and Expellers

Cottonseed is crushed for oil and cake, sold to ghee mills and feed makers. Oil mills usually need sales tax registration and keep production records showing seed used and output.

## Warehouses

Warehouses store cotton bales and grain. Rent from corporate tenants often has tax deducted; storage services may be taxable under the Punjab law.

## Transporters

Trucks carrying cotton and seed earn freight, with advance tax paid with vehicle tax adjustable.

## Getting Started

Share purchase slips, sales invoices, production records or trip records. We prepare returns and sales tax filings.""",
     [("What records should a ginner keep?",
       "Purchase slips with weights and prices, bale numbers, and sales invoices to mills."),
      ("Do oil mills need sales tax registration?",
       "Oil mills producing taxable goods generally do."),
      ("Is warehouse storage taxable in Punjab?",
       "Storage services can be taxable under the Punjab law depending on turnover.")])

page("wapda-city-multan",
     "WAPDA Town in Multan was developed for employees of the power sector and has grown into a residential area of engineers, utility staff, retirees and other families. Our clients here are utility employees, retirees and landlords.",
     "WAPDA Town Multan tax help for power sector employees, retirees and landlords: salary, free electricity benefits, pensions and returns online.",
     """## Power Sector Employees

Employees of distribution companies and WAPDA receive salaries with allowances and, in many cases, free or subsidised electricity units. Such benefits are valued and taxed under the perquisite rules and should appear on the salary certificate.

## Retirees

Retired utility employees draw pensions that may be exempt depending on the scheme. Rent and profit are taxable.

## Landlords

Houses in WAPDA Town are let to families; rent is declared each year.

## Families

Households should file together so gifts and joint assets match.

## Getting Started

Share salary certificates, pension statements and tenancy agreements. We prepare the returns.""",
     [("Is free electricity for WAPDA employees taxable?",
       "Benefits such as free electricity units are valued under the perquisite rules and included in taxable salary."),
      ("Is a power sector pension exempt?",
       "Government and similar pensions are generally exempt; we check your scheme."),
      ("Is rent from a WAPDA Town house taxable?",
       "Yes, rent is declared each year.")])
