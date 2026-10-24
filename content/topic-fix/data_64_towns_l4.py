"""Rewrites and local additions for towns L pages."""

PAGES = {}


def add(rel, text, key="body_more"):
    PAGES.setdefault(rel, {}).setdefault(key, "")
    PAGES[rel][key] += "\n\n" + text


def body(rel, text):
    PAGES.setdefault(rel, {})["body"] = text


PAGES["blogs/ntn-registration-pakistanis-dubai.html"] = {
    "regex": [(r'href="/income-tax-filing\.html"', 'href="/blogs/best-tax-consultant-overseas-pakistanis-dubai"')]}

body("blogs/tax-consultant-noorpur-thal.html", """## Life in the Heart of the Thal

Noorpur Thal is the most desert-like tehsil of Khushab district, a landscape of shifting dunes broken by patches of cultivation wherever the Thal canal's branches or tubewells bring water. Families here have lived for generations on a mix of rain-fed gram, a few acres of irrigated wheat, herds of goats, sheep and camels, and the salaries of sons serving in the army. Tax questions follow that mix.

## Crops and Herds

Gram sown after the monsoon and harvested in March, wheat on canal land and fodder for animals are all agricultural income from family land and fall outside federal income tax. Herds bred and raised on the family's own land are also part of farming. The picture changes for a family member who buys young camels or goats from neighbouring villages, fattens them and takes them to the cattle markets of Sargodha, Faisalabad or Lahore before Eid. That is trading, and the profit after purchase price, fodder and transport is business income.

## Army Salaries and Pensions

A large share of households include a serving or retired soldier. Serving personnel have tax withheld through their pay office. Pensions are generally exempt, but they are declared so that a house or tubewell bought with commutation money can be explained.

## Tubewells and Solar Pumps

Solar tubewells financed by banks are listed as assets with the loan as a liability. Water sold to neighbours by the hour is income from the pump.

## Shops and Transport

Shopkeepers in Noorpur town keep supplier bills from Khushab and Joharabad. Truck and pick-up owners carrying gram and animals keep freight records.""")

body("blogs/ntn-registration-nowshera.html", """## Becoming a Vendor in the Nowshera Industrial Estate

Factories in the industrial estate along the GT Road buy packing cartons, chemicals, spare parts, canteen services and transport from local businesses. Their purchase departments maintain approved vendor lists, and the first documents they ask for are an FBR NTN and a bank account in the vendor's own name. Suppliers of goods are often asked for a sales tax registration number as well, and service providers for KPRA registration. A Pabbi carton maker or an Akora Khattak transporter who completes these registrations can be paid by bank transfer every month rather than chasing cash.

## Hauling for the Cement Plants

Trucks carry clinker, coal and bagged cement to and from the plants in the Cherat hills. The plants withhold income tax on every freight bill, and the rate is lower for transporters who have filed a return for the latest year.

## Sand and Gravel Suppliers

Contractors who extract river sand and gravel under leases and sell to builders in Peshawar and to government projects are asked for registration by larger buyers who need proper invoices.

## Retirees from the Cantonment and Risalpur

Retired soldiers and airmen who invest their commutation in a pick-up, a shop or a share in a transport business should register when the business begins, so that its income is on record from the first year.

## Workers Abroad

Workers in the Gulf can register with a NICOP and file online.

## Getting Registered

Registration is free and online; our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows each step.""")

