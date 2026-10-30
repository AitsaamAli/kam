"""Rewrites and local additions for towns F pages below the floor."""

PAGES = {}


def add(rel, text, key="body_more"):
    PAGES.setdefault(rel, {}).setdefault(key, "")
    PAGES[rel][key] += "\n\n" + text


def body(rel, text):
    PAGES.setdefault(rel, {})["body"] = text


body("blogs/income-tax-filing-jaranwala.html", """## Cane Haulage During the Crushing Season

From November to March, tractor-trolleys and trucks from Jaranwala's villages carry cane to the mills. A farmer who hauls his own cane is part of his farming, but one who hauls for neighbours or under a contract with the mill earns freight income. The mill's payment advice shows the freight paid and the tax withheld; the return shows that freight less diesel, driver's wages, tyres, repairs and depreciation of the tractor and trolley. Keeping the mill's weighbridge slips for each trip makes the freight figure easy to prove.

## Power-Loom Sheds

Weavers who work on conversion for Faisalabad processors receive yarn and return grey cloth, so their sales are the conversion charges, not the cloth's value. The return shows those charges against electricity, wages, sizing, repairs and depreciation of the looms. Sheds that buy their own yarn and sell cloth show the full purchase and sale figures instead, and must match their sales tax returns.

## Arhtis in the Grain Market

The commission book is the arhti's main record. Loans given to farmers before wheat harvest are shown as receivables on 30 June, and any interest-free arrangement does not create income.

## Mill Employees and Commuters

Salaried workers copy salary and withholding from their certificates. Those who changed employer during the year add both certificates together.

## Family Land

Wheat, sugarcane and fodder grown on family land are declared as agricultural income, with the land listed in the wealth statement.""")

body("blogs/ntn-registration-jaranwala.html", """## Supplying the Sugar Mills

Every crushing season, Jaranwala's mills sign up hundreds of transporters, labour contractors and parts suppliers. Their accounts departments will not release payments without an NTN, and they withhold tax at a higher rate from anyone not on the Active Taxpayers List. A tractor-trolley owner who registers in October and files his first return is withheld at the lower rate for the whole season.

## Weavers Moving from Conversion to Own Sales

A power-loom owner who only weaves on conversion can manage without much paperwork, but one who wants to buy yarn and sell cloth to processors needs an NTN and then sales tax registration. Processors cannot claim input tax on cloth bought from unregistered weavers, so registration is what opens these orders.

## Arhtis and Flour Mills

Flour mills buying wheat through Jaranwala's arhtis pay by bank transfer. Registration lets the arhti receive those payments in the business name and reduces withholding once he files.

## Families Buying Plots

Buyers in Faisalabad's housing schemes pay lower advance tax at transfer when they are active filers.

## How to Register

Have your CNIC, a SIM in your own name and the address of your shed or shop ready. Our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows each IRIS screen.""")

body("blogs/income-tax-filing-kabirwala.html", """## Ginning Factories on the Khanewal Road

Kabirwala's ginners record each lot of phutti by weight and moisture, because the outturn of lint and seed from a lot decides their margin. Those weighbridge and outturn records, together with sale invoices to spinning mills and oil expellers, are the backbone of the return. Electricity for the gins and presses, seasonal labour and freight are the main costs, and the machinery is depreciated. Mills' withholding on lint purchases is claimed against the final liability, and the figures are reconciled with the monthly sales tax filings before submission.

## Mango Contractors

Contractors usually pay orchard owners for the season's crop in spring, before the fruit sets, and sell from June to August. Their return shows sales to commission agents and exporters against the contract price, picking labour, crates, cold storage and freight. A storm or poor fruit set can turn a season into a loss, which is shown and can generally be carried forward.

## Orchard Owners

Money received from a contractor for your orchard's crop is agricultural income, just like mangoes you sell yourself.

## Arhtis

Commission on wheat and cotton, less shop rent and staff, is income. Loans to growers are receivables.

## Salaried Residents

Teachers, bank staff and officials copy salary and withholding from their certificates.""")

