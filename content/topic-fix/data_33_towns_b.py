"""Towns B: Bhimber, Bhalwal, Battagram, Awaran, Bagh, Ahmadpur East, Badin, Builders, Buner, Burewala."""
from towns import town

PAGES = {}

AJK_NOTE = ("Azad Jammu and Kashmir has its own income tax law and administration for income arising within AJK, separate from FBR. "
            "Income from Pakistan proper, such as a salary from a federal employer or rent from a house in Islamabad, is dealt with by FBR.")

town(PAGES, "bhimber",
     tax=("Bhimber, in southern Azad Kashmir near Mirpur and the Samahni valley, is a district of farming villages, a growing town and many families with relatives in the UK and the Gulf. Its residents often deal with two tax systems: AJK's own for local income and FBR's for income and property in Pakistan.",
          "Bhimber AJK tax help: AJK and FBR obligations, UK and Gulf remittances, property in Pakistan and AJK, and returns prepared online.",
          f"""## Two Tax Systems

{AJK_NOTE} A Bhimber family that rents out a shop in the town and also owns a plot in Rawalpindi may therefore have obligations to both. Mapping each source of income to the right authority is the first step.

## British-Kashmiri Families

Many families in Bhimber and Samahni have relatives in Britain. Money sent home for houses and land should be traceable through bank transfers. Relatives living in the UK who own property in AJK or Pakistan also need to consider UK reporting of that property's income.

## Property in Pakistan

Families buying plots in Islamabad, Rawalpindi or Gujrat deal with FBR's advance tax at registration, which is lower for persons on the Active Taxpayers List.

## Government Employees

AJK government employees are taxed under AJK's system on their salaries; any income from Pakistan proper is an FBR matter.

## Getting Started

Tell us where each income and asset is located, and we help map them to the right system and prepare the FBR return where it applies.""",
          [("Does FBR tax my shop rent in Bhimber?",
            "Income arising in AJK is taxed under AJK's own law; FBR deals with income from Pakistan proper."),
           ("Do I need to file with FBR to buy a plot in Rawalpindi?",
            "Filing an FBR return puts you on the Active Taxpayers List and lowers the advance tax at registration."),
           ("How should UK relatives' money for a house be documented?",
            "Through bank transfers, with a note of what each transfer was for.")]),
     ntn=("People from Bhimber register for an FBR NTN mainly to deal with income or property in Pakistan proper, such as buying a plot in Islamabad, working for a federal employer or receiving payments from Pakistani companies.",
          "FBR NTN registration for Bhimber residents: when an AJK resident needs it, property in Pakistan proper, federal income and filer status.",
          """## When an AJK Resident Needs an FBR NTN

An NTN from FBR is needed where you have dealings within FBR's jurisdiction: a salary from a federal or private employer in Pakistan proper, rent from property in Rawalpindi or Islamabad, a business supplying Pakistani companies, or a property purchase in Pakistan where filer status lowers advance tax.

## Families with Relatives Abroad

Relatives in the UK or the Gulf who plan to buy property in Pakistan can register with their CNIC or NICOP and file from abroad.

## Contractors

Contractors who work on projects in Pakistan proper, such as in Gujrat or Jhelum, need an FBR NTN and often active filer status.

## AJK's Own Registration

Taxpayers with income arising in AJK deal with AJK's revenue authorities for that income; an FBR NTN does not replace AJK registration.

## Registering

The IRIS steps are in our [FBR registration guide](/blogs/fbr-registration-step-by-step). Use your current address in Bhimber; FBR registration does not depend on living in Pakistan proper.""",
          [("Do Bhimber residents need an FBR NTN?",
            "Only for dealings within FBR's jurisdiction, such as income or property in Pakistan proper."),
           ("Can relatives in the UK register?",
            "Yes, with their CNIC or NICOP, and file from abroad."),
           ("Does an FBR NTN cover AJK taxes?",
            "No, AJK income is dealt with by AJK's own authorities.")]),
     inc=("For Bhimber residents, an FBR income tax return covers income and assets connected with Pakistan proper, while AJK income follows AJK's system. This page explains what goes into the FBR return.",
          "FBR income tax return for Bhimber residents: which income to include, property in Pakistan, remittances and the wealth statement, filed online.",
          """## What Goes in the FBR Return

Income from Pakistan proper, such as salary from a Pakistani employer, rent from property in Rawalpindi or profit from a Pakistani bank, belongs in the FBR return. Income arising within AJK is dealt with under AJK's system.

## The Wealth Statement

Residents who file with FBR complete a wealth statement. Assets in AJK and Pakistan proper alike are listed so the statement reconciles, with notes on which income is taxed under which system.

## Remittances

Money from relatives in the UK or Gulf received through banks is not the receiver's taxable income, but it explains assets bought with it.

## A Worked Example

A Bhimber resident works for a bank branch in Mirpur and owns a flat in Islamabad let for Rs 600,000 a year. The flat's rent is declared in the FBR return; the salary's treatment depends on where the employment and income arise, which we review.

## Getting Started

Share details of each income and asset with their locations. We prepare the FBR return where it applies.""",
          [("Do I declare AJK property in my FBR wealth statement?",
            "We generally list all assets so the statement reconciles, noting which income is taxed under AJK's system."),
           ("Is rent from an Islamabad flat taxed by FBR?",
            "Yes, property in Pakistan proper is under FBR's jurisdiction."),
           ("Are remittances from the UK taxable?",
            "Generally not, when received through banks, but they explain assets bought.")]))