body("blogs/income-tax-filing-nowshera.html", """## Pay Certificates from the Cantonment and Risalpur

Soldiers, airmen and civilian staff receive an annual pay certificate showing basic pay, allowances and the tax withheld. Some allowances are exempt and others taxable, and the certificate separates them. Officers who move between stations during the year may have two certificates, which are combined. A return lets them claim back any tax withheld in excess, for example after arrears are paid.

## Retired Personnel

Pensions are declared as exempt. A retiree who also runs a shop in Nowshera Kalan, rents out a house in the cantonment area or owns a share in a truck declares that income in full.

## Industrial Estate Units

A factory's return shows sales, raw materials, power, wages, repairs and depreciation of machinery, with stock counted on 30 June. The figures are reconciled with the monthly sales tax returns and withholding statements before filing.

## Transporters and Contractors

Freight and contract receipts from the cement plants and factories, the tax withheld and the costs of fuel, wages and vehicle maintenance are listed. KPRA tax collected from customers is paid over and is not income.

## Sand and Gravel Lease Holders

Sales to builders less royalty, excavator hire and transport give the profit.

## Families Hit by Floods

Business stock or equipment lost to the Kabul river's floods is written off in the year of loss with evidence; houses lost are removed from the wealth statement with a note.""")

body("blogs/tax-consultant-nushki.html", """## A Desert District on the Road to Iran

Nushki lies about two hours west of Quetta, where the highway to Taftan and the Iranian border leaves the hills and enters the desert of the Chagai region. The town's economy depends on three things: the traffic and trade along that highway, farms watered by tubewells in the surrounding plain, and herds of sheep, goats and camels that graze the desert.

## Highway Businesses

Fuel stations, tyre shops, restaurants and small hotels along the highway serve trucks and buses travelling to and from Taftan and pilgrims heading to Iran. Most of this income is in cash. A daily sales note, supplier bills from Quetta and regular bank deposits give a profit figure that can be defended. Restaurant and hotel services are taxed by the Balochistan Revenue Authority.

## Goods from Across the Border

Goods arriving from Iran should be brought through customs channels, so that the importer has a record of duties and advance taxes paid, which may be credited against income tax.

## Wheat, Melons and Tubewells

Melons, wheat and vegetables grown with tubewell water on family land are agricultural income. A farmer who sells water to neighbours by the hour earns separate income from the pump.

## Herders and Livestock Traders

Animals raised on family land are part of farming. Traders who buy animals in Nushki's markets and sell them in Quetta or Karachi earn business income.

## Government Employees

Teachers, levies personnel and officials have tax withheld from salary.""")

body("blogs/income-tax-filing-pakpattan.html", """## A Year That Peaks at the Urs

For a shop near Baba Farid's shrine, the days of the annual urs can bring as much trade as several ordinary months. Langar suppliers, sellers of chadars and religious items, sweet shops, transporters and lodging houses all see this surge. The return still covers the full tax year from July to June: the urs takings are included alongside the rest of the year's sales, and the costs are the stock bought, extra staff hired for the urs, rent and electricity. A notebook of daily takings during the urs, and bank deposits made afterwards, are the best evidence of what was earned.

## Families Renting Rooms to Visitors

Households that rent rooms to visiting families during the urs earn rent that is income, even though it comes only once a year.

## Farmers Along the Old Sutlej Bed

Cotton, wheat, maize and fodder from family land are declared as agricultural income.

## Milk Collection and Dairies

Small farmers selling milk from their own animals earn agricultural income. Collection centre operators and commercial dairies show milk sales against purchases, feed, labour and chilling costs, and claim the processor's withholding.

## Commission Agents

Commission less costs, with loans to growers as receivables.

## Teachers and Officials

Salary and withholding are copied from certificates.""")

body("blogs/ntn-registration-pasrur.html", """## Finishing Work for Sialkot's Exporters

Many of the footballs, gloves and surgical instruments shipped from Sialkot pass through workshops in Pasrur for stitching, grinding, polishing or packing. Exporters now audit their supply chains, both for international buyers and for their own tax records, and they ask each workshop for an FBR NTN and a bank account in its own name before placing orders. Once registered, a workshop can be paid by bank transfer, and the exporter can document the payment and any tax it withholds.

## Rice Mills Selling Basmati

Exporters in Lahore and Sialkot buying basmati from Pasrur's mills need registered suppliers who can issue invoices, and mills need an NTN before applying for sales tax registration.

## Families with Members in Europe

Pasrur's relatives in Spain, Italy and France can register with a NICOP and file online so that plots bought at home are transferred at the lower advance tax rate.

## Border Area Contractors

Departments building roads and drains in the border villages require registered contractors.

## Shops and Clinics in the Town

Shops, pharmacies and clinics that accept card payments need business accounts.

## Getting Registered

Registration is free and online; see our [FBR registration guide](/blogs/fbr-registration-step-by-step).""")

