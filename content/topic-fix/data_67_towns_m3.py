"""Rewrites and local additions for towns M pages."""

PAGES = {}


def add(rel, text, key="body_more"):
    PAGES.setdefault(rel, {}).setdefault(key, "")
    PAGES[rel][key] += "\n\n" + text


def body(rel, text):
    PAGES.setdefault(rel, {})["body"] = text


body("blogs/income-tax-filing-rahim-yar-khan.html", """## Sugar Mill Haulers and Contractors

Rahim Yar Khan's mills run some of the longest crushing seasons in Punjab. A hauler's return is built from the mill's weighbridge slips and payment advices: freight earned, income tax withheld and the costs of diesel, drivers, tyres and repairs. Tractors and trolleys are depreciated. Labour contractors show what the mill paid them against wages paid to their gangs.

## Engineers and Staff at the Mills

Mill employees copy salary, perquisites and withholding from their certificates. Seasonal staff who earn below the threshold owe no tax but can still file for filer status.

## Ginners

Lint and seed sales against seed cotton, electricity, labour and depreciation, reconciled with monthly sales tax returns.

## Doctors at the Teaching Hospital

Hospital salary from the certificate and private clinic income from fee registers, shown separately.

## University Teachers

Salary plus consultancy and examining fees.

## Larger Landowners

Cane, cotton and wheat are declared as agricultural income, with the Punjab agricultural income tax paid noted.

## Wholesalers in the City

Sales, purchases, stock and receivables from shops in Khanpur, Liaquatpur and Sadiqabad.""")

body("blogs/ntn-registration-rahim-yar-khan.html", """## Registering Before the Crushing Season

Each October, the cane departments of Rahim Yar Khan's mills sign up hundreds of tractor-trolley owners, truck operators and labour contractors. They ask for an FBR NTN and a bank account in the contractor's own name, and the accounts department withholds income tax on every payment. The rate is lower for contractors who have filed a return for the latest year, so registering and filing in September pays off across the whole season.

## Vendors to Mills and Industrial Units

Suppliers of parts, chemicals, bags and services to the mills and other industrial units in the district need an NTN, and for goods often a sales tax registration.

## Ginners

Spinning mills buy only from ginners with an NTN and a sales tax registration number; the sales tax application involves biometric verification and a factory visit.

## Doctors and Laboratories

Doctors opening clinics on Hospital Road and laboratories in the city register to deal with pharmaceutical companies and panel clients who pay by bank.

## Plots in the City's Schemes

Buyers in the new housing schemes pay lower advance tax as active filers.

## Registering

Registration is free and online; our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows each step.""")

body("blogs/ntn-registration-rawalakot.html", """## Poonch Families Buying in the Twin Cities

Families from Rawalakot, Hajira and Abbaspur regularly buy plots in Rawalpindi's housing schemes and flats in Islamabad, often with savings from army service or work in the Gulf. The buyer's advance tax at transfer under section 236K is much lower for an FBR active filer. Being a filer requires an FBR NTN and a return filed for the latest tax year, so the time to register is before the sale agreement, not on the day of transfer.

## Young Graduates Taking Jobs Down-Country

Graduates of the University of Poonch who join banks, hospitals and telecom companies in Rawalpindi need their NTN for payroll; registering on IRIS also lets them file and claim refunds.

## Retired Soldiers with Rented Property

Retirees who have bought shops in Rawalpindi to rent out register to declare the rent and claim any withholding by company tenants.

## Workers in the Gulf

Rawalakot's workers in Saudi Arabia and the UAE can register with a NICOP and file online.

## Poonch Income Stays with AJK

Income arising in Poonch itself is registered and reported with AJK's authorities, separately.

## Applying

Registration is free; a Rawalakot address is accepted. See our [FBR registration guide](/blogs/fbr-registration-step-by-step).""")

body("blogs/income-tax-filing-rawalakot.html", """## A Retired Soldier's FBR Return

A common Rawalakot return belongs to a retired soldier who draws a pension, has bought a shop in Rawalpindi's Saddar or a flat in a housing scheme, and rents it out. The pension is declared as exempt. The rent is income from Pakistan proper and is taxable, with allowable deductions under the law for the year and any tax withheld by a company or bank tenant claimed. The shop or flat, and his house and land in Poonch, all appear in the wealth statement.

## Serving Personnel

Pay certificates from the army or air force show salary and withholding; officers posted in Pakistan proper file with FBR in the usual way.

## Graduates Employed in the Twin Cities

Salary and withholding from the employer's certificate.

## Money from the Gulf and Britain

Transfers from relatives abroad are receipts in the wealth statement.

## Selling Property in Pakistan Proper

Price, cost, gain and the seller's advance tax under section 236C are reported.

## Consistency with AJK

What is reported to AJK's office about Poonch income and to FBR about the same assets should match.""")

body("blogs/income-tax-filing-renala-khurd.html", """## Orchard Owners and Contract Sales

Many of Renala Khurd's citrus and mango orchards are sold each year to contractors before the fruit ripens. For the owner, the contract money is agricultural income, just as if he had sold the fruit himself. Owners who sell directly to juice processors receive payment by bank and declare it the same way.

## Orchard Contractors

A contractor's return shows sales to processors, to Lahore's fruit market and to exporters, against the contract price, picking labour, crates, grading and freight. Processors withhold tax on payments, which the contractor claims. A frost or storm that ruins a crop can turn the season into a loss, shown and generally carried forward.

## Dairies

Commercial dairies show milk sales to processors against feed, labour and veterinary costs; the herd is a business asset.

## Potato and Maize Traders

Purchases at harvest, cold storage rent, freight and sales, with stock on 30 June counted at cost.

## Employees

Salary and withholding are copied from certificates.

## Late Filing

A late return is accepted with the surcharge to rejoin the Active Taxpayers List.""")
PAGES["blogs/income-tax-filing-renala-khurd.html"]["desc"] = "Income tax return filing in Renala Khurd for orchard owners, fruit contractors, dairies, potato and maize traders and employees."

