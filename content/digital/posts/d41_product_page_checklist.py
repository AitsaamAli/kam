import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=41,
    slug="product-page-checklist-pakistan",
    title="Product Page Best Practices: A Pakistani Store Checklist",
    h1="Product Page Best Practices for Pakistani Online Stores: A 15-Point Checklist With Examples",
    crumb="Product Page Checklist",
    description="Product page best practices for Pakistani stores: a 15-point checklist for photos, size charts, delivery, COD and reviews, with Roman Urdu examples.",
    keyword="product page best practices",
    cluster=["product description examples", "ecommerce product page checklist", "urdu product description",
             "how to write product description", "product page design", "product page par kya likhein"],
    category="E-commerce in Pakistan",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=("Product page best practices for a Pakistani store come down to 15 checks: several real photos, a clear price, sizes or "
            "specifications, stock per variant, delivery charge and time, COD availability, returns terms, genuine reviews and a WhatsApp "
            "button. Customers should never need to message you to learn the basics."),
    takeaways=[
        "Show several real photos per product, including close-ups and the product in use.",
        "Put the full price, delivery charge, delivery time and COD availability on the product page itself.",
        "Give a size chart or specification table, and show stock for each size or variant.",
        "Write short, specific descriptions in plain English, with a Roman Urdu line where your buyers expect it.",
        "Show only genuine reviews, and make it easy to ask a question on WhatsApp.",
    ],
    body=f"""
<h2 id="why">Why Do Product Page Best Practices Matter So Much?</h2>
<p>The product page is where a visitor decides to buy or leave. In a shop, a customer can touch the fabric and ask the shopkeeper. Online, the page must answer those questions. When it does not, the customer messages you, waits, then often buys elsewhere.</p>
<p>The Nielsen Norman Group, a respected usability research firm, notes in its product page guidelines that one product view is rarely enough to answer shoppers' questions, and that descriptions should lead with key facts because people skim. The Baymard Institute's checkout research found unexpected extra costs, such as shipping, to be the top checkout-related reason shoppers abandon, cited by 40%. Both point the same way: show more, hide less.</p>

<h2 id="checklist">What Should Every Product Page Include?</h2>
<table>
<tr><th>#</th><th>Element</th><th>What good looks like</th></tr>
<tr><td>1</td><td>Product name</td><td>Plain and specific: "Black Cotton Kurta, Straight Cut"</td></tr>
<tr><td>2</td><td>Photos</td><td>At least 4: front, back, close-up, worn or in use</td></tr>
<tr><td>3</td><td>Price</td><td>Full price in rupees, with any discount shown honestly</td></tr>
<tr><td>4</td><td>Variants</td><td>Sizes, colours or weights as buttons, not a hidden list</td></tr>
<tr><td>5</td><td>Stock per variant</td><td>"Only 2 left in M" or "Out of stock in L"</td></tr>
<tr><td>6</td><td>Size chart or specs</td><td>Measurements in inches and centimetres, or a spec table</td></tr>
<tr><td>7</td><td>Short description</td><td>Three to five lines of key facts first</td></tr>
<tr><td>8</td><td>Material and care</td><td>Fabric, ingredients or build, and how to care for it</td></tr>
<tr><td>9</td><td>Delivery charge</td><td>Charge by city, or "free over Rs X"</td></tr>
<tr><td>10</td><td>Delivery time</td><td>"2 to 4 working days in major cities"</td></tr>
<tr><td>11</td><td>COD availability</td><td>Clear yes or no, with any order limit</td></tr>
<tr><td>12</td><td>Returns and exchange</td><td>One line plus a link to the full policy</td></tr>
<tr><td>13</td><td>Reviews</td><td>Genuine buyer reviews, with photos if possible</td></tr>
<tr><td>14</td><td>WhatsApp button</td><td>Opens a chat with the product name already written</td></tr>
<tr><td>15</td><td>Speed</td><td>Opens quickly on a mid-range phone over mobile data</td></tr>
</table>

<h2 id="photos">How Should You Photograph Products?</h2>
<p>Use real photos, not only supplier images that appear on dozens of other stores. Shoot in daylight or with a simple light box, on a plain background, from the same angles for every product. For clothing, show the item worn, the fabric close up and the embroidery or print detail. For food, show the portion size next to a familiar object. Compress images before upload, so pages load quickly on mobile data.</p>

<h2 id="descriptions">How Do You Write Descriptions That Sell?</h2>
<p>Lead with facts, then add feeling. Here are original examples you can adapt.</p>
<p><strong>English, clothing:</strong> "Unstitched 3-piece lawn suit. Printed front, back and sleeves, chiffon dupatta, cotton trouser. Shirt fabric 3 metres. Colour may vary slightly from screen."</p>
<p><strong>Roman Urdu line for the same product:</strong> "3 piece unstitched suit, shirt ka kapra 3 meter, chiffon dupatta. Rang screen se thora mukhtalif ho sakta hai."</p>
<p><strong>English, skincare:</strong> "50 ml vitamin C serum for daily use. Apply 2 to 3 drops after cleansing. Patch test first. Store away from sunlight."</p>
<p>Keep each product's description unique. Copying the same text across many products, or from a supplier, weakens your pages in Google search and does not answer buyers' questions.</p>

<h2 id="delivery-cod">Why Show Delivery and COD Details on the Product Page?</h2>
<p>Pakistani shoppers want to know three things before adding to cart: what delivery costs, how long it takes, and whether they can pay cash on delivery. Showing these on the product page, not only at checkout, prevents the surprise that makes shoppers abandon. If you charge a partial advance on some orders, say so here as well. Our guide to <a href="/digital/blog/cod-website-fake-orders-pakistan">cutting COD fake orders</a> explains when that makes sense.</p>

<h2 id="reviews">How Should You Handle Reviews?</h2>
<p>Show only genuine reviews from real buyers. Fake reviews are easy to spot, damage trust when found out, and break most platforms' rules. Ask buyers for a review with a WhatsApp message a few days after delivery, and invite a photo. Show negative reviews too, with a polite reply; a page with only perfect reviews looks less believable.</p>

<h2 id="mistakes">What Are the Most Common Product Page Mistakes?</h2>
<ul>
<li>"DM for price" or prices only in images.</li>
<li>One blurry photo, or only supplier photos.</li>
<li>No size chart, leading to wrong sizes and returns.</li>
<li>Showing a size as available when it is sold out.</li>
<li>Delivery charges revealed only at the last step.</li>
<li>Large, uncompressed images that load slowly on mobile.</li>
</ul>

<h2 id="what-we-build">How We Build Product Pages for Pakistani Stores</h2>
<p>When we build a store, starting at {P['store']}, every product page gets templates with variant buttons, stock per size, a size chart section, delivery and COD notes, a returns summary, reviews and a pre-filled WhatsApp button. We compress images on upload and test pages on mid-range Android phones. See our <a href="/digital/ecommerce-development">online store development</a> service. If you sell clothing, read our <a href="/digital/blog/clothing-brand-website-pakistan">clothing brand website guide</a>, and for the full set-up, <a href="/digital/blog/start-online-store-pakistan">how to start an online store in Pakistan</a>.</p>
""",
    faqs=[
        ("What should a product page include?",
         "A good product page includes several real photos, a clear price, variant buttons with stock per size, a size chart or specifications, a short factual description, material and care details, delivery charge and time, cash on delivery availability, a returns summary, genuine reviews and a WhatsApp button for questions."),
        ("How many photos should a product have?",
         "At least four for most products: front, back, a close-up of material or detail, and the product worn or in use. Usability research from the Nielsen Norman Group notes that one product view is rarely enough. Use real photos, consistent angles and compressed files so pages load quickly."),
        ("Should I write product descriptions in Urdu?",
         "Write in plain English for clarity and search, and add a short Roman Urdu or Urdu line where your buyers expect it, for example fabric length or care notes. Keep both short and factual. If most customers ask questions in Roman Urdu on WhatsApp, a Roman Urdu line on the page helps."),
        ("Should I show delivery charges on the product page?",
         "Yes. Unexpected extra costs such as delivery are a leading reason shoppers abandon checkout, according to Baymard Institute research. Show the delivery charge or a free-delivery threshold, the delivery time and whether cash on delivery is available on the product page, before the customer reaches checkout."),
        ("Can I use supplier photos and descriptions?",
         "You can start with them if you have permission, but replace them with your own as soon as possible. The same images and text appear on many other stores, which makes your products harder to trust and to find on Google. Your own photos and unique descriptions answer buyers' questions better."),
        ("Product page par kya kya likhna zaroori hai?",
         "Product page par saaf tasveerein, poori qeemat, size chart, har size ka stock, delivery charges aur waqt, COD ki sahulat, return policy aur asli reviews zaroor dein. Aik WhatsApp button bhi rakhein jismein product ka naam pehle se likha ho, taake customer aasani se sawal pooch sake."),
    ],
    sources=[
        ("Nielsen Norman Group — UX guidelines for ecommerce product pages", "https://www.nngroup.com/articles/ecommerce-product-pages/"),
        ("Baymard Institute — Cart abandonment rate statistics", "https://baymard.com/lists/cart-abandonment-rate"),
        ("Google Search Central — Creating helpful, reliable, people-first content", "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"),
        ("web.dev — Largest Contentful Paint", "https://web.dev/articles/lcp"),
        ("WhatsApp Help Center — How to use click to chat", "https://faq.whatsapp.com/5913398998672934"),
    ],
    method=("Product page guidance draws on the Nielsen Norman Group's ecommerce product page guidelines (2019) and Baymard Institute's "
            "checkout research (updated 22 September 2025), checked 29 October 2026. The 15-point checklist and the English and Roman "
            "Urdu descriptions are our own original examples. Store prices are our own."),
    related=["start-online-store-pakistan", "clothing-brand-website-pakistan", "cod-website-fake-orders-pakistan",
             "instagram-whatsapp-shop-to-website"],
    service_links=[("/digital/ecommerce-development", "Stores with product pages that sell"), ("/digital/contact", "Get your product pages reviewed")],
    cta="Want product pages that answer every question?",
    wa="Hi%2C%20I%20read%20your%20product%20page%20checklist%20and%20need%20help%20with%20my%20store",
)
