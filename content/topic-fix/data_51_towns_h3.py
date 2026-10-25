"""Rewrites and local additions for towns H pages."""

PAGES = {}


def add(rel, text, key="body_more"):
    PAGES.setdefault(rel, {}).setdefault(key, "")
    PAGES[rel][key] += "\n\n" + text


def body(rel, text):
    PAGES.setdefault(rel, {})["body"] = text


body("blogs/ntn-registration-kotli.html", """## A Kotli Family's Typical Reasons

Most Kotli households who come to us for an FBR NTN have one of four things in front of them. A son has taken a job with a bank or telecom company in Rawalpindi and his employer wants his tax number. The family is buying a flat or plot in Islamabad and wants the lower advance tax charged to active filers. A builder from Kotli has won a subcontract on a project run by a Pakistani company. Or a relative in Birmingham wants to buy property in Pakistan proper in his own name.

## The Employee in Rawalpindi

An employee's NTN is simply his CNIC once he is registered on IRIS. Registering lets him file his own return, claim back excess withholding and show his Kotli house in his wealth statement.

## The Builder on a Pakistani Project

Pakistani companies will not pay subcontractors without an FBR NTN, and they withhold tax at a higher rate from anyone who has not filed. Registering and filing the first return is what brings that rate down.

## The Relative in Britain

British-Kashmiris can register with a NICOP, file online from the UK and remain on the Active Taxpayers List while living abroad.

## Income Earned Inside AJK

Profit from a Kotli shop, rent from a building in the bazaar or salary from the AJK government stays with AJK's own tax authorities. The FBR NTN sits alongside that registration; it does not replace it.

## Getting It Done

Registration is online and does not require living in Pakistan proper; your Kotli address is fine. Our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows each screen.""")

body("blogs/income-tax-filing-kotli.html", """## A Return Built Around Pakistan-Proper Income

The FBR return of a Kotli resident usually has fewer income lines than people expect. Typical entries are a salary from an employer in Rawalpindi or Islamabad, rent from a flat in Pakistan proper, profit on a savings account held with a bank branch outside AJK, and occasionally contract income from a Pakistani company. Profit from a family shop in Kotli or a salary from the AJK government is reported under AJK's system instead.

## Why the Wealth Statement Still Lists Everything

Even though AJK income stays outside the FBR return, the FBR wealth statement is a statement of all assets. The house in Kotli, land in the villages along the Poonch, gold and bank balances in AJK branches all appear. Without them, the year-to-year change in wealth cannot be explained.

## Money from Birmingham and Bradford

Transfers from relatives in Britain are receipts, not income. Each transfer should arrive through a bank, and the return notes who sent it and what it was for, such as building a house or buying land.

## Selling Property in Pakistan Proper

When a Kotli family sells a plot in Rawalpindi, the return shows the sale price, the original cost, the gain and the advance tax deducted at transfer. How the gain is taxed depends on when the plot was bought.

## Hydropower Project Workers

Engineers and staff employed by companies building projects on the Poonch who are paid from Pakistan proper copy their salary certificate into the FBR return.

## Consistency Between Two Systems

Figures given to AJK's tax office and to FBR should agree, because either may ask about assets disclosed to the other.""")

body("blogs/ntn-registration-kharian.html", """## Kharian's Scandinavian Connection

Kharian's villages, such as Dhakkar, Guliana and Kakrali, sent some of the earliest Pakistani workers to Norway and Denmark in the late 1960s and 1970s. Their children and grandchildren now hold houses, plots and agricultural land here. When one of them wants to sell an inherited house or buy a plot in a new scheme on the GT Road, registering with FBR and filing a return is what reduces the advance tax charged at transfer.

## Registering from Oslo or Copenhagen

Registration is online with a NICOP or CNIC. The person needs an email address and a phone that can receive FBR's verification codes; many overseas Pakistanis use a Pakistani number kept active for this. After registering, a return must be filed for the owner to appear on the Active Taxpayers List.

## Officers' Families Renting Houses

Houses in Kharian's newer areas are often rented to officers posted to the cantonment or to companies. Landlords register so that rent is declared and the withholding by company tenants can be claimed.

## Suppliers to the Cantonment

Contractors supplying rations, maintenance and transport to the cantonment are asked for an NTN, and their bills are withheld at lower rates once they file.

## Showrooms and Petrol Pumps on the GT Road

Vehicle dealers and oil companies appoint only registered dealers.

## Applying

The process is set out in our [FBR registration guide](/blogs/fbr-registration-step-by-step).""")

