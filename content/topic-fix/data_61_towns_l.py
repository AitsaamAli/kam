"""Towns L: Nawabshah, Neelum, New Jersey, Noorpur Thal, Nowshera, Nushki, Okara, Dubai."""
from towns import town

PAGES = {}

town(PAGES, "nawabshah",
     tax=("Nawabshah, officially Shaheed Benazirabad, sits at the centre of Sindh between the Indus and the Nara canal. Sugar mills, banana and cotton farms, an engineering university, an air force base and the divisional offices shape the tax questions of its residents.",
          "Nawabshah tax consultant for sugar mill suppliers, banana and cotton growers, university and government staff, traders and transporters.",
          """## Sugar Mills Around Nawabshah and Sakrand

Several sugar mills operate in the district, buying cane from growers between November and March. A grower's cane sales are agricultural income, outside federal income tax, and larger holdings pay Sindh's agricultural income tax. Transporters carrying cane, labour contractors supplying gangs for the mill yard, and dealers selling parts, lubricants and bags to the mills earn business income. Mills withhold income tax from each payment to these suppliers, at a lower rate for those on the Active Taxpayers List, and the deduction certificates become credits in the supplier's return.

## Bananas and Cotton

Banana gardens around Nawabshah supply Karachi and Punjab through traders who buy standing crops, cut, pack and transport them. Their margin is business income. Cotton from family land is agricultural; ginners selling lint to mills earn business income and file sales tax returns.

## The Engineering University

Teachers and staff at the university have salary tax withheld. Consultancy, examining and research fees are declared separately.

## Divisional Offices and the Air Base

Civil servants, police and air force personnel have salary tax withheld; pensions are generally exempt.

## Traders and Transporters

Nawabshah's wholesale markets supply surrounding towns on credit. Truck owners on the national highway keep freight records and claim the advance tax paid with their tokens.

## Services Under SRB

Restaurants, marriage halls and many other services are taxed by the Sindh Revenue Authority.""",
          [("Is cane sold to a Nawabshah mill taxed by FBR?",
            "No, it is agricultural income; Sindh may tax larger holdings."),
           ("Do mills withhold tax from transporters?",
            "Yes, at a lower rate for active filers."),
           ("Do university teachers declare consultancy?",
            "Yes, separately from salary."),
           ("Who taxes marriage halls in Nawabshah?",
            "The Sindh Revenue Authority.")]),
     ntn=("Nawabshah residents register for an NTN to supply sugar mills, trade bananas and cotton, take government contracts, or buy property in Hyderabad and Karachi at filer rates.",
          "NTN registration in Nawabshah for sugar mill suppliers, banana traders, ginners, government contractors and families buying property.",
          """## Before the Crushing Season

The district's mills register cane transporters and labour contractors each autumn. Their cane offices ask for an FBR NTN and a bank account in the contractor's name, and their accounts departments withhold income tax from every payment. A contractor who has filed a return for the latest year is withheld at the lower rate for the whole season.

## Banana Traders Sending Trucks to Punjab

Commission agents in Lahore, Faisalabad and Multan pay Nawabshah's banana traders by bank transfer after each sale, and larger agents ask for the trader's NTN.

## Ginners

Spinning mills buy lint only from ginners with an NTN and sales tax registration, and sales tax registration needs biometric verification and a factory visit, so ginners should start in spring.

## Contractors for Divisional Departments

Roads, schools and drainage works across the division are given to registered contractors; departments check filer status before deciding withholding.

## Families Buying Flats in Hyderabad or Karachi

The buyer's advance tax at transfer is lower for active filers.

## Registering

Registration is free and online with a CNIC and a mobile number in your own name. Our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows every screen.""",
          [("When should mill transporters register?",
            "Before the crushing season begins."),
           ("Do banana commission agents ask for an NTN?",
            "Larger agents increasingly do."),
           ("Is registration free?",
            "Yes, FBR charges nothing.")]))

town(PAGES, "neelum-ajk",
     tax=("The Neelum valley, stretching north-east from Muzaffarabad along the Line of Control, draws growing numbers of summer visitors to Keran, Sharda, Kel and Arang Kel, and hosts a major hydropower project at its mouth. Guest houses, transport, trout farms and forest work make up its local economy.",
          "Neelum valley tax help for guest houses, tour transport, trout farms, hydropower contractors and families, under AJK and FBR rules.",
          """## Which Authority Applies

The Neelum valley is part of Azad Jammu and Kashmir, so income arising there, such as guest house earnings in Keran or Sharda, is dealt with under AJK's own income tax system. Income from Pakistan proper, such as a salary from an Islamabad employer or rent from a flat in Rawalpindi, is an FBR matter.

## Guest Houses and Hotels

Families in Keran, Sharda, Kel and Arang Kel have turned homes into guest houses, and investors have built hotels as the road improved. The season runs from late spring to early autumn, and much of the income arrives through bookings from tour operators in Islamabad and Lahore. A room register and records of bank transfers are the basic records, whichever authority's return is filed.

## Jeeps and Tour Transport

Jeep owners carrying visitors to Arang Kel, Taobat and Ratti Gali keep fare records and fuel and repair bills.

## Trout Farms

Trout farms along the Neelum river sell fish to hotels and visitors. Their profit is sales less feed, fry, labour and maintenance.

## Hydropower Contractors

Contractors and suppliers who worked on the hydropower project near Nauseri were paid under contracts whose withholding depends on the paying authority.

## Forest and Timber

Timber work under forest permits is business income for contractors.""",
          [("Does FBR tax my Keran guest house?",
            "Income arising in AJK falls under AJK's own system."),
           ("Do trout farms need records?",
            "Yes, sales against feed, fry, labour and maintenance."),
           ("Is my Islamabad salary an FBR matter?",
            "Yes.")]))

