"""Rewrites and local additions for towns I pages."""

PAGES = {}


def add(rel, text, key="body_more"):
    PAGES.setdefault(rel, {}).setdefault(key, "")
    PAGES[rel][key] += "\n\n" + text


def body(rel, text):
    PAGES.setdefault(rel, {})["body"] = text


body("blogs/income-tax-filing-mailsi.html", """## Tubewell Water Sold to Neighbours

Around Mailsi, where canal water at the tail of the distributaries is unreliable, many farmers have tubewells, increasingly run on solar panels. A farmer irrigating his own fields is farming. One who sells water by the hour to neighbouring farmers is earning a separate income from the tubewell, and that hire income belongs in the return as business income, with diesel or electricity, repairs and depreciation of the pump and panels as its costs. Solar systems bought on bank financing appear in the wealth statement with the loan as a liability.

## Land Given on Theka

Families who lease out land for a fixed cash rent per acre for the season receive agricultural income, just as if they had farmed it. The lease deed or a written note of the rent received helps if the wealth statement is questioned.

## Ginning Factories on the Vehari Road

A Mailsi ginner's return is built from the gate register of seed cotton received, the lint and seed sales invoices, and the mills' withholding statements. Electricity, labour and freight are the main costs, and stock on 30 June is counted.

## Commission Agents

Commission on cotton and wheat, less shop costs, is income; loans to growers are receivables.

## Teachers and Officials

Salary and withholding are copied from certificates.

## Families with Members in the Gulf

Money received from abroad through banks is a receipt shown in the wealth statement.""")

body("blogs/income-tax-filing-liaquatpur.html", """## Cotton-Picking Labour Contractors

In the picking season, contractors in Liaquatpur's villages organise teams of pickers, mostly women, for landowners and ginners. The contractor's income is what the landowner pays for the picking less what the pickers receive. Keeping a register of each field picked, the weight brought in and payments made to the team is the only way to show that margin honestly.

## Cane Haulers for the Mills

Freight for carrying cane, shown on mill payment advices and weighbridge slips, less diesel, tyres, the driver's wages and depreciation of the tractor and trolley, gives the hauler's profit. The mill's withholding is claimed.

## Ginners

The ginner's return reconciles phutti bought, lint and seed sold and the mills' withholding with the monthly sales tax returns.

## Brick Kilns

Kilns around Liaquatpur and Trinda show brick sales against clay, fuel, labour and the kiln lease; advances to kiln workers are receivables.

## Farmers

Cotton, cane and wheat from family land are agricultural income.

## Returned Gulf Workers

A worker who comes home and buys a tractor-trolley or a shop with savings should file from that year, showing the money brought home through banks as a receipt.

## Pensioners and Employees

Pensions are declared as exempt; salaries with withholding are copied from certificates.""")

body("blogs/income-tax-filing-lodhran.html", """## Employees of the Sugar Mills

Lodhran's mills employ engineers, chemists, cane officers and clerks year-round, plus seasonal staff during crushing. Their salary certificates show withholding and any housing or transport benefits. Seasonal workers who earn below the threshold owe no tax, but those who want filer status can still file.

## Cane Growers Paid Late

Mills sometimes pay growers months after the cane is delivered. The cane income remains agricultural whenever it is received, but the amount owed by the mill on 30 June is shown as a receivable in the wealth statement.

## Mango Contractors in Kahror Pacca and Dunyapur

Contractors pay orchard owners in spring for the season's fruit and sell from June to August. The return shows sales to commission agents and exporters against the contract price, picking, crates, cold storage and freight. Storms at flowering can cause a loss, which is shown and generally carried forward.

## Orchard Owners

Money received from a contractor for an orchard's crop is agricultural income.

## Arhtis

Commission less costs, with advances to farmers as receivables.

## Shops in Lodhran City

Shopkeepers show sales, purchases from Multan and Bahawalpur wholesalers and stock, claiming advance tax on electricity bills.

## Wealth Statement

Land, orchards, vehicles, receivables from mills and balances.""")

