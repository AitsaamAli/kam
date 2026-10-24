"""Karachi area pages, part A: city-level pages and central/south areas."""

PAGES = {}


def city(slug, kind, lead, desc, body, faq):
    PAGES[f"blogs/{kind}-{slug}.html"] = {"lead": lead, "desc": desc, "body": body, "faq": faq}


city("karachi", "tax-consultant",
     "Karachi produces a larger share of Pakistan's tax revenue than any other city, and its taxpayers range from port-based importers and industrial exporters to salaried bank staff and Saddar shopkeepers. This page explains how we work with Karachi clients and which federal and Sindh obligations usually apply.",
     "Tax consultant for Karachi: FBR returns, Sindh Revenue Board registration, importer and exporter filing, notices and wealth statements, handled online from Lahore.",
     """## Two Revenue Systems in One City

Every Karachi business answers to FBR for income tax and sales tax on goods, and to the Sindh Revenue Board for sales tax on services. A clearing agent in Keamari, a software house on Shahrah-e-Faisal and a restaurant in DHA can each owe tax to both bodies in the same month. Being up to date with one does not protect you from the other.

## How Karachi's Size Shapes FBR Contact

Large companies, banks and listed groups are handled by FBR's Large Taxpayers Office, while individuals and smaller businesses fall under the Regional Tax Offices. Whichever office you belong to, notices arrive through IRIS and replies are filed there too, so a consultant outside Karachi can handle them without a visit.

| Karachi taxpayer | Typical work we do |
| Importer clearing through the port | Income tax return claiming import-stage tax, sales tax returns |
| Industrial unit in SITE, Korangi or Landhi | Withholding statements, sales tax, annual return |
| Salaried professional | Return, refund of excess deductions, wealth statement |
| Landlord in Clifton or Gulshan | Rental income, property records, section 7E check |
| Service business | SRB registration and monthly returns alongside FBR |

## Working with Us from Karachi

Clients send documents on WhatsApp, approve a draft and receive the FBR acknowledgement. For Sindh registrations we prepare the SRB application and returns in the same way. Fees are listed on our [pricing page](/pricing).""",
     [("Can a Lahore consultant handle my Karachi tax matters?",
       "Yes. Returns, notices and registrations are all handled online through IRIS and the SRB portal, so location does not matter."),
      ("Do Karachi service businesses need SRB registration?",
       "If they provide services taxable under the Sindh sales tax on services law and cross the threshold, yes, in addition to FBR registration.")])

city("karachi", "ntn-registration",
     "Getting an NTN is the first step for anyone starting a business, freelancing or buying property in Karachi. Registration is done on FBR's IRIS portal using your CNIC, and Karachi businesses often need a Sindh Revenue Board registration soon after.",
     "NTN registration for Karachi residents and businesses: IRIS steps, documents, business profile details and when an SRB registration is also needed.",
     """## Who in Karachi Usually Registers

- **New shop owners** in markets such as Tariq Road, Saddar and Jodia Bazaar who need a bank account in the business name.
- **Freelancers and IT workers** receiving foreign payments who want the lower filer rates.
- **Importers** who need an NTN before clearing goods at the port.
- **Property buyers** who want to be on the Active Taxpayers List before registering a purchase.
- **Employees** asked by HR or a bank to show a tax number.

## Steps on IRIS

1. Open the IRIS registration page and enter your CNIC, mobile number and email.
2. Verify the codes sent to your phone and email.
3. Complete the profile: address, source of income and, for a business, its name, address and principal activity.
4. Submit, and download the NTN certificate once it is issued.

## The Business Address Matters

Many Karachi shops sit in buildings with several units and informal addresses. Enter the address exactly as it appears on the rent agreement or electricity bill, because banks, SRB and buyers check that it matches. A mismatch is a common reason for a later sales tax registration to be delayed.

## After the NTN

If your business provides taxable services in Sindh, the next step is SRB registration. If it supplies goods above the thresholds or imports, a federal sales tax registration may also be required. NTN registration is Rs 2,000 on our [pricing page](/pricing).""",
     [("Is my NTN the same as my CNIC?",
       "For individuals, the CNIC number serves as the NTN once you register on IRIS. Companies and AOPs receive a separate NTN."),
      ("Does NTN registration make me a filer?",
       "No. You become an active filer only after filing a return, which then puts you on the Active Taxpayers List.")])

