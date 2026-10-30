"""Islamabad pages, part A: city pages, Blue Area and E/F sectors."""

PAGES = {}


def page(slug, lead, desc, body, faq, kind="tax-consultant"):
    PAGES[f"blogs/{kind}-{slug}.html"] = {"lead": lead, "desc": desc, "body": body, "faq": faq}


page("islamabad",
     "Islamabad's taxpayers are dominated by federal employees, consultants, IT firms, embassies' local staff and property owners in the sectors and new housing schemes. The capital also has its own rules for sales tax on services and property, which differ from the provinces.",
     "Islamabad tax consultant: federal employees, IT and consulting firms, ICT sales tax on services, property and capital value tax, returns filed online.",
     """## The Capital's Own Tax Rules

Islamabad is not part of any province, so services provided in the Islamabad Capital Territory are taxed under the ICT tax on services law, administered by FBR rather than a provincial authority. A consultancy in Blue Area therefore files its services sales tax with FBR, while the same firm in Lahore would deal with the Punjab Revenue Authority. Property in Islamabad is taxed by the ICT Excise and Taxation department, and transfers involve Islamabad's capital value tax and CDA or society charges.

## Federal Employees

Thousands of residents work for federal ministries, regulators and attached departments. Their salary tax is deducted monthly; allowances, government accommodation and conveyance are reflected in the salary certificate. Many also own plots allotted through government employee housing schemes, which belong in the wealth statement from the date of allotment.

## IT and Consulting Firms

Islamabad has a large IT sector and many development-sector consultancies. Export receipts follow the IT export rules, local consulting income attracts deductions by clients, and ICT services sales tax may apply to local billing.

| Islamabad taxpayer | Main obligation |
| Federal employee | Salary return, allotted plots in wealth statement |
| IT exporter | Export proceeds records, PSEB registration |
| Local consultancy | Client deductions, ICT services sales tax |
| Property owner | ICT property tax, CVT on transfer |

## Working with Us

We work with Islamabad clients online and keep a yearly file for each household or business.""",
     [("Who collects sales tax on services in Islamabad?",
       "Services in the Islamabad Capital Territory are taxed under the ICT tax on services law, administered by FBR."),
      ("Do allotted government housing plots go in the wealth statement?",
       "Yes, from the date of allotment, at the amount paid so far."),
      ("Can I file from Islamabad without visiting an FBR office?",
       "Yes. Returns, registrations and notice replies are all handled online through IRIS.")])

page("islamabad",
     "Registering for an NTN in Islamabad is usually the first step for new consultants, IT freelancers, shop owners and families preparing to buy property in the capital. The process is online, and some Islamabad businesses also need registration for ICT sales tax on services.",
     "NTN registration in Islamabad: IRIS steps, documents for individuals and businesses, ICT services sales tax registration and getting on the ATL.",
     """## Who Registers in Islamabad

- **Consultants and contractors** working for development organisations, who are asked for an NTN before payment.
- **IT freelancers and software houses** receiving foreign payments.
- **Shopkeepers** in the markaz areas opening business bank accounts.
- **Families buying property** in sectors or housing schemes who want the lower advance tax rate as active filers.

## Online Registration Steps

1. Start registration on IRIS with your CNIC, an active mobile number and email.
2. Enter the verification codes received.
3. Fill in your address and income source; for a business, add the business name, address and activity.
4. Submit and download the NTN certificate.

## Business Details in the Capital

Islamabad addresses follow sector, sub-sector, street and house numbers. Use the same format as on your tenancy agreement or utility bill, because banks and FBR cross-check addresses during later registrations.

## ICT Sales Tax on Services

If your business provides taxable services in Islamabad, such as consulting, IT services to local clients or restaurant services, you may also need to register for the ICT tax on services, which FBR administers. We handle this registration alongside the NTN when needed. NTN registration is Rs 2,000 on our [pricing page](/pricing).""",
     [("Does a consultant in Islamabad need ICT sales tax registration?",
       "If the consulting services are taxable in the Islamabad Capital Territory and above the threshold, yes."),
      ("Will my NTN put me on the Active Taxpayers List?",
       "Only after you file a return; registration alone is not enough."),
      ("Can I register an NTN for my business in Islamabad online?",
       "Yes, through IRIS. Sole proprietors add the business to their individual profile; companies and AOPs get their own NTN.")],
     kind="ntn-registration")

