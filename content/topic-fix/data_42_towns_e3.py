"""Rewrites and local additions for towns E pages below the floor."""

PAGES = {}


def more(rel, text):
    PAGES[rel] = {"body_more": text}


def body(rel, text):
    PAGES[rel] = {"body": text}


body("blogs/income-tax-filing-haveli-lakha.html", """## Potato Growers Who Also Store and Sell

Many Haveli Lakha growers harvest potatoes in January and February, keep them in a cold storage and sell months later when prices recover. The crop from their own land stays agricultural income even when sold after storage. But a grower who also buys potatoes from neighbours at harvest and stores them for resale is trading; that part is business income, and the purchase price, storage rent per bag and freight are its costs. Keeping separate bag counts for own and bought potatoes avoids confusion.

## Cold Storage Owners

A storage owner's return shows rent collected per bag over the season. Electricity is the largest cost, followed by staff, ammonia, repairs and depreciation of the building and plant. The advance tax charged on the industrial electricity bill is listed month by month and claimed.

## Maize Sold to Feed Mills

Feed mills and starch factories pay growers and traders by bank transfer, and their payment advice shows any tax withheld. A trader declares the margin; a grower selling his own crop declares it as agricultural.

## Rice Husking Units

Small husking units near Head Sulemanki show paddy bought, rice and bran sold, power and labour, and match these to any sales tax returns filed.

## Teachers and Officials

Salaried residents report salary from the certificate and claim any excess deduction.

## Wealth Statement

Land, storage buildings, tractors, gold and balances are listed. Bags held for others in a cold storage are not the owner's assets and should not appear.""")

body("blogs/income-tax-filing-haroonabad.html", """## Ginning Factories

A ginner's year runs from the first seed cotton in August to the last bales sold in spring. The return shows seed cotton bought from growers and arhtis, lint and cottonseed sold, electricity, labour, bale-pressing and transport, and depreciation of gins and presses. Spinning mills deduct tax on lint purchases; those deductions are listed by mill and claimed. The ginner's monthly sales tax returns should tell the same story as the income tax return.

## Bad Seasons

Whitefly, rain at picking time or a fall in lint prices can turn a season into a loss. A business loss is shown as such and can generally be carried forward against business profit of later years, provided the return for the loss year was filed.

## Arhtis in the Grain Market

Commission on wheat and cotton sold for farmers, less shop rent, munshi's salary and other costs, is the arhti's income. Money lent to growers before harvest is shown as a receivable.

## Seed and Fertiliser Dealers

Dealers show sales, purchases from companies and stock at 30 June. Company deductions on supplies are credited.

## Farm Families

Cotton and wheat from family land are declared as agricultural income.

## Salaried Residents

Teachers and bank staff report salary and the tax withheld.""")

body("blogs/income-tax-filing-hangu.html", """## Families Living on Gulf Remittances

In many Hangu households the main earner works in Saudi Arabia or the UAE, and the family at home has no taxable income of its own. Such families often file only when they want filer status for a property or vehicle purchase. The return then shows the remittances received through banks as receipts, and the wealth statement lists the house, land and gold they have paid for.

## Workers Who Have Returned

Men who come back from the Gulf and invest savings in a shop, a coaster or a plot should file from the first year, so that the source of the investment is on record. Money brought home through banks is shown as a receipt; the new business then produces taxable profit.

## Shops in Hangu and Thall

Shopkeepers show sales, purchases from Kohat and Peshawar wholesalers, rent and wages, adjusting for stock at the start and end of the year.

## Contractors to Exploration Companies

Transporters and security firms list each payment and the tax withheld by the company, and deduct fuel, wages and vehicle costs.

## Government Staff

Police, teachers and health workers report salary from their certificates and list their property.

## Land

Wheat and maize from family land are agricultural income and are declared as exempt.""")