city("bahadurabad-karachi", "tax-consultant",
     "Bahadurabad, near the Tariq Road and Shahrah-e-Faisal belt, mixes apartment blocks with a busy commercial strip of restaurants, clinics and family-run shops. Most of our Bahadurabad clients are shop owners, professionals and owners of flats they rent out.",
     "Bahadurabad Karachi tax help: shop and restaurant returns, SRB for food services, rental income on flats and salaried refunds, filed online with Kamboh Associates.",
     """## Restaurants and Food Outlets

Bahadurabad's food street is one of the area's best-known features. Restaurants in Sindh charge provincial sales tax on services under the Sindh Revenue Board and also file a federal income tax return. Card and digital payments leave a clear record, so the declared turnover in both returns should match the sales recorded through point-of-sale terminals.

## Flats Let Out to Tenants

Many families in Bahadurabad own an extra apartment in the same building or nearby and rent it out. Rent is taxed separately from salary or business income, and the flat must appear in the wealth statement every year. Keep the tenancy agreement and a record of rent received month by month.

## Clinics and Professionals

Doctors, dentists and consultants practising from Bahadurabad clinics receive fees from patients directly and sometimes from hospitals or panel companies that deduct tax. Both kinds of receipts belong in the return, with the deducted tax claimed as a credit.

| Client type | What we file |
| Restaurant owner | Income tax return, SRB monthly returns |
| Flat owner | Rental income, wealth statement |
| Clinic or consultant | Professional income with tax credits |
| Shopkeeper | Business return with profit computation |""",
     [("Does a Bahadurabad restaurant pay tax to SRB or FBR?",
       "Both. Sales tax on restaurant services goes to the Sindh Revenue Board, while income tax on the profit is filed with FBR."),
      ("Do I declare a flat I rent out in the same building?",
       "Yes. The rent is taxable income and the flat is an asset in your wealth statement.")])

city("bath-island-karachi", "tax-consultant",
     "Bath Island is a small, quiet residential pocket between Clifton and the old city, with older bungalows, newer apartment towers and a high share of senior professionals and business families. Tax work here is mostly about property, investments and accurate wealth statements.",
     "Bath Island Karachi tax services: property and investment declarations, rental income, wealth statement accuracy and capital gains on sales, prepared online.",
     """## Older Bungalows and Redevelopment

Several Bath Island plots that once held single bungalows are now apartment buildings. Families who give their land to a builder in exchange for flats face a tax question many miss: the exchange is a disposal of the land, and the flats received are new assets. How the deal is documented decides how capital gains are worked out and how the flats appear in each family member's wealth statement.

## Investment Portfolios

Households in the area often hold listed shares, mutual funds and savings certificates. Dividends and profit come with tax already deducted, and capital gains on listed shares are calculated through the broker and the National Clearing Company. We collect the year-end certificates and include them correctly, so nothing is taxed twice or left out.

## Keeping the Wealth Statement Consistent

When a family's assets are spread across several names, the wealth statements of husband, wife and adult children must agree with each other: gifts out of one statement should appear in another, and jointly owned property should be split in the agreed shares.

## How We Help

We prepare returns for the whole household together, so that gifts, joint assets and investment income line up across every family member's filing.""",
     [("Is giving my plot to a builder for flats a taxable event?",
       "Generally the land is treated as disposed of in exchange for the flats, so capital gains rules apply. The agreement's wording matters, so review it before signing."),
      ("Why must family wealth statements match?",
       "Gifts and joint assets appear in more than one statement, and FBR compares them. Mismatches lead to questions about unexplained assets.")])

city("buffer-zone-karachi", "tax-consultant",
     "Buffer Zone in north Karachi is a dense residential area with markets, schools, tuition centres and small businesses that serve North Karachi and New Karachi. Our clients here are mainly shopkeepers, teachers, tuition centre owners and families with members working abroad.",
     "Buffer Zone Karachi tax help for shopkeepers, tuition centres, teachers and families receiving remittances: returns, wealth statements and filer status online.",
     """## Tuition Centres and Academies

Coaching academies are a common business in Buffer Zone. Fees are often collected in cash each month, and teachers may be paid per class. The academy owner should keep a fee register and a record of payments to teachers, because profit, not fee collection, is what income tax applies to. Teachers paid by an academy declare those payments as their own income.

## Small Retail and Wholesale

General stores, garment shops and mobile phone outlets in the area's markets mostly sell for cash. A simple purchase and sales record, plus a year-end stock count, is usually enough for an accurate return. The advance tax charged on a shop's commercial electricity bill is a credit worth claiming.

## Families with Members Abroad

Remittances from the Gulf support many households here. Money received through banks is not the receiver's taxable income, but houses and plots bought with it need to appear in the wealth statement, together with the remittance record that explains the funding.

| Who | Main filing point |
| Academy owner | Profit after teachers' pay and rent |
| Teacher | Salary or per-class income from academies and schools |
| Shopkeeper | Profit and electricity bill tax credit |
| Remittance family | Wealth statement showing how assets were funded |""",
     [("Does a tuition academy owner pay tax on total fees?",
       "Income tax applies to profit, so teachers' pay, rent and other costs are deducted from fees. Keep a fee register and payment records."),
      ("Are remittances from Saudi Arabia taxable for my family?",
       "Remittances through banks are generally not the receiver's income, but assets bought with them belong in the wealth statement.")])