page("blue-area-islamabad",
     "Blue Area along Jinnah Avenue is Islamabad's main business district, home to banks, corporate offices, law firms, consultancies and the shops and restaurants that serve them. Our Blue Area clients are firms, professionals and landlords of office floors.",
     "Blue Area Islamabad tax consultant for firms, law and consulting practices and office landlords: ICT services tax, withholding and returns, done online.",
     """## Offices and Professional Firms

Law firms, chartered accountancy practices, consultancies and recruitment agencies dominate Blue Area. Their corporate and government clients deduct income tax from fees, and their services can be taxable under the ICT tax on services. A schedule of each client's deductions, matched with invoices, is the backbone of the annual return.

## Firms as Employers

Office-based firms deduct salary tax from staff and file withholding statements. They also deduct tax when paying rent for their offices to individual landlords where the law requires it. Missing these deductions can make the firm liable for the tax it should have withheld.

## Owners of Office Floors

Office floors in Blue Area towers are let to banks, corporates and international organisations. Some tenants deduct tax from rent; diplomatic missions and certain international organisations may follow special arrangements. Rent remains taxable for the owner regardless.

## Restaurants and Retail

Restaurants on the avenue charge ICT sales tax on services and file income tax returns, while retail outlets deal with sales tax on goods.

| Client | Key issue |
| Law or consulting firm | Client deductions, ICT services tax |
| Employer | Salary and rent withholding |
| Office landlord | Rent declared, tenant deductions |
| Restaurant | ICT services tax and income tax |""",
     [("Do Blue Area law firms charge sales tax on services?",
       "Many professional services are taxable under the ICT tax on services law; we check your services and turnover."),
      ("Must a firm deduct tax on office rent?",
       "Prescribed persons paying rent to landlords must deduct tax under section 155 where it applies."),
      ("Is rent from an international organisation taxable?",
       "Yes, the rent is taxable income for the landlord even if the tenant does not deduct tax.")])

page("e7-islamabad",
     "E-7 sits at the foot of the Margalla Hills and is one of Islamabad's most exclusive residential sectors, with large houses owned by senior officials, business families and diplomats' landlords. Tax work here is about high-value property, rent and well-documented wealth.",
     "E-7 Islamabad tax help for owners of large houses, landlords to embassies and business families: rent, property valuation and wealth statements, online.",
     """## Houses Let to Diplomats and Organisations

Many E-7 houses are let to foreign missions, international organisations and their staff, often with rent paid in advance for a year or more. Advance rent should be declared under the rules for the year it relates to, and the tenancy agreement is the key document. Whether the tenant deducts tax depends on its status, but the rent is taxable for the owner in either case.

## High-Value Property

Property values in E-7 are among the highest in the country. Advance tax on purchase or sale, Islamabad's capital value tax on transfer and any section 7E calculation all rise with value. Owners with more than one property should review 7E annually.

## Senior Officials and Retired Officers

Retired officials living in E-7 have exempt government pensions but taxable rent and investment income. Filing keeps them on the Active Taxpayers List, which matters for withholding on profit and for any property sale.

## Documenting Wealth

Large houses, staff, foreign travel and children studying abroad are all visible. A wealth statement built from actual records, with clear sources for every asset, is the best defence against questions.

| Owner | Key point |
| Landlord to a mission | Advance rent and tenancy terms |
| Multi-property owner | Section 7E review |
| Retired official | Exempt pension, taxable rent |""",
     [("How is rent paid a year in advance taxed?",
       "It is generally taxed according to the period it relates to; the tenancy agreement determines the treatment."),
      ("Do embassies deduct tax from rent?",
       "It depends on the tenant's status and arrangements; the rent is taxable for the owner either way."),
      ("Is section 7E relevant for an E-7 owner?",
       "If you own more than one property above the aggregate limit and the extra property is not let out with rent declared, it can apply.")])

