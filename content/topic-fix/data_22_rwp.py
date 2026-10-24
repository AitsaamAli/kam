"""Rawalpindi, Wah Cantt and Taxila pages."""

PAGES = {}


def page(slug, lead, desc, body, faq, kind="tax-consultant"):
    PAGES[f"blogs/{kind}-{slug}.html"] = {"lead": lead, "desc": desc, "body": body, "faq": faq}


page("rawalpindi",
     "Rawalpindi is the older twin of Islamabad, a garrison and trading city whose taxpayers include army officers and civilian staff, Raja Bazaar wholesalers, transporters, doctors and families with members abroad. As part of Punjab, its businesses deal with the Punjab Revenue Authority for services as well as FBR.",
     "Rawalpindi tax consultant: officers, Raja Bazaar traders, transporters, doctors and overseas families; FBR returns and Punjab Revenue Authority, online.",
     """## Federal and Punjab Obligations

Income tax and sales tax on goods are federal, administered by FBR. Services provided in Rawalpindi, such as restaurants, consultancies, courier and IT services for local clients, are taxed by the Punjab Revenue Authority. Property tax is collected by the Punjab Excise department in civil areas and by the cantonment boards in cantonment areas. Each has its own registration and returns.

## The Garrison Economy

Rawalpindi's cantonments employ thousands of officers, soldiers and civilian staff, and many retired service families settle here. Their salaries are taxed at source; pensions are exempt; rent and savings income are taxable.

## Traders of the Old City

Raja Bazaar, Moti Bazaar and the surrounding markets are wholesale hubs for cloth, utensils, spices and household goods supplying northern Punjab and beyond. Traders' returns depend on purchase records, stock and bank deposits.

## Transport Hub

Rawalpindi is the main transport junction for the north, with bus and goods terminals at Pir Wadhai and Faizabad. Transport operators pay advance tax with vehicle tax and keep trip records.

| Rawalpindi client | Main filing |
| Officer or civilian staff | Salary return, allotted plots |
| Wholesaler | Profit from purchases, sales and stock |
| Transporter | Vehicle tax credits, trip income |
| Service business | PRA registration and FBR return |

## Getting Started

Share your documents on WhatsApp and we prepare returns, PRA filings and notice replies remotely. Fees are on our [pricing page](/pricing).""",
     [("Who taxes restaurant services in Rawalpindi?",
       "The Punjab Revenue Authority, under the Punjab sales tax on services law; income tax remains with FBR."),
      ("Who collects property tax in Rawalpindi Cantonment?",
       "The cantonment board collects property tax in cantonment areas; the Punjab Excise department collects it in civil areas."),
      ("Can I file my Rawalpindi return without visiting an office?",
       "Yes. Returns and PRA filings are made online from documents shared with us.")])

page("rawalpindi",
     "NTN registration is the first step for Rawalpindi residents starting a shop, freelancing, supplying the cantonments or buying property. Registration is online through FBR's IRIS portal, and service businesses usually follow it with registration at the Punjab Revenue Authority.",
     "NTN registration in Rawalpindi: IRIS steps, documents, business profile details and when Punjab Revenue Authority registration is also needed.",
     """## Who Registers in Rawalpindi

- **Suppliers and contractors** to the cantonments and military organisations, who need an NTN before bills are paid.
- **Traders** in Raja Bazaar and Saddar opening business bank accounts.
- **Freelancers and IT workers** receiving foreign payments.
- **Families** buying property who want the lower advance tax as active filers.

## Registration Steps

1. Begin on IRIS with your CNIC, a working mobile number and email.
2. Confirm the verification codes.
3. Enter address, income source and, for a business, its name, address and activity.
4. Submit and download the NTN certificate.

## Supplying the Cantonments

Contractors and suppliers to military and cantonment organisations generally need an NTN, may need sales tax registration, and often must be on the Active Taxpayers List to be paid at lower withholding rates. Registering well before bidding avoids delays.

## Punjab Revenue Authority

Businesses providing taxable services in Rawalpindi register with PRA after getting the NTN, and file monthly PRA returns.

## Getting Started

Send your CNIC, business details and address proof on WhatsApp. NTN registration is Rs 2,000 on our [pricing page](/pricing).""",
     [("Do cantonment suppliers need an NTN?",
       "Generally yes, and often sales tax registration and active filer status as well."),
      ("Do Rawalpindi service businesses register with PRA?",
       "If they provide services taxable under the Punjab law above the threshold, yes."),
      ("Does an NTN make me an active filer?",
       "No, you must file a return to appear on the Active Taxpayers List.")],
     kind="ntn-registration")

