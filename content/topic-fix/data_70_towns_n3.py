"""Rewrites and local additions for towns N pages."""

PAGES = {}


def add(rel, text, key="body_more"):
    PAGES.setdefault(rel, {}).setdefault(key, "")
    PAGES[rel][key] += "\n\n" + text


def body(rel, text):
    PAGES.setdefault(rel, {})["body"] = text


body("blogs/ntn-registration-sammundri.html", """## Weavers Supplying Faisalabad's Processing Houses

Sammundri's loom sheds sit about forty kilometres from Faisalabad's dyeing and printing units, and much of their grey cloth goes there. A shed that only weaves on conversion can run with little paperwork, because the processor owns the yarn and the cloth. The moment a weaver starts buying his own yarn from spinning mills and selling cloth by the metre, the buyers' accounts teams ask for two numbers: an FBR NTN and a sales tax registration number. Without them, the processor cannot claim input tax on the cloth, and will usually prefer a registered competitor. The NTN is the first step; the sales tax application follows, with biometric verification and a check of the shed and its electricity meter.

## Arhtis in the Grain Market

Flour mills in Faisalabad paying Sammundri's arhtis for wheat transfer money by bank and withhold income tax at a higher rate from those not on the Active Taxpayers List.

## Tractor-Trolley Owners and the Sugar Mills

Mills nearby register cane haulers each autumn and withhold tax from freight payments.

## Young People in Faisalabad's Offices

Graduates working in Faisalabad's textile offices register on IRIS to file their own returns.

## Applying

Registration is free and online; our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows each screen.""")

body("blogs/income-tax-filing-sanghar.html", """## A Ginner's Year in Shahdadpur or Sanghar

Ginning in Sanghar district begins as early as July, because cotton in lower Sindh is picked before Punjab's. A ginner's return therefore often straddles two seasons. It shows lint and cottonseed sold, seed cotton bought from growers and middlemen, electricity, labour, bale-pressing, freight and depreciation of gins and presses. Seed cotton and bales on hand on 30 June are closing stock. Spinning mills' withholding on lint purchases is claimed, and the figures are reconciled with the monthly sales tax returns.

## Contractors at the Oil and Gas Fields

A contractor supplying transport, security or civil works to an exploration company lists each invoice, the income tax withheld, and the costs of crews, vehicles, fuel and equipment. Sindh sales tax on services charged to the company is paid over to the Sindh Revenue Authority and is not income.

## Landowners with Well Sites

Rent received from a company for land used for a well site or pipeline corridor is income, declared with the withholding claimed. Compensation for crops damaged during drilling, and for land acquired, is documented separately.

## Growers

Cotton and wheat from family land are agricultural income; larger holdings pay Sindh agricultural tax.

## Wholesalers

Sales on credit to village shops are recorded when made, with unpaid amounts as receivables.""")

body("blogs/ntn-registration-shakargarh.html", """## Hauling Cane for the Mill

Shakargarh's sugar mill relies on tractor-trolleys from surrounding villages during the crushing season. Its cane office registers haulers in October and November and asks each for an FBR NTN and a bank account in his own name. The mill withholds income tax on every freight payment; a hauler who has filed a return for the latest year is withheld at the lower rate, which over a full season adds up to a meaningful amount.

## Basmati Mills Near the Ravi

Rice mills in the tehsil sell to exporters in Lahore who require income tax and sales tax registration and proper invoices.

## Contractors in the Border Belt

Departments building and repairing roads, culverts and schools in the border villages give work only to registered contractors and check their filer status.

## Families with Members in Spain and the Gulf

Relatives abroad who plan to buy plots in Shakargarh or Narowal can register online with a NICOP and file each year from abroad.

## Doctors and Shops in the City

Clinics and retailers that want card machines or wallet merchant accounts open business accounts after registering.

## Registering

Registration is free and online; see our [FBR registration guide](/blogs/fbr-registration-step-by-step).""")

