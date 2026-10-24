"""Faisalabad city and area pages."""

PAGES = {}


def page(slug, lead, desc, body, faq, kind="tax-consultant"):
    PAGES[f"blogs/{kind}-{slug}.html"] = {"lead": lead, "desc": desc, "body": body, "faq": faq}


page("faisalabad",
     "Faisalabad is Pakistan's textile capital, where spinning mills, weaving units, processing plants and garment exporters sit alongside the cloth markets around the Clock Tower and a large population of traders and workers. Tax work here is dominated by sales tax, exports and the records that link a mill's purchases to its sales.",
     "Faisalabad tax consultant for textile mills, power looms, exporters and cloth traders: sales tax, export regime, PRA services tax and returns online.",
     """## The Textile Chain

Faisalabad's textile chain runs from yarn spinners to weavers, processors, stitching units and exporters. Each link buys from the previous one and sells to the next, usually with sales tax invoices. A gap anywhere in the chain, such as an unregistered weaver or a supplier who stops filing, breaks the input tax trail for everyone downstream. Supplier verification is therefore a monthly task, not an annual one.

## Exporters

Exporters of home textiles and garments receive proceeds through banks with tax deducted. Recent budgets moved many exporters of goods towards the normal tax regime, where the deduction works as minimum tax and the return must show actual profit. Sales tax refunds and the Export Facilitation Scheme add monthly compliance.

## Cloth Markets

The bazaars around the Clock Tower and the wholesale cloth markets trade in large volumes on credit. Traders' returns depend on purchase and sales records and on bank deposits that match declared turnover.

## Services and PRA

Services provided in Faisalabad, such as dyeing on job-work, courier, restaurants and consultancy, can be taxable under the Punjab Revenue Authority's law.

## Getting Started

Share sales tax returns, supplier lists, export records or trade ledgers on WhatsApp 0328-4675162. Fees are on our [pricing page](/pricing).""",
     [("Why is supplier verification so important in Faisalabad's textile chain?",
       "Input tax can only be claimed on invoices from active registered suppliers; one inactive supplier breaks the claim for its buyers."),
      ("Are Faisalabad exporters on the final tax regime?",
       "Many exporters of goods now fall under the normal regime with the export deduction acting as minimum tax; we confirm each year's treatment."),
      ("Is job-work dyeing taxed by PRA?",
       "Processing on job-work can be a taxable service under the Punjab law depending on its nature and turnover.")])

page("faisalabad",
     "Faisalabad residents and businesses register for an NTN before opening business accounts, supplying mills, registering for sales tax or buying property. Registration is online through IRIS, and many textile businesses follow it with sales tax registration.",
     "NTN registration in Faisalabad: IRIS steps, documents for weavers, traders and freelancers, and when sales tax or PRA registration is also needed.",
     """## Who Registers in Faisalabad

- **Power loom owners** and small weavers supplying mills, which increasingly require an NTN and sales tax registration.
- **Cloth traders** opening business accounts and dealing with registered buyers.
- **Freelancers and students** at the city's universities earning from abroad.
- **Families** buying property who want the lower filer rate.

## Steps on IRIS

1. Register with your CNIC, your own mobile number and email.
2. Verify the codes received.
3. Enter your address and income source; for a business, add its name, address and activity, such as weaving or trading.
4. Submit and download the certificate.

## Weavers and Sales Tax

Mills buying from small weavers can only claim input tax if the weaver is registered and active. Many weavers therefore need sales tax registration soon after the NTN. Registration requires premises details and, often, a physical verification of the unit.

## PRA for Services

Businesses providing taxable services in Faisalabad register with the Punjab Revenue Authority after the NTN.

## Getting Started

Send your CNIC and business details on WhatsApp. NTN registration is Rs 2,000 and sales tax registration Rs 3,000 on our [pricing page](/pricing).""",
     [("Do small power loom owners need sales tax registration?",
       "If they supply registered mills that want to claim input tax, registration is usually needed."),
      ("Is the weaving unit inspected during registration?",
       "Sales tax registration often involves verification of the business premises."),
      ("Does an NTN make me an active filer?",
       "No, only filing a return puts you on the Active Taxpayers List.")],
     kind="ntn-registration")

