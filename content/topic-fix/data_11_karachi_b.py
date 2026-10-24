"""Karachi area pages, part B: DHA phases, FB Area, Gulberg, Gulistan-e-Jauhar, Gulshan and Keamari."""

PAGES = {}


def page(slug, lead, desc, body, faq):
    PAGES[f"blogs/tax-consultant-{slug}.html"] = {"lead": lead, "desc": desc, "body": body, "faq": faq}


page("defence-phase-2-karachi",
     "Phase 2 is one of the older DHA Karachi phases, with established houses, a busy commercial area and many families who have owned their property for decades. Tax questions here are often about long-held property, inheritance among siblings and rent from commercial units.",
     "DHA Phase 2 Karachi tax help: long-held and inherited property, commercial rent, capital gains on older houses and family wealth statements, done online.",
     """## Property Held for Decades

Houses in Phase 2 were often bought long before today's capital gains rules existed. When such a house is sold, the acquisition date decides which rules apply, and a property bought many years ago is treated very differently from one bought after July 2024. Find the original allotment or transfer letter from DHA; it is the key document for the calculation.

## Inherited Houses Shared by Siblings

Many Phase 2 homes have passed to the next generation. Until the transfer to legal heirs is completed with DHA, ownership can be unclear for tax purposes. Each heir should show their share in their own wealth statement from the year of inheritance, and rent from a shared house should be split in the same proportion.

## Commercial Units on the Phase 2 Strip

Shops and offices in the commercial lanes are often let to banks, pharmacies and franchise outlets. These tenants usually deduct tax from rent. Landlords should collect the deduction certificates every year and match them with the rent received.

| Situation | Key document |
| Selling an old house | Original DHA allotment or transfer letter |
| Inherited share | Succession or heirship papers and DHA transfer |
| Commercial tenant | Tenancy agreement and tax deduction certificates |

## Working with Us

We handle Phase 2 files remotely: you share scans of the property papers and bank statements, and we prepare the returns for each family member so that shares, rent and gifts agree across all of them.""",
     [("Which rules apply when I sell a Phase 2 house bought in the 1990s?",
       "The capital gains treatment depends on the acquisition date. Older holdings follow earlier rules, which are usually more favourable than those for property bought after July 2024."),
      ("How do siblings declare rent from an inherited DHA house?",
       "Each declares their own share of the rent and shows their share of the house in their wealth statement."),
      ("Do bank tenants deduct tax from rent in DHA?",
       "Usually yes. The deduction is credited against the landlord's tax when the return is filed.")])

page("defence-view-karachi",
     "Defence View sits next to the DHA boundary along Korangi Road, with middle-income housing, apartment blocks and small businesses serving the surrounding industrial and residential areas. Clients here are mainly salaried workers, small traders and first-time property buyers.",
     "Defence View Karachi tax help for salaried workers, small traders and first-time buyers: returns, NTN, filer status before buying property, done online.",
     """## First-Time Property Buyers

Families in Defence View are often buying their first flat or house, sometimes with help from relatives abroad. Becoming an active filer before the purchase lowers the advance tax at registration: for transfers from 1 July 2026 the buyer pays 1.25% under section 236K if on the Active Taxpayers List and 2.5% otherwise. On a Rs 8 million flat that is Rs 100,000 against Rs 200,000.

## Workers at Nearby Industrial Units

Many residents work in the Korangi industrial area as supervisors, accountants and technicians. Their employers deduct salary tax, but they may still need to file to claim refunds, show savings or support a loan application. Overtime and bonuses paid late in the tax year are a common source of over-deduction.

## Small Shops and Workshops

Grocery stores, tailors, mobile repair counters and motorcycle workshops make up much of the local economy. Profit is usually modest, and many owners earn below the taxable threshold, but filing still helps when opening bank accounts or buying a vehicle.

| Need | What helps |
| Buying a flat | Filing before registration to pay the lower rate |
| Refund of salary tax | Salary certificate and bank statement |
| Small shop | Simple sales and purchase record |

## How to Start

Send your CNIC and recent bank statements on WhatsApp 0328-4675162. We register your NTN if needed and file your return so your name appears on the Active Taxpayers List before a planned purchase.""",
     [("How much do I save on a flat purchase by being a filer?",
       "For transfers from 1 July 2026, advance tax under section 236K is 1.25% for active filers and 2.5% for others, so on Rs 8 million you save Rs 100,000."),
      ("I earn below the taxable limit. Should I still file?",
       "Filing still puts you on the Active Taxpayers List, which lowers withholding on bank, vehicle and property transactions."),
      ("Can overtime cause too much tax to be deducted?",
       "Yes. Late-year overtime and bonuses can push monthly deductions above the real annual liability, and the excess can be claimed back in the return.")])

