"""Towns D: Dadu to Fort Abbas, plus the tax consultant fees page."""
from towns import town

PAGES = {}

town(PAGES, "dadu",
     tax=("Dadu, on the right bank of the Indus in Sindh, is a district of rice and wheat farms between the river and the Kirthar range, with tehsil towns such as Mehar, Johi and Khairpur Nathan Shah. Floods, farm income and government employment shape most of its tax questions.",
          "Dadu tax consultant for rice growers, mills, shopkeepers, government employees and flood-affected families, with returns prepared online.",
          """## Rice Growers and Mills

Paddy from the canal-irrigated land around Dadu and Mehar goes to husking mills in the district and to traders in Larkana. A grower selling paddy from his own land earns agricultural income, which is outside federal income tax; the provincial agricultural income tax is a separate matter for larger landholders. A mill that buys paddy and sells rice is a business, and its profit after paddy, power, wages and depreciation is taxable.

## After the Floods

The 2022 floods destroyed houses, crops and shops across the district. Business assets lost in a flood are written off in the year of loss, with photographs, survey reports and relief records kept as evidence. Compensation and relief grants received should be noted in the wealth statement so the change in assets is explained.

## Government Employees

Teachers, health staff and clerks working for the Sindh government have salary tax deducted. Filing a return lets them claim excess deductions and keeps them on the Active Taxpayers List.

## Shops in Dadu and Mehar

General stores, cloth shops and pharmacies keep supplier bills from Larkana or Hyderabad wholesalers, daily takings notes and a year-end stock count.

## Services Under SRB

Restaurants, marriage halls and some other services are taxed by the Sindh Revenue Authority, not FBR.

## Gorakh Hill and Tourism

Guest houses and transport operators serving visitors to Gorakh Hill are a small but growing trade, best documented through booking records and bank deposits.""",
          [("Is paddy from my land taxed by FBR?",
            "No, agricultural income is outside federal income tax; Sindh has its own agricultural income tax."),
           ("Can flood losses be claimed?",
            "Losses of business assets can be recognised in the year of loss, with evidence."),
           ("Who taxes marriage halls in Dadu?",
            "The Sindh Revenue Authority.")]),
     ntn=("People in Dadu usually register for an NTN when a rice mill or trader needs to deal with buyers who pay through banks, when a contractor bids for government work, or when a family plans to buy a vehicle or property.",
          "NTN registration in Dadu for rice mills, traders, government contractors, shopkeepers and families buying vehicles or property.",
          """## Rice Mills and Paddy Traders

Buyers of rice in Karachi and exporters require their suppliers to be registered, and banks ask for an NTN before opening a business current account for a mill. Mills that also need sales tax registration must obtain the NTN first.

## Contractors on Rebuilding Work

Since the floods, roads, embankments, schools and houses have been rebuilt through government departments and aid programmes. Contractors and suppliers on this work are asked for an NTN, and those on the Active Taxpayers List suffer lower deductions from their bills.

## Shops Accepting Digital Payments

Shops in Dadu and Mehar that take wallet or card payments need an account in the shop's name, which requires registration.

## Families Buying Tractors and Cars

Advance tax at the registration of a vehicle is lower for active filers, so a family that registers and files before buying saves on the purchase.

## Government Employees

Employees already have tax deducted, but registering on IRIS lets them file their own returns online.

## What You Need

A CNIC, a mobile SIM in your own name, an email address and the address of your shop or mill. Our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows the IRIS screens one by one.""",
          [("Do rice mills in Dadu need sales tax registration?",
            "Many do once they cross the threshold, and the NTN is the first step."),
           ("Are flood rebuilding contractors asked for an NTN?",
            "Yes, departments and programmes generally require it."),
           ("Is registration free?",
            "FBR charges nothing for registration.")]),
     inc=("Dadu returns often combine salary, farm income and a shop or mill. This page explains what each part of the return should show.",
          "Income tax return filing in Dadu for salaried staff, rice mills, traders and farmers, including flood losses and the wealth statement.",
          """## Salaried Persons

Enter salary and the tax deducted as shown on the salary certificate. Allowances that are exempt should be identified separately.

## Agricultural Income

Crop income from your own land is entered as agricultural income. Keep the land record and sale receipts; provincial agricultural tax, where paid, is noted.

## Mills and Traders

Profit is sales less purchases, power, wages, rent and depreciation, with stock counted at 30 June. Tax deducted by buyers and collected on electricity bills is credited.

## Flood Losses

Business stock or equipment destroyed in a flood is written off with evidence. Houses and personal assets lost are reflected in the wealth statement as a reduction, with a note.

## Wealth Statement

Land, houses, vehicles, gold and balances are listed, and the change over the year explained by income, relief received and losses.

## Deadline

Returns are due by 30 September unless FBR extends the date; late filers pay a surcharge to rejoin the Active Taxpayers List.""",
          [("How do I show a house destroyed in the flood?",
            "Remove it from the wealth statement with a note explaining the loss."),
           ("Is relief money income?",
            "Relief grants are generally not income but should be shown as receipts."),
           ("Can I claim tax on my mill's electricity bill?",
            "Advance tax collected on commercial and industrial bills is generally credited.")]))