city("clifton-block-2-karachi", "tax-consultant",
     "Clifton Block 2 is one of Karachi's established residential blocks, with large houses, embassy-adjacent streets and family offices. Clients from Block 2 typically need help with high-value property, household staff, investments and wealth statements that hold up to scrutiny.",
     "Clifton Block 2 Karachi tax consultant: high-value property, household payroll, investment income and defensible wealth statements, prepared online.",
     """## Large Houses and Valuation

Houses in Block 2 sit on large plots, and the FBR valuation for the area is high. That affects three things: advance tax when a house is bought or sold, any section 7E calculation if the owner has more than one property, and the value at which a newly bought house appears in the wealth statement. We use the purchase deed and the valuation table for the relevant year.

## Household Staff and Expenses

Larger households employ drivers, cooks and guards, pay school fees abroad and travel frequently. FBR increasingly compares these visible expenses with declared income. The personal expenses figure in the wealth statement should be built from actual records, such as staff salaries, school invoices and utility bills, rather than a rough estimate.

## Family Offices and Holding Companies

Some Block 2 families hold business interests through private companies. Dividends, directors' remuneration and loans between the family and the company each have different tax consequences. Keeping a clear record of every transfer between personal and company accounts avoids questions under section 111.

## Our Approach

We prepare each family member's return together, reconcile personal and company flows, and review the result before submission.""",
     [("How is a large Clifton house valued in my wealth statement?",
       "At its cost, supported by the purchase deed. FBR's valuation table is used for advance tax and section 7E, not as the wealth statement value of a house you bought."),
      ("Do household expenses really matter to FBR?",
       "Yes. The wealth statement includes personal expenses, and FBR compares them with visible spending such as travel and school fees.")])

city("clifton-block-9-karachi", "tax-consultant",
     "Clifton Block 9 combines apartment buildings, offices and retail close to the main Clifton arteries, with a large population of tenants and young professionals. Most clients here are salaried employees, flat owners and small office-based businesses.",
     "Clifton Block 9 Karachi tax help for salaried tenants, flat owners and small offices: refunds, rental income, SRB registration and returns filed online.",
     """## Salaried Tenants Claiming Refunds

Employees of banks, telecoms and multinationals who rent flats in Block 9 usually have tax deducted monthly. Many are owed refunds, for example where tax was deducted on bonuses at a higher rate or where they made approved pension contributions. Filing a return is the only way to claim these.

## Owners Letting Out Apartments

Apartment owners who let flats in Block 9, often to corporate tenants, may find the company deducts tax from the rent. The deduction is a credit in the owner's return. Owners should also keep maintenance charges and building society receipts, which support the property's records.

## Small Offices

Consultancies, travel agents and design studios operate from Block 9 office floors. If they provide taxable services in Sindh, SRB registration is needed alongside the FBR return. Their corporate clients will usually deduct income tax from invoices and ask for both registration numbers.

| Situation | What to keep |
| Salaried with bonus | Salary certificate showing tax on bonus |
| Flat let to a company | Tenancy agreement, tax deduction certificates |
| Office-based service business | Invoices, SRB returns, client tax certificates |""",
     [("Can I claim a refund if my employer deducted too much tax?",
       "Yes. File your return showing actual income and credits; the excess deducted can be claimed as a refund."),
      ("My corporate tenant deducts tax from rent. Is that final?",
       "Generally it is an advance tax credited against your liability when you file your return.")])

city("clifton-karachi", "tax-consultant",
     "Clifton stretches from the old Clifton bridge to the sea, combining some of Karachi's most valuable homes with offices, malls, hospitals and seafront restaurants. Tax help for Clifton clients covers everything from landlords and doctors to retailers and corporate executives.",
     "Tax consultant for Clifton Karachi: landlords, doctors, retailers and executives, with SRB registration, rental income and wealth statement work done online.",
     """## Clifton's Mix of Taxpayers

| Taxpayer | Common issue |
| Landlord with commercial units | Rent from companies with tax deducted; property records |
| Doctor or specialist | Hospital fees with deductions plus private practice |
| Retail brand outlet | Sales tax on goods, card sales reconciliation |
| Corporate executive | Perquisites such as cars and housing in taxable salary |
| Seafront restaurant | SRB sales tax on services and income tax |

## Executives and Perquisites

Senior employees in Clifton offices often receive company cars, club memberships or housing. These perquisites are valued under specific rules and added to taxable salary. Checking that the salary certificate treats them correctly can change the final tax noticeably.

## Retail Outlets in Malls

Brand outlets in Clifton's malls are usually integrated with FBR's point-of-sale system, which reports sales in real time. The income tax return must match those reported sales. Differences between POS data and declared turnover are a frequent trigger for notices.

## How We Work with Clifton Clients

Most Clifton clients prefer to share documents digitally and approve drafts on their phones. We prepare returns, SRB filings and notice replies remotely and keep a yearly file so the next return is faster.""",
     [("Are company-provided cars taxable for executives?",
       "Yes. Perquisites such as a company car are valued under specific rules and included in taxable salary."),
      ("Why do mall outlets get FBR notices?",
       "Their sales are reported through FBR's point-of-sale system, and differences from the declared turnover in returns trigger questions.")])