page("faisalabad-district",
     "Beyond the city, Faisalabad district includes Jaranwala, Samundri, Tandlianwala, Chak Jhumra and hundreds of villages where farming, livestock, cotton ginning and small textile units shape the economy. Our district clients are landowners, ginners, rural traders and village-based weavers.",
     "Faisalabad district tax help for landowners, cotton ginners, rural traders and village weavers in Jaranwala, Samundri and Tandlianwala: returns online.",
     """## Landowners

Agricultural income is taxed by the Punjab government and declared as exempt income in the federal return. Landowners should keep their fard and records of crop sales, especially when sale proceeds fund property or vehicles.

## Cotton Ginners

Ginning factories buy seed cotton from farmers and sell lint and cottonseed to mills and oil expellers. Ginners usually need sales tax registration and keep careful weight and quality records. Their profit depends on the margin between seed cotton prices and lint and seed sales.

## Village Weavers

Power looms in villages around the city weave cloth for Faisalabad's traders and mills. Payments are often per metre. Records of cloth delivered and payments received support their returns, and registration helps them supply registered buyers.

## Rural Traders and Arhtis

Commission agents in the grain markets of the district towns earn commission on sales of wheat and other crops; amounts passed on to farmers are not their income.

## Getting Started

Share your land records, ginning or weaving records, or trading ledgers. We prepare returns for district clients remotely.""",
     [("Is agricultural income in Faisalabad district taxed by FBR?",
       "No, it is taxed by Punjab and declared as exempt income in the federal return."),
      ("Do cotton ginners need sales tax registration?",
       "Ginners supplying registered mills generally do."),
      ("How are arhtis in Jaranwala taxed?",
       "On commission earned; money passed to farmers is not their income.")])

page("d-ground-faisalabad",
     "D-Ground in People's Colony is one of Faisalabad's busiest commercial areas, with brand outlets, restaurants, banks and offices drawing shoppers from across the city. Our D-Ground clients are retailers, restaurant owners and owners of commercial property.",
     "D-Ground Faisalabad tax help for brand outlets, restaurants and commercial property owners: POS rules, PRA services tax, rent and returns online.",
     """## Brand Outlets and Retailers

Clothing and lifestyle brands at D-Ground often fall under FBR's point-of-sale requirements for larger retailers, which report each sale in real time. Their income tax returns must match POS data. Smaller shops keep sales records that match card and wallet receipts.

## Restaurants and Cafes

D-Ground's food outlets charge sales tax on services under the Punjab Revenue Authority's law and file income tax returns with FBR. Daily sales summaries should agree with both.

## Commercial Property Owners

Owners of shops and floors let to brands and banks receive substantial rent, often with tax deducted by corporate tenants. Rent is declared each year, and the property is in the wealth statement at cost.

## Offices

Professional firms and agencies above the shops deduct tax from staff and may need PRA registration for their services.

## Peak Seasons

Eid and wedding seasons bring sales peaks. Daily deposits into business accounts create a clear record.

## Getting Started

Share POS or card reports, PRA returns, tenancy agreements and bank statements. We prepare the returns.""",
     [("Do D-Ground brand outlets have to integrate with FBR's POS?",
       "Larger retailers meeting FBR's criteria must integrate; smaller shops still keep matching sales records."),
      ("Do restaurants in Faisalabad file with PRA?",
       "Yes, restaurant services are generally taxable under the Punjab law."),
      ("Is rent from a brand outlet taxed at source?",
       "Corporate tenants usually deduct tax from rent, which the owner claims as a credit.")])