town(PAGES, "darya-khan",
     tax=("Darya Khan, in Bhakkar district, faces Dera Ismail Khan across the Indus and sits where the Thal desert meets the river's flood plain. Gram, wheat and livestock farming, river trade and transport across the bridge define the local economy.",
          "Darya Khan tax help for gram traders, transporters, farmers, shops and government employees, with income tax returns prepared online.",
          """## Gram from the Thal

Thal farmers grow gram on sandy land in the rain-fed season. Selling your own crop is agricultural income. Traders who buy gram from farmers and send it to processors in Lahore, Faisalabad or Karachi earn business income, and buyers who pay through banks often deduct tax that the trader claims as credit.

## River Land

Farms on the kacha land along the Indus grow wheat and fodder, and families keep cattle and buffaloes. Floods change the river's course and the land available, so land records and crop records should be kept carefully each year.

## Transport Across the Bridge

The bridge to Dera Ismail Khan makes Darya Khan a crossing point for trucks moving between Punjab and southern Khyber Pakhtunkhwa. Truck owners keep freight receipts, fuel and repair bills, and the advance tax paid with their vehicle token, which is adjusted in the return.

## Shops and Services

Shops in the town's bazaar and roadside restaurants on the highway keep supplier bills and a daily sales note. Services such as restaurants fall under PRA.

## Government Employees

Teachers and other staff have tax deducted from salary and file to record land and claim any excess.

## Families Buying Land or Vehicles

Filer status lowers advance tax at property and vehicle registration.""",
          [("Is gram from my own field taxable?",
            "It is agricultural income and outside federal income tax."),
           ("Can truck owners adjust vehicle advance tax?",
            "Yes, it is credited in the annual return."),
           ("Do restaurants on the highway deal with PRA?",
            "Restaurant services in Punjab fall under the Punjab Revenue Authority.")]))

town(PAGES, "daska",
     tax=("Daska, in Sialkot district between Sialkot and Gujranwala, combines rice farming with small engineering and manufacturing units and has many families with members working in Europe and the Gulf. Its tax questions involve factory owners, suppliers to Sialkot's exporters, farmers and overseas Pakistanis.",
          "Daska tax consultant for small manufacturers, suppliers to Sialkot exporters, rice growers, overseas families and shops, prepared online.",
          """## Suppliers to Sialkot's Exporters

Workshops in Daska carry out stitching, finishing, forging and packing for exporters of sports goods, surgical instruments and garments in Sialkot. Exporters increasingly insist that their vendors are registered so that their own records are clean. A workshop's profit is its job charges less labour, power and materials, and any tax deducted by the exporter is credited.

## Small Engineering Units

Units making agricultural implements, pumps and machinery parts sell to dealers across Punjab. Once they cross the threshold, they need sales tax registration as well as an NTN, and their sales tax and income tax figures must agree.

## Basmati Rice

Daska lies in the heart of the basmati belt. Growers' crop sales are agricultural income; husking mills and rice traders earn business income.

## Families with Members in Europe

Many Daska families have relatives in Spain, Italy, Greece and the UK, as well as the Gulf. Money sent home through banks for houses and land is shown in the wealth statement of the person who receives and owns the asset. Overseas relatives buying property in Pakistan benefit from filing, because advance tax is lower for active filers.

## Shops and Services

Shops on the main bazaar and in the grain market keep purchase bills and daily takings.""",
          [("Do Sialkot exporters require registered vendors?",
            "Increasingly, yes, so their own records and deductions are documented."),
           ("Is basmati from my land taxable?",
            "It is agricultural income and outside federal income tax."),
           ("Can relatives in Spain file a Pakistani return?",
            "Yes, online, with their CNIC or NICOP.")]),
     ntn=("Daska businesses and families register for an NTN when a Sialkot exporter asks for it, when a small factory needs sales tax registration, or when a relative abroad plans to buy property at home.",
          "NTN registration in Daska for exporter vendors, engineering units, rice traders, overseas Pakistanis and families buying property.",
          """## Vendors to Exporters

Exporters' vendor forms ask for an NTN and a bank account in the supplier's name. A stitching or finishing unit that registers can be paid by bank transfer and build a steady relationship with the exporter.

## Factories Needing Sales Tax Registration

Engineering and manufacturing units that supply dealers need sales tax registration once their turnover is high enough. The NTN comes first, followed by the sales tax application with details of the premises and electricity connection.

## Overseas Relatives

Daska residents working in Europe or the Gulf can register with their CNIC or NICOP and file from abroad. Being on the Active Taxpayers List reduces advance tax when they buy a house or plot in Daska, Sialkot or Lahore.

## Rice Traders and Mills

Rice traders who sell to exporters and big mills deal with buyers who require registration.

## Young Freelancers

Graduates working online for foreign clients register so that foreign payments arrive in their own accounts.

## Starting

The application is made on IRIS with a CNIC, phone number and address. Each screen is described in our [FBR registration guide](/blogs/fbr-registration-step-by-step).""",
          [("Can I register from Italy for property in Daska?",
            "Yes, register online with your CNIC or NICOP and file each year."),
           ("Do small engineering units need sales tax registration?",
            "Usually once turnover crosses the threshold."),
           ("Does an exporter vendor need an NTN?",
            "Most exporters now ask for one.")]))

