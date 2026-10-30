import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=137,
    slug='store-shipping-rates-and-delivery-page',
    title='Shipping Policy Page: Delivery Charges and Times Explained',
    h1='Your Shipping Policy Page: How to Present Delivery Charges and Times on a Pakistani Store',
    crumb='Shipping Policy Page',
    description='How to write a shipping policy page for a Pakistani store: a delivery table by city, free shipping thresholds with simple maths, COD fees and dispatch cut-off times.',
    keyword='shipping policy page',
    cluster=['delivery charges website pakistan', 'shipping rates by city', 'free delivery threshold'],
    category='E-commerce in Pakistan',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="A good shipping policy page tells customers, before checkout, what delivery costs, how long it takes to their city, whether cash on delivery has an extra fee, and when orders are dispatched. Use a simple table by city or zone, show the same figures on product and cart pages, and review it every 3 months and before Eid.",
    takeaways=["Surprise delivery charges are a leading reason customers abandon checkout.", "A short table by city or zone answers most delivery questions at a glance.", "Free delivery thresholds should be set with simple maths, not guesswork.", "If cash on delivery costs extra, say so on the product page, not only at the last step.", "State dispatch cut-off times and holiday delays clearly."],
    body=f"""
<h2 id="why">Why Does a Shipping Policy Page Matter?</h2>
<p>"Delivery charges kitne hain?" and "Karachi kab tak pohanche ga?" are probably the two most common WhatsApp questions a Pakistani online store receives. A clear shipping policy page answers them once, for everyone, and supports the checkout by removing surprises. Baymard Institute's checkout research lists unexpected extra costs, including shipping, as the most common reason shoppers abandon a purchase, and slow delivery as another frequent one. Our <a href="/digital/blog/abandoned-cart-recovery-whatsapp">abandoned cart guide</a> covers the wider checkout picture.</p>
<p>Delivery terms are one of the pages covered in our store launch guide.</p>

<h2 id="table">What Should the Delivery Table Look Like?</h2>
<p>Group cities into zones that match your courier's pricing and real delivery times. An illustrative example for a Lahore-based store:</p>
<table>
<tr><th>Zone</th><th>Cities</th><th>Delivery charge</th><th>Usual delivery time</th></tr>
<tr><td>Same city</td><td>Lahore</td><td>Rs 150</td><td>1 to 2 working days</td></tr>
<tr><td>Major cities</td><td>Karachi, Islamabad, Rawalpindi, Faisalabad, Multan</td><td>Rs 250</td><td>2 to 4 working days</td></tr>
<tr><td>Other cities and towns</td><td>Rest of Pakistan</td><td>Rs 300</td><td>3 to 6 working days</td></tr>
<tr><td>Remote areas</td><td>Areas your courier lists as remote</td><td>Rs 400</td><td>5 to 8 working days</td></tr>
</table>
<p>These figures are invented for illustration. Use your own courier rates and the times you actually achieve, measured from your order records, not the courier's best case.</p>

<h2 id="free-delivery">How Do You Set a Free Delivery Threshold?</h2>
<p>Free delivery above a set order value can lift basket sizes, but it must still leave you a profit. A simple way to check, using illustrative numbers:</p>
<ol>
<li>Find your average order value, say Rs 3,200.</li>
<li>Find your average delivery cost per order to you, say Rs 250.</li>
<li>Set the threshold somewhat above the average order, say Rs 4,000, so customers add an item to qualify.</li>
<li>Check the margin: if your gross margin is around 40%, an extra Rs 800 of goods adds about Rs 320 of margin, more than the Rs 250 delivery you now absorb.</li>
</ol>
<p>Run the same check with your own numbers, and review after a month by comparing average order value and margin before and after.</p>

<h2 id="cod-fee">How Should You Show a Cash on Delivery Fee?</h2>
<p>Some stores add a fee for cash on delivery because couriers charge for cash collection and refused parcels cost money. If you do, show it on product pages and in the cart ("Cash on delivery: Rs 100 extra"), not as a surprise at the last step. Many stores instead build the cost into prices and offer a small discount for prepaid orders. Either way, be consistent. Our COD guide explains how to reduce refused orders.</p>

<h2 id="cut-off">What About Dispatch Times and Cut-Offs?</h2>
<p>Customers judge you by when the parcel arrives, so say when orders leave: "Orders confirmed by 3 PM, Monday to Saturday, are dispatched the same day." Mention Sundays and public holidays, and post a notice before Eid with the last order date for pre-Eid delivery. If you integrate with your courier, tracking numbers can be sent automatically; see our courier integration guide.</p>

<h2 id="contents">What Else Belongs on the Page?</h2>
<ul>
<li>Which couriers you use and how customers receive tracking details.</li>
<li>What happens if the customer is unavailable or refuses the parcel.</li>
<li>How damaged or wrong items should be reported, with a link to your exchange and refund policy.</li>
<li>International delivery, if offered, with a note that the buyer handles any import charges in their country.</li>
<li>A WhatsApp number for delivery questions.</li>
</ul>

<h2 id="privacy">What Data Do Couriers Receive?</h2>
<p>Your courier needs the customer's name, phone and address. Mention this in your privacy policy, and share only what the courier needs, not order histories or payment details.</p>

<h2 id="build">How We Build It In</h2>
<p>Our stores, from {P['store']}, calculate delivery charges by zone at checkout and show them on product and cart pages. See <a href="/digital/ecommerce-development">e-commerce development</a>.</p>
<p>See also <a href="/digital/blog/ecommerce-seo-pakistan-store">Ecommerce SEO in Pakistan</a>.</p>
""",
    faqs=[
        ('What should a shipping policy page include?',
         "Delivery charges by city or zone, usual delivery times, any cash on delivery fee, dispatch cut-off times, couriers used and how tracking is shared, what happens with refused parcels, how to report damaged items, holiday notices and a contact number for delivery questions."),
        ('How should I show delivery charges by city?',
         "Use a short table grouping cities into zones that match your courier's rates and your real delivery times, for example same city, major cities, other cities and remote areas. Show the same charges on product and cart pages so there are no surprises at checkout."),
        ('How do I decide a free delivery threshold?',
         "Start from your average order value and average delivery cost. Set the threshold somewhat above the average order, then check that the extra margin from larger baskets covers the delivery you absorb. Review average order value and margin after a month and adjust."),
        ('Should I charge extra for cash on delivery?',
         "Some stores do, because cash collection and refused parcels cost money. If you charge extra, show it clearly on product and cart pages. Alternatively, include the cost in prices and offer a small discount for prepaid orders. Consistency and clarity matter most."),
        ('What delivery times should I promise?',
         "Promise the times you actually achieve, measured from your own order records, not the courier's best case. Give ranges in working days by zone, state your dispatch cut-off time, and post notices before Eid and other holidays when couriers are slower."),
        ('Do I need a separate shipping page if I show charges at checkout?',
         "Yes. Many customers check delivery terms before adding anything to the cart, and search engines and AI tools can only read what is on a page. A dedicated shipping page also gives your team one link to share on WhatsApp instead of retyping answers."),
        ('Delivery charges website par kaise dikhayen?',
         "Shehron ko zones mein baant kar aik saada table banayein jismein charges aur din likhe hon. Yehi charges product aur cart page par bhi dikhayen taake checkout par koi surprise na ho. COD ki extra fee ho to pehle se batayen, aur Eid se pehle aakhri order ki tareekh likh dein."),
    ],
    sources=[('Baymard Institute — Cart abandonment rate statistics', 'https://baymard.com/lists/cart-abandonment-rate'), ('Google Merchant Center Help — Product data specification', 'https://support.google.com/merchants/answer/7052112'), ('Google Search Central — SEO starter guide', 'https://developers.google.com/search/docs/fundamentals/seo-starter-guide')],
    method="The checkout abandonment reasons come from Baymard Institute's page, checked 30 October 2026. The delivery table, charges and free-delivery calculation use invented figures, labelled as illustrative. No courier is named or priced. Our prices come from the published list.",
    related=['abandoned-cart-recovery-whatsapp', 'return-refund-policy-online-store-pakistan', 'ecommerce-seo-pakistan-store'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/ecommerce-development', 'Online store service')],
    cta='Customers keep asking about delivery?',
    wa='Hi%2C%20I%20read%20your%20shipping%20policy%20page%20guide',
)
