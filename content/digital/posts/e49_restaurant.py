import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=49,
    slug="restaurant-website-online-ordering-pakistan",
    title="Restaurant Website With Online Ordering in Pakistan",
    h1="Restaurant Website Online Ordering in Pakistan: Take Orders Without Marketplace Commission",
    crumb="Restaurant Online Ordering",
    description="Restaurant website online ordering in Pakistan: menu, delivery zones, WhatsApp orders, payments and the commission maths behind ordering direct.",
    keyword="restaurant website online ordering pakistan",
    cluster=["restaurant online ordering system", "food delivery website", "restaurant website cost",
             "direct ordering for restaurants", "menu website with whatsapp order", "restaurant ki website"],
    category="Websites by Industry",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=(f"A restaurant website with online ordering in Pakistan lets regular customers order directly through your menu, by WhatsApp "
            f"or checkout, so you keep the margin a delivery marketplace would take as commission. Keep the marketplace for new customers. "
            f"A direct ordering website starts from {P['store']}."),
    takeaways=[
        "Delivery marketplaces bring new customers but charge commission on each order; direct orders keep that margin.",
        "Your website should take repeat orders from customers who already know you.",
        "Delivery zones, minimum order and delivery charges must be set clearly per area.",
        "WhatsApp ordering from the menu suits many Pakistani restaurants better than a full checkout at first.",
        "You need your own riders or a delivery arrangement to take direct delivery orders.",
    ],
    body=f"""
<h2 id="why-direct">Why Add Online Ordering to a Restaurant Website in Pakistan?</h2>
<p>Food delivery marketplaces have changed how Pakistanis order, and they are useful: they bring customers who have never heard of you. They also charge the restaurant a commission on each order, set by your contract with them. For a customer who already orders from you every week, paying that commission again and again is a cost you can reduce.</p>
<p>A restaurant website with online ordering is not a replacement for the apps. It is a second channel for regulars, for customers who find you on Google Maps, and for large or catering orders that you would rather handle directly.</p>

<h2 id="commission-maths">How Much Does Commission Really Cost? A Worked Example</h2>
<p>Illustrative example. We do not quote any marketplace's commission rate, because rates vary by contract and change. Use the rate in your own agreement. The table shows what each 10 percentage points of commission costs on a Rs 2,000 order.</p>
<table>
<tr><th>Commission in your contract</th><th>Cost on a Rs 2,000 order</th><th>Cost on 300 such orders a month</th></tr>
<tr><td>10%</td><td>Rs 200</td><td>Rs 60,000</td></tr>
<tr><td>20%</td><td>Rs 400</td><td>Rs 120,000</td></tr>
<tr><td>30%</td><td>Rs 600</td><td>Rs 180,000</td></tr>
</table>
<p>Direct orders are not free: you pay for riders or a delivery service, gateway charges on online payments and some marketing. Even so, if a third of your regulars order direct, the saving can cover the website quickly. Run the numbers with your own rate and volumes.</p>

<h2 id="features">Which Features Does an Ordering Website Need?</h2>
<table>
<tr><th>Feature</th><th>Why it matters</th></tr>
<tr><td>Menu with photos and prices</td><td>Customers decide in seconds on a phone</td></tr>
<tr><td>Add-ons and options</td><td>Spice level, extra cheese, drink choice, half or full</td></tr>
<tr><td>Delivery zones</td><td>Areas you deliver to, with charge and minimum order per zone</td></tr>
<tr><td>Opening hours and order cut-off</td><td>Stops orders when the kitchen is closed</td></tr>
<tr><td>Payment options</td><td>Cash on delivery, plus wallet, card or Raast if you want</td></tr>
<tr><td>Order alerts</td><td>Sound alert on a kitchen tablet, plus WhatsApp to the manager</td></tr>
<tr><td>Branch selection</td><td>Routes orders to the nearest branch</td></tr>
</table>

<h2 id="whatsapp-or-checkout">WhatsApp Ordering or Full Checkout: Which Should You Start With?</h2>
<p>Many Pakistani restaurants already take orders on WhatsApp. A simple first step is a menu website where the customer builds an order and taps "Send on WhatsApp", which opens a chat with the items, total and address already written. Staff confirm and dispatch as they do now. It costs less and needs no new habits.</p>
<p>A full checkout with order screens, kitchen alerts and online payment suits restaurants with steady volume, several branches or a team that would otherwise retype WhatsApp orders. Many start with WhatsApp ordering and upgrade within a year.</p>

<h2 id="delivery-zones">How Should You Set Delivery Zones?</h2>
<p>List areas by name, because customers know their area better than a radius. For each zone, set the delivery charge, minimum order and expected time. Be honest about times at peak hours; a late order spoils the meal and the review. If you use a third-party rider service, agree how it receives orders and how cash on delivery money comes back to you.</p>

<h2 id="google">How Do Customers Find Your Restaurant Online?</h2>
<p>Your Google Business Profile is often the first thing customers see: photos, hours, menu link and reviews. Link it to the ordering page, keep hours accurate, especially in Ramadan and on public holidays, and reply to reviews. Put your website link and a QR code on takeaway bags and table cards so app customers can order direct next time.</p>

<h2 id="what-we-build">The Ordering Website We Build for Restaurants</h2>
<p>For a single outlet, a menu website with WhatsApp ordering can be built as a business website from {P['business']}. A full ordering site with cart, delivery zones, kitchen alerts, cash on delivery and an online payment option is built from {P['store']}. Multi-branch systems with rider assignment are web applications from {P['app']}. Every project starts with a written scope and a fixed price. See our <a href="/digital/ecommerce-development">online ordering and store development</a> service, our <a href="/digital/blog/clinic-website-design-pakistan">websites by industry hub</a> and our <a href="/digital/blog/payment-gateways-pakistan-compared">payment gateway comparison</a>. Hotels with restaurants may also like our <a href="/digital/blog/hotel-guest-house-booking-website">hotel booking website guide</a>.</p>
""",
    faqs=[
        ("Can a restaurant take online orders without a delivery app?",
         "Yes. A restaurant website can take orders through a cart and checkout or by sending the order to WhatsApp, with cash on delivery or online payment. You need your own riders or a delivery arrangement. Most restaurants keep delivery apps for new customers and use the website for regulars."),
        ("How much does a restaurant ordering website cost?",
         f"A menu website with WhatsApp ordering can be built from {P['business']}. A full ordering site with cart, delivery zones, kitchen alerts and payment options starts from {P['store']}. Multi-branch systems with rider assignment are web applications from {P['app']}. Add hosting, a domain and any gateway charges."),
        ("How much commission do food delivery apps charge?",
         "Commission rates depend on your contract with each platform and change over time, so we do not quote a figure. Check your agreement. Then multiply your rate by your average order value and monthly orders to see what direct ordering could save on customers who already know your restaurant."),
        ("Is WhatsApp ordering good enough for a restaurant?",
         "For many single-outlet restaurants, yes. A menu website that builds the order and sends it to WhatsApp with items, total and address is quick to launch and fits how staff already work. As volume grows, a full checkout with kitchen alerts saves retyping and reduces mistakes."),
        ("How do I get customers to order directly instead of through apps?",
         "Put your website link and QR code on bags, boxes and table cards, link your Google Business Profile to the ordering page, and offer regulars a small reason to order direct, such as a free drink. Make direct ordering as easy as the app, with a clear menu and fast confirmation."),
        ("Restaurant ki website par online order kaise lein?",
         "Apni website par menu tasveeron aur qeematon ke saath lagayen. Customer order bana kar WhatsApp par bhej sake ya checkout se COD ya online payment kare. Delivery areas, charges aur minimum order saaf likhein, aur bags par website ka QR code lagayen taake log seedha aap se order karein."),
    ],
    sources=[
        ("Google Business Profile Help — Create and manage your Business Profile", "https://support.google.com/business/answer/7039811"),
        ("Google Search Central — Local business structured data", "https://developers.google.com/search/docs/appearance/structured-data/local-business"),
        ("WhatsApp Help Center — How to use click to chat", "https://faq.whatsapp.com/5913398998672934"),
        ("State Bank of Pakistan — Press release on Raast P2M, 6 December 2023", "https://www.sbp.org.pk/press/2023/Pr-06-Dec-2023.pdf"),
        ("web.dev — Largest Contentful Paint", "https://web.dev/articles/lcp"),
    ],
    method=("We quote no delivery marketplace commission rate, because rates are set by contract and we could not source a current "
            "public figure; the commission table shows the maths at 10%, 20% and 30% for illustration only. Business Profile and WhatsApp "
            "points follow official help pages, checked 29 October 2026. Prices are our own packages."),
    related=["clinic-website-design-pakistan", "hotel-guest-house-booking-website", "salon-spa-booking-website",
             "payment-gateways-pakistan-compared"],
    service_links=[("/digital/ecommerce-development", "Restaurant online ordering"), ("/digital/business-websites", "Menu websites with WhatsApp")],
    cta="Want orders without paying commission on every one?",
    wa="Hi%2C%20I%20read%20your%20restaurant%20online%20ordering%20guide%20and%20need%20a%20quote",
)
