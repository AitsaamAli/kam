"""Islamabad pages, part C: housing schemes, outskirts and named localities."""

PAGES = {}


def page(slug, lead, desc, body, faq):
    PAGES[f"blogs/tax-consultant-{slug}.html"] = {"lead": lead, "desc": desc, "body": body, "faq": faq}


page("bahria-town-islamabad",
     "Bahria Town's phases along the Islamabad Expressway and GT Road form one of the largest private communities in the twin cities, with houses, apartments, commercial areas and a big investor base. Our Bahria Town clients are residents, investors in files and plots, and business owners in its commercial zones.",
     "Bahria Town Islamabad tax help for residents, file and plot investors and commercial businesses: property records, rent, transfers and returns, online.",
     """## Investors in Files and Plots

Much of Bahria Town's activity involves files and plots bought on instalments and traded before possession. A file is an asset from the first instalment and should appear in the wealth statement at the amount paid. Selling a file at a profit is a taxable gain; frequent trading can look like a business. Bahria Town's own transfer records and payment receipts are the key documents.

## Residents and Rented Houses

Many houses in the phases are let to families and expatriates. Rent is taxable each year; the owner pays tax through the return if the tenant does not deduct it. Owners living abroad still declare the rent in a Pakistani return.

## Commercial Areas

Shops, restaurants and offices in Bahria's commercial zones file business returns. Restaurants and some services may fall under sales tax on services. Because Bahria Town spans Islamabad and Rawalpindi district boundaries, check whether ICT or Punjab rules apply to services provided from your location.

## Maintenance Charges

Residents pay maintenance and utility charges to the developer. These are household expenses for a self-occupied home and are part of the personal expenses figure in the wealth statement.

## Getting Started

Share your allotment or transfer letters, payment receipts, tenancy agreements and income records. We prepare a return and wealth statement that account for each property and file.""",
     [("Is profit on selling a Bahria Town file taxable?",
       "Yes. The gain is taxable, and frequent trading may be treated as a business."),
      ("Which services tax applies to a business in Bahria Town?",
       "It depends on whether your location falls in the Islamabad Capital Territory or Punjab; ICT services tax or Punjab Revenue Authority rules then apply."),
      ("Do overseas owners declare rent from a Bahria house?",
       "Yes, rent from Pakistani property is taxable in Pakistan and declared in a Pakistani return.")])

page("bani-gala-islamabad",
     "Bani Gala is a hillside residential area overlooking Rawal Lake, known for large houses, farmhouses and a history of construction outside approved plans. Our Bani Gala clients are owners of houses and farmhouses and families building in the area.",
     "Bani Gala Islamabad tax help for house and farmhouse owners: property records, regularisation costs, rent and wealth statements, prepared online.",
     """## Houses Built on Private Land

Many Bani Gala homes were built on privately purchased land rather than in a CDA sector. Ownership records are land revenue documents (fard and mutation) rather than CDA allotments. These records, together with construction costs, establish the cost of the house for the wealth statement.

## Regularisation and Approval Costs

Owners who pay fees to regularise construction or obtain approvals add these costs to the property's cost. Keep receipts for every payment to the authority.

## Farmhouses and Event Venues

Some properties are used as event venues or rented out for weekends. Event rental income is taxable and should be recorded per booking. Farmhouses with orchards or livestock may also have agricultural income, which is declared as exempt in the federal return if it qualifies.

## Selling a Bani Gala Property

Buyers should confirm the land record and approval status before paying. Advance tax applies at transfer, and the seller's capital gains depend on when the property was acquired.

## Getting Started

Share the land record, construction receipts, approval or regularisation payments and any rental records. We prepare a wealth statement that reflects the full cost and the income from the property.""",
     [("Do regularisation fees add to my house's cost?",
       "Yes, fees paid to regularise or approve construction form part of the property's cost."),
      ("Is renting out my farmhouse for events taxable?",
       "Yes, event rental income is taxable and should be recorded for each booking."),
      ("What documents prove ownership of a Bani Gala house?",
       "Land revenue records such as the fard and mutation, along with construction and approval records.")])