body("blogs/ntn-registration-kabirwala.html", """## Ginners Before the Picking Season

Spinning mills purchasing lint require the ginner's NTN and sales tax registration. Sales tax registration involves biometric verification and a check of the factory's premises and electricity connection, which takes time, so ginners should apply in spring rather than wait for August.

## Mango Contractors Selling to Exporters

Exporters shipping mangoes to the Gulf, Europe and China buy from contractors who can issue invoices and receive bank payments. Registering lets a Kabirwala contractor sell directly to exporters and earn more than through the commission market.

## Seed and Fertiliser Dealers

Companies supplying dealers withhold tax on every supply, at a higher rate for dealers not on the Active Taxpayers List.

## Families Buying Plots in Multan or Khanewal

Filer status lowers the advance tax charged when the plot is transferred.

## Applying

The application is online with a CNIC, phone number and address. Our [FBR registration guide](/blogs/fbr-registration-step-by-step) walks through it.""")

body("blogs/income-tax-filing-kalat.html", """## Orchard Owners and Fruit Traders

Kalat's apple harvest runs from late summer into autumn. Owners selling their own fruit declare agricultural income. Traders who buy the crop on the trees, pick and pack it, store it in cold storage in Quetta and sell in winter show their sales against the orchard price, labour, crates, storage rent and freight. Stored fruit unsold at 30 June is closing stock.

## Mine Lease Holders

Mineral leases in the district produce stone and other minerals sold to buyers in Karachi and Punjab. The return shows tonnage sold, royalty paid to the province, wages, explosives, fuel and the cost of trucks. Tax withheld by buyers is credited.

## Transporters on the National Highway

Truck and coach owners running between Quetta and Karachi show freight and fares less diesel, tyres, repairs and drivers' wages, and claim the advance tax paid with their vehicle tokens.

## Government Employees and Levies

Salary and withholding are copied from certificates.

## Livestock

Flocks raised on family land are part of farming; buying animals to resell is a trading business.

## Wealth Statement

Orchards, land, leases, vehicles, cold storage receipts and bank balances are listed.""")

body("blogs/ntn-registration-kalat.html", """## Fruit Growers Selling to City Wholesalers

Wholesalers and supermarket suppliers in Karachi buying Kalat apples pay by bank transfer and increasingly ask for the seller's NTN. A grower or trader who registers can deal with them directly.

## Mineral Lease Holders

Mining authorities and buyers of minerals expect the lease holder to be registered. Buyers withhold tax at lower rates from active filers.

## Contractors for Roads and Schools

Provincial departments in Kalat require contractors to be registered and check filer status before deciding the withholding rate on bills.

## Transporters

Truck owners carrying fruit and minerals on the N-25 register to deal with companies and to adjust the advance tax paid with their tokens.

## Families Living in Quetta or Karachi

Kalat families who have moved to the cities register using their current address.

## Applying

IRIS registration uses your CNIC, a phone number registered to you and an email. Our [FBR registration guide](/blogs/fbr-registration-step-by-step) covers each step.""")

body("blogs/income-tax-filing-jacobabad.html", """## Rice Millers

A Jacobabad mill buys paddy from October to December and sells rice through the year. The return shows rice, broken rice and bran sold, paddy bought, electricity, labour, sacks and depreciation of the husking and polishing plant. Paddy and rice in the godown on 30 June are closing stock. The mill's sales tax returns, where registered, should match.

## Wholesalers Selling on Credit to Balochistan

Shops in Dera Murad Jamali, Sibi and Usta Muhammad buy from Jacobabad wholesalers on credit and pay after harvest. The wholesaler's return shows sales when made, and amounts unpaid on 30 June as receivables. Bad debts written off after genuine recovery efforts can be claimed under the rules.

## Landowners

Rice and wheat from family land are declared as agricultural income, with Sindh agricultural income tax paid noted for completeness.

## Transporters on the Quetta Road

Freight income is shown less fuel, repairs, wages and depreciation, with vehicle token tax credited.

## Government Employees

Salary and withholding are copied from certificates; property is listed.

## Heavy Electricity Bills

The advance tax charged on commercial and industrial electricity bills during Jacobabad's long summer can be substantial and is claimed.""")

