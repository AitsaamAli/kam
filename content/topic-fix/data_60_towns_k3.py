"""Rewrites and local additions for towns K pages."""

PAGES = {}


def add(rel, text, key="body_more"):
    PAGES.setdefault(rel, {}).setdefault(key, "")
    PAGES[rel][key] += "\n\n" + text


def body(rel, text):
    PAGES.setdefault(rel, {})["body"] = text


body("blogs/income-tax-filing-mirpur.html", """## The Usual Entries for a Mirpuri Household

A Mirpur family's FBR return is often shorter than people fear. The common entries are rent from a flat or house in Rawalpindi, Islamabad or Gujar Khan; profit on savings held in a bank branch in Pakistan proper; and, in a year when property in Pakistan proper is sold, the sale itself. Income that arises in Mirpur, such as rent from a shop on Allama Iqbal Road or profit from a business in the city, is reported to Azad Kashmir's tax office rather than to FBR.

## Houses Funded from Bradford and Birmingham

The large houses around Mirpur, Dadyal and Chakswari are mostly built with money sent from the UK. FBR's wealth statement asks who owns each asset and where the money came from. If a father in Mirpur owns the house, it is his asset and his sons' transfers are his receipts. If a son living in Britain owns it, it belongs in the son's own Pakistani return, not the father's. Mixing these up is the most common reason Mirpuri families receive questions about their wealth statements.

## Land Lost Under Mangla Lake

Families whose land went under the lake when the dam was raised received compensation and new plots. Compensation for land taken compulsorily is treated differently from a voluntary sale, and the plots received are shown at their recorded value.

## Selling a Plot in Pakistan Proper

The seller pays advance tax under section 236C at transfer; the return shows the sale price, original cost and gain.

## Consistency with AJK's Office

What is shown to AJK's tax office and to FBR about the same assets should match.""")

body("blogs/income-tax-filing-muzaffarabad.html", """## A Civil Servant with a Flat in Islamabad

A typical Muzaffarabad case: an officer of the AJK government, salaried and taxed under AJK's system, who has bought a flat in an Islamabad housing scheme and rents it out. The rent is income from Pakistan proper and goes in an FBR return. Expenses allowed against rent under the law for the year are deducted, and any tax withheld by a company tenant is claimed. The salary itself is mentioned only so that the wealth statement balances.

## Doctors and Engineers Paid from Pakistan Proper

Professionals employed by federal bodies, NGOs or companies headquartered in Islamabad copy their salary certificate into the FBR return and claim the tax withheld.

## Contractors After the Earthquake and on Hydropower Projects

Contractors paid by federal agencies or Pakistani companies list each payment, the tax withheld and their costs of labour, materials and machinery.

## Grants for Rebuilding

Reconstruction grants received after the 2005 earthquake, and any later disaster assistance, are receipts rather than income.

## The Wealth Statement

The house in Muzaffarabad, land in the villages up the Neelum or Jhelum valleys and the flat in Islamabad are all listed.

## Filing Late

A late FBR return is still accepted, but the surcharge is needed to appear on the Active Taxpayers List.""")

body("blogs/tax-consultant-muridke.html", """## Between Two Cities

Muridke sits almost exactly between Lahore and Gujranwala on the GT Road, close enough to Lahore's Shahdara for daily commuting and to Gujranwala's engineering trade for a steady flow of subcontract work. Its tax questions reflect that position.

## Subcontractors to Gujranwala's Engineering Firms

Small workshops in Muridke machine parts, cast components and fabricate assemblies for larger manufacturers in Gujranwala and Lahore. When their customers are registered for sales tax, they prefer suppliers who are too, because they can then claim input tax. A workshop's income tax return shows job charges or sales against steel, power, wages and depreciation of lathes and machines.

## Industrial Units on Nangal Sahdan Road

Units making food products, plastics and textiles in the industrial pockets around Muridke file monthly sales tax returns and withholding statements, which must match their annual accounts.

## Rice Husking

Paddy from the surrounding villages is husked in local mills and sold to traders in Kamoke and Lahore.

## Workers Commuting to Shahdara

Factory workers and office staff travelling to Lahore have salary tax withheld; a return claims any excess.

## Families Renting Out Portions

Owners renting portions of houses to workers declare rent as property income.

## Land Along the GT Road

When land is sold to developers, the acquisition date decides how the gain is taxed.""")

