"""Peshawar city and area pages."""

PAGES = {}


def page(slug, lead, desc, body, faq, kind="tax-consultant"):
    PAGES[f"blogs/{kind}-{slug}.html"] = {"lead": lead, "desc": desc, "body": body, "faq": faq}


page("peshawar",
     "Peshawar is the commercial capital of Khyber Pakhtunkhwa and the gateway for trade with Afghanistan, with taxpayers ranging from wholesale traders and transporters to doctors, academics and families supported by remittances from the Gulf. Its businesses answer to FBR for income tax and to the Khyber Pakhtunkhwa Revenue Authority for services.",
     "Peshawar tax consultant for traders, transporters, doctors and remittance families: FBR returns, KPRA sales tax on services and property records, online.",
     """## FBR and KPRA

Income tax and sales tax on goods are federal and administered by FBR's regional office in Peshawar. Sales tax on services in Khyber Pakhtunkhwa is collected by the Khyber Pakhtunkhwa Revenue Authority under the province's own law. A courier company, restaurant, consultancy or construction firm in Peshawar can therefore have monthly KPRA returns as well as an annual FBR return, and the two authorities do not share each other's records.

## Trade with Afghanistan and the Tribal Districts

Peshawar's wholesale markets supply goods towards Torkham and the merged tribal districts. Traders buying imported goods should keep invoices that show customs-stage taxes, and those dealing with suppliers in the merged districts should check whether the supplier still benefits from any transitional exemption, because that affects whether tax is passed on.

## Families Supported by Remittances

A very large share of Peshawar households receive money from relatives in Saudi Arabia, the UAE and Qatar. These remittances, received through banks, are not the receiver's taxable income, but the houses, plots and vehicles they fund must appear in the wealth statement with the bank records.

## Professionals and Academics

Peshawar's hospitals, universities and NGOs employ many professionals whose salaries are taxed at source, often alongside private practice or consulting income that must be declared separately.

## Getting Started

Send your documents on WhatsApp 0328-4675162. We prepare FBR returns and KPRA filings remotely; fees are on our [pricing page](/pricing).""",
     [("Do Peshawar service businesses register with KPRA?",
       "If they provide services taxable under the Khyber Pakhtunkhwa law above the threshold, yes, in addition to FBR."),
      ("Are Gulf remittances taxable for my family in Peshawar?",
       "Remittances through banks are generally not the receiver's income, but assets they fund belong in the wealth statement."),
      ("Can Peshawar clients file without travelling?",
       "Yes, returns and KPRA filings are handled online from shared documents.")])

page("peshawar",
     "Peshawar residents register for an NTN when they open a business account, take government or NGO contracts, start freelancing or prepare to buy property. Registration is online on IRIS, and service businesses usually follow it with KPRA registration.",
     "NTN registration in Peshawar: IRIS steps, documents for individuals and businesses, contractor requirements and when KPRA registration is also needed.",
     """## Who Registers in Peshawar

- **Contractors and suppliers** working for government departments, cantonment bodies and NGOs, who are asked for an NTN and often active filer status before payment.
- **Wholesale traders** opening business accounts and dealing with registered buyers.
- **Freelancers and students** earning from foreign clients.
- **Families** planning property purchases who want the lower filer rate on advance tax.

## The IRIS Process

1. Register with your CNIC, a mobile number in your own name and an email you can access.
2. Enter the verification codes.
3. Complete your address and income source; add business name, address and activity if you trade.
4. Submit and download the NTN certificate.

## Common Problems in Peshawar

Mobile numbers registered in a relative's name, and business addresses described by landmark rather than a street address, are the most common obstacles. Use the address exactly as on your rent agreement or utility bill, and a SIM registered to your own CNIC.

## KPRA After the NTN

Service businesses in Khyber Pakhtunkhwa register with KPRA for sales tax on services once they cross the threshold; the NTN is needed first.

## Getting Started

Send your CNIC and business details on WhatsApp. NTN registration is Rs 2,000 on our [pricing page](/pricing).""",
     [("Can I register an NTN if my SIM is in my father's name?",
       "IRIS sends codes to the mobile number entered; use a SIM registered to your own CNIC to avoid problems with later password resets."),
      ("Do NGO contractors in Peshawar need an NTN?",
       "Generally yes, and NGOs often deduct tax at the non-filer rate if the contractor is not on the Active Taxpayers List."),
      ("Is KPRA registration automatic with the NTN?",
       "No, KPRA registration is separate and done on the authority's own system.")],
     kind="ntn-registration")