page("saddar-rawalpindi",
     "Rawalpindi's Saddar, around Bank Road, Haider Road and Kashmir Road, is the cantonment's main shopping and business district, with banks, electronics and clothing shops, restaurants and offices. Our Saddar clients are retailers, restaurateurs, professionals and landlords of shops.",
     "Saddar Rawalpindi tax help for retailers, restaurants, professionals and shop landlords: FBR returns, PRA registration, rent and cantonment records.",
     """## Retailers on Bank Road and Haider Road

Saddar's electronics, garments and footwear shops increasingly take card and wallet payments. Larger outlets may fall under FBR's point-of-sale requirements. Every retailer needs purchase records and a sales record that matches bank deposits.

## Restaurants and Bakeries

Saddar's long-established bakeries and restaurants charge sales tax on services through the Punjab Revenue Authority where their services are taxable, and file income tax returns with FBR.

## Professionals

Doctors, lawyers and accountants with offices in Saddar receive fees from individuals and institutions. Institutional payments usually come with tax deducted.

## Cantonment Property

Shops in Saddar are in the cantonment area, where the cantonment board collects property tax and controls transfers. Landlords receive rent, often from long-standing tenants, and declare it each year.

## Getting Started

Retailers should share purchase and sales records and card statements; restaurants their PRA returns; professionals their fee registers; landlords their tenancy agreements. We prepare the return and any PRA filings.""",
     [("Do Saddar Rawalpindi restaurants pay PRA tax?",
       "Restaurant services taxable under the Punjab law are filed with PRA; income tax goes to FBR."),
      ("Who collects property tax on Saddar shops?",
       "The cantonment board, because Saddar lies in the cantonment area."),
      ("Must I declare rent from an old tenancy at low rent?",
       "Yes, all rent received is declared, regardless of amount.")])

page("satellite-town-rawalpindi",
     "Satellite Town is a large, established residential area of Rawalpindi with lettered blocks, schools, clinics and a busy Commercial Market. Our Satellite Town clients are families, doctors, school owners and shopkeepers.",
     "Satellite Town Rawalpindi tax help for families, doctors, school owners and shopkeepers: returns, rent, professional income and wealth statements online.",
     """## Families and Mixed Incomes

Satellite Town households often combine government or private salaries with rent from portions and savings in certificates. Each source is declared, and family wealth statements should agree on gifts and joint property.

## Doctors and Clinics

Clinics and laboratories line the main roads. Doctors working at hospitals in the city and running evening clinics declare both incomes and claim tax deducted by the hospitals.

## Private Schools

Schools in converted houses employ teachers and charge monthly fees. As employers they deduct tax from salaries above the threshold, and they keep fee registers that reconcile with bank deposits.

## Portions Let Out

Upper or lower portions of houses are commonly let to families. Rent is taxable, and owners pay tax with the return when tenants do not deduct it.

## Property Tax

Satellite Town is in a civil area, where the Punjab Excise department collects property tax. Keep the paid challans with the property file.

## Getting Started

Share salary certificates, clinic or school records, tenancy agreements and bank statements on WhatsApp. We prepare the returns for each earning member.""",
     [("Do doctors with evening clinics declare clinic income separately?",
       "Both hospital and clinic income are declared together as professional or salary income, with credits for tax deducted."),
      ("Who collects property tax in Satellite Town?",
       "The Punjab Excise and Taxation department, as it is a civil area."),
      ("Do private schools deduct tax from teachers?",
       "Yes, where salaries exceed the taxable threshold.")])

page("commercial-market-rawalpindi",
     "Commercial Market in Satellite Town is one of Rawalpindi's busiest shopping areas, with clothing, footwear, jewellery and household stores, eateries and upper-floor offices. Our Commercial Market clients are retailers, jewellers, restaurant owners and owners of shop floors.",
     "Commercial Market Rawalpindi tax help for retailers, jewellers, restaurants and shop owners: sales records, PRA, rent and FBR returns filed online.",
     """## Clothing and Footwear Retailers

High-volume retailers in Commercial Market see seasonal peaks before Eid and weddings. Daily sales records and card statements should be kept, and stock counted at year end. Larger retailers may need to integrate with FBR's point-of-sale system.

## Jewellers

Jewellers deal in gold by weight and purity. Stock registers in tolas or grams, with purchases from wholesalers and old gold bought from customers, form the basis of profit and closing stock. Old gold purchases should be documented with the seller's CNIC where possible.

## Eateries

Fast food outlets and dessert shops charge sales tax on services through PRA where applicable and file income tax returns.

## Upper-Floor Offices and Shop Owners

Owners of shops and offices let in the market receive rent; corporate tenants may deduct tax.

## Busy Seasons and Cash

Commercial Market traders handle large amounts of cash in peak seasons. Depositing takings regularly in a business account creates a record that supports the return.

## Getting Started

Share purchase and sales records, stock registers and bank statements, and we prepare the return and any PRA filings.""",
     [("How should jewellers record stock?",
       "By weight and purity, with purchases, sales and old gold bought, so profit and closing stock can be calculated."),
      ("Do eateries in Commercial Market file with PRA?",
       "If their services are taxable under the Punjab law and above the threshold, yes."),
      ("Why deposit daily takings in a bank account?",
       "It creates a clear record of sales that supports the declared turnover.")])