page("dha-karachi",
     "DHA Karachi covers several phases from the older inland blocks to the seafront, and its residents include business owners, senior professionals, overseas families and landlords. The common thread is high-value property and a lifestyle that FBR compares closely with declared income.",
     "DHA Karachi tax consultant: high-value property, rental income, overseas owners, section 7E and wealth statements that match lifestyle, prepared online.",
     """## Why DHA Residents Get Noticed

FBR's data on DHA Karachi is detailed: property transfers, vehicle registrations, electricity bills, school fees and foreign travel. When declared income is low compared with these, notices under section 111 or 122 follow. A wealth statement that accounts for actual living costs and the sources behind each asset is the best protection.

## Section 7E for Multiple Properties

Owners of more than one DHA property should check section 7E each year. One self-occupied house is excluded, and let-out property where rent is taxed is also excluded, but vacant plots and second homes above the aggregate value limit can attract deemed income tax. Many DHA owners hold an empty plot as an investment, which is exactly the case 7E targets.

## Overseas Owners

A large number of DHA houses belong to Pakistanis living in the Gulf, the UK or North America. Non-resident owners still owe tax on rent from the house and pay advance tax when selling. Filing a Pakistani return keeps them on the Active Taxpayers List and lowers that advance tax.

| Owner | Main issue |
| Resident with second plot | Section 7E check |
| Overseas owner letting the house | Rent declared in a Pakistani return |
| Business owner | Lifestyle versus declared income |

## Our Work with DHA Clients

We prepare the return and wealth statement together, check 7E for each property and draft replies if a notice has already arrived.""",
     [("Does section 7E apply to my vacant DHA plot?",
       "It can, if your total property value exceeds the limit and no exemption applies. Self-occupied homes and let-out property with rent declared are excluded."),
      ("Do overseas owners of DHA houses need to file in Pakistan?",
       "If they earn rent from the house or sell it, filing is needed for the income and keeps advance tax at the lower filer rate."),
      ("Why did I get a notice despite filing every year?",
       "Often because visible spending or new assets are higher than the declared income can explain. A detailed wealth statement usually resolves it.")])

page("dha-phase-1-karachi",
     "DHA Phase 1 is the original DHA Karachi phase near Korangi Road, with older houses, apartments and a commercial area that serves both residents and nearby offices. Many owners here are long-time residents, retired officers and small business families.",
     "DHA Phase 1 Karachi tax services: retired officers' pensions, older property sales, apartment rent and small business returns, filed online.",
     """## Retired Officers and Pensions

Phase 1 has many retired armed forces and government officers. Their government pension and commutation are exempt, but bank profit, rent and any post-retirement consulting income are taxable. Filing keeps them on the Active Taxpayers List, which keeps tax on savings profit at the lower rate.

## Converting Houses into Apartments

Some Phase 1 owners have rebuilt houses as multi-storey units and sell or rent individual floors. Selling floors one by one can turn an investment into a business activity, with different tax consequences. The intention, frequency and documentation of sales all matter, so planning before the first sale is worthwhile.

## Commercial Lanes

Small offices, clinics and shops operate from Phase 1's commercial area. Landlords receive rent, often with tax deducted by corporate tenants, and the businesses themselves file their own returns and, where they provide services, SRB returns.

| Phase 1 client | Typical filing |
| Retired officer | Exempt pension, taxable bank profit and rent |
| Owner selling floors | Advice on investment versus business treatment |
| Shop or clinic | Business or professional return |

## Getting Your Return Done

We need your CNIC, pension or salary certificate, bank certificates of tax deducted and property papers. Everything is shared on WhatsApp and the return is filed after you approve the draft.""",
     [("Is my military pension taxable?",
       "Government and armed forces pension is exempt, but bank profit, rent and other income are taxable and should be declared."),
      ("Is selling floors of my rebuilt house a business?",
       "It can be treated as business activity if sales are frequent and organised. Seek advice before selling the first unit."),
      ("Why should a retired officer file at all?",
       "To stay on the Active Taxpayers List, which lowers tax on bank profit and on any property sale or purchase.")])