page("hayatabad-peshawar",
     "Hayatabad is Peshawar's largest planned township, stretching westward towards the Khyber district, with residential phases, hospitals, the Karkhano market and offices. Our Hayatabad clients are professionals, traders, landlords and families who have invested in its phases.",
     "Hayatabad Peshawar tax help for professionals, Karkhano traders, landlords and families: returns, KPRA, rent and property records, filed online.",
     """## Karkhano Market Traders

The Karkhano market near Hayatabad's western edge is known for imported goods, electronics, fabric and household items. Traders should keep purchase invoices that show where goods came from and what taxes were paid at import. Goods without proper documentation create risks under customs law as well as for income tax, so a clean purchase trail protects the business.

## Hospitals and Doctors

Hayatabad hosts major hospitals and many private clinics. Doctors with hospital salaries and evening practices declare both, claiming tax deducted by hospitals. Laboratories and diagnostic centres keep records of equipment and staff costs.

## Landlords in the Phases

Houses in Hayatabad's phases are widely let to families, NGOs and offices. Rent from organisations often has tax deducted; rent from families usually does not. Each property's rent is declared every year.

## Plots and Development

Families hold plots in newer phases for future construction. Plots are shown at cost, and owners with several properties should consider section 7E.

## Getting Started

Share your purchase invoices, practice records, tenancy agreements or plot papers. We prepare returns and KPRA filings where services are provided.""",
     [("What records should Karkhano traders keep?",
       "Purchase invoices showing the source of goods and taxes paid at import, plus sales records and stock lists."),
      ("Is rent from an NGO tenant taxed at source?",
       "Organisations that are withholding agents usually deduct tax from rent, which the landlord claims as a credit."),
      ("Do Hayatabad clinics register with KPRA?",
       "Medical services may be treated differently under the provincial law; we check each clinic's position.")])

page("phase-4-peshawar",
     "Phase 4 of Hayatabad is one of the township's established residential phases, with family homes, schools and neighbourhood markets close to the main hospitals. Our Phase 4 clients are salaried families, doctors, retirees and small business owners.",
     "Hayatabad Phase 4 Peshawar tax help for salaried families, doctors, retirees and small businesses: returns, rent and wealth statements filed online.",
     """## Salaried Families

Phase 4 households typically include a government officer, a teacher or an NGO employee. Salaries are taxed at source, but many families also hold savings certificates and let part of their homes, both of which add taxable income. Filing together ensures that gifts and joint assets match across family members.

## Doctors Near the Hospitals

Doctors living close to the hospitals often run evening clinics from home or nearby. Consultation fees are professional income; a fee register and bank deposits support the figure.

## Retirees

Retired officials draw exempt pensions and often depend on profit from savings. Filing keeps them on the Active Taxpayers List, which keeps tax on that profit at the lower rate.

## Neighbourhood Businesses

Pharmacies, bakeries and grocery stores serve the phase. Purchase records, monthly sales and electricity bills are enough for their returns.

## Selling or Buying in Phase 4

Property transfers carry advance tax at registration; being on the Active Taxpayers List lowers it. The PDA's transfer records should be kept with the sale deed.

## Getting Started

Share salary or pension statements, clinic records, tenancy agreements and bank certificates. We prepare the household's returns together.""",
     [("Do I declare rent from a portion of my Phase 4 house?",
       "Yes, rent from any portion is taxable income from property."),
      ("Why should retirees in Hayatabad file?",
       "To stay on the Active Taxpayers List, which lowers tax on savings profit and property transactions."),
      ("What documents prove a Hayatabad property's ownership?",
       "The development authority's allotment or transfer letter and the registered sale deed.")])

