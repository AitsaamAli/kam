"""Karachi area pages, part D: Nazimabad to Timber Market."""

PAGES = {}


def page(slug, lead, desc, body, faq):
    PAGES[f"blogs/tax-consultant-{slug}.html"] = {"lead": lead, "desc": desc, "body": body, "faq": faq}


page("nazimabad-karachi",
     "Nazimabad is one of Karachi's earliest planned neighbourhoods, with numbered sub-areas, old family houses, schools, hospitals and long-established markets. Our clients here are largely professional families, shop owners and owners of inherited homes.",
     "Nazimabad Karachi tax help for professional families, shop owners and inherited homes: returns, rental income, succession and wealth statements, online.",
     """## Old Family Houses

Many Nazimabad houses were built decades ago and are now shared among heirs, partly occupied and partly let out. Each heir declares their share of the house in the wealth statement and their share of any rent. When one heir buys out the others, that purchase is a separate transaction with its own advance tax and capital gains consequences.

## Teachers and Medical Staff

Nazimabad's schools, colleges and hospitals employ many residents. Teachers may qualify for reductions available to full-time teachers in recognised institutions, depending on the year's rules, and medical staff often have income from more than one employer. Each source needs its own certificate.

## Shopkeepers in Established Markets

Shops in Nazimabad's markets have often passed from father to son. When a business changes hands within a family, the new owner should register under their own NTN and start their own records, rather than continuing under a parent's name.

## Practical Record-Keeping

A folder for each year with salary certificates, bank certificates, rent receipts and property papers keeps filing simple. Many of our Nazimabad clients send the folder once a year and receive the filed return within days.

| Situation | What to do |
| Inherited house | Each heir declares their share |
| Buy-out among heirs | Treat as a separate sale |
| Shop passing to a son | New NTN and fresh records |""",
     [("How do heirs declare a shared Nazimabad house?",
       "Each heir shows their share of the house in their wealth statement and declares their share of any rent."),
      ("My father's shop is now mine. Can I use his NTN?",
       "No. Register under your own NTN and file your own returns from the year you take over."),
      ("Do teachers get any tax reduction?",
       "Full-time teachers and researchers at recognised institutions have had a reduction under the Second Schedule; we check whether it applies in your tax year.")])

page("new-karachi",
     "New Karachi in the north of the city has a large industrial area of textile, garment and engineering units next to crowded residential sectors. Our clients here include factory owners, small manufacturers, traders and the workers employed in the area.",
     "New Karachi tax consultant for industrial units, small manufacturers, traders and workers: sales tax registration, withholding, returns and refunds online.",
     """## Small and Medium Manufacturers

New Karachi's industrial area is home to power looms, knitting units, dyeing and engineering workshops. Most manufacturers need federal sales tax registration and must file monthly returns even when sales are slow. Input tax is claimable only on invoices from active registered suppliers, so supplier verification is a monthly task.

## Units Supplying Exporters

Many New Karachi units work as subcontractors for exporters in SITE and Korangi. Exporters may deduct tax on payments and require sales tax invoices. Keeping purchase orders, delivery challans and invoices together lets the unit claim credits and prove its turnover.

## Shopkeepers and Traders

The sectors' markets serve hundreds of thousands of residents. Traders keep purchase bills and simple sales records and claim the advance tax on commercial electricity bills.

## Workers and Supervisors

Workers with salary tax deducted can file to claim refunds and stay on the Active Taxpayers List. Supervisors with overtime and bonuses often have excess deductions by year end.

| Client | Monthly or annual task |
| Manufacturer | Sales tax return, supplier checks |
| Subcontractor | Matching invoices with buyer deductions |
| Trader | Annual return with credits |
| Worker | Refund claim if over-deducted |""",
     [("Does a small knitting unit in New Karachi need sales tax registration?",
       "Manufacturers are generally required to register for federal sales tax, subject to limited exceptions."),
      ("Can a subcontractor claim tax deducted by an exporter?",
       "Yes, the deduction is a credit in the subcontractor's return, supported by the exporter's certificate."),
      ("Why are supervisors often over-deducted?",
       "Overtime and bonuses paid late in the year can push monthly deductions above the true annual liability.")])

