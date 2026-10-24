"""Towns H: Khanewal, Khanpur, Kharian, Khushab."""
from towns import town

PAGES = {}

town(PAGES, "khanewal",
     tax=("Khanewal, a railway junction north-east of Multan, sits in one of Punjab's most productive cotton, wheat and mango belts, with dairy processing, ginning and a busy grain market. Farmers, ginners, dairy suppliers, traders and railway and government employees make up its taxpayers.",
          "Khanewal tax consultant for ginners, dairy suppliers, mango and cotton farmers, arhtis, railway staff and traders, prepared online.",
          """## Cotton Ginning

Ginning factories on the roads to Multan and Kabirwala buy seed cotton from growers and arhtis and sell lint to spinning mills and seed to oil expellers. Spinning mills withhold income tax on lint purchases, and ginners above the threshold file monthly sales tax returns. A ginner's income tax return should match those sales tax figures, because FBR's systems compare them line by line. Seasonal labour, electricity and freight are the main costs, and gins and presses are depreciated.

## Milk Collection and Dairy Farms

Large milk processors collect from villages around Khanewal through collection centres. Small farmers selling milk from their own animals earn agricultural income. Commercial dairies with purchased feed, hired workers and dozens of animals are businesses, and the processor's payment advice shows any tax withheld. Collection centre operators who earn a margin or commission on milk they gather earn business income.

## Mango Orchards

Khanewal's mango orchards supply Multan's markets and exporters. Owners selling their own fruit, or receiving money from a contractor for the season's crop, earn agricultural income; the contractor earns business income.

## Railway and Government Employees

The junction and district offices employ many people whose salary tax is withheld. Filing claims back excess withholding and records the land or houses they own.

## The Grain Market

Arhtis earn commission on wheat and cotton; advances to farmers are receivables on 30 June.

## Property

Families buying plots in Khanewal's new schemes or in Multan benefit from active filer status, which lowers the buyer's advance tax.""",
          [("Is milk from my own buffaloes taxable?",
            "Small-scale dairy as part of farming is agricultural; a commercial dairy is a business."),
           ("Should a ginner's income tax match the sales tax returns?",
            "Yes, FBR compares them."),
           ("Is money from a mango contractor agricultural income?",
            "Yes, for the orchard owner it is agricultural income."),
           ("Do railway employees need to file?",
            "Filing claims excess withholding and keeps them on the Active Taxpayers List.")]),
     ntn=("Khanewal residents register for an NTN to supply ginning or milk to large buyers, export mangoes, deal with flour mills through the grain market, or buy property at filer rates.",
          "NTN registration in Khanewal for ginners, commercial dairies, mango contractors, arhtis and families buying property.",
          """## Ginners Before the Season

Spinning mills will not buy lint from a ginner without an NTN and a sales tax registration number. Sales tax registration involves biometric verification and a visit to the factory, and the electricity connection must be in the business's name or properly documented. Ginners who start this in spring are ready when the first phutti arrives in August.

## Commercial Dairies and Collection Centres

Milk processors sign supply contracts with large dairies and collection centre operators, pay through banks and withhold tax at a higher rate from suppliers who are not active filers. Registration lets the dairy sign the contract in its own name.

## Mango Contractors and Exporters

Exporters shipping Khanewal mangoes to the Gulf and Europe buy from registered contractors who can issue invoices and receive payment by bank transfer.

## Arhtis

Flour mills buying wheat through the grain market pay by bank and withhold tax, at a lower rate for filers.

## Railway Employees

Salaried staff can register on IRIS to file their own returns and claim refunds of excess withholding.

## Families Buying Plots

Filer status lowers the advance tax charged on transfer of plots in Khanewal and Multan.

## Applying

IRIS registration needs a CNIC, a mobile SIM in your own name, an email address and the address of your shop, dairy or factory. Our [FBR registration guide](/blogs/fbr-registration-step-by-step) walks through each screen.""",
          [("Do milk processors ask dairies for an NTN?",
            "Commercial suppliers are usually asked for one."),
           ("When should a ginner apply for sales tax registration?",
            "In spring, well before the picking season."),
           ("Do mango exporters require registered contractors?",
            "Most do.")]),
     inc=("Khanewal returns typically combine ginning, dairy, mango or commission income with farm income and salaries. This page explains how each is reported.",
          "Income tax return filing in Khanewal for ginners, dairies, mango contractors, arhtis, farmers and railway employees.",
          """## Ginners

The return shows lint and cottonseed sold, seed cotton bought, electricity, labour, bale-pressing, freight and depreciation of machinery. Each spinning mill's withholding is listed and claimed. Bales and seed cotton held on 30 June are closing stock at cost.

## Commercial Dairies

Milk sales to processors, less feed, fodder, labour, veterinary costs and electricity, give the dairy's profit. Animals bought for the herd are capital assets; calves born and sold are income. The processor's withholding is claimed.

## Mango Contractors

Sales to commission agents and exporters are shown against the contract price paid to orchard owners, picking, crates, cold storage and freight. A bad season's loss is shown and may be carried forward against later business profit.

## Orchard Owners and Farmers

Mangoes, wheat and cotton from family land, and contract money received for an orchard's crop, are declared as agricultural income.

## Railway and Government Employees

Salary and withholding are copied from certificates. Employees transferred during the year combine certificates.

## Arhtis

Commission less shop costs is income; loans to farmers are receivables.

## Wealth Statement

Land, orchards, factories, animals, vehicles, receivables and balances are listed, with the change over the year explained by declared income.""",
          [("Are dairy animals shown in the wealth statement?",
            "Yes, the herd is a business asset."),
           ("Can a mango contractor carry forward a loss?",
            "Business losses generally can be carried forward."),
           ("Is bale stock counted at year end?",
            "Yes, at cost.")]))