town(PAGES, "daska-city-centre",
     tax=("Daska's city centre, around the main bazaar, the grain market and the roads to Sialkot and Gujranwala, is where the town's traders, doctors, schools and money transfer agents work. This page covers the businesses at the heart of the town.",
          "Tax help for Daska city centre: bazaar traders, grain market arhtis, clinics, schools, jewellers and remittance agents, prepared online.",
          """## Jewellers

Daska's jewellers sell gold to families preparing for weddings, often bought with money sent from abroad. Gold sales, purchases and making charges should be recorded, with stock weighed at 30 June. Customers' old gold taken in exchange is also recorded.

## Grain Market Arhtis

Commission agents dealing in rice and wheat earn commission; advances given to farmers are assets at year end.

## Clinics and Pharmacies

Doctors' fees, laboratory income and pharmacy sales are taxable, with distributor invoices and fee registers forming the records.

## Private Schools and Academies

Schools and coaching centres keep fee registers and teachers' salary sheets.

## Money Transfer and Mobile Shops

Agents of banks and mobile wallets earn commission on remittances and payments. The commission, not the amounts transferred, is their income, and banks deduct tax on it.

## Rent from Shops

Families renting out shops in the bazaar declare rent as property income.""",
          [("Is a remittance agent taxed on money transferred?",
            "No, only on commission earned."),
           ("How do jewellers record exchanges of old gold?",
            "By weight and value, as both a purchase and a sale."),
           ("Is shop rent taxable?",
            "Yes, it is property income.")]))

town(PAGES, "depalpur",
     ntn=("Depalpur, in Okara district near the Indian border, is a farming tehsil known for potatoes, maize and rice. Its growers, cold storage owners and traders register for an NTN to deal with buyers and banks.",
          "NTN registration in Depalpur for potato cold storages, maize traders, rice mills, shops and families buying property or vehicles.",
          """## Cold Storages

Potato growers store their crop in cold storages until prices rise. Storage owners charge rent per bag, which is business income. Banks financing these storages require an NTN, and food companies buying potatoes deal only with registered sellers.

## Maize and Feed Mills

Maize from Depalpur goes to feed mills and starch factories, which pay through banks and deduct tax. Traders and growers who sell large lots directly to factories benefit from registration and filing.

## Rice Husking Mills

Mills need an NTN before applying for sales tax registration.

## Shops in Depalpur and Haveli Lakha

Shops that accept wallet and card payments need a business account.

## Families Buying Land or Tractors

Filer status lowers advance tax on property and vehicles.

## Overseas Workers

Workers in the Gulf can register with their CNIC or NICOP.

## How to Register

Registration is done on IRIS with a CNIC, mobile SIM and address. Our [FBR registration guide](/blogs/fbr-registration-step-by-step) shows how.""",
          [("Is cold storage rent business income?",
            "Yes, it is income from a business, not agricultural income."),
           ("Do feed mills require registered suppliers?",
            "Many do, and they deduct tax on payments."),
           ("Do I need an NTN to buy a tractor?",
            "Not to buy, but filer status lowers the advance tax at registration.")]),
     inc=("Depalpur returns combine potato and maize farming, cold storage or mill income and salaries. This page explains what goes where.",
          "Income tax return filing in Depalpur: crop income, cold storage rent, mill profit, salaries and the wealth statement, filed online.",
          """## Crop Income

Potatoes, maize and rice from your own land are agricultural income. Keep the land record and sale receipts.

## Cold Storage Owners

Storage rent received, less electricity, staff, repairs and depreciation, gives the profit. Electricity is often the biggest cost, and the advance tax on industrial bills is credited.

## Potato Traders

Traders who buy potatoes and store them for later sale earn business income on the difference, after storage and transport costs.

## Rice Mills

Profit is rice and by-product sales less paddy, power, wages and depreciation.

## Salaried Persons

Teachers and government staff enter salary and tax deducted.

## Wealth Statement

Land, cold storage buildings, machinery, vehicles and balances are listed.""",
          [("Is potato trading agricultural income?",
            "No, buying and reselling potatoes is business income."),
           ("Can I claim tax on the cold storage's electricity bill?",
            "Advance tax on industrial bills is generally credited."),
           ("Is storage rent taxable?",
            "Yes, it is business income.")]))
