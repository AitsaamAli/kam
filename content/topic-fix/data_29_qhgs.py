"""Quetta, Hyderabad, Gujranwala, Sialkot and DHA Lahore area pages."""

PAGES = {}


def page(slug, lead, desc, body, faq, kind="tax-consultant"):
    PAGES[f"blogs/{kind}-{slug}.html"] = {"lead": lead, "desc": desc, "body": body, "faq": faq}


page("quetta",
     "Quetta is the capital of Balochistan and a trading crossroads for Afghanistan and Iran, with an economy built on wholesale trade, transport, dry fruit, coal and government employment. Its businesses deal with FBR for income tax and with the Balochistan Revenue Authority for services.",
     "Quetta tax consultant for traders, transporters, dry fruit and coal businesses and government staff: FBR returns, BRA sales tax and records, online.",
     """## FBR and the Balochistan Revenue Authority

Income tax is federal; sales tax on services in Balochistan is collected by the Balochistan Revenue Authority under the province's own law. Contractors, hotels, restaurants and consultancies in Quetta may therefore have BRA obligations alongside their FBR return.

## Wholesale and Transit Trade

Quetta's wholesale markets, including those around Liaquat Bazaar, deal in goods arriving from Karachi and across the borders. Traders should keep purchase invoices showing import-stage taxes and records of sales to retailers across the province. Goods without proper documentation create customs risks as well as tax questions.

## Dry Fruit and Agriculture

Orchards in Quetta valley and the surrounding districts grow apples, apricots, grapes and almonds. Orchard income is agricultural and taxed by the province; dry fruit traders who buy, process and sell earn business income.

## Coal and Minerals

Coal mining and transport in the districts around Quetta involve leases, royalties to the province and payments to contractors with tax deducted. Each payment needs documentation.

## Government Employees

Provincial and federal employees make up a large share of Quetta's formal workforce; their salaries are taxed at source.

## Getting Started

Send your documents on WhatsApp 0328-4675162; we prepare FBR returns and BRA filings remotely.""",
     [("Do Quetta service businesses register with BRA?",
       "Services taxable under the Balochistan law above the threshold require BRA registration, separate from FBR."),
      ("Is Quetta orchard income taxed by FBR?",
       "No, orchard income from your own land is agricultural and taxed by the province."),
      ("Are mineral royalties income tax?",
       "No, royalties are paid to the province under the lease and are a business cost; income tax still applies to profit.")])

page("quetta",
     "Quetta residents register for an NTN to open business accounts, bid for government contracts, trade with registered buyers or buy property at the lower filer rate. Registration is online on IRIS; service businesses then register with the Balochistan Revenue Authority.",
     "NTN registration in Quetta for traders, contractors and families: IRIS steps, documents and when Balochistan Revenue Authority registration follows.",
     """## Who Registers in Quetta

- **Government contractors** who must have an NTN and, often, active filer status before bills are paid.
- **Traders** in Quetta's wholesale markets opening business accounts.
- **Transporters** operating goods and passenger services.
- **Families** buying property in Quetta or elsewhere.

## Registering from Quetta

The registration itself takes place on IRIS and follows the steps in our [FBR registration guide](/blogs/fbr-registration-step-by-step). For Quetta applicants, the practical hurdle is usually the mobile number: verification codes go to the number entered, and SIMs registered to a relative or a former employer cause trouble later when passwords need resetting. Traders who describe their shop by bazaar name should also add the street and building, because BRA and banks later compare the address with the rent agreement.

## Connectivity and Documents

Clients in Quetta sometimes face slow connections; registration can be completed by us remotely once you share your CNIC, a working mobile number for codes and your address proof.

## BRA After the NTN

Service businesses register with the Balochistan Revenue Authority once they cross its threshold.

## Getting Started

Send your CNIC and business details on WhatsApp. NTN registration is Rs 2,000 on our [pricing page](/pricing).""",
     [("Do Quetta government contractors need active filer status?",
       "Being on the Active Taxpayers List lowers deductions on payments and is often required."),
      ("Can you register my NTN remotely from Quetta?",
       "Yes, with your CNIC, a working mobile number for verification codes and address proof."),
      ("Is BRA registration automatic?",
       "No, it is separate from FBR and required only for taxable services.")],
     kind="ntn-registration")