add("blogs/tax-consultant-qila-saifullah.html", "Records of royalty receipts should be kept.")
add("blogs/ntn-registration-rajanpur.html", "## Overseas Workers\n\nWorkers from Rajanpur's villages in the Gulf can register with a NICOP and file online.\n\n## Teachers and Officials\n\nSalaried residents can register on IRIS and file to claim refunds.")
add("blogs/tax-consultant-rawalakot.html", "They keep simple daily records.")
add("blogs/ntn-registration-renala-khurd.html", "## Workers Abroad\n\nYoung men from Renala's villages in the Gulf can register with a NICOP and file online so that land at home is bought at the filer rate.\n\n## Teachers and Officials\n\nSalaried residents can register on IRIS and file their own returns.")
add("blogs/tax-consultant-rohri.html", "## Sukkur Barrage and Irrigation\n\nContractors on barrage and canal maintenance work for irrigation authorities that withhold tax.\n\n## Overseas Workers\n\nRemittances from the Gulf are receipts in the wealth statement.")
add("blogs/tax-consultant-sadiqabad.html", "## Turnaround Contracts\n\nWhen the fertiliser plant shuts down for annual maintenance, local contractors supply crews and equipment. These short, intense contracts carry withholding and should be recorded in full.\n\n## Machhi Goth and Rural Markets\n\nShops in the smaller towns keep supplier bills and daily sales.")
add("blogs/tax-consultant-sahiwal.html", "## Chichawatni and Arifwala Links\n\nThe division's other towns share Sahiwal's mix of dairy, cotton and grain trade.")

add("blogs/ntn-registration-rahim-yar-khan.html", "## Students at the Engineering University\n\nStudents who begin freelancing in software and design register with their CNIC so that foreign payments reach their own accounts and a tax record begins early.")
add("blogs/income-tax-filing-rahim-yar-khan.html", "## Families with Members in the Gulf\n\nRemittances received through banks are receipts shown in the wealth statement of the person who receives them.\n\n## Late Filing\n\nA late return is accepted with the surcharge to rejoin the Active Taxpayers List.")
add("blogs/ntn-registration-rajanpur.html", "Registration costs nothing.")
add("blogs/ntn-registration-rawalakot.html", "## Contractors\n\nBuilders from Poonch who take subcontracts on projects in Pakistan proper need an FBR NTN to be paid without the higher withholding rate.")
add("blogs/income-tax-filing-rawalakot.html", "## Bank Profit in Pakistan Proper\n\nProfit on savings held in bank branches in Pakistan proper is declared with the bank's withholding.\n\n## Late Filing\n\nA late FBR return is still accepted, with the surcharge to appear on the Active Taxpayers List.")
add("blogs/ntn-registration-renala-khurd.html", "There is no fee.")
add("blogs/income-tax-filing-renala-khurd.html", "## Rent from Highway Shops\n\nOwners of shops on the N-5 declare rent as property income.\n\n## Pensioners\n\nRetired staff declare their pension as exempt and list their land.")
add("blogs/tax-consultant-rohri.html", "Their wealth statements list the houses and land they buy.")
add("blogs/income-tax-filing-sadiqabad.html", "## Pensioners\n\nRetired plant staff declare pensions as exempt.")
add("blogs/ntn-registration-sahiwal.html", "Registration is free.")
add("blogs/income-tax-filing-sahiwal.html", "## Traders and Shops\n\nShopkeepers show sales, purchases from Lahore and Multan wholesalers and stock on 30 June.\n\n## Late Filing\n\nLate returns are accepted with the surcharge.")
add("blogs/ntn-registration-rajanpur.html", "## Fazilpur and the Hill Torrent Areas\n\nFarmers and traders in Fazilpur and the hill-torrent belt who sell to buyers in Dera Ghazi Khan increasingly receive bank payments.")
add("blogs/ntn-registration-renala-khurd.html", "## Shops in the Town\n\nRetailers who want card machines need a business account.")
add("blogs/income-tax-filing-renala-khurd.html", "## Bank Profit\n\nProfit on savings is declared with the bank's withholding, which is claimed or treated as final according to the rules for the year.\n\n## Transporters\n\nTruck owners carrying fruit and potatoes show freight against fuel, repairs and wages.")
add("blogs/tax-consultant-rohri.html", "## Lime Kilns\n\nKiln owners selling lime to builders keep fuel and sales records.")
add("blogs/income-tax-filing-sadiqabad.html", "Their wealth statement still lists their house and land.")
add("blogs/ntn-registration-sahiwal.html", "## Harappa Visitors\n\nGuides and shops serving visitors open accounts after registering.")
add("blogs/income-tax-filing-sahiwal.html", "## Bank Profit\n\nProfit on savings and certificates is declared with the bank's withholding.\n\n## Pensioners\n\nRetired civil servants declare pensions as exempt.")
add("blogs/income-tax-filing-sadiqabad.html", "## Bank Profit\n\nProfit on savings is declared with the bank's withholding.")
add("blogs/income-tax-filing-sahiwal.html", "## Transporters\n\nTruck owners carrying milk and grain show freight against diesel and repairs, claiming the token tax.")