page("north-nazimabad-karachi",
     "North Nazimabad's lettered blocks hold some of Karachi's busiest markets, including the Hyderi area, alongside hospitals, schools and well-established family homes. Our clients from here are shop owners, doctors, school owners and salaried professionals.",
     "North Nazimabad Karachi tax help for Hyderi traders, doctors, school owners and professionals: returns, sales records, withholding and wealth statements.",
     """## Hyderi Market Traders

Garment, footwear, jewellery and electronics shops around Hyderi do high volumes, increasingly through card machines and bank transfers. These digital receipts are visible to FBR, so the declared turnover should match them. Jewellers should also keep stock records by weight, because gold stock is both the main asset and the main source of profit.

## Doctors and Hospitals

North Nazimabad has several large hospitals and many private clinics. Consultants working across them collect tax certificates from each and add private practice income. Hospitals and clinics themselves deduct tax from doctors' fees and file withholding statements.

## Private Schools

Schools in converted houses and purpose-built campuses are common. As employers, they deduct salary tax from teachers above the threshold. Fee income, concessions and arrears should be recorded consistently.

## Families with Long-Held Homes

Many family homes here were bought decades ago. When one is sold, the acquisition date and original cost decide the capital gains position, and the seller pays advance tax at registration.

| Client | Key record |
| Jeweller | Gold stock by weight, sales register |
| Garment retailer | Card machine statements, purchases |
| Doctor | Hospital tax certificates |
| School | Fee register, payroll |""",
     [("Can FBR see card sales at my Hyderi shop?",
       "Card and bank receipts leave a record, so declared turnover should match them."),
      ("How should a jeweller keep stock records?",
       "By weight and purity for gold and silver, with purchase and sale records, so that profit and closing stock can be worked out."),
      ("Does a private school deduct tax from teachers?",
       "Yes, where a teacher's salary is above the taxable threshold, and it files withholding statements.")])

page("orangi-town-karachi",
     "Orangi Town is one of the largest settlements in Pakistan, with self-built neighbourhoods, home-based industries and a strong tradition of community organisation. Our Orangi clients are mostly home-based manufacturers, small traders, transporters and wage earners.",
     "Orangi Town Karachi tax help for home industries, small traders, transporters and wage earners: NTN, simple records and returns, handled online.",
     """## Home-Based Industries

Weaving, embroidery, shoe-making and small assembly work are carried out in homes across Orangi, often for traders in the old city. Payments are frequently in cash and per piece. A record of pieces delivered and amounts received, kept in a notebook or on a phone, is enough to show income for a return.

## Small Traders and Shops

Neighbourhood shops supply daily needs on thin margins. Purchase bills from wholesalers, a monthly sales total and electricity bills are the basis for a simple return. Many owners are below the taxable threshold but benefit from filing.

## Transporters

Rickshaw, minibus and loader operators run much of Orangi's transport. Advance tax is collected with vehicle tax, and filing allows it to be adjusted. Operators who own several vehicles should keep a record per vehicle.

## Houses Built in Stages

Families often build their homes floor by floor over years. Each stage of construction is an investment that should appear in the wealth statement, funded by declared income, savings or remittances.

| Resident | Simple record |
| Home worker | Pieces delivered, payments |
| Shopkeeper | Wholesale bills, monthly sales |
| Transport operator | Per-vehicle income and costs |
| Family building a house | Construction costs by year |""",
     [("Can a home-based embroidery worker file a return?",
       "Yes. A simple record of work delivered and payments received supports the return, and filing helps when traders ask for an NTN."),
      ("How do I show a house built over several years?",
       "Add each year's construction cost to the house's value in the wealth statement, funded by income, savings or remittances."),
      ("Is the tax paid with rickshaw vehicle tax adjustable?",
       "Advance income tax collected with vehicle tax is adjustable when you file a return.")])