body("blogs/income-tax-filing-haripur.html", """## Factory Employees at Hattar

Workers and managers at Hattar's factories receive salary certificates showing basic pay, allowances and tax withheld. Some allowances are taxable and some, such as certain medical benefits, are not. The return reproduces these figures and claims a refund if the employer withheld too much, for example after a mid-year salary change.

## WAPDA and Dam Staff

Employees at Tarbela and Khanpur often have free accommodation or utilities. How these perquisites are valued for tax is set by the rules, and the salary certificate should show them.

## Vendors and Contractors

Suppliers to Hattar factories show sales, purchases and expenses, and list deductions made by each customer. Contractors on project work show each contract's receipts and costs.

## Orchard Owners and Orchard Contractors

Owners who sell their own oranges and lychees declare agricultural income. A contractor who pays an owner for the season's crop and sells it in Islamabad shows the contract price, picking, packing and transport as costs against his sales.

## Plots in Islamabad Schemes

Instalments paid on plots are shown as assets at the amount paid to date.

## Pensioners

Retired employees declare their pension as exempt so that their wealth statement balances.""")

body("blogs/income-tax-filing-gwadar.html", """## Boat Owners and Fish Traders

A Gwadar boat owner's year is measured in trips. The return shows the value of each catch sold at the harbour or to processors, less diesel, ice, nets, engine repairs and the crew's share, which is a business cost for the owner. Boats and engines are depreciated. Fish traders who buy at the harbour and send consignments to Karachi show their purchases, ice, packing and freight.

## Seafood Exporters

Export proceeds received through banks have tax collected at source. Depending on the regime that applies, this may be the final tax on export income or a credit against normal tax.

## Port and Project Contractors

Subcontractors list each payment received from the main contractor, the tax withheld and their costs of labour, materials and equipment.

## Land and Plot Files

Plots bought in housing schemes, including files not yet converted to registered title, are shown at cost. Sales during the year are reported with the gain and the advance tax paid under section 236C.

## Concessions

Income covered by a valid Gwadar concession is declared as exempt with the reference to the approval.

## Salaried Employees

Port, municipal and project staff report salary and tax withheld.""")

body("blogs/ntn-registration-haveli-lakha.html", """## Selling Potatoes to Chip Makers

Snack manufacturers buy large quantities of processing potatoes from growers and traders in Okara district under contracts. Their procurement teams ask suppliers for an NTN and pay by bank transfer, withholding tax at a lower rate from active filers. A trader who registers before the season can sign contracts directly instead of selling through a middleman.

## Cold Storage Financing

Banks lend against cold storage buildings and stored produce, and an NTN is part of their documents. Storage owners also need it to deal with corporate customers who rent space.

## Maize for Feed Mills

Feed mills in Lahore and Okara pay maize suppliers through banks. Registration lets a supplier receive payments in his own account and claim the tax withheld.

## Rice Units

Husking units need an NTN before they can apply for sales tax registration.

## Shops near Head Sulemanki

Shops serving visitors and travellers that want wallet or card payments need a business account.

## Getting Registered

Registration is online on IRIS. Keep your CNIC, a SIM in your own name and the address from your electricity bill ready; our [FBR registration guide](/blogs/fbr-registration-step-by-step) walks through each screen.""")

body("blogs/tax-consultant-harnai.html", """## Coal from the Harnai and Sharig Fields

Harnai's coal comes from small underground mines worked under provincial leases. Much of it travels by truck to brick kilns in Punjab and Sindh. The lease holder's accounts should show tonnage raised and sold, royalty paid to the province, wages and advances to miners, timber for props, explosives and the cost of trucks. Kiln owners and industrial buyers often withhold tax on purchases, and those deductions become credits when the lease holder files.

## Labour Contractors and Mine Workers

Many mines are run through contractors who hire and pay the miners. The contractor's income is the difference between what the lease holder pays him and what he pays the workers, so his pay sheets matter.

## Orchards in the Valley

Harnai's apples, apricots and pomegranates are sold in Quetta and down-country. Orchard owners selling their own fruit earn agricultural income. Traders who buy orchards before harvest and transport the fruit earn business income.

## Transport on the Harnai Road

Truck owners carrying coal and fruit keep freight slips and fuel bills and claim the advance tax paid with their vehicle tax.

## Government Employees

Teachers, levies and health staff have tax withheld from salary.

## Services Tax

Services in Balochistan are taxed by the Balochistan Revenue Authority, not FBR.""")

