import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=151,
    slug='homepage-content-guide',
    title='Homepage Content: What to Write, Section by Section',
    h1='Homepage Content Guide: What to Write on Your Homepage, Section by Section',
    crumb='Homepage Content Guide',
    description='Homepage content for a small business: a section-by-section guide in mobile-first order, with illustrative Pakistani examples and links to every content guide.',
    keyword='homepage content',
    cluster=['what to put on homepage', 'homepage copy examples', 'business homepage structure'],
    category='Content and Conversion',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="Good homepage content tells a visitor within 5 seconds what you do, for whom and where, then proves it and shows the next step. In mobile-first order: a clear headline, a call or WhatsApp button, main services, proof such as reviews and real photos, a price signal, a short about section, FAQs and contact details.",
    takeaways=["Most visitors decide within seconds whether they are in the right place, so the headline does the heavy lifting.", "Write for phones first: the top of the screen must show what you do and how to contact you.", "Specific beats impressive: say what you do, where and for whom, instead of adjectives.", "Proof, such as real reviews, photos and numbers, persuades more than claims.", "Every section should lead to one action: call, WhatsApp, book or buy."],
    body=f"""
<h2 id="why">Why Does Homepage Content Matter So Much?</h2>
<p>The homepage is usually the most visited page on a small business website and the one owners struggle with most. The temptation is to fill it with a slider, a welcome message and a list of everything the business has ever done. Visitors on a phone in Lahore or Leeds do not read like that. They glance at the top of the screen, decide whether they are in the right place, and either scroll for reassurance or leave. Good homepage content is built for that behaviour.</p>
<p>This guide is the hub of our series on website content and conversion. It sets out each section in the order it should appear on a phone, with illustrative examples, and links to detailed guides for each part. Preparing this content before a build also shortens projects; see our website brief template.</p>

<h2 id="sections">What Sections Should a Homepage Have?</h2>
<table>
<tr><th>Order</th><th>Section</th><th>Job it does</th></tr>
<tr><td>1</td><td>Headline and subheading</td><td>Say what you do, for whom and where</td></tr>
<tr><td>2</td><td>Primary action</td><td>Call, WhatsApp, book or shop button</td></tr>
<tr><td>3</td><td>Main services or product categories</td><td>Let visitors pick their path</td></tr>
<tr><td>4</td><td>Proof</td><td>Reviews, real photos, numbers, client logos with permission</td></tr>
<tr><td>5</td><td>Price signal</td><td>Prices, "from" prices or how pricing works</td></tr>
<tr><td>6</td><td>How it works</td><td>Three or four steps from enquiry to result</td></tr>
<tr><td>7</td><td>Short about section</td><td>Who is behind the business, since when, where</td></tr>
<tr><td>8</td><td>FAQs</td><td>Answer the questions that stop people enquiring</td></tr>
<tr><td>9</td><td>Contact and location</td><td>Phone, WhatsApp, address, map, hours</td></tr>
</table>
<p>This order works for most service firms, shops and clinics, though some will skip a section or two. Online stores usually move product categories higher, while clinics and salons put booking first.</p>

<h2 id="headline">What Makes a Good Homepage Headline?</h2>
<p>Name the service, the customer and, for local businesses, the place. Compare these illustrative examples:</p>
<ul>
<li>Weak: "Welcome to Excellence Solutions, where quality meets innovation."</li>
<li>Better: "AC installation and repair in Johar Town and DHA, Lahore. Same-day visits."</li>
<li>Weak: "Your trusted partner in fashion."</li>
<li>Better: "Unstitched lawn and khaddar suits, delivered across Pakistan in 2 to 5 days."</li>
</ul>
<p>The subheading adds one detail that matters to buyers: experience, delivery, guarantee terms you genuinely offer, or who you serve. These examples are invented to show the pattern.</p>

<h2 id="action">Where Should the Call to Action Go?</h2>
<p>Put one main action directly under the headline, visible without scrolling on a phone, and repeat it after key sections. For most Pakistani small businesses that is a WhatsApp button with a pre-filled message plus a phone number; for shops, "Shop lawn suits"; for clinics, "Book an appointment". Our WhatsApp button guide explains pre-filled messages and tracking.</p>

<h2 id="services">How Should Services Be Presented?</h2>
<p>Show three to six main services or categories as cards with a plain name, one line of description and a link to a full page. Each service page then does the detailed selling, as covered in our <a href="/digital/blog/service-page-structure">service page structure guide</a>.</p>

<h2 id="proof">What Counts as Proof?</h2>
<p>Real reviews with names and permission, photos of your actual work, team and premises, numbers you can stand behind (years in business, projects completed), and logos of clients who have agreed to be shown. Avoid stock photos of strangers shaking hands. See our guides on <a href="/digital/blog/reviews-testimonials-on-website">reviews and testimonials</a>, <a href="/digital/blog/stock-photos-vs-real-photos">stock versus real photos</a> and <a href="/digital/blog/trust-signals-for-small-business-website">trust signals</a>.</p>

<h2 id="prices">Should the Homepage Mention Prices?</h2>
<p>Where possible, yes. Even a "from" price or a link to a price list filters out poor-fit enquiries and builds trust. We publish ours: landing pages from {P['landing']}, starter websites from {P['starter']}. Our guide on <a href="/digital/blog/show-prices-on-website-or-not">whether to show prices</a> covers businesses where this is harder.</p>

<h2 id="about">How Much About Us Belongs on the Homepage?</h2>
<p>A short paragraph: who runs the business, since when, where you are, and what makes your approach different, with a link to the full page. Our <a href="/digital/blog/about-us-page-that-builds-trust">About Us guide</a> covers the full version.</p>

<h2 id="faqs-contact">How Should FAQs and Contact Details Close the Page?</h2>
<p>Four to six FAQs that answer the real hesitations: price, timing, area served, payment methods. Then full contact details: phone, WhatsApp, email, address, map and hours, matching your Google Business Profile exactly. A short form is optional; our <a href="/digital/blog/contact-forms-that-convert">contact form guide</a> explains how to keep it short.</p>

<h2 id="language">Should the Homepage Be in English or Urdu?</h2>
<p>Write in the language your customers search and read in. Many Pakistani businesses use English with a few Roman Urdu touches; some serve Urdu-first audiences and need a proper Urdu version. Our <a href="/digital/blog/urdu-english-bilingual-website">bilingual website guide</a> explains the set-up.</p>

<h2 id="writing">Who Should Write It?</h2>
<p>You know your customers best, so a draft from you, edited for clarity, usually beats generic copy. If writing is not your strength, our guide on <a href="/digital/blog/website-copywriting-cost-pakistan">website content writing</a> compares doing it yourself and hiring a writer.</p>

<h2 id="mistakes">What Are the Most Common Homepage Mistakes?</h2>
<ul>
<li><strong>A slogan instead of a description.</strong> "Excellence in every project" tells a visitor nothing.</li>
<li><strong>Rotating sliders.</strong> Most visitors see only the first slide, and sliders slow mobile pages.</li>
<li><strong>Everything at once.</strong> Twenty services listed in a block of text overwhelm people; group them.</li>
<li><strong>No visible contact option</strong> on the first screen of a phone.</li>
<li><strong>Stock photos</strong> of people who obviously do not work for you.</li>
<li><strong>Old news</strong>, such as an Eid offer from two years ago, which suggests the business is inactive.</li>
</ul>

<h2 id="test">How Can You Test Your Homepage?</h2>
<p>Show the homepage on a phone to three people who do not know your business for five seconds, then ask what you do, where, and how they would contact you. If they cannot answer, the top section needs work. After launch, compare clicks on the WhatsApp and call buttons month by month, and look at which services people tap most; our guide to visitors who do not enquire covers what to check when enquiries are low.</p>

<h2 id="privacy">What Privacy Points Apply to Homepage Content?</h2>
<p>Use customer names, photos and logos only with permission, and keep staff personal numbers off public pages. If the homepage has a form, link to your privacy policy beside it.</p>

<h2 id="build">How We Help Write Your Homepage</h2>
<p>Every business website we build, from {P['business']}, starts with this structure and a content checklist. See <a href="/digital/business-websites">business websites</a>.</p>
""",
    faqs=[
        ('What should I put on my homepage?',
         "In mobile-first order: a clear headline saying what you do, for whom and where; a main action such as WhatsApp or call; your main services; proof such as reviews and real photos; a price signal; how it works; a short about section; FAQs; and full contact details."),
        ('How long should homepage content be?',
         "Long enough to answer the main questions, short enough to scan. Most small business homepages work well with brief sections, each a heading plus two or three lines or a few cards, linking to detailed pages. The top of the screen on a phone matters far more than total length."),
        ('What makes a good homepage headline?',
         "It names the service, the customer and, for local businesses, the place, in plain words. For example, AC repair in Johar Town and DHA, Lahore, same-day visits, works better than a slogan about quality and innovation. Add one useful detail in the subheading."),
        ('Should I use a slider on my homepage?',
         "Usually not. Sliders hide most of their messages, slow pages on mobile and push the headline and call to action down. A single strong headline with one real photo and a clear button generally serves visitors better than rotating banners."),
        ('Where should the WhatsApp or call button go?',
         "Directly under the headline, visible without scrolling on a phone, then repeated after key sections such as services and reviews. A floating WhatsApp button also helps. Use a pre-filled message so you know which page each enquiry came from and can reply in context."),
        ('Should my homepage show prices?',
         "Where possible, yes. A from price or a link to a price list filters out poor-fit enquiries and builds trust. If prices vary widely, explain how pricing works and give typical ranges or examples instead of hiding the topic completely."),
        ('Do I need FAQs on my homepage?',
         "A few short FAQs help, especially for the questions that stop people enquiring: price, timing, area served and payment methods. Keep the full list on a separate page or on service pages, and make sure answers match what your staff say on the phone."),
        ('Should I write my own homepage content?',
         "You know your customers best, so a draft from you is valuable even if someone edits it. If writing is not your strength, a writer can interview you and shape the text. Avoid generic copy that could describe any business in any city."),
        ('Homepage par kya likhna chahiye?',
         "Sab se upar saaf likhein ke aap kya kaam karte hain, kis ke liye aur kis ilaqe mein. Uske neeche WhatsApp ya call ka button, phir services, asli reviews aur tasveerein, qeemat ka andaza, chhota sa taaruf, aam sawal aur raabte ki tafseel dein. Mobile par sab se upar wala hissa sab se ahem hai."),
    ],
    sources=[('Google Search Central — Creating helpful, reliable, people-first content', 'https://developers.google.com/search/docs/fundamentals/creating-helpful-content'), ('Google Search Central — SEO starter guide', 'https://developers.google.com/search/docs/fundamentals/seo-starter-guide'), ('W3C WAI — WCAG overview', 'https://www.w3.org/WAI/standards-guidelines/wcag/'), ('WhatsApp Help Center — How to use click to chat', 'https://faq.whatsapp.com/5913398998672934')],
    method="The section order and headline guidance are editorial, based on how visitors use small business homepages on phones. All headline examples are invented and labelled illustrative; they do not describe real businesses. Our prices come from the published list.",
    related=['service-page-structure', 'about-us-page-that-builds-trust', 'trust-signals-for-small-business-website'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/business-websites', 'Business website service')],
    cta='Not sure what your homepage should say?',
    wa='Hi%2C%20I%20read%20your%20homepage%20content%20guide',
)
