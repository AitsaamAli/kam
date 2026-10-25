"""Towns L continued: Nowshera, Nushki, Okara, Dubai, Pakpattan, Panjgur."""
from towns import town

PAGES = {}

town(PAGES, "nowshera",
     tax=("Nowshera, on the Kabul river east of Peshawar, combines a large cantonment and the air force academy at Risalpur with an industrial estate, cement plants near Cherat, sand and gravel from the river, and towns such as Pabbi and Akora Khattak.",
          "Nowshera tax consultant for cantonment and air force families, industrial estate units, cement and gravel contractors, and traders.",
          """## Cantonment and Risalpur

Nowshera's cantonment and the air force academy at Risalpur employ soldiers, airmen, officers and civilian staff whose salaries carry withholding at source. Retired personnel's pensions are generally exempt but should still be declared, so that houses and plots bought with commutation can be explained in the wealth statement.

## Industrial Estate and Cement

Units in the Nowshera industrial estate make food products, ghee, textiles and building materials. They file sales tax returns with FBR, withhold tax on payments to suppliers and register with KPRA for services they provide. Cement plants in the Cherat hills engage transporters and contractors whose bills carry withholding at lower rates for active filers.

## Sand and Gravel from the Kabul River

Contractors extracting sand and gravel under leases and selling to builders in Peshawar earn business income after royalty, machinery and transport costs.

## Floods

The 2010 flood devastated Nowshera's lower areas. Business losses from floods are written off in the year of loss with evidence.

## Pabbi and Akora Khattak Traders

Shopkeepers in these towns keep supplier bills from Peshawar wholesalers and daily sales.

## Remittances

Many families have members in the Gulf; money sent through banks is a receipt in the wealth statement.""",
          [("Do Nowshera industrial units need KPRA registration?",
            "For services they provide, usually yes."),
           ("Is gravel extraction income taxable?",
            "Yes, after royalty, machinery and transport costs."),
           ("Is an air force pension declared?",
            "Yes, as exempt income.")]),
     ntn=("Nowshera residents register for an NTN to supply the industrial estate and cement plants, take sand and gravel contracts, or buy property at filer rates.",
          "NTN registration in Nowshera for industrial estate suppliers, cement plant contractors, gravel lease holders and families.",
          """## Supplying the Industrial Estate

Factories in the estate buy packing materials, chemicals and maintenance services from local firms and require an FBR NTN, and often sales tax and KPRA registration, before placing regular orders.

## Cement Plant Contractors

Transporters carrying clinker and cement from Cherat and labour contractors at the plants are withheld at lower rates once they file.

## Gravel and Sand Lease Holders

Builders and government contractors buying aggregates prefer registered suppliers who can issue invoices.

## Retired Servicemen Starting Businesses

Retirees investing commutation in transport or shops should register when the business starts.

## Gulf Workers

Workers abroad can register with a NICOP and file online.

## How to Apply

Registration is free and online; our [FBR registration guide](/blogs/fbr-registration-step-by-step) explains each step.""",
          [("Do industrial estate factories require registered suppliers?",
            "Most do."),
           ("Do builders prefer registered gravel suppliers?",
            "Increasingly, yes."),
           ("Is registration free?",
            "Yes.")]),
     inc=("Nowshera returns combine military and civilian salaries, industrial and contract income, trade and remittances. This page explains each.",
          "Income tax return filing in Nowshera for cantonment staff, industrial units, contractors, traders and remittance families.",
          """## Serving Personnel and Pensioners

Pay certificates show salary and withholding; pensions are declared as exempt.

## Industrial Units

Sales, raw materials, power, wages and depreciation, reconciled with sales tax and withholding filings.

## Contractors

Each payment, tax withheld and costs; KPRA tax collected is not income.

## Gravel Lease Holders

Sales of aggregate less royalty, machinery running costs and transport.

## Traders

Sales, purchases and stock on 30 June.

## Remittances

Money from abroad is shown as receipts.

## Flood Losses

Business stock or equipment lost is written off with evidence.""",
          [("Is KPRA tax collected income?",
            "No."),
           ("Are flood losses deductible?",
            "Business losses are, with evidence."),
           ("Do pensioners file?",
            "Filing keeps them on the Active Taxpayers List.")]))

