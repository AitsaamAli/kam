"""Rewrites and local additions for towns J pages."""

PAGES = {}


def add(rel, text, key="body_more"):
    PAGES.setdefault(rel, {}).setdefault(key, "")
    PAGES[rel][key] += "\n\n" + text


def body(rel, text):
    PAGES.setdefault(rel, {})["body"] = text


body("blogs/tax-consultant-mansehra-city.html", """## Abbottabad Road and the Kashmir Road Markets

Mansehra city grew where the Karakoram Highway meets the road towards Muzaffarabad, and its markets still reflect that crossing. Wholesalers here send flour, ghee, cement and roofing sheets up the Kaghan valley, towards Batagram and Kohistan, and across to Garhi Habibullah. Valley shopkeepers usually settle their accounts after the tourist season or the maize harvest, so a Mansehra wholesaler's books carry large balances owed by customers at the end of June. Those balances are receivables in the wealth statement, and the khata in which each customer's account is kept is the most important record the business has.

## Building Materials After the Earthquake

Reconstruction after the 2005 earthquake created a lasting trade in cement, steel and timber. Dealers selling to government-funded projects and contractors often have tax withheld at the point of payment and claim it in their returns.

## Doctors at King Abdullah Teaching Hospital

Doctors employed at the district's teaching hospital have salary tax withheld; their evening clinics in the city are a separate business whose fees and costs are declared alongside.

## Coaches to Rawalpindi and Naran

Transport companies running daily coaches to Rawalpindi and seasonal services to Naran keep ticket records and fuel bills; the advance tax paid with each vehicle's token is claimed.

## Hazara University Staff Living in the City

Faculty who rent homes in the city and own land in their villages list both in their wealth statements.""")

body("blogs/ntn-registration-mardan.html", """## Supplying Mardan's Sugar Mills

Each autumn, Mardan's mills sign up tractor-trolley owners, truck operators and labour gangs for the crushing season. The mill's cane office asks every contractor for an FBR NTN, and its accounts department withholds income tax from each payment. A contractor who has filed a return for the latest year is on the Active Taxpayers List and is withheld at the lower rate, so registering in September rather than December makes a difference across the whole season.

## Gur Sellers Moving to Bank Payments

Mardan's gur goes to Peshawar, Lahore and Faisalabad. Buyers in Punjab who pay by bank transfer increasingly ask for the seller's NTN so that their own purchase records are complete.

## Tobacco Growers with Side Businesses

A tobacco grower who also runs a curing barn for neighbours or hauls leaf to the company's depot earns business income from those services, and registration lets him receive those payments in his own account.

## Shops in Saddar and Bank Road

Retailers that want card machines or wallet merchant accounts need a business account, opened after registration.

## Teachers at Abdul Wali Khan University

Faculty receiving consultancy or examining fees with tax withheld register on IRIS to file and claim it.

## Registering

Registration is free and online. You will need your CNIC and a mobile SIM registered in your own name; our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows each screen.""")

body("blogs/income-tax-filing-mardan.html", """## Cane Growers and Their Mill Receipts

A Mardan grower's cane is delivered to the mill on a permit and paid for by cheque or bank transfer, sometimes months later. The cane income is agricultural and outside federal tax; the return simply declares it as exempt so that the wealth statement balances. Amounts the mill still owes on 30 June are shown as a receivable.

## Families Who Make Gur

Crushing your own cane in a belna and selling the gur is generally treated as part of farming. A family that also buys cane from neighbours to keep the belna running is partly trading, and that part produces business income after the price paid for cane, fuel and labour.

## Contractors Working for the Mills

Haulage and labour contractors list each mill payment and the tax withheld, then deduct diesel, drivers' and labourers' wages, repairs and depreciation of tractors and trolleys.

## Cantonment Personnel

Serving soldiers at Mardan cantonment copy their pay certificate; pensioners declare their pension as exempt.

## Traders in the City

Shopkeepers in Saddar and the main bazaar show sales, purchases from Peshawar wholesalers and stock at 30 June.

## Remittances from the Gulf

Money from family members in Saudi Arabia and the UAE is shown as a receipt in the wealth statement of the person who receives it.""")

body("blogs/ntn-registration-mastung.html", """## Apple and Grape Growers Selling to Karachi

Mastung's growers increasingly send their fruit directly to commission agents in Karachi's Sabzi Mandi rather than selling the whole orchard on the tree. The commission agent pays by bank transfer after the sale, and many now ask for the grower's NTN. The fruit income itself remains agricultural; registration simply makes the payments easier and keeps them in the grower's own account.

## Contractors Who Buy Orchards

Contractors who buy a whole orchard's crop in spring and pick, pack and send it to market are traders, and they need an NTN for invoices and bank accounts.

## Employees Commuting to Quetta

Government and private employees who travel daily to Quetta can register on IRIS to file their own returns and claim back any excess withholding.

## Highway Fuel Stations and Restaurants

Oil companies appoint only registered dealers, and restaurant owners need registration with the Balochistan Revenue Authority as well as FBR.

## Families Buying Plots in Quetta

The buyer's advance tax is charged at the lower filer rate only if the buyer has filed a return before the transfer.

## Getting Registered

Registration is free and online; our [FBR registration guide](/blogs/fbr-registration-step-by-step) explains the IRIS process.""")