page("cantt-quetta",
     "Quetta Cantonment hosts military institutions, including the well-known staff college, alongside officers' residences and cantonment markets. Our Quetta Cantt clients are officers, their families, civilian staff and cantonment businesses.",
     "Quetta Cantt tax help for officers, families, civilian staff and cantonment businesses: salary, allotted plots, pensions and returns, filed online.",
     """## Officers on Courses and Postings

Officers posted to Quetta, including those attending courses at the cantonment's institutions, often have families and property in other cities. Their returns cover all income and assets wherever located, and their salary tax is deducted at source. Plots allotted through defence schemes are shown at the amounts paid.

## Families Managing Property Elsewhere

Spouses managing rented houses in Lahore, Rawalpindi or Karachi while the officer is posted in Quetta should declare the rent in the name of the owner, and the owner's return should show it.

## Civilian Staff

Civilian employees of cantonment and military bodies file salaried returns.

## Cantonment Businesses

Shops and service providers within the cantonment file FBR returns and, for taxable services, BRA returns.

## Getting Started

Share salary certificates, allotment letters and tenancy agreements. We prepare returns for officers and families wherever they are posted.""",
     [("Do officers posted in Quetta declare rent from houses elsewhere?",
       "Yes, the property owner declares rent from all properties regardless of where they are."),
      ("Do cantonment businesses in Quetta register with BRA?",
       "If they provide taxable services under the Balochistan law, yes."),
      ("How are defence scheme plots shown?",
       "At the amounts paid, from allotment.")])

page("double-road-quetta",
     "Double Road is one of Quetta's main commercial arteries, with showrooms, offices, restaurants and residential blocks. Our Double Road clients are showroom owners, office-based businesses, restaurateurs and landlords.",
     "Double Road Quetta tax help for showrooms, offices, restaurants and landlords: FBR returns, BRA services tax, rent and records, filed online.",
     """## Showrooms

Car, motorcycle and electronics showrooms on Double Road deal in high-value goods. Stock registers recording each item's purchase and sale, together with invoices, support profit figures. Vehicles sold involve advance tax at registration in the buyer's name.

## Offices

Contractors, consultants and NGOs maintain offices here. Their staff salaries require tax deduction, and services may fall under BRA's law.

## Restaurants

Restaurants charge sales tax on services under the Balochistan law and file FBR returns.

## Landlords

Owners of buildings let to showrooms and offices receive rent, often with tax deducted by organisational tenants.

## Getting Started

Share stock registers, payroll, BRA returns or tenancy agreements. We prepare the filings.""",
     [("Do Quetta restaurants file with BRA?",
       "Restaurant services are generally taxable under the Balochistan law."),
      ("What records should a showroom keep?",
       "A stock register with each item's purchase and sale details, plus invoices."),
      ("Is rent from an NGO office taxed at source?",
       "Organisations that are withholding agents usually deduct tax from rent.")])

page("zarghoon-road-quetta",
     "Zarghoon Road runs through central Quetta past government offices, hotels, banks and residential areas, named after the Zarghoon mountain that overlooks the city. Our Zarghoon Road clients are hotels, government employees, banks' staff and local businesses.",
     "Zarghoon Road Quetta tax help for hotels, government employees and local businesses: BRA services tax, salaried returns and records, done online.",
     """## Hotels and Guest Houses

Hotels along Zarghoon Road serve government visitors, business travellers and tourists heading to Ziarat and other destinations. Room and food services are generally taxable under the Balochistan law, and occupancy records support BRA and FBR returns.

## Government Employees

Provincial secretariat and department staff living along the road file salaried returns; arrears and allowances should be checked on salary certificates.

## Banks' Staff

Bank employees receive salaries with tax deducted and often have staff loans; loan balances are liabilities in the wealth statement.

## Local Businesses

Shops and restaurants keep sales records and file returns; restaurants register with BRA.

## Getting Started

Share occupancy records, salary certificates or business records. We prepare returns and BRA filings.""",
     [("Do Quetta hotels charge BRA sales tax?",
       "Accommodation and food services are generally taxable under the Balochistan law."),
      ("Are staff loans shown in the wealth statement?",
       "Yes, outstanding loan balances are liabilities."),
      ("Can government employees claim refunds?",
       "Yes, if tax deducted exceeds their liability.")])