body("blogs/ntn-registration-mirpurkhas.html", """## Exporting Sindhri Mangoes

Mirpurkhas's Sindhri mango is one of Pakistan's best-known export varieties. An exporter needs an NTN for customs clearance, for the bank that receives foreign proceeds and for the quarantine and plant protection paperwork. Growers who want to export directly rather than through Karachi exporters therefore have to register first.

## Contractors Supplying Exporters and Supermarkets

Contractors who buy orchards and supply exporters, supermarket chains and corporate gift orders are paid by bank transfer, and those buyers ask for registration details. A registered contractor who files is withheld at a lower rate.

## The Mango Festival

Growers and contractors selling to visitors and corporate buyers at the annual festival increasingly accept card and bank payments.

## Sugar Mill Transporters

Mills register haulage and labour contractors before the crushing season.

## Red Chilli Traders

Chilli from Kunri and the surrounding area is sold to spice companies in Karachi, which pay suppliers by bank and ask for an NTN.

## Getting Registered

Registration is free and online with a CNIC and a mobile number in your name; our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows each IRIS screen.""")

body("blogs/income-tax-filing-mirpurkhas.html", """## Orchard Owners and the Sindh Agricultural Tax

Mango income from family orchards is outside federal income tax. Owners of larger holdings pay Sindh's agricultural income tax, and the federal return notes the agricultural income as exempt so that the wealth statement balances.

## A Mango Contractor's Season

Contractors usually pay orchard owners in instalments between flowering and harvest, then sell from May to August. The return shows sales to commission agents in Karachi, to exporters and at the festival, against the contract price, picking labour, crates, packing, cold storage and freight. A storm at flowering or a fall in export demand can cause a loss, which is shown and can generally be carried forward against later business profit.

## Exporters

Export proceeds received through banks and the tax collected on them are listed. Depending on the regime, the tax may be final.

## Sugar Mill Haulers

Freight from the mill, less diesel, wages and repairs, with the mill's withholding claimed.

## Chilli and Cotton Traders

Purchases from growers, sales to companies and stock on 30 June.

## Government Employees

Salary and withholding are copied from the certificate.""")

body("blogs/ntn-registration-muzaffargarh.html", """## Vendors at the Power Station

The thermal power station's procurement office keeps a vendor list for transport, scaffolding, cleaning, security and spare parts. Joining it requires an FBR NTN, a bank account in the vendor's own name and, for services, PRA registration. The station withholds income tax on every bill, at a lower rate for vendors who have filed.

## Contractors at the Mahmood Kot Refinery

The refinery's contractors and their subcontractors face the same requirements and are increasingly audited for documentation.

## Ginners in Alipur, Jatoi and Muzaffargarh

Spinning mills buy lint only from ginners with an NTN and sales tax registration.

## Mango and Date Traders

Muzaffargarh's mangoes and dates are bought by exporters and supermarket suppliers who pay by bank and want registered sellers.

## Boat and Fishing Operators on the Rivers

Fish traders on the Chenab and Indus selling to Multan's markets register to receive bank payments.

## Applying

Registration is free and online with a CNIC; our [FBR registration guide](/blogs/fbr-registration-step-by-step) has each screen.""")