town(PAGES, "khanpur",
     tax=("Khanpur, in Rahim Yar Khan district on the main railway and the road to Bahawalpur, is a sugarcane, cotton and wheat town with sugar mills, ginning factories and a large grain market. Its taxpayers include mill suppliers, ginners, arhtis, farmers and employees.",
          "Khanpur tax consultant for sugar mill suppliers, ginners, arhtis, farmers, traders and employees in Rahim Yar Khan district.",
          """## Sugar Mills and Cane Growers

Sugar mills around Khanpur crush cane from November to March. Growers selling cane from their own land earn agricultural income, outside federal income tax. Families who also run tractor-trolleys to carry cane for neighbours or under contract with the mill earn freight income, and the mill withholds tax on those payments. Labour contractors and suppliers of spare parts and lubricants are also withheld at source.

## Cotton Ginners

Ginners buy seed cotton during the picking season and sell lint to mills that withhold tax on purchases. Their sales tax and income tax figures should agree.

## Grain Market

Khanpur's arhtis handle wheat and cotton for farmers from surrounding villages. Commission is their income; advances to growers before harvest are assets at 30 June.

## Farmers

Wheat, cotton and sugarcane from family land are agricultural income. Larger landowners pay the Punjab agricultural income tax, and their federal wealth statement lists the land.

## Shops and Services

Shops in the city's bazaars keep supplier bills and daily sales; restaurants deal with PRA.

## Employees

Railway, school and government staff have salary tax withheld.""",
          [("Is cane haulage for neighbours agricultural income?",
            "No, carrying others' cane for hire is business income."),
           ("Do sugar mills withhold tax from transporters?",
            "Yes, at lower rates for active filers."),
           ("Is cane from my land taxable?",
            "It is agricultural income.")]),
     ntn=("Khanpur's mill suppliers, ginners, arhtis and families register for an NTN to be paid by sugar and spinning mills, deal with flour mills and buy property at filer rates.",
          "NTN registration in Khanpur for sugar mill transporters, ginners, arhtis, input dealers and families buying property.",
          """## Transporters and Contractors at the Sugar Mills

Before each crushing season, Khanpur's mills register transporters and labour contractors. They ask for an NTN and withhold tax from each payment, at a higher rate from those not on the Active Taxpayers List. A tractor-trolley owner who registers and files before November saves on every trip.

## Ginners

Spinning mills require the ginner's NTN and sales tax registration before buying lint.

## Arhtis

Flour mills pay arhtis through banks and withhold tax at lower rates from filers.

## Seed and Fertiliser Dealers

Companies supply registered dealers and withhold tax on supplies.

## Families with Property Plans

Plots in Khanpur and Rahim Yar Khan attract lower advance tax for active filers.

## Overseas Workers

Workers in the Gulf can register with a CNIC or NICOP and file online.

## How to Register

IRIS registration uses a CNIC, a mobile number in your own name and your business address. Our [FBR registration guide](/blogs/fbr-registration-step-by-step) explains the process screen by screen.""",
          [("Should transporters register before the crushing season?",
            "Yes, to be withheld at the lower rate."),
           ("Do ginners need sales tax registration?",
            "Yes, spinning mills require it."),
           ("Can Gulf workers register?",
            "Yes, online with a CNIC or NICOP.")]),
     inc=("Khanpur returns combine sugar and cotton-related business, commission, farm income and salaries. This page explains what each needs.",
          "Income tax return filing in Khanpur for mill transporters, ginners, arhtis, farmers and employees, with the wealth statement.",
          """## Mill Transporters

Freight received from the mill, shown on weighbridge and payment slips, less diesel, tyres, repairs, drivers' wages and depreciation of tractors and trolleys. The mill's withholding is claimed.

## Ginners

Lint and seed sales against seed cotton, power, wages and depreciation, with stock at 30 June. Mill withholding claimed and figures matched to sales tax returns.

## Arhtis

Commission less rent, staff and other costs. Advances to farmers are receivables.

## Farmers

Cane, cotton and wheat from family land declared as agricultural income, with any Punjab agricultural income tax noted.

## Employees

Salary and withholding from the certificate.

## Wealth Statement

Land, tractors, trolleys, factories, receivables and balances are listed.""",
          [("How do I prove mill freight income?",
            "With weighbridge slips and the mill's payment advice."),
           ("Is Punjab agricultural tax part of the federal return?",
            "It is noted, but it is a separate provincial tax."),
           ("Are trolleys depreciated?",
            "Yes, as business assets.")]))

