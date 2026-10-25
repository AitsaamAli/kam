"""Rewrites and local additions for towns P pages."""

PAGES = {}


def add(rel, text, key="body_more"):
    PAGES.setdefault(rel, {}).setdefault(key, "")
    PAGES[rel][key] += "\n\n" + text


def body(rel, text):
    PAGES.setdefault(rel, {})["body"] = text


body("blogs/ntn-registration-tando-adam.html", """## Why Tando Adam's Ginners Register in Spring

Lower Sindh's cotton is ready earlier than Punjab's, and the first pickings around Tando Adam often reach the ginning factories in July. Spinning mills in Hyderabad, Karachi and Faisalabad buy lint only from ginners who hold an FBR NTN and a sales tax registration number, because they need proper sales tax invoices to claim input tax. The sales tax application involves biometric verification at an e-Sahulat or NADRA centre, details of the factory's electricity connection and, often, a visit to the premises. Ginners who start in March or April are ready when the first trucks of phutti arrive; those who wait until July often lose the early weeks of the season.

## Oil Expellers and Cottonseed Cake

Oil mills crushing cottonseed sell oil to ghee factories and cake to feed mills and dairy farmers. Their buyers need registered suppliers, and their income tax and sales tax figures must agree.

## Commission Agents in the Cotton Market

Mills and exporters paying arhtis through banks withhold income tax at a higher rate from those not on the Active Taxpayers List.

## Truck Owners Carrying Bales

Spinning mills hire registered transporters for bales and withhold tax on freight.

## Families Buying Flats in Hyderabad

Filer status lowers advance tax at transfer.

## Registering

Registration is free and online with a CNIC; our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows each screen.""")

body("blogs/income-tax-filing-tando-adam.html", """## Ginning Accounts That Straddle Two Seasons

Because picking near Tando Adam begins in July, a ginner's tax year from July to June contains almost a whole season. Purchases of seed cotton from growers and middlemen are recorded from gate slips; sales of lint to spinning mills and of cottonseed to oil mills from invoices. Electricity, seasonal labour, bale-pressing, freight and depreciation of gins and presses are the main costs. Seed cotton and bales still in the factory on 30 June are closing stock at cost. Spinning mills' withholding on lint is listed mill by mill and claimed. The total sales figure must match the monthly sales tax returns before filing.

## Oil Mill Owners

Oil and cake sales against cottonseed bought, electricity, labour, packing and depreciation of expellers.

## Commission Agents

Commission received, less shop rent and munshis' salaries; loans to growers are receivables.

## Cotton Growers

Cotton and wheat from family land are agricultural income; any Sindh agricultural income tax paid is noted.

## Transporters

Freight from mills against diesel, wages, tyres and repairs; the annual token tax is claimed.

## Railway Staff and Teachers

Salary and withholding are copied from certificates.""")

body("blogs/ntn-registration-tando-allahyar.html", """## Weavers and Merchants of Nasarpur

Nasarpur, a short drive from Tando Allahyar, has woven khes, susi and lungi on handlooms for generations. Most weavers work for merchants who supply yarn and buy the finished cloth. When a merchant, or a young family member, starts selling Nasarpuri textiles online through a website, Instagram or a marketplace, the payment gateway and courier's cash-on-delivery account ask for registration details. A design store in Karachi or Lahore stocking the cloth will also want invoices from a registered supplier. Registering with FBR is the first step in all of these.

## Sugar Mill Haulers and Contractors

The district's mills sign up tractor-trolley owners and labour contractors each autumn and withhold income tax on their payments, at a lower rate for those who have filed.

## Banana and Mango Traders

Commission agents in Karachi's fruit market and in Punjab pay traders by bank after each sale and increasingly ask for an NTN.

## Commuters Working in Hyderabad

Salaried residents can register on IRIS and file their own returns.

## Applying

Registration is free and online; our [FBR registration guide](/blogs/fbr-registration-step-by-step) explains every step.""")

body("blogs/income-tax-filing-tando-allahyar.html", """## Growers of Cane, Bananas and Mangoes

Crops from family land, whether cane delivered to the mill, bananas sold standing to a contractor or mangoes sold by the crate, are agricultural income and outside federal tax. Larger holdings pay Sindh's agricultural income tax, which is noted in the federal return. Cane money still owed by the mill on 30 June is a receivable.

## Mill Haulers and Labour Contractors

The return lists each payment from the mill, the tax withheld and the costs: diesel, tyres, drivers' wages and depreciation of tractors and trolleys for haulers; wages paid to gangs for labour contractors.

## Nasarpur Textile Merchants

Sales to shops, design stores and online customers are shown against cloth bought from weavers, dyeing and finishing, packing, courier charges, returned parcels and advertising. Cloth in stock on 30 June is counted at cost.

## Fruit Contractors

Sales in Karachi and Punjab against the price paid for standing crops, cutting, packing and freight.

## Commuters to Hyderabad

Salary and withholding are copied from certificates.

## Shops in Tando Allahyar and Chamber

Sales, purchases from Hyderabad wholesalers and stock on 30 June.""")