page("batala-colony-faisalabad",
     "Batala Colony is a busy residential and commercial neighbourhood of Faisalabad, with markets, workshops, small textile units and families involved in the city's cloth trade. Our Batala Colony clients are traders, small manufacturers and salaried families.",
     "Batala Colony Faisalabad tax help for cloth traders, small textile units and salaried families: sales tax, records and returns, filed online.",
     """## Small Textile Units

Embroidery, stitching and finishing units operate from Batala Colony's lanes, often working for larger traders and exporters. Buyers may deduct tax and require registration. Purchase orders, delivery challans and invoices together show turnover and support credits.

## Cloth Traders

Traders buying from weavers and selling to retailers across Punjab keep ledgers of credit sales. Bank deposits should match declared turnover.

## Workshops and Repairs

Machinery repair workshops serving power looms provide services that may be taxable under the Punjab law.

## Salaried Families

Residents working in mills, banks and schools file salaried returns and declare any rent from portions.

## Family Businesses

Many businesses are run by brothers jointly. A partnership deed and an AOP return keep shares clear.

## Getting Started

Share your purchase and sales records, delivery challans, salary certificates or partnership deed. We prepare the returns needed.""",
     [("Do embroidery units supplying exporters need registration?",
       "Exporters often require an NTN and sales tax registration from suppliers; tax may be deducted on payments."),
      ("How should brothers running a cloth business file?",
       "As a partnership (AOP) with a deed, with each brother declaring his share."),
      ("Do machinery repair workshops register with PRA?",
       "Repair services can be taxable under the Punjab law depending on turnover.")])

page("dijkot-road-faisalabad",
     "Dijkot Road on Faisalabad's south-western side has textile processing units, warehouses, housing schemes and the farmland that surrounds the city's edge. Our Dijkot Road clients are processing units, landowners, scheme investors and transporters.",
     "Dijkot Road Faisalabad tax help for processing units, landowners, housing scheme investors and transporters: sales tax, land and returns online.",
     """## Processing Units

Dyeing and finishing units along Dijkot Road process cloth for traders and exporters, sometimes on job-work. Job-work charges can be taxable services under the Punjab law, while units buying and selling processed cloth deal with federal sales tax. Chemical purchases and utility bills are major costs.

## Landowners Near the City

Farmland on the city's edge earns agricultural income taxed by the province. When land is sold to developers, each owner declares their share, and advance tax may apply at transfer.

## Housing Schemes

New schemes along the road attract investors. Plots are assets at the amounts paid; sales are taxable gains.

## Transporters

Trucks carrying cloth and chemicals between units, the city and ports pay advance tax with vehicle tax, adjustable when filing.

## Getting Started

Share job-work records, sales tax returns, land records or scheme documents. We prepare the appropriate returns.""",
     [("Is job-work dyeing a service for tax purposes?",
       "Processing on job-work can be a taxable service under the Punjab law; units buying and selling cloth deal with federal sales tax."),
      ("How do landowners declare land sold to a developer?",
       "Each owner declares their share of the sale; advance tax may apply at transfer."),
      ("Can transporters adjust tax paid with vehicle tax?",
       "Yes, in their annual return.")])

page("gulberg-faisalabad",
     "Gulberg in Faisalabad is an upscale residential area with large houses, private schools and clinics, home to mill owners, senior professionals and business families. Our Gulberg clients need returns that reflect business income, property and lifestyle accurately.",
     "Gulberg Faisalabad tax help for mill owners, senior professionals and business families: business drawings, property, wealth statements online.",
     """## Mill Owners and Directors

Industrialists living in Gulberg often hold shares in family-owned mills. Their income comes as directors' remuneration, dividends and sometimes loans from the company. Each has different tax treatment, and transfers between company and personal accounts should be documented.

## Lifestyle and Wealth Statements

Large houses, several cars, foreign travel and children studying abroad are visible to FBR through its data. The wealth statement's personal expenses figure should reflect these, built from actual records.

## Professionals

Doctors, lawyers and consultants living in Gulberg declare professional income and claim tax deducted by institutions.

## Property

Families often hold property in Gulberg, other parts of the city and Lahore. A property schedule helps with section 7E checks and future sales.

## Getting Started

Share company records, bank statements, property papers and expense records. We prepare returns for each family member together.""",
     [("How are loans from a family mill to a director treated?",
       "They should be documented as loans, with repayments; undocumented transfers can be questioned as income."),
      ("Why does FBR care about household expenses?",
       "The wealth statement must reconcile, and visible spending is compared with declared income."),
      ("Do dividends from a family company need to be declared?",
       "Yes, with the tax deducted by the company shown as tax paid.")])