PAGES["blogs/tax-consultant-khanpur-ryk.html"] = {
    "drop_all": True, "faq_skip_all": True,
    "regex": [(r"Khanpur Ryk", "Khanpur, Rahim Yar Khan"), (r"Khanpur RYK", "Khanpur, Rahim Yar Khan")],
    "lead": "This page is for people in Khanpur city and its surrounding villages in Rahim Yar Khan district who run shops, clinics, schools and small workshops, rather than the sugar and cotton trade covered on our main Khanpur page.",
    "desc": "Tax help in Khanpur, Rahim Yar Khan: shops, clinics, private schools, workshops, landlords and overseas families, prepared online.",
    "body": """## Shops in the City

Khanpur's bazaars sell cloth, jewellery, electronics and household goods to families from surrounding villages, with business peaking after harvests and before Eid and weddings. Shopkeepers buy from wholesalers in Rahim Yar Khan, Multan and Lahore. Keeping those purchase bills, a daily takings note and a stock count on 30 June gives a reliable profit figure. Shops that sell on credit until harvest should record what each customer owes, because those amounts are receivables at year end.

## Clinics and Pharmacies

Doctors in private practice, dental clinics and laboratories serve patients from across the tehsil. Fee registers, laboratory records and distributor invoices form their records. Doctors who also hold government posts declare salary and private practice income separately.

## Private Schools and Academies

Schools and coaching academies collect monthly fees and pay teachers. Fee registers, salary sheets and rent agreements support their returns.

## Workshops

Agricultural machinery workshops and vehicle repair shops serve farmers and transporters. Their profit is charges less parts, labour and rent.

## Landlords

Owners renting shops in the bazaar or houses to employees declare rent as property income.

## Overseas Families

Families with members in the Gulf show remittances as receipts in their wealth statements and benefit from filer status when buying property or vehicles.""",
    "faq": [("Are credit sales to farmers shown at year end?",
             "Yes, unpaid amounts are receivables."),
            ("Do doctors with government jobs declare private practice separately?",
             "Yes, salary and clinic income are separate."),
            ("Is rent from a shop taxable?",
             "Yes, it is property income.")]}