page("university-town-peshawar",
     "University Town, around the University of Peshawar and Islamia College, is home to academics, NGO and international organisation offices, guest houses and families who have lived in its spacious houses for decades. Our University Town clients are faculty, NGO staff, landlords and guest house owners.",
     "University Town Peshawar tax help for faculty, NGO staff, landlords and guest houses: salary, consulting, rent to organisations and returns online.",
     """## Faculty and Researchers

University faculty have salary tax deducted and may qualify for reductions available to full-time teachers and researchers, depending on the year's rules. Research grants, consulting for donors and visiting lectures add other income that must be declared.

## NGO and International Organisation Staff

Many organisations have offices in University Town. Pakistani staff of some international organisations may receive salaries without tax deducted; they must still declare and pay tax, often through quarterly advance tax. Staff of local NGOs usually have tax deducted.

## Houses Let to Organisations

Large University Town houses are often let as offices or guest houses to NGOs. Rent is taxable, often with tax deducted by the tenant. Advance rent for a year or more should be declared according to the period it covers.

## Guest Houses

Guest houses serving visitors earn business income from rooms and meals. Accommodation services may be taxable under KPRA's law.

## Getting Started

Share salary certificates, consulting contracts, tenancy agreements or guest house records. We prepare returns and any KPRA filings.""",
     [("Do staff of international organisations pay tax if none is deducted?",
       "Pakistani nationals generally must declare the salary and pay tax directly, often through quarterly advance tax."),
      ("Is consulting for donors taxable for faculty?",
       "Yes, consulting fees are income declared alongside salary."),
      ("Do guest houses in Peshawar charge KPRA sales tax?",
       "Accommodation services can be taxable under the Khyber Pakhtunkhwa law depending on turnover.")])

page("saddar-peshawar",
     "Peshawar's Saddar, within the cantonment, is a long-established shopping and business area with markets, banks, hotels and offices along Saddar Road and the surrounding streets. Our Saddar clients are retailers, hoteliers, money changers' customers and office-based businesses.",
     "Saddar Peshawar tax help for retailers, hotels and offices in the cantonment: FBR returns, KPRA services tax, cantonment property and records online.",
     """## Retailers and Wholesalers

Saddar's shops sell clothing, shoes, electronics and household goods to the city and visitors. Daily sales records, purchase invoices and bank deposits form the basis of returns. Larger outlets may face FBR's point-of-sale requirements.

## Hotels and Restaurants

Hotels and restaurants in Saddar serve business travellers and families. Their services are generally taxable under KPRA's law, with monthly returns, while income tax goes to FBR.

## Foreign Currency and Remittances

Saddar's banks and exchange companies handle remittances and currency purchases. Families and traders buying large amounts of foreign currency should keep receipts, and foreign currency held on 30 June belongs in the wealth statement.

## Cantonment Property

Shops and houses in Saddar are in the cantonment area, where the cantonment board collects property tax and manages transfers. Keep its receipts and transfer records.

## Getting Started

Share your sales and purchase records, KPRA returns or property documents. We prepare the returns and filings needed.""",
     [("Do Saddar restaurants pay KPRA tax?",
       "Restaurant services are generally taxable under the Khyber Pakhtunkhwa law, filed with KPRA."),
      ("Must I declare foreign currency kept at home?",
       "Yes, foreign currency held on 30 June is an asset in the wealth statement."),
      ("Who collects property tax in Peshawar Saddar?",
       "The cantonment board, as Saddar lies in the cantonment area.")])

page("cantt-peshawar",
     "Peshawar Cantonment includes military areas, officers' residences, government offices and civilian neighbourhoods under the cantonment board. Our Cantt clients are serving and retired officers, civilian employees and cantonment businesses.",
     "Peshawar Cantt tax help for serving and retired officers, civilian employees and cantonment businesses: salary, pension, property and returns online.",
     """## Officers and Families

Serving officers have tax deducted from salary, and many own plots allotted through defence schemes elsewhere. These are shown in the wealth statement at the amounts paid. Spouses and children with property or savings should file their own returns, with gifts recorded on both sides.

## Retired Officers

Pensions and commutation are exempt. Retired officers who invest in businesses, let houses or keep large savings declare those incomes.

## Civilian Employees

Civilian staff of military and cantonment organisations are salaried employees whose allowances follow their service rules.

## Cantonment Businesses

Shops and service providers within cantonment limits file FBR returns and, for taxable services, KPRA returns. Contractors working for military organisations need NTNs and often active filer status.

## Cantonment Property

The cantonment board collects property tax and manages transfers. Leases and transfer records should be kept with the property file.

## Getting Started

Share salary or pension statements, allotment letters and business records. We prepare the returns needed.""",
     [("Do military contractors in Peshawar need active filer status?",
       "Being on the Active Taxpayers List lowers withholding on payments and is often required by the paying organisation."),
      ("Is military pension taxable?",
       "No, pension and commutation are exempt."),
      ("Who manages property transfers in Peshawar Cantt?",
       "The cantonment board, alongside federal advance tax at registration.")])

