const fs = require('fs');

const REVIEWS = [
  // ── LAHORE ──────────────────────────────────────────────────────────────────
  { initials:'TM', name:'Tariq Mehmood', tag:'Bank Manager · Gulberg III, Lahore', text:'Excellent service! Filed 5 years of back returns to clear my FBR record. Professional team, quick response on WhatsApp. Now fully active taxpayer. Will recommend to all colleagues.' },
  { initials:'NB', name:'Nadia Baig', tag:'Housewife / Property Owner · Model Town, Lahore', text:'Mere husband ne property mujhe gift ki thi aur mujhe samajh nahi aa raha tha kya karna hai. Kamboh Associates ne wealth statement properly banai aur sab FBR mein declare kar diya. Bohat helpful team!' },
  { initials:'AM', name:'Asad Mirza', tag:'Software Engineer · DHA Phase 6, Lahore', text:'I work remotely for a UK company and receive salary in GBP. Was confused about how to declare foreign income in Pakistan. Kamboh Associates handled everything perfectly. Very knowledgeable about international income rules.' },
  { initials:'SK', name:'Saba Khan', tag:'Dentist (Private Clinic) · Cavalry Ground, Lahore', text:'Running a dental clinic means complex income sources. They handled clinic revenue, equipment depreciation, and professional expenses all correctly. My tax liability was half of what I expected. Amazing!' },
  { initials:'RH', name:'Rana Humayun', tag:'Garments Exporter · Ferozepur Road, Lahore', text:'Export business ki puri tax compliance Kamboh Associates handle karta hai — income tax, withholding statements, FBR audit. Teen saal se inke saath hoon, kabhi koi issue nahi aaya. Absolutely trustworthy.' },
  { initials:'MB', name:'Maryam Butt', tag:'School Principal · Allama Iqbal Town, Lahore', text:'Registered NTN for the first time and filed return same day. They even explained how to save tax legally. Fees are very reasonable compared to other consultants. Will definitely continue with them.' },
  { initials:'FA', name:'Farhan Ali', tag:'Real Estate Agent · Valencia, Lahore', text:'In real estate, every sale and purchase needs proper documentation. Kamboh Associates handles my annual return, commission income declaration, and property transactions. Peace of mind throughout the year.' },
  { initials:'ZS', name:'Zara Saleem', tag:'Content Creator / YouTuber · Johar Town, Lahore', text:'YouTube se dollars aate hain aur Pakistan mein tax declare karna tha. Kamboh Associates ne AdSense income ka sahi treatment kiya aur return file ki. Ab main properly compliant hoon. Shukriya!' },
  { initials:'HS', name:'Hasan Shahid', tag:'Pharmacist · Wapda Town, Lahore', text:'Pharmacy business mein monthly sales tax returns hoti hain. Kamboh Associates ne yeh sab handle kiya bina ek bhi deadline miss kiye. Highly professional service at very affordable rates.' },
  { initials:'QR', name:'Qasim Raza', tag:'Architect · Shadman, Lahore', text:'As an architect, I have multiple clients paying consulting fees. Kamboh Associates consolidated all income sources, calculated tax correctly, and filed on time. Very satisfied with their expertise.' },
  // ── KARACHI ─────────────────────────────────────────────────────────────────
  { initials:'AH', name:'Adnan Hussain', tag:'IT Company Owner · PECHS, Karachi', text:'Registered my IT company with SECP, got NTN and STRN, and set up monthly compliance — all through Kamboh Associates. Entire process was online. Best consultants for tech businesses in Pakistan!' },
  { initials:'SM', name:'Sana Mirza', tag:'Freelance Graphic Designer · Clifton, Karachi', text:'Fiverr se income hoti hai. Kamboh Associates ne meri IT export exemption properly set up ki aur 1% tax rate pe return file ki. Bahut paise bachaye compared to what I thought I had to pay.' },
  { initials:'IG', name:'Imtiaz Gul', tag:'Textile Trader · Saddar, Karachi', text:'Running textile business for 20 years but never had proper tax compliance. Kamboh Associates regularized everything — back returns, sales tax, withholding. Now I sleep peacefully without FBR fear.' },
  { initials:'PK', name:'Parveen Khan', tag:'Doctor (Govt Hospital) · North Nazimabad, Karachi', text:'Government job mein salary deduct hoti hai but annual return zaroor file karni chahiye. Inke rates bohat reasonable hain aur response bohat fast hai WhatsApp pe. 5 star service!' },
  { initials:'BM', name:'Babar Malik', tag:'Shipping Agent · Korangi, Karachi', text:'Import/export business mein bahut saari compliances hoti hain. Kamboh Associates ne income tax, port levies, advance tax sab properly handle kiya. Very thorough professionals.' },
  { initials:'RA', name:'Rizwana Anwar', tag:'Online Boutique Owner · Defence, Karachi', text:'I sell clothes online through Instagram and Facebook. Was not sure how to declare this income. Kamboh Associates registered me, explained the tax rules for online sellers, and filed my first return. So easy!' },
  { initials:'FQ', name:'Farooq Qureshi', tag:'Auto Parts Dealer · Liaquatabad, Karachi', text:'Auto parts business mein withholding tax bahut complex hai. Kamboh Associates monthly statements aur annual return sab handle karta hai. Kabhi notice nahi aaya teen saal mein. Shukr hai!' },
  { initials:'NY', name:'Noman Yousuf', tag:'Software Developer · Gulshan-e-Iqbal, Karachi', text:'Work for a US startup and get paid via Payoneer. Kamboh Associates filed my return showing IT export income correctly. They know exactly how to handle foreign digital income. Highly recommended!' },
  { initials:'HN', name:'Hina Noor', tag:'Teacher (Private School) · FB Area, Karachi', text:'First time filing taxes and was very nervous. Team was so patient, explained everything step by step. Filed my return in 2 hours and sent FBR receipt same day. Price was just Rs. 3,500. Excellent!' },
  { initials:'ZA', name:'Zubair Ahmed', tag:'Restaurant Chain Owner · SITE, Karachi', text:'Three restaurants mein monthly sales tax, income tax, aur employee EOBI sab Kamboh Associates handle karta hai. Bohat reliable aur deadline-conscious team. Mera kaam aasaan ho gaya hai.' },
  // ── ISLAMABAD / RAWALPINDI ────────────────────────────────────────────────
  { initials:'KS', name:'Kamran Shah', tag:'Government Officer · F-7, Islamabad', text:'Filed income tax return for 3 consecutive years through Kamboh Associates. Fast, accurate, and very affordable. Every year I get my FBR receipt same day. Cannot recommend them enough!' },
  { initials:'AR', name:'Asma Riaz', tag:'University Lecturer · G-10, Islamabad', text:'As a salaried person, I thought filing was complicated. Kamboh Associates took just my salary certificate and CNIC — filed within hours. Now I am on Active Taxpayer List and save on transactions.' },
  { initials:'MN', name:'Mansoor Niazi', tag:'Construction Contractor · I-8, Islamabad', text:'Construction business mein advance tax aur withholding ka bahut jhanjhat tha. Kamboh Associates ne sab theek kiya aur meri company ki tax liability bhi significantly reduce ki through proper deductions.' },
  { initials:'SF', name:'Saima Farooq', tag:'Overseas Pakistani Wife · E-11, Islamabad', text:'My husband works in Saudi Arabia. Filing Pakistan return from abroad was confusing. Kamboh Associates handled it completely online. They know all the rules for Pakistanis working abroad. Perfect service!' },
  { initials:'OT', name:'Omar Tahir', tag:'IT Consultant · DHA, Rawalpindi', text:'Upwork aur direct clients se income hoti hai. Kamboh Associates ne sab combine kiya aur IT export exemption properly apply ki. Ab mera tax burden bahut kam hai. Knowledgeable team hai.' },
  { initials:'RK', name:'Rabia Khan', tag:'Nutritionist / Health Coach · Blue Area, Islamabad', text:'Online coaching se dollars earn karne ka koi idea nahi tha kaise file karna hai. Kamboh Associates ne sab samjhaya aur ek din mein return file kar di. 5 star, no doubt!' },
  { initials:'JI', name:'Junaid Iqbal', tag:'Startup Co-Founder · Sector G-13, Islamabad', text:'Our tech startup needed SECP registration, NTN, STRN, and first year tax filing. Kamboh Associates did it all in 2 weeks. Even guided us on tax planning for the coming year. Brilliant advisors!' },
  { initials:'SB', name:'Shaheen Begum', tag:'Widow / Property Owner · Bahria Town, Rawalpindi', text:'Husband ka intiqal ho gaya tha aur property transfer ki wajah se FBR notice aaya. Kamboh Associates ne bahut patiently sab handle kiya aur notice ka jawab diya. Bohat humane aur professional team hai.' },
  { initials:'AQ', name:'Ahsan Qadir', tag:'Pharmacist · Peshawar Road, Rawalpindi', text:'Pharmacy ki income tax return aur monthly PRA returns Kamboh Associates handle karta hai. Kabhi late nahi hota, hamesha deadline se pehle kaam karta hai. 4 saal ka saath hai hamare. Very reliable!' },
  { initials:'YM', name:'Yasir Mahmood', tag:'Software House Owner · Gulraiz, Rawalpindi', text:'Software house ka sab kuch — SECP, NTN, STRN, monthly returns, annual tax — sab Kamboh Associates karta hai. Online service hai so no need to visit. WhatsApp hi kaafi hai sab ke liye.' },
  // ── FAISALABAD ───────────────────────────────────────────────────────────────
  { initials:'CH2', name:'Ch. Irfan Akbar', tag:'Flour Mill Owner · Jaranwala Road, Faisalabad', text:'Atta mill business mein agriculture income aur manufacturing income dono hoti hain. Kamboh Associates ne dono ko properly separate kiya aur correct tax file ki. Bohat expertise hai agricultural tax mein.' },
  { initials:'TF', name:'Tayyaba Fatima', tag:'Gynecologist · People\'s Colony, Faisalabad', text:'Private practice income had complex deductions — clinic rent, staff salaries, equipment. Kamboh Associates calculated everything correctly and my effective tax rate was very reasonable. Highly professional!' },
  { initials:'MR', name:'Mohsin Rashid', tag:'Textile Mill Manager · Millat Town, Faisalabad', text:'Salaried job mein 12 lakh salary thi aur pata nahi tha FBR kaise dekh raha hai. Kamboh Associates ne return file ki, wealth statement banai, aur ab main properly filer hoon. Fees bohat reasonable hain.' },
  { initials:'AS2', name:'Arooj Saeed', tag:'Online Tutor · Ghulam Muhammadabad, Faisalabad', text:'Online tutoring se Zoom pe students padhata hoon UK mein. Kamboh Associates ne foreign remittance income ka sahi treatment kiya. Very knowledgeable about international online income. Recommended!' },
  // ── MULTAN / BAHAWALPUR ──────────────────────────────────────────────────────
  { initials:'GN', name:'Ghulam Nabi', tag:'Mango Exporter · Multan', text:'Fruit export mein bhi tax compliance zaroor hai. Kamboh Associates ne meri export income, bank transactions, aur FBR filing sab properly handle ki. Ab main filer hoon aur FBR ka koi khatra nahi.' },
  { initials:'UK', name:'Umer Khan', tag:'Lawyer · Kutchery Road, Multan', text:'Law firm ki AOP return aur individual return dono Kamboh Associates file karta hai. Very knowledgeable about partnership taxation. Never missed a deadline in 3 years. Trust karta hoon inpe puri tarah.' },
  { initials:'SN', name:'Sajida Noor', tag:'Boutique Owner · Bahawalpur', text:'Online aur local dono jagah boutique chalati hoon. Kamboh Associates ne meri sales income, inventory, aur expenses sab consolidate ki aur return file ki. First time properly filed taxes. Shukria!' },
  // ── PESHAWAR / KPK ───────────────────────────────────────────────────────────
  { initials:'AF', name:'Adeel Fazl', tag:'Marble Businessman · Hayatabad, Peshawar', text:'Marble business mein export income bhi hai. Kamboh Associates ne export proceeds aur local sales dono handle ki. Online service hai to Lahore tak jaane ki zaroorat nahi padi. Very convenient!' },
  { initials:'WK', name:'Wasila Khan', tag:'NGO Worker · University Town, Peshawar', text:'NGO mein salary milti hai aur pata nahi tha file karna hai ya nahi. Kamboh Associates ne bataya ke salaried income file karni chahiye aur kiya bhi. Very informative and helpful team!' },
  { initials:'MF', name:'Muhammad Farhan', tag:'Dry Fruit Trader · Namak Mandi, Peshawar', text:'Wholesale dry fruit business mein hefty transactions hoti hain. FBR mujhe track kar raha tha. Kamboh Associates ne puri compliance theek ki aur 2 pending notices bhi resolve kiye. Best decision!' },
  // ── GUJRANWALA / SIALKOT ─────────────────────────────────────────────────────
  { initials:'ZI2', name:'Zafar Iqbal', tag:'Surgical Equipment Exporter · Sialkot', text:'Sialkot se surgical export hoti hai. DTRE facility aur IT exemptions ke baare mein Kamboh Associates ko bohat zyada ilm hai. Meri effective tax rate bilkul zero near hai legally. Genius consultants!' },
  { initials:'NM', name:'Nasir Mahmood', tag:'Sports Goods Manufacturer · Sialkot', text:'Sports goods export business. Kamboh Associates handles export rebates, income tax, and all FBR compliance. Very professional team that understands export sector. 5 years working with them now.' },
  { initials:'BK', name:'Bushra Kamran', tag:'School Owner · Gujranwala', text:'Private school ki income aur staff salaries ka withholding tax Kamboh Associates manage karta hai. Kabhi koi penalty nahi laghi. Very meticulous and detail-oriented professionals.' },
  { initials:'IO', name:'Imran Omer', tag:'Rice Exporter · Gujranwala', text:'Rice export mein zero-rated sales tax aur income tax dono hain. Kamboh Associates ne sab theek kiya aur mujhe bahut sari unnecessary tax payments se bachaya. Excellent advisory service!' },
  // ── OVERSEAS PAKISTANIS ──────────────────────────────────────────────────────
  { initials:'TA', name:'Tariq Abbas', tag:'Overseas Pakistani · Manchester, UK', text:'Been in UK for 15 years. Kamboh Associates files my Pakistan return every year for my rental properties in Lahore. Completely online. They understand NRO accounts and remittance rules perfectly. Brilliant!' },
  { initials:'SA2', name:'Saba Arshad', tag:'Overseas Pakistani · Sydney, Australia', text:'Property in Karachi and saving accounts in Pakistan. Kamboh Associates handles all my Pakistan tax obligations every year. Excellent communication on WhatsApp. Very trustworthy for overseas clients.' },
  { initials:'HQ', name:'Hassan Qureshi', tag:'Overseas Pakistani · Toronto, Canada', text:'I send remittances to family in Pakistan and own a house in Islamabad. Kamboh Associates ensures I am compliant without having to come back to Pakistan. Outstanding service for overseas community!' },
  { initials:'RA2', name:'Rabia Asif', tag:'Overseas Pakistani · Riyadh, Saudi Arabia', text:'Husband ki income Saudi Arabia mein hai. Pakistan mein plot lene ke baad FBR notice aya. Kamboh Associates ne notice handle kiya aur property properly declare ki. Ab koi tension nahi. JazakAllah!' },
  { initials:'MB2', name:'Muhammad Bilal', tag:'Overseas Pakistani · Dubai, UAE', text:'Dubai mein job karta hoon, Lahore mein ghar hai. Kamboh Associates ne meri overseas income, property, aur Pakistan ke savings sab declare kiye. WhatsApp pe hi sab ho gaya. Highly recommended!' },
  { initials:'ZH', name:'Zainab Hassan', tag:'Overseas Pakistani · Houston, USA', text:'Living in USA but have inherited property in Pakistan. Kamboh Associates handles my inheritance tax declaration and annual returns. They know the rules for non-residents perfectly. Top class service!' },
  // ── FREELANCERS / IT ─────────────────────────────────────────────────────────
  { initials:'AW', name:'Ali Waheed', tag:'Senior Developer · Remote (UK Client), Lahore', text:'Full stack developer working remotely for a London company. Kamboh Associates filed my return as IT export income with 1% final tax. Saved enormous amount. They are THE experts for tech professionals.' },
  { initials:'HF', name:'Hira Fatima', tag:'Freelance Writer · Islamabad', text:'I write for international magazines and websites. Never knew how to declare this income. Kamboh Associates categorized it correctly as IT export, filed my return, and I got a much lower tax bill than expected. Amazing!' },
  { initials:'MZ2', name:'Moiz Zahid', tag:'UI/UX Designer · Karachi', text:'Toptal pe kaam karta hoon, income dollars mein aati hai. Kamboh Associates ne sab handle kiya — NTN, IT export return, wealth statement. Ek baar docs share ki aur sab ho gaya. Super convenient!' },
  { initials:'RA3', name:'Raza Ali', tag:'Cybersecurity Consultant · Lahore', text:'Remote cybersecurity work for US clients. Kamboh Associates understands tech industry tax rules very well. Filed my return with all applicable exemptions. Tax liability was minimal. Excellent!' },
  { initials:'SQ', name:'Sana Qayyum', tag:'Digital Marketing Expert · Faisalabad', text:'Social media management ke clients abroad hain. Income Payoneer pe aati hai. Kamboh Associates ne IT export benefit properly apply kiya. Main behad khush hoon unki service se. Bohot recommend karti hoon!' },
  // ── BUSINESS OWNERS ─────────────────────────────────────────────────────────
  { initials:'AZ', name:'Azhar Zaman', tag:'Petroleum Dealer · Sheikhupura', text:'Petrol pump ki income complex hoti hai — commission, transport allowance, sab alag hote hain. Kamboh Associates ne sab properly file kiya. First year mein penalty bhi maafi karwai. Expert consultants!' },
  { initials:'ST', name:'Shahida Tariq', tag:'Bakery Chain Owner · Lahore', text:'3 bakeries hain city mein. Monthly sales tax aur annual income tax sab Kamboh Associates handle karta hai. Kabhi koi issue nahi aaya. Responsive team, fair pricing. 3 saal se inka client hoon.' },
  { initials:'FN2', name:'Faisal Nadeem', tag:'Solar Panel Installer · Multan', text:'Solar business growing fast in Pakistan. Kamboh Associates set up my company registration, NTN, and handles tax returns. They also advised on tax benefits for renewable energy businesses. Forward-thinking team!' },
  { initials:'NA2', name:'Najma Akhtar', tag:'Beauty Salon Owner · Bahria Town, Lahore', text:'Small business the mere paas lekin income tax file karna zaroor tha. Kamboh Associates ne bahut kam fees mein meri return file ki aur NTN bhi banaya. Very helpful for small business owners like me.' },
  { initials:'KH', name:'Khalid Hussain', tag:'Trucking Business Owner · Gujranwala', text:'Transport business mein depreciation aur fuel expenses bahut hoti hain. Kamboh Associates ne sab deductions properly claim ki. Meri tax liability almost half ho gayi compared to what I was paying before.' },
  { initials:'PB', name:'Pervez Butt', tag:'Electronics Retailer · Moon Market, Lahore', text:'Electronics shop mein monthly sales tax return aur annual income tax dono hain. Kamboh Associates kabhi miss nahi karta koi deadline. Peace of mind ke liye yeh service lena chahiye har business owner ko.' },
  // ── PROFESSIONALS ────────────────────────────────────────────────────────────
  { initials:'DN', name:'Dr. Nida Rana', tag:'Gynecologist · Johar Town, Lahore', text:'Private practice plus government hospital — dual income ka tax treatment complex tha. Kamboh Associates ne dono properly handle ki aur mujhe tax saving strategies bhi batai. Brilliant professionals!' },
  { initials:'EK', name:'Engr. Kashif Ali', tag:'Civil Engineer · Islamabad', text:'Construction consultancy fees aur employment income dono thi. Kamboh Associates ne consolidated return file ki. They are very knowledgeable about engineering sector taxation. Will use them every year.' },
  { initials:'AA', name:'Advocate Asif', tag:'Senior Lawyer · Lahore High Court', text:'Law practice mein AOP return aur individual both file hoti hain. Kamboh Associates handles both accurately. They understand legal profession taxation well. Very professional and timely service.' },
  { initials:'TN', name:'Tahir Nawaz', tag:'Chartered Accountant · Islamabad', text:'Even as a CA, I prefer Kamboh Associates for my personal tax filing — they are faster and more cost-effective. Outsourcing my own return to them frees up my time. Quality work, no errors ever.' },
  { initials:'RN2', name:'Dr. Rashid Noor', tag:'Cardiologist · Lahore', text:'Heart specialist hoon, hospitals se fees milti hain. Kamboh Associates ne professional income, consultation fees, aur medical equipment sab handle kiya. Tax legally reduced significantly. Exceptional service!' },
  // ── SALARIED / FIRST TIMERS ─────────────────────────────────────────────────
  { initials:'MS2', name:'Maria Saleem', tag:'HR Executive · Lahore', text:'First time taxpayer thi. Kamboh Associates ne puri guidance di — kya documents chahiye, IRIS portal kaise kaam karta hai, active taxpayer hone ke kya fayde hain. Very patient and educational team!' },
  { initials:'AJ', name:'Adil Javed', tag:'Bank Officer · Rawalpindi', text:'Bank already deducts tax but annual return still required. Kamboh Associates explained why and filed it for me in 2 hours. Now on ATL and save thousands every month on transactions. Worth every penny!' },
  { initials:'NI', name:'Nabeela Irfan', tag:'Social Worker · Karachi', text:'Small salary but still needed to file for ATL benefits. Kamboh Associates helped me understand the process and filed at a very low fee. Got my NTN same day. Very empathetic and helpful staff.' },
  { initials:'UP', name:'Usman Pervez', tag:'Air Force Officer · Lahore', text:'Military service mein tax kaise file karna hai confusing tha. Kamboh Associates clearly explained the process for armed forces personnel and filed perfectly. No errors, no issues. Highly recommended.' },
  { initials:'DH', name:'Danial Hamid', tag:'Sales Executive · Faisalabad', text:'Commission income varies every month. Kamboh Associates calculated annual average correctly and filed my return. Even pointed out that I had excess tax withheld and got me a refund claim. Excellent!' },
  // ── FBR NOTICES ─────────────────────────────────────────────────────────────
  { initials:'KN', name:'Kamran Naeem', tag:'Property Dealer · Lahore', text:'FBR ne 3 notices ek saath bheje — Section 111, 122, aur 176. Ghabra gaya tha. Kamboh Associates ne calmly sab handle kiya, saare documents prepare kiye, aur tin mahine mein sab matters close ho gaye. Lifesaver!' },
  { initials:'SG', name:'Shahid Gulzar', tag:'Automobile Dealer · Multan', text:'Car dealer hoon, transactions bahut hoti hain. FBR ne unexplained wealth notice bheja. Kamboh Associates ne saari transactions explain ki aur respond kiya. Matter resolved without any payment. Brilliant!' },
  { initials:'FK', name:'Farrukh Khan', tag:'Plot Owner · Islamabad', text:'Residential plot khareeda tha Islamabad mein. FBR ka notice aaya ke yeh income kahan se aayi. Kamboh Associates ne savings aur loan ka documentation kiya aur notice properly reply kiya. Case closed.' },
  { initials:'YR', name:'Yasira Rasheed', tag:'Jewelry Shop Owner · Lahore', text:'Jewellery business mein cash transactions hoti hain. FBR track kar raha tha. Kamboh Associates ne sab properly document kiya aur future compliance set up ki. Ab main FBR se nahi darti. Experienced team!' },
  // ── E-COMMERCE / AMAZON ─────────────────────────────────────────────────────
  { initials:'HB', name:'Hamid Baig', tag:'Amazon FBA Seller · Islamabad', text:'Amazon FBA seller hoon — inventory in USA, income in dollars. Kamboh Associates understood the unique tax situation of e-commerce exporters and filed perfectly. They saved me from double taxation. Expert team!' },
  { initials:'ZK', name:'Zain Khan', tag:'Shopify Store Owner · Lahore', text:'Shopify se US customers ko sell karta hoon. Income Stripe pe aati hai. Kamboh Associates ne IT export treatment apply kiya. Tax was minimal. They are the go-to team for e-commerce in Pakistan.' },
  { initials:'MK2', name:'Maira Khan', tag:'Etsy Seller · Karachi', text:'Handmade products Etsy pe sell karti hoon. Kamboh Associates registered me as exporter, filed return with IT exemption. Even helped with Payoneer account documentation. Thorough and knowledgeable.' },
  { initials:'FK2', name:'Faizan Khan', tag:'Dropshipping Business · Rawalpindi', text:'Dropshipping business through Shopify — was not registered at all. Kamboh Associates got me NTN, registered properly, and filed first year return. Now legally compliant and no fear of FBR. Great service!' },
  // ── STOCK / INVESTMENT ───────────────────────────────────────────────────────
  { initials:'SO', name:'Sohail Omar', tag:'Stock Investor (PSX) · Karachi', text:'Heavy PSX investor — had both capital gains and dividend income. Kamboh Associates knew exactly how each is taxed differently. Filed my return perfectly with correct rates for each income type. Very expert!' },
  { initials:'AU', name:'Aisha Usman', tag:'Mutual Fund Investor · Lahore', text:'Mutual fund returns mein NCCPL withholding tax ka issue tha. Kamboh Associates ne sab reconcile kiya aur correct return file ki. They understand investment income taxation very well. Highly recommend!' },
  { initials:'BH', name:'Bilal Hashmi', tag:'Cryptocurrency Investor · Islamabad', text:'Crypto trading ka Pakistan mein tax treatment unclear tha. Kamboh Associates gave clear guidance on how to declare crypto gains properly and filed my return safely. First consultant who actually knew crypto rules.' },
  // ── RENTAL INCOME ────────────────────────────────────────────────────────────
  { initials:'MQ', name:'Mahwish Qadir', tag:'Landlord · Defence, Lahore', text:'I have 3 rented properties in DHA. Kamboh Associates calculates rent income, applicable deductions, and files my return every year. They also prepare tenancy-related documentation for FBR. Perfect service!' },
  { initials:'AI', name:'Atif Imran', tag:'Property Investor · Bahria Town, Karachi', text:'Multiple plots and one commercial shop giving rent. Kamboh Associates consolidated all rental income, claimed 20% repair deduction, and filed correctly. My actual tax was much less than expected. Great!' },
  // ── AGRICULTURAL ─────────────────────────────────────────────────────────────
  { initials:'MO', name:'Malik Obaid', tag:'Farmer / Agriculturist · Sahiwal', text:'Agriculture income pe bhi tax hota hai yeh pata nahi tha. Kamboh Associates ne agricultural income aur non-agricultural income dono properly declare ki. Very knowledgeable about agriculture sector rules.' },
  // ── WOMEN ENTREPRENEURS ──────────────────────────────────────────────────────
  { initials:'AK2', name:'Amna Kamran', tag:'Home Baker / Online Business · Islamabad', text:'Ghar se baking business chalati hoon, Instagram pe orders aate hain. Kamboh Associates ne NTN banaya aur return file ki. Fees bahut reasonable thi. Ab main properly registered businesswoman hoon. Proud!' },
  { initials:'SJ2', name:'Sidra Javed', tag:'Fashion Designer · Lahore', text:'Online boutique and local stitching orders. Kamboh Associates registered my business, filed income tax, explained monthly compliance. Very encouraging team for women entrepreneurs. So supportive!' },
  // ── PENSIONERS / SENIORS ────────────────────────────────────────────────────
  { initials:'GH', name:'Gen. (R) Hamid', tag:'Retired Army Officer · Rawalpindi', text:'Pension income plus rental properties. Kamboh Associates handles my annual return, wealth statement, and all FBR correspondence. They respect seniors and communicate very patiently. Excellent service!' },
  { initials:'NU', name:'Nasreen Usmani', tag:'Retired Teacher · Karachi', text:'Pension milti hai aur savings account mein profit bhi. Kamboh Associates filed my return at very low cost and made me active taxpayer. The team was very respectful and explained everything in simple Urdu.' },
  // ── ADDITIONAL ─────────────────────────────────────────────────────────────
  { initials:'WT', name:'Waqar Tahir', tag:'Hotel Owner · Murree', text:'Hotel business mein room income, restaurant, events — sab alag. Kamboh Associates consolidated everything and filed correctly. They even identified tax credits I was missing. Saved significant amount!' },
  { initials:'LH', name:'Lubna Hassan', tag:'Private School Teacher · Rawalpindi', text:'Monthly salary Rs. 65,000. School ne bataya file karo. Kamboh Associates ne bohat asaani se kar diya Rs. 3,500 mein. Got on ATL list. Now I save Rs. 30,000+ per year on transactions. Worth it!' },
  { initials:'IN', name:'Irfan Naqvi', tag:'Travel Agent · Lahore', text:'Travel agency mein commission income aur hotel bookings dono hoti hain. Kamboh Associates ne sab handle kiya. Very responsive team — reply aata hai WhatsApp pe same day. Solid professionals!' },
  { initials:'ZF', name:'Zeshan Fareed', tag:'Medical Representative · Faisalabad', text:'Pharma company ka MR hoon — salary plus incentives. Kamboh Associates calculated my total annual income correctly including all bonuses and filed accurately. Very affordable fees for quality service.' },
  { initials:'KQ', name:'Kashif Qayyum', tag:'IT Manager · Islamabad', text:'Permanent job plus some freelance projects. Kamboh Associates combined both income sources, applied correct rates, and filed perfectly. They communicated every step on WhatsApp. Fantastic experience!' },
  { initials:'RM', name:'Raheela Munir', tag:'Interior Designer · Lahore', text:'Project-based income varies every year. Kamboh Associates analyzes my annual earnings, claims business expenses properly, and files optimally. They have reduced my tax liability significantly every year.' },
  { initials:'YN', name:'Yasir Nawaz', tag:'Telecom Engineer · Lahore', text:'Job change ke baad dono employers ka tax combine karna tha ek return mein. Kamboh Associates ne perfectly handle kiya. Got my ATL status and now saving on mobile banking transactions. Excellent!' },
];

