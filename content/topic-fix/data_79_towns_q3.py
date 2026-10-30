"""Rewrites and local additions for towns Q pages."""

PAGES = {}


def add(rel, text, key="body_more"):
    PAGES.setdefault(rel, {}).setdefault(key, "")
    PAGES[rel][key] += "\n\n" + text


def body(rel, text, desc=None):
    PAGES.setdefault(rel, {})["body"] = text
    if desc:
        PAGES[rel]["desc"] = desc


body("blogs/ntn-registration-toba-tek-singh.html", """## A Ginner an Hour from Faisalabad

Toba Tek Singh's ginning factories sit within easy reach of Faisalabad's spinning mills, and that proximity shapes their paperwork. A spinning mill's purchase department will not issue a purchase order for lint until it has the ginner's FBR NTN and sales tax registration number on file, because it needs proper sales tax invoices to claim input tax. The sales tax application asks for biometric verification, details of the factory's electricity meter and, often, a physical check of the premises. A ginner who applies in March is ready for the first phutti in late summer.

## Loom Sheds Moving to Their Own Sales

Weavers who stop working only on conversion and start buying yarn and selling cloth need registration so that processors buying their cloth can claim input tax.

## Arhtis in the Grain Market

Flour mills paying arhtis by bank withhold income tax at a lower rate from those who have filed a return.

## Seed, Fertiliser and Pesticide Dealers

National companies appoint dealers only after registration.

## Shops in Pirmahal and Toba City

Retailers who want card machines or wallet merchant accounts open business accounts after registering.

## Registering

Registration is free and online with a CNIC and a mobile number in your name; our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows each screen.""")

body("blogs/income-tax-filing-toba-tek-singh.html", """## Families Farming Chak Land

A typical Toba Tek Singh family return declares cotton, wheat, sugarcane and fodder from the family's squares of chak land as agricultural income, notes any Punjab agricultural income tax paid, and lists the land, tubewell, tractor and house in the wealth statement. If part of the land is leased out for cash rent, that rent is also agricultural income for the owner.

## Ginners

Lint and cottonseed sales against seed cotton bought, electricity, labour, bale-pressing and depreciation of machinery. Bales and seed cotton on hand on 30 June are closing stock. Each spinning mill's withholding is listed and claimed, and the sales figure is reconciled with the monthly sales tax returns.

## Loom Owners

Conversion charges or cloth sales against electricity, weavers' wages, sizing and repairs, with looms depreciated and the advance tax on industrial electricity bills claimed.

## Arhtis and Dealers

Commission less shop costs for arhtis; sales, purchases, stock and farmers' unpaid balances for input dealers, with companies' withholding claimed.

## Commuters to Faisalabad

Salary and withholding from certificates.

## Shops and Professionals

Shopkeepers show sales and purchases; doctors and lawyers show fees against professional costs.""")

body("blogs/ntn-registration-turbat.html", """## Kech Dates on Karachi's Shelves

Turbat's date traders increasingly sell dried and packed dates directly to wholesalers, supermarket suppliers and online stores in Karachi rather than through middlemen. These buyers pay by bank transfer, and larger ones ask for the trader's FBR NTN before placing regular orders. Registration also allows a trader to open a business account and, if exporting, to clear goods through customs.

## Contractors for Kech's Departments

Roads, water schemes, schools and the canals fed by the Mirani dam are built through registered contractors, and departments decide the withholding rate on each bill according to the contractor's filer status.

## Coach Companies Running to Karachi and Gwadar

Transport companies with daily coaches to Karachi, Gwadar and Quetta register to deal with fuel companies, corporate bookings and the advance tax paid with each vehicle's annual token.

## Workers in Oman and the UAE

Turbat's many workers in Muscat, Dubai and Sharjah can register with a NICOP and file online, so that land and houses bought at home attract the lower advance tax charged to active filers.

## Graduates

Graduates of the University of Turbat starting jobs or consultancy register with their CNIC.

## Registering

Registration is free and online; see our [FBR registration guide](/blogs/fbr-registration-step-by-step).""",
     "NTN registration in Turbat for date traders, Kech contractors, coach companies, workers in Oman and the UAE, and graduates.")

