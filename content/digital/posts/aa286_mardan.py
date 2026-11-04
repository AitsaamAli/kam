import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=286,
    slug="website-design-mardan",
    title="Website Design Mardan: Agri Traders, Shops and Schools",
    h1="Website Design for Mardan Businesses Serving Pashto and Urdu Speaking Customers",
    crumb="Website Design Mardan",
    description="Website design for Mardan businesses: agri traders in the sugarcane and tobacco belt, shops, clinics and schools, with Pashto and Urdu content and remote work.",
    keyword="website design mardan",
    cluster=["web developer mardan", "mardan business online", "pashto language website",
             "agri trader website kpk", "mardan school website"],
    category="Local Guides",
    published="2026-11-04", published_h="4 November 2026",
    updated="2026-11-04", updated_h="4 November 2026",
    answer=("Website design for Mardan businesses should speak to customers in the language they use: Pashto and Urdu for most local shoppers, English for trade and education. "
            "Agri traders need product and contact pages, shops and clinics need WhatsApp and timings, and schools need admissions information. "
            f"We work online from Lahore, with business websites from {P['starter']}."),
    takeaways=[
        "Mardan is one of the largest cities in Khyber Pakhtunkhwa and a major farming area for sugarcane and tobacco.",
        "Agri traders, sugar-related businesses and input dealers need clear product and contact pages.",
        "Most local customers speak Pashto, and many prefer Urdu for reading, so language choice matters.",
        "Takht-i-Bahi, a World Heritage Buddhist site, brings visitors and student groups to the district.",
        "We work with Mardan clients online from Lahore and have no office in Khyber Pakhtunkhwa.",
    ],
    body=f"""
<h2 id="city">What Shapes Website Design in Mardan?</h2>
<p>Mardan, north-east of Peshawar, is one of the largest cities in Khyber Pakhtunkhwa and the centre of a fertile farming district. The plains around it are known for sugarcane, which feeds local sugar mills, and for tobacco, alongside wheat and vegetables. Abdul Wali Khan University and other colleges make it an education centre for the region. A short drive away is Takht-i-Bahi, a Buddhist monastery complex listed as a UNESCO World Heritage Site, which draws visitors and school trips. Mardan's customers are mostly Pashto speakers, many of whom read Urdu comfortably, and that should guide how a local website is written.</p>

<h2 id="sectors">What Do Mardan Businesses Need Online?</h2>
<table>
<tr><th>Business</th><th>What customers look for</th><th>Key pages</th></tr>
<tr><td>Agri traders and commission agents</td><td>Crops traded, contact, location, trust</td><td>About, products, contact with phone and WhatsApp</td></tr>
<tr><td>Seed, fertiliser and pesticide dealers</td><td>Brands, availability, delivery to villages</td><td>Product categories, branches, enquiry button</td></tr>
<tr><td>Shops and showrooms</td><td>Stock, prices, timings, location</td><td>Products, map, WhatsApp ordering</td></tr>
<tr><td>Clinics and labs</td><td>Doctors, timings, tests, fees</td><td>Doctor pages, booking, test notes</td></tr>
<tr><td>Schools and academies</td><td>Admissions, fees, results, transport</td><td>Admissions, fee page, contact</td></tr>
</table>

<h2 id="language">Should a Mardan Website Be in Pashto?</h2>
<p>It depends on who reads it. Pashto is the everyday language for most people in Mardan, but many prefer to read Urdu, and trade and education audiences often expect English. A practical approach for shops and clinics is a site in Urdu or English with key information, such as timings, address and how to order, also in Pashto. Pashto, like Urdu, is written right to left in its own script, and many people also type it in Roman letters on WhatsApp. If you need full Pashto pages, tell us at the start; we will be honest about whether a translator is needed. Our guide on <a href="/digital/blog/urdu-english-bilingual-website">bilingual websites</a> explains the technical setup.</p>

<h2 id="agri">How Can an Agri Business Use a Simple Website?</h2>
<p>Many traders and dealers do business by phone and in person, and do not need a large website. A few clear pages, covering who you are, what you trade or stock, where you are and how to contact you, help new suppliers, buyers and banks check that you are established. A WhatsApp button with a pre-filled message makes enquiries easy. Add photos of your shop, warehouse or yard, and keep phone numbers current. If you stock many products, list them by category so farmers can check before travelling.</p>

<h2 id="visitors">Pages for Visitors to Takht-i-Bahi</h2>
<p>Hotels, restaurants, transport services and guides near Takht-i-Bahi can attract visitors who search before travelling. A page explaining how to reach the site from Mardan or Peshawar, what you offer, prices and contact details answers their questions. Use your own photos and keep the information accurate; visitors notice when details are copied or out of date.</p>

<h2 id="remote">How Do Mardan Clients Work With Us?</h2>
<p>Our only office is in Lahore, several hours away by motorway, and Mardan projects are handled online. You explain your business on a video call or WhatsApp, we send a fixed-price written scope, you review designs as we share them on screen, and payments follow agreed stages. Shop and product photos are taken locally with a shot list we send.</p>

<h2 id="cost">What Does a Mardan Website Cost?</h2>
<p>A trader, dealer or shop that needs a few clear pages usually starts with a business website from {P['starter']}. A school or clinic group with many pages may need the larger package from {P['business']}, and a single-page presence with a WhatsApp button can start from {P['landing']}. Details are on our <a href="/digital/business-websites">business website packages</a> page, and our guide on <a href="/digital/blog/website-design-peshawar">website design in Peshawar</a> covers the wider region.</p>
""",
    faqs=[
        ("Do you have an office in Mardan?",
         "No. Our only office is in Lahore, and Mardan projects are handled online through video calls or WhatsApp, a fixed-price written scope, on-screen design reviews and staged payments. Shop and product photos are taken locally using a shot list we send you."),
        ("Can you build a website in Pashto?",
         "Pashto is written right to left in its own script, and the site layout must support it. Many Mardan businesses use Urdu or English pages with key information in Pashto. Tell us at the start if you need full Pashto pages, and we will confirm honestly whether a translator is needed."),
        ("Does a small agri trader in Mardan need a website?",
         "A few clear pages help new suppliers, buyers and banks confirm you are established: who you are, what you trade or stock, location, photos and contact with a WhatsApp button. It does not need to be large, but it must be accurate and current."),
        ("How can businesses near Takht-i-Bahi attract visitors online?",
         "Create a page explaining how to reach the site from Mardan or Peshawar, what you offer, prices and contact details, with your own photos. Keep a complete Google Business Profile with reviews, and update information whenever prices or timings change."),
        ("Which languages should a Mardan clinic website use?",
         "Most clinic websites in Mardan work well in Urdu or English, with timings, address, doctor availability and booking instructions also in Pashto for patients who prefer it. Keep the language simple, and never publish patient details or photos without clear consent."),
        ("What does Kamboh Associates Digital charge for a Mardan website?",
         f"A trader, dealer or shop site usually starts from {P['starter']}, a larger school or clinic site from {P['business']}, and a single-page presence with a WhatsApp button from {P['landing']}. Our prices are the same in every province, and each project starts with a written quote."),
    ],
    sources=[
        ("Khyber Pakhtunkhwa Culture and Tourism Authority", "https://www.kptourism.com/"),
        ("SMEDA: Small and Medium Enterprises Development Authority", "https://smeda.org/"),
        ("W3C: Structural markup and right-to-left text in HTML", "https://www.w3.org/International/questions/qa-html-dir"),
        ("Pakistan Bureau of Statistics", "https://www.pbs.gov.pk/"),
    ],
    method="Local facts about Mardan's farming economy, education sector and Takht-i-Bahi come from public information and official sites including the Khyber Pakhtunkhwa tourism authority, SMEDA and the Pakistan Bureau of Statistics. Language advice uses W3C guidance. Our own prices come from our published packages. Checked on 4 November 2026.",
    related=["website-design-peshawar", "urdu-english-bilingual-website", "whatsapp-button-website-leads", "google-business-profile-pakistan"],
    service_links=[("/digital/business-websites", "Business website packages"), ("/digital/pricing", "Our published prices")],
    cta="Running a business in Mardan?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20website%20design%20in%20Mardan.%20I%20would%20like%20a%20quote.",
)