body("blogs/income-tax-filing-muzaffargarh.html", """## Engineers and Staff at the Power Station and Refinery

Employees' salary certificates show basic pay, allowances, the value of company housing and transport where taxable, and tax withheld. Engineers who receive shift allowances or bonuses late in the year often have too much withheld; the return is the way to claim it back.

## Contractors and Vendors

The return lists every bill paid by the power station or refinery, the income tax withheld and the costs of the work: wages, materials, vehicle running and depreciation of equipment. PRA tax charged on services is collected for the province and is not income.

## Ginners

Lint and cottonseed sales, seed cotton purchases, power, labour and depreciation, reconciled with monthly sales tax returns.

## Mango Contractors

Sales against contract prices, picking, crates and freight; losses carried forward where they arise.

## Farm Families Between the Rivers

Cotton, cane, wheat and mangoes from family land are agricultural income.

## Flood Years

Business stock or equipment lost in a flood is written off with evidence; houses lost are removed from the wealth statement with a note.""")

body("blogs/tax-consultant-muzaffargarh-city.html", """## Courts, Hospital and Offices

Muzaffargarh city is the district's administrative centre. Its district courts, the hospital, the education and revenue offices and the police lines employ a large share of its salaried residents. Their salary certificates show tax withheld; a return claims any excess and records property in the city and in their villages.

## Lawyers at the District Courts

Advocates' fees, less chamber rent, clerks' pay and travel, are taxable. Banks and companies that hire them withhold tax on fees, which is claimed.

## Doctors with Evening Clinics

Doctors at the district hospital who run clinics on the Multan road in the evenings declare clinic fees as business income, separately from salary.

## Wholesale Trade

Wholesalers supplying grocery, cloth and building materials to Alipur, Jatoi and the riverine villages sell on credit until harvest. Their khata books, distributors' invoices and the stock count on 30 June are the core records.

## Private Schools

Schools in the city keep fee registers and salary sheets.

## Coaches to Multan

Transport operators keep fare and fuel records and claim token tax.""")

body("blogs/tax-consultant-narowal.html", """## A Border District with a Pilgrim Corridor

Narowal sits in the north-eastern corner of Punjab, bounded by the Ravi and the border with India. Since the Kartarpur corridor opened, Sikh pilgrims cross daily to visit Gurdwara Darbar Sahib, where Guru Nanak spent his final years. The corridor has created work in transport, catering and supplies around Kartarpur, and businesses there should keep records from the beginning rather than trying to reconstruct them later.

## Basmati Country

Narowal, Shakargarh and Zafarwal are part of the basmati belt. Paddy from family land is agricultural income. Husking mills and rice traders earn business income, and exporters in Lahore buying from them require registration and proper invoices.

## University and Colleges

Teachers at the University of Narowal and the district's colleges have salary tax withheld; examining and consultancy fees are declared separately.

## Families in Europe and the Gulf

Many households have members in Spain, Italy and the Gulf. Money sent through banks is a receipt in the wealth statement of the person who receives it.

## Shops and Wholesalers

Traders buy from Sialkot and Lahore and keep supplier bills and daily sales.

## Government Employees

District and border-area staff have salary tax withheld.""")

body("blogs/ntn-registration-narowal.html", """## Rice Mills Supplying Lahore's Exporters

Basmati exporters in Lahore buy from mills in Narowal, Shakargarh and Zafarwal only when the mill is registered for income tax and sales tax, because they need proper invoices for their own refunds and records. The NTN comes first, then the sales tax application, which involves verification of the mill and its electricity connection.

## Businesses Serving Kartarpur Visitors

Transport operators, caterers and shops that serve visitors around the corridor and want to accept card or bank payments need business accounts, opened after registration.

## Teachers Earning Consultancy Fees

University and college teachers receiving fees with tax withheld register on IRIS to claim it.

## Relatives in Europe Buying at Home

Narowal families' relatives in Spain and Italy can register with a NICOP and file online so that plots bought at home are transferred at the filer rate.

## Young People Applying for Visas

A filed return is often used as evidence of income in visa applications.

## Registering

Registration is free and online; our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows each step.""")

