# Kamboh Associates Digital — 100-Blog Master Plan (Web Development)
**Prepared:** 28 October 2026
**Section:** `/digital/blog/<slug>` only. Nothing in this plan touches the tax site.

The isolation guard applies to every post:
- no tax terms in titles or H1s
- no links to tax pages
- the post is listed only in `sitemap-digital.xml`

---

## Part 1 — What the competitors have (and where they are weak)

Research is from competitors' live sitemaps and pages on 28 Oct 2026. Semrush had no API units, so we looked at what they publish and what Google shows on page 1.

| Competitor | What they built | Weakness we exploit |
|---|---|---|
| **Ezitech** (261 posts) | Price pages for every software type (POS, ERP, clinic, school, hospital, accounting software price in Pakistan), website/ecommerce/app cost guides, ~25 comparisons (WordPress vs custom, Shopify vs WooCommerce vs custom), industry software pages, case studies. About 40% of posts are career/FYP/student content that brings traffic but no buyers. | Generic writing; one table and 4 FAQs on the main cost guide; mixed audience (students vs buyers). We write **only for buyers**, with deeper data. |
| **Webo Creators** (huge sitemap) | Hundreds of `[service]-service-in-[city]` pages for London, Dubai, Chicago and others — the doorway pattern Google penalises. Strong Google Business Profile how-to cluster. | Doorway pages; thin location copy. We never copy that pattern. One strong page per real market. |
| **Progriso** (27 posts) | Website cost Pakistan / USA / 2026, speed guides, "website no traffic" fixes, Shopify vs custom. | Small cluster, single H2 structure, no FAQ on the money page. |
| **SyncDigital** (30 insights) | Smart categories: *Costs & Budgets, Compare & Choose, Before You Hire, Fix a Problem, What's Changing*. UAE focus (website cost Dubai, Shopify vs WooCommerce UAE). | Mostly UAE. Pakistan coverage is one article. We copy the category model for Pakistan and the Gulf. |
| **Digital Sita / FMEOS / Webo** price pages | PKR price tables, 10–12 FAQs, ~1,500 words. | Inconsistent numbers in the same article, no schema, weak authorship, 100% advance payment. |
| **Directories** (Clutch, GoodFirms, DesignRush) | Own "best / top web development company Pakistan / Lahore". | We cannot outrank them; we get **listed and reviewed** on them (off-page task). |

**Seven ways we leave them behind:**
1. **One price list, everywhere.** Every post quotes the same PKR prices as `/digital/pricing`. Competitors contradict themselves.
2. **Depth over volume.** Each post is 1,800–3,000 words of real substance, against their 1,500. That means tables, worked examples, real screenshots and dated data.
3. **Buyer-only topics.** No student or career filler, so every visitor is a potential client.
4. **Pakistan-specific detail they skip:** COD, courier booking (TCS, Leopards, PostEx, Trax), JazzCash/Easypaisa/PayFast/Raast, .pk domains (PKNIC), Urdu/RTL, load-shedding-proof hosting choices, slow mobile networks.
5. **AEO built in:** a 40–60 word answer box, question-style H2s, 8–12 FAQs, and FAQPage schema that matches the visible FAQ.
6. **GEO built in:** one consistent entity description, quotable dated facts, original data (our own price survey and calculator), and the same facts repeated on Clutch, GoodFirms and LinkedIn.
7. **Trust:**
   - an 18-year registered firm with a real Lahore office
   - named authors
   - case studies
   - milestone payments (competitors ask for 100% upfront)

---

## Part 2 — "Outclass" quality standard (non-negotiable for every post)

A post is not published until every box is ticked.

**Content**
- [ ] **One primary keyword plus a 5–15 keyword cluster** (synonyms, Roman Urdu variants, questions). No other post targets the same primary keyword.
- [ ] **Search intent matched**: Informational, Commercial investigation, Transactional, Local or Navigational (column *Intent* below).
- [ ] **Answer box (AEO).** The first 40–60 words answer the main question directly, with a number where possible.
- [ ] **Structure:** question-style H2s, at least one comparison/price table, one worked example or mini case, and a "What we'd do for you" section linking to the service page.
- [ ] **Depth:** 1,800–3,000 words for pillar posts, 1,200–1,800 for spokes. Every section adds a fact, a number, a step or an example. No filler.
- [ ] **Original value:** at least one item a competitor does not have, such as our own price data, a checklist, a template, a real screenshot, or a decision table.
- [ ] **Accuracy:**
  - prices match `/digital/pricing`
  - third-party facts (gateway fees, PKNIC, Shopify plans) are linked to the official source and dated
  - nothing is invented: no fake clients, reviews or statistics