body("blogs/ntn-registration-jacobabad.html", """## Mills Selling to Karachi

Exporters and large rice buyers in Karachi purchase only from registered mills. A Jacobabad mill needs its NTN first and then sales tax registration, which involves verification of the premises.

## Wholesalers and Distributors

Distributors of branded cooking oil, tea, soap and other goods appoint Jacobabad wholesalers to supply Balochistan. They require registered partners, and banks ask for an NTN before opening business accounts with large turnover.

## Transporters

Goods carriers on the N-65 towards Sibi and Quetta register to deal with companies that require registered carriers.

## Government Contractors

District departments check filer status before deciding how much tax to withhold.

## Shops with Card Machines

Shops that want merchant accounts open business accounts after registration.

## Starting

IRIS registration needs a CNIC, a phone number in your name and an address. Our [FBR registration guide](/blogs/fbr-registration-step-by-step) explains the process.""")

add("blogs/ntn-registration-hub.html", "## Scrap Dealers\n\nScrap and waste buyers who purchase from Hub's factories are asked for an NTN, and the tax collected on scrap sales is credited to them only if they are registered.")
add("blogs/income-tax-filing-hub.html", "## Scrap Dealers\n\nDealers buying scrap from factories show purchases, sales to recyclers in Karachi and the tax collected at purchase, which is claimed.\n\n## Workers Who Live in Karachi\n\nA worker living in Orangi or Baldia who works in Hub files one return with his Karachi address; the Hub factory's salary certificate is used as usual.")
add("blogs/ntn-registration-hunza.html", "## Gojal and the Upper Valley\n\nTraders and hotel owners in Gulmit, Passu and Sost register with the same process, using their village address as on the CNIC.")
add("blogs/income-tax-filing-hunza.html", "## Teachers and Health Workers\n\nStaff of schools and hospitals in Hunza run by private institutions have tax withheld by their employers; their returns copy the salary certificate.\n\n## Students Funded by Family\n\nStudents studying down-country whose fees are paid by parents do not need to declare the fees as income.")
add("blogs/tax-consultant-hunza-city.html", "## Apricot Products\n\nShops selling dried apricots, apricot oil and jams made by local women's groups record purchases from those groups.")
add("blogs/tax-consultant-isa-khel.html", "## Kundian and Chashma\n\nResidents working at the power and irrigation projects at Chashma and Kundian have tax withheld from salary and list their land and houses in their wealth statements.")
add("blogs/tax-consultant-jalalpur-pirwala.html", "## Fishermen on the Rivers\n\nFishermen and fish traders on the Chenab and Sutlej sell to markets in Multan. Fishing is not agricultural income, so the trader's profit after boats, nets and transport is business income.")
add("blogs/tax-consultant-jaranwala.html", "## Faisalabad Road Factories\n\nUnits along the Faisalabad road make textiles, food products and building materials. They withhold tax on payments to suppliers, file sales tax returns and must keep their income tax accounts consistent with both.\n\n## Property\n\nFamilies buying plots in Jaranwala or Faisalabad benefit from filer status at transfer.")
add("blogs/tax-consultant-jhang.html", "## Shorkot and Athara Hazari\n\nShorkot's grain market and the riverine land of Athara Hazari have their own traders and farmers, whose records follow the same pattern.")
add("blogs/ntn-registration-jhang.html", "## Shops in Jhang Saddar\n\nCloth and electronics shops in Jhang Saddar and Jhang city that accept card payments need business accounts, opened after registration.")
body("blogs/ntn-registration-jhelum.html", """## Owners Living in Britain

Thousands of Jhelum houses belong to families living in Birmingham, Bradford, Luton and London. An owner who rents out a house or plans to sell can register online with a NICOP and file each year from the UK. Registration alone does not lower tax; a filed return that puts the owner on the Active Taxpayers List does, both for the buyer's advance tax under section 236K and the seller's under section 236C.

## Tenants Who Withhold Tax

When a bank, mobile company or other business rents a building in Jhelum, it withholds tax from the rent. The landlord's NTN and return are needed to claim that deduction.

## Cantonment Contractors

Works and services for the cantonment are given to registered contractors, whose bills are withheld at lower rates if they file.

## GT Road Petrol Pumps and Showrooms

Oil companies and car and motorcycle manufacturers appoint only registered dealers.

## Heirs

When a parent's house is sold, each heir's share is taxed in that heir's hands, so each heir who sells benefits from being a filer.

## Applying

Follow our [FBR registration guide](/blogs/fbr-registration-step-by-step); the process is the same from Jhelum or abroad.""")
add("blogs/income-tax-filing-jhelum.html", "## UK Pensions\n\nResidents who have returned from Britain and draw UK state or private pensions declare them under the rules on foreign income; whether they are taxable in Pakistan depends on the law and treaty position for the year.")
add("blogs/tax-consultant-jhelum-city.html", "## Gold and Jewellery\n\nJewellers in the main bazaar record gold bought, sold and exchanged, and weigh their stock at 30 June.")
add("blogs/tax-consultant-joharabad.html", "## Courts and Lawyers\n\nAdvocates practising at the district courts in Joharabad declare fees less chamber and clerk costs, and claim any tax withheld by institutional clients.")
add("blogs/tax-consultant-kabirwala.html", "## Dairy and Livestock\n\nFamilies keep buffaloes for milk sold to collectors for processors. Small-scale dairy as part of farming is agricultural, while a commercial dairy with purchased feed and hired workers is a business.")
add("blogs/tax-consultant-kalat.html", "## Mangochar and Surab\n\nThe smaller towns of Mangochar and Surab along the highway have shops, restaurants and fuel stations serving travellers. Their records are daily sales and purchase bills from Quetta suppliers.\n\n## Family Members in the Cities\n\nMany Kalat families have members working in Quetta and Karachi whose salaries are taxed by their employers.")
add("blogs/tax-consultant-kalur-kot.html", "## Darya Khan and Bhakkar Links\n\nKalur Kot's traders buy from wholesalers in Bhakkar and Darya Khan and sell to villages along the river. Goods given on credit until harvest are receivables at 30 June.\n\n## Overseas Workers\n\nWorkers in the Gulf who send money home show it as receipts in their families' wealth statements.")

