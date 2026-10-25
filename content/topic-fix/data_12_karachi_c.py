"""Karachi area pages, part C: industrial, old-city and western areas."""

PAGES = {}


def page(slug, lead, desc, body, faq):
    PAGES[f"blogs/tax-consultant-{slug}.html"] = {"lead": lead, "desc": desc, "body": body, "faq": faq}


page("baldia-town-karachi",
     "Baldia Town in west Karachi is a working-class district beside the SITE industrial belt, with garment and small manufacturing units, transport businesses and thousands of factory workers. Our clients here are small unit owners, contractors, transporters and salaried workers.",
     "Baldia Town Karachi tax help for small factories, labour contractors, transporters and workers: registration, sales tax, withholding and returns, done online.",
     """## Small Units Supplying Bigger Factories

Many Baldia workshops stitch, wash, print or pack goods for larger exporters in SITE. The buyer often deducts tax from payments and asks for an NTN, and sometimes a sales tax registration. Keeping each purchase order with its invoice and payment record lets the workshop claim the tax deducted and shows its real turnover.

## Labour Contractors

Contractors who supply workers to factories receive payments that include wages they pass on. Only the contractor's margin is profit, but tax may be deducted on the full payment. A wage register and bank record of payments to workers are needed to show the difference.

## Transporters

Pick-up and loader operators carrying goods between Baldia, SITE and the port pay advance tax with vehicle tax and may have tax deducted on freight. These are credits in the annual return.

## Workers

Factory workers whose salary crosses the taxable threshold have tax deducted by the employer. Filing is optional for many, but it puts them on the Active Taxpayers List and allows any excess deduction to be refunded.

| Client | First record to keep |
| Workshop | Purchase orders, invoices, buyer's tax certificates |
| Labour contractor | Wage register, bank transfers to workers |
| Transporter | Freight bills and vehicle tax receipts |
| Worker | Salary certificate |""",
     [("My buyer deducts tax from my workshop's payments. Can I get it back?",
       "It is credited against your tax when you file. If it exceeds your liability, the excess can be claimed as a refund."),
      ("Is a labour contractor taxed on the full payment from the factory?",
       "Income tax applies to the contractor's profit. Wages passed on to workers are costs, supported by a wage register and payment records."),
      ("Should a factory worker file a return?",
       "It is worthwhile if tax is deducted from salary or if you want the lower rates available to people on the Active Taxpayers List.")])

page("kharadar-karachi",
     "Kharadar, in Karachi's old city near Jodia Bazaar and the Mithadar markets, is one of the oldest trading neighbourhoods, home to wholesale merchants, commission agents and family firms that have traded for generations. Tax work here centres on wholesale trade and family businesses.",
     "Kharadar Karachi tax help for wholesale traders, commission agents and family firms: profit computation, sales tax, AOP returns and records, filed online.",
     """## Wholesale Trading Firms

Kharadar's wholesalers deal in dry fruit, spices, cloth, chemicals and household goods in large volumes and on credit. For income tax, the key figure is gross profit after purchases and stock changes. Ledgers of credit sales and receivables also matter, because FBR compares bank deposits with declared turnover.

## Commission Agents

Agents who arrange sales between importers and retailers earn commission, which is their income, while the goods' value passes through their accounts. Separating commission from pass-through money in the books keeps the return accurate.

## Family Partnerships

Many firms are run by brothers or cousins as partnerships. The firm files as an association of persons, and each partner declares their share in their own return. A written deed with profit-sharing ratios avoids confusion when a partner leaves or a new generation joins.

## Sales Tax for Wholesalers

Wholesalers above the turnover thresholds may need a sales tax registration and monthly returns, and buyers who are registered may insist on proper invoices. Supplying unregistered retailers can also attract further tax on sales.

| Firm type | Key filing |
| Wholesaler | Profit from purchases, sales and stock |
| Commission agent | Commission as income, pass-through separated |
| Family partnership | AOP return plus partners' returns |""",
     [("Does a Kharadar wholesaler pay tax on turnover?",
       "Income tax is on profit, worked out from purchases, sales and closing stock. Minimum tax on turnover can apply in some cases."),
      ("How is a family partnership taxed?",
       "The firm files an AOP return and pays tax on its income; partners declare their share in their own returns."),
      ("Do wholesalers need sales tax registration?",
       "Above the prescribed thresholds or depending on the goods traded, yes. We check each firm's position.")])

