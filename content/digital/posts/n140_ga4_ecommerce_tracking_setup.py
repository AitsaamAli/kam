import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=140,
    slug='ga4-ecommerce-tracking-setup',
    title='GA4 Ecommerce Tracking: What a Store Should Measure',
    h1='GA4 Ecommerce Tracking: What a Pakistani Online Store Should Measure, Including COD Orders',
    crumb='GA4 Ecommerce Tracking',
    description='GA4 ecommerce tracking for online stores: the recommended events, purchase and refund data, separating COD from prepaid orders, and the few numbers worth watching.',
    keyword='ga4 ecommerce tracking',
    cluster=['google analytics ecommerce setup', 'track cod orders analytics', 'ecommerce kpis'],
    category='E-commerce in Pakistan',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="GA4 ecommerce tracking records events such as view_item, add_to_cart, begin_checkout and purchase, so you can see where shoppers drop off. Google notes these events are not sent automatically; your platform or developer adds them. For cash on delivery stores, also record refused parcels with the refund event, so revenue figures stay honest.",
    takeaways=["Ecommerce events must be added to your store; GA4 does not collect them automatically.", "The core funnel is view_item, add_to_cart, begin_checkout, add_payment_info and purchase.", "Record payment method so you can compare cash on delivery with prepaid orders.", "Use the refund event for refused or returned COD orders, otherwise revenue looks better than it is.", "Watch a handful of numbers weekly rather than every report GA4 offers."],
    body=f"""
<h2 id="basics">What Is GA4 Ecommerce Tracking?</h2>
<p>Google Analytics 4 can show how shoppers move through your store, from viewing a product to paying, and where they give up. GA4 ecommerce tracking works by sending named events with product and order details. Google's Analytics Help states that ecommerce events are not sent automatically: they must be added to your website, app or Tag Manager set-up, although some platforms, including Shopify through its pixel, send some of them for you. Reports can take up to 24 hours to fill, and DebugView shows events in real time while testing.</p>
<p>Tracking matters most once the basics in our store start-up guide are in place.</p>

<h2 id="events">Which Events Should a Store Track?</h2>
<p>Google's developer documentation lists recommended ecommerce events. The ones most stores need:</p>
<table>
<tr><th>Event</th><th>When it fires</th><th>What it tells you</th></tr>
<tr><td>view_item_list</td><td>A category or search results page is shown</td><td>Which lists get attention</td></tr>
<tr><td>view_item</td><td>A product page is viewed</td><td>Product interest</td></tr>
<tr><td>add_to_cart</td><td>A product is added to the cart</td><td>Which products convert interest to intent</td></tr>
<tr><td>begin_checkout</td><td>Checkout starts</td><td>Cart-to-checkout drop-off</td></tr>
<tr><td>add_shipping_info</td><td>Delivery details entered</td><td>Whether delivery costs stop people</td></tr>
<tr><td>add_payment_info</td><td>Payment method chosen</td><td>COD vs prepaid choice</td></tr>
<tr><td>purchase</td><td>Order placed</td><td>Orders and revenue</td></tr>
<tr><td>refund</td><td>Order refunded fully or partly</td><td>Lost revenue from refusals and refunds</td></tr>
</table>
<p>Each event carries an items array with product details. Google's example purchase event includes a transaction ID, value and currency, and it recommends setting currency whenever you send a value. Use PKR consistently.</p>

<h2 id="cod">How Should Cash on Delivery Orders Be Tracked?</h2>
<p>In a COD store, a purchase event fires when the order is placed, but some parcels are refused at the door. If you do nothing, GA4 counts that revenue forever. Two practical steps help:</p>
<ol>
<li><strong>Record the payment method</strong> (COD, card, wallet, bank transfer) as a parameter on add_payment_info and purchase, so reports can separate them.</li>
<li><strong>Send a refund event</strong> when a COD order is refused, cancelled or returned, with the same transaction ID and the items involved. Google's help page says each refunded item should be included in the items array, for full or partial refunds.</li>
</ol>
<p>Sending refunds usually needs a small server-side integration or a manual import, because the refusal happens days later at the courier. Our COD guide covers reducing refusals in the first place.</p>

<h2 id="kpis">Which Numbers Are Worth Watching?</h2>
<table>
<tr><th>Number</th><th>How to read it</th></tr>
<tr><td>Sessions to purchase rate</td><td>Overall store performance; compare month to month</td></tr>
<tr><td>Add-to-cart rate by product</td><td>Low rates suggest price, photos or description problems</td></tr>
<tr><td>Checkout completion rate</td><td>Low rates point to delivery costs or form problems</td></tr>
<tr><td>Revenue after refunds</td><td>The honest revenue figure</td></tr>
<tr><td>COD refusal rate</td><td>Share of COD orders later refunded</td></tr>
<tr><td>Revenue by traffic source</td><td>Which channels bring buyers, not just visitors</td></tr>
</table>
<p>Our <a href="/digital/blog/abandoned-cart-recovery-whatsapp">abandoned cart guide</a> explains what to do about checkout drop-off.</p>

<h2 id="pitfalls">What Commonly Goes Wrong?</h2>
<ul>
<li>Purchase events firing twice when the thank-you page is refreshed; use the transaction ID and test.</li>
<li>Values sent without currency, or in mixed currencies.</li>
<li>Apps and the platform both sending the same events.</li>
<li>Test orders left in the live data.</li>
<li>Nobody checking DebugView after theme or app changes.</li>
</ul>

<h2 id="privacy">What About Privacy and Consent?</h2>
<p>Never send names, phone numbers, emails or addresses to GA4; Google's policies prohibit personal information in Analytics. Use order IDs instead. If you have visitors from the UK or EU, cookie consent rules apply, and Google's consent mode can adjust tracking based on choices. Mention analytics in your privacy policy.</p>

<h2 id="setup">Getting It Set Up</h2>
<p>Our stores, from {P['store']}, include GA4 ecommerce events and payment-method tracking, tested in DebugView before launch. See <a href="/digital/ecommerce-development">e-commerce development</a>.</p>
<p>See also <a href="/digital/blog/ecommerce-seo-pakistan-store">Ecommerce SEO in Pakistan</a>.</p>
""",
    faqs=[
        ('Does GA4 track ecommerce automatically?',
         "No. Google's Analytics Help says ecommerce events are not sent automatically and must be added to your site, app or Tag Manager set-up. Some platforms, including Shopify through its pixel, send some events for you. Test with DebugView, because reports can take up to 24 hours."),
        ('Which GA4 events does an online store need?',
         "The core set is view_item_list, view_item, add_to_cart, begin_checkout, add_shipping_info, add_payment_info, purchase and refund. Together they show the path from browsing to buying and where shoppers drop off. Each event should include an items array with product details."),
        ('How do I track cash on delivery orders in GA4?',
         "Record the payment method as a parameter on add_payment_info and purchase so reports can separate COD from prepaid orders. When a COD parcel is refused or returned, send a refund event with the same transaction ID and items, so revenue figures stay accurate."),
        ('Why does GA4 show more revenue than I actually received?',
         "Common causes are refused COD parcels not recorded as refunds, purchase events firing twice when customers refresh the thank-you page, test orders in live data and duplicate events from apps. Fix each cause and compare GA4 revenue against your order system monthly."),
        ('Which ecommerce numbers should I check every week?',
         "Sessions to purchase rate, add-to-cart rate by product, checkout completion rate, revenue after refunds, COD refusal rate and revenue by traffic source. These few numbers show whether the store is improving and where to act, without drowning in dozens of reports nobody reads."),
        ('Can I send customer phone numbers to GA4?',
         "No. Google's policies prohibit sending personally identifiable information such as names, phone numbers, emails or addresses to Analytics. Use order IDs and product data instead. Mention analytics in your privacy policy and handle cookie consent for visitors from the UK or EU."),
        ('GA4 mein COD orders ka hisaab kaise rakhein?',
         "Order lagne par purchase event jaata hai, lekin jo parcel wapas aa jaye uske liye refund event bhejna zaroori hai, warna sales zyada nazar aayengi. Payment ka tareeqa, COD ya card, bhi saath record karein. Customer ka naam ya phone number GA4 mein kabhi na bhejein."),
    ],
    sources=[('Google Analytics Help — Measure ecommerce', 'https://support.google.com/analytics/answer/12200568'), ('Google Analytics developers — Measure ecommerce (GA4)', 'https://developers.google.com/analytics/devguides/collection/ga4/ecommerce'), ('Google Analytics Help — Best practices to avoid sending PII', 'https://support.google.com/analytics/answer/6366371'), ('ICO — UK GDPR guidance and resources', 'https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/')],
    method="Event names, the not-automatic note, Shopify pixel mention, 24-hour delay, DebugView, refund items rule and the currency recommendation come from Google Analytics Help and developer pages checked 30 October 2026. The KPI table and COD approach are editorial. Our prices come from the published list.",
    related=['abandoned-cart-recovery-whatsapp', 'ecommerce-seo-pakistan-store', 'eid-sale-website-readiness'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/ecommerce-development', 'Online store service')],
    cta='Not sure your sales data is right?',
    wa='Hi%2C%20I%20read%20your%20GA4%20ecommerce%20tracking%20guide',
)