more("blogs/income-tax-filing-ghotki.html", """## Plant Employees Who Move

Engineers transferred between plants, or who join mid-year, may have two salary certificates. Both are combined in the return so that the total salary and total tax withheld are correct.""")
more("blogs/ntn-registration-gilgit.html", """## Gemstone Dealers

Dealers in gemstones from the region who sell to buyers in Islamabad, Peshawar or abroad register to receive payments through banks and to document their stock.""")
more("blogs/ntn-registration-gojra.html", """## Hockey Academies

Coaching academies that charge monthly fees and receive sponsorship from companies need an NTN for sponsors' records.""")
more("blogs/income-tax-filing-gojra.html", """## Seed and Pesticide Dealers

Dealers show sales on credit to farmers as receivables until harvest, and claim the tax withheld by supplying companies.

## Transporters

Truck owners carrying grain show freight, fuel, repairs and depreciation, and claim the advance tax paid with their tokens.

## Families with Members in Faisalabad

Sons working in Faisalabad's mills file their own returns covering salary; money they send home is a receipt in the parents' wealth statement.""")
more("blogs/ntn-registration-gujrat.html", """## Ceramics and Pottery Units

Ceramic units supplying tableware to retailers and hotels deal with buyers who prefer registered suppliers. Registration also allows the unit to open accounts with gas and electricity suppliers in the business name.""")
more("blogs/income-tax-filing-gujrat.html", """## Fan Dealers and Distributors

Distributors who buy fans from Gujrat manufacturers and sell to retailers across Pakistan show purchases, sales, freight and warehouse costs, and their input tax records support the purchase side.

## Retired Overseas Workers

People who have returned from Europe with savings and pensions declare foreign pensions under the rules on foreign income, and list their property.""")
more("blogs/tax-consultant-gujrat-city-centre.html", """## Travel Agents

Agents booking tickets and visas for Gujrat's travellers to Europe and the Gulf earn commission and service charges; only these are income, not the ticket prices passed to airlines.""")
more("blogs/ntn-registration-gwadar.html", """## Fishing Boat Owners

Boat owners who sell to processors and exporters are asked for an NTN by buyers who pay through banks.

## Local Landowners Selling to Investors

Gwadar residents selling land to investors from other cities pay lower advance tax at transfer when they are active filers, so registering before the sale saves money.""")
PAGES["blogs/ntn-registration-gwadar.html"]["desc"] = "NTN registration in Gwadar for port contractors, seafood exporters, boat owners, hotels and property investors, with steps."
more("blogs/tax-consultant-hafizabad.html", """## Sukheke and Rural Markets

Smaller markets such as Sukheke serve surrounding villages with grain trading and shops whose records follow the same pattern as Hafizabad city's.""")
more("blogs/ntn-registration-hafizabad.html", """## Exporters' Quality Requirements

Exporters audit their suppliers for food safety and traceability. A registered mill with proper invoices and bank records passes these checks more easily.

## Shops and Clinics

Shops, pharmacies and clinics in Hafizabad city that accept digital payments open business accounts after registration.

## Overseas Workers

Workers abroad can register with their CNIC or NICOP and file online.""")
more("blogs/tax-consultant-hangu.html", """## Coal and Building Materials

Kohat region coal and local stone and sand are supplied to builders. Suppliers record sales and the tax withheld by contractors.""")
more("blogs/ntn-registration-hangu.html", """## Shops in Thall

Thall's bazaar serves the upper valleys and traders bringing goods from Kohat. Shopkeepers who want business accounts or card machines register first.

## Contractors for Schools and Roads

Government departments require contractors to be registered and check filer status before paying.""")
more("blogs/tax-consultant-hangu-city.html", """## Mobile and Electronics Shops

Mobile phone shops sell handsets, accessories and repair services. Handsets are often bought from Peshawar dealers; invoices and IMEI records support purchases.""")
more("blogs/tax-consultant-haripur.html", """## Telecom Equipment Factory

Staff of the telecom equipment factory in Haripur have tax withheld from salary.""")
more("blogs/ntn-registration-haripur.html", """## Transporters

Truck owners carrying raw materials and finished goods for Hattar factories register to be paid by bank transfer.

## Shops on the GT Road

Shops and restaurants along the highway that accept card payments need business accounts.

## Students

Students at the University of Haripur who start freelancing register with their CNIC.""")
more("blogs/ntn-registration-haroonabad.html", """## Sugar Cane Growers with Side Businesses

Growers who also run tractor-trolley haulage for sugar mills register for that business, since mills withhold tax on freight payments.

## Young People

Graduates from Haroonabad working in Lahore or abroad register with their CNIC to build a record.""")
more("blogs/tax-consultant-havelian.html", """## Railway Terminus

As the end of the railway line, Havelian once handled freight for Hazara; goods yards and warehouses near the station are rented out, and that rent is property income.""")
more("blogs/tax-consultant-hazro.html", """## Weddings Funded from Abroad

Large weddings paid for by relatives abroad involve gifts of gold and cash. Gifts from close relatives are generally not income, but the gold belongs in the recipient's wealth statement.""")