page("hyderabad",
     "Hyderabad, Sindh's second city, combines a historic trading centre with Kotri's industrial estate, Latifabad and Qasimabad's residential towns and a hinterland of farms. Its businesses report to FBR for income tax and to the Sindh Revenue Board for services.",
     "Hyderabad Sindh tax consultant for traders, Kotri industry, bangle makers and families: FBR returns, SRB services tax, agricultural income and records.",
     """## FBR and SRB

Income tax is federal; sales tax on services in Sindh is administered by the Sindh Revenue Board. Restaurants, hotels, consultancies and many other services in Hyderabad need SRB registration once above the threshold, alongside FBR filing.

## Historic Trade and Crafts

Hyderabad's markets, including the old Shahi Bazaar, are known for trading and for the city's glass bangle industry, much of which is carried out in homes and small workshops. Bangle makers earn business income per batch or piece, and traders supplying markets across Pakistan keep purchase and sales records.

## Kotri and Industry

The industrial estate at Kotri, across the Indus, has textile, chemical and food units. Manufacturers register for sales tax, deduct tax from staff and suppliers and file monthly returns.

## Farmland in the Hinterland

Many Hyderabad families own farmland in surrounding districts. Agricultural income is taxed by Sindh and declared as exempt in the federal return.

## Getting Started

Share your documents on WhatsApp 0328-4675162. We prepare FBR returns and SRB filings remotely.""",
     [("Do Hyderabad restaurants register with SRB?",
       "Restaurant services in Sindh are generally taxable under the Sindh law."),
      ("How are home-based bangle makers taxed?",
       "On business income from their work after material costs, supported by a record of batches and payments."),
      ("Is Sindh agricultural income taxed by FBR?",
       "No, it is taxed by Sindh and declared as exempt in the federal return.")])

page("hyderabad",
     "Hyderabad residents register for an NTN when starting businesses, supplying Kotri's industries, freelancing or preparing to buy property. Registration is online on IRIS, and service businesses then register with the Sindh Revenue Board.",
     "NTN registration in Hyderabad Sindh: IRIS steps, documents for traders, suppliers and freelancers, and when SRB registration is also needed.",
     """## Who Registers in Hyderabad

- **Suppliers** to Kotri's factories, which ask for NTNs and sales tax registration.
- **Traders** in the city's markets opening business accounts.
- **Students and freelancers** at the universities in Jamshoro and Hyderabad earning from abroad.
- **Families** buying property who want the lower filer rate.

## Registering from Hyderabad

The online steps are the same everywhere and are set out in our [FBR registration guide](/blogs/fbr-registration-step-by-step). What differs in Hyderabad is the paperwork that follows: suppliers to Kotri's factories are usually asked for sales tax registration within weeks, which needs electricity connection details for the premises, so it helps to have the latest commercial bill ready when you start.

## Addresses in Latifabad and Qasimabad

Units in Latifabad and Qasimabad are identified by unit and block numbers; enter them exactly as on your utility bill.

## SRB After the NTN

Service businesses register with the Sindh Revenue Board once they cross its threshold.

## Getting Started

Send your CNIC and business details on WhatsApp. NTN registration is Rs 2,000 on our [pricing page](/pricing).""",
     [("Do Kotri suppliers need sales tax registration?",
       "Suppliers of taxable goods to registered manufacturers usually do."),
      ("Can students at Jamshoro register for an NTN?",
       "Yes, once they earn income or need a tax number for banking."),
      ("Is SRB registration part of the NTN process?",
       "No, it is separate and required only for taxable services.")],
     kind="ntn-registration")

page("latifabad-hyderabad",
     "Latifabad is Hyderabad's largest residential town, organised in numbered units with markets, schools, hospitals and small businesses. Our Latifabad clients are salaried families, shopkeepers, doctors and owners of rented portions.",
     "Latifabad Hyderabad tax help for salaried families, shopkeepers, doctors and landlords: returns, SRB where needed, rent and wealth statements online.",
     """## Salaried Families

Latifabad's households include government employees, bank staff and teachers. Their salary tax is deducted; filing claims refunds and keeps them on the Active Taxpayers List.

## Shopkeepers in the Units' Markets

Each unit has its own market of grocery, clothing and electronics shops. Purchase bills, monthly sales and electricity bills support returns.

## Doctors

Clinics and hospitals serve the town; doctors declare salary and private practice income.

## Rented Portions

Houses are often split into portions let to families; rent is declared each year.

## Property

Latifabad houses change hands frequently. Filing before buying lowers the advance tax.

## Getting Started

Share salary certificates, shop or clinic records and tenancy agreements. We prepare returns for the household.""",
     [("Do Latifabad shopkeepers need SRB registration?",
       "Retail sale of goods is not a service; SRB applies to taxable services such as restaurants."),
      ("Is rent from a portion taxable?",
       "Yes, rent is declared each year."),
      ("Can salaried residents claim refunds?",
       "Yes, by filing returns if tax deducted exceeds liability.")])