**FAQ, schema and meta**
- [ ] **FAQ:** 8–12 real questions with 40–60 word answers, visible on the page.
- [ ] **Schema:**
  - BlogPosting (author Person, publisher `/digital#organization`, dateModified)
  - FAQPage
  - BreadcrumbList
  - HowTo is not used (deprecated)
- [ ] **Title** ≤ 60 characters with the keyword first. **Meta description** 140–160 characters with the answer and a CTA. Both unique site-wide. One H1.

**Linking**
- [ ] **Internal links (inside /digital only):**
  - 1 up to the cluster pillar
  - 2–4 to sibling posts
  - 1 to the matching service page
  - 1 to pricing or contact
- [ ] **External links:** 1–3 authoritative sources (Google Search Central, PKNIC, SBP, Shopify Help, W3C).

**Media and performance**
- [ ] **Images:** original screenshots or diagrams, WebP, descriptive alt text. Lighthouse 90+ on mobile; no layout shift.

**Conversion**
- [ ] **CTA:** WhatsApp with a pre-filled message per post, plus the call button and quote link.

**Sign-off**
- [ ] **Review:** writer → developer fact-check → SEO QA → `guard.py` passes → publish.

---

## Part 3 — Keyword clusters and the 100 posts

### Legend

**Intent**

| Code | Meaning |
|---|---|
| I | Informational |
| C | Commercial investigation |
| T | Transactional |
| L | Local |

**Audience**

| Code | Meaning |
|---|---|
| PK | Pakistan |
| OS | Overseas (Gulf, UK, US, Canada) |

**Service-page link codes** (where each post sends readers)

| Code | Page |
|---|---|
| BW | business-websites |
| EC | ecommerce-development |
| WA | web-app-development |
| PR | pricing |
| LH | web-development-lahore |
| CT | contact |

**P** = pillar post for its cluster.

### Cluster A — Cost and pricing (money cluster)
Pillar: #1. Competitors here: Ezitech, Webo Creators, Progriso, Digital Sita, GoDaddy.

| # | Title | Primary keyword · cluster terms | Intent | Aud | Link | Beat competitors by |
|---|---|---|---|---|---|---|
| 1 **P** | Website Price in Pakistan 2026: Real Costs by Type, City and Platform | website price in pakistan · website development cost in pakistan, website kitne ki banti hai, website banane ka kharcha | C | PK | PR | Tables by type, platform and city; recurring costs; our published prices; cost calculator embed; 12 FAQs |
| 2 | E-commerce Website Price in Pakistan: Shopify vs WooCommerce vs Custom | ecommerce website price in pakistan · online store price, online store banane ki qeemat | C | PK | EC | 3-way total-cost table incl. gateway and courier fees |
| 3 | Shopify Store Price in Pakistan: Setup, Monthly Plan and Hidden Costs | shopify store price pakistan · shopify setup cost, shopify monthly fee pakistan | C | PK | EC | USD plan converted with a dated rate, app costs, payment workaround |
| 4 | WordPress Website Price in Pakistan: Theme, Custom and Woo Costs | wordpress website price in pakistan · wordpress website cost | C | PK | BW | Theme vs custom table, licences, plugins |
| 5 | Web App Development Cost in Pakistan: Portals, Booking and SaaS | web application development cost pakistan · custom software cost | C | PK/OS | WA | Scope-to-price examples, phased MVP |
| 6 | Website Maintenance Charges in Pakistan: What a Monthly Plan Should Cover | website maintenance charges pakistan · website ki monthly fees | C | PK | PR | Plan comparison, what's excluded |
| 7 | Domain and Hosting Price in Pakistan 2026 (.pk vs .com) | domain hosting price pakistan · .pk domain price, hosting charges pakistan | C | PK | BW | PKNIC process, renewal traps, ownership |
| 8 | Landing Page Design Cost in Pakistan (and When One Page Is Enough) | landing page price pakistan · single page website cost | C | PK | PR | Ad-campaign examples |
| 9 | How Much Does a Website Cost in the UK — and What a Lahore Team Charges | website cost uk · small business website cost uk | C | OS | PR | GBP ranges vs our PKR price, honest trade-offs |
| 10 | Website Cost in Dubai vs Hiring a Pakistani Team | website development cost dubai · web design price uae | C | OS | PR | AED ranges, Arabic/RTL cost |
| 11 | Website Redesign Cost: When to Redesign and When to Fix | website redesign cost · website redesign price pakistan | C | PK/OS | BW | Fix-vs-redesign decision table |
| 12 | Why Website Quotes Vary From Rs 20,000 to Rs 500,000 | why website prices vary · cheap vs expensive website | I/C | PK | PR | Line-by-line quote comparison |