town(PAGES, "nushki",
     tax=("Nushki, west of Quetta on the road towards Iran, is a desert district of wheat and melons grown with tubewells, livestock herding and trade along the highway to Taftan.",
          "Nushki tax help for traders on the Taftan road, livestock owners, farmers, transporters and government employees, prepared online.",
          """## Trade Along the Taftan Road

Nushki lies on the highway linking Quetta with the Iranian border at Taftan. Transporters, fuel stations, restaurants and traders along the route earn much of their income from this traffic. Goods brought across the border should come through documented customs channels, so that duties and taxes paid are on record.

## Farming with Tubewells

Wheat, melons and vegetables grown on family land with tubewell irrigation are agricultural income. Families who sell water from their tubewells to neighbours earn separate income from the pump.

## Livestock

Sheep and goats raised on family land are part of farming; traders who buy animals for markets in Quetta and Karachi earn business income.

## Transporters

Truck owners on the Quetta-Taftan route keep freight and fuel records and claim advance tax paid with their tokens.

## Government Employees and Levies

Salaried staff have tax withheld.

## Services Tax

Services in Balochistan fall under the Balochistan Revenue Authority.""",
          [("Are melons from my land taxable?",
            "They are agricultural income."),
           ("Do goods from Iran need documentation?",
            "Yes, through customs, so duties and taxes are recorded."),
           ("Who taxes restaurants in Nushki?",
            "The Balochistan Revenue Authority.")]))

town(PAGES, "okara",
     tax=("Okara, between Lahore and Sahiwal on the national highway, is known for its military farms, dairy and livestock, potato and maize farming, and textile mills. Farmers, dairy suppliers, millers, traders and employees are its main taxpayers.",
          "Okara tax consultant for dairy farms, potato and maize growers, textile mill suppliers, traders and employees, prepared online.",
          """## Dairy and Livestock

Okara's buffaloes and Sahiwal cattle supply milk to processors and city markets. Milk from a few animals kept as part of farming is agricultural. A commercial dairy with purchased feed, hired workers and a large herd is a business, and processors withhold tax on payments to it. Animals bought for the herd are capital assets; calves sold are income.

## Potatoes and Maize

Potatoes and maize grown on family land are agricultural income. Cold storage owners earn rent per bag, which is business income, and potato traders who buy at harvest and sell later earn a trading margin.

## Textile Mills

Okara's spinning and weaving mills buy cotton and yarn and engage transporters and contractors. They file sales tax returns and withhold tax on payments.

## The Grain Market

Arhtis earn commission; advances to farmers are receivables.

## Highway Businesses

Restaurants and fuel stations on the N-5 keep daily records; restaurants deal with PRA.

## Employees

Teachers, mill staff and officials have salary tax withheld.""",
          [("Is milk from my buffaloes taxable?",
            "Small-scale dairy as part of farming is agricultural; a commercial dairy is a business."),
           ("Is cold storage rent business income?",
            "Yes."),
           ("Do textile mills withhold tax from transporters?",
            "Yes.")]))

PAGES["blogs/ntn-registration-pakistanis-dubai.html"] = {
    "drop_all": True, "faq_skip_all": True,
    "lead": "Pakistanis living in Dubai and the other emirates often need an FBR NTN for property, bank accounts or family business at home. Registration is entirely online and can be done from the UAE with a NICOP or CNIC.",
    "desc": "NTN registration for Pakistanis in Dubai: why you need it, NICOP registration from the UAE, filer status, property and remittances.",
    "body": """## Why a Dubai Resident Needs an NTN

The UAE does not tax individuals' salaries, so many Pakistanis in Dubai assume they have nothing to do with FBR. The need usually arises at home. A plot or apartment bought in Lahore, Karachi or Islamabad attracts advance tax under section 236K at a much lower rate if the buyer is on FBR's Active Taxpayers List. Selling property carries the seller's advance tax under section 236C, again lower for filers. Rent from a house let out in Pakistan is Pakistani income that has to be declared. And banks in Pakistan increasingly ask overseas customers for their NTN.

## Registering from the UAE

Registration is done on FBR's IRIS portal with a NICOP or CNIC. FBR sends verification codes to a Pakistani mobile number registered in the applicant's name and to an email address. Many Dubai residents keep a Pakistani SIM on international roaming, or ask a family member to read out the code from a SIM in the applicant's name. Our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows each screen.

## Registration Alone Is Not Filer Status

An NTN does not put you on the Active Taxpayers List. You must file a return for the latest tax year. For a Dubai resident with no Pakistani income, that return can be simple, declaring foreign salary as exempt under the residence rules and listing assets in Pakistan.

## Residence Status

A Pakistani who spends fewer than 183 days in Pakistan in a tax year is generally non-resident and taxed only on Pakistani-source income.

## Remittances

Money sent home through banks or exchange companies is not income. It is shown in the wealth statement of whoever receives it.

## More Help

Our page for [Pakistanis in Dubai](/blogs/best-tax-consultant-overseas-pakistanis-dubai) covers returns and property in more detail.""",
    "faq": [("Can I register for an NTN from Dubai?",
             "Yes, online with a NICOP or CNIC."),
            ("Do I become a filer as soon as I register?",
             "No, you must file a return for the latest tax year."),
            ("Is my Dubai salary taxed in Pakistan?",
             "A non-resident is generally taxed only on Pakistani-source income."),
            ("Do I need a Pakistani SIM?",
             "FBR sends codes to a Pakistani mobile in your name, so keeping one active helps.")]}