body("blogs/tax-consultant-phalia.html", """## A Tehsil Built by Remittances from Southern Europe

Drive through the villages around Phalia and the newer houses tell the story: two and three storeys, often unoccupied for much of the year, built with money from relatives working in Barcelona, Athens, Milan and Paris. Phalia, in Mandi Bahauddin district, has one of the highest rates of migration to southern Europe in Punjab. Its tax questions revolve around that fact.

## Whose House Is It?

The most frequent issue is ownership. A house may be registered in a father's name, paid for by a son in Spain and lived in by another son. FBR's wealth statement asks each filer to list what he or she owns and how it was paid for. The cleanest arrangement is for the registered owner to file, showing the transfers from abroad as receipts. If the son abroad owns the property, it belongs in his own Pakistani return.

## Buying and Selling

The buyer's advance tax at transfer under section 236K, and the seller's under section 236C, are lower for active filers. Gains depend on when the property was acquired.

## Farming Families

Wheat, rice, sugarcane and fodder from family land are agricultural income. Land leased out for cash rent is also agricultural income for the owner.

## Shops and Services

Phalia's shops, pharmacies and clinics keep supplier bills and daily sales.

## Weddings

Gold given at weddings by relatives abroad belongs in the recipient's wealth statement.""")

body("blogs/ntn-registration-phalia.html", """## Registering a Relative Who Lives in Spain or Greece

When a Phalia family plans to buy a plot or a house in a son's name while he works in Spain or Greece, the son should be an FBR filer before the transfer. He can register on IRIS from abroad with his NICOP or CNIC, using an email address and a Pakistani mobile number registered in his name, which many overseas workers keep active for exactly this reason. After registering, he files a return for the latest tax year; only then does he appear on the Active Taxpayers List.

## Owners Renting Out Empty Houses

Many houses built with money from abroad are rented out. Owners register so that rent can be declared and tenants that are companies can withhold tax properly.

## Sugar Cane and Grain Sellers

Larger growers and traders selling to mills in the district are paid by bank and asked for registration details.

## Shopkeepers Accepting Card Payments

Retailers who want card machines or wallet merchant accounts need business accounts, opened after registration.

## Students Applying for Visas

Young people applying to study in Europe often need a filed return as evidence of their family's income.

## Registering

Registration is free and online; our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows the steps.""")

body("blogs/income-tax-filing-phalia.html", """## Families Living on Money from Europe

In many Phalia households, the money that builds the house and pays for weddings comes from a son or brother in Spain, Greece or Italy. Those transfers, when received through banks, are not income. The return of the family member at home shows them as receipts in the wealth statement, alongside the house, land, gold and vehicles they paid for. When the money arrives, the purpose of each transfer should be noted, because a few years later nobody remembers which transfer paid for what.

## A Son Abroad Who Owns Property Here

If the son abroad owns a plot or house in his own name, it belongs in his own Pakistani return, not his father's. Non-residents are taxed in Pakistan only on Pakistani-source income, so his return may show only rent from that property, if any.

## Farm Income

Wheat, rice, cane and fodder from family land are declared as agricultural income.

## Rent from Houses

Rent received from tenants is property income, with any withholding claimed.

## Property Sales

A sale is reported with price, cost, gain and the advance tax paid at transfer.

## Shops and Salaries

Shopkeepers show sales, purchases and stock; employees copy their salary certificates.""")

