"""Rewrites and local additions for towns O pages."""

PAGES = {}


def add(rel, text, key="body_more"):
    PAGES.setdefault(rel, {}).setdefault(key, "")
    PAGES[rel][key] += "\n\n" + text


def body(rel, text):
    PAGES.setdefault(rel, {})["body"] = text


body("blogs/ntn-registration-sibi.html", """## Selling Animals Before Eid to City Buyers

In the weeks before Eid ul Adha, traders from Sibi send truckloads of cattle, goats and camels to the markets of Karachi, Hyderabad and Punjab, and increasingly sell to buyers who pay through bank transfers and mobile wallets. A trader who receives these payments into his own account needs it to be a proper business account, and banks ask for an FBR NTN before opening one. Registration also gives the trader a record of his trade, which helps when he later buys property or a truck.

## Breeders of Bhag Nari Cattle

Breeders who sell prize animals at the Sibi Mela to livestock departments, research farms and development projects are paid by bank and asked for registration. Selling animals they bred themselves stays agricultural income.

## Contractors for Divisional Departments

Road, irrigation and building works across the Sibi division are given to registered contractors, and departments check filer status before deciding the withholding rate on each bill.

## Truck Owners Crossing the Bolan

Companies hiring trucks to carry goods between Sindh and Quetta through the Bolan pass require registered carriers and withhold tax on freight.

## Railway Staff

Employees at Sibi junction can register on IRIS to file their own returns and claim back excess withholding.

## Getting Registered

Registration is free and online; our [FBR registration guide](/blogs/fbr-registration-step-by-step) explains each step.""")

body("blogs/tax-consultant-sillanwali.html", """## A Citrus Town West of Sargodha

Sillanwali sits on the western side of Sargodha district, where the canal colonies laid out in the early twentieth century give way to the Thal. Its villages, many still known by their chak numbers, grow kinnow, wheat, sugarcane and fodder, and it has a busy grain market.

## Who Owns the Crop

The key tax question for Sillanwali's citrus is who earns what. An orchard owner who sells the season's fruit on the tree to a contractor, often in instalments from spring onwards, earns agricultural income from that sale and pays no federal tax on it. The contractor who then picks, crates and sells the fruit to packing houses in Sargodha and Bhalwal is a trader, and his margin after the contract price, picking labour, crates and transport is business income. In a year when frost or hail ruins the fruit, the contractor may lose money; that loss is shown in the return and can generally be set against later business profit.

## Cane Haulage

Families who carry cane to the mills for others with their tractor-trolleys earn freight income; the mills withhold tax on it.

## Commission Agents

Arhtis in the grain market earn commission and record advances to growers as receivables on 30 June.

## Soldiers and Airmen

Serving personnel have tax withheld; pensions are generally exempt but declared.

## Remittances

Money from family members abroad, received through banks, is a receipt in the wealth statement.""")

add("blogs/ntn-registration-shikarpur.html", "## Pickle Makers Supplying Distributors\n\nDistributors who carry Shikarpuri brands to shops across Sindh and Punjab appoint only registered suppliers, so that their own sales tax records are complete.")
add("blogs/income-tax-filing-shikarpur.html", """## Merchants with Businesses in Karachi

Shikarpuri families who run shops or wholesale businesses in Karachi while keeping homes in the old city file one return covering all their income. Rent from Shikarpur property and profit from the Karachi business both belong in it.

## Sweet Makers

Sweet shops show daily sales against milk, sugar, ghee, dry fruit, packing and wages, with festival seasons noted.

## Gold and Jewellery Shops in the Bazaar

Jewellers near the Lakhi Dar weigh their gold stock on 30 June and record old gold taken in exchange by weight and value.""")
add("blogs/income-tax-filing-sibi.html", """## Contractors for Departments

Contractors list each bill paid by divisional departments, the tax withheld and their costs of labour, materials and machinery.

## Families in Quetta

Sibi families living partly in Quetta file one return covering all their income.

## Mela Season Accounts

The Sibi Mela falls in February, in the middle of the tax year; stall holders who trade only during the mela still file for the whole year, showing the mela takings and the stock bought for it.

## Dates and Kachhi Produce

Traders who buy dates and grain from the Kachhi plain to send to Quetta show their margin after purchase, packing and freight.""")
add("blogs/ntn-registration-skardu.html", "## Guides and Porters' Contractors\n\nContractors who supply porters to agencies and are paid by bank need registration details for those payments.\n\n## Shigar and Khaplu Guest Houses\n\nHeritage guest houses in Shigar and Khaplu taking bookings from tour companies in Islamabad are paid by bank transfer.")
add("blogs/income-tax-filing-skardu.html", """## Porters and High-Altitude Staff

Porters and high-altitude workers paid per expedition usually earn below the taxable threshold, but those who want filer status can file returns showing their earnings and assets.

## Government and Army Staff

Salaried staff copy their certificates.

## Late Filing

A late return is accepted with the surcharge.""")
add("blogs/tax-consultant-sohawa.html", "## Domeli and the Villages\n\nVillages around Domeli have many British-funded houses, often empty for much of the year; owners who let them declare the rent.")
add("blogs/ntn-registration-sukkur.html", "## IBA Graduates and Freelancers\n\nGraduates of Sukkur's universities who begin freelancing or consulting register with their CNIC so that payments reach their own accounts.\n\n## Hotels Near the Barrage\n\nHotels serving business travellers register with FBR and the Sindh Revenue Authority.")
add("blogs/tax-consultant-swabi.html", "Their contracts and payment slips are the main records.")
add("blogs/ntn-registration-swabi.html", "## Students at GIKI and Swabi's Colleges\n\nStudents who begin freelancing register with their CNIC so that foreign payments reach their own accounts.\n\n## Marriage Halls\n\nHalls register with FBR and KPRA to accept bookings by bank transfer.")
add("blogs/tax-consultant-swat.html", "## Honey\n\nBeekeepers in the Swat valley sell honey to visitors and shops; honey from your own hives is generally treated as part of farming, while buying honey to pack and resell is trading.")
add("blogs/tax-consultant-talagang.html", "## Property\n\nPlots in Talagang city and Rawalpindi cost less in advance tax for active filers.")
add("blogs/ntn-registration-talagang.html", "## Teachers and Officials\n\nSalaried residents can register on IRIS to file their own returns.\n\n## Shops\n\nShops wanting card machines open business accounts after registering.")
add("blogs/income-tax-filing-talagang.html", """## Serving Soldiers

Pay certificates show salary and withholding; soldiers posted elsewhere still list their Talagang house and land.

## Transporters

Truck and coach owners show freight and fares against diesel, repairs and wages, with token tax claimed.

## Bank Profit

Profit on savings is declared with the bank's withholding.

## Dhanni Cattle Traders

Buying cattle to resell at shows and markets is trading; the margin after purchase, fodder and transport is business income.""")