town(PAGES, "bhimber-city",
     tax=("Bhimber town is the district's commercial centre, with shops, government offices, schools and a growing number of businesses run by returning overseas families. This page focuses on town businesses and families buying property in Pakistan proper.",
          "Bhimber town businesses and families: AJK and FBR obligations for shops, returning overseas families and property purchases in Pakistan, online.",
          """## Town Shops

Retailers in Bhimber's bazaar earn income arising in AJK, taxed under AJK's system. Those who also supply customers or buy from wholesalers in Pakistan proper should keep invoices showing taxes paid on the goods.

## Returning Overseas Families

Families returning from the UK after years abroad often open businesses or build houses. Their foreign savings explain these investments; bank records of transfers from abroad are the key evidence. Returning residents should also consider the UK tax position of income left behind.

## Buying Property in Gujrat, Jhelum or Islamabad

Town families investing in Pakistan proper pay FBR advance tax at registration, lower for active filers.

## Government Offices

Employees of AJK departments are taxed under AJK's system.

## Getting Started

Share where your income and assets are; we help you file with FBR where needed.""",
          [("Are Bhimber shops taxed by FBR?",
            "Income arising in AJK is taxed under AJK's own system."),
           ("How do returning families show savings from the UK?",
            "Through bank records of transfers, which explain assets bought in Pakistan or AJK."),
           ("Does FBR filing help when buying in Jhelum?",
            "Yes, filer status lowers the advance tax at registration.")]))