page("cbr-town-islamabad",
     "CBR Town is a cooperative housing society established for employees of the Central Board of Revenue, now FBR, and today houses tax officials, retirees and other residents. Our CBR Town clients are serving and retired officers, their families and later buyers.",
     "CBR Town Islamabad tax help for serving and retired revenue officers, their families and later buyers: salary, pension, property and wealth statements.",
     """## Serving Officers

Officers of FBR and its field formations living in CBR Town file salaried returns like any other federal employee. Their salary certificates include allowances under federal pay rules. Like everyone else, they should declare all assets fully; officials are expected to set an example in their own filings.

## Retired Officers

Pensions are exempt, and many retirees have income from rent or savings. Some take up consulting or practice as tax advisers after retirement, which is professional income to be declared.

## Members and Later Buyers

Plots in the society were first allotted to members, and many have since been sold to buyers from outside the service. Buyers should keep the society's transfer records and pay advance tax at registration.

## Family Property

Retired members often transfer houses to children. Gifts should be documented and shown in both parents' and children's wealth statements.

## Getting Started

Share your salary or pension statement, society allotment or transfer letters, and any income records. We prepare the return and wealth statement remotely.""",
     [("Can retired tax officers practise as advisers?",
       "Retired officers who advise clients earn professional income, which is declared in their returns."),
      ("Do buyers from outside the service face different rules?",
       "No, the same federal advance tax applies at registration, along with the society's transfer requirements."),
      ("How is a house transferred to children recorded?",
       "As a gift in both the parent's and the child's wealth statements, supported by the transfer documents.")])

page("dha-islamabad",
     "DHA Islamabad's phases along GT Road and the Expressway attract serving and retired officers, overseas Pakistanis and investors, with many plots still held for future construction. Our DHA Islamabad clients are allottees, investors and residents.",
     "DHA Islamabad tax help for officer allottees, overseas owners and investors: plots, section 7E, transfers and rent, with wealth statements prepared online.",
     """## Officer Allottees

Serving and retired officers often hold DHA plots allotted through service schemes, paid in instalments over years. The total paid each year is shown in the wealth statement. Allotment letters and DHA payment records are the key documents.

## Overseas Owners

A large share of DHA Islamabad plots and houses belong to Pakistanis living abroad. Non-residents with rent or sales from DHA property declare them in a Pakistani return, and filing keeps their advance tax on transfers at the lower rate.

## Investors and Section 7E

Investors holding several DHA plots should check section 7E each year. Vacant plots above the aggregate value limit, without an exemption, can attract deemed income tax.

## Selling a DHA Plot

Advance tax under section 236C is collected at transfer, and capital gains depend on when the plot was acquired. DHA's own transfer process runs alongside, and its records should be kept.

## Getting Started

Share allotment letters, DHA payment schedules, transfer documents and any tenancy agreements. We prepare a property schedule and the return.""",
     [("Do I show a DHA plot I am still paying for?",
       "Yes, at the instalments paid to date, as an asset in your wealth statement."),
      ("Does section 7E apply to my DHA plots?",
       "It can apply to vacant plots if your total property value is above the limit and no exemption applies."),
      ("Can overseas owners sell DHA plots at filer rates?",
       "Yes, if they are on the Active Taxpayers List by filing a Pakistani return.")])