page("e-8-islamabad",
     "E-8 is closely associated with defence institutions and the families of serving and retired officers, alongside a small number of private residences and offices. Our E-8 clients are mainly officers, their families and retirees managing property and savings.",
     "E-8 Islamabad tax help for serving and retired officers and their families: salary, pension, allotted plots, rent and filer status, prepared online.",
     """## Serving Officers

Salary tax for serving officers is deducted at source, and their pay includes various allowances that are treated according to the rules for each allowance. Officers posted to Islamabad often own plots in defence housing schemes elsewhere, allotted over years of service. These belong in the wealth statement at the amounts paid.

## Retired Officers

Pensions of retired armed forces officers are exempt, as is commutation. Income from re-employment, consultancy or business after retirement, rent from houses and profit on savings are taxable.

## Spouses and Adult Children

Property and savings in a spouse's or child's name should be supported by gifts recorded in both wealth statements, or by their own income. Many families transfer plots within the family; each transfer should be documented.

## Selling Allotted Plots

When a defence scheme plot is sold, advance tax applies at registration and capital gains depend on the acquisition date. The allotment letter and payment receipts are essential.

| Situation | Key document |
| Serving officer | Salary certificate, allotment letters |
| Retired officer | Pension statement, savings certificates |
| Plot sale | Allotment letter, payment receipts |""",
     [("Is armed forces pension taxable?",
       "No, the pension and commutation are exempt, but other income such as rent and profit is taxable."),
      ("When do I show a plot allotted through a defence scheme?",
       "From allotment, at the amounts paid, and at full cost once fully paid."),
      ("How are plots transferred within the family declared?",
       "As a gift out of one wealth statement and into the other, with the transfer documents kept on file.")])

page("e11-islamabad",
     "E-11 is a privately developed sector along Margalla Avenue with apartment buildings, houses and busy commercial areas, popular with young professionals, students and investors. Our E-11 clients include flat owners, tenants, small businesses and IT workers.",
     "E-11 Islamabad tax help for flat owners, investors, small businesses and IT workers: rental income, apartment purchases and returns filed online.",
     """## Apartment Investors

E-11's apartment buildings attract investors who buy flats to let to students and professionals. Rent from individual tenants usually arrives without tax deducted, so the owner pays tax with the return or as advance tax. Flats bought from developers on instalments should appear in the wealth statement at the amount paid.

## Young Professionals and IT Workers

Many tenants work remotely for foreign companies or in Islamabad's IT firms. Remote workers who are resident in Pakistan declare their foreign salary or freelance income, with credit for any foreign tax where the rules allow.

## Small Businesses in the Commercial Areas

Cafes, salons, gyms and offices operate from E-11's markets. Services in Islamabad may attract ICT sales tax on services administered by FBR, and the businesses file income tax returns.

## Buying in E-11

For transfers from 1 July 2026, buyers pay advance tax of 1.25% under section 236K if on the Active Taxpayers List and 2.5% otherwise, in addition to Islamabad's charges on transfer.

| Client | Main point |
| Flat investor | Rent declared, instalments shown |
| Remote worker | Foreign income declared |
| Cafe or gym | ICT services tax and income tax |
| Buyer | 236K advance tax rate by status |""",
     [("Is rent from an E-11 flat let to students taxable?",
       "Yes. You declare the rent and pay tax with your return if the tenant does not deduct it."),
      ("Do remote workers in Islamabad pay Pakistani tax on foreign salary?",
       "If resident in Pakistan, yes, with credit for foreign tax where the rules allow."),
      ("Does an E-11 gym need to register for ICT services tax?",
       "If its services are taxable in Islamabad and above the threshold, registration with FBR for ICT services tax may be needed.")])

page("f-5-islamabad",
     "F-5 combines government offices, the Software Technology Park area and institutional buildings with a small residential section. Our F-5 clients are mainly IT companies, technology startups and professionals working in the sector's offices.",
     "F-5 Islamabad tax help for IT companies, startups and professionals: PSEB registration, IT export records, company returns and payroll withholding.",
     """## IT Companies and Startups

F-5's technology park has long hosted software houses and startups. Their foreign revenue follows the IT export rules, which depend on conditions such as receipt through banks and PSEB registration. Local revenue from Pakistani clients is taxed normally and may attract ICT sales tax on services.

## Startups as Private Limited Companies

Most startups incorporate early to accept investment. A company files its own return by 31 December for a June year end, keeps audited accounts as the law requires and deducts tax on salaries and certain payments. Founders who draw salaries declare them in their personal returns.

## Employee Stock Options and Bonuses

Some startups reward staff with stock options or performance bonuses. These are taxed under specific rules when options are exercised or benefits received, and should be reflected in the salary certificate.

## Professionals in Government Offices

Employees of government bodies in F-5 file standard salaried returns and declare any other income such as rent or profit.

| Client | Main obligation |
| Software house | Export proceeds records, PSEB, company return |
| Startup | Company return, payroll withholding |
| Employee with options | Correct valuation on exercise |""",
     [("Do F-5 software houses need PSEB registration?",
       "It is generally needed for the reduced treatment of IT exports and is renewed annually."),
      ("When is a startup's company return due?",
       "For a 30 June year end, by 31 December."),
      ("Are stock options taxable for employees?",
       "They are taxed under specific rules, usually when exercised or when the benefit is received.")])