page("dha-phase-2-karachi",
     "DHA Phase 2 Extension and the surrounding blocks are known for compact houses, apartment buildings and a dense commercial zone with offices, eateries and clinics. Tenants, small business owners and landlords make up most of our clients from this area.",
     "DHA Phase 2 Extension Karachi tax help: small offices and eateries, SRB registration, apartment rent and tenant refunds, prepared online by Kamboh Associates.",
     """## A Commercial Hub of Small Businesses

Phase 2 Extension has a high concentration of small offices, salons, cafes and consultancies. Many are run by first-time entrepreneurs who register with FBR but forget the Sindh Revenue Board. If the business provides taxable services in Sindh, SRB registration and monthly returns are required once the threshold is crossed.

## Landlords of Small Apartments

Owners of one or two small flats in the area often let them to young professionals. Rent from individuals usually arrives without tax deducted, so the landlord pays the whole tax through the return or quarterly advance tax. A simple rent register avoids surprises.

## Freelancers Working from Rented Flats

Phase 2 Extension attracts freelancers and remote workers. Their foreign receipts, platform statements and home office costs need to be organised for the return, and a filer status helps when banks process foreign payments.

| Who | Main obligation |
| Cafe or salon | FBR return and SRB returns |
| Small landlord | Rent declared, tax paid with return |
| Freelancer | Foreign receipts and expenses declared |

## How We Help

We register businesses with SRB where needed, prepare monthly returns and file the annual income tax return, all remotely.""",
     [("Does a small cafe in DHA need SRB registration?",
       "If it provides restaurant or other taxable services in Sindh above the threshold, yes. SRB registration is separate from FBR."),
      ("My tenant is an individual and deducts no tax. What do I pay?",
       "You pay the tax on rent yourself, through quarterly advance tax if required, and settle the balance with the return."),
      ("Can freelancers in DHA file without visiting an office?",
       "Yes. Platform statements, bank certificates and CNIC are shared online and the return is filed on IRIS.")])

page("dha-phase-6-karachi",
     "Phase 6 is among the most sought-after DHA Karachi addresses, with large houses, the Bukhari and Ittehad commercial areas and proximity to the seafront. Owners here often hold several properties, business interests and investments, which makes careful filing essential.",
     "DHA Phase 6 Karachi tax consultant: several properties, section 7E, business owners' returns and investment income, with wealth statements prepared carefully.",
     """## Several Properties in One Family

Phase 6 families frequently own a home, a second house let out and one or more plots elsewhere. Each property affects the return differently: rent is taxed, vacant property may fall under section 7E, and all of them must appear in the wealth statement at cost. A property schedule listing each asset with its purchase date and cost makes every later return simpler.

## Business Owners and Personal Withdrawals

Many residents own trading or manufacturing businesses. Money moved from the business to personal accounts, or used to buy personal assets, should be traceable to declared profit or to drawings from a company. Unexplained transfers are a frequent trigger for notices.

## Commercial Areas

Shops and restaurants in the Phase 6 commercial lanes pay high rents. Tenants that are companies deduct tax from rent, and landlords claim those credits. Restaurants also deal with SRB for sales tax on services.

| Asset | Treatment |
| Home | Wealth statement only |
| Let-out house | Rent taxed, tenant credits claimed |
| Vacant plot | Possible section 7E |
| Business share | Profit or dividends declared |

## Our Service

We build a property schedule on the first engagement and update it every year, so returns, 7E checks and any sale calculation use the same figures.""",
     [("Do I pay section 7E on my DHA Phase 6 home?",
       "No, one self-occupied house is excluded. Other properties may be covered depending on use and total value."),
      ("How should business owners record money taken from the business?",
       "As drawings from a sole proprietorship or as salary, dividends or loans from a company, with a bank trail for each transfer."),
      ("What is a property schedule?",
       "A list of every property with purchase date, cost, use and income, kept updated so that returns and sale calculations stay consistent.")])