### Cluster B — Choosing and hiring a developer
Pillar: #13. Competitors here: Ezitech ("how to choose a software company"), Clutch, GoodFirms.

| # | Title | Primary keyword · cluster | Intent | Aud | Link | Beat by |
|---|---|---|---|---|---|---|
| 13 **P** | How to Choose a Web Development Company in Pakistan: 20 Questions to Ask | how to choose web development company · best web developer pakistan | C | PK | CT | Downloadable question checklist, red flags |
| 14 | Best Web Development Company in Lahore: What Separates Good From Cheap | best web development company in lahore · web developer lahore | C/L | PK | LH | Evaluation criteria, not a fake ranking |
| 15 | Freelancer vs Agency vs Software House: Who Should Build Your Website? | freelancer vs agency website · website banwane ke liye kis se rabta karein | C | PK/OS | CT | Risk/cost matrix |
| 16 | Website Development Contract Checklist (Pakistan) | website development contract · web design agreement | C | PK | CT | Clause list: ownership, milestones, handover |
| 17 | Who Owns Your Website? Domain, Hosting and Code Ownership Explained | who owns my website · website ownership | I | PK/OS | BW | Lock-in warning signs |
| 18 | Fixed Price vs Hourly Website Projects: Which Protects You? | fixed price vs hourly web development | C | PK/OS | PR | Scenario table |
| 19 | How to Write a Website Brief (Free Template) | website brief template · website requirements document | I/T | PK/OS | CT | Downloadable template |
| 20 | Website Portfolio Red Flags: How to Check a Developer's Past Work | check web developer portfolio | C | PK | CT | Verification steps |
| 21 | Milestone Payments for Websites: How a Fair Payment Plan Works | website advance payment · milestone payment web project | C | PK | PR | Contrast with 100%-upfront competitors |
| 22 | Website Handover Checklist: What You Must Receive at Launch | website handover checklist | I | PK/OS | BW | Credentials, backups, documentation |

### Cluster C — Platforms and technology comparisons
Pillar: #23. Competitors here: Ezitech (24 comparisons), Progriso.

| # | Title | Primary keyword · cluster | Intent | Aud | Link | Beat by |
|---|---|---|---|---|---|---|
| 23 **P** | WordPress vs Shopify vs Custom: Which Should a Pakistani Business Choose? | wordpress vs shopify · best platform for website pakistan | C | PK | BW | Decision tree by business type |
| 24 | Shopify vs WooCommerce for Pakistani Stores | shopify vs woocommerce pakistan | C | PK | EC | Local payments and COD focus |
| 25 | Wix and Squarespace vs a Custom Website in Pakistan | wix vs custom website | C | PK | BW | Payment and SEO limits locally |
| 26 | Next.js vs WordPress for a Business Website | nextjs vs wordpress | C | PK/OS | WA | Speed, cost, editing trade-offs |
| 27 | Laravel vs Node.js for Business Web Apps | laravel vs node | C | PK/OS | WA | Hiring pool in Pakistan |
| 28 | Website or Mobile App First? A Small-Business Decision Guide | website or app for business | C | PK | WA | Cost and reach comparison |
| 29 | Progressive Web App vs Native App for Pakistani Users | pwa vs native app | C | PK | WA | Data cost, low-end Android |
| 30 | Headless CMS vs WordPress: Do You Need It? | headless cms vs wordpress | I/C | OS | WA | When it's overkill |
| 31 | Template vs Custom Design: What You Really Get | template vs custom website | C | PK | BW | Side-by-side examples |
| 32 | Best Hosting for Pakistani Websites: Local vs International Servers | best hosting for pakistan website | C | PK | BW | Speed tests from Pakistan |

### Cluster D — E-commerce in Pakistan
Pillar: #33. Competitors here: Ezitech ("payment gateway integration pakistan", "raast"), Progriso.