page("f-12-islamabad",
     "F-12 lies at the western end of the F series, near the Margalla foothills, where development has been slower and much of the area remains under acquisition and planning. Our F-12 clients are original landowners, affectees and plot holders awaiting development.",
     "F-12 Islamabad tax help for landowners, affectees and plot holders awaiting development: compensation, allotments and property records, prepared online.",
     """## Land Acquisition and Compensation

Sectors in this part of Islamabad have involved acquisition of private land, with compensation paid to landowners and, in some cases, developed plots allotted to affectees. Compensation for land and the plots received each have their own treatment, and the acquisition award and allotment documents establish the facts.

## Affectees' Plots

Plots allotted to affectees are assets from the date of allotment. When sold, the cost and acquisition date determine capital gains. Many affectees sell their entitlements before development; these sales should be documented and declared.

## Plot Holders Waiting for Development

Holders of F-12 plots may wait years for development. Payments for development charges add to cost. Holders with several properties should consider section 7E.

## Getting Started

Share the acquisition award, compensation receipts, allotment letters and payment records. We advise on the treatment of each step and prepare the return.""",
     [("Is compensation for acquired land taxable?",
       "It depends on the land's nature and the law at the time; agricultural land compensation is often treated differently. We review each award."),
      ("Can affectees sell their plot entitlements?",
       "Usually yes, subject to the authority's rules; the sale is declared and advance tax may apply at transfer."),
      ("Do development charges count as cost?",
       "Yes, they add to the plot's cost in the wealth statement.")])

page("farash-town-islamabad",
     "Farash Town is a CDA-developed residential scheme on Islamabad's outskirts, created to provide affordable housing for lower-income families. Our Farash Town clients are working families, small shopkeepers and first-time filers.",
     "Farash Town Islamabad tax help for working families, small shopkeepers and first-time filers: simple returns, NTN and Active Taxpayers List status.",
     """## Families in Affordable Housing

Many residents bought small houses or plots in Farash Town through the scheme. The house is the family's main asset and belongs in the wealth statement at cost. Instalments paid to the authority are part of that cost.

## Shopkeepers

Small shops serve the neighbourhood with groceries, mobile services and repairs. Purchase bills, monthly sales totals and electricity bills are enough for a simple return.

## Workers and Drivers

Residents work as drivers, security guards and factory workers across the twin cities. Most earn below the taxable threshold, but filing gives them access to lower filer rates on bank transactions and vehicles.

## First Returns

A first return needs a CNIC, bank statement and a list of what you own. It is short and inexpensive and establishes a tax record.

## Getting Started

Send your CNIC, bank statement and house documents on WhatsApp 0328-4675162. We prepare the return in a simple format and explain each figure.""",
     [("Do I need to file if I earn below the taxable limit?",
       "It is not always required, but filing gives access to lower filer rates and builds a record."),
      ("How do I show my Farash Town house?",
       "At its cost, including instalments paid, in your wealth statement."),
      ("What does a first return cost?",
       "A salaried return is Rs 3,500 on our pricing page; most first returns for residents are simple.")])

page("golra-islamabad",
     "Golra, home to the historic Golra Sharif shrine and old railway station, sits near E-11 and F-11 and combines an old village core with newer housing and markets. Our Golra clients are long-time residents, shop owners and families who have sold or developed ancestral land.",
     "Golra Islamabad tax help for long-time residents, shopkeepers and families selling or developing ancestral land: returns, land records and filer status.",
     """## Ancestral Land and Development

Many Golra families owned land long before neighbouring sectors were developed. Selling part of this land, or developing it into plots or shops, brings tax questions about cost, acquisition date and shares among heirs. Land revenue records establish each person's share.

## Shopkeepers Serving Visitors

Shops and eateries near the shrine serve visitors, with busy days around religious events. Cash sales should be recorded daily, because takings vary sharply.

## Residents Working in the City

Golra's residents work in nearby sectors and offices. Salaried members file standard returns and declare any rent from portions of family houses.

## Rent from Shops on Family Land

Families who build shops on their land and let them out receive rent, which is taxable. Each co-owner declares their share.

## Getting Started

Share your land records, any sale documents, shop tenancy agreements and income records. We prepare returns for family members so that shares and proceeds agree across all of them.""",
     [("How are proceeds from selling ancestral land split for tax?",
       "Each heir declares their own share of the sale, based on the land record, in their own return."),
      ("Is rent from shops on family land taxable?",
       "Yes, and each co-owner declares their share of the rent."),
      ("Should shopkeepers near the shrine record daily sales?",
       "Yes, because takings vary widely; daily records support an accurate annual profit.")])