page("fb-area-karachi",
     "Federal B Area in central Karachi combines residential blocks with one of the city's older industrial estates, along with markets around Water Pump and Ayesha Manzil. Our clients here include factory owners, traders, salaried staff and landlords.",
     "FB Area Karachi tax help: industrial units, traders, salaried staff and landlords, with sales tax, withholding statements and returns filed online.",
     """## Small Manufacturers in the Industrial Area

FB Area's industrial estate hosts garment, printing, plastic and food units. Manufacturers generally need a federal sales tax registration regardless of turnover, file monthly sales tax returns and, as employers, deduct salary tax. Input tax claims depend on registered suppliers, so supplier checks are part of each month's work.

## Traders Around Water Pump and Ayesha Manzil

Retail and wholesale traders in these markets deal heavily in cash. Electricity bill tax, bank deposits and stock records together form the basis of an accurate return. Traders who supply registered manufacturers may be asked for an NTN and may have tax deducted when paid.

## Families and Landlords

FB Area's older houses often have upper portions let to tenants. Rent from individual tenants is usually received without deduction, so the owner pays the tax with the return.

| Client | Monthly or annual work |
| Manufacturer | Sales tax return, withholding statements, annual return |
| Trader | Annual return with profit and electricity credits |
| Landlord | Rent in the annual return |

## How We Work

Monthly sales tax and withholding work is handled from documents shared each month; the annual return pulls everything together.""",
     [("Does a small garment unit in FB Area need sales tax registration?",
       "Manufacturers are generally required to register for federal sales tax, subject to limited exceptions such as cottage industry rules."),
      ("Why do manufacturers lose input tax claims?",
       "Usually because suppliers are unregistered, not active, or did not declare the sale in their own returns."),
      ("Is rent from an upper portion taxable?",
       "Yes. Rent is taxable income and is declared in the return even if the tenant does not deduct tax.")])

page("gulberg-karachi",
     "Gulberg Town in Karachi includes Gulberg Chowrangi, Azizabad and nearby blocks, with dense housing, schools, clinics and a large number of small traders and salaried families. Most of our clients from here are first-time filers and small businesses.",
     "Gulberg Karachi tax services for first-time filers, small traders, clinics and salaried families: NTN, returns and filer status, filed online by Kamboh Associates.",
     """## First-Time Filers

Many Gulberg residents start filing because a bank, employer or property dealer asks for an NTN. The first return is the most important one: it sets the opening wealth statement, listing every asset already owned. Declaring a house, motorcycle, gold and bank balances accurately at the start prevents questions later.

## Clinics and Medical Stores

Small clinics and pharmacies are common in the area. Doctors declare consultation fees as professional income; pharmacies, which sell goods, may also face sales tax requirements depending on turnover and structure. Purchase invoices from distributors are the main record for a pharmacy's profit.

## School Owners

Private schools in residential houses are a feature of the area. Fee income is business income, and the school as an employer deducts tax from teachers whose salaries cross the threshold. A school also needs clear records of fee concessions and arrears.

| Client | First step |
| New filer | Opening wealth statement listing current assets |
| Pharmacy | Purchase invoices and stock record |
| Private school | Fee register, payroll and withholding |

## Starting Out

Send your CNIC, bank statement and a list of assets you own. We register you if needed and prepare the first return with a complete opening wealth statement.""",
     [("What should my first wealth statement include?",
       "Everything you own on 30 June: property, vehicles, gold, bank balances, cash and any loans you owe."),
      ("Do private schools deduct tax from teachers?",
       "Yes, as employers they deduct salary tax where a teacher's annual salary is above the taxable threshold."),
      ("Is a small pharmacy taxed like a clinic?",
       "No. A pharmacy sells goods and is taxed on trading profit, while a clinic earns professional fees.")])