town(PAGES, "kharian",
     tax=("Kharian, on the GT Road in Gujrat district, is home to one of Pakistan's largest cantonments and to families with deep links to Norway, Denmark, Spain and the UK. Military salaries and pensions, property bought with money from abroad, rent and GT Road businesses shape its tax questions.",
          "Kharian tax consultant for military families, Scandinavian and UK-linked owners, landlords, GT Road businesses and employees.",
          """## The Cantonment

Kharian cantonment employs serving soldiers, officers and civilian staff whose salary tax is withheld at source. Retired personnel draw pensions that are generally exempt. Defence housing allotments, plots in military schemes and houses built with commutation money belong in the wealth statement of the person who owns them.

## Families in Norway, Denmark and Spain

Kharian and its villages sent some of the first Pakistani migrants to Scandinavia, and many families still have relatives in Oslo, Copenhagen and Barcelona. Money sent home for houses and plots should arrive through banks and appear in the wealth statement of the family member who owns the property. Relatives abroad who own Pakistani property in their own names need to declare any rent here and consider their obligations in their country of residence.

## Rental Property

Large houses built by overseas families are often rented to officers' families or to businesses. Rent is property income in Pakistan; company and bank tenants withhold tax.

## Selling Property

Sellers pay advance tax under section 236C at rates depending on filer status. Capital gains depend on when the property was acquired. Non-resident sellers should file before selling.

## GT Road Businesses

Restaurants, petrol pumps, showrooms and workshops keep daily sales and purchase records; restaurants deal with PRA.

## Professionals

Doctors, lawyers and teachers file returns covering salary and private income.""",
          [("Is rent from a Kharian house owned by someone in Norway taxable?",
            "Yes, rent from Pakistani property is taxable in Pakistan."),
           ("Are military pensions taxable?",
            "Pensions are generally exempt but should be declared."),
           ("Should an overseas seller file before selling?",
            "Usually yes, because advance tax is lower for active filers.")]),
     ntn=("Kharian residents and their relatives abroad register for an NTN to manage rental property, buy and sell property at filer rates, or run businesses on the GT Road and near the cantonment.",
          "NTN registration in Kharian for overseas owners in Norway, Denmark, Spain and the UK, landlords, cantonment contractors and businesses.",
          """## Owners Living in Scandinavia and Europe

A Kharian family member living in Norway or Denmark can register online with a NICOP or CNIC, using an email address and a phone that receives FBR messages. Filing a return each year keeps the owner on the Active Taxpayers List, which lowers advance tax both when buying and when selling property.

## Landlords

Owners renting houses to officers' families or businesses register to declare rent and to deal with tenants who withhold tax.

## Cantonment Contractors and Suppliers

Contractors supplying works, food and services to the cantonment are asked for an NTN and withheld at lower rates if they file.

## GT Road Businesses

Petrol pump dealers, restaurants and vehicle showrooms register to deal with oil companies, manufacturers and banks.

## Heirs

When a parent's house is sold, each heir's share is taxed separately, so each heir benefits from being registered and filing.

## Retired Servicemen

Soldiers retiring and investing in business or property register at the start.

## Applying

The process is online and the same from Kharian or abroad. Our [FBR registration guide](/blogs/fbr-registration-step-by-step) explains each screen.""",
          [("Can I register from Norway?",
            "Yes, online with a NICOP or CNIC."),
           ("Do cantonment suppliers need an NTN?",
            "Yes, and filing lowers withholding."),
           ("Does each heir need to file when selling inherited property?",
            "Each heir's share is taxed separately.")]),
     inc=("Kharian returns often bring together military salaries or pensions, rent, money from abroad and property sales. This page explains how each is reported.",
          "Income tax return filing in Kharian: military pay and pensions, rent, overseas remittances, property sales and the wealth statement.",
          """## Military Pay and Pensions

Serving personnel copy salary and withholding from their pay certificates. Retired personnel declare their pension as exempt; other income such as rent or business profit is taxable.

## Rental Income

Rent received is declared under property income, with tenants' withholding claimed. Repairs allowance and other permitted deductions apply under the law for the year.

## Money from Relatives Abroad

Remittances from Norway, Denmark, Spain or the UK received through banks are receipts shown in the wealth statement of the person who receives them.

## Foreign Pensions

Residents who have returned after working in Scandinavia and draw foreign pensions declare them under the rules on foreign income; whether they are taxable depends on the law and any treaty for the year.

## Property Sales

A sale is reported with price, cost, gain and the advance tax paid. The gain's treatment depends on the acquisition date.

## Wealth Statement

Houses, plots, defence allotments, vehicles, gold and balances, with the year's change explained.""",
          [("Is a Norwegian pension taxable in Pakistan?",
            "It depends on the law and treaty position; we check each case."),
           ("Do I declare my military pension?",
            "Yes, as exempt income."),
           ("Are remittances income?",
            "No, they are receipts shown in the wealth statement.")]))