page("gulbahar-peshawar",
     "Gulbahar is an older residential neighbourhood of Peshawar near the GT Road and the walled city, with dense housing, small markets and many families who have lived there for generations. Our Gulbahar clients are shopkeepers, government employees and families with members abroad.",
     "Gulbahar Peshawar tax help for shopkeepers, government employees and remittance families: returns, inherited homes, filer status and records online.",
     """## Family Homes Across Generations

Gulbahar's houses have often passed through several generations and are shared by brothers and their families. Each heir shows their share in the wealth statement. Where part of the house is let, each declares their share of the rent.

## Government Employees

Many residents work for provincial and federal departments. Their salary tax is deducted, and filing claims refunds and keeps them on the Active Taxpayers List.

## Shopkeepers

Neighbourhood shops and small wholesalers serve the area and the nearby old city. Purchase bills and monthly sales summaries support their returns, and electricity bill tax is claimed.

## Remittance Families

Remittances from relatives in the Gulf fund new floors, vehicles and plots. Bank records of each transfer explain these assets.

## Proximity to the Walled City

Families with shops in the old city's bazaars and homes in Gulbahar should keep business and household money separate, so the shop's profit and the home's expenses are both clear.

## Getting Started

Send your CNIC, salary certificate or shop records and bank statements on WhatsApp. We prepare the return in a few days.""",
     [("How do brothers sharing a Gulbahar house file?",
       "Each shows his share of the house and of any rent in his own return and wealth statement."),
      ("Should government employees file if tax is deducted?",
       "Yes, to claim any refund and to stay on the Active Taxpayers List."),
      ("Why separate shop money from household money?",
       "It makes the shop's profit clear and explains household spending in the wealth statement.")])

page("dalazak-road-peshawar",
     "Dalazak Road on Peshawar's north-eastern side has grown with housing schemes, schools, marriage halls and roadside businesses. Our Dalazak Road clients are plot investors, school owners, hall operators and families in the new schemes.",
     "Dalazak Road Peshawar tax help for plot investors, schools, marriage halls and families in new schemes: KPRA, property and returns, filed online.",
     """## Housing Schemes

Private schemes along Dalazak Road sell plots on instalments. Payments are shown as assets in the wealth statement; selling a plot or file is a taxable gain. Buyers should confirm the scheme's approval before paying.

## Private Schools

Schools along the road charge fees and employ teachers. They deduct tax from salaries above the threshold and keep fee registers.

## Marriage Halls

Halls charge for venue, catering and decoration, often with advances received months ahead. These services are generally taxable under KPRA's law; booking registers support both KPRA and income tax returns.

## Families Moving In

Families leaving older neighbourhoods for Dalazak Road's schemes often sell an old house to fund the new one. Recording both transactions together explains the funding.

## Roadside Businesses

Workshops, fuel stations and eateries keep daily records of cash sales.

## Getting Started

Share your scheme documents, school or hall records and bank statements. We prepare the returns and KPRA filings.""",
     [("Do Peshawar marriage halls charge KPRA sales tax?",
       "Venue, catering and similar services are generally taxable under the Khyber Pakhtunkhwa law."),
      ("Is selling a plot in a Dalazak Road scheme taxable?",
       "Yes, the gain is taxable and advance tax applies at transfer."),
      ("How do schools record fee income?",
       "In a fee register that reconciles with bank deposits, alongside payroll records.")])