town(PAGES, "bhalwal",
     tax=("Bhalwal in Sargodha district is at the heart of Pakistan's kinnow (citrus) belt, with orchards, grading and waxing plants, and exporters shipping fruit to the Gulf, Russia and Asia. Our Bhalwal clients are orchard owners, fruit contractors, processing plants and exporters.",
          "Bhalwal tax consultant for kinnow orchard owners, fruit contractors, waxing plants and exporters: farm and export income, returns online.",
          """## Orchard Owners

Kinnow orchards are agricultural land, and income from selling fruit grown on your own orchard is taxed by Punjab and declared as exempt in the federal return. Many owners sell the whole season's crop on the tree to contractors; the payment is still agricultural income for the owner.

## Fruit Contractors

Contractors who buy orchards' crops and sell the fruit to markets or processors are traders. Their profit is business income taxed by FBR, calculated from the price paid for orchards, picking and transport costs and sale proceeds.

## Grading and Waxing Plants

Plants that wash, wax, grade and pack kinnow for export run business operations with machinery, labour and packaging costs. They may provide processing on charge to exporters or process their own fruit.

## Exporters

Exporters receive proceeds through banks with tax deducted under the export rules. Shipping documents and bank realisation records for each consignment support the return.

## Getting Started

Share orchard sale agreements, contractor records, plant records or export documents on WhatsApp 0328-4675162.""",
          [("Is selling my orchard's crop to a contractor agricultural income?",
            "Yes, for the orchard owner; the contractor's resale profit is business income."),
           ("Do kinnow exporters have tax deducted?",
            "Banks deduct tax on export proceeds under the export rules."),
           ("How do waxing plants calculate income?",
            "From processing charges or fruit sales, less labour, packaging, chemicals and depreciation.")]))

town(PAGES, "battagram",
     tax=("Battagram district lies on the Karakoram Highway in the Hazara mountains, with terraced farming, forests and many families supported by men working in the Gulf and in Pakistan's cities. Our Battagram clients are government employees, traders and remittance families.",
          "Battagram tax help for government employees, traders and remittance families in Hazara: returns, filer status, property records and KPRA, online.",
          """## Remittance Families

Many Battagram households rely on relatives working in Saudi Arabia, the UAE and Karachi. Remittances through banks are not the receiver's taxable income, but houses and land bought with them belong in the wealth statement, supported by bank records.

## Government Employees

Teachers, health workers and officials file salaried returns; filing claims refunds of excess deductions and keeps them on the Active Taxpayers List.

## Traders on the Highway

Shops and eateries along the Karakoram Highway serve travellers and trucks heading north. Daily cash records and regular deposits create the evidence needed for returns.

## Forestry and Agriculture

Small farms grow maize and wheat; agricultural income is taxed by the province. Timber trade is regulated and documented through permits, which also serve as records.

## Getting Started

Share salary certificates, shop records or property papers on WhatsApp; we prepare returns remotely.""",
          [("Are Gulf remittances taxable for Battagram families?",
            "Generally not, when received through banks, but assets bought with them belong in the wealth statement."),
           ("Do highway eateries need records?",
            "Yes, daily cash records and deposits support their returns."),
           ("Can teachers in Battagram claim refunds?",
            "Yes, if tax deducted exceeds their liability.")]))

town(PAGES, "battagram-city",
     tax=("Battagram town is the district headquarters, where government offices, the bazaar, schools and transport stands serve surrounding valleys. This page covers town traders, transporters and office staff.",
          "Battagram town tax help for bazaar traders, transporters and government office staff: returns, vehicle tax credits and records, prepared online.",
          """## Bazaar Traders

Wholesalers and shopkeepers in Battagram's bazaar supply villages across the district, often on credit until remittances or harvests arrive. A credit ledger is as important as purchase invoices, because amounts owed by customers on 30 June are assets.

## Transport Stands

Wagons and coaches connect the town with Mansehra, Abbottabad and Rawalpindi. Owners pay advance tax with vehicle tax, adjustable when filing.

## District Office Staff

Officials posted to Battagram from elsewhere often own property in their home districts, all of which belongs in their wealth statements.

## Contractors

Contractors working on roads and buildings for government departments have tax deducted on bills; filer status lowers the rate.

## Getting Started

Share ledgers, vehicle records or salary certificates; we prepare the return.""",
          [("Is credit given to village customers an asset?",
            "Yes, amounts receivable on 30 June are assets in the wealth statement."),
           ("Can wagon owners adjust vehicle tax?",
            "The advance income tax part is adjustable in the return."),
           ("Do posted officials declare property elsewhere?",
            "Yes, all assets are declared wherever they are.")]))