body("blogs/tax-consultant-pindigheb.html", """## Oil Country in the Potohar

Pindigheb tehsil in Attock district sits over some of the Potohar plateau's oil and gas fields. Exploration and production companies have drilled wells across its hills and ravines, and their operations have changed the local economy. Transport companies, security firms, caterers and labour contractors from Pindigheb now work for the fields. Every payment they receive from an oil company has income tax withheld at a rate that depends on whether they are on the Active Taxpayers List. Contractors who file regularly are withheld less and can set the deductions against their actual tax.

## Landowners and Well Sites

Companies pay landowners rent for well sites, access roads and pipelines, and sometimes compensation for crops damaged during drilling. Rent for land is income for the owner, declared with any withholding claimed. Compensation for compulsory acquisition is treated differently from a sale, and each payment should be documented.

## Barani Farms

Wheat, groundnut and gram grown on rain-fed land are agricultural income.

## Soldiers and Gulf Workers

Pindigheb has long sent its men to the army and, more recently, to the Gulf. Pensions are generally exempt but declared; remittances are receipts in the wealth statement.

## Traders and Transporters

Shops keep supplier bills from Attock and Rawalpindi; truck owners keep freight records.""")

body("blogs/tax-consultant-piplan.html", """## Between the Thal and the Indus

Piplan, in Mianwali district, sits where the irrigated land along the Thal canal gives way to the desert, a short distance from the Chashma barrage and the power installations at Kundian and Chashma. Its residents earn from farming, from salaries at those installations and in the army, and from the trade of a small market town.

## Salaried Staff at Chashma and Kundian

Engineers, technicians and support staff working at the barrage and the nearby power facilities receive salary certificates that show basic pay, allowances, the taxable value of any company housing or transport, and the tax withheld. Staff who join or transfer mid-year combine certificates, and a return lets them claim back excess withholding.

## Contractors for the Installations

Firms providing transport, maintenance, catering and security to these installations have tax withheld from every bill and claim it in their returns.

## Canal-Irrigated Farms

Wheat, sugarcane and gram from family land are agricultural income. Cane sold to the mills in the district is part of farming; hauling cane for others is business.

## The Market Town

Piplan's shops keep supplier bills from Mianwali and Bhakkar wholesalers and daily sales notes.

## Army Families

Many households have serving or retired soldiers; pensions are generally exempt but declared.""")

body("blogs/ntn-registration-pishin.html", """## Apple and Grape Growers in the Pishin Valley

Pishin's orchards, watered by karez and tubewells, grow apples, grapes, apricots and pomegranates for markets in Quetta, Karachi and Punjab. Growers who used to sell the whole crop on the tree to a contractor are increasingly sending fruit themselves to commission agents in Karachi's fruit market, who pay by bank transfer after the sale and ask for the grower's NTN. The fruit income stays agricultural; registration lets the payment reach the grower's own account.

## Contractors Who Buy Orchards

Contractors buying orchards in spring and selling the crop are traders; they need an NTN for invoices and bank accounts.

## Transporters on the Chaman and Karachi Routes

Truck owners register to work for companies that require registered carriers and to adjust the advance tax paid with their vehicle tokens.

## Contractors for Roads and Water Schemes

Departments in the district require registered contractors and check filer status before deciding withholding.

## Families Buying in Quetta

Filer status lowers advance tax on plots and houses in Quetta.

## Getting Registered

Registration is free and online with a CNIC and a mobile number in your name. Our [FBR registration guide](/blogs/fbr-registration-step-by-step) explains each screen.""")