def more(slug, kind, text):
    PAGES[f"blogs/{kind}-{slug}.html"]["body"] += "\n\n" + text


more("karachi", "tax-consultant", """## Sindh Levies Outside the FBR Return

Karachi property owners also pay Sindh's urban immovable property tax to the Excise department, many businesses pay Sindh professional tax, and importers meet the Sindh infrastructure cess on goods moving through the port. None of these reduce federal income tax, but they belong in your records and, where they relate to a business, can be business expenses.""")
more("bahadurabad-karachi", "tax-consultant", """## Shop Electricity Bills

Commercial electricity bills in Bahadurabad's shopping strip carry advance income tax, shown separately on the bill. Over a year this adds up, and it is adjustable against the shop owner's income tax only when a return is filed. Keep all twelve bills, or download them from K-Electric's online account, before filing.""")
more("bath-island-karachi", "tax-consultant", """## Retired Residents

Many long-time Bath Island residents are retired professionals living on pensions, rent and investment income. Government pension is exempt, but profit on savings and rent are taxable, and filing keeps withholding on bank profit at the lower rate. A short annual return is usually all that is needed.""")
more("buffer-zone-karachi", "tax-consultant", """## Getting Started

Send a photo of your CNIC and the year's bank statements on WhatsApp, along with any salary certificate or shop records. We prepare the return and wealth statement, explain each figure, and submit after your approval. Most Buffer Zone returns are completed within a day or two.""")
more("clifton-block-2-karachi", "tax-consultant", """## Selling a Large House

When a Block 2 house is sold, the seller pays advance tax under section 236C, 2.75% for persons on the Active Taxpayers List and 5.5% for others for transfers from 1 July 2026, on the higher of the price and the FBR value. Capital gains tax depends on when the house was acquired, so locate the original purchase deed before agreeing a price.""")
more("clifton-block-9-karachi", "tax-consultant", """## New to Karachi?

Professionals who move to Block 9 from other cities often keep property or bank accounts back home. All of these belong in one wealth statement, wherever they are located. Update your address on IRIS after moving so notices reach you, and keep the previous city's tenancy and utility records for the year of the move.""")
more("clifton-karachi", "tax-consultant", """## Specialists Working Across Several Hospitals

Many Clifton doctors consult at two or three hospitals, each deducting tax on fees. Collect a tax certificate from every hospital, add private clinic receipts, and claim all deductions together. Doctors who skip one hospital's certificate often end up paying the same tax twice.""")


def faq(slug, kind, q, a):
    PAGES[f"blogs/{kind}-{slug}.html"]["faq"].append((q, a))


faq("bahadurabad-karachi", "tax-consultant", "Can I file my Bahadurabad shop's return without visiting an office?",
    "Yes. Send your CNIC, bank statements, electricity bills and a summary of sales and purchases on WhatsApp; we prepare the return and you approve it before submission.")
faq("bath-island-karachi", "tax-consultant", "Do I need to file if my only income is pension and bank profit?",
    "Government pension is exempt, but bank profit is taxable and filing keeps you on the Active Taxpayers List, which lowers the tax deducted on that profit and on property transactions.")
faq("buffer-zone-karachi", "tax-consultant", "How long does a return take for a Buffer Zone shopkeeper?",
    "Usually one to two days once we have the CNIC, bank statements and a simple record of the year's sales and purchases.")
faq("clifton-block-9-karachi", "tax-consultant", "I moved to Clifton mid-year. Which address goes in my return?",
    "Use your current address in the IRIS profile, and declare all assets wherever they are. The return covers the whole tax year regardless of the move.")
faq("clifton-karachi", "tax-consultant", "Does a Clifton landlord need to file if the tenant company already deducts tax?",
    "Yes. The deduction is an advance tax credit; you still declare the rent and claim the credit in your return, and the property stays in your wealth statement.")
more("clifton-block-9-karachi", "tax-consultant", "Keep your rent receipts too: tenants who later buy a flat often need to show where their savings came from, and a record of rent paid supports the household expenses figure in the wealth statement.")
more("clifton-karachi", "tax-consultant", "For seafront restaurants and cafes, keep daily sales summaries from the till alongside SRB returns, so both filings tell the same story.")