body("blogs/ntn-registration-loralai.html", """## Orchard Owners Sending Fruit Down-Country

Loralai's apple and almond growers who send their own produce to commission agents in Lahore, Multan or Karachi are increasingly paid by bank transfer. The commission agent's accounts may ask for an NTN, and registering makes those payments straightforward even though the fruit income itself is agricultural.

## Almond and Dry Fruit Traders

Traders who buy almonds on the trees, shell, grade and sell them to dry fruit wholesalers in Punjab need an NTN for invoices and bank accounts.

## Coal Supplied to Brick Kilns

Lease holders sending coal to brick kilns in Punjab are asked by larger buyers for registration, and kilns that withhold tax do so at a lower rate for active filers.

## Contractors at the Cantonment

Suppliers of rations, maintenance and transport to Loralai cantonment are registered before they are paid.

## Truck Owners on the Fort Munro Route

Truck owners carrying fruit and coal through Fort Munro towards Dera Ghazi Khan register to work for companies and to adjust the advance tax paid with their annual vehicle tax.

## Registering

The IRIS process takes a CNIC, a phone number registered in your own name and your address. Our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows each step.""")

body("blogs/ntn-registration-lasbela.html", """## Working for the Duddar Mine

The company operating the zinc-lead mine at Duddar, and its main contractors, keep vendor lists. A local firm supplying drivers, water tankers, food or security must have an FBR NTN, a bank account in its own name and registration with the Balochistan Revenue Authority, because services in Balochistan carry provincial sales tax. Without these, payments are delayed or withheld at the higher non-filer rate.

## Shrimp and Fish Sellers at Sonmiani and Damb

Processors in Karachi's fish harbour who buy shrimp and fish from Lasbela's boats pay by bank and ask suppliers for registration details, particularly for export-quality catch.

## Farmers Near Bela with Side Businesses

A farmer who runs a tractor hire service or a seed shop alongside his land registers for the business, while crop income stays agricultural.

## Industrial Workers in Hub

Many Lasbela residents work in Hub's factories; they can register on IRIS and file their own returns to claim excess withholding.

## Graduates of the University in Uthal

Graduates joining companies or starting consultancy register with their CNIC.

## Applying

IRIS registration uses a CNIC, a phone in your name and an address; our [FBR registration guide](/blogs/fbr-registration-step-by-step) has the screens.""")

body("blogs/income-tax-filing-lasbela.html", """## Mine Contractors

A contractor working for the Duddar mine lists every invoice, the payments received and the income tax withheld by the mining company. Diesel, drivers' wages, vehicle maintenance, food for camp crews and depreciation of trucks and tankers are deducted. The Balochistan sales tax charged on services is collected for the province and paid over, so it is not part of income.

## Boat Owners and Fish Traders

A boat owner shows the value of catches sold against diesel, ice, nets, engine repairs and the crew's share, which is a business cost. Boats and engines are depreciated over their life.

## Farmers Around Bela and Uthal

Cotton, wheat, vegetables and fruit from family land are agricultural income. Land watered by hill torrents in good years and left dry in bad ones still belongs in the wealth statement.

## University and Government Staff

Salary and withholding are copied from certificates; consultancy and research fees are declared separately.

## Hub Factory Workers

Lasbela residents working in Hub copy their salary certificate and list their property at home.

## Traders in Uthal and Bela

Shopkeepers show sales, purchases from Karachi and Hub wholesalers and stock on 30 June.""")
PAGES["blogs/income-tax-filing-lasbela.html"]["desc"] = "Income tax return filing in Lasbela for mine contractors, boat owners, farmers, Hub factory workers, university staff and traders."
PAGES["blogs/ntn-registration-mailsi.html"] = {"desc": "NTN registration in Mailsi for ginners, arhtis, input dealers, tubewell owners, transporters and families buying property."}