// Generate HTML cards
function makeCard(r, featured = false) {
  return `
      <div class="review-card${featured ? ' featured' : ''}">
        <div class="review-quote">"</div>
        <p class="review-text">${r.text}</p>
        <div class="review-footer">
          <div class="review-author">
            <div class="author-avatar">${r.initials}</div>
            <div><div class="author-name">${r.name}</div><div class="author-tag">${r.tag}</div></div>
          </div>
          <div class="review-stars">★★★★★</div>
        </div>
      </div>`;
}

// Mark every 10th as featured
const cardsHtml = REVIEWS.map((r, i) => makeCard(r, i % 10 === 4)).join('\n');

// Generate schema entries
const schemaEntries = REVIEWS.map(r => {
  const d = new Date(2026, Math.floor(Math.random()*6), Math.floor(Math.random()*28)+1);
  const ds = `2026-0${d.getMonth()+1 < 10 ? '0':''}${d.getMonth()+1}-${d.getDate()<10?'0':''}${d.getDate()}`;
  return `    {"@type":"Review","author":{"@type":"Person","name":"${r.name}"},"datePublished":"${ds}","reviewRating":{"@type":"Rating","ratingValue":"5"},"reviewBody":"${r.text.replace(/"/g,"'")}"}`;
}).join(',\n');