page("murree-road-rawalpindi",
     "Murree Road runs through the heart of Rawalpindi from Committee Chowk and Liaquat Bagh towards Faizabad, lined with shops, hotels, hospitals, offices and wholesale outlets. Our Murree Road clients are hoteliers, traders, medical businesses and office-based firms.",
     "Murree Road Rawalpindi tax help for hotels, traders, medical businesses and offices: PRA services tax, returns, withholding and rent, done online.",
     """## Hotels and Guest Houses

Hotels along Murree Road serve travellers heading north and visitors to the city. Room and food services are generally taxable under the Punjab sales tax on services law, administered by PRA. Occupancy registers and revenue reports support both the PRA returns and the income tax return.

## Wholesale and Retail Traders

Murree Road's traders supply goods to the city and surrounding areas. Purchase and sales records, stock lists and bank statements form the basis of their returns.

## Medical Businesses

Hospitals, clinics, laboratories and pharmacies cluster along the road. Hospitals deduct tax from doctors' fees and file withholding statements; pharmacies keep distributor invoices.

## Offices

Professional firms and agencies with offices on Murree Road deduct tax from staff and may register with PRA for services.

## Getting Started

Hotels should share occupancy and revenue records; traders their purchase and sales records; medical businesses their fee and payroll records. We prepare the filings each needs.""",
     [("Do Rawalpindi hotels charge PRA sales tax?",
       "Hotel accommodation and food services are generally taxable under the Punjab law, filed with PRA."),
      ("Do hospitals deduct tax from doctors' fees?",
       "Yes, hospitals act as withholding agents and file withholding statements."),
      ("What records support a hotel's return?",
       "Occupancy registers, revenue reports, PRA returns and expense records.")])

page("cantt-rawalpindi",
     "Rawalpindi Cantonment is home to the army's headquarters, military institutions and residential areas for serving and retired officers, as well as civilian businesses within cantonment limits. Our Cantt clients are officers, their families, retired personnel and cantonment traders.",
     "Rawalpindi Cantt tax help for serving and retired officers, families and cantonment businesses: salary, pension, allotted plots and returns, online.",
     """## Serving Officers

Officers' salaries are taxed at source, with allowances treated under specific rules. Many hold plots in defence housing schemes allotted through service; these are shown in the wealth statement at the amounts paid.

## Retired Personnel

Pensions and commutation are exempt. Many retirees take up second careers, run businesses or earn rent and profit, all of which are taxable.

## Families

Property and savings held in spouses' or children's names should be supported by gifts recorded in both wealth statements or by their own income.

## Cantonment Businesses

Shops and service providers in cantonment markets operate under the cantonment board's rules. They file income tax returns, and service businesses may need PRA registration.

## Allotted Plots and Their Sale

When a defence scheme plot is sold, advance tax applies at transfer and capital gains depend on the acquisition date. Allotment letters and payment receipts are essential.

## Getting Started

Share salary certificates or pension statements, allotment letters and bank certificates. We prepare returns for each family member.""",
     [("Is army pension taxable?",
       "No, pension and commutation are exempt; other income such as rent and profit is taxable."),
      ("How are plots allotted through service declared?",
       "At the amounts paid, from allotment, and at full cost once fully paid."),
      ("Do cantonment shops register with PRA?",
       "If they provide taxable services under the Punjab law above the threshold, yes.")])

page("chaklala-rawalpindi",
     "Chaklala covers the old airport area, the airbase and the Chaklala schemes, with residential housing for service families and civilians and a commercial strip along Airport Road. Our Chaklala clients are air force and civilian employees, retirees and local businesses.",
     "Chaklala Rawalpindi tax help for air force and civilian employees, retirees and local businesses: salary, pension, property and returns filed online.",
     """## Air Force and Civilian Employees

Personnel and civilian staff at the airbase have tax deducted from salary. Allowances, accommodation and other benefits are treated under service rules and reflected in salary certificates.

## Chaklala Housing Schemes

Families in the Chaklala schemes own homes bought or allotted over decades. Older properties have low recorded costs; when sold, the acquisition date and cost determine capital gains.

## After the Airport Moved

Since passenger flights moved to the new airport, some Airport Road businesses that depended on travellers have changed or closed. Assets disposed of or written off should be documented in the business accounts.

## Retirees

Many retirees from the air force and civil aviation live here. Pensions are exempt; rent and profit are taxable, and filing keeps them on the Active Taxpayers List.

## Getting Started

Share salary or pension statements, property documents and business records, and we prepare the returns.""",
     [("Is air force pension taxable?",
       "No, pension and commutation are exempt; other income is taxable."),
      ("What if my Airport Road business closed after the airport moved?",
       "Record the closure and any assets sold or written off in that year's accounts."),
      ("How is an old Chaklala house taxed on sale?",
       "Capital gains depend on the acquisition date and cost; advance tax applies at transfer.")])