page("margalla-hills-islamabad",
     "The Margalla Hills frame Islamabad's northern edge, and the residential areas, eateries and tourism businesses along the hillside roads and nearby villages depend on them. Our clients here are hospitality operators, residents of hillside villages and owners of homes near the hills.",
     "Margalla Hills Islamabad tax help for hospitality and tourism operators, hillside village residents and homeowners: business returns, rent and records.",
     """## Hospitality and Tourism Businesses

Restaurants, tea stalls and guide services around the hill trails and viewpoints serve visitors, with peaks on weekends and holidays. Restaurant services are taxable under the ICT tax on services, and the businesses file income tax returns. Daily sales records are important where cash dominates.

## Hillside Villages

Residents of villages within or near the national park often combine livestock and small farming with jobs in the city. Agricultural income is declared as exempt in the federal return; salaries are taxed normally.

## Homes Near the Hills

Houses in the sectors bordering the hills are high-value. Owners letting them to diplomats or organisations declare rent, and those selling pay advance tax at transfer.

## Environmental Rules

Activities within the national park are restricted, and businesses there may face closures or relocation. Assets lost or written off as a result should be documented, because they affect the business's accounts.

## Getting Started

Share sales records, tenancy agreements or salary certificates, and we prepare the appropriate return.""",
     [("Do restaurants near the Margalla trails charge sales tax?",
       "Restaurant services in Islamabad are generally taxable under the ICT tax on services law."),
      ("How do hillside village residents declare livestock income?",
       "Small-scale livestock linked to farming is generally declared with agricultural income as exempt; commercial operations are business income."),
      ("What if my business was closed under park rules?",
       "Document the closure and any assets written off; these affect the business accounts for that year.")])

page("media-town-islamabad",
     "Media Town is a cooperative housing society originally formed for journalists and media workers, now home to a broader mix of residents in the twin-city area. Our Media Town clients are journalists, media professionals, freelancers and other residents.",
     "Media Town Islamabad tax help for journalists, media professionals and freelancers: salary and freelance income, society plots and returns filed online.",
     """## Journalists and Media Workers

Salaried journalists have tax deducted by their organisations, while many also earn from freelance writing, television appearances or digital content. Each source is income: honoraria from channels may have tax deducted, and payments from platforms or foreign outlets arrive through banks.

## Content Creators

Media professionals increasingly run YouTube channels or podcasts. Platform earnings, sponsorships and brand deals are business income. Records of each source, and of equipment and editing costs, support the return.

## Society Plots

Members who received plots through the society hold them as assets at the amounts paid. Plots sold to non-members are declared as sales, with advance tax at transfer.

## Residents Beyond the Media

Later residents include government employees and professionals, who file standard returns.

## Getting Started

Share salary certificates, honorarium records, platform statements and society documents. We prepare the return and keep a record of each income stream.""",
     [("Are TV appearance fees taxable for journalists?",
       "Yes, honoraria are income, and channels often deduct tax at payment."),
      ("How do journalists with YouTube channels file?",
       "Platform earnings and sponsorships are business income, declared with supporting statements and expenses."),
      ("Do society plots allotted to members go in the wealth statement?",
       "Yes, at the amounts paid, from the date of allotment.")])

page("pak-town-islamabad",
     "Pak Town is one of the smaller private housing communities on Islamabad's periphery, with houses, plots and local shops serving residents. Our Pak Town clients are homeowners, plot investors and small business owners.",
     "Pak Town Islamabad tax help for homeowners, plot investors and small businesses: property records, local business returns and filer status online.",
     """## Homeowners

Residents who bought or built homes in Pak Town show them in the wealth statement at cost, including construction and later additions. Receipts from the society for each payment establish the cost.

## Plot Investors

Investors holding plots should keep allotment and transfer records. Sale proceeds are declared, and advance tax applies at transfer.

## Local Businesses

Grocery shops, pharmacies and service providers in the community file business returns, keep purchase records and claim electricity bill tax.

## Checking a Society Before Buying

Before buying in any private society, check its approval status with the relevant authority. An unapproved society carries legal risk; the purchase must still be declared, and records of payments protect the buyer.

## Getting Started

Share the society's documents, payment receipts and income records. We prepare the return and wealth statement remotely.""",
     [("Should I check a society's approval before buying a plot?",
       "Yes, because unapproved societies carry legal risk, even though the purchase must still be declared."),
      ("How do I declare additions to my house?",
       "Add their cost to the house's value in the wealth statement in the year they are built."),
      ("Can local shops file without visiting an office?",
       "Yes, returns are filed online from records shared on WhatsApp.")])