body("blogs/ntn-registration-thatta.html", """## Working for the Wind Corridor

The wind farms between Jhimpir and Gharo are built by large engineering contractors and then operated for decades. Both stages need local partners: transport for turbine parts and workers, security, water tankers, catering, civil works for roads and foundations, and maintenance. Developers and their contractors add vendors only after seeing an FBR NTN, a bank account in the vendor's own name and Sindh Revenue Authority registration for services. Payments are then made by bank with income tax withheld, at a lower rate for vendors who have filed.

## Landowners Leasing Land to Developers

Landowners whose land is leased for turbines, substations or access roads receive lease rent, often with tax withheld. Registering and filing lets them claim the withholding and lowers the rate.

## Fish Traders at Keti Bandar

Processors and exporters in Karachi's fish harbour pay by bank and ask suppliers for registration.

## Suppliers to Dhabeji Factories

Factories in the Dhabeji area near Karachi buy from registered suppliers.

## Applying

Registration is free and online; our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows each step.""")

body("blogs/income-tax-filing-thatta.html", """## Contractors in the Wind Corridor

A contractor serving wind projects lists each invoice, the income tax withheld by the developer and the costs of crews, vehicles, fuel and equipment hire. Sindh sales tax on services charged to the developer is collected for the province. Equipment owned is depreciated.

## Landowners Receiving Lease Rent

Lease rent from wind projects is declared as income, with withholding claimed. Compensation for land acquired, if any, is documented separately.

## Boat Owners at Keti Bandar

A boat owner shows the value of catches sold against diesel, ice, nets, engine repairs and the crew's share. Boats and engines are depreciated. Losses from storms are written off with evidence.

## Fish Traders

Purchases at the harbour, ice, packing and freight to Karachi against sales to processors.

## Delta Farmers

Rice, bananas and other crops from family land are agricultural income.

## Employees

Teachers and officials copy salary and withholding from certificates.

## Wealth Statement

Land, boats, vehicles and balances, with the year's change explained.""")

body("blogs/ntn-registration-timergara.html", """## Cement and Steel Dealers in a Building Boom

Money from the Gulf keeps Lower Dir's builders busy, and Timergara's dealers supply cement, steel, timber and tiles to contractors across the district. Contractors working on government schools, roads and water schemes need invoices from registered suppliers to claim their costs, and many larger dealers are asked for an FBR NTN before receiving bank payments.

## Contractors for District Departments

Departments in Timergara give work only to contractors with an NTN, and withhold income tax on each bill at a rate that depends on filer status.

## Doctors Near the Teaching Hospital

Doctors opening clinics and laboratories register to deal with pharmaceutical companies and panel clients.

## Lawyers at the District Courts

Advocates whose clients include banks and companies register so that tax withheld from their fees can be claimed.

## Workers in Saudi Arabia and the UAE

Workers abroad can register with a NICOP and file online so that land and houses bought at home are transferred at the filer rate.

## Registering

Registration is free and online; see our [FBR registration guide](/blogs/fbr-registration-step-by-step).""")

body("blogs/income-tax-filing-timergara.html", """## Wholesalers Supplying the Valleys

A Timergara wholesaler's return shows sales to village shops across Lower and Upper Dir, purchases from Peshawar and Mardan suppliers, freight over the Malakand pass and the stock on 30 June. Much of the trade is on credit; what village shops owe at year end is listed as receivables.

## Building Material Dealers

Sales of cement, steel and timber to contractors and families building houses, against purchases and transport, with contractors' withholding claimed.

## Doctors at the Teaching Hospital

Salary from the hospital and fees from evening clinics are shown separately.

## Lawyers

Fees less chamber rent and clerks' pay, with tax withheld by institutional clients claimed.

## Contractors

Each department payment, the tax withheld and the costs of labour and materials.

## Families Living on Gulf Remittances

Remittances are receipts shown in the wealth statement of the person who receives them, together with the houses and land they pay for.

## Former PATA Concessions

Income that was exempt under a PATA concession in a given year is still declared, as exempt.""")

add("blogs/tax-consultant-tando-adam-city.html", "## Cotton Season Spending\n\nThe weeks after cotton payments reach growers are the busiest of the year for the bazaar; shops that stock up beforehand should record those purchases and the credit they extend.")
add("blogs/tax-consultant-tando-allahyar.html", "## Chamber and Rural Markets\n\nShops in Chamber and the smaller towns buy from Hyderabad and keep supplier bills and daily sales notes.")
add("blogs/tax-consultant-tank.html", "Their purchases should be documented.")
add("blogs/tax-consultant-taunsa-sharif.html", "## Vehova and the Hill Areas\n\nTraders in Vehova and the foothills of the Suleman range supply goods to the hill communities and keep credit records.")
add("blogs/tax-consultant-timergara.html", "## Doctors' Evening Clinics\n\nMany specialists at the teaching hospital run clinics in the bazaar in the evenings; that income is separate from salary.")