page("jamrud-road-peshawar",
     "Jamrud Road runs from University Town towards Hayatabad and the Khyber, lined with hospitals, educational institutions, offices and the Board Bazaar trading area. Our Jamrud Road clients are traders, medical businesses, institutions and their staff.",
     "Jamrud Road Peshawar tax help for traders, medical businesses, institutions and staff: returns, KPRA, withholding and records, done online.",
     """## Board Bazaar Traders

Traders in the Board Bazaar area deal in fabric, electronics and imported goods. Purchase invoices that show the source of goods and taxes paid at import protect traders, along with sales records and stock lists.

## Medical Businesses

Hospitals, clinics and laboratories along the road employ doctors and staff. Hospitals deduct tax from doctors' fees and file withholding statements; pharmacies keep distributor invoices.

## Educational Institutions

Schools, colleges and training institutes employ teachers and charge fees. As employers, they deduct salary tax; as service providers, some services may fall under KPRA's law.

## Staff Living Along the Road

Doctors, teachers and administrators living near their workplaces file salaried returns and declare any private practice or tuition.

## Getting Started

Traders should share invoices and stock lists; institutions their payroll and fee records; staff their salary certificates. We prepare the filings needed.""",
     [("What should Board Bazaar traders keep for tax?",
       "Purchase invoices showing the source of goods and taxes paid at import, sales records and stock lists."),
      ("Do hospitals file withholding statements?",
       "Yes, for tax deducted from doctors' fees and staff salaries."),
      ("Is private tuition by teachers taxable?",
       "Yes, it is income declared alongside salary.")])

page("kohat-road-psh-peshawar",
     "Kohat Road on Peshawar's southern side carries traffic towards Kohat and Darra, with truck stands, workshops, marble and building material dealers and growing residential areas. Our Kohat Road clients are transporters, material dealers and workshop owners.",
     "Kohat Road Peshawar tax help for transporters, building material and marble dealers and workshops: vehicle tax credits, records and returns online.",
     """## Transporters

Goods transporters on Kohat Road move cargo between Peshawar and the southern districts. Advance income tax paid with vehicle tax is adjustable, and freight paid by companies may have tax deducted. A trip register supports the return.

## Building Material and Marble Dealers

Dealers sell sand, gravel, cement, steel and marble to builders. Large sales to contractors and companies may have tax deducted. Purchase and sales records by quantity help calculate profit.

## Workshops

Truck and machinery workshops provide repair services, which can be taxable under KPRA's law depending on turnover.

## Residential Growth

New housing along the road attracts families and investors. Plots and houses are declared at cost; sales carry advance tax.

## Brick Kilns Nearby

Kilns near the city's southern edge sell bricks to builders. Their income is business income, with fuel, labour and royalty costs.

## Getting Started

Share vehicle and trip records, purchase and sales records, or property papers. We prepare the return.""",
     [("Can Kohat Road transporters claim vehicle tax payments?",
       "Yes, advance income tax collected with vehicle tax is adjustable in the annual return."),
      ("Do marble dealers have tax deducted on sales to contractors?",
       "Sales to companies and contractors may have tax deducted; keep certificates to claim credits."),
      ("Is brick kiln income business income?",
       "Yes, from selling bricks, with fuel, labour and other costs deducted.")])

page("mattni-peshawar",
     "Mattni lies on Peshawar's southern outskirts along the Kohat Road towards Darra, a semi-rural area of villages, farmland, brick kilns and roadside trade. Our Mattni clients are landowners, kiln owners, transporters and families with members abroad.",
     "Mattni Peshawar tax help for landowners, brick kiln owners, transporters and remittance families: agricultural income, business returns and filer status.",
     """## Landowners and Farming

Agricultural income from farmland around Mattni is taxed by Khyber Pakhtunkhwa, not FBR, and declared as exempt income in the federal return. Land records establish ownership and shares among heirs.

## Brick Kilns

Kilns in the area sell bricks to builders in Peshawar. Kiln owners earn business income from sales after coal, labour and transport costs, and should keep records of each.

## Transporters

Tractor-trolley and truck operators carry bricks, sand and crops. Advance tax with vehicle tax is adjustable when they file.

## Remittance Families

Many families have members in the Gulf. Remittances through banks are not the receiver's income, but houses and land bought with them belong in the wealth statement.

## Selling Land to Developers

As the city expands, some families sell land for housing. Each heir declares their share, and advance tax may apply at transfer.

## Getting Started

Share your land record, kiln or transport records and bank statements. We prepare a return suited to your situation.""",
     [("Is farm income in Mattni taxed by FBR?",
       "No, agricultural income is taxed by the province and declared as exempt in the federal return."),
      ("How is a brick kiln taxed?",
       "On business income from brick sales after coal, labour and transport costs."),
      ("Do heirs declare land sales separately?",
       "Yes, each heir declares their own share of the sale proceeds.")])