page("westridge-rawalpindi",
     "Westridge, on the Peshawar Road side of the cantonment, is a residential area of serving and retired officers' families and civilians, with schools, markets and nearby military institutions. Our Westridge clients are officers' families, retirees and local traders.",
     "Westridge Rawalpindi tax help for officers' families, retirees and local traders: pensions, rent, allotted property and returns, filed online.",
     """## Officers' Families

Families of serving officers often manage property and savings while the officer is posted elsewhere. Each family member with income or assets files their own return, and assets bought with the officer's money are gifts recorded in both statements.

## Retired Officers

Retired officers in Westridge have exempt pensions and often taxable rent from houses in other schemes. Some invest in businesses with relatives; their share of profit is declared.

## Schools and Markets

Private schools and local markets serve the area. Schools deduct tax from teachers above the threshold; shopkeepers keep purchase records and claim electricity bill tax.

## Houses on Peshawar Road

Properties along Peshawar Road are let to businesses and offices. Rent from corporate tenants often has tax deducted.

## Getting Started

Share salary or pension statements, property documents, tenancy agreements and bank certificates. We prepare returns for the household.""",
     [("Does a spouse need to file if the officer pays for everything?",
       "If the spouse holds property or savings, filing with a wealth statement showing gifts received is advisable."),
      ("Is rent from a Peshawar Road property taxed at source?",
       "Corporate tenants usually deduct tax, which the owner claims as a credit."),
      ("Do retired officers declare business profit shares?",
       "Yes, profit from any business, including family businesses, is taxable.")])

page("dhoke-hassu-rawalpindi",
     "Dhoke Hassu is a densely populated older neighbourhood of Rawalpindi with narrow lanes, small workshops, shops and many families who have lived there for generations. Our Dhoke Hassu clients are workshop owners, shopkeepers and wage earners.",
     "Dhoke Hassu Rawalpindi tax help for workshop owners, shopkeepers and wage earners: simple records, NTN, returns and Active Taxpayers List status.",
     """## Small Workshops

Furniture, metal and repair workshops in Dhoke Hassu serve customers across the city. Job cards for each order and records of materials and wages are enough to work out profit.

## Shopkeepers

Grocery and general stores operate on thin margins. Purchase bills, monthly sales totals and electricity bills are the basis for a return.

## Wage Earners

Many residents work as drivers, labourers and technicians. Most earn below the taxable threshold, but filing provides access to lower filer rates on banking and vehicle purchases.

## Family Houses

Houses passed down within families should be declared by each heir according to their share.

## Why File

Being on the Active Taxpayers List lowers tax on bank transactions, vehicle registration and property. For a family planning to buy a motorcycle or a plot, filing first can save money.

## Getting Started

Send your CNIC, bank statement and any work records on WhatsApp 0328-4675162. We prepare a simple return and explain it.""",
     [("Do small workshops need to file returns?",
       "If profit is above the taxable threshold, yes; filing is beneficial even below it."),
      ("How do heirs declare a family house in Dhoke Hassu?",
       "Each heir shows their share in their own wealth statement."),
      ("Is filing expensive for a wage earner?",
       "A salaried return is Rs 3,500 on our pricing page; the savings on filer rates often exceed this.")])

page("faizabad-rawalpindi",
     "Faizabad, at the junction of Rawalpindi and Islamabad, is a major transport interchange with bus terminals, goods transport offices and roadside businesses. Our Faizabad clients are transport operators, booking agents and businesses serving travellers.",
     "Faizabad Rawalpindi tax help for bus operators, booking agents, goods transporters and roadside businesses: trip records, vehicle tax credits and returns.",
     """## Bus and Coach Operators

Intercity bus and coach companies operating from Faizabad terminals earn from ticket sales, often through agents and online booking. Ticket revenue, fuel, tolls, driver salaries and maintenance are the main records. Advance income tax paid with vehicle tax on each coach is adjustable.

## Booking Agents

Agents selling tickets for several operators earn commission. Their income is the commission, not the full ticket value, and records should separate the two.

## Goods Transport

Goods transport offices book trucks for clients. Fleet owners earn freight; brokers earn margins. Each should keep a trip or booking register.

## Roadside Businesses

Eateries and shops serving travellers deal in cash; daily records are important. Eateries may need PRA registration for services.

## Jurisdiction

Faizabad straddles the twin cities. Businesses should confirm whether they fall in Rawalpindi (Punjab) or Islamabad (ICT), because services tax rules differ.

## Getting Started

Share vehicle documents, ticket or freight records and bank statements. We prepare the return and any services tax filings.""",
     [("Is a booking agent taxed on full ticket value?",
       "No, only on the commission earned; ticket money passed to operators is not the agent's income."),
      ("Can bus operators claim tax paid with vehicle tax?",
       "Yes, advance income tax collected with vehicle tax is adjustable in the annual return."),
      ("Which services tax applies at Faizabad?",
       "It depends on whether the business is located in Rawalpindi (PRA) or Islamabad (ICT, administered by FBR).")])