body("blogs/income-tax-filing-kharian.html", """## Serving Soldiers and Officers

Personnel posted to Kharian cantonment receive a salary certificate from their pay office showing basic pay, allowances and tax withheld. Some allowances are exempt and some taxable, and the certificate separates them. Officers who rent out a house elsewhere while living in official accommodation also declare that rent.

## Retired Personnel

Pensions are entered as exempt income. A retired officer who has started a business or receives rent declares those incomes in full.

## Overseas Owners from Norway and Denmark

A Kharian-born owner living in Scandinavia who rents out a house here files a Pakistani return showing that rent. Whether the same income must be reported in Norway or Denmark is a matter for those countries' rules and the relevant tax treaty.

## Returned Migrants with Foreign Pensions

People who have returned after a working life in Scandinavia often draw foreign state or occupational pensions. Their treatment in Pakistan depends on the law and treaty position for the year, which we check before filing.

## Rental Income

Rent is declared with any withholding by company tenants claimed.

## Property Sales

Each sale is reported with price, cost, gain and advance tax paid.

## Wealth Statement

Houses, plots, agricultural land, vehicles, gold and balances, with money from abroad shown as receipts.""")

add("blogs/income-tax-filing-khanewal.html", "## Pensioners\n\nRetired railway and government employees declare their pension as exempt, which keeps their wealth statement consistent with the houses and land they own.")
body("blogs/tax-consultant-khanpur.html", """## Sugar Mills Around Khanpur

The mills near Khanpur crush cane from roughly November to March. For a cane grower, the crop sold to the mill is agricultural income. The questions arise around the edges: the tractor-trolleys that carry cane for neighbours, the labour gangs supplied to the mill yard, and the parts and lubricants sold to the mill workshop. Each of these is a business, and the mill withholds tax from every payment. The rate is lower for anyone on the Active Taxpayers List, so filing pays for itself.

## Ginning Season

Khanpur's ginners buy phutti from August and sell lint to spinning mills, which withhold tax on purchases. The ginner's monthly sales tax returns and annual income tax return should agree.

## The Grain Market

Commission agents in Khanpur's grain market earn commission on wheat and cotton sold for farmers. Loans given to growers before the harvest are receivables on 30 June, not expenses.

## Landowners

Larger landowners pay the Punjab agricultural income tax on crop income. The federal return lists the land and notes the agricultural income as exempt from federal tax.

## Railway Town Employees

Khanpur is an important stop on the main line, and railway staff, teachers and officials have salary tax withheld.

## City Shops

Shops in the main bazaars keep purchase bills and daily sales; restaurants deal with PRA.""")
add("blogs/ntn-registration-khanpur.html", "## Shops in the City\n\nShops that accept wallet and card payments open business accounts after registration.\n\n## Students\n\nStudents and graduates who begin freelancing register with their CNIC so that payments from abroad reach their own accounts.")
add("blogs/income-tax-filing-khanpur.html", """## Shopkeepers in the City

Shops in Khanpur's bazaars show sales, purchases from wholesalers in Rahim Yar Khan and Multan, rent and staff, with stock counted on 30 June. Advance tax charged on commercial electricity bills is claimed.

## Teachers and Railway Staff

Salaried residents copy salary and withholding from their certificates and list the land or house they own.

## Families with Members Abroad

Money sent home from the Gulf through banks is a receipt in the wealth statement.

## Late Filing

A late return is accepted; rejoining the Active Taxpayers List needs the surcharge.""")
add("blogs/tax-consultant-khushab.html", "## Pensioners\n\nRetired soldiers from the district declare pensions as exempt.")
add("blogs/ntn-registration-khushab.html", """## Sweet Shops Selling by Courier

Khushab's dhoda makers who now sell by courier and through online orders need registration details for courier cash-on-delivery accounts and payment gateways.

## Soon Valley Farmers with Side Businesses

Farmers who also run tractor hire or input dealerships register for the business, while their crop income stays agricultural.

## Students

Students of the district's colleges who start earning register with their CNIC.""")
add("blogs/income-tax-filing-khushab.html", """## Sweet Shops

Dhoda and sweet makers show sales, including courier orders, against milk, sugar, ghee, dry fruit, packing, wages and rent.

## Soon Valley Families

Families farming terraced land in the Soon Valley declare their crop as agricultural income; those renting rooms to visitors declare that rent.

## Pensioners

Retired soldiers declare their pension as exempt and list their property.

## Late Filing

Returns can be filed after the deadline, with the surcharge to rejoin the Active Taxpayers List.""")
body("blogs/ntn-registration-khuzdar.html", """## Selling Minerals Down-Country

A Khuzdar lease holder sending chromite or barite to a processor in Hub, or marble blocks to a cutting unit in Karachi, will be asked for an NTN before the buyer's accounts department releases payment. Buyers withhold tax on purchases at a lower rate when the seller is on the Active Taxpayers List, so filing makes a direct difference on every truckload.

## Mining Contractors

Contractors who drill, blast and haul for lease holders register to receive payments by bank and to claim the tax withheld.

## Transporters on the N-25

Truck owners carrying minerals and goods between Khuzdar, Karachi and Quetta register to work for companies that require registered carriers, and to adjust the advance tax paid with their vehicle tokens.

## Contractors for District Departments

Roads, water schemes and school buildings in the Jhalawan region are built by contractors who must be registered; withholding on their bills depends on filer status.

## Engineering Graduates

Graduates of the university in Khuzdar starting jobs or consultancy register with their CNIC to build a tax record.

## Applying

IRIS registration uses a CNIC, a phone number in your own name and an address. Our [FBR registration guide](/blogs/fbr-registration-step-by-step) explains each step.""")
add("blogs/income-tax-filing-kohat.html", "## Cement Plant Employees\n\nStaff of the cement plant have salary tax withheld and may receive housing or transport benefits; the salary certificate shows which are taxable.")
body("blogs/tax-consultant-kot-addu.html", """## Working at the Power Plant

Kot Addu's power plant is one of the larger thermal stations in Pakistan, and its engineers, operators and support staff are paid salaries that often come with company housing, transport and medical cover. The salary certificate separates taxable from exempt items, and a return lets staff claim back any excess withholding, for example after a mid-year promotion.

## The Refinery Nearby

The refinery at Mahmood Kot employs technical staff and engages contractors for maintenance, catering, security and transport. Contractors' bills are withheld at source, at a lower rate for active filers, and providers of services deal with the Punjab Revenue Authority for sales tax on services.

## Cotton Between Two Rivers

The land between the Indus and the Chenab grows cotton, wheat and sugarcane. Ginners in the tehsil sell lint to spinning mills that withhold tax, and their sales tax filings should match their income tax accounts.

## Mangoes

Orchard owners declare their mangoes, or the money paid by a contractor for the crop, as agricultural income. Contractors earn a trading margin after the contract price, picking and freight.

## River Floods

The riverine belt floods in heavy monsoon years. Business stock and equipment lost are written off in the year of loss with evidence.

## Property

Plant and refinery employees buying plots in Multan or Lahore pay lower advance tax as active filers.""")
add("blogs/tax-consultant-kot-momin.html", "## Commuters and Employees\n\nTeachers and officials posted in Kot Momin, and residents working in Sargodha, have salary tax withheld and file to record their land.")
add("blogs/tax-consultant-kot-radha-kishan.html", "## Property Near Lahore\n\nLand towards Lahore has risen in value. Sellers keep the acquisition record, because the date of acquisition decides how the gain is taxed.")
add("blogs/tax-consultant-kotri.html", "## Railway Workers\n\nKotri's railway history means many retired railway employees live in the town; their pensions are exempt but declared.")
add("blogs/ntn-registration-khanpur.html", "## Clinics\n\nDoctors opening clinics register to deal with suppliers and panel payments.")
add("blogs/income-tax-filing-khanpur.html", "## Doctors\n\nDoctors at the tehsil hospital who also practise privately declare salary and clinic fees separately.")
add("blogs/ntn-registration-khushab.html", "## Joharabad Employees\n\nGovernment staff at the district headquarters can register on IRIS to file their own returns and claim refunds.")
add("blogs/income-tax-filing-khushab.html", """## Transporters

Truck owners carrying gram, salt and gypsum show freight against diesel, tyres, repairs and wages, and claim the advance tax paid with their token. A truck bought during the year is depreciated from the date of purchase.

## Bank Profit

Profit on savings accounts has tax withheld by the bank; it is declared and the withholding claimed.""")
add("blogs/ntn-registration-khuzdar.html", "## Livestock Traders\n\nTraders sending sheep and goats to Karachi's markets before Eid increasingly receive payment by bank and register to document their trade.")
add("blogs/income-tax-filing-kohat.html", """## Doctors and Professionals

Doctors at the district hospital who practise privately, and lawyers at the courts, declare salary and professional fees separately, claiming any withholding by institutional clients.

## Transporters Through the Tunnel

Truck and coach owners on the Peshawar-Kohat route show freight and fares against fuel, tolls, repairs and wages.""")