town(PAGES, "awaran",
     tax=("Awaran is one of Balochistan's most remote districts, with a small, largely agricultural and livestock-based economy and a population served mainly by government employment. Our Awaran clients are government employees, contractors and small traders.",
          "Awaran Balochistan tax help for government employees, contractors and small traders: salaried returns, contract income and filer status, online.",
          """## Government Employees

Teachers, health staff and officials form much of Awaran's formal workforce. Their salary tax is deducted at source, and filing claims any refund and keeps them on the Active Taxpayers List.

## Contractors on Development Works

Roads, schools and water schemes are built by contractors paid by government departments, which deduct income tax and may require BRA registration for services. A register of contracts and deductions supports their returns.

## Agriculture and Livestock

Dates, crops and livestock are important to local livelihoods. Agricultural income is taxed by the province.

## Small Traders

Shops in Awaran town supply surrounding villages; simple purchase and sales records support returns.

## Filing Remotely

Because Awaran is far from tax offices, filing online through a consultant avoids long journeys. Documents can be shared by WhatsApp.""",
          [("Do Awaran contractors need BRA registration?",
            "Construction and other services can be taxable under the Balochistan law depending on turnover."),
           ("Can government employees file without travelling?",
            "Yes, returns are filed online from shared documents."),
           ("Is livestock income taxed by FBR?",
            "Livestock as part of farming is generally agricultural; commercial trading is business income.")]))

town(PAGES, "bagh-ajk",
     tax=("Bagh is a hilly district of Azad Kashmir known for its forests, the Sudhan Gali and Ganga Choti areas and a large number of families with members in the armed forces and abroad. Its residents deal with AJK's tax system for local income and FBR for income and assets in Pakistan proper.",
          "Bagh AJK tax help: AJK and FBR obligations, army families, overseas workers, tourism businesses and property in Pakistan, prepared online.",
          f"""## Two Systems

A Bagh household can owe returns in two places. Shop profits, rent from a building in Bagh bazaar or a guest house near Sudhan Gali fall under the AJK Council's tax administration, while a salary paid by a federal department or rent from a flat in Rawalpindi is an FBR matter. Keeping a short list of every income source, with the place where it arises, settles which return each one belongs to.

## Army Families

Many Bagh families have members serving in the army. Serving personnel's salaries are taxed at source by their federal employer, and plots allotted through defence schemes in Pakistan proper belong in their wealth statements.

## Overseas Workers

Workers in the Gulf send money home for houses and land; bank transfers document these.

## Tourism

Guest houses near Sudhan Gali and Ganga Choti serve visitors in summer; their income arises in AJK.

## Getting Started

Tell us where each income and asset is located; we prepare the FBR return where it applies.""",
          [("Do soldiers from Bagh file with FBR?",
            "Their salary from the federal government is taxed at source, and filing an FBR return claims credits and declares assets."),
           ("Is a Sudhan Gali guest house taxed by FBR?",
            "Income arising in AJK is taxed under AJK's system."),
           ("Do remittances need documentation?",
            "Yes, bank transfers explain houses and land bought with them.")]))

town(PAGES, "ahmadpur-east",
     tax=("Ahmadpur East in Bahawalpur district is a historic town of the former Bahawalpur state, near Uch Sharif, with an economy of farming, cotton, small industry and trade. Our Ahmadpur East clients are landowners, ginners, traders and government employees.",
          "Ahmadpur East tax help for landowners, ginners, traders and government employees: farm income, sales tax and returns, filed online.",
          """## Farming and Cotton

Canal-irrigated land around Ahmadpur East grows cotton, wheat and sugarcane. Agricultural income is taxed by Punjab and declared as exempt. Ginning units in the area process seed cotton, deal with sales tax on lint and keep weight and price records.

## Traders

The town's markets sell agricultural inputs, consumer goods and building materials. Input dealers sell on credit until harvest; credit ledgers show amounts owed.

## Heritage and Visitors

Visitors to Uch Sharif's shrines and the old palaces pass through the town; eateries and shops benefit in season.

## Government Employees

Teachers and officials file salaried returns and declare land and houses.

## Getting Started

Share land records, ginning or trade records, or salary certificates on WhatsApp.""",
          [("Do Ahmadpur East ginners register for sales tax?",
            "Ginners selling lint to registered mills generally do."),
           ("Is credit to farmers an asset?",
            "Yes, amounts receivable on 30 June are assets."),
           ("Is cotton farming income taxed by FBR?",
            "No, it is agricultural income taxed by Punjab.")]))