body("blogs/income-tax-filing-mastung.html", """## Growers Who Sell Through Commission Agents

When a Mastung grower sends apples to a commission agent in Karachi, the agent deducts commission, labour and freight and pays the balance. The grower's return declares the net amount as agricultural income; the agent's sale slips are the evidence.

## Orchard Contractors

A contractor's return shows sales against the price paid to orchard owners in spring, picking and packing labour, wooden crates, cold storage rent in Quetta and truck freight. Apples still in cold storage on 30 June are closing stock at cost.

## Tubewell and Solar Investments

Solar pumps bought for orchards, often on bank financing, are listed in the wealth statement with the loan as a liability. Water sold to neighbours is business income.

## Salaried Commuters

Employees working in Quetta copy their salary certificate and list their land and orchard in Mastung.

## Highway Restaurants

Daily sales against food purchases, wages and rent; provincial services tax collected is paid over and is not income.

## Late Returns

A return can still be filed after the deadline, with the surcharge to rejoin the Active Taxpayers List.""")

body("blogs/ntn-registration-matiari.html", """## Ajrak and Tile Workshops in Hala

Hala's family workshops have sold ajrak, kashi tiles and lacquered woodwork for generations, mostly for cash to visitors and to shops in Hyderabad and Karachi. As more sales move to online stores, Instagram shops and export orders, payment gateways and marketplaces ask for registration details before releasing money. A workshop that registers can receive those payments in an account in its own name.

## Selling to Design Stores and Exporters

Design stores in Karachi and Lahore, and exporters sending Sindhi crafts abroad, prefer registered suppliers who can issue invoices. Exporters themselves need an NTN for customs and for the bank to receive proceeds.

## Shops and Guest Houses at Bhit Shah

Businesses serving visitors to the shrine register with FBR and with the Sindh Revenue Authority for services.

## Banana and Cane Traders

Traders who buy crops in Matiari and sell to buyers in Karachi or Punjab register to be paid by bank.

## Employees at Power Facilities

Salaried staff can register on IRIS and file their own returns.

## Registering

Registration is free and online with a CNIC and a mobile number in your name. Our [FBR registration guide](/blogs/fbr-registration-step-by-step) covers the steps.""")

body("blogs/tax-consultant-mian-channu.html", """## Tulamba and the Old Highway Town

Mian Channu grew around a railway station and the grand trunk route between Lahore and Multan, a few miles from the ancient fort mound at Tulamba. Today the N-5 carries a constant flow of trucks and buses past the town, and much of the town's business serves that traffic: truck stops, tyre shops, puncture and repair workshops, diesel stations and dhabas that open through the night. These businesses take most of their income in cash. A simple daily sales note, regular bank deposits and the invoices from tyre and parts suppliers are what turn that cash into a profit figure that FBR will accept.

## Dairy Collection

Milk from villages around Mian Channu is gathered by collection centres for processors. Collection centre operators earn a margin or commission on milk they gather, which is business income; processors withhold tax on their payments.

## Ginning and the Grain Market

Ginners sell lint to spinning mills and claim the mills' withholding; arhtis earn commission on wheat and cotton sold for growers.

## Families Farming Canal Land

Cotton and wheat from family land are agricultural income.

## Employees

Teachers, bank staff and officials have salary tax withheld and file to claim excess deductions.""")

body("blogs/ntn-registration-mian-channu.html", """## Truck Stops and Tyre Dealers on the N-5

Tyre companies, lubricant brands and oil marketing companies appoint dealers only after checking their NTN, and they withhold tax on commissions and supplies. A Mian Channu tyre shop or diesel station that wants a direct dealership has to register first.

## Milk Collection Centres

Processors pay collection centre operators by bank transfer and withhold tax. A registered operator who files is withheld at the lower rate and can sign the collection agreement in his own name.

## Ginners Before Picking

Spinning mills will buy lint only from ginners with an NTN and a sales tax registration number. The sales tax application requires biometric verification and a check of the factory, so it should start in spring.

## Commission Agents

Flour mills buying wheat through arhtis pay through banks and withhold tax.

## Young People from Tulamba and Surrounding Villages

Students and graduates who start online work register with their CNIC so that payments reach their own accounts.

## How to Apply

Registration is free and online. Our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows the IRIS screens.""")