add("blogs/ntn-registration-hunza.html", "## Mountaineering and Trekking Agencies\n\nAgencies organising expeditions to the Karakoram peaks receive fees from foreign climbers by bank transfer and deal with permit authorities; an NTN is part of their paperwork.")
add("blogs/income-tax-filing-hunza.html", "## Rent from Rooms and Shops\n\nFamilies renting rooms to seasonal staff or shops in Aliabad's bazaar should note where that income arises when deciding how it is reported.")
add("blogs/tax-consultant-isa-khel.html", "## Teachers and Health Staff\n\nGovernment teachers and health workers in the tehsil have tax withheld and file to record their property.")
add("blogs/ntn-registration-jacobabad.html", "## Doctors and Clinics\n\nDoctors starting private practice and diagnostic labs register to deal with pharmaceutical suppliers and panel clients who pay by bank.\n\n## Landowners with Businesses\n\nA landowner who sets up a rice mill, petrol pump or fertiliser dealership registers for that business, while his crop income stays agricultural.")
add("blogs/income-tax-filing-jacobabad.html", "## Doctors\n\nDoctors at the civil hospital who also practise privately declare salary and clinic fees separately.")
add("blogs/tax-consultant-jamshoro.html", "## Hostel and Housing Rent\n\nLandlords renting rooms and houses to students and staff near the universities declare that rent as property income.")
add("blogs/tax-consultant-jaranwala.html", "## Teachers and Doctors\n\nSalaried professionals in the town who also tutor or practise privately declare that income separately.")
add("blogs/ntn-registration-jaranwala.html", "## Young Workers Abroad\n\nYoung men from Jaranwala's villages working in the Gulf or Europe can register with their CNIC or NICOP before buying land at home.")
add("blogs/ntn-registration-jhang.html", "## Contractors on Canal and Road Works\n\nIrrigation and road departments in the district require contractors to be registered and active filers to avoid higher withholding.")
add("blogs/ntn-registration-jhelum.html", "## Retired Servicemen\n\nSoldiers retiring from Jhelum cantonment and investing commutation in transport or shops register when the business starts.")
add("blogs/income-tax-filing-jhelum.html", "## Shopkeepers in the Bazaar\n\nTraders show sales, purchases and stock, with advance tax charged on commercial electricity bills claimed.")
add("blogs/tax-consultant-jhelum-city.html", "## Rented Flats in the Newer Schemes\n\nFlats and portions let to families moving into the city are a common investment for overseas owners, whose rent is declared in Pakistan.")
add("blogs/tax-consultant-joharabad.html", "## Mitha Tiwana and Rural Markets\n\nTraders in smaller markets nearby supply villages on credit until harvest, and amounts outstanding at 30 June are receivables.")
add("blogs/tax-consultant-kabirwala.html", "## Teachers and Bank Staff\n\nSalaried residents have tax withheld and file to claim any excess.")
add("blogs/ntn-registration-kabirwala.html", "## Arhtis\n\nArhtis selling wheat to flour mills are withheld at lower rates once they file.\n\n## Overseas Workers\n\nWorkers in the Gulf can register with their CNIC or NICOP and file online.")
add("blogs/tax-consultant-kalat.html", "## Cold Storage in Quetta\n\nFruit traders who store apples in Quetta cold storages pay rent per crate, which is a cost of their trade.")
add("blogs/ntn-registration-kalat.html", "## Orchard Owners Buying Vehicles\n\nPick-ups and trucks used to carry fruit attract lower advance tax at registration when the buyer is an active filer.")
add("blogs/income-tax-filing-kalat.html", "## Families in Quetta\n\nKalat families living in Quetta file using their current address while listing their orchards and land at home.")
add("blogs/tax-consultant-kalur-kot.html", "## Brick Kilns\n\nKilns supplying builders in Bhakkar district show brick sales against coal, clay and labour.")
add("blogs/ntn-registration-jacobabad.html", "## Students and Graduates\n\nYoung people from Jacobabad studying in Sukkur, Larkana or Karachi who begin tutoring or freelancing register with their CNIC so that payments arrive in their own accounts and a tax record begins early.")
add("blogs/tax-consultant-kabirwala.html", "## Property in Khanewal and Multan\n\nFamilies investing harvest income in plots benefit from filer rates at transfer.")
add("blogs/ntn-registration-kabirwala.html", "## Dairy Farms\n\nCommercial dairies selling milk to processors are paid by bank transfer and asked for registration details. A registered dairy can sign a supply contract in its own name and claim the tax the processor withholds.\n\n## Teachers and Officials\n\nSalaried residents can register on IRIS and file their own returns to claim back any excess withholding.")
add("blogs/income-tax-filing-kabirwala.html", "## Late Filers\n\nA return can still be filed after the deadline; rejoining the Active Taxpayers List then needs the surcharge.")
add("blogs/ntn-registration-kalat.html", "## Students\n\nStudents from Kalat at universities in Quetta and Khuzdar who start earning register with their CNIC to build a tax record useful for jobs and scholarships later.")
add("blogs/income-tax-filing-kalat.html", "## Late Filing\n\nA late return is still accepted, with the surcharge needed to rejoin the Active Taxpayers List.")
add("blogs/tax-consultant-kalur-kot.html", "## Property\n\nLand purchases attract lower advance tax for active filers.")
add("blogs/ntn-registration-kalat.html", "Women running embroidery businesses can also register under their own CNIC.")