add("blogs/ntn-registration-mailsi.html", """## Tubewell and Solar Pump Owners

Farmers who invest in solar tubewells through bank financing, and who sell water to neighbours, need an NTN for the bank's documents and to show the hire income properly.

## Shops in the Bazaar

Cloth, mobile and grocery shops that accept card and wallet payments need business accounts.

## Students and Young Workers

Young people from Mailsi studying in Multan or working abroad register with their CNIC or NICOP.""")
add("blogs/ntn-registration-lakki-marwat.html", "## Pezu and the Indus Highway\n\nRestaurant and fuel station owners at Pezu who deal with oil companies and suppliers that pay by bank need an NTN for those agreements.")
add("blogs/income-tax-filing-lakki-marwat.html", "## Teachers and Officials\n\nSalaried residents copy salary and withholding from their certificates. Teachers who also run a private academy in the evening declare its fees separately.")
add("blogs/ntn-registration-lalamusa.html", """## Shops and Clinics

Shops in the bazaar near the station and clinics serving the villages open business accounts after registration to accept card and wallet payments.

## Railway Contractors

Contractors on railway maintenance and station works are paid by bank and withheld at lower rates if they file.""")
add("blogs/income-tax-filing-lalamusa.html", """## Gifts and Weddings

Gold and cash given at weddings by relatives abroad belong in the recipient's wealth statement with a note of who gave them; gifts from close relatives are generally not income.

## Foreign Pensions

Returned migrants drawing pensions from Spain or Italy declare them under the rules on foreign income for the year.""")
add("blogs/tax-consultant-larkana.html", "## Lawyers and Courts\n\nAdvocates at the high court bench and district courts declare fees less chamber costs.")
add("blogs/ntn-registration-larkana.html", """## Guava Contractors

Contractors who buy guava orchards for the season and send fruit to Karachi's markets deal with commission agents who pay by bank.

## Private Schools and Academies

Schools and coaching centres register to open accounts in the institution's name and to deal with fee collection through banks.""")
add("blogs/income-tax-filing-larkana.html", """## Guava Contractors

Sales in Karachi's markets against the contract price paid to orchard owners, picking, crates and freight.

## Private Schools

Fee income less teachers' salaries, rent and utilities.

## Pensioners

Retired officials declare pensions as exempt and list their property.""")
add("blogs/tax-consultant-lasbela.html", "## Hingol and Coastal Tourism\n\nGuest houses and transport operators serving visitors to the Hingol national park and the coastal highway are small seasonal businesses; their services fall under BRA.")
add("blogs/tax-consultant-layyah.html", "## Chaubara and Karor Lal Esan\n\nThe district's other tehsils have their own gram markets and shops; traders there buy from Layyah and Bhakkar wholesalers and sell on credit until harvest.")
add("blogs/ntn-registration-layyah.html", """## Shops in Layyah City

Shops that accept wallet and card payments need business accounts.

## Gulf Workers

Workers from Layyah's villages abroad can register with a CNIC or NICOP and file online so that land bought at home attracts the filer rate.

## Teachers and Officials

Salaried residents can register on IRIS to file their own returns and claim refunds of excess withholding.""")
add("blogs/tax-consultant-layyah-city.html", "## Building Material Dealers\n\nCement, steel and brick dealers supplying the city's growing housing schemes record sales to contractors, who may withhold tax on purchases.\n\n## Mobile and Electronics Shops\n\nShops selling handsets and appliances keep dealer invoices and sales records.")
add("blogs/tax-consultant-liaquatpur.html", "## Cotton-Picking Contractors\n\nContractors who organise pickers for landowners and ginners earn the difference between what they are paid and what they pay the pickers; a register of fields and payments supports this.")
add("blogs/tax-consultant-lodhran.html", "## Dairy and Livestock\n\nCommercial dairies supplying milk collectors show milk sales against feed and labour.\n\n## Property\n\nFamilies buying plots in Lodhran, Multan or Bahawalpur pay lower advance tax as active filers.")
add("blogs/ntn-registration-lodhran.html", """## Dairies Supplying Processors

Commercial dairies selling milk to processors are paid by bank and asked for an NTN.

## Shops in the City

Shops accepting wallet payments need business accounts.

## Overseas Workers

Workers abroad can register with a CNIC or NICOP and file online.""")
add("blogs/tax-consultant-loralai.html", "## Families in Quetta\n\nMany Loralai families also live in Quetta, filing with their current address while listing orchards at home.")
add("blogs/income-tax-filing-loralai.html", """## Almond Traders

Traders who buy almonds on the trees, shell, grade and sell them to wholesalers in Punjab show sales against the orchard price, labour, shelling and freight, with unsold almonds on 30 June counted as stock.

## Cantonment Suppliers

Contractors list payments from the cantonment with tax withheld, deducting their costs.

## Teachers

Teachers in government and private schools copy salary and withholding from certificates.""")
add("blogs/tax-consultant-mailsi.html", """## Tubewells and Solar Pumps

Farmers who sell tubewell water to neighbours by the hour earn business income from the pump, separate from their crops.

## Land Leased on Theka

Cash rent from leasing out farmland is agricultural income for the owner.""")
add("blogs/tax-consultant-lower-dir.html", "## Teachers and Health Staff\n\nSalaried staff copy their certificates and list property.")
add("blogs/tax-consultant-malakand.html", "## Dargai\n\nDargai's traders and transporters, at the foot of the Malakand pass, keep records similar to Batkhela's.")

