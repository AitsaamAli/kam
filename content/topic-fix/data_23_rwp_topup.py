"""Extra sections for Rawalpindi, Wah and Taxila pages below the word floor."""

PAGES = {}


def more(rel, text):
    PAGES[rel] = {"body_more": text}


def tc(slug, text):
    more(f"blogs/tax-consultant-{slug}.html", text)


more("blogs/ntn-registration-rawalpindi.html", """## Common Registration Problems

The most frequent problems are a mobile number not registered in the applicant's own name, an email address the applicant cannot access later, and a business address that does not match the rent agreement. Fix these before starting, because the same details are used for password resets and for later sales tax or PRA registrations. If your CNIC has expired, renew it first; IRIS checks it against NADRA's records.""")
tc("saddar-rawalpindi", """## Banks and Money Changers

Saddar's banks and exchange companies make it a centre for remittances and foreign currency. Families receiving money from abroad should keep bank advices, and anyone buying foreign currency in large amounts should keep receipts, because these transactions are reported. Foreign currency held at home or in accounts on 30 June is an asset in the wealth statement.

## Shops Changing Hands

When a Saddar shop's tenancy or ownership changes, both sides should document the payment involved, whether rent, pugri or sale price.""")
tc("satellite-town-rawalpindi", """## Tuition and Coaching

Satellite Town has many tuition centres and home tutors preparing students for board and entry exams. Tutors earn business or professional income; centres pay teachers and rent. Keeping a monthly fee record and a list of teacher payments makes the return straightforward and shows the real profit.""")
tc("commercial-market-rawalpindi", """## Upper Floors Converted to Offices and Clinics

Many buildings in Commercial Market have converted upper floors into clinics, academies and offices. Owners receive rent from several tenants; a simple register of each unit, its tenant and the rent received avoids missing any income when filing.""")
tc("murree-road-rawalpindi", """## Liaquat Bagh and Committee Chowk Traders

The busy stretch around Liaquat Bagh and Committee Chowk has wholesale and retail shops dealing in books, stationery, electronics and clothing. Many are long-established family businesses where the shop has passed between generations. Each new owner should register under their own NTN, open a business account and start fresh records, rather than continuing under a parent's name.""")
tc("cantt-rawalpindi", """## Civilian Staff in Military Organisations

Civilians employed by military organisations and cantonment boards have tax deducted under the same rules as other salaried employees. Their salary certificates should show allowances clearly. Many also run small businesses or own property, which must be declared alongside salary.

## Cantonment Board Property Tax

Property in the cantonment is taxed by the cantonment board. Keep paid receipts with the property file.""")
tc("chaklala-rawalpindi", """## Schools and Colleges in the Area

Schools and colleges serving service families employ teachers and staff. As employers they deduct tax where salaries exceed the threshold. Teachers with private tuition income add it to their returns.

## Allotted Units

Service personnel who received units in Chaklala schemes record the instalments paid; when fully paid, the unit's full cost appears in the wealth statement. Transfers to family members should be documented as gifts.""")
tc("westridge-rawalpindi", """## Families Running Businesses from Home

Some Westridge families run catering, tailoring or online shops from home while one member serves in the forces. These businesses are taxable in the name of the person running them. Keeping their income and expenses separate from household accounts makes filing simpler and avoids questions about where money came from.

## Domestic Help and Expenses

Household wages and school fees belong in the personal expenses figure of the wealth statement.""")
tc("dhoke-hassu-rawalpindi", """## Rented Rooms and Shops

Families in Dhoke Hassu often let a room or a ground-floor shop to earn extra income. Even a small monthly rent adds up over the year and should be declared. A written agreement, even a simple one, protects both the owner and the tenant and supports the figure in the return.""")
tc("faizabad-rawalpindi", """## Drivers and Conductors

Drivers and conductors employed by bus companies are salaried; their employers deduct tax if salaries exceed the threshold. Owner-drivers who run their own vans or coaches earn business income, with fuel, maintenance and terminal fees as costs.

## Cash at Terminals

Terminal businesses handle cash all day. Daily deposits into a business account create the best record of income.""")
tc("gulzar-e-quaid-rawalpindi", """## Families with Members Abroad

Many Gulzar-e-Quaid households receive support from relatives working in the Gulf and Europe. Remittances through banks are not the receiver's taxable income, but houses and cars bought with them belong in the wealth statement with the bank advices as proof.

## Moving to Newer Schemes

When a family sells its Gulzar-e-Quaid house and buys in a newer scheme, both transactions should be documented in the same year, so the new purchase is explained by the sale proceeds.

## First-Time Filers

Young earners in the household should start filing early; a simple first return builds a record.""")
tc("gunjmandi-rawalpindi", """## Weighing and Quality Records

Commodity dealers buy by weight and grade. Keeping weighing slips and quality notes with purchase records helps explain price differences and stock losses from moisture or spoilage, which affect profit. These records also help if FBR questions the gross profit rate.""")
tc("pindora-rawalpindi", """## Builders and Contractors

Pindora's growth has brought small builders and contractors. Those building houses for sale earn business income on each project; those working on contract earn from contract payments, sometimes with tax deducted by companies or government bodies. A project or contract register is essential.

## Families Letting Portions

Portions in Pindora's houses are often let to families working in either city. Rent is declared, with tax paid through the return when tenants do not deduct it.

## Shops on IJP Road

Shops along IJP Road serve both residents and passing traffic. Daily cash records and electricity bills support their returns.""")
tc("airport-road-rawalpindi", """## Banquet Halls and Wedding Seasons

Wedding seasons bring sharp peaks in bookings. Halls should record each booking with the date, client, package and payment, including advances received months earlier. Advances are recorded when received and the event income when the event takes place, according to the method used consistently.""")
tc("rwp-airport-rawalpindi", """## Umrah and Tour Operators

Operators organising Umrah and tours collect package payments that cover flights, hotels and transport. Only their margin is income. Package records listing each traveller, the amounts paid to airlines and hotels and the operator's charge make this clear. Advances received before travel should be tracked so income is recognised in the right year.""")
tc("askari-14-rawalpindi", """## Apartments Let to Families

Askari apartments are popular with tenants who want security and maintained buildings. Owners letting them declare the rent; if the tenant is a company, tax may be deducted. Keep the tenancy agreement and the scheme's permission if required for letting.

## Heirs of Allottees

When an allottee dies, heirs complete the transfer with the scheme and each declares their share from that year. Keep the succession documents with the unit's file.""")
tc("bahria-town-rawalpindi", """## Short-Term Rentals

Some Bahria owners let apartments for short stays through online platforms. This income is taxable and should be declared; platform statements show bookings and payouts.

## Construction Deadlines

Bahria may set deadlines for building on plots. Any surcharge paid for delay adds to the plot's cost.

## Maintenance Disputes

Unpaid maintenance charges can delay transfers; settle them before selling.""")
tc("wah-cantt", """## Families Building Outside the Cantonment

Many POF families have built houses in villages and towns around Wah. These houses belong in the wealth statement at cost, including the land and construction. Land records and building receipts should be kept, because the house may later be sold or inherited.

## Small Businesses Run by Retirees

Retirees often open shops or small businesses. Their profit is taxable even though their pension is not.""")
more("blogs/ntn-registration-wah-cantt.html", """## Business Details for Contractors

Contractors should register the business name exactly as it appears on tender documents and bank accounts, with the correct principal activity. Mismatches between the NTN profile and tender documents can delay payments from the factories. If you operate as a partnership, register the firm as an AOP with its own NTN rather than under one partner's personal NTN.

## Keeping the Profile Updated

When your address, phone or email changes, update the IRIS profile so notices and verification codes reach you.""")
more("blogs/income-tax-filing-wah-cantt.html", """## A Simple Example

A POF technician with an annual salary of Rs 1,500,000 has tax deducted every month. He also has Rs 40,000 profit on a savings account, with tax deducted by the bank, and pays tax on his phone and electricity bills. In his return he declares the salary and profit and claims every deduction as a credit. If the credits exceed his final tax, the excess can be refunded.""")
tc("wah-cantt-rawalpindi", """## Families with Members Abroad

Many families in the Wah area receive remittances from the Gulf and Europe, which often fund houses and land. Remittances through banks are not the receiver's taxable income, but the assets bought belong in the wealth statement with bank records.

## Hasan Abdal and GT Road Businesses

Businesses along GT Road towards Hasan Abdal serve travellers and pilgrims; eateries and guest houses should keep daily records.""")
tc("taxila", """## Heritage Site Guides and Museum Shops

Guides and shops near the museum and excavation sites earn from visitors, with peaks during tourist seasons and school trips. Daily records of sales and guide fees support their returns.

## Students and Faculty

The engineering university brings students and faculty. Faculty salaries are taxed at source; consulting or research income is declared separately.""")