town(PAGES, "ahmedpur-east",
     ntn=("In Ahmedpur East, NTN registration is usually sought by input dealers, ginners, contractors and families buying vehicles or property. This page explains who needs it and what follows.",
          "NTN registration in Ahmedpur East for input dealers, ginners, contractors and families: who needs it, local address details and next registrations.",
          """## Input Dealers

Fertiliser and pesticide dealers buy from distributors that require an NTN and deduct tax on supplies. Registering lets dealers buy directly and claim those deductions.

## Ginners

Ginning units register for an NTN and then for sales tax before the picking season; mills require both.

## Contractors

Contractors on irrigation and road works for government departments need an NTN and benefit from active filer status, which lowers deductions on their bills.

## Families

Farming families buying tractors, motorcycles or plots register and file to pay advance tax at the lower filer rate.

## Address Details

Units outside the town should use the chak or mauza shown on the electricity bill. The online steps are in our [FBR registration guide](/blogs/fbr-registration-step-by-step).""",
          [("Why do distributors deduct tax from dealers?",
            "Distributors act as withholding agents on supplies to dealers; registered dealers claim the deduction as a credit."),
           ("When should a ginner register for sales tax?",
            "Before the season, as registration involves verification of the factory."),
           ("Do farmers need an NTN?",
            "Not for agricultural income alone, but filing gives filer rates on purchases.")]),
     inc=("Returns from Ahmedpur East typically combine exempt farm income with taxable trade, ginning or salary income. This page shows what to include and which credits to claim.",
          "Income tax return filing in Ahmedpur East for landowners, dealers, ginners and employees: farm and business income, credits and an example, online.",
          """## Farm and Trade

A landowner who also runs a fertiliser shop declares crop income as exempt and shop profit as taxable. Separate bank accounts make this easy to show.

## Ginners

A ginner's return shows lint and seed sales, seed cotton purchases, labour, electricity and depreciation. Tax deducted by mills and on electricity bills is credited.

## Employees

Teachers and officials claim tax deducted on salary, bank profit and phone bills.

## A Worked Example

A dealer sells inputs worth Rs 9,000,000 on which his gross margin is Rs 900,000; after shop expenses of Rs 300,000, profit is Rs 600,000. Tax deducted by distributors on his purchases is credited against the tax on that profit.

## Wealth Statement

Land, shop stock, credit to farmers and vehicles appear in the wealth statement on 30 June.""",
          [("Is a dealer taxed on sales or profit?",
            "On profit, though minimum tax rules can apply in some cases."),
           ("Do ginners claim tax deducted by mills?",
            "Yes, as credits."),
           ("Is stock part of the wealth statement?",
            "Yes, business stock on 30 June is an asset.")]))