town(PAGES, "khushab",
     tax=("Khushab, on the Jhelum where the Salt Range meets the Thal, has the scenic Soon Valley and its lakes to the north, sugar mills and irrigated farms near the river, and gram fields in the desert to the south. Farmers, mill suppliers, traders, mine operators and employees are its main taxpayers.",
          "Khushab tax consultant for farmers, sugar mill suppliers, Salt Range mine operators, traders, Soon Valley businesses and employees.",
          """## Soon Valley and the Salt Range

The Soon Valley's farms grow wheat, groundnut and vegetables on terraced land, and its lakes draw visitors to Uchhali, Khabeki and Jahlar. Rest houses, restaurants and guest houses serving these visitors keep booking records and daily sales. Mines in the Salt Range produce salt, gypsum and coal under provincial leases; lease holders' profit is sales less royalty, labour, explosives and transport.

## Sugar Mills

Mills near Khushab and Joharabad buy cane from growers and engage transporters and contractors. Growers' cane sales are agricultural income; haulage and contracting are businesses withheld at source.

## Thal Farming

Gram, wheat and fodder grown in the Thal on family land are agricultural income. Traders who buy gram and send it to processors earn business income.

## Khushab's Sweet Shops

Shops selling the town's well-known dhoda and other sweets to travellers and by courier keep daily sales and ingredient purchase records.

## Employees

Government staff in the district headquarters and teachers have salary tax withheld.

## Property

Families buying land or houses benefit from filer status.""",
          [("How is Salt Range mine profit calculated?",
            "Sales less royalty, labour, explosives and transport."),
           ("Is gram from my Thal land taxable?",
            "It is agricultural income."),
           ("Do Soon Valley guest houses need records?",
            "Yes, booking records and daily sales support their returns.")]),
     ntn=("Khushab residents register for an NTN to supply sugar mills, sell minerals, run tourism businesses in the Soon Valley or buy property and vehicles at filer rates.",
          "NTN registration in Khushab for sugar mill vendors, mine lease holders, Soon Valley businesses, gram traders and families.",
          """## Sugar Mill Vendors

Transporters and labour contractors working for the mills are asked for an NTN and withheld at lower rates if they file.

## Mine Lease Holders

Buyers of salt, gypsum and coal increasingly require registered suppliers who can issue invoices, and pay through banks.

## Soon Valley Guest Houses and Restaurants

Bookings through platforms and corporate groups are paid by bank transfer and need registration details.

## Gram Traders

Processors buying gram from Khushab's traders pay through banks and withhold tax, at lower rates for filers.

## Families Buying Vehicles and Land

Filer status lowers advance tax at registration of vehicles and transfer of property.

## Getting Registered

Have your CNIC, a mobile number in your own name and your business address ready. Our [FBR registration guide](/blogs/fbr-registration-step-by-step) explains the IRIS steps one by one.""",
          [("Do mineral buyers require registered suppliers?",
            "Increasingly, yes."),
           ("Do guest houses need an NTN for platforms?",
            "Platforms often ask for it."),
           ("Does filing lower advance tax on vehicles?",
            "Yes, active filers pay less.")]),
     inc=("Khushab returns cover farming in the Thal and Soon Valley, mill-related business, mining, tourism and salaries. This page explains what to include.",
          "Income tax return filing in Khushab for farmers, mill suppliers, mine operators, guest houses and employees, with the wealth statement.",
          """## Farmers

Crops from family land, whether in the Thal, the river belt or the Soon Valley, are agricultural income.

## Mill Suppliers

Freight and contract receipts from sugar mills, less fuel, wages and vehicle costs, with the mill's withholding claimed.

## Mine Operators

Sales of salt, gypsum or coal against royalty, labour, explosives, timber and transport. Buyers' withholding is claimed.

## Guest Houses and Restaurants

Room and food income less staff, food, utilities and maintenance, with buildings depreciated.

## Gram Traders

Sales less purchase price, cleaning, bags and freight.

## Employees

Salary and withholding from certificates.

## Wealth Statement

Land, leases, buildings, vehicles and balances, with changes explained.""",
          [("Is a mining lease shown in the wealth statement?",
            "Yes, at cost."),
           ("Can mine operators claim buyers' withholding?",
            "Yes, as credit."),
           ("Are guest house buildings depreciated?",
            "Yes, as business assets.")]))