page("gulzar-e-quaid-rawalpindi",
     "Gulzar-e-Quaid is a residential society near the old airport and Airport Road in Rawalpindi, home to families of service personnel, government employees and private sector workers. Our Gulzar-e-Quaid clients are salaried families, retirees and small business owners.",
     "Gulzar-e-Quaid Rawalpindi tax help for salaried families, retirees and small businesses: returns, refunds, rent and property records filed online.",
     """## Salaried Families

Most households include salaried members working in government, the services or private firms. Filing claims any refunds and keeps them on the Active Taxpayers List.

## Retirees

Retirees with exempt pensions often have taxable income from savings and rent. Filing keeps tax on savings profit lower.

## Portions and Houses Let Out

Families who have moved to newer schemes often let their Gulzar-e-Quaid houses. Rent is declared, and owners pay tax with the return when tenants do not deduct it.

## Small Businesses

Shops and service providers in the society keep purchase records and file business returns.

## Property Records

Houses in older societies sometimes have incomplete transfer records. Regularising them with the society helps both for tax and for future sales.

## Getting Started

Share salary or pension statements, tenancy agreements and property documents. We prepare the returns remotely.""",
     [("Can I claim a refund of salary tax?",
       "Yes, if tax deducted exceeds your actual liability, by filing a return."),
      ("Is rent from my old house taxable if I live elsewhere?",
       "Yes, rent is taxable and declared each year."),
      ("Why regularise transfer records with the society?",
       "Clear records establish ownership for the wealth statement and make a future sale easier.")])

page("gunjmandi-rawalpindi",
     "Gunjmandi, near Raja Bazaar in Rawalpindi's old city, is a traditional grain and commodity market area where wholesalers and commission agents have traded for generations. Our Gunjmandi clients are grain dealers, commission agents and family trading firms.",
     "Gunjmandi Rawalpindi tax help for grain dealers, commission agents and family trading firms: profit records, AOP returns and filer status, online.",
     """## Grain and Commodity Dealers

Dealers buy wheat, pulses, rice and other commodities from farmers and wholesalers and sell to retailers and mills. Profit depends on purchase and sale prices and on stock held at year end. Seasonal stockpiling makes year-end stock counts important.

## Commission Agents

Arhtis who arrange sales between growers and buyers earn commission. Money that passes through their accounts on behalf of growers is not their income, but their records must show it clearly.

## Family Trading Firms

Many firms are partnerships among family members. The firm files as an association of persons, and partners declare their shares.

## Cash and Credit

Commodity trade runs on cash and credit. A credit ledger of amounts owed by buyers and to suppliers supports the year's figures.

## Supplying Mills and Institutions

Sales to flour mills, hostels and institutions may have tax deducted on payment. These are credits.

## Getting Started

Share purchase and sales records, credit ledgers, stock counts and bank statements. We prepare the firm's and partners' returns.""",
     [("How is a commission agent's income calculated?",
       "On commission earned; money passed on to growers is not the agent's income."),
      ("Why is year-end stock important for grain dealers?",
       "Stock held on 30 June affects profit for the year and must be valued correctly."),
      ("How do family firms file?",
       "The firm files an AOP return; each partner declares their share in their own return.")])

page("pindora-rawalpindi",
     "Pindora is a mixed residential and commercial area in Rawalpindi near IJP Road and the routes towards Islamabad, with small factories, workshops, shops and middle-income housing. Our Pindora clients are small manufacturers, traders and salaried families.",
     "Pindora Rawalpindi tax help for small manufacturers, traders and salaried families: sales tax, records, returns and filer status, handled online.",
     """## Small Manufacturers

Units making furniture, plastic goods and building materials operate around Pindora. A manufacturer here usually registers for federal sales tax, files every month even in slow months, and checks before buying that each supplier is active, because tax on an inactive supplier's invoice cannot be adjusted.

## Traders

Hardware, building material and general stores supply the growing neighbourhoods. Purchase invoices, sales records and electricity bills form the basis of their returns.

## Salaried Families

Residents working in both cities file salaried returns, claim refunds and keep wealth statements current.

## Workshops

Vehicle and machinery repair workshops may provide services taxable under the Punjab law.

## Property

Houses and portions are let to families; rent is declared each year.

## Getting Started

Manufacturers should share sales tax returns and supplier lists; traders their purchase and sales records; employees their salary certificates. We prepare the filings needed.""",
     [("Does a small furniture unit need sales tax registration?",
       "Manufacturers are generally required to register for federal sales tax, with limited exceptions."),
      ("Do repair workshops register with PRA?",
       "Repair services can be taxable under the Punjab law depending on turnover."),
      ("Can salaried residents file online?",
       "Yes, from documents shared on WhatsApp.")])