page("jinnah-colony-faisalabad",
     "Jinnah Colony is one of Faisalabad's older commercial and residential areas, close to the city centre, with wholesale markets, workshops and long-established family businesses. Our Jinnah Colony clients are wholesalers, workshop owners and families.",
     "Jinnah Colony Faisalabad tax help for wholesalers, workshops and family businesses near the city centre: records, AOP returns and filer status online.",
     """## Wholesale Trade

Wholesalers in Jinnah Colony supply retailers across the city and surrounding towns, often on credit. Ledgers of receivables and payables, purchase invoices and stock lists form the basis of their returns.

## Workshops

Workshops making machine parts and repairing looms serve the textile sector. Job cards and material bills support their income figures, and services may be taxable under PRA's law.

## Family Businesses Across Generations

Many shops have passed from fathers to sons. Each new owner registers under his own NTN; partnerships among brothers file as AOPs.

## Families

Households combine business income with rent from portions and savings. Each source is declared.

## Getting Started

Share ledgers, purchase invoices, stock lists and bank statements. We prepare the firm's and family members' returns.""",
     [("What records do wholesalers need?",
       "Purchase invoices, sales and credit ledgers, stock lists and bank statements."),
      ("Can a son continue under his father's NTN?",
       "No, he registers under his own NTN when he takes over."),
      ("Do loom repair workshops pay PRA tax?",
       "Repair services can be taxable under the Punjab law depending on turnover.")])

page("kohinoor-city-faisalabad",
     "Kohinoor City on Jaranwala Road is a modern commercial and residential hub in Faisalabad, with shopping centres, offices, hotels and apartments. Our Kohinoor City clients are retailers, office-based businesses, hotel operators and apartment owners.",
     "Kohinoor City Faisalabad tax help for retailers, offices, hotels and apartment owners: PRA services tax, POS, rent and returns, filed online.",
     """## Shopping Centre Retailers

Retailers in Kohinoor City's malls and plazas see high footfall and card payments. Larger retailers may be under FBR's point-of-sale requirements; all keep records that match card receipts.

## Offices

Software houses, consultancies and agencies with offices here deduct tax from staff, may register with PRA for local services and follow the IT export rules for foreign revenue.

## Hotels

Hotels serving business visitors charge PRA sales tax on accommodation and food and file income tax returns.

## Apartment Owners

Apartments are let to professionals and visitors. Rent is declared each year; short-term rentals through platforms are also taxable.

## Getting Started

Share POS or card reports, payroll, PRA returns or tenancy agreements. We prepare the returns.""",
     [("Do hotels in Faisalabad charge PRA tax?",
       "Accommodation and food services are generally taxable under the Punjab law."),
      ("How do software houses in Kohinoor City treat foreign revenue?",
       "Under the IT export rules when received through banks and conditions such as PSEB registration are met."),
      ("Is short-term apartment rental income taxable?",
       "Yes, it should be declared with platform statements as evidence.")])

page("madina-town-faisalabad",
     "Madina Town is one of Faisalabad's most popular residential areas, with large houses, schools, clinics and the Susan Road commercial strip nearby. Our Madina Town clients are business families, doctors, school owners and landlords.",
     "Madina Town Faisalabad tax help for business families, doctors, schools and landlords: returns, rent, professional income and wealth statements online.",
     """## Business Families

Many textile traders and mill owners live in Madina Town. Their personal returns must reconcile with their businesses' accounts, especially drawings and transfers.

## Doctors and Clinics

Specialists with hospital salaries and private clinics declare both and claim tax deducted by hospitals.

## Private Schools

Schools in large houses employ teachers and charge fees. They deduct tax from salaries above the threshold and keep fee registers.

## Landlords

Houses and portions in Madina Town are let to families and offices. Rent is taxable; office tenants may deduct tax.

## Property Transactions

Houses here sell at high values, so advance tax at transfer is significant. Being on the Active Taxpayers List halves the federal rate.

## Getting Started

Share your business drawings records, practice records, school records or tenancy agreements. We prepare the household's returns.""",
     [("How should business drawings appear in a personal return?",
       "Drawings from a sole proprietorship or AOP are not new income, but they should match the business accounts and explain personal spending."),
      ("Do doctors declare hospital and clinic income together?",
       "Yes, both are declared, with credits for tax deducted by hospitals."),
      ("Does filing reduce advance tax on a Madina Town house sale?",
       "Yes, sellers on the Active Taxpayers List pay the lower rate under section 236C.")])