page("korangi-karachi",
     "Korangi hosts one of Pakistan's largest industrial areas, with textile, pharmaceutical, food and engineering plants, alongside residential sectors for the workers and managers who run them. Our Korangi clients include factory owners, vendors, contractors and salaried staff.",
     "Korangi Karachi tax consultant for factories, vendors, contractors and staff: sales tax, withholding statements, export filing and returns, handled online.",
     """## Exporters in Korangi Industrial Area

Textile and garment exporters in Korangi deal with tax on export proceeds, sales tax refunds on inputs and, where approved, the Export Facilitation Scheme. Since recent budgets moved many exporters towards the normal tax regime, profit and expense records matter more than before.

## Vendors and Service Contractors

Hundreds of smaller firms supply packaging, chemicals, maintenance and transport to Korangi's plants. Their customers deduct income tax on payments and often require sales tax or SRB registration. Monthly matching of invoices with tax certificates prevents credits from being lost.

## Payroll and Withholding

Factories with large workforces deduct salary tax each month and file withholding statements. Errors in these statements show up later when employees' returns do not match, so payroll data and withholding records should be reconciled before each filing.

## Managers and Engineers

Salaried managers living in Korangi's residential sectors often receive perquisites such as company transport or housing, which are valued and added to taxable salary.

| Client | Recurring work |
| Exporter | Proceeds records, refunds, annual return |
| Vendor | Invoices, tax certificates, SRB or sales tax returns |
| Factory payroll | Monthly withholding statements |
| Manager | Salary certificate with perquisites |""",
     [("Do Korangi vendors need SRB registration?",
       "If they provide taxable services in Sindh, such as maintenance or security, above the threshold, yes."),
      ("Why reconcile payroll with withholding statements?",
       "Employees' returns are matched with the employer's statements; mismatches lead to notices for both."),
      ("Are exporters still on a final tax regime?",
       "Many exporters of goods have moved towards the normal regime where the export deduction acts as minimum tax. We confirm the treatment for each year.")])

page("landhi-karachi",
     "Landhi in east Karachi combines a large industrial area, the Karachi Export Processing Zone and dense residential sectors. Our Landhi clients include export-zone businesses, small manufacturers, transporters and the salaried workers employed by them.",
     "Landhi Karachi tax help for export zone firms, manufacturers, transporters and workers: zone rules, sales tax, withholding and returns, done online.",
     """## Businesses in the Export Processing Zone

Units in the Karachi Export Processing Zone operate under the zone's special customs and tax framework, which was designed around exports. Benefits are tied to zone registration and conditions, and they do not automatically extend to suppliers outside the zone. Zone businesses still keep proper records and file returns.

## Manufacturers Outside the Zone

Landhi's industrial area hosts steel, plastics, food and garment units. They usually need sales tax registration, file monthly returns, deduct tax from suppliers and staff, and claim input tax only on invoices from active registered suppliers.

## Transport and Logistics

Trucking companies moving goods from Landhi to the port and up-country pay advance tax with vehicle tax and have tax deducted on freight by corporate clients. A freight register makes the return straightforward.

## Residents and Workers

Landhi's residential sectors are home to factory and port workers. Those with salary tax deducted can file to claim refunds and join the Active Taxpayers List, which lowers withholding on bank and vehicle transactions.

| Client | Main concern |
| Zone unit | Conditions of zone registration |
| Manufacturer | Sales tax and supplier verification |
| Transporter | Freight records, tax credits |
| Worker | Refund of excess salary tax |""",
     [("Do zone benefits apply to my business if I supply a Landhi EPZ unit?",
       "Not automatically. Zone incentives depend on the unit's own registration and conditions; suppliers outside the zone follow the normal rules."),
      ("Can a manufacturer claim input tax on any purchase invoice?",
       "Only on valid invoices from suppliers who are registered and active, and subject to the inadmissible list."),
      ("Can Landhi workers get refunds?",
       "Yes, if tax deducted from salary exceeds the actual liability, by filing a return.")])