page("pishtakhara-peshawar",
     "Pishtakhara on Peshawar's western side, near Hayatabad and the Ring Road, has grown from villages into residential neighbourhoods with schools, shops and small businesses. Our Pishtakhara clients are families, shopkeepers and small contractors.",
     "Pishtakhara Peshawar tax help for families, shopkeepers and small contractors: simple returns, property records and filer status, done online.",
     """## Growing Neighbourhoods

Families in Pishtakhara have built homes on ancestral land or bought plots as the area developed. Houses are declared at cost, including construction. Where land is shared among heirs, each declares their share.

## Shopkeepers

Grocery, hardware and mobile shops serve the growing population. Purchase bills, monthly sales totals and electricity bills are enough for a return.

## Small Contractors

Contractors building houses and shops in the area are paid by households and sometimes by companies. A contract register with amounts received and tax deducted supports the return.

## Working Members

Residents work in Hayatabad's hospitals and offices, the Karkhano market and across the city. Salaried workers file to claim refunds and stay on the Active Taxpayers List.

## Families with Members Abroad

Remittances fund many new houses. Bank records of each transfer explain the funding.

## Getting Started

Send your CNIC, bank statement and property or business records on WhatsApp. We prepare a straightforward return.""",
     [("How do I declare a house built on ancestral land?",
       "Show your share of the land and the construction cost you paid in your wealth statement."),
      ("Do small contractors need to keep records?",
       "Yes, a register of contracts, amounts received and tax deducted supports the return."),
      ("Is filing useful for low-income shopkeepers?",
       "Yes, it gives access to lower filer rates and builds a record for bank accounts and loans.")])

page("regi-model-town-peshawar",
     "Regi Model Town is a planned township on Peshawar's western edge, developed by the provincial authorities, where plots have been allotted and construction is progressing. Our Regi clients are allottees, affectees, investors and families building homes.",
     "Regi Model Town Peshawar tax help for allottees, affectees, investors and builders: plot payments, transfers, construction costs and returns online.",
     """## Allottees and Instalments

Plots in Regi Model Town were allotted through balloting and paid in instalments. The amounts paid are shown in the wealth statement each year, with the allotment letter and payment receipts as evidence.

## Affectees

Landowners whose land was acquired for the township received compensation and, in some cases, plots. Compensation and plots received have their own tax treatment; acquisition documents establish the facts.

## Investors

Plots and allotment letters have been traded actively. Each sale is a taxable gain; frequent trading can be treated as business income.

## Building Homes

Families constructing homes add costs to the property each year and record how construction is funded.

## Possession and Development Charges

Payments for possession and development add to the plot's cost and should be recorded with the authority's receipts.

## Getting Started

Share the allotment letter, payment receipts and any transfer documents. We prepare a wealth statement that tracks each payment.""",
     [("How do I show a Regi plot I am paying for?",
       "At the instalments paid so far, as an asset, increasing with each payment."),
      ("Is selling an allotment letter taxable?",
       "Yes, the gain is taxable; frequent trading can be treated as business income."),
      ("Are possession charges part of the plot's cost?",
       "Yes, they add to the cost shown in the wealth statement.")])

page("ring-road-peshawar",
     "Peshawar's Ring Road circles the city, with warehouses, goods terminals, car showrooms, marriage halls and new housing along its length. Our Ring Road clients are warehouse owners, transporters, showroom dealers and hall operators.",
     "Ring Road Peshawar tax help for warehouses, goods terminals, car showrooms and marriage halls: KPRA services tax, rent, records and returns online.",
     """## Warehouses and Goods Terminals

Warehouses along the Ring Road store goods for distributors and traders moving cargo towards Torkham and the rest of the province. Rent from corporate tenants often has tax deducted, and storage services can be taxable under KPRA's law.

## Transporters

Goods transport companies operating from terminals earn freight; brokers earn margins. Each keeps a trip or booking register, and fleet owners claim advance tax paid with vehicle tax.

## Car Showrooms

Dealers buying and selling used cars keep a stock register of each vehicle. Profit is the margin on each sale; advance tax at registration and transfer depends on whose name the car is registered in.

## Marriage Halls

Halls along the Ring Road charge for venues and catering, services generally taxable under KPRA's law. Booking registers support returns.

## Getting Started

Share lease agreements, trip records, vehicle stock registers or booking registers. We prepare returns and KPRA filings.""",
     [("Are storage services taxable in Khyber Pakhtunkhwa?",
       "Storage and warehousing services can be taxable under KPRA's law depending on turnover."),
      ("How do car dealers record stock?",
       "In a register showing each vehicle's purchase and sale details."),
      ("Do marriage halls file with KPRA?",
       "Venue and catering services are generally taxable under the provincial law.")])