PAGES["blogs/tax-consultant-new-jersey-pakistanis.html"] = {
    "drop_all": True, "faq_skip_all": True,
    "regex": [(r"Best Tax Consultant in New Jersey Pakistanis", "Tax Consultant for Pakistanis in New Jersey"),
              (r"Tax Consultant in New Jersey Pakistanis", "Tax Consultant for Pakistanis in New Jersey"),
              (r"New Jersey Pakistanis", "Pakistanis in New Jersey")],
    "lead": "Pakistani families in Jersey City, Paterson, Edison and across New Jersey often keep property, bank accounts or family businesses back home. This page explains when FBR matters to them and how we handle the Pakistani side remotely.",
    "desc": "FBR help for Pakistanis in New Jersey: property and rent in Pakistan, inherited homes, filer status, NICOP registration and remote filing.",
    "body": """## Common Situations We See from New Jersey

The questions that reach us from New Jersey usually fall into a handful of patterns. A family in Jersey City owns a house in Lahore or Karachi that a brother rents out for them. A couple in Edison has inherited a share of a parent's property in Gujranwala or Rawalpindi and wants to sell it. A business owner in Paterson wants to buy a plot in a Pakistani housing scheme and has been quoted a high advance tax because he is not a filer. Or a retiree is moving back to Pakistan and needs to understand how a US pension and Social Security will be treated.

## Rent Collected by Relatives

Rent from Pakistani property is Pakistani-source income and is taxed in Pakistan even when the owner lives in New Jersey. The owner declares it, not the relative who collects it. A company or bank tenant withholds tax, which the owner claims.

## Selling Inherited Property

Each heir's share is taxed separately. The seller's advance tax under section 236C is lower for active filers, so heirs in the US usually save by registering and filing before the sale. The gain depends on when the property was acquired, and inherited property generally carries the deceased owner's acquisition history.

## Buying a Plot in Pakistan

Registering with a NICOP and filing a return before the transfer reduces the buyer's advance tax under section 236K.

## Residence and Your US Obligations

If you spend less than half the year in Pakistan, you are generally non-resident here and taxed only on Pakistani income. US citizens and green card holders report worldwide income to the IRS and may need to report foreign accounts; we handle only the Pakistani return, and your US preparer handles the US side.

## Working Across Nine or Ten Hours

Pakistan is nine hours ahead of New Jersey in summer and ten in winter. Documents sent by WhatsApp or email in your evening are usually reviewed by your next morning. Our guide for [Pakistanis in the USA](/blogs/best-tax-consultant-overseas-pakistanis-usa) covers the wider picture.""",
    "faq": [("Do I need a Pakistani return if I live in New Jersey?",
             "Only if you have Pakistani-source income or want filer rates on property transactions."),
            ("Is rent collected by my brother in Lahore my income?",
             "Yes, the owner declares it."),
            ("Can I register with FBR from New Jersey?",
             "Yes, online with a NICOP or CNIC."),
            ("Do you prepare US returns?",
             "No, only the Pakistani side.")]}

town(PAGES, "noorpur-thal",
     tax=("Noorpur Thal, in the Thal desert of Khushab district, is a tehsil of sand dunes, gram fields, camel and goat herds and canal-irrigated pockets, whose residents also serve in large numbers in the army.",
          "Noorpur Thal tax help for gram farmers, livestock owners, traders, army families and government employees, prepared online.",
          """## Gram in the Dunes

Noorpur Thal's farmers sow gram after the monsoon rains and harvest in spring. Where the Thal canal reaches, wheat and fodder are also grown. Crop income from family land is agricultural, outside federal income tax.

## Camels, Goats and Sheep

Herds raised on family land are part of farming. Traders who buy camels and goats in the Thal and sell them in Punjab's cattle markets before Eid earn business income on their margin after purchase, feed and transport.

## Gram Traders

Traders who buy gram at harvest and sell to processors keep purchase slips, sale invoices and freight bills, and count stock on 30 June.

## Army Families

Many Noorpur Thal households have members in the army. Serving soldiers have tax withheld; pensions are generally exempt but are declared.

## Government Employees

Teachers and officials have salary tax withheld.

## Families Abroad

Remittances through banks are receipts in the wealth statement.""",
          [("Is gram from Thal land taxable?",
            "It is agricultural income."),
           ("Is camel trading agricultural?",
            "No, buying and selling animals is business."),
           ("Is an army pension declared?",
            "Yes, as exempt income.")]))