page("liaquatabad-karachi",
     "Liaquatabad is a densely populated central Karachi district known for its furniture market, small workshops and busy bazaars. Most of our Liaquatabad clients are furniture makers and dealers, shopkeepers, artisans and families with modest incomes.",
     "Liaquatabad Karachi tax help for furniture makers and dealers, shopkeepers and artisans: simple records, returns, NTN and filer status, handled online.",
     """## The Furniture Trade

Liaquatabad's furniture market combines workshops that build furniture with showrooms that sell it. A workshop's profit depends on wood, hardware and labour costs; a showroom's on purchase price and sale price. Many businesses do both. Simple job cards for each order and a record of material purchases are enough to work out profit.

## Artisans and Small Workshops

Carpenters, upholsterers and polishers often work on contract for showrooms. Their income is what they are paid, less materials and tools. Most earn modest amounts, but registering and filing helps them get bank accounts and supplier credit.

## Shopkeepers in the Bazaar

General stores and garment shops in Liaquatabad's markets mostly deal in cash. Keeping purchase bills and a monthly summary of sales, along with electricity bills, forms an adequate basis for a return.

## Selling to Companies

Furniture makers who supply offices, hotels or schools may find these buyers deduct income tax on payments and ask for an NTN. These deductions are credits, so keep every payment advice.

| Business | Simple records |
| Workshop | Job cards, material bills, wages |
| Showroom | Purchase and sale invoices |
| Artisan | Payments received, tools bought |
| Shop | Purchase bills, monthly sales summary |""",
     [("How does a Liaquatabad furniture workshop calculate profit?",
       "Sales minus wood, hardware, labour and workshop costs, supported by job cards and purchase bills."),
      ("Do artisans working for showrooms need to file?",
       "If their income is above the threshold, yes; filing also helps with bank accounts and credit even below it."),
      ("Why did a company deduct tax from my furniture payment?",
       "Companies are withholding agents for certain payments. The deduction is a credit you claim in your return.")])

page("malir-karachi",
     "Malir in east Karachi stretches from the cantonment and airport surroundings to farmhouses and new housing schemes along the Malir river. Our clients here include cantonment residents, farm owners, airline and airport staff and property investors.",
     "Malir Karachi tax help for cantonment residents, farmhouse owners, airport staff and property investors: returns, agricultural income and property records.",
     """## Farmhouses and Agricultural Land

Parts of Malir still have orchards, poultry farms and agricultural land. Crop income is taxed by Sindh under its agricultural income tax law and declared as exempt income in the federal return. Poultry and dairy run as commercial operations are generally business income taxed by FBR. The distinction depends on how the activity is organised.

## Airport and Airline Staff

Many Malir and nearby cantonment residents work at the airport, for airlines or ground handlers. Their salary includes allowances and sometimes travel benefits, which should be shown correctly on the salary certificate.

## New Housing Schemes

Investors buy plots in Malir's new schemes on booking and instalments. Every instalment is part of the investment, shown in the wealth statement until possession. Instalment schedules and receipts are the key documents, and the developer's approvals should be checked before buying.

## Cantonment Property

Houses in Malir Cantonment are subject to the cantonment board's own property tax, separate from federal income tax. Keep both records.

| Client | Key record |
| Farm owner | Land record, sales of produce |
| Airport staff | Salary certificate with allowances |
| Plot investor | Booking letter, instalment receipts |
| Cantonment resident | Cantonment property tax receipts |""",
     [("Is income from my Malir farmhouse orchard taxable by FBR?",
       "Agricultural income is taxed by Sindh, not FBR, but it is declared as exempt income in the federal return."),
      ("How do I declare a plot bought on instalments?",
       "Show the total paid to date as an advance for property in the wealth statement until possession."),
      ("Is poultry farming agricultural income?",
       "Commercial poultry operations are generally treated as business income for federal tax. We review how your farm runs.")])