| # | Title | Primary keyword · cluster | Intent | Aud | Link | Beat by |
|---|---|---|---|---|---|---|
| 33 **P** | How to Start an Online Store in Pakistan: The Complete 2026 Guide | online store kaise shuru karein · start ecommerce pakistan | I/C | PK | EC | End-to-end steps and costs |
| 34 | Payment Gateways in Pakistan Compared: JazzCash, Easypaisa, PayFast and Banks | payment gateway pakistan · jazzcash payment gateway for website | C | PK | EC | Fees, documents, settlement times (sourced) |
| 35 | Stripe and PayPal in Pakistan: What Actually Works for Your Website | stripe pakistan alternative · paypal pakistan website | I | PK/OS | EC | Legal options explained |
| 36 | Raast and Bank Transfers on Your Website: How to Set Them Up | raast payment integration | I | PK | EC | Step-by-step |
| 37 | Cash on Delivery Websites: How to Cut Fake Orders and Returns | cod website pakistan · fake orders cod | I | PK | EC | Order-verification flow |
| 38 | Courier Integration for Online Stores (TCS, Leopards, PostEx, Trax) | courier api integration pakistan | I | PK | EC | Feature and fee comparison |
| 39 | Daraz vs Your Own Website: Where Should You Sell? | daraz vs own website | C | PK | EC | Margin maths example |
| 40 | Instagram and WhatsApp to Website: Moving Your Shop Online Properly | instagram shop to website · whatsapp order website | C | PK | EC | Migration plan |
| 41 | Product Pages That Sell: A Pakistani Store Checklist | product page best practices | I | PK | EC | Urdu/English copy examples |
| 42 | Clothing Brand Website in Pakistan: Features, Cost and Launch Plan | clothing brand website pakistan | C | PK | EC | Size charts, lawn-season launches |
| 43 | Dropshipping Website in Pakistan: What Works Legally and Practically | dropshipping website pakistan | I/C | PK | EC | Realistic margins |
| 44 | Multi-Vendor Marketplace Website: Cost and Features | multi vendor marketplace development | C | PK/OS | WA | Commission flows |

### Cluster E — Industry websites
Pillar: #45. Competitors here: Ezitech (software for industries); few website-focused pages.

| # | Title | Primary keyword · cluster | Intent | Aud | Link | Beat by |
|---|---|---|---|---|---|---|
| 45 **P** | Website for Doctors and Clinics in Pakistan: Features, Booking and Cost | clinic website design pakistan · doctor website | C | PK | BW | Booking, PMDC details, patient privacy |
| 46 | Dental Clinic Website: Treatments, Before/After Galleries and Booking | dental clinic website | C | PK/OS | BW | Consent and privacy rules |
| 47 | Law Firm Website in Pakistan: Professional, Compliant and Credible | law firm website design pakistan | C | PK | BW | Bar-council-safe wording |
| 48 | School and Academy Website: Admissions, Fees and Parent Portal | school website design pakistan | C | PK | WA | Admissions flow |
| 49 | Restaurant Website With Online Ordering (Without Foodpanda Commission) | restaurant website online ordering pakistan | C | PK | EC | Commission maths |
| 50 | Real Estate Website in Pakistan: Listings, Leads and WhatsApp | real estate website pakistan | C | PK | WA | Lead routing |
| 51 | Exporter Website: Winning Foreign Buyers From Sialkot and Faisalabad | export company website · b2b website for exporters | C | PK | BW | RFQ forms, catalogue SEO |
| 52 | Manufacturer B2B Catalogue Website: Features That Bring Orders | b2b catalogue website | C | PK | BW | Spec sheets, distributor portal |
| 53 | Salon and Spa Website With Booking | salon booking website | C | PK | WA | No-show reduction |
| 54 | Gym Website: Memberships, Classes and Payments | gym website pakistan | C | PK | WA | Membership flows |
| 55 | Pharmacy Website: Product Catalogue and WhatsApp Ordering (DRAP-Aware) | pharmacy website pakistan | C | PK | EC | Prescription-item rules |
| 56 | Travel Agency Website: Packages, Visa Pages and Enquiries | travel agency website pakistan | C | PK | BW | Package builder |
| 57 | Construction Company Website: Projects, Tenders and Trust | construction company website | C | PK | BW | Project portfolio structure |
| 58 | NGO and Trust Website: Donations, Reports and Transparency | ngo website pakistan · donation website | C | PK | WA | Donation gateways |
| 59 | Hotel and Guest House Website: Direct Bookings | hotel website booking engine | C | PK | WA | OTA commission maths |
| 60 | Logistics and Courier Company Website: Tracking and Quotes | logistics company website | C | PK | WA | Tracking integration |