page("qasimabad-hyderabad",
     "Qasimabad is a fast-growing residential and commercial area of Hyderabad, known for its restaurants, schools, clinics and new housing schemes. Our Qasimabad clients are restaurant owners, school owners, professionals and property investors.",
     "Qasimabad Hyderabad tax help for restaurants, schools, professionals and property investors: SRB services tax, returns and property records online.",
     """## Restaurants and Food Streets

Qasimabad's restaurants and food outlets draw diners from across Hyderabad. Restaurant services are taxable under the Sindh law, so outlets above the threshold register with SRB and file monthly, alongside their FBR returns.

## Private Schools and Colleges

Schools and colleges charge fees and employ teachers, deducting tax from salaries above the threshold.

## Professionals

Doctors, lawyers and engineers living in Qasimabad declare professional income and claim tax deducted by institutions.

## Housing Schemes

New schemes attract investors; plots are assets at amounts paid and sales are taxable gains.

## Getting Started

Share SRB returns, sales records, school records or property papers. We prepare the returns.""",
     [("Do Qasimabad restaurants file SRB returns?",
       "Yes, restaurant services are taxable under the Sindh law once above the threshold."),
      ("How do schools handle teachers' tax?",
       "They deduct tax from salaries above the threshold and file withholding statements."),
      ("Is selling a plot in a Qasimabad scheme taxable?",
       "Yes, the gain is taxable and advance tax applies at transfer.")])

page("hyderabad-qasimabad",
     "This page focuses on Qasimabad's families and residents rather than its businesses: households of professionals, government employees and landowners who have moved to the area's newer neighbourhoods.",
     "Qasimabad Hyderabad residents: tax help for professional and landowning families, government employees and home buyers, with returns filed online.",
     """## Landowning Families

Many Qasimabad families own farmland in districts around Hyderabad. Agricultural income is taxed by Sindh and declared as exempt in the federal return; it often explains the purchase of homes and vehicles.

## Government Employees

Families of provincial and federal employees file salaried returns and declare any rent and profit.

## Home Buyers

Families moving from the old city or Latifabad to Qasimabad should document both the sale of the old home and the purchase of the new one.

## Children's Education

Fees for private schools and universities are household expenses in the wealth statement.

## Getting Started

Share land records, salary certificates and property documents. We prepare returns for each earning family member.""",
     [("How does farm income in Sindh appear in my return?",
       "As exempt income, supported by land and sale records."),
      ("How do I show a move from Latifabad to Qasimabad?",
       "Declare the sale of the old home and the purchase of the new one in the same year's wealth statement."),
      ("Are school fees part of my wealth statement?",
       "Yes, as household expenses.")])

page("gujranwala",
     "Gujranwala is one of Punjab's major manufacturing cities, known for fans, sanitary fittings, steel, cutlery from nearby Wazirabad and electrical goods, along with a large wholesale trade. Tax work here centres on manufacturing, sales tax and family businesses.",
     "Gujranwala tax consultant for manufacturers, wholesale traders and family businesses: sales tax, withholding, PRA and returns, filed online.",
     """## Manufacturing Clusters

Fan makers, sanitary fittings producers, steel re-rolling mills and electrical goods manufacturers make up Gujranwala's industry. Manufacturers generally register for sales tax, file monthly returns and verify suppliers so input tax can be claimed. Scrap and metal purchases are a common area of FBR scrutiny, so purchase documentation matters.

## Family Businesses

Many factories are owned by families and run as partnerships or private companies. Partners' shares, directors' remuneration and loans between family and firm should be documented.

## Wholesale Trade

Gujranwala's markets distribute goods across northern Punjab. Traders keep purchase and sales records and credit ledgers.

## Services and PRA

Services provided in Gujranwala, such as restaurants and repair services, are taxed by the Punjab Revenue Authority.

## Getting Started

Share sales tax returns, purchase records and partnership documents on WhatsApp 0328-4675162.""",
     [("Why is scrap purchase documentation important?",
       "Scrap and metal purchases are often scrutinised; proper invoices from registered suppliers support input tax and costs."),
      ("Do Gujranwala fan manufacturers need sales tax registration?",
       "Manufacturers are generally required to register for federal sales tax."),
      ("How should family factories be structured for tax?",
       "As a documented partnership or company, with each member's share or remuneration recorded.")])

