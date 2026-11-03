import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=220,
    slug="mobile-repair-shop-website",
    title="Mobile Repair Website With Prices by Phone Model",
    h1="Mobile Repair Shop Website: Repair Price Tables, Bookings and Warranty Terms",
    crumb="Mobile Repair Website",
    description="How a mobile repair website should list prices by phone model, book repairs, explain warranty and data privacy, and offer pickup for customers who cannot visit.",
    keyword="mobile repair website",
    cluster=["phone repair shop website lahore", "mobile repair booking", "screen replacement price list",
             "phone repair warranty page", "mobile pickup and drop repair"],
    category="Websites by Profession",
    published="2026-11-03", published_h="3 November 2026",
    updated="2026-11-03", updated_h="3 November 2026",
    answer=(f"People with a broken phone ask two questions: how much and how long. "
            f"A mobile repair website should show repair prices by brand and model, let customers book a slot or a pickup, explain the warranty on parts and labour, and say how customer data is protected during repair. "
            f"Our starter package at {P['starter']} covers this."),
    takeaways=[
        "A price table by brand, model and repair type (screen, battery, charging port, back glass) answers most enquiries.",
        "State the repair time for common jobs, such as same day for screens on popular models.",
        "Explain the difference between original, OEM-grade and copy parts, and price each honestly.",
        "Customers worry about their photos and chats; explain your data privacy practice in plain words.",
        "A written warranty on parts and labour, with clear exclusions, sets you apart from roadside repairers.",
    ],
    body=f"""
<h2 id="first-question">Why Is "How Much?" the First Question on a Mobile Repair Website?</h2>
<p>Someone with a cracked screen or a phone that will not charge usually messages several shops asking for prices. The shop that answers first, clearly, usually gets the repair. A mobile repair website can answer that question before the customer even messages, by publishing prices for common repairs on popular models. It saves your staff time on WhatsApp and brings customers who already accept the price.</p>

<h2 id="price-table">How Should the Repair Price Table Work?</h2>
<table>
<tr><th>Brand and model</th><th>Repair</th><th>Part grade</th><th>Typical time</th></tr>
<tr><td>Popular Samsung, Infinix, Tecno, Oppo, Vivo, Xiaomi models</td><td>Screen, battery, charging port</td><td>Original or compatible, priced separately</td><td>Often same day</td></tr>
<tr><td>iPhone models</td><td>Screen, battery, back glass, camera</td><td>Original, OEM-grade or compatible</td><td>Same day to a few days</td></tr>
<tr><td>Older or rare models</td><td>Any</td><td>Depends on availability</td><td>Price and time on request</td></tr>
</table>
<p>Let customers pick their brand and model from a list, then show the repair options and prices. Keep prices dated and update them when part prices change, which happens often with imported parts. If a price depends on diagnosis, show a starting price and the diagnosis fee, and say whether that fee is waived if the customer goes ahead.</p>

<h2 id="parts">Explaining Part Grades Honestly</h2>
<p>Many customers do not know that a replacement screen can be original, OEM-grade or a cheaper copy, and that they differ in brightness, touch response and battery use. Explain each in one sentence, show the price for each and recommend one for their situation. Never install a copy part while charging for an original. This honesty is the main reason customers return and recommend a repair shop.</p>

<h2 id="booking">Bookings, Walk-ins and Pickup</h2>
<p>Booking lets customers reserve a slot and lets you order parts in advance for less common models. Ask for brand, model, the problem and a preferred time. For busy customers, a pickup and drop service within your area can be offered, with the charge and the handover process explained. Confirm bookings on WhatsApp and send updates: received, diagnosed, repaired, ready. Our guide on <a href="/digital/blog/whatsapp-button-website-leads">WhatsApp buttons for website leads</a> explains how to track which pages bring enquiries.</p>

<h2 id="privacy">What Should the Website Say About Customer Data?</h2>
<p>A phone holds photos, chats and banking apps, and customers worry about handing it over. Explain your practice: that customers can remove passwords or log out of sensitive apps before repair where possible, that technicians only test what the repair requires, and that phones are stored securely. Recommend a backup before any repair. A clear privacy statement makes customers far more comfortable choosing your shop over a stall in a market.</p>

<h2 id="warranty">Writing Warranty Terms Customers Understand</h2>
<p>State the warranty period for each type of repair, what it covers (the replaced part and the workmanship) and what it excludes (new physical damage, water damage, opening by another shop). Explain how to claim. Put the same terms on the receipt. Clear terms prevent arguments at the counter and show that the shop stands behind its work.</p>

<h2 id="reviews">Reviews and Local Search for Repair Shops</h2>
<p>When someone searches for phone repair nearby, Google Maps results usually appear above websites. Keep your Google Business Profile complete with opening hours, photos of the shop and workbench, and the services you offer, and make sure the phone number matches the website. After each repair, send a short WhatsApp message thanking the customer and asking for an honest review if they were happy with the work. Reply to every review, including critical ones, politely and factually. Over a few months, a steady flow of genuine reviews mentioning specific repairs does more for a shop than any advertisement.</p>

<h2 id="package">Which Package Suits a Mobile Repair Shop?</h2>
<p>A single shop fits our starter package at {P['starter']}: price tables by model, booking, pickup requests, warranty and privacy pages, with WhatsApp updates. Shops that also sell accessories or used phones online need the store package at {P['store']}. See our <a href="/digital/business-websites">business website packages</a>, and for selling accessories, our guide to <a href="/digital/blog/start-online-store-pakistan">starting an online store in Pakistan</a>.</p>
""",
    faqs=[
        ("Should a mobile repair shop publish repair prices online?",
         "Yes. Customers message several shops asking for prices, and the one that answers clearly first usually gets the repair. Publish prices by brand, model and repair type, separate original and compatible parts, date the table and update it when part prices change."),
        ("How should part grades be explained on a phone repair website?",
         "Explain in one sentence each what original, OEM-grade and compatible parts are and how they differ in brightness, touch response and battery use. Show the price for each and recommend one. Never fit a cheaper part while charging for an original one."),
        ("What should a phone repair warranty cover?",
         "It should cover the replaced part and the workmanship for a stated period, and exclude new physical damage, water damage and phones opened by another shop. Explain how to claim, and print the same terms on the receipt so there is no argument later."),
        ("How can a repair shop reassure customers about their data?",
         "Explain that customers can remove passwords or log out of sensitive apps where possible, that technicians test only what the repair requires, and that phones are stored securely. Recommend a backup before any repair. A plain privacy statement builds trust quickly."),
        ("What does a mobile repair shop website cost?",
         f"A single repair shop fits our starter package at {P['starter']}, with price tables by model, booking, pickup requests, warranty and privacy pages and WhatsApp updates. Shops that also sell accessories or used phones online need the store package at {P['store']}."),
        ("Is pickup and drop worth offering for phone repairs?",
         "It can be, for customers who cannot leave work or home. Offer it within a defined area, state the charge and explain the handover, including noting the phone's condition at pickup. Send WhatsApp updates during the repair so the customer always knows where the phone is."),
        ("Mobile repair ki website par qeematein kaise likhein?",
         "Brand aur model ke hisaab se table banayein jis mein screen, battery, charging port aur back glass ki qeemat ho. Original aur copy parts ki qeemat alag likhein aur waqt bhi batayein. Parts ki qeemat badle to table foran update karein aur tareekh likh dein."),
    ],
    sources=[
        ("Schema.org: MobilePhoneStore", "https://schema.org/MobilePhoneStore"),
        ("Schema.org: Offer", "https://schema.org/Offer"),
        ("Google Business Profile Help: Tips to improve your local ranking", "https://support.google.com/business/answer/7091"),
        ("WhatsApp Business: Business platform", "https://business.whatsapp.com/products/business-platform"),
    ],
    method="We followed what customers ask when they need a phone repaired, the part grades sold in Pakistan and common warranty disputes, and priced the build from our published packages. Sources checked on 3 November 2026.",
    related=["whatsapp-button-website-leads", "start-online-store-pakistan", "show-prices-on-website-or-not", "website-for-hall-road-electronics-traders"],
    service_links=[("/digital/business-websites", "Business website packages"), ("/digital/ecommerce-development", "Online store service")],
    cta="Want customers to see your repair prices before they message?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20mobile%20repair%20websites.%20I%20would%20like%20a%20quote.",
)
