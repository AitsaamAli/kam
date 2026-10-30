import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=67,
    slug="website-design-peshawar",
    title="Website Design Peshawar: Sites for Wholesale and Trade",
    h1="Website Design in Peshawar: Websites for Wholesalers, Marble Firms and Handicraft Traders",
    crumb="Peshawar Trader Websites",
    description="Website design in Peshawar for wholesalers, marble and stone firms and handicraft traders: catalogues, Urdu and Pashto pages, WhatsApp ordering and prices.",
    keyword="website design peshawar",
    cluster=["web development peshawar", "wholesale website", "marble company website", "pashto website",
             "handicraft export website", "peshawar mein website"],
    category="Local Guides",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=(f"Website design in Peshawar should suit how its traders sell: wholesale catalogues with WhatsApp ordering for dealers across "
            f"Khyber Pakhtunkhwa, stone and marble sites with finish and size galleries, and handicraft stores for buyers at home and "
            f"abroad, with Urdu or Pashto pages where customers need them. Websites start from {P['starter']}."),
    takeaways=[
        "Peshawar is one of South Asia's oldest trading cities, with large wholesale markets and long-standing cross-border trade.",
        "Wholesalers need price-on-request catalogues and WhatsApp ordering rather than consumer checkouts.",
        "Marble and stone businesses sell on looks, so galleries of real slabs, finishes and completed projects matter most.",
        "Many customers prefer Urdu or Pashto; both are right-to-left scripts and need proper fonts and layout.",
        "We work with Peshawar businesses remotely from Lahore and welcome visits to our Lahore office.",
    ],
    body=f"""
<h2 id="trading-city">What Should Website Design in Peshawar Focus On?</h2>
<p>Peshawar has been a trading city for centuries, at the eastern end of the routes through the Khyber Pass. Its wholesale markets, including the old city around Qissa Khwani Bazaar and the Karkhano market, supply retailers across Khyber Pakhtunkhwa and beyond. The wider province is known for marble and stone, and Peshawar's traders also deal in carpets, dry fruits and handicrafts.</p>
<p>For most Peshawar businesses, customers are retailers and repeat buyers who order by phone and WhatsApp. A website should make that ordering easier and reach new buyers, not force a style of selling that does not fit.</p>

<h2 id="by-business">Which Website Fits Which Peshawar Business?</h2>
<table>
<tr><th>Business</th><th>Website focus</th><th>Starting price with us</th></tr>
<tr><td>Wholesaler or distributor</td><td>Catalogue, price on request, WhatsApp ordering, new arrivals</td><td class="price">{P['starter']}</td></tr>
<tr><td>Marble and stone firm</td><td>Slab and finish galleries, sizes, project gallery, quotation form</td><td class="price">{P['business']}</td></tr>
<tr><td>Carpet or handicraft trader</td><td>Online store or export catalogue with sizes and origin details</td><td class="price">{P['store']}</td></tr>
<tr><td>Dry fruit seller</td><td>Store with packs and gift boxes, seasonal offers</td><td class="price">{P['store']}</td></tr>
</table>

<h2 id="wholesale">How Should a Wholesale Catalogue Work?</h2>
<p>Wholesale prices change often and depend on quantity and the customer, so many wholesalers prefer not to publish them. A catalogue can still save hours:</p>
<ul>
<li>each product with photos, brand, pack size and minimum order</li>
<li>a "new arrivals" section updated as containers or consignments arrive</li>
<li>a WhatsApp button on each item that opens a chat with the product name and code</li>
<li>an optional login where approved retailers see current prices</li>
</ul>
<p>Our <a href="/digital/blog/b2b-catalogue-website-manufacturers">B2B catalogue website guide</a> explains dealer logins in more detail.</p>

<h2 id="marble">What Does a Marble and Stone Website Need?</h2>
<p>Stone is chosen by eye. Buyers, architects and builders want to see real slabs, not stock images. A marble website should show each stone type with photos of polished and other finishes, available sizes and thicknesses, the source area if you know it, and photos of completed floors, walls and kitchen tops. Note that natural stone varies from slab to slab and invite buyers to request current slab photos on WhatsApp. A quotation form should ask for area in square feet, finish and city. Construction clients may also read our <a href="/digital/blog/construction-company-website">construction company website guide</a>.</p>

<h2 id="languages">Should Your Website Be in Urdu or Pashto?</h2>
<p>If many of your customers read Urdu or Pashto more comfortably than English, add key pages in those languages: products, ordering and contact. Both are written right to left. The W3C advises setting the direction with the <em>dir</em> attribute in the HTML, and a proper web font is needed so letters join and display correctly on older phones. Keep product codes and prices in a consistent format across languages so orders are not misread.</p>

<h2 id="remote">How Do We Work With Peshawar Businesses?</h2>
<p>We have no office in Peshawar; our team is in Lahore. Peshawar traders work with us through WhatsApp and video calls, with a written scope and fixed price agreed before any payment and milestone payments by bank transfer. For catalogue websites, we usually ask for a product list with photos, which your staff can send on WhatsApp in batches. If you travel to Lahore, you are welcome to meet us at our office.</p>

<h2 id="what-we-build">What We Would Build for You</h2>
<p>A wholesale catalogue with WhatsApp ordering starts from {P['starter']} for up to 5 pages. A marble or stone website with galleries and quotation forms usually needs up to 10 pages, from {P['business']}. A carpet, handicraft or dry fruit store starts from {P['store']}. Urdu or Pashto pages can be added in the written scope. See our <a href="/digital/business-websites">business websites</a> service and our <a href="/digital/blog/best-web-development-company-lahore">guide to choosing a developer</a>.</p>
""",
    faqs=[
        ("What kind of website does a Peshawar wholesaler need?",
         "Usually a catalogue rather than a shop: products with photos, pack sizes and minimum orders, a new arrivals section, and a WhatsApp button on each item. Prices can stay on request, or appear behind a login for approved retailers, because wholesale prices change often and depend on quantity."),
        ("How should a marble company show its stone online?",
         "Use real photos of slabs in each finish, list sizes and thicknesses, show completed projects, and explain that natural stone varies between slabs. Invite buyers to request current slab photos on WhatsApp, and use a quotation form that asks for area, finish and delivery city."),
        ("Can a website be made in Pashto?",
         "Yes. Pashto, like Urdu, is written right to left, so pages need the correct direction set in the HTML and a web font that joins letters properly on phones. Most businesses translate key pages, such as products, ordering and contact, rather than the whole website."),
        ("Do you have an office in Peshawar?",
         "No. Our only office is in Lahore. We work with Peshawar businesses through WhatsApp and video calls, with a written scope and fixed price before any payment and milestone payments by bank transfer. Clients travelling to Lahore are welcome at our office."),
        ("How much does a website cost for a Peshawar business?",
         f"A wholesale catalogue with WhatsApp ordering starts from {P['starter']}, a marble or stone website with galleries from {P['business']}, and a handicraft, carpet or dry fruit store from {P['store']}. Urdu or Pashto pages are added in the written scope. Prices are the same in every city."),
        ("Peshawar mein karobar ki website kaisi honi chahiye?",
         "Wholesale ke liye products ki tasveeron wala catalogue aur har item par WhatsApp button kaafi hai. Marble ke karobar ke liye asli slabs aur mukammal projects ki tasveerein zaroori hain. Agar customers Urdu ya Pashto parhte hain to aham pages un zabanon mein bhi banayein."),
    ],
    sources=[
        ("W3C — Structural markup and right-to-left text in HTML", "https://www.w3.org/International/questions/qa-html-dir"),
        ("Google Search Central — Managing multi-regional and multilingual sites", "https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites"),
        ("Google Business Profile Help — Create and manage your Business Profile", "https://support.google.com/business/answer/7039811"),
        ("WhatsApp Help Center — How to use click to chat", "https://faq.whatsapp.com/5913398998672934"),
        ("Nielsen Norman Group — Usability 101", "https://www.nngroup.com/articles/usability-101-introduction-to-usability/"),
    ],
    method=("Peshawar's trading history, Qissa Khwani and Karkhano markets, and the province's marble, carpet and dry fruit trades are "
            "general public knowledge; we quote no statistics. Right-to-left guidance follows W3C, checked 29 October 2026. The business "
            "table reflects how we scope trader websites. Prices are our own packages."),
    related=["best-web-development-company-lahore", "web-development-multan", "website-design-gujranwala-manufacturers",
             "b2b-catalogue-website-manufacturers"],
    service_links=[("/digital/business-websites", "Websites for Peshawar traders"), ("/digital/contact", "Get a quote")],
    cta="Trading from Peshawar?",
    wa="Hi%2C%20I%20read%20your%20Peshawar%20website%20design%20guide%20and%20need%20a%20quote",
)