body("blogs/income-tax-filing-turbat.html", """## Date Growers

Dates harvested from the family's own palms in the Kech valley, whether sold fresh or dried, are agricultural income and declared as such.

## Date Traders and Packers

A trader's return shows dates bought from growers during the summer harvest, drying and sorting labour, cartons and packing, freight to Karachi, and sales to wholesalers and stores. Dates still in the godown on 30 June, which falls in the middle of the harvest, are closing stock at cost; getting this cut-off right avoids a false loss in one year and a false profit in the next.

## Contractors

Each bill paid by Kech's departments, the tax withheld and the costs of labour, materials and machinery.

## Coach and Truck Owners

Fares and freight against diesel, tyres, repairs and drivers' wages, with vehicles depreciated and the token tax claimed.

## University and Government Staff

Salary and withholding from certificates.

## Families Supported from the Gulf

Transfers from Oman and the UAE are receipts in the wealth statement of the person who receives them, together with what they pay for.""",
     "Income tax return filing in Turbat for date growers and packers, Kech contractors, transporters, staff and families supported from the Gulf.")

body("blogs/ntn-registration-vehari.html", """## Burewala, Mailsi and Vehari Ginners

Vehari district's ginners sell lint to spinning mills in Multan, Faisalabad and Lahore. Those mills require an FBR NTN and a sales tax registration number from every ginner before purchase, and they withhold income tax on each payment at a rate that depends on the ginner's filer status. Because the sales tax application includes biometric verification and a factory inspection, a new ginner or one re-registering after a change of ownership should begin well before the picking season.

## Appointed Input Dealers

Seed, fertiliser and pesticide companies appoint dealers in Vehari's bazaars only after registration and withhold tax on each consignment supplied.

## Commercial Dairies

Milk processors collecting from Vehari's larger dairies pay by bank and withhold tax at a higher rate from suppliers who have not filed.

## Commission Agents

Flour mills buying wheat through Vehari's grain market pay by bank.

## Families Buying Plots in the City

The buyer's advance tax at transfer is lower for active filers.

## Registering

Registration is free and online; our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows each step.""")

body("blogs/income-tax-filing-vehari.html", """## Cotton Growers

Cotton, wheat and fodder from family land are declared as agricultural income, with Punjab agricultural income tax noted for larger holdings. The land, tubewells and tractors are listed in the wealth statement.

## Ginners

The return shows lint and cottonseed sales against seed cotton bought, electricity, seasonal labour, bale-pressing and depreciation of gins and presses. Seed cotton and bales on hand on 30 June are closing stock. Spinning mills' withholding is listed and claimed, and the figures are reconciled with sales tax returns.

## Input Dealers

Sales to farmers, much of it on credit until cotton is picked, purchases from companies and stock on 30 June. Farmers' unpaid balances are receivables; debts written off after genuine recovery efforts can be claimed under the rules.

## Commercial Dairies

Milk sales against feed, labour, veterinary costs and electricity, with the herd shown as an asset.

## Arhtis

Commission less costs; loans to growers as receivables.

## Government Employees

Salary and withholding from certificates.""",
     "Income tax return filing in Vehari for cotton growers, ginners, input dealers, commercial dairies, arhtis and government staff.")

body("blogs/ntn-registration-wazirabad.html", """## Exporting Wazirabad Cutlery

Knives, scissors and cookware from Wazirabad are shipped to buyers in Europe, the Middle East and North America. Exporting requires an FBR NTN for customs clearance and for the bank that receives export proceeds and collects tax on them. Exporters also need an account with the export promotion and chamber bodies that issue certificates of origin.

## Selling Through Distributors and Online

Kitchenware distributors and large retailers in Lahore and Karachi buy only from registered manufacturers who can issue sales tax invoices. Online marketplaces ask sellers for registration details before paying out.

## Polishing and Grinding Units

Larger manufacturers pay their subcontractors by bank and ask for an NTN before releasing job charges.

## Railway Contractors

Contractors on works at Wazirabad junction need registration.

## Relatives in Europe

Family members in Spain or Italy can register with a NICOP and file online so that plots at home are transferred at the filer rate.

## How to Register

Registration is free and online; our [FBR registration guide](/blogs/fbr-registration-step-by-step) explains each step.""")