add("blogs/income-tax-filing-lakki-marwat.html", "## Shops in Lakki City and Naurang\n\nShopkeepers who buy from Bannu and D.I. Khan wholesalers show purchases, sales and stock on 30 June, and claim the advance tax on their commercial electricity bills.")
add("blogs/ntn-registration-lalamusa.html", "## Women Running Home Businesses\n\nWomen stitching clothes or selling food from home can register under their own CNIC and keep their earnings in their own accounts.")
add("blogs/income-tax-filing-lalamusa.html", "## Shopkeepers Near the Station\n\nShops around the railway station and main bazaar show sales, purchases and stock, claiming the advance tax on electricity bills.")
add("blogs/ntn-registration-larkana.html", "## Hotels Near Mohenjo-daro\n\nGuest houses taking bookings from tour groups and researchers visiting the ruins register to receive bank payments and deal with SRB for services.")
add("blogs/income-tax-filing-larkana.html", """## Lawyers

Advocates at the high court bench and district courts show professional fees against chamber rent and clerks' pay, claiming withholding by institutional clients.

## Transporters

Truck owners carrying rice to Karachi and Quetta show freight against diesel, repairs and wages, with the vehicle token tax claimed.

## Property in Karachi

Rent from a flat or shop in Karachi owned by a Larkana family is declared under property income, with any tenant withholding claimed.""")
add("blogs/ntn-registration-lasbela.html", "## Marble and Stone\n\nOwners of small marble and stone quarries selling to cutting units in Karachi and Hub register to issue invoices.")
add("blogs/income-tax-filing-lasbela.html", "## Rent from Property in Hub or Karachi\n\nFamilies who own rented property in Hub or Karachi declare that rent and claim tenant withholding.")
add("blogs/tax-consultant-layyah.html", "## Families Abroad\n\nRemittances from the Gulf are receipts in the wealth statement.")
add("blogs/ntn-registration-layyah.html", "## Doctors and Clinics\n\nDoctors opening clinics in Layyah city register to deal with suppliers and panel payments.")
add("blogs/tax-consultant-layyah-city.html", "## Rent from Shops\n\nShop owners in the main bazaar declare rent as property income.")
add("blogs/tax-consultant-liaquatpur.html", "## Property\n\nPlots in Liaquatpur and Rahim Yar Khan cost less in advance tax for active filers.")
add("blogs/income-tax-filing-liaquatpur.html", "## Late Filing\n\nA late return is accepted, with the surcharge needed to rejoin the Active Taxpayers List.")
add("blogs/tax-consultant-lodhran.html", "## Kahror Pacca and Dunyapur Shops\n\nShops in the district's smaller towns keep supplier bills from Multan and daily sales notes.")
add("blogs/ntn-registration-lodhran.html", "## Brick Kilns\n\nKiln owners supplying builders in Lodhran and Multan register because contractors prefer documented suppliers and may withhold tax on purchases.")
add("blogs/income-tax-filing-lodhran.html", "## Late Filing\n\nReturns filed after the deadline are accepted; the surcharge applies to rejoin the Active Taxpayers List.")
add("blogs/tax-consultant-loralai.html", "## Pomegranates and Apricots\n\nThe valley's pomegranate and apricot orchards are agricultural income for their owners.")
add("blogs/ntn-registration-loralai.html", "## Teachers and Officials\n\nSalaried residents can register on IRIS and file their own returns to claim back excess withholding.")
add("blogs/income-tax-filing-loralai.html", """## Selling Coal to Kilns

Sales of coal to kilns and industry are shown against royalty, miners' wages and advances, timber, explosives and haulage, with buyers' withholding claimed.

## Fruit from Family Orchards

Apples, almonds and pomegranates from family orchards are declared as agricultural income.

## Late Filing

A late return is accepted with the surcharge to rejoin the Active Taxpayers List.""")
add("blogs/tax-consultant-mailsi.html", "## Property\n\nPlots in Mailsi and Vehari cost less in advance tax for active filers.")
add("blogs/ntn-registration-mailsi.html", "## Seed and Fertiliser Dealers\n\nCompanies supply registered dealers and withhold tax at lower rates from filers.")

