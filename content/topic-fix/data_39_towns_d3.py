"""Local additions for towns D pages below the floor."""

PAGES = {}


def more(rel, text):
    PAGES[rel] = {"body_more": text}


more("blogs/income-tax-filing-dadu.html", """## Landowners Paying Sindh Agricultural Tax

Larger landholders in Dadu pay agricultural income tax to the Sindh government. That payment is noted in the federal return so the wealth statement shows where crop income went, but the crop income itself is not taxed again by FBR.""")

more("blogs/ntn-registration-daska.html", """## Shops in the Main Bazaar

Cloth, mobile and electronics shops in Daska that accept card and wallet payments need a business account in the shop's name, which banks open after the NTN is issued.""")

more("blogs/tax-consultant-daska-city-centre.html", """## Wedding Season

Wedding halls, caterers, tent services and boutique tailors near the city centre do much of their year's business between October and March. Advance bookings should be recorded when received, and each event's costs noted, so that the profit is assigned to the right tax year.""")

more("blogs/ntn-registration-depalpur.html", """## Seed and Pesticide Dealers

Input dealers in Depalpur buy from national companies that supply only registered dealers and deduct tax on each supply. A registered dealer who files is deducted at the lower rate, and the deduction becomes a credit in his return.""")

more("blogs/income-tax-filing-depalpur.html", """## Input Dealers

Seed, fertiliser and pesticide dealers show sales, purchases from companies and closing stock. Companies deduct tax on supplies to dealers, and these deductions are listed and credited.

## Families Leasing Out Land

Land leased to another farmer for cash rent remains agricultural income for the owner, while the tenant's crop sales are his own agricultural income.

## Remittances

Money from family members in the Gulf, received through banks, is shown in the wealth statement as receipts.

## Late Filing

A return filed after the deadline is still accepted; the surcharge applies to rejoin the Active Taxpayers List.""")

more("blogs/tax-consultant-dera-bugti.html", """## Families Living Elsewhere

Many Dera Bugti families now live in Quetta, Sui or Sindh's cities. Each family member files where needed using their own CNIC, and property held in the home district is listed in their own wealth statement.""")

more("blogs/ntn-registration-dera-ghazi-khan.html", """## Shops in Fort Munro Road Markets

Traders supplying goods towards Balochistan from markets on the Fort Munro road register so that payments from buyers arrive in business accounts.""")

more("blogs/tax-consultant-dera-ismail-khan.html", """## Livestock Markets

D.I. Khan's cattle markets supply animals across the region, especially before Eid ul Adha. Breeders raising animals on their own land earn agricultural income, while traders who buy and sell within weeks earn business income on the margin.""")

more("blogs/ntn-registration-dera-ismail-khan.html", """## Wholesalers Supplying Southern KP

Wholesalers in D.I. Khan who supply shops in Tank, Lakki Marwat and the former tribal districts deal with distributors that prefer registered buyers and banks that ask for an NTN before opening business accounts.""")

more("blogs/ntn-registration-dina.html", """## Contractors at Mangla

Contractors who supply maintenance, transport and services to the dam and its colony are asked for an NTN by the employing organisation, which deducts tax on bills at lower rates for active filers.""")

more("blogs/ntn-registration-dinga.html", """## Farmers Selling to Mills

Larger growers selling rice or wheat directly to mills may be asked for an NTN by the mill's purchase department even though their crop income itself is agricultural.""")

more("blogs/tax-consultant-dir-lower.html", """## Chakdara and the Swat Motorway

The motorway link to Chakdara has brought new petrol pumps, restaurants and shops. These businesses keep daily sales and purchase records from the start.""")

more("blogs/ntn-registration-fort-abbas.html", """## Teachers and Government Staff

Teachers and other salaried residents whose tax is deducted can register on IRIS to file their own returns and claim back any excess deduction.""")

more("blogs/income-tax-filing-fort-abbas.html", """## Input Dealers

Dealers in seed, fertiliser and pesticide show sales on credit to farmers as receivables at 30 June, collected after harvest. Tax deducted by companies on supplies is credited.

## Transporters

Truck owners show freight less fuel, repairs, wages and depreciation, and claim advance tax paid with the vehicle token.

## Families with Members Abroad

Remittances received through banks are shown in the wealth statement.""")

PAGES["blogs/income-tax-filing-depalpur.html"]["body_more"] += "\n\n## Haveli Lakha Shops\n\nShopkeepers in Haveli Lakha and the smaller bazaars show purchases from Okara wholesalers and a daily sales total."
PAGES["blogs/ntn-registration-dera-ismail-khan.html"]["body_more"] += " Registering under the trading name used on invoices avoids mismatches later."
PAGES["blogs/ntn-registration-fort-abbas.html"]["body_more"] += " A filed return also helps when applying for loans or bank accounts."
PAGES["blogs/income-tax-filing-fort-abbas.html"]["body_more"] += "\n\n## Livestock\n\nAnimals raised on your own land are part of farming. Buying cattle to fatten and resell before Eid is a trading business, and its margin is declared as business income after feed and transport."