body("blogs/income-tax-filing-wazirabad.html", """## Cutlery Manufacturers

A Wazirabad cutlery unit's return shows sales to distributors, retailers, exporters and online buyers against steel and stainless sheet, handle materials, grinding wheels and polishing compounds, wages for forging, grinding and polishing, electricity and depreciation of machinery. Finished goods and raw steel on hand on 30 June are closing stock. Sales figures are matched to sales tax returns where the unit is registered.

## Exporters

Export proceeds received through banks and the tax collected on them are listed. Under the final tax regime that tax is the final liability on export income; if the exporter opts out where the law allows, normal tax applies.

## Subcontractors

Grinding and polishing units show job charges against wages, power and consumables.

## Railway Staff and Pensioners

Salary and withholding from certificates; pensions declared as exempt.

## Families with Relatives Abroad

Money received through banks from relatives in Europe or the Gulf is shown as receipts.

## Shops

Traders show sales, purchases and stock.""")

body("blogs/ntn-registration-zafarwal.html", """## Before Buying a Plot with Money from Abroad

Zafarwal families often buy plots and build houses with money sent by sons and brothers in Spain, Italy and the Gulf. If the plot is to be registered in the name of the relative abroad, he should register with FBR and file a return before the transfer, because the buyer's advance tax under section 236K is much lower for active filers. Registration is online with a NICOP or CNIC, an email address and a Pakistani mobile number registered in his name.

## Contractors in the Border Villages

Departments building roads, culverts and schools near the working boundary require registered contractors and check filer status before deciding withholding.

## Rice Traders and Husking Units

Mills and exporters in Narowal and Sialkot buying paddy and rice pay by bank and ask for registration.

## Shops and Clinics

Retailers and clinics in Zafarwal town that want card machines open business accounts after registering.

## Students Applying Abroad

Young people applying to study in Europe often include a filed return in their visa file.

## Registering

Registration is free and online; see our [FBR registration guide](/blogs/fbr-registration-step-by-step).""",
     "NTN registration in Zafarwal for relatives abroad buying plots, border-area contractors, rice traders, shops and students.")

body("blogs/income-tax-filing-zafarwal.html", """## Growers Near the Working Boundary

Basmati, wheat and fodder from family land in Zafarwal's villages are declared as agricultural income. Tubewell owners who sell water to neighbours declare that hire income separately.

## Households Supported from Europe

Many Zafarwal households receive regular transfers from relatives in Spain, Italy or Greece. These are receipts, shown in the wealth statement of the family member who receives them, with a note of what each large transfer paid for: a house, a plot, a wedding or a tractor. If the relative abroad owns the property in his own name, it belongs in his own return.

## Border-Area Contractors

Each bill paid by the department, the tax withheld and the costs of labour, materials and machinery.

## Rice Traders and Husking Units

Sales against paddy bought, husking costs and freight, with stock counted on 30 June.

## Shopkeepers

Sales, purchases from Narowal and Sialkot wholesalers and stock.

## Teachers and Officials

Salary and withholding from certificates.""",
     "Income tax return filing in Zafarwal for growers, households supported from Europe, border contractors, rice traders and staff.")