page("maripur-karachi",
     "The Maripur Road corridor in west Karachi is lined with truck stands, container yards, workshops and goods transport offices that link the port with the rest of the country. Our clients from Maripur are transporters, workshop owners and logistics staff.",
     "Maripur Road Karachi tax help for transporters, container yards, workshops and logistics staff: freight income, vehicle tax credits and returns, online.",
     """## Goods Transport Companies

Transport offices along Maripur Road book trucks for importers and manufacturers. Some own fleets; others act as brokers between clients and independent truck owners. A fleet owner's income is freight less running costs; a broker's income is the margin. Mixing the two in one bank account without records causes problems at filing time.

## Truck Owners

Individual truck owners pay advance income tax with their annual vehicle tax, based on the vehicle's capacity, and may have tax deducted on freight by corporate clients. Both are credits against their annual liability, but only if they file.

## Container Yards and Workshops

Yards that store containers and workshops that repair trucks and trailers provide services and may fall under Sindh sales tax on services. Their customers, often logistics companies, will usually ask for registration numbers.

## Records That Work

A trip book showing date, route, client, freight and payment is the most useful single record for any transporter.

| Client | What income is |
| Fleet owner | Freight less fuel, tolls, salaries and repairs |
| Broker | Margin between client freight and truck hire |
| Truck owner | Freight received less running costs |
| Workshop | Repair charges less parts and wages |""",
     [("Is the advance tax paid with truck vehicle tax adjustable?",
       "Yes, it is credited against your annual income tax when you file a return."),
      ("How is a transport broker taxed?",
       "On the margin between what clients pay and what is paid to truck owners, supported by a booking record."),
      ("Do truck repair workshops pay SRB tax?",
       "Repair and maintenance services can be taxable under Sindh's sales tax on services law, depending on the service and turnover.")])

page("mauripur-karachi",
     "Mauripur in west Karachi lies near the coast and the Hawke's Bay road, with fishing settlements, salt works, warehouses and businesses serving the nearby air base and port. Our Mauripur clients include fish traders, boat owners, warehouse operators and local suppliers.",
     "Mauripur Karachi tax help for fish traders, boat owners, warehouse operators and suppliers: business returns, cash records and filer status, handled online.",
     """## Fishing and Fish Trading

Boat owners and fish traders around Mauripur sell catch at the harbour auction or directly to processors. Income is the sale proceeds less fuel, ice, crew shares and boat maintenance. Many boats are jointly owned, so each partner declares their share of profit.

## Processors and Exporters

Fish processors and exporters buy from boat owners and sell abroad. Exports are paid through banks with tax deducted on proceeds, and processors often deduct tax when paying suppliers. Boat owners selling to processors should keep sale receipts and any deduction certificates.

## Warehouses and Storage

Warehouses along the Mauripur corridor store imported goods and salt. Rent from warehouses let to companies may have tax deducted at source, and storage services can fall under Sindh sales tax on services.

## Local Suppliers

Shops supplying fuel, nets, ice and food to the fishing community deal mostly in cash and credit. A simple credit register helps show real sales and debts.

| Client | Main record |
| Boat owner | Catch sales, fuel and crew payments |
| Processor or exporter | Export proceeds, supplier payments |
| Warehouse owner | Lease agreements, tax certificates |
| Supplier | Credit register, purchase bills |""",
     [("How is a jointly owned fishing boat taxed?",
       "The profit is shared, and each owner declares their share in their own return, supported by a record of sales and costs."),
      ("Do fish exporters deduct tax from boat owners?",
       "Processors and exporters may deduct tax on payments to suppliers. Keep certificates to claim the credit."),
      ("Is warehouse rent taxable?",
       "Yes. Rent from warehouses is taxable, and company tenants usually deduct tax at source.")])