body("blogs/income-tax-filing-narowal.html", """## Rice Growers

Paddy grown on family land in Narowal, Shakargarh and Zafarwal is agricultural income, outside federal tax. Land leased out for cash rent also produces agricultural income for the owner.

## Husking Mills and Rice Traders

The return shows rice, broken rice and bran sold, paddy bought, electricity, labour, sacks and depreciation of machinery, with paddy and rice on hand on 30 June counted as stock. Exporters' withholding is claimed, and figures are reconciled with sales tax returns.

## Corridor Businesses

Income from transport, catering or shops serving visitors to Kartarpur, less purchases, wages and rent.

## University Staff

Salary and withholding are copied from certificates, with consultancy and examining fees added separately.

## Families Receiving Money from Abroad

Transfers from relatives in Europe or the Gulf are receipts shown in the wealth statement, together with the houses or land they pay for.

## Shopkeepers

Sales, purchases from Sialkot and Lahore and stock on 30 June.""")
PAGES["blogs/income-tax-filing-narowal.html"]["desc"] = "Income tax return filing in Narowal for rice growers, mills, Kartarpur corridor businesses, university staff and remittance families."

add("blogs/income-tax-filing-mingora.html", "## Saidu Sharif Officials and Doctors\n\nStaff of the divisional offices and the teaching hospital copy their salary certificates; doctors with private clinics in Mingora declare clinic fees separately.")
add("blogs/tax-consultant-mirpurkhas.html", "## Thar Coal and the Road North\n\nThe road to the Thar coalfield passes through Mirpurkhas, and transporters and suppliers serving the coal projects are paid with tax withheld.")
add("blogs/tax-consultant-moro.html", "## Moro's Grain Market\n\nCommission agents dealing in wheat and cotton for farmers from Moro and Kandiaro earn commission, with advances to growers shown as receivables.\n\n## Railway and Bus Connections\n\nCoach operators running to Karachi and Sukkur keep fare and fuel records.")
add("blogs/ntn-registration-muzaffarabad.html", "## Neelum Valley Guest Houses\n\nGuest houses in Keran, Sharda and Kel taking bookings from tour companies in Islamabad are increasingly paid by bank.")
add("blogs/tax-consultant-muzaffargarh.html", "## Rangpur and Alipur\n\nThe district's tehsil towns have their own grain markets and ginners whose records follow the same pattern.")
add("blogs/tax-consultant-nankana-sahib.html", "## Shahkot and Sangla Hill\n\nThe district's other towns have rice mills, grain markets and shops whose owners keep similar records.\n\n## Overseas Families\n\nMany families have members in the Gulf and Europe; remittances are receipts in the wealth statement.")