body("blogs/ntn-registration-sheikhupura.html", """## Vendor Lists on the Lahore and Faisalabad Roads

Sheikhupura's large textile, steel and food factories buy transport, packaging, chemicals, canteen services and maintenance from hundreds of local firms. Each factory's purchase department keeps an approved vendor list and adds a new supplier only after seeing an FBR NTN, a bank account in the supplier's own name and, depending on what is supplied, a sales tax registration number or Punjab Revenue Authority registration. Payments are then made by bank transfer, with income tax withheld at a lower rate for suppliers who have filed.

## Moving a Workshop Out of Lahore

Many small manufacturers are moving from crowded parts of Lahore to cheaper sheds around Sheikhupura and Ferozewala. The business keeps its NTN, but the new factory premises must be added to its registration, and sales tax registration for the new site involves fresh verification of the premises and electricity connection.

## Rice Husking Units

Exporters buy only from units registered for income tax and sales tax.

## Landlords Renting Sheds

Owners renting industrial sheds register to declare rent and to receive it after the tenant's withholding.

## Workers

Factory staff can register on IRIS to file their own returns.

## Applying

Registration is free and online; our [FBR registration guide](/blogs/fbr-registration-step-by-step) explains each step.""")

body("blogs/income-tax-filing-sheikhupura.html", """## Factory Owners

A Sheikhupura factory's return is the end of a year-long chain of filings: monthly sales tax returns, withholding statements for tax deducted from suppliers, and quarterly advance tax payments. The annual accounts show sales, raw materials, power and gas, wages, repairs and depreciation of machinery, with stock counted on 30 June. Before filing, the sales figure is reconciled with the sales tax returns and the expense figures with the withholding statements, because FBR's systems compare them automatically.

## Contractors and Suppliers

Each payment received from factories, the tax withheld and the costs of the work are listed. PRA tax charged on services is collected for the province and is not income.

## Rice Mills

Rice and by-product sales against paddy, power, labour and depreciation, with stock on 30 June.

## Factory Workers and Commuters

Salary and withholding from certificates; workers who changed jobs combine both.

## Landlords

Rent from sheds and houses, with tenants' withholding claimed.

## Farmers

Paddy and wheat from family land are agricultural income.

## Selling Land on the Industrial Roads

A sale is reported with price, cost, gain and the seller's advance tax; the gain's treatment depends on when the land was acquired.""")
PAGES["blogs/income-tax-filing-sheikhupura.html"]["desc"] = "Income tax return filing in Sheikhupura for factory owners, contractors, rice mills, workers, landlords and farmers, filed online."

body("blogs/income-tax-filing-sammundri.html", """## Weaving on Conversion

Most of Sammundri's loom sheds weave for Faisalabad processors on conversion. The return shows the conversion charges received from each processor, usually per metre or per pick, against electricity, weavers' wages, sizing, spare parts and depreciation of the looms. Electricity is the largest cost, and the advance tax charged on industrial bills is listed month by month and claimed.

## Weavers Who Buy Their Own Yarn

Sheds that buy yarn and sell cloth show purchases, sales and the stock of yarn and cloth on 30 June, matched to their sales tax returns.

## Arhtis

Commission on wheat, cotton and cane sold for growers, less shop costs. Loans to growers are receivables, and flour mills' withholding is claimed.

## Cane Haulers

Freight from mill slips, less diesel, drivers' wages, tyres and depreciation of tractors and trolleys.

## Farm Families

Crops from family land are agricultural income.

## Faisalabad Commuters

Salary and withholding are copied from certificates.

## Wealth Statement

Looms, sheds, land, vehicles, receivables and balances, with changes explained.""")
PAGES["blogs/income-tax-filing-sammundri.html"]["desc"] = "Income tax return filing in Sammundri for conversion weavers, loom owners, arhtis, cane haulers, farmers and Faisalabad commuters."