add("blogs/ntn-registration-shikarpur.html", "Registration is also needed before the brand can export to buyers in the Gulf.")
add("blogs/ntn-registration-skardu.html", "## Jeep Owners on the Deosai Route\n\nJeep owners carrying tourists to Deosai and Shigar register to accept payments from tour companies by bank transfer and to deal with corporate groups.")
add("blogs/income-tax-filing-skardu.html", "## Jeep Owners\n\nFares from tourists and tour companies against fuel, repairs and drivers' wages, with the jeep depreciated.\n\n## Families with Property in Islamabad\n\nRent from a flat in Islamabad is declared with any tenant withholding claimed.")
add("blogs/ntn-registration-sukkur.html", "Registration is free and does not need an office visit.")
add("blogs/ntn-registration-swabi.html", "## Maize and Gur Traders\n\nTraders sending maize to feed mills and gur to Punjab's markets are paid by bank and asked for registration by larger buyers.")
add("blogs/tax-consultant-talagang.html", "Sellers keep the acquisition record.")
add("blogs/ntn-registration-talagang.html", "## Transport Businesses\n\nCoach companies running between Talagang, Rawalpindi and Mianwali register to deal with corporate bookings and to adjust the advance tax paid with each vehicle's token.")
add("blogs/income-tax-filing-talagang.html", "## Groundnut Traders\n\nTraders buying groundnut from barani farmers and selling to processors show their margin after purchase, cleaning and freight, with stock counted on 30 June.")
add("blogs/ntn-registration-shikarpur.html", "Exporters need it for customs.")
add("blogs/income-tax-filing-shikarpur.html", "Their making charges are income.")
add("blogs/income-tax-filing-sibi.html", "## Railway Pensioners\n\nRetired railway staff living in Sibi declare their pension as exempt and list their houses and land, so that the wealth statement shows where their assets came from.")
add("blogs/ntn-registration-skardu.html", "## Students\n\nBaltistan's students at universities in Islamabad and Lahore register with their CNIC once they begin earning.")
add("blogs/income-tax-filing-skardu.html", "## Hotels in Shigar and Khaplu\n\nHeritage hotels and guest houses show room and food income against staff, food and maintenance, with buildings depreciated over their useful life.")
add("blogs/ntn-registration-sukkur.html", "## Shops in the Old Bazaar\n\nShops in Sukkur's old bazaar and on Military Road that want card machines need a business account.")
add("blogs/ntn-registration-swabi.html", "## Contractors on Tarbela and Canal Works\n\nWAPDA and irrigation departments require registered contractors.")
add("blogs/tax-consultant-talagang.html", "Gains depend on when land was acquired.")
add("blogs/ntn-registration-talagang.html", "## Students and Graduates\n\nYoung people from Talagang who begin freelancing or take jobs in Rawalpindi register with their CNIC to start a tax record.")
add("blogs/income-tax-filing-talagang.html", "## Teachers and Officials\n\nTeachers and civil servants in Talagang copy salary and withholding from their certificates and list the land they own.")
add("blogs/income-tax-filing-shikarpur.html", "Stock taken on credit is recorded too.")
add("blogs/ntn-registration-skardu.html", "Registration needs no office visit.")
add("blogs/income-tax-filing-skardu.html", "Furniture is depreciated too.")
add("blogs/ntn-registration-sukkur.html", "## Contractors at the Barrage\n\nIrrigation authorities maintaining the barrage and its canals give work to registered contractors and withhold tax on their bills.")
add("blogs/ntn-registration-swabi.html", "## Teachers and Officials\n\nSalaried residents can register on IRIS to file their own returns and claim back any excess withholding from their employers.")
add("blogs/tax-consultant-talagang.html", "Records should be kept.")
add("blogs/ntn-registration-talagang.html", "## Groundnut Traders\n\nProcessors buying groundnut from Talagang's traders pay by bank and ask for an NTN.")
add("blogs/income-tax-filing-talagang.html", "## Property Sales\n\nA plot or house sold during the year is reported with the price, its cost, the gain and the advance tax paid at transfer.")
add("blogs/income-tax-filing-shikarpur.html", "Credit purchases from Karachi suppliers are liabilities.")
add("blogs/ntn-registration-skardu.html", "Filing comes next.")
add("blogs/income-tax-filing-skardu.html", "Generators are depreciated as well.")
add("blogs/ntn-registration-talagang.html", "There is no charge for registration.")
add("blogs/income-tax-filing-talagang.html", "The deed should be kept.")
