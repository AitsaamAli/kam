import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=152,
    slug='about-us-page-that-builds-trust',
    title='How to Write an About Us Page That Builds Trust',
    h1='Writing an About Us Page That Builds Trust: Real Facts, Real People, No Invented Claims',
    crumb='About Us Page',
    description='How to write an About Us page that builds trust: real facts over adjectives, team photos, founding year, address and credentials, with a simple structure.',
    keyword='about us page',
    cluster=['about us page examples', 'company profile website', 'about page writing'],
    category='Content and Conversion',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="A good About Us page answers who is behind the business, how long you have operated, where you are and why customers can trust you, using checkable facts instead of adjectives. Include the founders or team with real photos, the founding year, your address, genuine credentials and 3 or 4 things that set your way of working apart.",
    takeaways=["Visitors read About pages to check you are real and reliable, not to admire your vision statement.", "Facts that can be checked, such as a founding year, address and registrations, build more trust than adjectives.", "Real photos of real people outperform stock images for small businesses.", "Never invent awards, client numbers or years of experience.", "End with a clear next step, such as a contact button or links to services."],
    body=f"""
<h2 id="why">Why Do Visitors Read the About Us Page?</h2>
<p>When someone is about to pay a business they have never met, especially online, they look for reassurance. The About Us page is where many go to check: is this a real business, who runs it, how long has it existed, and where is it? In Pakistan, where buyers are wary of fake online shops and fly-by-night service providers, a convincing About Us page can decide whether an enquiry happens. It is usually among the most visited pages after the homepage and service pages.</p>
<p>This guide belongs to our content series, which starts with the <a href="/digital/blog/homepage-content-guide">homepage content guide</a>.</p>

<h2 id="structure">What Structure Works for an About Us Page?</h2>
<table>
<tr><th>Section</th><th>What to include</th></tr>
<tr><td>Opening</td><td>One or two sentences on what you do, for whom, where and since when</td></tr>
<tr><td>Story</td><td>How and why the business started, in plain words, briefly</td></tr>
<tr><td>People</td><td>Founders and key team members with real photos, roles and relevant experience</td></tr>
<tr><td>How you work</td><td>Three or four specifics, such as same-day replies, written quotes or fixed prices</td></tr>
<tr><td>Proof</td><td>Genuine registrations, memberships, certifications, notable projects with permission</td></tr>
<tr><td>Location</td><td>Full address, map, office hours and photos of the premises</td></tr>
<tr><td>Next step</td><td>Contact button and links to services</td></tr>
</table>

<h2 id="facts">Why Do Facts Beat Adjectives?</h2>
<p>"We are a leading, innovative, customer-focused company" could describe anyone and convinces no one. Compare an illustrative alternative: "Started in 2012 by two electrical engineers, we have installed solar systems for homes and factories across Lahore and Sheikhupura. Our office and store are on Ferozepur Road, open Monday to Saturday." Each sentence can be checked, which is exactly what makes it believable. Our own parent firm, Kamboh Associates, was established in 2008, and we say that plainly rather than calling ourselves experienced.</p>

<h2 id="people">How Should You Present the Team?</h2>
<p>Use real photos, taken in decent light, of the people customers will actually deal with. Give names, roles and one or two relevant facts, such as qualifications or years in the trade. Ask each person for permission before publishing their photo and name, and do not publish personal phone numbers. If staff privacy is a concern, show the founders and describe the team without individual photos.</p>

<h2 id="credentials">Which Credentials Should You Show?</h2>
<p>Show only what is genuine and current: professional body memberships, licences, registrations, certifications from manufacturers or platforms, and awards you can document. Link to the issuing body's verification page where one exists. Never display logos of organisations you are not actually registered with, or awards you did not receive. Invented credentials are easy for competitors and customers to expose, and the damage to trust lasts. Our <a href="/digital/blog/trust-signals-for-small-business-website">trust signals guide</a> covers this in more depth.</p>

<h2 id="tone">What Tone Should It Use?</h2>
<p>Write as you would speak to a customer across the counter: direct, warm and specific. Use "we" and "you". Short paragraphs read better on phones. If many customers are more comfortable in Urdu, a short Urdu summary or a bilingual version helps; see our <a href="/digital/blog/urdu-english-bilingual-website">bilingual website guide</a>.</p>

<h2 id="mistakes">What Mistakes Should You Avoid?</h2>
<ul>
<li>Long histories that bury the basics under several paragraphs.</li>
<li>Mission and vision statements with no concrete meaning.</li>
<li>Stock photos of strangers presented as your team.</li>
<li>An address missing or different from your Google Business Profile.</li>
<li>Claims such as "best in Pakistan" or "number one" without evidence.</li>
<li>No way to contact you from the page.</li>
</ul>

<h2 id="search">Does the About Us Page Help Search and AI Visibility?</h2>
<p>It can. Search engines and AI tools look for consistent information about who a business is: name, founding date, location, people and what it does. A factual About page, matching your Google listing and directory entries, supports that consistency. Our <a href="/digital/blog/ai-search-optimisation-checklist-local-business">AI search checklist</a> lists related steps.</p>

<h2 id="privacy">What Privacy Points Apply to Team Photos and Bios?</h2>
<p>Get written permission for staff photos and names, avoid publishing home addresses or personal numbers, and remove former employees promptly.</p>

<h2 id="build">How We Help With Your About Page</h2>
<p>Our business websites, from {P['business']}, include an About page built from a short questionnaire about your business. See <a href="/digital/business-websites">business websites</a>.</p>
""",
    faqs=[
        ('What belongs on an About Us page?',
         "What you do, for whom and where; when and why the business started; the founders or team with real photos; how you work; genuine credentials; your full address, map and hours; and a clear contact button. Checkable facts persuade visitors far more than adjectives or slogans."),
        ('How long should an About Us page be?',
         "Usually a few short sections that a visitor can scan on a phone in a minute or two. Lead with the essentials: what you do, since when and where. A long company history can go further down the page or be left out entirely."),
        ('Should I put team photos on my About Us page?',
         "Yes, if possible. Real photos of the people customers will deal with build trust far better than stock images. Ask each person for permission before publishing their photo and name, and never publish their personal phone numbers or home addresses anywhere on the site."),
        ('Can I mention awards and certifications on my website?',
         "Only genuine, current ones you can document. Link to the issuing body's verification page where available. Never show logos of organisations you are not registered with or awards you did not receive, because invented credentials are easily exposed and damage trust."),
        ('Does an About Us page help SEO?',
         "It helps search engines and AI tools understand who the business is, when it started, where it operates and who runs it. Keeping these facts consistent with your Google Business Profile and directory listings supports accurate information about your business across search results."),
        ('What tone should an About Us page use?',
         "Write as you would talk to a customer face to face: direct, warm and specific. Use we and you, short paragraphs and plain words. Avoid corporate phrases such as leading provider or innovative solutions that could describe any company anywhere."),
        ('About Us page mein kya likhna chahiye?',
         "Saaf likhein ke aap kya kaam karte hain, kab se, kahan aur kis ke liye. Maalik ya team ki asli tasveerein, mukammal pata, auqaat-e-kaar aur sirf asli certificates dikhayen. Bade bade daawe ya jhoote awards bilkul na likhein, aur page ke aakhir mein raabte ka button zaroor rakhein."),
    ],
    sources=[('Google Search Central — Creating helpful, reliable, people-first content', 'https://developers.google.com/search/docs/fundamentals/creating-helpful-content'), ('Google Business Profile Help', 'https://support.google.com/business/'), ('Google Search Central — Organization structured data', 'https://developers.google.com/search/docs/appearance/structured-data/organization')],
    method="The structure, tone advice and mistakes list are editorial. The solar business example is invented for illustration. Our parent firm's founding year (2008) is an approved business fact. Our prices come from the published list.",
    related=['homepage-content-guide', 'trust-signals-for-small-business-website', 'urdu-english-bilingual-website', 'ai-search-optimisation-checklist-local-business'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/business-websites', 'Business website service')],
    cta='Need an About page people believe?',
    wa='Hi%2C%20I%20read%20your%20About%20Us%20page%20guide',
)