body("blogs/income-tax-filing-mian-channu.html", """## Truck Stop and Workshop Owners

A dhaba or tyre shop on the N-5 shows daily takings, purchases of food, tyres and parts, wages for the night shift, rent and electricity. Many of these businesses run twenty-four hours, so electricity is a large cost and the advance tax charged on commercial bills is a substantial credit. PRA tax collected from restaurant customers is paid over to the province and is not income.

## Milk Collection Centre Operators

The return shows milk bought from farmers, milk sold to the processor, chilling costs, staff and transport. The processor's withholding statement is listed and claimed.

## Ginners

Lint and seed sales, seed cotton purchases, power, labour and depreciation, reconciled with sales tax returns.

## Arhtis

Commission less shop costs, with advances to farmers as receivables.

## Farmers

Crops from family land are agricultural income.

## Salaried Residents

Salary and withholding from certificates, with land and houses listed.

## Wealth Statement

All assets and liabilities at 30 June, with the year's change explained.""")

body("blogs/tax-consultant-mehrabpur.html", """## A Railway Town Among Orchards

Mehrabpur grew around its station on the main line between Karachi and Lahore, and many families still have a member who works, or worked, for Pakistan Railways. Around the town, the land of Naushahro Feroze district is planted with bananas, mangoes, sugarcane and cotton.

## Banana Growers and Contractors

Bananas are harvested almost year-round and sent by truck to Karachi and Punjab. Growers selling their own crop earn agricultural income. Contractors who buy standing crops, cut, pack and transport them are traders whose margin is business income.

## Mango Orchards

Mangoes from family orchards are agricultural income; money received from a contractor for the season's crop is too.

## Sugar Mill Suppliers

Transporters and labour contractors working for mills in the district are paid with income tax withheld, at a lower rate if they have filed.

## Railway Staff and Pensioners

Serving railway staff have tax withheld; pensions are generally exempt but are declared.

## Shops and Restaurants

Shops near the station keep supplier bills and daily sales; restaurants deal with the Sindh Revenue Authority.

## Larger Landholders

Larger holdings pay Sindh agricultural income tax, noted in the federal return for completeness.""")

body("blogs/ntn-registration-mansehra.html", """## Naran and Kaghan Hotels Before the Season Opens

The road to Naran usually opens in late spring, and the first bookings arrive weeks before that. Online booking platforms, travel agencies in Lahore and Islamabad, and companies sending staff on retreats pay by bank transfer and ask the hotel for its NTN. A hotel that registers with FBR and with KPRA in March or April is ready for those payments; one that waits often finds its first payouts held.

## Tour Operators in Balakot

Operators offering trips to Saiful Muluk, Lalazar and Babusar need registration to issue invoices and open business accounts.

## Contractors on Valley Roads

Departments maintaining the valley roads and rebuilding after floods require registered contractors.

## Timber and Furniture

Timber traders and furniture makers selling to Punjab need an NTN to issue invoices.

## Tea Growers Near Shinkiari

Growers supplying tea leaf to processors are increasingly paid by bank.

## Registering

Registration is free and online; see our [FBR registration guide](/blogs/fbr-registration-step-by-step).""")

body("blogs/income-tax-filing-mansehra.html", """## A Naran Hotel's Year

A hotel in Naran may earn almost its whole year's income between May and September and then close for winter. The return covers the full tax year from July to June, so the summer season straddles two returns. Room and food income is recorded month by month from the room register and booking platform statements. Costs include staff wages, food purchases, generator fuel, maintenance and, if the building is leased, rent to its owner. Buildings and furniture owned are depreciated. The KPRA tax charged to guests is paid over and is not income.

## Advances Taken in June

Bookings paid in June for July stays are advances on 30 June and become income in the next year, when guests stay.

## Tour Operators

Package fees less payments to hotels, drivers and guides, with vehicles depreciated.

## Traders in Mansehra and Balakot

Purchases, sales and stock, with advance tax on electricity bills claimed.

## University and Government Staff

Salary and withholding from certificates.

## Families with Members Abroad

Remittances received through banks are shown as receipts in the wealth statement.""")