page("gujranwala",
     "Gujranwala residents and manufacturers register for an NTN when starting a factory or trade, supplying registered buyers, or buying property. Registration is online, and manufacturers usually follow it with sales tax registration.",
     "NTN registration in Gujranwala for manufacturers, traders and families: IRIS steps, documents and sales tax or PRA registration afterwards.",
     """## Who Registers in Gujranwala

- **Small manufacturers** of fans, fittings and electrical goods supplying distributors.
- **Traders** opening business accounts.
- **Workers and engineers** starting their own workshops.
- **Families** buying property.

## Registering a Gujranwala Workshop

The IRIS process is described in our [FBR registration guide](/blogs/fbr-registration-step-by-step). For a Gujranwala workshop, describe the principal activity precisely, for example fan assembly or sanitary fittings casting, because the activity code is used later for sales tax registration and affects which rules apply. Register the business under the owner's CNIC if it is a sole proprietorship; brothers running a unit together should register the firm as an AOP.

## Sales Tax Registration for Factories

After the NTN, manufacturers apply for sales tax registration, which involves premises details, electricity connection information and verification.

## PRA for Services

Service businesses register with the Punjab Revenue Authority.

## Getting Started

Send your CNIC and business details on WhatsApp. NTN registration is Rs 2,000 and sales tax registration Rs 3,000 on our [pricing page](/pricing).""",
     [("What does sales tax registration need for a factory?",
       "Premises details, the industrial electricity connection information and verification of the unit."),
      ("Can a small workshop register an NTN online?",
       "Yes, through IRIS with the owner's CNIC."),
      ("Does an NTN make me an active filer?",
       "No, only filing a return does.")],
     kind="ntn-registration")

page("trust-colony-gujranwala",
     "Trust Colony is a residential area of Gujranwala where many factory owners, managers and professionals live, close to the city's commercial roads. Our Trust Colony clients are business families, professionals and landlords.",
     "Trust Colony Gujranwala tax help for factory-owning families, professionals and landlords: returns, drawings, rent and wealth statements online.",
     """## Factory-Owning Families

Families who own factories elsewhere in Gujranwala live in Trust Colony. Personal returns should match business accounts: drawings from partnerships, salaries and dividends from companies, and loans between the family and the business.

## Professionals

Doctors, lawyers and engineers declare professional income and claim tax deducted by institutions.

## Landlords

Houses and portions let to families produce rent declared each year.

## Lifestyle and Wealth Statements

Visible spending such as vehicles and foreign travel should be reflected in household expenses.

## Getting Started

Share business drawings records, salary or practice records and tenancy agreements. We prepare returns for the household.""",
     [("How should factory drawings appear in personal returns?",
       "Drawings are not new income, but they should match the business accounts and explain personal spending."),
      ("Do professionals in Trust Colony claim tax deducted by clients?",
       "Yes, as credits against their liability."),
      ("Is rent from a portion taxable?",
       "Yes, rent is declared each year.")])