page("airport-road-rawalpindi",
     "Airport Road in Rawalpindi connects the cantonment and Chaklala areas, with car showrooms, hotels, offices, marriage halls and restaurants along its length. Our Airport Road clients are showroom owners, hoteliers, event venues and office-based businesses.",
     "Airport Road Rawalpindi tax help for car showrooms, hotels, marriage halls and offices: PRA services tax, vehicle trade records and returns online.",
     """## Car Showrooms

Used and new car dealers along Airport Road buy and sell vehicles, often registering cars in their own or customers' names. Profit is the margin on each vehicle less costs. Advance tax at registration and transfer applies depending on who registers the vehicle. A stock register of vehicles with purchase and sale details is essential.

## Marriage Halls and Event Venues

Halls and marquees charge for venues, catering and decoration. These services are generally taxable under the Punjab sales tax on services law, and booking registers support PRA returns and income tax returns.

## Hotels and Restaurants

Hotels and restaurants file PRA returns for services and FBR returns for income.

## Offices

Offices along the road deduct tax from staff and, where applicable, register with PRA.

## After the Airport Moved

Businesses that depended on airport traffic may have changed activities. Changes should be reflected in their accounts.

## Getting Started

Showrooms should share vehicle stock registers; venues their bookings; hotels and offices their revenue and payroll records. We prepare the returns.""",
     [("How do car showrooms calculate profit?",
       "From the margin on each vehicle, supported by a stock register with purchase and sale details."),
      ("Do marriage halls pay PRA tax?",
       "Venue, catering and similar services are generally taxable under the Punjab law."),
      ("Who pays advance tax when a showroom registers a car?",
       "The person in whose name the vehicle is registered or transferred pays the advance tax at that stage.")])

page("rwp-airport-rawalpindi",
     "The old Rawalpindi airport area around Chaklala retains businesses and housing built when it was the twin cities' main airport, now adapting to life after commercial flights moved to the new airport. Our clients here are hospitality businesses, travel agents and residents.",
     "Old Rawalpindi airport area tax help for hotels, travel agents and residents: changing businesses, PRA services tax and returns filed online.",
     """## Travel Agents

Travel agencies near the old airport sell tickets and Umrah and tour packages. Their income is commission and service charges; ticket money passed to airlines is not income. Travel agency services may be taxable under the Punjab law.

## Hotels and Guest Houses

Hotels that once relied on airport traffic now serve other visitors. Room and food services are taxable under the Punjab law, and occupancy records support returns.

## Businesses That Changed

Car rentals, parking and catering firms that served the airport have shifted activities. Assets sold or written off should be recorded in the year it happened.

## Residents

Families in the surrounding schemes file salaried returns and declare rent from portions.

## Getting Started

Travel agents should share sales reports and airline statements; hotels their occupancy and revenue records; residents their salary and property documents. We prepare the returns.""",
     [("Is a travel agent taxed on full ticket sales?",
       "No, on commission and service charges; ticket money passed to airlines is not income."),
      ("Do travel agencies register with PRA?",
       "Travel agency services can be taxable under the Punjab law depending on turnover."),
      ("How do I record assets sold when my business changed?",
       "Record the sale or write-off in that year's accounts with supporting documents.")])

page("askari-14-rawalpindi",
     "Askari 14 is an army housing scheme in Rawalpindi with houses and apartments allotted to serving and retired officers and later sold to civilians. Our Askari 14 clients are officer allottees, retirees and civilian buyers.",
     "Askari 14 Rawalpindi tax help for officer allottees, retirees and civilian buyers: allotted houses, rent, transfers and wealth statements filed online.",
     """## Allotted Houses and Apartments

Officers receive units through service schemes and pay over years. The amount paid each year is shown in the wealth statement, and the allotment letter is the key document.

## Retirees Living in or Letting Units

Retirees may live in their Askari units or let them while living elsewhere. Rent is taxable each year.

## Civilian Buyers

Civilians who buy from allottees pay advance tax under section 236K at transfer and the housing authority's fees. Being on the Active Taxpayers List before buying lowers the federal rate.

## Selling an Askari Unit

Sellers pay advance tax under section 236C at transfer; capital gains depend on when the unit was acquired.

## Maintenance Charges

Monthly maintenance paid to the scheme is a household expense in the wealth statement.

## Getting Started

Share allotment or transfer letters, payment receipts and tenancy agreements. We prepare the return and a property record.""",
     [("How do I show an Askari unit still being paid for?",
       "At the instalments paid, from allotment, in your wealth statement."),
      ("What advance tax does a civilian buyer pay?",
       "For transfers from 1 July 2026, 1.25% under section 236K for active filers and 2.5% for others."),
      ("Is rent from an Askari apartment taxable?",
       "Yes, rent is declared each year.")])