page("pechs-karachi",
     "PECHS (Pakistan Employees Cooperative Housing Society) combines residential blocks with some of Karachi's busiest commercial roads, including Tariq Road and stretches of Shahrah-e-Faisal. Clients here include retailers, office-based businesses, landlords and professionals.",
     "PECHS Karachi tax consultant for retailers, offices, landlords and professionals: sales tax, SRB, rental income and returns, prepared online.",
     """## Retail Along the Commercial Roads

Fashion, footwear and home-goods retailers in PECHS increasingly fall under FBR's point-of-sale rules for larger retailers, which report sales to FBR in real time. Their income tax returns must match those reported sales. Smaller shops not covered by POS still need purchase and sales records.

## Offices Along Shahrah-e-Faisal

Consultancies, software houses, travel agents and advertising firms operate from PECHS office buildings. Services provided in Sindh may require SRB registration, and corporate clients deduct income tax from invoices. Keeping a schedule of each client's deductions makes credits easy to claim.

## Landlords of Commercial Property

Owners of shops and office floors let to banks and chains receive rent with tax deducted. Rent from commercial property is a significant income for many PECHS families and must be declared together with the credits.

## Residents

PECHS residential blocks house professionals and business families whose returns combine salary or business income with rent and investments.

| Client | Main concern |
| Large retailer | POS-reported sales match the return |
| Office business | SRB registration and client deductions |
| Commercial landlord | Rent with tax deducted |
| Resident family | Combined income and wealth statement |""",
     [("Is my PECHS shop required to use FBR's POS system?",
       "Larger retailers meeting FBR's criteria must integrate; smaller shops are not covered but still keep sales records."),
      ("Do PECHS consultancies need SRB registration?",
       "If they provide taxable services in Sindh above the threshold, yes."),
      ("Is rent from a shop let to a bank taxable?",
       "Yes. The bank deducts tax at source, which you claim as a credit in your return.")])

page("qasba-colony-karachi",
     "Qasba Colony in west Karachi, near Manghopir and Orangi, is home to many families from Khyber Pakhtunkhwa working in transport, construction and trade. Our clients here are transporters, builders, small traders and families with members abroad.",
     "Qasba Colony Karachi tax help for transporters, construction contractors, traders and remittance families: returns, vehicle tax credits, filer status.",
     """## Transport Owners

Many Qasba Colony families own buses, trucks or water tankers. Each vehicle pays advance income tax with its vehicle tax, and freight from companies may have tax deducted. Filing a return lets these amounts be adjusted against actual income.

## Construction Contractors and Labour

Residents work as contractors and skilled labour on construction sites across Karachi. Contractors paid by companies or government departments have tax deducted on their bills. A contract register with amounts received and tax deducted is the basis of the return.

## Traders

Shops dealing in building materials, dry fruit and general goods serve the area. Purchase bills and stock counts support the profit figure.

## Families with Members in the Gulf

Remittances from Saudi Arabia and the UAE fund houses and vehicles. Remittances through banks are not the receiver's taxable income, but assets bought with them belong in the wealth statement with the bank record as proof.

| Client | Credits or records |
| Transporter | Vehicle tax receipts, freight deductions |
| Contractor | Contract register, bill deductions |
| Trader | Purchase bills, stock count |
| Remittance family | Bank advices for each transfer |""",
     [("Can a water tanker owner claim the tax paid with vehicle tax?",
       "Yes, the advance income tax collected with vehicle tax is adjustable in the annual return."),
      ("Is tax deducted from construction bills final?",
       "For most contractors it is adjustable against the final liability, depending on the contract type and the year's rules."),
      ("Do I pay tax on money my brother sends from Saudi Arabia?",
       "Remittances through banks are generally not your taxable income, but assets they fund should be in your wealth statement.")])