town(PAGES, "badin",
     tax=("Badin district in lower Sindh combines sugarcane and rice farming, coastal fishing villages and oil and gas fields operated by exploration companies. Our Badin clients are landowners, oil field contractors, rice and sugar businesses and government employees.",
          "Badin tax consultant for landowners, oil and gas field contractors, rice and sugar businesses and employees: FBR, SRB and returns, filed online.",
          """## Oil and Gas Field Contractors

Exploration and production companies in Badin hire local contractors for transport, catering, security and civil works. These companies deduct income tax on payments and require NTNs; many services also fall under the Sindh sales tax on services law administered by the Sindh Revenue Board.

## Sugarcane and Rice Farming

Agricultural income is taxed by Sindh and declared as exempt in the federal return. Sugar mills and rice mills that process crops are federal taxpayers.

## Coastal Fishing

Fishing communities on Badin's coast sell catch to traders; commercial boat owners and traders earn business income.

## Government Employees

Teachers and officials file salaried returns.

## Getting Started

Share contracts, land records or salary certificates on WhatsApp.""",
          [("Do Badin oil field contractors need SRB registration?",
            "Many services such as security and catering are taxable under the Sindh law."),
           ("Is sugarcane farm income taxed by FBR?",
            "No, it is taxed by Sindh."),
           ("Do exploration companies deduct tax on payments?",
            "Yes, contractors claim these as credits.")]),
     ntn=("Badin contractors, traders and families register for an NTN to work with exploration companies and government departments, open business accounts and buy property at filer rates. Service contractors usually follow with SRB registration.",
          "NTN registration in Badin for oil field contractors, traders and families: who needs it, and SRB registration for services in Sindh.",
          """## Contractors for Exploration Companies

Exploration companies require an NTN from every contractor before payment and deduct tax at rates that depend on filer status. Many also require SRB registration for services such as security, catering and vehicle hire.

## Traders

Shops supplying the district's towns register to open business accounts and deal with registered distributors.

## Rice and Sugar Businesses

Mills and traders in rice and sugar need NTNs and sales tax registration.

## Families

Families buying vehicles or land benefit from filer status.

## Registering

The IRIS steps are in our [FBR registration guide](/blogs/fbr-registration-step-by-step). Contractors should use the firm name that appears in contracts.""",
          [("Do exploration companies require SRB registration?",
            "For taxable services, they usually require it from contractors."),
           ("Does filer status matter for contractors?",
            "Yes, deductions on payments are lower for active filers."),
           ("Do rice traders need sales tax registration?",
            "Depending on activity and turnover; we check each case.")]))

town(PAGES, "builders-developers-pakistan",
     tax=("Builders and developers in Pakistan face a mix of federal income tax, provincial sales tax on construction services, withholding duties and advance tax on property, alongside special regimes introduced in recent years. This page covers the compliance side of running a construction or development business.",
          "Tax help for builders and developers in Pakistan: project accounting, provincial sales tax on construction, withholding, buyer advances and returns.",
          """## Project-by-Project Records

A developer's profit is earned project by project, often over several tax years. Keeping a separate cost ledger for each project, covering land, approvals, materials, labour, finance and marketing, makes it possible to recognise profit in the right year and defend it in an audit.

## Advances from Buyers

Buyers usually pay in instalments before possession. These advances are recorded as liabilities until the units are delivered or income is recognised under the method chosen. Instalment schedules and receipts for each buyer are essential.

## Provincial Sales Tax on Construction Services

Construction and development services are taxed by the provinces: PRA in Punjab, SRB in Sindh, KPRA in Khyber Pakhtunkhwa and BRA in Balochistan, with Islamabad under the ICT law administered by FBR. Rates and treatments differ by province.

## Withholding Duties

Developers pay contractors, suppliers and staff and must deduct tax where the law requires, filing withholding statements.

## Special Regimes

Special tax regimes for builders and developers have been introduced in some years; whether a project qualifies depends on registration dates and conditions. Our [real estate developer guide](/blogs/real-estate-developer-tax-pakistan) covers these in more detail.""",
          [("When does a developer recognise profit?",
            "According to the accounting method used consistently, usually linked to delivery or project completion."),
           ("Which authority taxes construction services?",
            "The province where the services are provided, or the ICT law in Islamabad."),
           ("Must developers deduct tax from contractors?",
            "Yes, where the law requires, and file withholding statements.")]))