### Cluster F — Local (Pakistan cities)
Rule: each post must state real local facts. **Never a city-name swap.** Pillar: #14 (Lahore).

| # | Title | Primary keyword · cluster | Intent | Aud | Link | Real local angle |
|---|---|---|---|---|---|---|
| 61 | Web Development in Karachi: What Importers and Online Sellers Need | web development company karachi | L/C | PK | CT | Port importers, courier hubs, Tariq Road brands |
| 62 | Web Development in Islamabad and Rawalpindi: Consultants, NGOs and Tenders | web development company islamabad | L/C | PK | CT | Donor reporting, tender portals |
| 63 | Sialkot Exporters: Websites That Win International Buyers | website design sialkot | L/C | PK | BW | Sports and surgical B2B |
| 64 | Faisalabad Textile Businesses: B2B Websites and Catalogues | web development faisalabad | L/C | PK | BW | Mills, yarn and fabric catalogues |
| 65 | Gujranwala Manufacturers: Product Catalogue Websites | website design gujranwala | L/C | PK | BW | Fans, cutlery, sanitary |
| 66 | Multan Businesses Online: Agri, Mango Exports and Retail | web development multan | L/C | PK | BW | Mango exporters, agri dealers |
| 67 | Peshawar Traders: Websites for Wholesale and Cross-Border Trade | website design peshawar | L/C | PK | BW | Wholesale, marble |
| 68 | Lahore Retail Brands: From Liberty and Packages Mall to Online | ecommerce website lahore | L/C | PK | EC | Boutique and fashion launches |
| 69 | Lahore Clinics and Doctors in DHA, Johar Town and Model Town: Getting Booked Online | clinic website lahore | L/C | PK | BW | Map-pack, reviews |
| 70 | Website Designer Near Me (Lahore): How to Pick and What to Expect | website designer near me | L/T | PK | LH | Office visit, GBP, response times |

### Cluster G — Overseas clients
Pillar: #71. Competitors here: cost-estimator sites, Upwork, SyncDigital (UAE).

| # | Title | Primary keyword · cluster | Intent | Aud | Link | Beat by |
|---|---|---|---|---|---|---|
| 71 **P** | Hiring Web Developers From Pakistan: Costs, Risks and How to Do It Safely | hire pakistani web developers · outsource web development pakistan | C | OS | CT | Risk checklist, contracts, time zones |
| 72 | White-Label Web Development: How Agencies Work With a Pakistani Team | white label web development | C/T | OS | CT | NDA, QA, sample workflow |
| 73 | Dedicated Developer vs Fixed Project: Which Model Fits Your Agency? | dedicated developer model | C | OS | WA | Cost scenarios |
| 74 | Time Zones and Communication: Working With a Lahore Team From the UK, US and Gulf | offshore team time zone | I | OS | CT | Overlap-hour table |
| 75 | IP, NDA and Code Ownership When Outsourcing a Website | outsourcing contract ip ownership | C | OS | CT | Clause examples |
| 76 | How Overseas Clients Pay a Pakistani Agency (Wire, Wise, Payoneer) | pay developer in pakistan | I | OS | PR | Steps, invoice format |
| 77 | Arabic (RTL) Website Development for Gulf Businesses | arabic website development | C | OS | BW | RTL checklist |
| 78 | Shopify Experts for UAE and Saudi Stores: Payments and Shipping | shopify developer uae | C | OS | EC | Gulf payments and shipping |
| 79 | UK Small Business Websites: Offshore Quality Without Agency Prices | web design uk small business | C | OS | BW | GDPR/UK GDPR basics |
| 80 | Canadian Small Business Website: Building With an Offshore Team | website for small business canada | C | OS | BW | AODA accessibility basics |
| 81 | Overseas Pakistanis Starting a Business Back Home: Website and Online Setup | start business in pakistan from abroad website | C | OS | CT | Remote setup steps (no tax keywords) |
| 82 | MVP Development for Startups: Scope, Cost and a 6-Week Plan | mvp development company | C/T | OS | WA | Week-by-week plan |

### Cluster H — Getting found: SEO, Google and AI visibility for business websites
Pillar: #83. Competitors here: Webo Creators (GBP cluster), Ezitech ("generative engine optimization").