town(PAGES, "pakpattan",
     tax=("Pakpattan, on the old bed of the Sutlej in southern Punjab, is home to the shrine of Baba Farid Ganjshakar, whose annual urs draws hundreds of thousands of visitors. Farming, dairy, shrine-related trade and government employment shape its tax questions.",
          "Pakpattan tax consultant for shrine-area businesses, farmers, dairy suppliers, arhtis, traders and government employees.",
          """## Baba Farid's Urs

During the annual urs, when the Bahishti Darwaza is opened, Pakpattan's shops, langar suppliers, transporters and lodging houses earn a large share of their year's income in a few days. Daily sales notes during the urs, supplier bills and bank deposits afterwards are what allow a realistic return. Families renting rooms to visitors earn rent that is income even if it lasts only a few weeks.

## Farming

Cotton, wheat, maize and fodder grown on family land are agricultural income.

## Dairy

Milk collected from villages for processors is part of farming for small farmers; commercial dairies and collection centres earn business income.

## The Grain Market

Arhtis earn commission; advances to farmers are receivables.

## Government Employees

Teachers and officials have salary tax withheld.

## Traders

Shops in the bazaar around the shrine and the city keep supplier bills and daily sales.""",
          [("Is room rent during the urs taxable?",
            "Yes, it is income even if short-term."),
           ("Do shrine-area shops need records?",
            "Yes, especially daily sales during the urs."),
           ("Is milk from my animals taxable?",
            "Small-scale dairy is agricultural.")]),
     inc=("Pakpattan returns combine farm income, shrine-season trade, dairy, commission and salaries. This page explains what to include.",
          "Income tax return filing in Pakpattan for farmers, shrine-area traders, dairy suppliers, arhtis and government employees.",
          """## Shrine-Season Trade

Shops and lodging houses near the shrine show sales and rent from the urs and the rest of the year, against purchases, wages and rent. A business that earns half its year in two weeks still files one return for the full year.

## Farmers

Crops from family land are agricultural income.

## Dairy

Commercial dairies show milk sales against feed, labour and veterinary costs.

## Arhtis

Commission less costs, with advances as receivables.

## Employees

Salary and withholding from certificates.

## Wealth Statement

Land, shops, animals, vehicles and balances.

## Late Filing

A late return is accepted with the surcharge.""",
          [("Do seasonal businesses file a full-year return?",
            "Yes."),
           ("Is a dairy herd an asset?",
            "Yes."),
           ("Can I file late?",
            "Yes, with the surcharge.")]))

town(PAGES, "panjgur",
     tax=("Panjgur, in Balochistan's Makran region near the Iranian border, is famous for its dates, grown in palm groves watered by karez channels and the Rakhshan river. Date growers and traders, border trade and government service shape its economy.",
          "Panjgur tax help for date growers and traders, transporters, border traders and government employees in Makran, prepared online.",
          """## Dates

Panjgur's dates, including the prized varieties grown in its groves, are sold across Pakistan and abroad. Growers selling dates from their own palms earn agricultural income. Traders who buy dates, dry, sort, pack and send them to Karachi and beyond earn business income on their margin after purchase, labour, packing and freight.

## Border Trade

Goods crossing from Iran should come through documented customs channels so that duties and taxes paid are recorded.

## Transporters

Truck and coach owners on the Makran routes towards Turbat, Quetta and Karachi keep freight and fare records and claim the advance tax paid with their tokens.

## Government Employees and Teachers

Salaried staff have tax withheld.

## Services Tax

Services in Balochistan are taxed by the Balochistan Revenue Authority.

## Families Abroad

Many Makran families have members in the Gulf; remittances are receipts in the wealth statement.""",
          [("Is date income from my palms taxable?",
            "It is agricultural income."),
           ("Are date traders taxed?",
            "Yes, on their margin."),
           ("Who taxes services in Panjgur?",
            "The Balochistan Revenue Authority.")]))