town(PAGES, "buner",
     tax=("Buner district in the Malakand division of Khyber Pakhtunkhwa is known for its marble industry, its mountain valleys and a large number of families supported by work abroad. Malakand division has had a special tax status over the years, which makes careful checking of each tax essential.",
          "Buner tax help for marble businesses, traders and remittance families in Malakand division: special tax status, FBR and KPRA, prepared online.",
          """## Malakand Division's Special Status

The former Provincially Administered Tribal Areas, including Buner, have enjoyed exemptions from certain federal and provincial taxes, extended in stages over the years. Whether a particular tax applies to a Buner business in a given year depends on the latest extension and its conditions. We check the position for each tax, rather than assuming either full exemption or full liability.

## The Marble Industry

Quarries and marble factories in Buner cut and polish stone for markets across the country. Quarry leases involve royalties to the province; factories deal with machinery, electricity and labour costs. Buyers in other provinces may deduct tax on purchases.

## Remittance Families

Many households depend on relatives abroad; bank transfers document the houses and land bought.

## Traders

Shops in Daggar and other towns supply the valleys.

## Getting Started

Share your business records and we review which taxes apply to you this year.""",
          [("Is Buner still exempt from income tax?",
            "Malakand division has had exemptions extended in stages; the position depends on the year and conditions, so we check each case."),
           ("Do buyers outside Malakand deduct tax on marble purchases?",
            "Buyers acting as withholding agents may deduct tax on payments."),
           ("Are marble quarry royalties a tax?",
            "Royalties are paid to the province under the lease and are a cost of the business.")]))

town(PAGES, "burewala",
     tax=("Burewala in Vehari district is a cotton town with textile mills, ginning factories and one of the region's busy grain markets. Our Burewala clients are mill vendors, ginners, arhtis, landowners and mill staff.",
          "Burewala tax consultant for textile mill vendors, ginners, arhtis, landowners and staff: sales tax, farm income and returns, filed online.",
          """## Textile Mills and Their Vendors

Spinning and textile mills in Burewala buy cotton, spare parts and services from local vendors. Mills deduct income tax on payments and require sales tax registration, because they can claim input tax only on invoices from active registered suppliers.

## Ginners

Ginners sell lint to the mills and seed to oil expellers; weight records and invoices are key.

## Grain Market

Arhtis earn commission on wheat and other crops; amounts passed to farmers are not their income.

## Landowners

Farm income is declared as exempt in the federal return.

## Mill Staff

Managers and workers have salary tax deducted and can claim refunds by filing.

## Getting Started

Share invoices, commission ledgers, land records or salary certificates on WhatsApp.""",
          [("Why do Burewala mills require supplier registration?",
            "They can claim input tax only on invoices from active registered suppliers."),
           ("How are arhtis taxed?",
            "On commission earned."),
           ("Can mill workers claim refunds?",
            "Yes, if tax deducted exceeds their liability.")]),
     ntn=("Burewala vendors, ginners and traders register for an NTN to supply the town's textile mills, deal with registered buyers and open business accounts. Many then register for sales tax.",
          "NTN registration in Burewala for mill vendors, ginners and traders: who needs it and why mills ask for sales tax registration too.",
          """## Vendors to the Mills

Mills ask suppliers of cotton, spare parts, packing material and services for an NTN and usually sales tax registration. Vendors who are inactive lose business because mills cannot claim input tax on their invoices.

## Ginners

Ginners register before the season and keep their sales tax registration active by filing monthly returns.

## Grain Traders

Arhtis and grain dealers register to deal with flour mills and procurement centres.

## Families

Families buying property or vehicles register and file for filer rates.

## Registering

The IRIS steps are in our [FBR registration guide](/blogs/fbr-registration-step-by-step). Use the factory or shop address as on its electricity bill.""",
          [("Do mill vendors need monthly sales tax returns?",
            "Yes, once registered, monthly returns are required to stay active."),
           ("Should ginners register before the season?",
            "Yes, mills require registration before buying lint."),
           ("Do flour mills deduct tax from grain dealers?",
            "They may deduct tax on payments; registered dealers claim the credit.")]))
