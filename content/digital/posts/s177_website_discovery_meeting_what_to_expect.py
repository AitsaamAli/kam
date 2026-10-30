import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=177,
    slug='website-discovery-meeting-what-to-expect',
    title='Website Discovery Meeting: What to Prepare and Expect',
    h1='Your First Website Discovery Meeting: What to Prepare, What We Ask and What You Decide',
    crumb='Website Discovery Meeting',
    description='What happens in a website discovery meeting: a typical agenda, documents and examples to bring, the questions a good developer asks, and the decisions you will make.',
    keyword='website discovery meeting',
    cluster=['website consultation', 'questions web designer will ask', 'website kickoff meeting'],
    category='Hiring a Developer',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="A website discovery meeting is a first working session, usually 45 to 90 minutes, where you and the developer agree goals, audience, pages, features, content, budget and timeline. Bring examples you like, your logo, a rough page list, and the questions customers ask most. You should leave with a clear scope and a written quote to follow.",
    takeaways=["The meeting is about your business goals first, design second.", "Bring examples of sites you like and dislike, with reasons.", "Know your rough budget and deadline; it saves time for both sides.", "Expect questions about customers, content, features and who will maintain the site.", "A written scope and quote should follow, ideally within a few working days."],
    body=f"""
<h2 id="purpose">What Is a Website Discovery Meeting For?</h2>
<p>Before any design starts, a good web developer sits down with you to understand the business, the people the site must serve and what success looks like. This website discovery meeting turns a vague idea, "we need a new website", into a defined project with pages, features, content responsibilities, a timeline and a price. It also helps you judge the developer: do they listen, ask useful questions and explain things plainly? Many disputes later in a project trace back to a rushed or skipped first meeting.</p>
<p>This guide is part of our series on working with a developer, which starts with how to choose a web development company.</p>

<h2 id="agenda">What Does a Typical Agenda Look Like?</h2>
<table>
<tr><th>Part</th><th>Time</th><th>What is covered</th></tr>
<tr><td>Your business</td><td>10 to 15 min</td><td>What you sell, to whom, where, and what makes you different</td></tr>
<tr><td>Goals</td><td>10 min</td><td>Enquiries, sales, bookings, trust, recruitment</td></tr>
<tr><td>Audience</td><td>10 min</td><td>Who visits, on which devices, in which languages</td></tr>
<tr><td>Pages and features</td><td>15 to 20 min</td><td>Page list, forms, payments, booking, integrations</td></tr>
<tr><td>Content</td><td>10 min</td><td>Who writes, who supplies photos, deadlines</td></tr>
<tr><td>Budget, timeline, next steps</td><td>10 min</td><td>Range, launch date, decision-makers, quote timing</td></tr>
</table>

<h2 id="bring">What Should You Bring?</h2>
<ul>
<li>Two or three websites you like and one or two you dislike, with reasons.</li>
<li>Your logo files and any brand colours or fonts.</li>
<li>A rough list of pages you think you need.</li>
<li>The ten questions customers ask most often on WhatsApp or the phone.</li>
<li>Logins or details for your current domain, hosting and website, if any.</li>
<li>Your budget range and any fixed launch date.</li>
</ul>
<p>Our website brief template organises all of this in one document; filling it in before the meeting makes it far more productive.</p>

<h2 id="questions">Which Questions Will a Good Developer Ask?</h2>
<ul>
<li>What should a visitor do on the site: call, WhatsApp, book, buy?</li>
<li>Which services or products matter most to your business?</li>
<li>Who are your main competitors, and what do they do well online?</li>
<li>Do you need Urdu, Arabic or other languages?</li>
<li>Which payment methods, couriers or systems must connect?</li>
<li>Who will update the site after launch?</li>
<li>Who approves designs and content, and how quickly?</li>
</ul>
<p>If a developer asks none of these and jumps straight to colours and templates, treat that as a warning sign.</p>

<h2 id="decide">What Will You Need to Decide?</h2>
<p>By the end of the meeting, or soon after, you should settle the page list, the main features, who provides content, the approval process and a realistic launch date. You do not need to decide every detail; open questions can be listed in the scope. Clear decisions now prevent change requests later, which our guide on <a href="/digital/blog/website-change-requests-cost">change requests</a> explains.</p>

<h2 id="budget">Should You Share Your Budget?</h2>
<p>Yes, at least a range. It lets the developer suggest what is realistic and avoid proposing a design you cannot afford. Published prices help too: our landing pages start from {P['landing']}, starter websites from {P['starter']} and business websites from {P['business']}, so you can match scope to budget before the meeting.</p>

<h2 id="after">What Should Happen After the Meeting?</h2>
<p>You should receive a written scope and quote listing pages, features, timeline, payment milestones, what you must provide and what is excluded. We reply to enquiries within one business day and send quotes after the scope is agreed. Compare it against your notes, and ask questions before signing. Our contract checklist covers what the agreement should include.</p>

<h2 id="remote">Can the Meeting Be Online?</h2>
<p>Yes. Many discovery meetings happen by video call, especially with overseas clients. Share your screen to show sites you like, and record the call with permission so nothing is lost. For local clients, our office in Awan Town, Lahore, is open Monday to Saturday, with shorter hours on Friday.</p>

<h2 id="privacy">What Information Is Shared?</h2>
<p>You may share logins, customer examples and business plans. Share passwords through a secure method, not plain WhatsApp messages, and change them after the project. Ask about confidentiality if your plans are sensitive.</p>

<h2 id="book">Booking a Discovery Meeting</h2>
<p>Contact us to arrange a meeting at our office or online. See our <a href="/digital/contact">contact page</a>.</p>
<p>Before the design round, read <a href="/digital/blog/how-to-give-website-design-feedback">how to give design feedback developers can use</a>.</p>
""",
    faqs=[
        ('What happens in a website discovery meeting?',
         "You and the developer agree your business goals, audience, pages, features, content responsibilities, budget and timeline. It usually lasts 45 to 90 minutes. A good developer asks many questions about customers and goals before discussing design, and follows up with a written scope and quote."),
        ('What should I prepare for my first meeting with a web developer?',
         "Bring examples of websites you like and dislike with reasons, your logo and brand colours, a rough page list, the questions customers ask most, details of any current domain and hosting, your budget range and any fixed launch date. A filled-in brief template helps greatly."),
        ('What questions will a web designer ask me?',
         "Expect questions about what visitors should do on the site, your most important services or products, competitors, languages, payment and courier needs, who will update the site after launch, and who approves designs and content. These shape the scope, timeline and price."),
        ('Should I tell the developer my budget?',
         "Yes, at least a range. It lets the developer propose a realistic scope instead of guessing, and avoids wasted time on designs you cannot afford. Published price lists also help you match your expectations to typical package costs before the meeting."),
        ('Can a website discovery meeting be done online?',
         "Yes. Many meetings happen by video call, especially with overseas clients. Share your screen to show examples, and record the call with permission so decisions are not lost. Follow up with written notes listing what was agreed and any open questions."),
        ('What should I receive after the discovery meeting?',
         "A written scope and quote listing pages, features, timeline, payment milestones, what you must provide and what is excluded. Compare it with your own notes and ask questions before signing. A clear scope prevents disagreements and extra charges later in the project."),
        ('Website ki pehli meeting mein kya le kar jayen?',
         "Pasandeeda aur napasandeeda websites ki misaalein, apna logo, pages ki andazan list, customers ke aam sawal, maujooda domain aur hosting ki tafseel, aur budget ka andaza saath le jayen. Meeting ke baad likhit scope aur quote zaroor lein aur sign karne se pehle parh lein."),
    ],
    sources=[('Google Search Central — SEO starter guide', 'https://developers.google.com/search/docs/fundamentals/seo-starter-guide'), ('W3C WAI — WCAG overview', 'https://www.w3.org/WAI/standards-guidelines/wcag/'), ('Google Search Central — Creating helpful, reliable, people-first content', 'https://developers.google.com/search/docs/fundamentals/creating-helpful-content')],
    method="The agenda, preparation list and questions are editorial, based on how we and other developers run discovery meetings; timings are typical, not fixed. Our office location, hours and one-business-day reply standard are approved business facts. Our prices come from the published list.",
    related=['website-change-requests-cost', 'website-testing-before-sign-off', 'how-to-give-website-design-feedback'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/contact', 'Get a written quote')],
    cta='Ready to plan your website?',
    wa='Hi%2C%20I%20read%20your%20discovery%20meeting%20guide',
)