page("millat-road-faisalabad",
     "Millat Road connects central Faisalabad to its northern areas, with markets, workshops, housing and small manufacturing units along its length. Our Millat Road clients are traders, small manufacturers and residents.",
     "Millat Road Faisalabad tax help for traders, small manufacturers and residents: sales tax, purchase records and returns, handled online.",
     """## Small Manufacturers

Units making hosiery, plastic goods and machine parts operate along Millat Road. Manufacturers generally register for sales tax, file monthly and verify suppliers before buying, because input tax depends on suppliers being active.

## Traders

Shops dealing in hardware, electrical goods and building materials keep purchase and sales records and claim electricity bill tax.

## Residents

Families working in mills and offices file salaried returns, claim refunds and declare rent from portions.

## Workers in Small Units

Workers paid weekly in cash often earn below the threshold; filing still helps with bank accounts and filer rates.

## Getting Started

Share sales tax returns, purchase records or salary certificates. We prepare the returns needed.""",
     [("Do hosiery units need sales tax registration?",
       "Manufacturers are generally required to register for federal sales tax, with limited exceptions."),
      ("Can traders claim electricity bill tax?",
       "Yes, advance income tax on commercial electricity bills is adjustable."),
      ("Should low-paid workers file?",
       "It is optional below the threshold but gives access to lower filer rates.")])

page("nishatabad-faisalabad",
     "Nishatabad grew around large textile mills on Faisalabad's eastern side and remains a mill and industrial area with housing for workers and staff. Our Nishatabad clients are mill vendors, contractors, staff and small businesses.",
     "Nishatabad Faisalabad tax help for mill vendors, contractors, staff and small businesses: sales tax, withholding credits and returns, done online.",
     """## Vendors to the Mills

Suppliers of spare parts, chemicals, packing material and services deal with mills that deduct income tax and require sales tax or PRA registration. Vendors who fall off the Sales Tax Active Taxpayers List can lose business because mills cannot claim input tax on their invoices.

## Labour and Service Contractors

Contractors providing labour, security and maintenance to mills have tax deducted on payments. Wage records support their actual costs.

## Mill Staff

Managers, engineers and workers have salary tax deducted. Overtime and bonuses can lead to over-deduction, which filing recovers.

## Small Businesses

Shops serving the mill workforce keep simple records and claim electricity bill tax.

## Getting Started

Vendors should share invoices, mills' tax certificates and sales tax returns; contractors their wage records; staff their salary certificates. We prepare the returns.""",
     [("Why must mill vendors stay active for sales tax?",
       "Mills cannot claim input tax on invoices from inactive suppliers, so inactive vendors lose orders."),
      ("Do labour contractors pay tax on full payments?",
       "Tax may be deducted on the full payment, but income tax applies to their profit after wages."),
      ("Can mill workers get refunds?",
       "Yes, if tax deducted exceeds their liability, by filing a return.")])

page("peoples-colony-faisalabad",
     "People's Colony is a large, established area of Faisalabad with residential blocks, the D-Ground commercial zone, schools and clinics. Our People's Colony clients are families, shopkeepers, professionals and landlords.",
     "People's Colony Faisalabad tax help for families, shopkeepers, professionals and landlords: returns, rent and wealth statements filed online.",
     """## Families

Households combine salaries from mills, banks and schools with rent and savings. Returns for all earners should be prepared together so gifts and shared assets match.

## Shopkeepers Outside D-Ground

Neighbourhood shops away from the main commercial zone serve residents. Purchase records and electricity bills support their returns.

## Professionals

Lawyers, accountants and doctors practising from People's Colony declare professional income and claim tax deducted by institutional clients.

## Landlords

Portions and houses are let to families moving into the area. Rent is declared each year.

## Getting Started

Share salary certificates, practice or shop records and tenancy agreements. We prepare returns for the household.""",
     [("Should all earning members of a family file together?",
       "Each files separately, but preparing them together keeps gifts and shared assets consistent."),
      ("Do lawyers claim tax deducted by companies?",
       "Yes, as credits against their liability."),
      ("Is rent from a family tenant taxed at source?",
       "Usually not; the landlord pays tax with the return.")])