page("sialkot",
     "Sialkot is one of Pakistan's most export-oriented cities, famous for sports goods, surgical instruments, leather and gloves, with thousands of small workshops feeding large exporters. Tax work here is about export proceeds, sales tax refunds and documenting the supply chain.",
     "Sialkot tax consultant for exporters of sports goods, surgical instruments and leather, and their vendors: export regime, refunds and returns online.",
     """## Exporters

Sialkot's exporters receive foreign payments through banks, with tax deducted on proceeds. Recent budgets moved many exporters of goods towards the normal regime, where the deduction is a minimum tax and the return must show profit and expenses. Export documents for each shipment are essential.

## The Vendor Network

Behind each exporter are forging, polishing, stitching and packing workshops. Exporters increasingly require vendors to hold NTNs and sales tax registration, because unregistered purchases weaken the exporter's records and input tax claims.

## Sales Tax Refunds

Exporters' input tax refunds depend on registered suppliers and accurate invoices. Supplier verification before purchase protects refund claims.

## Small Workshops

Workshops supplying exporters earn business income; tax deducted by exporters on payments is a credit.

## Getting Started

Share export documents, supplier lists and sales tax returns on WhatsApp 0328-4675162. See also our [Paris Road Sialkot guide](/blogs/paris-road-sialkot).""",
     [("Is tax on Sialkot export proceeds final?",
       "For many exporters of goods it now works as minimum tax under the normal regime; we confirm the treatment each year."),
      ("Why do exporters ask vendors for sales tax registration?",
       "Unregistered purchases weaken input tax claims and the exporter's records."),
      ("Can vendors claim tax deducted by exporters?",
       "Yes, as credits in their returns.")])

page("sialkot",
     "Sialkot's workshops and exporters register for an NTN to open business accounts, supply exporters, receive foreign payments and obtain sales tax registration. Registration is online on IRIS.",
     "NTN registration in Sialkot for exporters, workshops and vendors: IRIS steps, documents and sales tax registration for the export supply chain.",
     """## Who Registers in Sialkot

- **Workshops** in forging, polishing and stitching that supply exporters.
- **New exporters** setting up to ship directly.
- **Freelancers** working for foreign clients.
- **Families** buying property.

## Registering a Sialkot Supplier

The online steps are in our [FBR registration guide](/blogs/fbr-registration-step-by-step). Sialkot vendors should register under the name that will appear on invoices to exporters, with the workshop's actual address, because exporters match supplier details when they claim input tax and when banks process export documents. A forging or polishing unit working from home should still use the address where the work is done.

## After the NTN

Exporters register with relevant export bodies and banks for export documentation; vendors supplying exporters register for sales tax so their invoices support input tax claims.

## Getting Started

Send your CNIC and business details on WhatsApp. NTN registration is Rs 2,000 and sales tax registration Rs 3,000 on our [pricing page](/pricing).""",
     [("Do small Sialkot workshops need sales tax registration?",
       "Exporters increasingly require it from vendors whose invoices support their input tax claims."),
      ("What else does a new exporter need after the NTN?",
       "Bank and export documentation arrangements and membership of relevant export bodies."),
      ("Can freelancers in Sialkot register online?",
       "Yes, through IRIS.")],
     kind="ntn-registration")

page("dha-lahore-area",
     "This page covers DHA Lahore as a whole, from the older phases near the cantonment to the newer phases towards Bedian Road, as a guide to the tax questions that come up across DHA rather than in any single phase. For phase-specific guides, see our Lahore area pages.",
     "DHA Lahore tax overview across all phases: plots and files, rental income, section 7E, transfers and wealth statements, with links to phase guides.",
     """## Files, Plots and Houses

DHA Lahore's market moves through files, allocated plots and built houses. Each stage has its own documents: the file's allocation letter, the plot's allotment, and the house's completion records. The wealth statement shows each at the amounts paid.

## Section 7E Across Phases

Owners holding plots in several phases should review section 7E annually. One self-occupied house is excluded, and let-out property with rent declared is excluded, but vacant plots above the aggregate value limit can attract deemed income tax.

## Rental Income

Houses in DHA are let to families and companies; corporate tenants deduct tax from rent. Rent from every property is declared.

## Transfers

DHA's transfer process runs alongside federal advance tax at registration. Being on the Active Taxpayers List halves the federal rate.

## Phase Guides

For local detail, see our guides to individual phases, such as [DHA Phase 5](/blogs/tax-consultant-dha-phase-5-lahore), and the [Lahore hub](/tax-consultant-lahore).""",
     [("Is a DHA file an asset before a plot is allocated?",
       "Yes, the amounts paid are shown in the wealth statement as an asset."),
      ("Does section 7E apply to vacant DHA plots?",
       "It can, if your total property value exceeds the limit and no exemption applies."),
      ("Does filing reduce advance tax on DHA transfers?",
       "Yes, the federal advance tax rate is lower for persons on the Active Taxpayers List.")])