page("pwd-islamabad",
     "PWD Housing Society, originally for public works department employees, sits along the Islamabad Expressway near Police Foundation and Korang Town, with houses, a commercial area and a large resident population. Our PWD clients are government employees, retirees and commercial-area businesses.",
     "PWD Housing Society Islamabad tax help for government employees, retirees and commercial businesses: returns, rent, property records and filer status.",
     """## Government Employees and Retirees

Many residents are serving or retired public servants. Salaries are taxed through deduction at source; pensions are exempt; rent and profit are taxable. Retirees who let out part of their houses declare the rent.

## Commercial Area Businesses

PWD's commercial area hosts restaurants, shops, clinics and offices. Restaurants may charge sales tax on services; all businesses file income tax returns and claim credits for tax on electricity bills.

## Houses Let to Families

Houses and portions in PWD are often let to families who work along the Expressway corridor. Rent is taxable, and owners pay tax with their returns if tenants do not deduct it.

## Buying and Selling

Transfers in the society involve its own transfer fees and federal advance tax. Filing before a transaction lowers the advance tax.

## Getting Started

Share salary or pension statements, tenancy agreements and business records. We prepare returns and wealth statements for each earning member.""",
     [("Do retirees in PWD pay tax on rent?",
       "Yes, rent is taxable even though government pension is exempt."),
      ("Do PWD commercial-area restaurants charge sales tax?",
       "Restaurant services are generally taxable; the applicable law depends on the location's jurisdiction."),
      ("Does filing reduce advance tax on a PWD house sale?",
       "Yes, sellers on the Active Taxpayers List pay a lower rate under section 236C.")])

page("rawat-islamabad",
     "Rawat, on GT Road south-east of Islamabad, is known for its historic fort and for the industries, warehouses and housing schemes that have grown along the highway. Our Rawat clients are factory owners, transporters, scheme investors and local traders.",
     "Rawat tax help for factories, warehouses, transporters, housing scheme investors and traders on GT Road: sales tax, withholding and returns online.",
     """## Industries Along GT Road

Factories in the Rawat area produce goods ranging from food to building materials. Manufacturers usually need sales tax registration, deduct tax from staff and suppliers, and file monthly and annual returns. Being on the boundary of Islamabad and Punjab, some businesses need to confirm which jurisdiction applies to their services.

## Warehouses and Logistics

Warehouses serving the twin cities store goods for distributors. Rent from corporate tenants often has tax deducted; storage services can attract services tax.

## Transporters

Goods transporters on GT Road pay advance tax with vehicle tax and may have tax deducted on freight. A trip register supports their returns.

## Housing Scheme Investors

Schemes near Rawat attract investors buying files and plots. Payments are assets; sales are taxable gains.

## Getting Started

Manufacturers should share sales tax returns and payroll; transporters their freight records; investors their scheme documents. We prepare the returns needed for each.""",
     [("Do Rawat businesses follow ICT or Punjab rules for services tax?",
       "It depends on the exact location; businesses on the boundary should confirm their jurisdiction."),
      ("Is warehouse rent from distributors taxed at source?",
       "Corporate tenants usually deduct tax from rent, which the owner claims as a credit."),
      ("How do transporters show freight income?",
       "With a trip register linking freight bills to payments, and credits for tax deducted and paid with vehicle tax.")])