def add(rel, text, key="body_more"):
    PAGES.setdefault(rel, {}).setdefault(key, "")
    PAGES[rel][key] += "\n\n" + text


add("blogs/ntn-registration-gojra.html", "## Commission Agents' Munshis\n\nClerks who keep the books for arhtis and later open their own commission shops register under their own CNIC from the first season, so their commission income is on record from the start.")
add("blogs/tax-consultant-gujrat-city-centre.html", "## Property Dealers\n\nEstate agents in the city centre earn commission on sales and rentals, often from buyers abroad. Their income is commission, and advance tax collected at transfers belongs to the buyer and seller, not the dealer.")
add("blogs/ntn-registration-gwadar.html", "## Guest Houses and Tour Operators\n\nVisitors drawn to the Hammerhead, Ormara and Kund Malir beaches book guest houses and drivers in advance, often by bank transfer, and corporate clients ask for registration details.")
add("blogs/income-tax-filing-gwadar.html", "## Shops in the Old Town\n\nShopkeepers in Gwadar's old bazaar show purchases from Karachi and Turbat suppliers, sales and closing stock, with goods from Iran recorded only when bought through documented channels.")
add("blogs/ntn-registration-hafizabad.html", "## Brick Kilns\n\nKiln owners supplying housing schemes in Hafizabad and Gujranwala deal with contractors who withhold tax from payments and prefer registered sellers.")
add("blogs/tax-consultant-hangu.html", "## Thall and the Upper Valleys\n\nThall's bazaar is a trading point for the upper Kurram region. Wholesalers there supply shops further up the valley and keep records of goods sent on credit, which are receivables at 30 June.")
add("blogs/ntn-registration-hangu.html", "## Women Running Home Businesses\n\nWomen who sell embroidered clothes or run tailoring from home can register under their own CNIC, keeping their earnings in their own bank accounts.\n\n## Doctors Starting Private Practice\n\nDoctors who open clinics in Hangu register to deal with pharmaceutical suppliers and panels that pay fees by bank transfer.")
add("blogs/tax-consultant-hangu-city.html", "## Hotels and Restaurants\n\nRoadside restaurants and small hotels on the Kohat road serve travellers to Thall and Parachinar. Their services fall under KPRA, and their daily sales notes and food purchase bills support the income tax return.")
add("blogs/ntn-registration-haripur.html", "## Poultry and Dairy Farms\n\nCommercial poultry sheds and dairies supplying Islamabad register to deal with processors and feed companies that pay and are paid through banks.")
add("blogs/income-tax-filing-haripur.html", "## Shops in Haripur City\n\nShopkeepers on the main bazaar show sales, purchases and stock, together with the advance tax charged on their commercial electricity bills.")
add("blogs/ntn-registration-haroonabad.html", "## Shops in the Main Bazaar\n\nCloth and grocery shops that accept wallet and card payments need business accounts, and suppliers in Bahawalnagar and Bahawalpur prefer registered retailers.")
add("blogs/income-tax-filing-haroonabad.html", "## Transporters\n\nTruck owners carrying bales to mills in Faisalabad and Multan show freight receipts, fuel and repair costs, and the advance tax paid with their annual token.")
add("blogs/ntn-registration-haveli-lakha.html", "## Workers Abroad\n\nYoung men from Haveli Lakha working in the Gulf can register with their NICOP and file online, so that land bought in their name back home attracts the filer rate.")
add("blogs/tax-consultant-havelian.html", "## Construction Materials\n\nStone crushers and sand suppliers around Havelian serve motorway and housing projects; contractors withhold tax on their bills, which is claimed as credit.")
add("blogs/ntn-registration-haripur.html", "## Tarbela Fishermen and Boat Operators\n\nBoat operators at Tarbela and Khanpur who take visitors out register to accept online bookings.")
add("blogs/ntn-registration-haroonabad.html", "## Rice Mills\n\nHusking units in the tehsil register before applying for sales tax registration, which exporters require.")