add("blogs/ntn-registration-sambrial.html", "## Packing and Labelling Units\n\nFirms that pack and label goods for exporters near the dry port are asked for registration before being paid by bank.")
add("blogs/income-tax-filing-sambrial.html", "## Families with Members in Italy and Spain\n\nRelatives who own property in Sambrial in their own names file their own returns; those living abroad are generally taxed here only on Pakistani income.\n\n## Shops\n\nShopkeepers show sales, purchases and stock.\n\n## Late Filing\n\nA late return is accepted with the surcharge.")
add("blogs/tax-consultant-sammundri.html", "## Transporters\n\nTruck owners carrying cloth and grain to Faisalabad keep freight records and claim the token tax.")
add("blogs/tax-consultant-sanghar.html", "## Shahdadpur and Sinjhoro\n\nThe district's other towns have their own ginners and grain markets, with similar records.")
add("blogs/tax-consultant-sargodha.html", "## Cold Storage for Citrus\n\nCold stores holding kinnow for later sale charge rent per crate, which is business income for the owner.\n\n## Shops\n\nRetailers keep supplier bills and daily sales.")
add("blogs/income-tax-filing-sargodha.html", "## Cold Store Owners\n\nRent per crate less electricity, staff and depreciation.\n\n## Doctors\n\nSalary from the hospital plus private clinic fees.\n\n## Landlords\n\nRent declared, with tenants' withholding claimed.\n\n## Late Filing\n\nLate returns are accepted with the surcharge.")
add("blogs/tax-consultant-sargodha-lyon-colony.html", "## Tutors and Academies\n\nTeachers who run evening tuition from home declare fees as income.")
add("blogs/tax-consultant-sehwan.html", "## Boat Owners on the Indus\n\nBoatmen ferrying visitors and goods across the river keep simple records of fares.")
add("blogs/tax-consultant-shahpur.html", "## Teachers and Officials\n\nSalaried residents have tax withheld and file to record property.")
add("blogs/tax-consultant-shakargarh.html", "## Transporters\n\nTruck owners carrying paddy and cane keep freight records.\n\n## Doctors and Clinics\n\nDoctors declare fees less clinic costs.")
add("blogs/income-tax-filing-shakargarh.html", "## Mill Employees\n\nStaff of the sugar mill copy salary and withholding from their certificates.\n\n## Doctors and Shopkeepers\n\nDoctors show clinic fees against rent and staff; shopkeepers show sales against purchases.\n\n## Late Filing\n\nA late return is accepted with the surcharge.")
add("blogs/tax-consultant-shangla.html", "Their records should start early.")
add("blogs/tax-consultant-sheikhupura.html", "## Hiran Minar and Visitors\n\nRestaurants and shops near the Hiran Minar serve weekend visitors from Lahore; restaurants deal with PRA.")