page("saddar-karachi",
     "Saddar is Karachi's historic commercial centre, with Empress Market, the electronics markets on Abdullah Haroon Road, bookshops, offices and wholesale trade of every kind. Our Saddar clients are traders, importers, professionals and office-based firms.",
     "Saddar Karachi tax consultant for traders, electronics importers, professionals and offices: profit records, import taxes, SRB and returns, online.",
     """## Electronics and Mobile Phone Trade

Saddar's electronics markets deal in imported phones, accessories and appliances. Importers pay customs duty, sales tax and advance income tax at the port, and the advance income tax is usually adjustable in their returns. Retailers buying from importers should keep invoices that show these taxes.

## Wholesale and Retail Traders

From cloth to crockery, Saddar's traders work with high volumes and narrow margins. Profit is calculated from purchases, sales and closing stock, and the minimum tax on turnover can apply in some cases. Bank deposits are compared with declared turnover, so they should be consistent.

## Lawyers, Accountants and Professionals

Saddar's offices house lawyers, chartered accountants and consultants. Professional fees from companies come with tax deducted; fees from individuals do not. Professionals providing services in Sindh may also need SRB registration.

## Old Buildings and Rent

Many Saddar shops sit in old buildings with long-standing tenancies at low rents. Landlords still declare the rent they receive, however small, and keep tenancy records.

| Client | Key point |
| Electronics importer | Import-stage advance tax credit |
| Wholesaler | Profit from purchases, sales and stock |
| Professional | Client deductions, SRB if applicable |
| Landlord | Rent declared even if small |""",
     [("Is the advance tax paid at import adjustable?",
       "Advance income tax collected at the import stage is generally adjustable against the importer's final liability."),
      ("Do Saddar lawyers need SRB registration?",
       "Legal and professional services can be taxable in Sindh; registration depends on the service and turnover."),
      ("Must I declare a very small rent from an old tenancy?",
       "Yes. All rent received is declared, regardless of amount.")])

page("seaview-karachi",
     "Seaview is Karachi's seafront strip along DHA and Clifton, with apartment towers, restaurants, cafes and leisure businesses. Our clients from Seaview are apartment owners, restaurant and cafe operators and residents of the beachfront towers.",
     "Seaview Karachi tax help for apartment owners, restaurants and cafes: SRB sales tax, rental income from sea-facing flats and returns, done online.",
     """## Restaurants and Cafes on the Seafront

Seaview's food businesses are busy in the evenings and on weekends, with a large share of card payments. They charge Sindh sales tax on services through the Sindh Revenue Board and file a federal income tax return. Daily sales summaries from the till should match both the SRB returns and the annual return.

## Sea-Facing Apartments Let Out

Apartments in Seaview towers are often let to executives and expatriates, sometimes through companies that deduct tax from rent. Short-term lets through online platforms are also growing. Both kinds of rent are taxable and should be declared.

## Apartment Buyers

Seaview apartments are high-value purchases. For transfers from 1 July 2026, buyers pay advance tax of 1.25% under section 236K if on the Active Taxpayers List and 2.5% otherwise. The purchase should be funded from declared income, savings or loans recorded in the wealth statement.

## Building Management and Maintenance

Owners pay maintenance charges to building management. These are household expenses for a self-occupied flat; for a let-out flat, check what can be claimed under the rules for that year.

| Client | Main filing |
| Restaurant | SRB returns and income tax return |
| Landlord | Rent, including short-term lets |
| Buyer | Advance tax and funding in wealth statement |""",
     [("Is short-term rental income from a Seaview flat taxable?",
       "Yes. Rent from short-term and long-term lets is taxable and should be declared."),
      ("Do seafront cafes pay SRB tax?",
       "Restaurant and cafe services in Sindh are generally subject to Sindh sales tax on services."),
      ("What advance tax applies when buying a Seaview apartment?",
       "For transfers from 1 July 2026, 1.25% under section 236K for active filers and 2.5% for others.")])