page("f7-islamabad",
     "F-7 is one of Islamabad's best-known sectors, centred on Jinnah Super Market and surrounded by large houses, schools and offices. Our F-7 clients are retailers and restaurant owners in Jinnah Super, landlords and established families.",
     "F-7 Islamabad tax consultant for Jinnah Super retailers and restaurants, landlords and families: ICT services tax, rent and returns, filed online.",
     """## Jinnah Super Market Businesses

Bookshops, boutiques, restaurants and cafes in Jinnah Super serve a well-off clientele that pays largely by card. Restaurants charge sales tax on services under the ICT law administered by FBR. Larger retailers may fall under FBR's point-of-sale requirements. Either way, digital receipts make declared turnover easy to check, so the records must match.

## Houses Let to Offices and Schools

Some F-7 houses are let to schools, NGOs and offices. Institutional tenants deduct tax from rent where required, and owners claim those credits. Owners should keep the tenancy agreement and records of any advance rent.

## Established Families

Long-time F-7 families often own property in several sectors and in other cities. A schedule of all properties, with purchase dates and costs, helps with section 7E checks and with any future sale.

## Selling an F-7 House

For transfers from 1 July 2026 the seller pays advance tax under section 236C, 2.75% for active filers and 5.5% otherwise, plus Islamabad's transfer charges.

| Client | Key point |
| Restaurant | ICT services tax and income tax |
| Retailer | Card sales match the return |
| Landlord | Tenant deductions, advance rent |
| Family with several properties | Property schedule and 7E |""",
     [("Do Jinnah Super restaurants pay provincial sales tax?",
       "No, Islamabad restaurants charge sales tax on services under the ICT law, administered by FBR."),
      ("Is rent from a school tenant taxable?",
       "Yes; the school deducts tax where required and you claim it in your return."),
      ("What advance tax applies when selling an F-7 house?",
       "For transfers from 1 July 2026, 2.75% under section 236C for active filers and 5.5% for others.")])

page("f8-islamabad",
     "F-8 is home to the district courts, law chambers and offices along with residential streets and F-8 Markaz. Many of our F-8 clients are lawyers, legal practitioners, office-based professionals and residents of the sector.",
     "F-8 Islamabad tax help for lawyers, legal practices, professionals and residents: professional income, ICT services tax, withholding and returns online.",
     """## Lawyers and Legal Practices

The district courts in F-8 make it a centre for legal practice. Lawyers earn fees from individuals, which come without deduction, and from companies, banks and government bodies, which deduct tax. All fees are professional income, and the deducted tax is a credit. Legal services may also fall under the ICT tax on services.

## Chambers and Associates

Senior lawyers often share chambers with associates who are paid a fixed amount or a share of fees. Payments to associates are expenses for the senior lawyer and income for the associate; both should be documented.

## Office Professionals

Accountants, consultants and architects in F-8 Markaz serve government and private clients. Keeping a register of invoices with tax deducted by each client helps claim every credit.

## Residents

F-8's residents include officials and professional families. Their returns combine salary, practice income and property.

| Client | Main record |
| Lawyer | Fee register, client deduction certificates |
| Associate | Payments from chambers |
| Consultant | Invoice and deduction register |""",
     [("Are lawyers' fees from companies taxed at source?",
       "Yes, companies and government bodies deduct tax on fees; the lawyer claims the credit in the return."),
      ("How are payments to associate lawyers treated?",
       "As an expense for the senior lawyer and as income for the associate, supported by records."),
      ("Do legal services attract ICT sales tax?",
       "Many professional services are taxable under the ICT tax on services law, depending on turnover and the service.")])