add("blogs/tax-consultant-topi.html", "## Staff Housing\n\nFaculty living in campus housing may have a taxable perquisite shown on their certificate.\n\n## Property\n\nPlots in Swabi and Islamabad cost less in advance tax for active filers.")
add("blogs/tax-consultant-turbat.html", "## Mirani Dam Farms\n\nLand irrigated by the dam's canals grows wheat and vegetables, which are agricultural income.")
add("blogs/tax-consultant-uch-sharif.html", "## Handicrafts\n\nArtisans making embroidered textiles and pottery for visitors earn business income from their sales.")
add("blogs/tax-consultant-umerkot.html", "## Chilli Grinding Units\n\nUnits that grind chillies into powder for spice brands earn business income after raw chillies, power and packing.")
add("blogs/tax-consultant-upper-dir.html", "## Dir Town's Hospital and Offices\n\nDoctors and staff at the district hospital and offices have salary tax withheld; doctors with private clinics declare those fees separately.")
add("blogs/tax-consultant-vehari.html", "## Burewala and Mailsi\n\nThe district's other tehsils have their own ginners and grain markets; residents there file in the same way.")
add("blogs/tax-consultant-vehari-city.html", "## Private Hospitals\n\nPrivate hospitals and laboratories show patient fees against staff, medicines and equipment depreciation.")
add("blogs/tax-consultant-wazirabad.html", "## Sohdra and the Chenab Bank\n\nWorkshops in nearby Sohdra and along the Chenab follow the same patterns as Wazirabad's.")
add("blogs/tax-consultant-yazman.html", "Their purchase bills support costs.")
add("blogs/tax-consultant-zafarwal.html", "## Property\n\nPlots in Zafarwal and Narowal cost less in advance tax for active filers.")