page("gulistan-jauhar-karachi",
     "Gulistan-e-Jauhar is a large residential district of high-rise apartments, gated blocks and busy commercial roads near Johar Mor. Its residents are mostly salaried professionals, university staff, freelancers and families who own flats as investments.",
     "Gulistan-e-Jauhar Karachi tax help for salaried professionals, freelancers and flat owners: refunds, rental income and wealth statements, filed online.",
     """## Apartment Ownership and Rent

Owning a second flat in a Jauhar tower and letting it out is a common investment. The rent is taxable, building maintenance charges are not deductible in the way many owners assume, and the flat must be in the wealth statement at its purchase cost. If the flat was bought on instalments from a builder, show the amount paid to date until possession.

## Flats Bought on Instalments

Many Jauhar projects are sold on booking and instalments. Each instalment paid is part of your investment and should be shown in the wealth statement as an advance against property until the flat is handed over. The builder's payment receipts are the evidence.

## University Staff and Teachers

Faculty at nearby universities have salary tax deducted and may also earn from visiting lectures or consulting. Full-time teachers and researchers at recognised institutions may qualify for a reduction in tax, depending on current rules, which is worth checking each year.

| Situation | Record to keep |
| Flat bought on instalments | Builder receipts, allotment letter |
| Let-out flat | Tenancy agreement, rent record |
| Visiting faculty income | Payment advices from each institution |

## Getting Help

We file for Jauhar residents remotely; send your documents on WhatsApp and approve the draft before submission.""",
     [("How do I show a flat bought on instalments?",
       "Show the total paid to date as an advance for property in the wealth statement until possession, then as the property at full cost."),
      ("Is income from visiting lectures taxable?",
       "Yes. Declare it with your salary; any tax deducted by the institution is claimed as a credit."),
      ("Do teachers get a tax reduction?",
       "Full-time teachers and researchers at recognised institutions have had a reduction under the Second Schedule; check whether it applies in your tax year.")])

page("gulshan-block-1-karachi",
     "Block 1 of Gulshan-e-Iqbal lies near the University Road side of Gulshan, with apartment buildings, older houses and shops serving students and families. Our clients here include shop owners, landlords letting rooms and flats, and salaried residents.",
     "Gulshan-e-Iqbal Block 1 Karachi tax help: rooms and flats let to students, small shops, salaried returns and filer status, handled online.",
     """## Letting Rooms and Portions to Students

Proximity to universities means many Block 1 households let rooms or portions to students. Even small monthly amounts add up to taxable rent over the year. Keep a simple register of who stayed, for how long and what was paid, and declare the total as rent.

## Stationery, Photocopy and Food Shops

Small shops that serve students operate on thin margins with seasonal peaks around exams and admissions. Records of purchases from wholesalers and a record of daily takings are enough to work out profit. Commercial electricity bill tax is a credit to claim.

## Salaried Families

Many residents work in offices along Shahrah-e-Faisal and University Road. Besides salary, they often have savings certificates and bank profit. Including all certificates of tax deducted ensures they do not overpay.

| Client | Key point |
| Room landlord | Total yearly rent declared |
| Student-area shop | Purchase records and daily takings |
| Salaried family | Salary plus profit on savings |

## How to Begin

WhatsApp your CNIC and documents to 0328-4675162 and we prepare the return within a day or two.""",
     [("Is rent from rooms let to students taxable?",
       "Yes. All rent received over the year is declared as income from property."),
      ("What records does a small stationery shop need?",
       "Wholesale purchase bills, a daily takings record and electricity bills showing advance tax."),
      ("Do I declare profit on savings certificates?",
       "Yes, with the tax already deducted shown as tax paid, so you are not charged twice.")])