page("f-9-islamabad",
     "F-9 is dominated by Fatima Jinnah Park, one of Islamabad's largest green spaces, with residential areas, sports facilities and nearby institutions. Our clients here are residents, sports and fitness businesses and event organisers.",
     "F-9 Islamabad tax help for residents, fitness and sports businesses and event organisers: income tax, ICT services tax and returns, done online.",
     """## Fitness and Sports Businesses

Gyms, sports academies and fitness trainers operating around F-9 earn membership fees and coaching income. These services may be taxable under the ICT tax on services, and the businesses file income tax returns showing fees less rent, equipment and staff costs.

## Event Organisers and Caterers

Events, fairs and festivals held in and around the park involve organisers, caterers and vendors. Organisers receiving payments from sponsors and companies may have tax deducted, and event and catering services can attract sales tax on services.

## Independent Trainers and Coaches

Personal trainers and coaches who work with several clients or gyms earn business income. A record of sessions and payments, and of fees paid to gyms for space, supports their returns.

## Residents

Residents with salaried jobs, pensions or rental income file standard returns and keep their wealth statements current.

| Client | Main point |
| Gym or academy | Membership income, ICT services tax |
| Event organiser | Sponsor payments and deductions |
| Personal trainer | Sessions and payments record |""",
     [("Does a gym in Islamabad charge sales tax on services?",
       "Fitness services can be taxable under the ICT tax on services law depending on turnover; we check your position."),
      ("Are sponsorship payments to event organisers taxed at source?",
       "Companies paying for services often deduct tax; the organiser claims it in the return."),
      ("How does a personal trainer file?",
       "As business income, with a record of sessions, payments and costs such as gym space and equipment.")])

page("f10-islamabad",
     "F-10 is a mature residential sector built around the busy F-10 Markaz, known for its shops, restaurants and offices. Our F-10 clients are markaz shopkeepers and restaurateurs, landlords and professional families.",
     "F-10 Islamabad tax help for markaz shops, restaurants, landlords and families: income tax, ICT services tax on food, rent and wealth statements online.",
     """## F-10 Markaz Businesses

Retail shops, salons and eateries in F-10 Markaz have high footfall and growing card payments. Restaurants charge ICT sales tax on services; retailers may be under FBR's point-of-sale rules if large enough. The annual return should match the turnover shown by card machines and POS data.

## Flats Above the Markaz

Many markaz buildings have apartments above shops, let to students and families. Rent is taxable for the owner. Where the building is jointly owned, each owner declares their share.

## Professional Families

F-10 residents often combine government or corporate salaries with rent from a second property. Both go in the return, and the second property in the wealth statement.

## Property Transfers

Islamabad transfers involve capital value tax and CDA charges, and federal advance tax under sections 236K and 236C. Being on the Active Taxpayers List before a transfer halves the federal advance tax rate.

| Client | Key point |
| Markaz restaurant | ICT services tax and income tax |
| Retailer | Card and POS turnover |
| Owner of flats above shops | Rent and joint ownership shares |""",
     [("Do F-10 Markaz shops need to use FBR's POS system?",
       "Only larger retailers meeting FBR's criteria must integrate; others still keep sales records."),
      ("How do co-owners of a markaz building declare rent?",
       "Each declares their share of the rent and of the building."),
      ("Does being a filer reduce tax on an Islamabad property transfer?",
       "Yes, federal advance tax under 236K and 236C is about half for persons on the Active Taxpayers List.")])

page("f11-islamabad",
     "F-11 is a popular residential sector with a lively markaz of shops, offices and restaurants, close to E-11 and Golra. Our F-11 clients are families, tenants, small business owners and freelancers working from home.",
     "F-11 Islamabad tax help for families, small businesses and home-based freelancers: returns, ICT services tax, rent and wealth statements, done online.",
     """## Home-Based Freelancers

F-11's houses and portions are home to many freelancers working for foreign clients. Their income, received through banks or payment platforms, is declared under the IT export rules where applicable, and balances held abroad at 30 June belong in the wealth statement.

## Small Businesses in F-11 Markaz

Pharmacies, salons, tutoring centres and food outlets in the markaz file business returns. Services taxable in Islamabad may require registration for the ICT tax on services.

## Portions Let Out

Many F-11 houses have upper and lower portions let separately. Rent from each portion is declared, and owners who pay little attention to small rents often face mismatches when tenants' data appears elsewhere.

## Families Buying Homes

Families moving up from rented portions to owned houses need clear funding records. Savings, gifts from parents and bank loans should all appear in the wealth statement.

| Client | Main point |
| Freelancer | Foreign receipts and wallet balances |
| Markaz business | Business return, ICT services tax |
| Landlord | Rent from each portion |
| Buyer | Funding sources recorded |""",
     [("Do freelancers in F-11 declare Payoneer balances?",
       "Yes, balances held in foreign wallets on 30 June are assets in the wealth statement."),
      ("Is rent from a single portion of a house taxable?",
       "Yes, rent from each portion is income from property."),
      ("Does a tuition centre in F-11 Markaz pay sales tax on services?",
       "It depends on the service and turnover under the ICT law; education services may be treated differently, so we check each case.")])