page("soan-garden-islamabad",
     "Soan Garden is a private housing society off the Islamabad Expressway near Koral, with houses, plots and a commercial area serving families who work in the twin cities. Our Soan Garden clients are homeowners, investors and local businesses.",
     "Soan Garden Islamabad tax help for homeowners, investors and local businesses off the Expressway: property records, rent and returns filed online.",
     """## Homeowners Commuting to Work

Families in Soan Garden often work in Islamabad's sectors or Rawalpindi. Salaried members file returns claiming deductions; the family home is in the wealth statement at cost.

## Rented Houses and Portions

Owners letting houses or portions receive rent, usually without deduction, and pay tax with their returns.

## Plot Investors

Investors holding plots keep the society's allotment and transfer records. Sales are declared, with advance tax at transfer.

## Commercial Area

Shops and service businesses in the commercial area file business returns and claim credits.

## Getting Started

Share your society documents, salary certificates, tenancy agreements and bank statements. We prepare returns for each family member and a wealth statement that tracks property costs.""",
     [("Is rent from a Soan Garden portion taxable?",
       "Yes, and if the tenant does not deduct tax, you pay it with your return."),
      ("What documents prove my plot's cost?",
       "The society's allotment letter, transfer documents and payment receipts."),
      ("Can I file for my whole family online?",
       "Yes, we prepare each earning member's return and review them together.")])

page("tarlai-islamabad",
     "Tarlai is a growing semi-urban area in the southern part of the Islamabad Capital Territory, where old village land is being turned into homes, shops and small housing schemes. Our Tarlai clients are landowning families, builders and new residents.",
     "Tarlai Islamabad tax help for landowning families, small builders and new residents: land sales, construction and returns in a growing area, online.",
     """## Landowning Families

Families who have owned land in Tarlai for generations are now selling plots or building shops and houses for rent. Land records establish each family member's share, and each declares their share of sales and rent.

## Small Builders

Local builders who construct houses for sale are running a business. Profit on each house is business income, calculated from sale price less land and construction costs.

## New Residents

Families moving to Tarlai from the city often buy houses built by local builders. The purchase should be supported by the builder's documents and the land record, and advance tax applies at transfer.

## Shops and Services

Shops and workshops serving the growing population keep purchase records and file business returns.

## Getting Started

Share land records, sale or purchase documents and income records. We advise on the treatment and prepare the returns.""",
     [("Is selling plots carved from family land taxable?",
       "Yes, each family member declares their share of the sale; the treatment depends on the land's history and frequency of sales."),
      ("Is building houses to sell a business?",
       "Yes, profit from building and selling houses is business income."),
      ("What should buyers check in Tarlai?",
       "The land record and the builder's documents, and that the transfer is properly registered.")])

page("zero-point-islamabad",
     "Zero Point is the junction where the Islamabad Highway, Kashmir Highway and other main roads meet, surrounded by offices, institutions, hotels and commercial activity. Our Zero Point clients are office-based firms, hospitality businesses and professionals working in the area.",
     "Zero Point Islamabad tax help for offices, hotels and professionals near the main junction: ICT services tax, withholding, rent and returns, filed online.",
     """## Offices and Institutions

Offices around Zero Point include corporate branches, consultancies and institutions. As employers, they deduct salary tax and file withholding statements; as service providers, they may be subject to ICT sales tax on services.

## Hotels and Hospitality

Hotels and guest houses near the junction serve business travellers. Room charges and food services can be taxable under the ICT tax on services, and hotels file income tax returns with records of occupancy and revenue.

## Professionals

Consultants and contractors working with institutions in the area receive fees with tax deducted. A register of invoices and deductions supports their returns.

## Property Owners

Owners of commercial buildings let to offices and hotels receive rent, usually with tax deducted by corporate tenants.

## Getting Started

Firms should share payroll and invoice records; hotels their occupancy and revenue reports; professionals their invoices and certificates. We prepare the filings each needs.""",
     [("Do Islamabad hotels charge sales tax on room charges?",
       "Hotel and accommodation services can be taxable under the ICT tax on services law."),
      ("Must offices file withholding statements?",
       "Yes, employers and prescribed persons deducting tax must file periodic withholding statements."),
      ("Is rent from an office building taxed at source?",
       "Corporate tenants usually deduct tax from rent; the owner claims it as a credit.")])