page("warsak-road-peshawar",
     "Warsak Road runs north-west from Peshawar towards the Warsak dam, with schools, housing schemes, farms and roadside markets. Our Warsak Road clients are school owners, families in the schemes, farmland owners and local traders.",
     "Warsak Road Peshawar tax help for school owners, scheme residents, farmland owners and traders: returns, agricultural income and property records.",
     """## Private Schools and Academies

Warsak Road is known for its many private schools. Owners keep fee registers and payroll records and deduct tax from teachers above the threshold. Schools in rented buildings may also have to deduct tax on rent paid to individual landlords if they are prescribed persons.

## Families in Housing Schemes

New schemes attract families from the inner city. Plots and houses are declared at cost; scheme approval should be checked before buying.

## Farmland

Orchards and farms further along the road earn agricultural income taxed by the province and declared as exempt in the federal return.

## Local Traders

Markets along the road sell groceries, building materials and household goods. Purchase records and electricity bills support returns.

## Getting Started

Share school records, property documents, land records or business records. We prepare the appropriate return.""",
     [("Do private schools on Warsak Road deduct tax on rent?",
       "If they are prescribed persons under the law, they must deduct tax when paying rent to individual landlords."),
      ("Is orchard income taxed by FBR?",
       "No, agricultural income is taxed by the province and declared as exempt in the federal return."),
      ("Should I check a scheme's approval before buying?",
       "Yes, to avoid legal risk; the purchase still needs to be declared.")])


def faq(slug, q, a):
    PAGES[f"blogs/tax-consultant-{slug}.html"]["faq"].append((q, a))


faq("saddar-peshawar", "Can Saddar shopkeepers file without visiting the tax office?", "Yes. Send purchase and sales records and bank statements on WhatsApp; we prepare the return on IRIS and file after your approval.")
faq("cantt-peshawar", "Should an officer's spouse file a separate return?", "If the spouse holds property, savings or income, a separate return with a wealth statement showing gifts received is advisable.")
faq("dalazak-road-peshawar", "How should advance bookings at a marriage hall be recorded?", "Record each advance when received with the event date, and record the balance when the event takes place, using the same method every year.")
faq("jamrud-road-peshawar", "Do training institutes on Jamrud Road register with KPRA?", "Some training and education services may be taxable under the provincial law depending on the service and turnover; we check each institute.")
faq("kohat-road-psh-peshawar", "Do workshops on Kohat Road need KPRA registration?", "Repair and maintenance services can be taxable under KPRA's law once turnover crosses the threshold.")
faq("mattni-peshawar", "Can families in Mattni file without visiting the city?", "Yes. Land records, bank statements and other documents are shared on WhatsApp and the return is filed online.")
faq("pishtakhara-peshawar", "Do I need an NTN to buy a plot in Pishtakhara?", "It is not always required, but being on the Active Taxpayers List lowers the advance tax at transfer.")
faq("regi-model-town-peshawar", "What if I inherited a Regi Model Town allotment?", "Complete the transfer with the authority; each heir then shows their share in their own wealth statement from that year.")
faq("ring-road-peshawar", "Is warehouse rent from a distributor taxed at source?", "Corporate tenants usually deduct tax from rent, which the owner claims as a credit in the return.")
faq("warsak-road-peshawar", "How do school owners show building improvements?", "Additions to a school building owned by the owner are assets at cost; improvements to rented premises are business expenses or depreciated over time.")
PAGES["blogs/tax-consultant-jamrud-road-peshawar.html"]["body"] += "\n\nInstitutions along Jamrud Road that rent buildings from individuals should also check whether they must deduct tax on that rent."
PAGES["blogs/tax-consultant-ring-road-peshawar.html"]["body"] += "\n\nMany Ring Road businesses are family partnerships; the firm files as an AOP and each partner declares his share of profit in his own return."
PAGES["blogs/tax-consultant-warsak-road-peshawar.html"]["body"] += "\n\nTeachers who also give private tuition after school hours declare that income with their salary."