page("bahria-town-rawalpindi",
     "The Rawalpindi side of Bahria Town includes several of the original phases along GT Road, with houses, apartments, commercial centres and a large investor base. Our clients here are residents, landlords and investors in Bahria's Rawalpindi phases.",
     "Bahria Town Rawalpindi phases tax help for residents, landlords and investors: Punjab services tax, rent, file trading and property records, online.",
     """## Punjab Rules for the Rawalpindi Phases

Phases within Rawalpindi district fall under Punjab, so businesses providing taxable services there deal with the Punjab Revenue Authority rather than the ICT services tax. Property tax in these phases follows Punjab's system.

## Landlords

Houses and apartments in the older phases are widely let. Rent is declared each year; owners abroad declare it in a Pakistani return.

## File and Plot Investors

Investors trade files and plots in Bahria's phases. Each sale is a taxable gain; frequent trading can be treated as business income.

## Commercial Centres

Shops, restaurants and offices file income tax returns and PRA returns where applicable.

## Residents

Families living in the phases declare their homes at cost and keep maintenance receipts.

## Getting Started

Share Bahria's allotment or transfer letters, payment receipts and income records. We prepare returns with a clear property schedule.""",
     [("Do businesses in Bahria's Rawalpindi phases file with PRA?",
       "Yes, services taxable under the Punjab law in Rawalpindi district are filed with PRA."),
      ("Is trading Bahria files a business?",
       "Frequent, organised trading can be treated as business income; occasional sales are capital gains."),
      ("Do overseas owners declare rent from Bahria houses?",
       "Yes, in a Pakistani return, as Pakistan-source income.")])

page("wah-cantt",
     "Wah Cantonment grew around Pakistan Ordnance Factories and remains a town of POF employees, retirees and the businesses that serve them. Our Wah Cantt clients are POF staff, retired employees, contractors and local traders.",
     "Wah Cantt tax consultant for POF employees, retirees, contractors and traders: salary and pension, supplier filing, property and returns online.",
     """## POF Employees

Employees of the ordnance factories have salary tax deducted and receive allowances under their service rules. Overtime and arrears can raise deductions; filing claims any excess.

## Retirees

Retired POF staff have exempt pensions but taxable rent and savings income. Many retirees have built houses in nearby areas, which belong in their wealth statements.

## Contractors and Suppliers

Firms supplying materials and services to the factories and the cantonment need NTNs, often sales tax registration, and active filer status. Payments to them have tax deducted, which is a credit.

## Local Traders

Shops in Wah's markets serve the cantonment population. Purchase records and electricity bill tax credits form the basis of their returns.

## Cantonment Property

Houses in cantonment areas are subject to the cantonment board's property tax and transfer rules.

## Getting Started

Share salary certificates, pension statements, contract records or shop records. We prepare the appropriate return.""",
     [("Can POF employees claim refunds on arrears?",
       "Yes; arrears may be taxed at the rates of the years they relate to, which can lead to a refund."),
      ("Do suppliers to POF need to be active filers?",
       "Being on the Active Taxpayers List lowers withholding and is often required by buyers."),
      ("Is POF pension taxable?",
       "Government pension is exempt; other income is taxable.")])

page("wah-cantt",
     "Registering for an NTN in Wah Cantt is often needed by contractors seeking work with the ordnance factories, new shop owners, and families buying property. Registration is online, and suppliers may also need sales tax registration.",
     "NTN registration in Wah Cantt for POF contractors, shop owners and property buyers: IRIS steps, documents and sales tax registration when needed.",
     """## Why Wah Residents Register

- **Contractors and vendors** bidding for work with the factories.
- **Shopkeepers** opening business bank accounts.
- **Employees** asked by banks or for loans to show an NTN.
- **Buyers** of property who want the lower filer rate.

## Steps on IRIS

1. Register with CNIC, mobile number and email.
2. Verify the codes received.
3. Enter address and income source; add business details if you trade.
4. Submit and download the certificate.

## For Contractors

After the NTN, contractors supplying goods may need sales tax registration, and service providers may need PRA registration. Factories often check filer status before payment.

## After Registration

File a return to appear on the Active Taxpayers List; registration alone is not enough.

## Getting Started

Send your CNIC and business details on WhatsApp. NTN registration is Rs 2,000 on our [pricing page](/pricing).""",
     [("Do POF contractors need sales tax registration?",
       "Suppliers of taxable goods above thresholds generally do; service providers may need PRA registration."),
      ("How long does NTN registration take?",
       "Usually a day or two once your mobile number and email are verified."),
      ("Will my NTN make me a filer?",
       "Only after you file a return for the tax year.")],
     kind="ntn-registration")

page("wah-cantt",
     "Filing an income tax return from Wah Cantt is mostly about salaried POF staff, retirees with savings and rent, and local traders. This page walks through what each needs to file and how to avoid common mistakes.",
     "Income tax return filing in Wah Cantt for POF staff, retirees and traders: documents, credits to claim and common mistakes, filed online.",
     """## For POF and Cantonment Employees

Collect the annual salary certificate showing all allowances and tax deducted. Add bank certificates for tax on profit, mobile and internet bills, and vehicle token tax. Each is a credit that reduces final tax.

## For Retirees

Declare pension as exempt income, then rent and profit on savings. Filing keeps tax on savings profit at the lower rate for active filers.

## For Traders

Prepare a summary of purchases and sales, closing stock and electricity bills. Profit, not turnover, is taxed.

## Common Mistakes

- Forgetting the wealth statement, which must accompany the return.
- Leaving out a house built in a nearby village or a plot bought years ago.
- Not claiming tax paid on electricity, phone and vehicle bills.

## Deadline

Returns for tax year 2026 are due by 30 September 2026. Filing early avoids the last-week rush on IRIS.

## Getting Started

Send your documents on WhatsApp 0328-4675162; a salaried return is Rs 3,500 on our [pricing page](/pricing).""",
     [("What credits do POF employees often miss?",
       "Tax deducted on bank profit, mobile and internet bills and vehicle token tax."),
      ("Must retirees attach a wealth statement?",
       "Yes, individuals filing returns generally attach a wealth statement listing assets and liabilities."),
      ("When is the return due?",
       "For tax year 2026, by 30 September 2026.")],
     kind="income-tax-filing")

