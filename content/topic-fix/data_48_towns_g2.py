"""Local additions for towns G pages below the floor."""

PAGES = {}


def add(rel, text, key="body_more"):
    PAGES.setdefault(rel, {}).setdefault(key, "")
    PAGES[rel][key] += "\n\n" + text


add("blogs/ntn-registration-kamalia.html", "## Women Weavers\n\nWomen who weave or embroider at home for Kamalia's merchants can register under their own CNIC when they start selling directly, keeping their earnings in their own accounts.")
add("blogs/income-tax-filing-kamalia.html", """## Wage Weavers

Weavers paid by the piece or by the metre by a merchant report that as income from work. Where it is below the taxable threshold no tax is due, but a return may still be filed to get onto the Active Taxpayers List, which lowers advance tax on a motorcycle or plot purchase.

## Dyeing and Finishing Units

Units that dye, print and finish khaddar for merchants charge processing fees. Their return shows those fees against dyes, chemicals, gas, electricity and labour. Waste water treatment, where required, is a business cost.""")
add("blogs/income-tax-filing-kamoke.html", """## Paddy Driers and Husk Sales

Many Kamoke mills now dry paddy mechanically and sell husk as boiler fuel to factories. Husk sales are part of the mill's income, and buyers may withhold tax on them. Fuel used for drying is a cost.

## Transporters

Truck owners carrying paddy from Sheikhupura, Hafizabad and Narowal into Kamoke, and rice out to Karachi, show freight less diesel, tyres, repairs and drivers' wages, with the advance tax paid with their annual token claimed.

## Shopkeepers on the GT Road

Shops along the GT Road show sales, purchases and stock, and claim the advance tax charged on commercial electricity bills.""")
add("blogs/tax-consultant-kamonke.html", "## Teachers and Doctors\n\nTeachers at the town's schools and doctors in private practice declare salary and fee income separately; patients' panel payments from companies may carry withholding.")
add("blogs/tax-consultant-kandhkot.html", "## Doctors and Clinics\n\nPrivate clinics and pharmacies serving the district keep fee registers and distributor invoices.")
add("blogs/ntn-registration-karak.html", "## Contractors for Schools and Roads\n\nGovernment departments building schools, roads and water schemes in the district require contractors to be registered and check filer status before deciding the withholding rate.")
add("blogs/income-tax-filing-karak.html", """## Families Living on Remittances

Where a Karak household's only money comes from a son in Dubai or Riyadh, the parents often file only when they need filer status, for example before buying a plot. Their return then shows no taxable income, the remittances as receipts and the property bought with them in the wealth statement.

## Returned Workers Starting Businesses

Men who come home and invest savings in a pick-up, a shop or a share in an oilfield transport business should file from the first year so that the source of their capital is on record and the new business's profit is declared.

## Army Personnel

Serving soldiers' salary certificates show tax withheld; land allotted to them and houses built are listed.""")
add("blogs/tax-consultant-kashmor.html", "## Rice Mills\n\nRice mills in Kashmore and Kandhkot buy paddy after harvest and sell to buyers in Sukkur and Balochistan; their stock on 30 June is valued at cost.")
add("blogs/tax-consultant-kasur.html", "## Pattoki, Chunian and Kot Radha Kishan\n\nKasur district's other towns have their own nurseries, rice mills and industrial units, and their taxpayers face similar questions about sales tax registration and documentation.")
add("blogs/ntn-registration-kasur.html", """## Shoe Makers Going Online

Small Kasur footwear brands selling through social media and marketplaces need registration details for seller accounts and payment gateways. Registering at the start keeps the brand's sales in its own bank account.

## Falooda and Sweet Shops

Well-known food shops that open branches or sell through delivery apps register to deal with the apps' payment systems and with PRA for services where applicable.

## Overseas Workers

Workers from Kasur's villages working abroad can register with a CNIC or NICOP and file online.""")
add("blogs/income-tax-filing-kasur.html", """## Online Footwear Sellers

Sales through marketplaces and courier cash-on-delivery are shown from the platform and courier statements. Returned parcels reduce sales, and courier charges, packaging and advertising are costs.

## Food Shops

Falooda and sweet shops show daily sales against milk, sugar, ingredients, wages and rent. Delivery app commissions are expenses.

## Commuters' Returns

Kasur residents working in Lahore's factories or offices report salary from the certificate and claim any excess tax withheld, often due to a mid-year salary change.""")
add("blogs/tax-consultant-khairpur.html", "## Kot Diji and Tourism\n\nHotels and guides serving visitors to Kot Diji fort and the Faiz Mahal are small seasonal businesses; their services fall under SRB.")
add("blogs/ntn-registration-khairpur.html", """## Date Growers Selling in Bulk

Larger growers who sell their whole crop to processors or exporters are asked for an NTN by buyers even though the income itself is agricultural.

## Transporters

Truck owners carrying dates to Karachi port and to markets in Punjab register to deal with exporters and processors who pay by bank.

## Students and Graduates

Students of Shah Abdul Latif University who begin tutoring or freelancing register with their CNIC.""")
add("blogs/income-tax-filing-khairpur.html", """## Date Season in the Accounts

The date harvest runs from June to August, so a processor's purchases fall at the very end of one tax year and the start of the next. Fresh dates bought in June and still being dried on 30 June are closing stock of the earlier year. Getting this cut-off right avoids showing a false loss in one year and a false profit in the next.

## Gas Field Contractors

Contractors list each payment from the gas companies with the tax withheld, deducting fuel, wages and vehicle costs. Some withholding may be minimum tax.

## Traders

Shopkeepers and wholesalers show sales, purchases and stock, with advance tax on electricity bills claimed.""")
add("blogs/ntn-registration-karak.html", "## Army Families\n\nRetired soldiers investing in transport or shops register when the business starts.")
add("blogs/income-tax-filing-kasur.html", """## Ganda Singh Wala and Border Villages

Farmers in the border villages declare their crop income as agricultural and list their land, while families who run a shop or tractor service declare that profit separately.

## Property Sold Near Lahore

Land on the Kasur-Lahore road has risen in value. A sale is reported with the price, cost and gain, and the advance tax paid under section 236C is claimed; the gain's treatment depends on when the land was acquired.""")
add("blogs/ntn-registration-khairpur.html", "## Shops in the Old City\n\nShops near the Faiz Mahal and the old bazaar that accept card payments need a business account.")
add("blogs/income-tax-filing-khairpur.html", "## Pensioners\n\nRetired teachers and officials declare their pension as exempt and list the land and houses they own.")
add("blogs/income-tax-filing-khairpur.html", "Their returns also claim any tax withheld on bank profit from savings accounts.")