page("samanabad-faisalabad",
     "Samanabad in Faisalabad is a dense residential and trading area with markets, small workshops and families engaged in the cloth and garment trade. Our Samanabad clients are traders, stitching units and salaried families.",
     "Samanabad Faisalabad tax help for traders, stitching units and salaried families: records, sales tax and returns, filed online.",
     """## Stitching Units

Small garment units stitch for local brands and exporters, paid per piece. Records of orders, deliveries and payments support their returns, and buyers may deduct tax.

## Cloth and Garment Traders

Traders supply retailers across the city and Punjab. Purchase and sales ledgers and bank statements support their turnover.

## Salaried Families

Workers in mills and offices file returns to claim refunds and stay on the Active Taxpayers List.

## Family Homes

Houses shared among brothers are declared by each according to his share.

## Getting Started

Share order and delivery records, ledgers or salary certificates. We prepare the returns.""",
     [("How do stitching units paid per piece file?",
       "From records of orders, deliveries and payments, with expenses such as wages and electricity."),
      ("Do brand buyers deduct tax from stitching units?",
       "They may deduct tax on payments; keep certificates to claim the credit."),
      ("How is a shared family home declared?",
       "Each owner declares his share in his own wealth statement.")])

page("susan-road-faisalabad",
     "Susan Road is one of Faisalabad's main commercial roads, lined with showrooms, restaurants, banks, schools and offices next to Madina Town. Our Susan Road clients are showroom owners, restaurateurs, school owners and landlords.",
     "Susan Road Faisalabad tax help for showrooms, restaurants, schools and landlords: PRA services tax, POS, rent and returns, done online.",
     """## Showrooms

Furniture, electronics and car showrooms on Susan Road deal in high-value goods. Stock registers, purchase invoices and sales records support their returns; car dealers record each vehicle's purchase and sale.

## Restaurants

Restaurants charge PRA sales tax on services and file FBR returns.

## Schools and Academies

Schools and academies charge fees, employ teachers and deduct tax from salaries above the threshold.

## Commercial Landlords

Owners of buildings let to showrooms and banks receive rent with tax deducted by corporate tenants.

## Getting Started

Share stock registers, PRA returns, school records or tenancy agreements. We prepare the returns.""",
     [("How do car showrooms on Susan Road record stock?",
       "In a register with each vehicle's purchase and sale details."),
      ("Do schools on Susan Road charge PRA tax?",
       "Education services may be treated differently under the Punjab law; we check each case."),
      ("Is rent from a bank tenant taxed at source?",
       "Yes, banks deduct tax from rent, which the landlord claims.")])

page("war-memorial-faisalabad",
     "The area around Faisalabad's war memorial and the nearby roads combines government offices, residential streets and commercial activity close to the cantonment and civil lines. Our clients here are government employees, retirees and local businesses.",
     "Faisalabad civil lines and war memorial area tax help for government employees, retirees and local businesses: returns, pensions and records online.",
     """## Government Employees

Offices of district and provincial departments employ many residents. Salary tax is deducted at source, and arrears paid later may be taxed at earlier years' rates if the option is chosen.

## Retirees

Retired officials with exempt pensions declare rent and profit and file to stay on the Active Taxpayers List.

## Local Businesses

Shops, restaurants and service businesses keep sales and purchase records and file returns; restaurants register with PRA.

## Property in Civil Lines

Older houses in civil areas carry high value and long ownership histories. Their sale involves advance tax and capital gains based on acquisition dates.

## Getting Started

Share salary or pension statements, business records or property papers. We prepare the returns.""",
     [("Can pay arrears be taxed at earlier rates?",
       "Yes, there is an option to tax arrears at the rates of the years they relate to."),
      ("Do retirees need to file?",
       "Filing keeps them on the Active Taxpayers List, lowering tax on savings profit."),
      ("How is an old civil lines house taxed on sale?",
       "Capital gains depend on the acquisition date; advance tax applies at transfer.")])