page("shah-faisal-colony-karachi",
     "Shah Faisal Colony near Drigh Road and the airport is a long-established residential area of government employees, airline and railway staff and small businesses. Our clients here are salaried employees, retirees and shopkeepers.",
     "Shah Faisal Colony Karachi tax help for government, airline and railway staff, retirees and shopkeepers: returns, refunds and filer status, online.",
     """## Government and Public Sector Employees

Many residents work or worked for the federal government, the airline and the railways. Their salary tax is deducted monthly and they receive detailed pay slips. Filing a return claims any excess deductions and keeps them on the Active Taxpayers List.

## Retirees

Government pension and commutation are exempt, but profit on the savings that many retirees keep in banks and National Savings is taxable through withholding. Being an active filer keeps that deduction at the lower rate.

## Shopkeepers and Small Businesses

Shops and service businesses on the colony's main roads keep purchase records and claim electricity bill tax. Most are small, and a simple return is enough.

## Families Helping Children Buy Property

Retired parents often help children buy flats with commutation money. The gift should be shown in both the parent's and the child's wealth statements, ideally made through a bank transfer.

| Resident | Main benefit of filing |
| Serving employee | Refund of excess salary tax |
| Retiree | Lower tax on savings profit |
| Shopkeeper | Electricity bill tax credit |""",
     [("Is commutation of government pension taxable?",
       "No. Commutation of government pension is exempt, as is the monthly pension."),
      ("How do I show money given to my son for a flat?",
       "As a gift in your wealth statement and as a receipt in his, preferably supported by a bank transfer."),
      ("Can railway employees claim refunds?",
       "Yes, if salary tax deducted exceeded their actual liability, by filing a return.")])

page("site-karachi",
     "SITE (Sindh Industrial Trading Estate) is Karachi's oldest and one of its largest industrial estates, home to textile mills, garment exporters, chemical and engineering plants. Our SITE clients are manufacturers, exporters, vendors and their finance teams.",
     "SITE Karachi tax consultant for textile mills, exporters, vendors and finance teams: sales tax, export regime, withholding statements and returns.",
     """## Textile and Garment Exporters

SITE's mills and garment units export through banks, with tax deducted on proceeds. Since recent budgets moved many exporters of goods towards the normal regime, the deduction can act as minimum tax and the return must show profit. Sales tax refunds on inputs, or input purchases under the Export Facilitation Scheme, add a monthly compliance load.

## Vendors to the Mills

Suppliers of yarn, dyes, spare parts and services deal with mills that deduct income tax and require sales tax or SRB registration. Vendors who are not active on the Sales Tax Active Taxpayers List can lose business, because buyers cannot claim input tax on their invoices.

## Finance Teams

Large SITE employers deduct salary tax for hundreds of workers and file withholding statements. Reconciling payroll, statements and employees' tax certificates every quarter avoids mismatches.

## Utilities and Energy Costs

Industrial electricity and gas bills include advance income tax and sales tax. Manufacturers registered for sales tax claim input tax on utilities, and the advance income tax is adjustable in the annual return.

| Client | Recurring task |
| Exporter | Proceeds records, refunds, annual return |
| Vendor | Active registration, invoices |
| Finance team | Withholding statements, reconciliations |
| Manufacturer | Utility tax credits |""",
     [("Are SITE exporters taxed on final or normal regime?",
       "Many exporters of goods now fall under the normal regime with the export deduction acting as minimum tax; we confirm each year's treatment."),
      ("Why must vendors stay on the Sales Tax Active Taxpayers List?",
       "Buyers cannot claim input tax on invoices from inactive suppliers, so inactive vendors lose business."),
      ("Is tax on industrial electricity bills adjustable?",
       "The advance income tax on industrial bills is adjustable in the annual return, and registered manufacturers can claim the sales tax as input.")])