| # | Title | Primary keyword · cluster | Intent | Aud | Link | Beat by |
|---|---|---|---|---|---|---|
| 83 **P** | How to Get Your Business Website on Google (Pakistan Guide) | google par business kaise laye · website on google | I | PK | BW | Indexing + GBP + reviews in one plan |
| 84 | Google Business Profile for Pakistani Businesses: Setup and Verification | google business profile pakistan | I | PK | LH | Pakistan-specific verification issues |
| 85 | SEO-Ready Website: The 15 Things Built In Before Launch | seo friendly website development | C | PK/OS | BW | Checklist with schema examples |
| 86 | Getting Your Business Mentioned by ChatGPT, Gemini and AI Overviews | ai search visibility for business | I | PK/OS | BW | Our own GEO method |
| 87 | Schema Markup for Business Websites Explained Simply | schema markup for business websites | I | PK/OS | BW | Copy-paste examples |
| 88 | Website Speed for Pakistani Mobile Users: What Actually Matters | website speed optimization | I | PK | BW | Tests on local 4G |
| 89 | Website Gets Visitors but No Enquiries: 12 Fixes | website no enquiries · website traffic no leads | I | PK/OS | CT | Conversion audit list |
| 90 | WhatsApp Leads From Your Website: Buttons, Pre-Filled Messages and Tracking | whatsapp button website | I | PK | BW | GA4 tracking setup |

### Cluster I — Fix a problem and maintenance

| # | Title | Primary keyword · cluster | Intent | Aud | Link | Beat by |
|---|---|---|---|---|---|---|
| 91 | My Website Was Hacked: The First 24 Hours | website hacked what to do | I | PK/OS | PR | Recovery steps |
| 92 | Website Security Checklist for Small Businesses | website security checklist | I | PK/OS | PR | Plugin, backup and access rules |
| 93 | Website Down? How to Find the Cause in 10 Minutes | website down check | I | PK/OS | PR | Diagnostic flow |
| 94 | Moving to a New Website Without Losing Google Traffic | website redesign without losing traffic | I | PK/OS | BW | Redirect map template |
| 95 | Website Slow on Mobile? Causes and Fixes | website slow kyun hai | I | PK | BW | Before/after case |
| 96 | Website Backups: How Often and Where | website backup | I | PK/OS | PR | 3-2-1 rule for SMEs |

### Cluster J — Planning, accessibility and launch

| # | Title | Primary keyword · cluster | Intent | Aud | Link | Beat by |
|---|---|---|---|---|---|---|
| 97 | How Long Does It Take to Build a Website? Realistic Timelines | how long to build a website | I | PK/OS | PR | Timeline by type |
| 98 | What Pages Does a Small Business Website Need? | pages for business website | I | PK/OS | BW | Sitemap templates by industry |
| 99 | Website Accessibility (WCAG) Basics for Business Owners | website accessibility basics | I | OS | BW | 10-point checklist |
| 100 | Website Launch Checklist: 40 Checks Before Going Live | website launch checklist | I/T | PK/OS | CT | Downloadable checklist |

**Intent coverage**

| Intent | Posts |
|---|---|
| Commercial / Transactional | about 70 |
| Informational (feeds the commercial pages) | about 25 |
| Local | 10 |

Every informational post links to a commercial page in the same cluster.

---

## Part 4 — Publishing order (fastest results first)

| Wave | Posts | Why |
|---|---|---|
| 1 (days 1–7) | #1, #2, #3, #4, #6, #7, #13, #23, #24, #34 | Highest buying intent; competitors' pages are beatable; Shopify, price and payment searches have weak results |
| 2 (days 8–14) | #5, #8, #12, #14, #33, #37, #38, #39, #45, #49, #70, #83, #84 | Pillars + local + industries with low competition |
| 3 (days 15–21) | #71–#82 (overseas), #47, #48, #50, #51, #63, #64 | Overseas trust cluster and export cities |
| 4 (days 22–30) | everything remaining | Complete the clusters; internal-link pass |

---

## Part 5 — Off-page and measurement (alongside the blogs)

- **Directory profiles:** Clutch, GoodFirms, DesignRush, Sortlist and SoftwareSuggest, using the same name, address, phone and PKR prices.
- **Reviews:** a request from every finished web client.
- **Search Console:** submit `sitemap-digital.xml` after every wave and request indexing for new posts.
- **Weekly report:**
  - impressions and clicks for `/digital/` (GSC page filter)
  - WhatsApp clicks per post (GA4)
  - a 20-prompt AI-mention check
- **Isolation:** run `python3 content/digital-guard/guard.py` before every commit. The tax site must stay untouched.