add("blogs/ntn-registration-sambrial.html", "## Restaurants Near the Airport\n\nEateries serving travellers and airport staff register with FBR and the Punjab Revenue Authority to accept card payments.")
add("blogs/income-tax-filing-sambrial.html", "## Airport and Dry Port Employees\n\nStaff employed at the airport, the dry port and by airlines copy salary and withholding from their certificates; shift allowances and overtime are part of taxable salary.\n\n## Bank Profit\n\nProfit on savings is declared with the bank's withholding.")
add("blogs/tax-consultant-sammundri.html", "Their vehicles are depreciated.")
add("blogs/ntn-registration-sammundri.html", "## Shops in Sammundri Town\n\nRetailers wanting card machines open business accounts after registering.")
add("blogs/income-tax-filing-sammundri.html", "## Shops in the Bazaar\n\nShopkeepers show sales, purchases from Faisalabad wholesalers and stock on 30 June, claiming the advance tax charged on commercial electricity bills.\n\n## Bank Profit\n\nProfit on savings is declared with the bank's withholding.\n\n## Late Filing\n\nA return filed after the deadline is accepted; the surcharge applies for the Active Taxpayers List.")
add("blogs/income-tax-filing-sanghar.html", "## Late Filing\n\nA late return is accepted with the surcharge.")
add("blogs/tax-consultant-sargodha.html", "Their stock is counted on 30 June.")
add("blogs/income-tax-filing-sargodha.html", "## Contractors Who Buy Kinnow on the Tree\n\nThese contractors show sales to packing houses and markets against the contract price, picking labour, crates and freight. Frost or hail can cause a loss, which is shown and generally carried forward.\n\n## Bank Profit\n\nProfit on savings and certificates is declared with the bank's withholding.")
add("blogs/tax-consultant-sargodha-lyon-colony.html", "Tutors who rent rooms for classes deduct that rent.")
add("blogs/tax-consultant-sehwan.html", "## Sweets and Food Stalls\n\nSweet makers and food stalls that run day and night during the urs buy ingredients in bulk beforehand; their purchase bills and daily sales notes form their records.")
add("blogs/tax-consultant-shahpur.html", "## Property\n\nPlots in Shahpur and Sargodha cost less in advance tax for active filers, and sellers keep acquisition records.")
add("blogs/tax-consultant-shakargarh.html", "## Teachers and Officials\n\nSalaried staff copy their salary certificates and list land and houses.\n\n## Late Filing\n\nA late return is accepted with the surcharge.")
add("blogs/ntn-registration-shakargarh.html", "## Students\n\nStudents who start freelancing register with their CNIC so that payments reach their own accounts.")
add("blogs/income-tax-filing-shakargarh.html", "## Rice Husking Units\n\nUnits show rice sold against paddy, power and labour, with stock on 30 June.\n\n## Teachers and Officials\n\nSalary and withholding are copied from certificates.\n\n## Bank Profit\n\nProfit on savings is declared with the bank's withholding.")
add("blogs/tax-consultant-shangla.html", "## Alpuri and Puran\n\nShops in the district's other towns bring goods from Besham and Mingora and keep supplier bills and daily sales notes.")
add("blogs/tax-consultant-sheikhupura.html", "Their sales are recorded daily.")
add("blogs/ntn-registration-sheikhupura.html", "It costs nothing to register.")
add("blogs/income-tax-filing-sheikhupura.html", "## Bank Profit\n\nProfit on savings is declared with the bank's withholding.\n\n## Late Filing\n\nA late return is accepted with the surcharge to rejoin the Active Taxpayers List.")

add("blogs/tax-consultant-sammundri.html", "Loom owners also list their sheds in the wealth statement.")
add("blogs/ntn-registration-sammundri.html", "Filing the first return completes the process.")
add("blogs/income-tax-filing-sammundri.html", "Pensioners declare their pension as exempt.")
add("blogs/income-tax-filing-sanghar.html", "Bank profit is declared with the bank's withholding.")
add("blogs/income-tax-filing-sargodha.html", "## Pensioners\n\nRetired air force and civil officers declare pensions as exempt and list their houses.")
add("blogs/tax-consultant-sargodha-lyon-colony.html", "Their fee records should be kept.")
add("blogs/tax-consultant-shakargarh.html", "Their wealth statements list houses and land.")
add("blogs/ntn-registration-shakargarh.html", "## Teachers and Officials\n\nSalaried residents can register on IRIS to file their own returns and claim back excess withholding.")
add("blogs/income-tax-filing-shakargarh.html", "## Border-Area Farmers\n\nFarmers whose land lies near the border keep land records current; their crop income is agricultural like any other.\n\n## Pensioners\n\nRetired soldiers declare their pension as exempt.")
add("blogs/tax-consultant-sheikhupura.html", "Their kitchens' purchase bills support costs.")
add("blogs/ntn-registration-sheikhupura.html", "Then file every year to stay on the list.")
add("blogs/income-tax-filing-sheikhupura.html", "## Pensioners\n\nRetired workers declare pensions as exempt and list their houses.")
add("blogs/income-tax-filing-sargodha.html", "Commutation used to buy property is shown as its source.")
add("blogs/tax-consultant-shakargarh.html", "Late filers pay a surcharge to rejoin the list.")
add("blogs/income-tax-filing-shakargarh.html", "## Transporters\n\nTruck and trolley owners carrying paddy to mills and cane to the sugar mill show freight against diesel, tyres and wages, and claim the token tax paid each year.")
add("blogs/income-tax-filing-sheikhupura.html", "Commutation used for a house is shown as its source.")