add("blogs/income-tax-filing-malakwal.html", "## Gifts at Weddings\n\nGold and cash given by relatives abroad at weddings are generally not income but belong in the recipient's wealth statement with a note of who gave them.")
add("blogs/ntn-registration-mandi-bahauddin.html", "## Students and Graduates\n\nYoung people preparing to study in Europe often need a tax record for their visa file; registering and filing builds one.")
add("blogs/tax-consultant-mandi-bahauddin-city.html", "## Rent from City Shops\n\nShop owners on Phalia Road and in the main bazaar declare rent as property income, with tenant withholding claimed.\n\n## Building Material Dealers\n\nCement and steel dealers supplying the many houses being built with money from abroad record sales to contractors and families.")
add("blogs/tax-consultant-mankera.html", "## The Fort and Visitors\n\nA few shops and eateries near the old fort serve visitors; their income is small but should be recorded.")
add("blogs/tax-consultant-mansehra.html", "## Tea Near Shinkiari\n\nTea leaf grown in the Shinkiari area and sold to processors is agricultural income for the grower.")
add("blogs/tax-consultant-mardan.html", "## Takht-i-Bahi Visitors\n\nGuides, shops and eateries near the Takht-i-Bahi ruins serve visitors and keep simple records.")
add("blogs/tax-consultant-mastung.html", "## Karez Water Rights\n\nShares in karez water passed down through families are part of farming and are not separately taxed.")
add("blogs/tax-consultant-matiari.html", "## Saeedabad and Highway Towns\n\nShops and workshops in Saeedabad and along the highway keep supplier bills and daily sales.")
add("blogs/tax-consultant-mianwali.html", "## Namal and Education\n\nTeachers and staff at colleges and the university near Namal lake have tax withheld from salary.")

add("blogs/ntn-registration-mansehra.html", "## Overseas Workers from the Valleys\n\nMany young men from Kaghan, Balakot and Oghi work in the Gulf. They can register with a NICOP and file online, so that land or a house bought at home is transferred at the filer rate.\n\n## Students at Hazara University\n\nStudents who start freelancing register with their CNIC.")
add("blogs/income-tax-filing-mansehra.html", "## Hotel Buildings Leased from Landowners\n\nMany Naran hotels operate in buildings leased from local landowners. The lease rent is a cost for the operator and property income for the owner, who declares it in his own return.\n\n## Late Filing\n\nA late return is accepted with the surcharge needed to rejoin the Active Taxpayers List.")
add("blogs/tax-consultant-mardan.html", "Their entry fees and souvenir sales are small but should still be recorded.")
add("blogs/income-tax-filing-mardan.html", "## Late Filing\n\nReturns can still be filed after the deadline, with the surcharge.")
add("blogs/tax-consultant-mastung.html", "Only income from them is relevant.")
add("blogs/ntn-registration-mastung.html", "## Students\n\nStudents from Mastung at universities in Quetta who begin earning register with their CNIC to start a tax record.")
add("blogs/income-tax-filing-mastung.html", "## Government Contractors\n\nContractors on roads and water schemes list each bill, the tax withheld by the department and their costs of labour, materials and machinery.\n\n## Teachers\n\nTeachers in the district's schools copy their salary certificates.")
add("blogs/tax-consultant-matiari.html", "Their stock is counted on 30 June.")
add("blogs/ntn-registration-matiari.html", "## Students\n\nStudents from Hala and Matiari studying in Hyderabad and Jamshoro who start freelancing register with their CNIC.")
add("blogs/tax-consultant-mehrabpur.html", "## Kandiaro and Bhiria Road\n\nTraders in nearby Kandiaro and along the Bhiria road buy bananas and dates from growers and load trucks at night for Karachi; their margin after freight and labour is business income, and their records are the weighbridge and truck receipts.")
add("blogs/tax-consultant-mian-channu.html", "## Property\n\nPlots along the highway cost less in advance tax for active filers.")
add("blogs/ntn-registration-mian-channu.html", "## Overseas Workers\n\nWorkers from Mian Channu's villages in the Gulf can register with a NICOP and file online.\n\n## Shops in the Main Bazaar\n\nShops that accept wallet payments open business accounts after registration.")
add("blogs/income-tax-filing-mian-channu.html", "## Transporters\n\nTruck owners show freight against diesel, tyres, repairs and wages, claiming the token tax.\n\n## Remittances\n\nMoney from relatives abroad is a receipt in the wealth statement.\n\n## Late Filing\n\nA late return is accepted with the surcharge.")
add("blogs/tax-consultant-mianwali.html", "Some also run private academies.")

add("blogs/ntn-registration-mastung.html", "A filed return also helps with scholarship and job applications.")
add("blogs/income-tax-filing-mastung.html", "## Pensioners\n\nRetired officials living in Mastung declare their pension as exempt and list their orchards.")
add("blogs/ntn-registration-matiari.html", "Registration also helps with bank loans for new kilns and looms.")
add("blogs/ntn-registration-mian-channu.html", "Registration is also needed for bank financing of tractors and solar pumps.")
add("blogs/income-tax-filing-mian-channu.html", "## Bank Profit\n\nProfit on savings accounts is declared with the bank's withholding.\n\n## Pensioners\n\nRetired teachers and railway staff declare their pension as exempt.")
add("blogs/income-tax-filing-mian-channu.html", "Their wealth statement lists the house and land they own.")