add("blogs/income-tax-filing-toba-tek-singh.html", "## Pensioners\n\nRetired soldiers and teachers living in the chak villages declare their pension as exempt and list the land and house they own, so that the wealth statement shows how their assets were built up.")
add("blogs/tax-consultant-topi.html", "## Shops Near the Campus\n\nPhotocopy shops, eateries and stationers serving students keep daily sales notes; most of their trade follows the semester calendar.")
add("blogs/tax-consultant-turbat.html", "Their crop records should be kept up to date.")
add("blogs/ntn-registration-turbat.html", "Filing the first return completes the process.")
add("blogs/income-tax-filing-turbat.html", "## Shops in Turbat Bazaar\n\nShopkeepers show sales, purchases from Karachi suppliers brought by coach and truck, and stock on 30 June. Goods bought across the border should be supported by customs documents.\n\n## Pensioners\n\nRetired teachers and officials declare their pension as exempt.")
add("blogs/tax-consultant-uch-sharif.html", "## Property\n\nPlots in Uch and Bahawalpur cost less in advance tax for active filers, and sellers keep acquisition records.")
add("blogs/tax-consultant-umerkot.html", "Their stock is counted at year end.")
add("blogs/tax-consultant-upper-dir.html", "## Honey and Walnuts\n\nHoney from family hives and walnuts from family trees are generally part of farming; buying them to resell is trading.")
add("blogs/tax-consultant-vehari.html", "Their returns follow the same pattern.")
add("blogs/ntn-registration-vehari.html", "## Students\n\nStudents at Vehari's university campus who begin freelancing register with their CNIC.\n\n## Overseas Workers\n\nWorkers from the district in the Gulf can register with a NICOP.")
add("blogs/income-tax-filing-vehari.html", "## Shops in the City\n\nShopkeepers show sales, purchases from Multan wholesalers and stock, claiming advance tax charged on commercial electricity bills.\n\n## Pensioners\n\nRetired staff declare pensions as exempt and list their houses.")
add("blogs/tax-consultant-vehari-city.html", "## Tutors and Academies\n\nAcademies preparing students for entry tests keep fee registers.")
add("blogs/tax-consultant-wazirabad.html", "Their exports are documented through banks.")
add("blogs/ntn-registration-wazirabad.html", "## Shops in the Bazaar\n\nRetailers in Wazirabad's bazaar who want card machines open business accounts after registering.\n\n## Teachers and Officials\n\nSalaried residents can register on IRIS to file their own returns.")
add("blogs/income-tax-filing-wazirabad.html", "## Online Cutlery Sellers\n\nUnits selling knives and kitchenware through marketplaces show sales from platform statements against product cost, courier charges, returns and advertising.\n\n## Property\n\nPlots bought in Gujranwala's schemes are shown at cost.")
add("blogs/tax-consultant-yazman.html", "Hotels in Bahawalpur also benefit from rally visitors.")
add("blogs/tax-consultant-zafarwal.html", "Sellers keep acquisition records.")
add("blogs/ntn-registration-zafarwal.html", "It is free to register.")
add("blogs/income-tax-filing-zafarwal.html", "## Pensioners\n\nRetired soldiers and teachers declare their pension as exempt and list their land and house.\n\n## Property Sales\n\nA plot sold during the year is reported with price, cost, gain and the advance tax paid.")
add("blogs/tax-consultant-topi.html", "Their busiest months are the teaching terms.")
add("blogs/tax-consultant-turbat.html", "## Families in Oman\n\nMany households receive transfers from Muscat; these are receipts in the wealth statement.")
add("blogs/ntn-registration-turbat.html", "Then file every year to stay on the list.")
add("blogs/income-tax-filing-turbat.html", "## Property in Karachi\n\nA flat in Karachi rented out by a Turbat family is declared under property income.")
add("blogs/tax-consultant-uch-sharif.html", "## Rice Husking\n\nSmall husking units near Uch earn charges from traders, which are business income after power and labour.")
add("blogs/tax-consultant-umerkot.html", "## Kunri's Commission Agents\n\nAgents in the chilli market earn commission, with advances to growers recorded as receivables.")
add("blogs/tax-consultant-upper-dir.html", "Records of purchases matter.")
add("blogs/tax-consultant-vehari.html", "## Teachers and Doctors\n\nSalaried professionals declare private tuition or clinic fees separately from salary.")
add("blogs/ntn-registration-vehari.html", "Registration is free.")
add("blogs/income-tax-filing-vehari.html", "## Transporters\n\nTruck owners carrying bales to mills show freight against diesel, tyres and wages, and claim the token tax.")
add("blogs/tax-consultant-vehari-city.html", "## Building Material Dealers\n\nCement and steel dealers supplying the city's new housing record sales to contractors.")
add("blogs/tax-consultant-wazirabad.html", "Customs papers support each shipment.")
add("blogs/ntn-registration-wazirabad.html", "Registration costs nothing.")
add("blogs/income-tax-filing-wazirabad.html", "## Pensioners\n\nRetired railway and factory staff declare their pension as exempt and list the houses and land they own.")
add("blogs/tax-consultant-yazman.html", "Rally fuel sales are recorded too.")
add("blogs/tax-consultant-zafarwal.html", "## Teachers and Doctors\n\nSalaried professionals who tutor or run clinics declare those fees separately.")
add("blogs/ntn-registration-zafarwal.html", "After registering, the first return should be filed promptly.")
add("blogs/income-tax-filing-zafarwal.html", "## Transporters\n\nTractor-trolley and truck owners carrying paddy to mills show freight against diesel and repairs.")
add("blogs/tax-consultant-upper-dir.html", "Dealers keep invoices.")
add("blogs/ntn-registration-vehari.html", "## Teachers and Officials\n\nSalaried residents can register on IRIS and file their own returns to claim back excess withholding.")
add("blogs/income-tax-filing-vehari.html", "Vehicles are depreciated over their life.")
add("blogs/tax-consultant-vehari-city.html", "Contractors may withhold tax.")
add("blogs/ntn-registration-wazirabad.html", "## Cutlery Brands Selling Abroad Online\n\nSmall brands shipping knives to customers abroad through international marketplaces need an NTN for the bank account that receives foreign payouts.")
add("blogs/income-tax-filing-wazirabad.html", "## Bank Profit\n\nProfit on savings held by cutlery families is declared with the withholding deducted by their bank.")
add("blogs/ntn-registration-zafarwal.html", "No fee is charged.")
add("blogs/income-tax-filing-zafarwal.html", "## Bank Profit\n\nProfit earned on savings accounts in Zafarwal's bank branches is declared, with the bank's withholding.")
add("blogs/income-tax-filing-vehari.html", "Fuel slips support the freight figure.")
add("blogs/income-tax-filing-wazirabad.html", "The bank's certificate is kept.")
add("blogs/income-tax-filing-zafarwal.html", "## Shops Rented Out\n\nOwners renting shops in Zafarwal town declare the rent.")