add("blogs/income-tax-filing-mingora.html", "## Late Filing\n\nA Swat return filed after the deadline is still accepted; rejoining the Active Taxpayers List needs the surcharge.")
add("blogs/ntn-registration-mirpurkhas.html", "## Families Buying in Hyderabad and Karachi\n\nMirpurkhas families investing in flats in Hyderabad's Qasimabad or in Karachi pay lower advance tax at transfer when they are active filers, so registering and filing before the purchase saves money.\n\n## Teachers and Officials\n\nSalaried residents can register on IRIS and file their own returns.")
add("blogs/income-tax-filing-mirpurkhas.html", "## Traders Supplying Thar\n\nWholesalers selling to shops in Mithi, Islamkot and Chachro on credit show those sales when made, with amounts unpaid on 30 June as receivables.")
add("blogs/tax-consultant-moro.html", "## Overseas Workers\n\nWorkers from Moro's villages in the Gulf can file online to secure filer rates on property at home.")
add("blogs/tax-consultant-muzaffarabad.html", "## Property in Islamabad\n\nOfficials buying flats in Islamabad pay lower advance tax with FBR filer status.")
add("blogs/ntn-registration-muzaffarabad.html", "## Students\n\nStudents from Muzaffarabad studying in Islamabad or Lahore who begin earning register with their CNIC.")
add("blogs/income-tax-filing-muzaffarabad.html", "Bank profit earned in Pakistan proper is declared with the bank's withholding.")
add("blogs/tax-consultant-muzaffargarh.html", "## Property\n\nPlots in Muzaffargarh and Multan cost less in advance tax for active filers.")
add("blogs/ntn-registration-muzaffargarh.html", "## Shops and Clinics in the City\n\nRetailers, pharmacies and clinics that accept card payments need a business account, opened after registration.\n\n## Gulf Workers\n\nWorkers from the district abroad can register with a NICOP and file online so that land bought at home is transferred at the filer rate.")
add("blogs/income-tax-filing-muzaffargarh.html", "## Traders and Shops\n\nShopkeepers in Muzaffargarh city and the tehsil towns show sales, purchases from Multan wholesalers and stock on 30 June, claiming the advance tax charged on commercial electricity bills.\n\n## Remittances\n\nMoney from relatives abroad is shown as receipts.")
add("blogs/tax-consultant-muzaffargarh-city.html", "## Landlords\n\nOwners renting shops on the Multan road declare rent as property income, with bank tenants' withholding claimed.")
add("blogs/tax-consultant-nankana-sahib.html", "Their income is declared only where they own Pakistani property or earn here.")
add("blogs/tax-consultant-narowal.html", "## Property\n\nPlots in Narowal's new schemes cost less in advance tax for active filers.")
add("blogs/ntn-registration-narowal.html", "## Shops in Shakargarh and Zafarwal\n\nRetailers in the district's other towns open business accounts after registration to accept card and wallet payments.\n\n## Contractors on Border Roads\n\nDepartments building roads in the border areas require registered contractors.")
add("blogs/income-tax-filing-narowal.html", "## Government Employees\n\nDistrict staff copy salary and withholding from their certificates and list the land they own.\n\n## Transporters\n\nTruck owners carrying paddy to mills and rice to Lahore show freight against diesel, repairs and wages, claiming the token tax.\n\n## Late Filing\n\nA late return is accepted, with the surcharge to rejoin the Active Taxpayers List.")
add("blogs/income-tax-filing-mirpurkhas.html", "Bad debts written off after real recovery efforts can be claimed under the rules.")
add("blogs/tax-consultant-moro.html", "## Sugar Mill Employees\n\nStaff of the district's mills have salary tax withheld, and seasonal workers who want filer status can still file a return even if no tax is due.")
add("blogs/ntn-registration-muzaffarabad.html", "A filed return also helps with scholarship and visa applications.")
add("blogs/ntn-registration-muzaffargarh.html", "Filing the first return completes the process.")
add("blogs/income-tax-filing-muzaffargarh.html", "Late returns are accepted with the surcharge.")
add("blogs/tax-consultant-muzaffargarh-city.html", "Banks deduct tax from the rent they pay.")
add("blogs/tax-consultant-nankana-sahib.html", "## Gurdwara Visitors and Guest Houses\n\nGuest houses and families renting rooms to pilgrims during festivals receive rent that is income, even if earned only a few weeks a year.")
add("blogs/tax-consultant-narowal.html", "Sellers keep acquisition records.")
add("blogs/ntn-registration-narowal.html", "## Students at the University\n\nStudents who begin freelancing register with their CNIC so payments reach their own accounts.")
add("blogs/income-tax-filing-narowal.html", "## Pensioners\n\nRetired soldiers and teachers declare their pension as exempt and list their land and house.")
add("blogs/ntn-registration-muzaffarabad.html", "It costs nothing to register.")
add("blogs/ntn-registration-muzaffargarh.html", "After that, file every year to stay on the list.")
add("blogs/income-tax-filing-muzaffargarh.html", "Notices on IRIS should be checked regularly.")
add("blogs/tax-consultant-muzaffargarh-city.html", "That deduction is claimed in the landlord's return.")
add("blogs/tax-consultant-narowal.html", "The acquisition date decides how the gain is taxed.")
add("blogs/ntn-registration-narowal.html", "Registration is free.")
add("blogs/income-tax-filing-narowal.html", "Bank profit on their savings is declared with the bank's withholding.")