page("gulshan-block-7-karachi",
     "Gulshan-e-Iqbal Block 7 is a settled residential block with bungalows, apartment buildings and nearby markets, home to many professional and business families. Clients from Block 7 typically need returns that combine salary or business income with property and investments.",
     "Gulshan-e-Iqbal Block 7 Karachi tax services: combined salary, business and property income, investments and family wealth statements, prepared online.",
     """## Families with Mixed Income

A typical Block 7 household might have one member in salaried employment, another running a shop or office, a let-out portion and savings in certificates or mutual funds. Each income head has its own rules, and the household's wealth statements must agree on shared assets and gifts.

## Mutual Funds and Savings

Investors in mutual funds receive dividends with tax deducted and may realise capital gains on redemption. Fund managers issue annual tax certificates; collect them for every fund. National Savings certificates and bank deposits also come with tax certificates that should be claimed.

## Business Owners Working from Gulshan

Small trading and service businesses run by Block 7 residents often operate from offices in Gulshan's commercial areas. Business profit, rent paid and staff salaries need records; if services are provided in Sindh, SRB rules may apply.

| Income | Document |
| Salary | Employer's salary certificate |
| Mutual fund | Annual tax certificate from each fund |
| Business | Profit and loss summary, bank statements |
| Rent | Tenancy agreement, rent record |

## Our Approach

We prepare returns for every earning member together, so gifts and shared assets match across all statements.""",
     [("Are mutual fund dividends taxed?",
       "Yes, through withholding at source. Collect each fund's annual tax certificate and declare the income."),
      ("Why prepare family returns together?",
       "Gifts, joint property and shared expenses appear in several statements and must match."),
      ("Do I need SRB registration for a small consultancy?",
       "If it provides taxable services in Sindh above the threshold, yes, alongside the FBR return.")])

page("gulshan-iqbal-karachi",
     "Gulshan-e-Iqbal is one of Karachi's largest middle-class districts, stretching along University Road with residential blocks, universities, hospitals and markets. Its taxpayers are as varied as the city: salaried staff, teachers, doctors, traders and landlords.",
     "Gulshan-e-Iqbal Karachi tax consultant for salaried staff, teachers, doctors, traders and landlords: returns, refunds and wealth statements filed online.",
     """## A District of Salaried Professionals

Gulshan's residents work across Karachi in banks, hospitals, universities and corporate offices. For them the main tax tasks are claiming every credit, from tax on bank profit, mobile bills and vehicle token to tax deducted on salary, and keeping a wealth statement that tracks flats, plots and savings bought over the years.

## Hospitals and Doctors

Gulshan has several hospitals and many private clinics. Doctors working in more than one place receive fees from each, often with tax deducted. All certificates should be gathered, and private practice income added, before filing.

## Traders and Market Shopkeepers

Shopkeepers in Gulshan's markets sell everything from electronics to garments. Profit is calculated from purchases, sales and closing stock, and electricity bill tax is claimed as credit. Traders who sell to companies may face deduction of tax on payments.

| Gulshan taxpayer | Credits to claim |
| Salaried | Salary tax, bank profit tax, mobile and vehicle tax |
| Doctor | Hospital deductions |
| Shopkeeper | Electricity bill tax, deductions by corporate buyers |

## Filing with Us

We file for Gulshan residents remotely and keep a yearly record so that next year's return starts from this year's figures.""",
     [("What credits do salaried people often forget?",
       "Tax deducted on bank profit, mobile phone bills, vehicle token and electricity bills, all of which reduce the final liability."),
      ("How do doctors with several hospitals file?",
       "Collect tax certificates from each hospital and declare all fees together with private practice income."),
      ("Can a Gulshan shopkeeper claim electricity bill tax?",
       "Yes. The advance income tax on a commercial electricity bill is a credit in the return.")])

page("keamari-karachi",
     "Keamari is home to Karachi Port, oil terminals and the clearing, shipping and transport businesses that serve them. Our Keamari clients are mostly clearing and forwarding agents, transporters, port-linked traders and salaried port staff.",
     "Keamari Karachi tax help for clearing agents, shipping and transport businesses, port traders and staff: returns, sales tax and withholding, handled online.",
     """## Clearing and Forwarding Agents

Clearing agents receive large amounts from importers, most of which pass on to customs, port and shipping charges. Only the agent's commission and service charges are income. Separating reimbursed expenses from fees in the books is the most important step in getting the return right. Agency services in Sindh are also generally subject to SRB sales tax on services.

## Transporters and Goods Carriers

Trucking and container transport companies around Keamari pay advance tax with vehicle tax and may have tax deducted on freight by corporate clients. These deductions are credits. A trip register linking each freight bill to a payment makes the return straightforward.

## Port Staff and Shipping Company Employees

Salaried employees of the port, terminals and shipping lines have tax deducted monthly and often receive allowances and overtime. Their salary certificate should show each component so that exempt and taxable parts are treated correctly.

| Client | Main point |
| Clearing agent | Separate reimbursements from fees; SRB on services |
| Transporter | Freight records and tax credits |
| Port employee | Allowances and overtime on the salary certificate |

## Working with Us

We handle Keamari files remotely, including monthly SRB returns for agents and annual returns for all.""",
     [("Is all the money a clearing agent receives taxable?",
       "No. Amounts passed on for duties, port and shipping charges are reimbursements; the agent's fees and commission are the taxable income."),
      ("Do clearing agents pay SRB sales tax?",
       "Agency and similar services in Sindh are generally taxable under the Sindh sales tax on services law."),
      ("Can transporters claim tax deducted on freight?",
       "Yes. Tax deducted by clients and advance tax paid with vehicle tax are claimed in the annual return.")])