add("blogs/ntn-registration-lasbela.html", "Registering also lets them receive payment in their own account.")
add("blogs/income-tax-filing-lasbela.html", "## Late Filing\n\nA late return is still accepted, with a surcharge to rejoin the Active Taxpayers List.")
add("blogs/ntn-registration-layyah.html", "## Cotton Ginners in Karor and Chaubara\n\nGinners in the district's smaller towns need the same NTN and sales tax registration before spinning mills will buy their lint.\n\n## Overseas Pakistanis\n\nLayyah families' relatives in the Gulf can register with a NICOP.")
add("blogs/tax-consultant-layyah-city.html", "Tenants that are banks or companies withhold tax on rent.")
add("blogs/ntn-registration-lodhran.html", "## Students\n\nStudents who start freelancing register with their CNIC so that payments reach their own accounts.")
add("blogs/income-tax-filing-lodhran.html", "Late filers should also check notices on IRIS.")
add("blogs/tax-consultant-loralai.html", "Traders who buy them on the trees earn business income.")
add("blogs/ntn-registration-loralai.html", "Teachers who run private academies register those separately.")
add("blogs/income-tax-filing-loralai.html", "## Trucking on the Fort Munro Route\n\nTruck owners on the Fort Munro route show freight, fuel and repairs.")
add("blogs/tax-consultant-mailsi.html", "## Teachers and Officials\n\nSalaried residents copy their salary certificates and claim excess withholding.")
add("blogs/ntn-registration-mailsi.html", "## Cotton-Picking Contractors\n\nContractors arranging pickers for ginners and landowners are increasingly paid by bank and need an NTN for those payments.")

add("blogs/tax-consultant-mailsi.html", "Those who also teach privately declare academy fees separately.")
add("blogs/ntn-registration-mailsi.html", "## Shops Near the Siphon\n\nRestaurants and shops serving visitors to the Mailsi siphon open business accounts once registered.")