add("blogs/ntn-registration-nawabshah.html", "## Doctors and Clinics\n\nDoctors opening clinics in Nawabshah register to deal with pharmaceutical suppliers and panel clients who pay by bank.\n\n## Students at the University\n\nEngineering students who start freelancing register with their CNIC.")
add("blogs/tax-consultant-okara.html", "## Renala and Depalpur Links\n\nOkara's traders supply shops in Renala Khurd and Depalpur on credit; amounts owed on 30 June are receivables.")
add("blogs/tax-consultant-pakpattan.html", "## Families Renting Rooms\n\nHouseholds near the shrine who rent rooms during the urs earn rent that is income, even if only for a few weeks.\n\n## Transport During the Urs\n\nCoach and van operators bringing visitors from Lahore, Multan and Sahiwal keep trip records.")
add("blogs/tax-consultant-panjgur.html", "## Karez and Date Groves\n\nThe karez channels that water Panjgur's groves are shared among families; water shares are part of farming and not separately taxed.\n\n## Date Processors\n\nUnits that dry, pit and pack dates for supermarkets in Karachi earn business income and need records of purchases and sales.")
add("blogs/tax-consultant-pasrur.html", "## Teachers and Doctors\n\nSalaried professionals who tutor or practise privately declare that income separately.\n\n## Border Villages\n\nFarmers in the villages near the border keep their land records up to date.")
add("blogs/tax-consultant-pattoki.html", "## Seed and Sapling Sales to Departments\n\nForest and agriculture departments buying saplings in bulk pay by bank and withhold tax, which nurseries claim.")

add("blogs/tax-consultant-okara.html", "## Military Farms and Tenants\n\nFamilies farming land around Okara's military farms declare crop income as agricultural and keep their lease or tenancy documents.")
add("blogs/tax-consultant-pakpattan.html", "Their fares and fuel costs are recorded per trip.")
add("blogs/income-tax-filing-pakpattan.html", "## Late Filing\n\nA late return is accepted; rejoining the Active Taxpayers List needs the surcharge.\n\n## Bank Profit\n\nProfit on savings is declared with the bank's withholding.")
add("blogs/tax-consultant-panjgur.html", "Their stock on 30 June is counted at cost.")
add("blogs/tax-consultant-pasrur.html", "## Transporters\n\nTruck owners carrying paddy to mills and finished goods to Sialkot keep freight records and claim the token tax.\n\n## Overseas Workers Returning\n\nWorkers who return from the Gulf and start a business should file from the first year so that their capital's source is on record.")
add("blogs/tax-consultant-pattoki.html", "## Property on the Highway\n\nLand along the Lahore-Multan road has gained value; when it is sold, its acquisition date decides how the gain is taxed.")
add("blogs/ntn-registration-phalia.html", "A filed return also supports a student visa application's financial evidence.")
add("blogs/income-tax-filing-phalia.html", "## Late Filing\n\nA late return is accepted with the surcharge to rejoin the Active Taxpayers List.\n\n## Pensioners\n\nRetired soldiers and teachers declare their pension as exempt.")
add("blogs/tax-consultant-pindigheb.html", "Truck owners claim the token tax.")
add("blogs/tax-consultant-piplan.html", "Their land is listed in the wealth statement.")
add("blogs/ntn-registration-pishin.html", "## Students\n\nStudents from Pishin at Quetta's universities who start earning register with their CNIC.")
add("blogs/tax-consultant-panjgur.html", "## Families in the Gulf\n\nMany Panjgur households have members in Oman and the UAE; transfers received through banks are receipts in the wealth statement.")
add("blogs/tax-consultant-pattoki.html", "Sellers should keep the mutation and sale deed.")
add("blogs/income-tax-filing-phalia.html", "Their wealth statement lists the house and land they own.")
add("blogs/tax-consultant-pindigheb.html", "Contracts should be kept.")
add("blogs/ntn-registration-pishin.html", "A filed return also helps when applying for jobs.")
add("blogs/tax-consultant-pattoki.html", "Nurseries should also keep their own land records.")
add("blogs/income-tax-filing-phalia.html", "Each transfer note should say who sent it.")
add("blogs/ntn-registration-pishin.html", "There is no fee for any of this.")