add("blogs/income-tax-filing-tando-adam.html", "## Shopkeepers in the Town\n\nTraders on the main bazaar show sales, purchases from Hyderabad wholesalers and stock, with credit given to growers until the cotton is paid for recorded as receivables on 30 June.")
add("blogs/tax-consultant-tando-adam-city.html", "Those records protect the shop if its turnover is questioned.")
add("blogs/tax-consultant-tando-allahyar.html", "## Families Commuting to Hyderabad\n\nMany households combine a salary earned in Hyderabad with farm income from family land; the salary is taxable, the farm income agricultural.")
add("blogs/ntn-registration-tando-allahyar.html", "## Shops and Clinics in the Town\n\nRetailers, pharmacies and clinics that accept card payments open business accounts after registering.\n\n## Students\n\nStudents from the district at universities in Hyderabad and Jamshoro who start freelancing register with their CNIC.")
add("blogs/income-tax-filing-tando-allahyar.html", "## Pensioners\n\nRetired teachers and officials declare their pension as exempt and list land and houses.\n\n## Property in Hyderabad\n\nA flat or plot bought in Hyderabad is shown at cost, with the advance tax paid at transfer.")
add("blogs/tax-consultant-taunsa-sharif.html", "Their customers often settle accounts after harvest or the sale of animals.")
add("blogs/ntn-registration-thatta.html", "## Makli Guides and Shops\n\nGuides and handicraft shops near the Makli necropolis that take bookings from tour companies register to receive payments by bank.")
add("blogs/income-tax-filing-thatta.html", "## Dhabeji Factory Workers\n\nWorkers in factories near Dhabeji copy their salary certificates; those who changed jobs combine both.\n\n## Makli Visitors' Trade\n\nShops and guides near Makli show sales and fees against purchases and stall costs.")
add("blogs/tax-consultant-timergara.html", "Their fee registers are the record.")
add("blogs/ntn-registration-timergara.html", "## Students\n\nStudents from Lower Dir at the University of Malakand who start freelancing register with their CNIC so that foreign payments reach their own accounts.")
add("blogs/income-tax-filing-timergara.html", "## Pensioners\n\nRetired teachers and soldiers declare their pension as exempt and list their land and houses.\n\n## Transporters\n\nCoach and truck owners on the Timergara-Peshawar route show fares and freight against diesel and repairs.")
add("blogs/tax-consultant-tando-adam-city.html", "## Rice and Wheat Commission\n\nAgents dealing in wheat after the rabi harvest follow the same pattern, earning commission rather than the crop's value.")
add("blogs/income-tax-filing-tando-allahyar.html", "Its later sale is reported with the gain.")
add("blogs/tax-consultant-taunsa-sharif.html", "## Property\n\nPlots in Taunsa and Dera Ghazi Khan cost less in advance tax for active filers.")
add("blogs/ntn-registration-thatta.html", "Registration costs nothing and takes place entirely online.")
add("blogs/income-tax-filing-thatta.html", "## Pensioners\n\nRetired teachers and officials living in Thatta and Sujawal declare their pension as exempt and list the land they own in the delta, which keeps the wealth statement complete.")
add("blogs/tax-consultant-timergara.html", "## Transport over the Malakand Pass\n\nCoach companies running to Peshawar keep fare records.")
add("blogs/ntn-registration-timergara.html", "## Shops in the Bazaar\n\nRetailers wanting card machines open business accounts after registering.")
add("blogs/income-tax-filing-timergara.html", "## Property Bought in Peshawar\n\nA flat or plot bought in Peshawar with Gulf savings is listed at cost.")
add("blogs/income-tax-filing-tando-allahyar.html", "Keep the sale deed.")
add("blogs/ntn-registration-thatta.html", "After that, file every year.")
add("blogs/income-tax-filing-thatta.html", "Their bank profit is declared too.")
add("blogs/tax-consultant-timergara.html", "Fuel bills support their costs.")
add("blogs/ntn-registration-timergara.html", "## Teachers and Officials\n\nSalaried residents can register on IRIS and file their own returns to claim back excess withholding.")
add("blogs/income-tax-filing-timergara.html", "## Shops Rented Out in the Bazaar\n\nOwners renting shops in Timergara's bazaar declare rent as property income.")
add("blogs/income-tax-filing-thatta.html", "Coastal storm damage is recorded with photographs.")
add("blogs/income-tax-filing-timergara.html", "Bank tenants withhold tax on that rent.")