page("mehmoodabad-karachi",
     "Mehmoodabad, between Korangi Road and the Manzoor Colony area, is a dense residential neighbourhood of working families, small shops and home-based workshops. Most of our clients here are first-time filers, small traders and salaried workers.",
     "Mehmoodabad Karachi tax help for first-time filers, small traders and salaried workers: NTN, simple returns and Active Taxpayers List status, done online.",
     """## Home-Based Workshops

Embroidery, tailoring, packaging and small assembly work done from homes in Mehmoodabad often supplies larger traders. Payments are irregular and partly in cash. A notebook or phone record of orders and payments is enough to support a return, and filing helps when larger customers ask for an NTN.

## Small Retailers

Corner shops, vegetable sellers and mobile shops serve the neighbourhood. For most, the important tax steps are keeping purchase bills and claiming the advance tax on electricity bills. Many earn below the taxable threshold, but filing still provides access to the lower filer rates.

## Salaried Residents

Residents work in nearby industrial areas, offices and the airport. Where tax is deducted from salary, filing can bring a refund; where it is not, filing still keeps them on the Active Taxpayers List.

## Why Filing Is Worth It

Being on the list lowers tax on bank cash withdrawals, vehicle registration and property purchases. For a family planning to buy a motorcycle or a small flat, filing first can save more than the cost of preparing the return.

| Resident | Benefit of filing |
| Home workshop | NTN for larger customers |
| Shopkeeper | Electricity bill tax credit |
| Salaried worker | Possible refund, lower filer rates |""",
     [("Do home-based workers need an NTN?",
       "It helps when supplying traders who ask for one, and filing even with low income gives access to filer rates."),
      ("What does filing cost compared with what I save?",
       "A salaried return is Rs 3,500 on our pricing page, while filer rates can save much more on property or vehicle purchases."),
      ("Can I file if I have no bank account?",
       "Yes, but opening one is strongly recommended because it creates a record of income and savings.")])

page("model-colony-karachi",
     "Model Colony near Karachi's airport is a settled residential area whose families have long ties to aviation, government service and small business. Clients here are mostly retirees, airline staff, small business owners and property owners.",
     "Model Colony Karachi tax help for retirees, aviation staff, small businesses and property owners: pension, rent and filer status, prepared online.",
     """## Retirees and Pensions

Many Model Colony households are headed by retired government or airline employees. Government pension is exempt, while pension from private schemes depends on the scheme's status. Bank profit and rent remain taxable, and filing keeps withholding on bank profit at the lower rate.

## Aviation and Airport Staff

Current airline, ground handling and airport employees receive salary with allowances such as shift and travel benefits. Checking the salary certificate component by component prevents both under-declaration and overpayment.

## Converting Houses into Rented Portions

As children move away, some families let out portions of their houses. Rent from individual tenants arrives without deduction, so the owner pays tax through the return. A tenancy agreement and rent record are the main documents.

## Small Businesses

Shops, pharmacies and small offices along Model Colony's main roads file business returns and claim electricity bill tax. Pharmacies and others selling goods should keep distributor invoices to support their cost of goods.

| Household | Typical need |
| Retiree | Exempt pension, taxable profit and rent |
| Airline employee | Correct treatment of allowances |
| Landlord | Rent declared, tax paid with return |
| Shop owner | Business return and credits |""",
     [("Is pension from a private airline taxable?",
       "It depends on whether the pension scheme is approved and on the Second Schedule limits. We check the scheme's status."),
      ("Do I pay tax on rent from a portion of my house?",
       "Yes, rent is taxable. If the tenant does not deduct tax, you pay it through your return."),
      ("Why should a retiree with exempt pension file?",
       "To stay on the Active Taxpayers List, which keeps tax on bank profit and property transactions lower.")])


def faq(slug, q, a):
    PAGES[f"blogs/tax-consultant-{slug}.html"]["faq"].append((q, a))


faq("korangi-karachi", "Can Korangi factories file withholding statements online?", "Yes. Withholding statements are filed on IRIS; we prepare them from payroll and supplier payment data each period.")
faq("landhi-karachi", "Do Landhi residents need to visit an FBR office to file?", "No. Returns are filed on IRIS; send your CNIC and documents on WhatsApp and we file after you approve the draft.")
faq("liaquatabad-karachi", "Is filing worthwhile for a small Liaquatabad shop below the taxable limit?", "Yes. It costs little, gives access to the lower filer rates and helps when opening bank accounts or seeking supplier credit.")
faq("malir-karachi", "Do I need an NTN to buy a plot in a Malir housing scheme?", "It is not always required, but being on the Active Taxpayers List lowers advance tax when the plot is transferred to you.")
faq("mauripur-karachi", "Can fishermen with irregular income file returns?", "Yes. A simple record of catch sales and costs is enough, and filing helps with bank accounts and boat financing.")
faq("model-colony-karachi", "How long does a pensioner's return take?", "Usually a day once we have the CNIC, pension statement, bank certificates and any rent details.")