page("wah-cantt-rawalpindi",
     "This page covers the wider Wah area in Rawalpindi district, including the civil neighbourhoods and roads that surround the cantonment, where trade, transport and housing have grown alongside the factories. Our clients here are traders, transporters, builders and families.",
     "Wah area (Rawalpindi district) tax help for traders, transporters, builders and families outside the cantonment: returns, PRA and property records.",
     """## Civil Areas Around the Cantonment

Outside cantonment limits, property tax is collected by Punjab's Excise department and land records are kept by the revenue authorities. Families who buy land or houses here should keep the fard, mutation and registry.

## Builders and Construction

Housing around Wah has expanded, with small builders constructing homes for sale. Building and selling houses is a business, taxed on profit.

## Transporters

Transport operators on GT Road and the routes to Taxila and Hasan Abdal pay advance tax with vehicle tax and keep trip records.

## Traders

Markets outside the cantonment serve growing neighbourhoods. Traders keep purchase and sales records.

## Families

Households combine salaries from the factories, businesses and remittances; returns and wealth statements should reflect each source.

## Getting Started

Share land records, business records or salary certificates and we prepare the appropriate filings.""",
     [("Who collects property tax outside Wah Cantonment?",
       "The Punjab Excise and Taxation department in civil areas."),
      ("Are houses built for sale taxed as business income?",
       "Yes, building and selling houses is a business."),
      ("What land documents should buyers keep?",
       "The fard, mutation and registered sale deed.")])

page("taxila",
     "Taxila is known worldwide for its Gandhara heritage, and locally for heavy industry, engineering institutions and the traditional stone-carving craft. Our Taxila clients are employees of the industrial complexes, stone craftsmen and dealers, contractors and traders.",
     "Taxila tax consultant for industrial employees, stone craftsmen and dealers, contractors and traders: returns, sales tax and export records, online.",
     """## Industrial and Engineering Employees

Taxila's heavy industrial complexes and engineering university employ many residents. Salaries are taxed at source; overtime, allowances and arrears should be checked on salary certificates.

## Stone Carving and Handicrafts

Taxila's stone craftsmen produce carvings and replicas sold locally, to tourists and abroad. Craftsmen working from home earn business income; dealers buying from them and selling to shops or exporters earn trading profit. Export sales through banks have tax deducted on proceeds.

## Contractors and Suppliers

Firms supplying the industrial complexes need NTNs, often sales tax registration, and active filer status. Tax deducted on payments is a credit.

## Tourism Businesses

Guest houses, guides and shops near the heritage sites serve visitors. Services may be taxable under the Punjab law.

## Traders

Markets in Taxila and nearby towns supply households. Purchase records and electricity bill tax credits support returns.

## Getting Started

Share salary certificates, craft or trading records, contracts or shop records. We prepare the return and any registrations needed.""",
     [("How are Taxila stone craftsmen taxed?",
       "On business income from their sales, with records of materials and tools as costs."),
      ("Do exporters of handicrafts have tax deducted?",
       "Yes, banks deduct tax on export proceeds under the export rules."),
      ("Do suppliers to industrial complexes need sales tax registration?",
       "Suppliers of taxable goods above thresholds generally do.")])


def faq(rel, q, a):
    PAGES[rel]["faq"].append((q, a))


faq("blogs/tax-consultant-dhoke-hassu-rawalpindi.html", "Can I file without a bank account?", "Yes, but a bank account is strongly recommended because it records income and savings and supports your wealth statement.")
faq("blogs/tax-consultant-bahria-town-rawalpindi.html", "Is rent from a short-term Bahria rental taxable?", "Yes, income from short stays booked through platforms is taxable and should be declared with the platform's statements.")
faq("blogs/tax-consultant-wah-cantt.html", "Do I declare a house built in my village near Wah?", "Yes, at the cost of land and construction, in your wealth statement.")
faq("blogs/ntn-registration-wah-cantt.html", "Should a partnership use a partner's personal NTN?", "No. A partnership registers as an AOP with its own NTN.")
faq("blogs/tax-consultant-wah-cantt-rawalpindi.html", "Do remittances from abroad count as my income?", "Remittances through banks are generally not the receiver's taxable income, but assets they fund belong in the wealth statement.")