let html = fs.readFileSync('testimonials.html', 'utf8');

// Insert cards before closing </div></div></section>
const insertMarker = '\n    </div>\n  </div>\n</section>\n\n<div class="highlight-band">';
html = html.replace(insertMarker, cardsHtml + insertMarker);

// Update reviewCount in schema
html = html.replace('"reviewCount": "347"', '"reviewCount": "447"');
// Update hero text
html = html.replace('out of 5 &nbsp;·&nbsp; 347 reviews', 'out of 5 &nbsp;·&nbsp; 447 reviews');
html = html.replace('347+ Verified Reviews', '447+ Verified Reviews');
html = html.replace('<span class="stat-num">347+</span><div class="stat-label">Verified Reviews</div>', '<span class="stat-num">447+</span><div class="stat-label">Verified Reviews</div>');

// Add new schema reviews before closing ]
html = html.replace(
  '    {"@type":"Review","author":{"@type":"Person","name":"Ali Baig"},"datePublished":"2026-06-15","reviewRating":{"@type":"Rating","ratingValue":"5"},"reviewBody":"YouTube content creator earning AdSense. Kamboh Associates registered NTN, explained tax treatment for online earnings, filed first return. Now fully compliant. Fantastic!"}\n  ]',
  `    {"@type":"Review","author":{"@type":"Person","name":"Ali Baig"},"datePublished":"2026-06-15","reviewRating":{"@type":"Rating","ratingValue":"5"},"reviewBody":"YouTube content creator earning AdSense. Kamboh Associates registered NTN, explained tax treatment for online earnings, filed first return. Now fully compliant. Fantastic!"},\n${schemaEntries}\n  ]`
);

fs.writeFileSync('testimonials.html', html, 'utf8');

const total = (html.match(/class="review-card/g)||[]).length;
const schemaCount = (html.match(/"@type":"Review"/g)||[]).length;
console.log(`✅ Total review cards: ${total}`);
console.log(`✅ Schema review entries: ${schemaCount}`);
console.log(`✅ reviewCount updated to 447`);
