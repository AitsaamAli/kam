import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=102,
    slug='website-designer-wahdat-road-awan-town',
    title='Website Designer on Wahdat Road: Meet Us in Awan Town',
    h1='Website Designer on Wahdat Road and Awan Town: Meet the Team Down the Road',
    crumb='Wahdat Road Website Designer',
    description='A website designer on Wahdat Road? Our only office is in Awan Town by Rizwan Park. Walk-in hours, who you meet, what to bring and what each package costs.',
    keyword='website designer wahdat road',
    cluster=['web developer awan town', 'website design near wahdat road', 'web designer near me lahore wahdat road'],
    category='Local Guides',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer=f"A website designer on Wahdat Road you can visit: Kamboh Associates Digital works from Rizwan Block Market in Awan Town, facing Rizwan Park, open 6 days a week. Message us on WhatsApp, drop in, and leave with a written scope. Small business websites start from {P['starter']}.",
    takeaways=["Our office is in Rizwan Block Market, Awan Town, facing Rizwan Park, a short way off Wahdat Road.", "Message on WhatsApp before you come, so the right person is in to meet you.", "A first visit is free and usually takes 30 to 45 minutes.", "You meet the people who will scope and build your site, not a sales agent.", "Wahdat Road businesses can be online quickly with a one-page or 5-page site and a Google Business Profile."],
    body=f"""
<h2 id="where">Where Is a Website Designer on Wahdat Road You Can Walk Into?</h2>
<p>Most "website designer near me" searches around Wahdat Road return freelancer ads with a phone number and nothing else. Our office is a real shop front you can visit: number 34 in Rizwan Block Market, Awan Town, Lahore 54660, facing Rizwan Park. Awan Town sits beside Wahdat Road, with Allama Iqbal Town and Samanabad close by, so for most businesses on the road we are a short drive away.</p>
<p>If you are unsure of the turn, ask anyone locally for Rizwan Park. The market's shops look onto the park. Or message us on WhatsApp at 0328-4675162 and we will send the exact pin.</p>

<h2 id="hours">When Can You Walk In?</h2>
<table>
<tr><th>Day</th><th>Hours (Pakistan time)</th><th>Good for</th></tr>
<tr><td>Monday to Thursday</td><td>9:00 AM to 6:00 PM</td><td>First meetings, design reviews, handovers</td></tr>
<tr><td>Friday</td><td>9:00 AM to 12:30 PM</td><td>Short meetings and quick questions</td></tr>
<tr><td>Saturday</td><td>9:00 AM to 6:00 PM</td><td>Owners who are busy during the week</td></tr>
<tr><td>Sunday</td><td>Closed</td><td>Send a WhatsApp message; we reply on Monday</td></tr>
</table>
<p>Walk-ins are welcome when someone is free, but a quick WhatsApp message first means you will not wait.</p>

<h2 id="who-you-meet">Who Will You Meet, and What Happens?</h2>
<p>You meet the team that scopes and builds the website, so technical questions get real answers on the spot. A typical first visit runs like this:</p>
<ol>
<li>You describe your business, customers and how they contact you today.</li>
<li>We show live examples of the kind of site that suits you, on a phone and a screen.</li>
<li>We agree the pages, features and any online payments you need.</li>
<li>We explain prices, timeline and what you will need to provide.</li>
<li>Within one business day, you receive a written scope and fixed price on WhatsApp or email.</li>
</ol>
<p>There is no charge for the visit and no pressure to sign on the day. If you already have a website, bring it up on your phone; we will tell you honestly whether it needs fixing or replacing.</p>

<h2 id="bring">What Should You Bring?</h2>
<ul>
<li>your logo, or a photo of your signboard if you have no logo file yet</li>
<li>a list of what you sell, and prices if you are willing to show them</li>
<li>photos of your shop, products or work on your phone</li>
<li>the phone number customers should call or WhatsApp</li>
<li>logins for any domain, hosting, Facebook or Instagram page you already have</li>
</ul>

<h2 id="wahdat-businesses">What Do Wahdat Road and Awan Town Businesses Usually Need?</h2>
<p>Wahdat Road is a busy commercial road lined with shops, showrooms, eateries, banks and private schools, while Awan Town behind it is mainly residential, with neighbourhood services such as tutors, salons, bakeries and clinics serving the surrounding streets. For these businesses, a website mainly needs to be found on Google Maps, show what you offer and prices, and make it one tap to WhatsApp or call. Our guide to Google Business Profile in Pakistan covers the Maps side.</p>
<table>
<tr><th>Need</th><th>Simplest fix</th><th>Starting price</th></tr>
<tr><td>Be found on Maps</td><td>Verified Google Business Profile linked to a site</td><td>Included with every site</td></tr>
<tr><td>One page with services and WhatsApp</td><td>Landing page</td><td class="price">{P['landing']}</td></tr>
<tr><td>Full information site</td><td>Up to 5 pages</td><td class="price">{P['starter']}</td></tr>
<tr><td>Orders with delivery</td><td>Online store with COD</td><td class="price">{P['store']}</td></tr>
</table>

<h2 id="after-launch">What Support Do You Get After Launch?</h2>
<p>Being nearby helps after launch too. If you need a price changed or a new photo added, you can send it on WhatsApp or bring it in. Optional maintenance at {P['maint']} a month covers updates, backups and small changes. For the full picture of how we work near Iqbal Town, read our <a href="/digital/blog/website-developer-allama-iqbal-town-lahore">Iqbal Town and nearby areas guide</a>, and see <a href="/digital/blog/website-design-samanabad-lahore">our Samanabad guide</a> if your shop is on that side. Visit our <a href="/digital/web-development-lahore">Lahore team page</a> to book.</p>
""",
    faqs=[
        ('Where exactly is your office near Wahdat Road?',
         "We are at shop number 34 in Rizwan Block Market, Awan Town, Lahore 54660, facing Rizwan Park. Awan Town sits beside Wahdat Road. Ask locally for Rizwan Park, or message 0328-4675162 on WhatsApp and we will send a map pin before you set off."),
        ('Can I walk in without an appointment?',
         "Yes, during opening hours, if someone is free. The office opens at 9:00 AM six days a week, closes at 6:00 PM, and closes early on Friday at 12:30 PM. A short WhatsApp message first means the right person will be ready and you will not wait."),
        ('Is the first meeting free?',
         "Yes. The first visit is free and usually takes 30 to 45 minutes. We discuss your business, show suitable examples and explain prices. Within one business day, you receive a written scope and fixed price, with no obligation to go ahead."),
        ('What does a website cost for a shop on Wahdat Road?',
         f"For a shop on Wahdat Road, a single page with services and a WhatsApp button costs {P['landing']}, five pages cost {P['starter']}, and an online store with cash on delivery from {P['store']}. Prices are published and the same across Lahore, and every project starts with a written scope."),
        ('Do you help with Google Maps listings?',
         "Yes. We help set up or fix your Google Business Profile with you as the owner, link it to your website and make sure your address, phone and hours match everywhere. For many local shops, the Maps listing brings more customers than the website alone."),
        ('Wahdat Road ke qareeb website banane wala daftar kahan hai?',
         "Hamara daftar Awan Town ki Rizwan Block Market mein, Rizwan Park ke samne, dukan number 34 hai. Somwar se Hafta subah 9 se shaam 6 baje tak khula hai, Jumma ko sirf dopehar sadhe 12 tak. Aane se pehle WhatsApp 0328-4675162 par message kar dein."),
    ],
    sources=[('Google Business Profile Help — Create and manage your Business Profile', 'https://support.google.com/business/answer/7039811'), ('Google Business Profile Help — Verify your business', 'https://support.google.com/business/answer/7107242'), ('Google Search Central — Local business structured data', 'https://developers.google.com/search/docs/appearance/structured-data/local-business'), ("ICANN — Registrants' benefits and responsibilities", 'https://www.icann.org/resources/pages/benefits-2013-09-16-en'), ('WhatsApp Help Center — How to use click to chat', 'https://faq.whatsapp.com/5913398998672934')],
    method="Office address, hours and prices are our approved business facts. Wahdat Road and Awan Town descriptions are general local knowledge with no statistics. The visit steps describe our actual process. Business Profile points follow Google's help pages, checked 30 October 2026.",
    related=['website-developer-allama-iqbal-town-lahore', 'website-design-samanabad-lahore', 'lahore-web-design-prices-by-area'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/web-development-lahore', 'Our Lahore team')],
    cta='On Wahdat Road and need a website?',
    wa='Hi%2C%20I%20read%20your%20Wahdat%20Road%20guide%20and%20want%20to%20visit',
)
