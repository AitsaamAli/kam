import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=139,
    slug='product-photography-for-online-store',
    title='Product Photography for Website: A Low-Budget Guide',
    h1='Product Photography for Your Website: A Low-Budget Guide for Pakistani Online Stores',
    crumb='Product Photography',
    description='Product photography for a website on a small budget: phone setup, natural light, backgrounds, image sizes and WebP, file names and alt text for Pakistani stores.',
    keyword='product photography for website',
    cluster=['product photos for online store', 'mobile product photography', 'image size for website'],
    category='E-commerce in Pakistan',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="Good product photography for a website needs a recent phone, soft window light, a plain background and a steady surface, not an expensive studio. Shoot every product the same way, at least 4 angles plus a detail and a scale shot, then resize and compress images, save them as WebP where supported, and add descriptive alt text.",
    takeaways=["Consistency across products matters more than expensive equipment.", "Soft daylight from a window beats harsh flash or yellow tube lights.", "Show what customers ask about: back, detail, label, size against a hand or model.", "Resize and compress before uploading; oversized images slow mobile pages badly.", "Write alt text that describes the product for people using screen readers and for search."],
    body=f"""
<h2 id="why">Why Does Product Photography for a Website Matter So Much?</h2>
<p>Online shoppers cannot touch the fabric, check the stitching or hold the item. Photos do that job. In Pakistan, where many shoppers still worry that "jo dikhaya woh nahin aaya", honest, clear photos also build trust and reduce exchanges. The good news is that product photography for a website does not need a professional studio. A recent phone, a window and some care produce photos that sell, provided every product is shot the same way.</p>
<p>This guide is part of our e-commerce series led by the online store guide. For the rest of the page, see our product page checklist.</p>

<h2 id="setup">What Is the Simplest Setup?</h2>
<table>
<tr><th>Item</th><th>Low-budget option</th><th>Why</th></tr>
<tr><td>Camera</td><td>A recent mid-range phone, lens cleaned</td><td>Sharp enough for web use</td></tr>
<tr><td>Light</td><td>A large window with indirect daylight</td><td>Soft, true colours</td></tr>
<tr><td>Diffuser</td><td>A white curtain or tracing paper over the window</td><td>Softens harsh sun</td></tr>
<tr><td>Reflector</td><td>White foam board or chart paper</td><td>Fills shadows on the dark side</td></tr>
<tr><td>Background</td><td>White or light grey sheet, or a sweep of chart paper</td><td>Clean, consistent look</td></tr>
<tr><td>Stability</td><td>A cheap phone tripod or stack of books</td><td>No blur, same angle every time</td></tr>
</table>
<p>Avoid shooting under yellow bulbs or mixed light, which shifts colours. For clothing, colour accuracy prevents a large share of exchange requests.</p>

<h2 id="shots">Which Shots Does Each Product Need?</h2>
<ul>
<li><strong>Front</strong> on a plain background, used as the main image.</li>
<li><strong>Back and side</strong> views.</li>
<li><strong>Detail:</strong> embroidery, stitching, texture, buttons, ports or labels.</li>
<li><strong>Scale:</strong> the item in a hand, on a model or next to a familiar object.</li>
<li><strong>In use:</strong> worn, installed or styled, where it helps.</li>
<li><strong>What is in the box,</strong> for electronics and sets.</li>
</ul>
<p>For clothing on models, state the model's height and the size worn. For three-piece suits, show each piece separately as well as together.</p>

<h2 id="consistency">How Do You Keep Photos Consistent?</h2>
<p>Mark the positions of the phone, product and reflector with tape so every shoot matches. Shoot at the same time of day, use the same zoom, and fill the frame similarly. Edit with the same simple adjustments: straighten, crop to a fixed ratio such as square or 4:5, correct white balance, and brighten slightly if needed. Do not change colours to make products look better than they are.</p>

<h2 id="sizes">Which Image Sizes and Formats Should You Use?</h2>
<p>Large photos straight from a phone can be several megabytes each, which makes category pages painfully slow on mobile data. Resize product images to around 1,200 to 2,000 pixels on the longest side, enough for zoom, and compress them. WebP files are usually much smaller than JPEGs at similar quality, and modern browsers support them; platforms such as Shopify serve optimised formats automatically. Google's image SEO guidance recommends high-quality images, descriptive file names and alt text. Our mobile speed guide explains why image weight matters.</p>

<h2 id="alt">How Should You Write File Names and Alt Text?</h2>
<p>Name files descriptively: "black-chiffon-abaya-front.webp" rather than "IMG_4521.jpg". Alt text should describe the image for someone who cannot see it: "Black chiffon abaya with silver embroidery on the sleeves, front view". Keep it natural; do not stuff keywords.</p>

<h2 id="privacy">What About People in Photos?</h2>
<p>If you photograph staff, friends or customers wearing your products, get their written permission, especially for use in ads. Never use customer photos sent on WhatsApp without asking first, and blur faces of children unless parents have agreed.</p>

<h2 id="ai-and-stock">Can You Use Supplier or AI-Edited Photos?</h2>
<p>Supplier photos appear on many other stores and may not match what you deliver. Use them only with permission and when accurate. AI tools can remove backgrounds well, but avoid AI changes that alter the product itself, and follow Google Merchant Center's rules on labelling AI-generated images if you advertise there.</p>

<h2 id="build">How Our Stores Handle Images</h2>
<p>Our stores, from {P['store']}, resize and compress uploaded images automatically and prompt for alt text. See <a href="/digital/ecommerce-development">e-commerce development</a>.</p>
<p>See also <a href="/digital/blog/ecommerce-seo-pakistan-store">Ecommerce SEO in Pakistan</a> and <a href="/digital/blog/abandoned-cart-recovery-whatsapp">Abandoned Cart Recovery for Pakistani Stores</a>.</p>
""",
    faqs=[
        ('Can I take product photos for my website with a phone?',
         "Yes. A recent mid-range phone with a clean lens, soft window light, a plain background and a tripod or steady surface produces photos good enough for most online stores. Consistency across products and accurate colours matter more than expensive cameras or studio equipment."),
        ('What background is best for product photos?',
         "A plain white or light grey background works for most products and keeps the store looking consistent. A sheet of chart paper curved from the wall to the table avoids a visible line. Lifestyle shots with styled backgrounds can be added as extra images."),
        ('How many photos should each product have?',
         "Usually at least four: front, back or side, a close detail and a scale shot such as the item in a hand or on a model. Add in-use and box-contents images where helpful. Show what customers ask about most often on WhatsApp."),
        ('What image size should I upload to my online store?',
         "Around 1,200 to 2,000 pixels on the longest side is enough for zoom on most stores. Compress images before uploading and use WebP where your platform supports it. Very large original phone photos slow down category and product pages, especially on mobile data."),
        ('What is alt text and why does it matter?',
         "Alt text is a short description of an image, read aloud by screen readers and used by search engines to understand pictures. Describe the product naturally, for example colour, material and view, without stuffing keywords. It helps accessibility and image search."),
        ('Can I use photos from my supplier?',
         "Only with permission and when they accurately show what you deliver. Supplier photos also appear on many other stores, so they do little to set you apart. Taking your own photos, even simply, builds more trust and reduces complaints that items look different."),
        ('Mobile se product ki tasveer kaise khenchein?',
         "Khirki ki naram roshni mein, safed ya halki grey background par, phone ko stand par rakh kar tasveer lein. Har product ke aage, peeche, detail aur size wali tasveer zaroor lein. Upload se pehle size chhota karein aur file ka naam product ke mutabiq rakhein, jaise black-abaya-front."),
    ],
    sources=[('Google Search Central — Image SEO best practices', 'https://developers.google.com/search/docs/appearance/google-images'), ('web.dev — Use WebP images', 'https://web.dev/articles/serve-images-webp'), ('Google Merchant Center Help — Product data specification', 'https://support.google.com/merchants/answer/7052112'), ('W3C WAI — Images tutorial (alt text)', 'https://www.w3.org/WAI/tutorials/images/')],
    method="Image format, alt text and image SEO points come from Google Search Central, web.dev and W3C WAI pages. The setup table, shot list and size range are editorial recommendations. Example file names and alt text are illustrative. Our prices come from the published list.",
    related=['ai-product-descriptions-online-store', 'ga4-ecommerce-tracking-setup', 'ecommerce-seo-pakistan-store'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/ecommerce-development', 'Online store service')],
    cta='Product photos not doing your stock justice?',
    wa='Hi%2C%20I%20read%20your%20product%20photography%20guide',
)