def more(slug, text):
    PAGES[f"blogs/tax-consultant-{slug}.html"]["body"] += "\n\n" + text


more("dha-phase-1-karachi", """## Documents for Phase 1 Clients

Pension book or bank pension statement, certificates of tax deducted on savings, DHA transfer letters for any property, and tenancy agreements for let-out portions. With these, a return for a retired resident usually takes a day, and we explain each figure before it is submitted.""")
more("dha-phase-2-karachi", """## Moving In and Out of the Area

Phase 2 Extension has a high turnover of tenants. When you move, update your address on IRIS so notices reach you, and keep the old tenancy agreement with your records. If you paid a large security deposit, it is an asset in your wealth statement until it is returned, and its refund explains the cash you receive back.""")
more("dha-phase-6-karachi", """## Selling a Phase 6 Property

For transfers from 1 July 2026, the seller pays advance tax of 2.75% under section 236C if on the Active Taxpayers List and 5.5% otherwise, on the higher of the price and the FBR value. Capital gains tax then depends on when the property was acquired. Having the original purchase papers and payment trail ready shortens the sale and the later return.""")
more("fb-area-karachi", """## Workers and Contract Labour

Factories in FB Area often hire through contractors. Payments to labour contractors can require tax deduction, and the contractor's own registration status affects the rate. Keeping contracts, invoices and deduction records for each contractor protects the factory's expense claims if FBR later reviews the payroll costs.""")
more("gulberg-karachi", """## Families Receiving Help from Abroad

Many Gulberg families receive money from relatives in the Gulf. Remittances through banks are not the receiver's taxable income, but the first return should show them in the wealth reconciliation when they paid for a house, motorcycle or furniture. Keep the bank advice for each transfer, and note what it was used for, so the record is complete.""")
more("gulistan-jauhar-karachi", """## Freelancers in Jauhar's Towers

The area's apartment towers are home to many freelancers and remote workers. Their foreign receipts arrive through Payoneer or direct bank transfers, and banks deduct tax on some of these receipts. Keeping platform earnings reports alongside bank certificates makes it simple to declare income correctly and claim the deductions.""")
more("gulshan-block-1-karachi", """## Students Who Start Earning

Students living in Block 1 who begin freelancing or tutoring should register early. A first return with a small income and a simple wealth statement costs little and establishes a record that helps with bank accounts, visas and future scholarships abroad. If income is below the taxable threshold, no tax is due, but the return still counts.

Tuition given privately at home is also income; keep a note of what each student paid.""")
more("gulshan-block-7-karachi", """## Gifts Between Family Members

Parents in Block 7 often help adult children buy flats or cars. A gift should be shown as an outflow in the parent's wealth statement and an inflow in the child's, ideally made through a bank transfer with a short written note. Matching entries on both sides prevent either statement from looking unexplained.""")
more("gulshan-iqbal-karachi", """## Property Purchases in Gulshan

Flats and portions in Gulshan change hands frequently. For transfers from 1 July 2026, buyers pay advance tax under section 236K at 1.25% if on the Active Taxpayers List and 2.5% otherwise, and sellers pay 2.75% or 5.5% under section 236C. Filing before a planned purchase or sale is one of the simplest ways to cut its cost.""")
more("keamari-karachi", """## Port-Linked Traders

Traders who buy imported goods directly from port terminals or bonded warehouses deal with customs-stage taxes passed on by importers. Their purchase invoices, showing the sales tax and duties included, support both the cost in the income tax return and any input tax claim if they are registered for sales tax.""")
