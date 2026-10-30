import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=153,
    slug='service-page-structure',
    title='Service Page Structure That Gets Enquiries',
    h1='Service Page Structure: How to Build a Service Page That Turns Visitors Into Enquiries',
    crumb='Service Page Structure',
    description='A service page structure that gets enquiries: problem, offer, proof, price signal, process, FAQs and a clear call to action, plus a note on structured data.',
    keyword='service page structure',
    cluster=['service page template', 'services page website', 'landing page vs service page'],
    category='Content and Conversion',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="A strong service page structure follows the buyer's questions in order: what the service is and who it is for, what problem it solves, what is included, proof that you deliver, a price or price signal, how the process works, FAQs and a clear call to action. Give each main service its own page rather than 1 list.",
    takeaways=["Give each main service its own page, so it can answer specific questions and rank for specific searches.", "Start with the customer's problem, not your company history.", "Be concrete about what is included and what is not.", "A price, starting price or typical range filters enquiries and builds trust.", "Every service page needs one obvious next step."],
    body=f"""
<h2 id="why">Why Does Service Page Structure Matter?</h2>
<p>Many small business websites list all their services on one page as a block of bullet points. Visitors who need one specific service, say kitchen renovation or corporate gift hampers, find too little detail to decide, and search engines have no page that clearly matches the search. A clear service page structure fixes both problems: one page per main service, built around the questions a buyer asks before getting in touch.</p>
<p>The homepage points visitors here; our <a href="/digital/blog/homepage-content-guide">homepage content guide</a> explains that first step.</p>

<h2 id="template">What Is the Best Order for a Service Page?</h2>
<table>
<tr><th>Section</th><th>Question it answers</th><th>Example (illustrative)</th></tr>
<tr><td>Headline and summary</td><td>Is this what I need?</td><td>"Kitchen renovation in Lahore, designed and fitted in 3 to 5 weeks"</td></tr>
<tr><td>The problem</td><td>Do they understand my situation?</td><td>Old cabinets, poor storage, damp, no ventilation</td></tr>
<tr><td>What is included</td><td>What exactly do I get?</td><td>Design visit, 3D layout, cabinets, counters, fitting, clean-up</td></tr>
<tr><td>Proof</td><td>Can they actually do it?</td><td>Photos of finished kitchens, reviews, number of projects</td></tr>
<tr><td>Price signal</td><td>Can I afford it?</td><td>Typical range or starting price, and what changes it</td></tr>
<tr><td>Process</td><td>What happens after I enquire?</td><td>Visit, quote, deposit, build, handover</td></tr>
<tr><td>FAQs</td><td>What about my specific worry?</td><td>Warranty, timelines, materials, payment</td></tr>
<tr><td>Call to action</td><td>How do I start?</td><td>WhatsApp button, call, booking form</td></tr>
</table>

<h2 id="problem">Why Start With the Problem?</h2>
<p>People search because they have a problem: a leaking roof, a website nobody visits, a slow-moving stock line. Describing that problem in their words shows you understand it, and makes the solution feel relevant. Keep it to a short paragraph or a few bullets, then move quickly to what you offer.</p>

<h2 id="included">How Specific Should "What Is Included" Be?</h2>
<p>As specific as possible. List deliverables, timelines and what the customer must provide. Say what is not included, too: "Electrical rewiring is quoted separately." Clear scope prevents disputes and filters out mismatched expectations. Our own package pages work this way, with each tier listing what it covers.</p>

<h2 id="price">Should a Service Page Show Prices?</h2>
<p>Where you can, yes: a fixed price, a starting price or a typical range, plus what moves the price up or down. We publish ours; for example, our landing pages start from {P['landing']}. When prices truly vary, give example projects with their costs. Our guide on <a href="/digital/blog/show-prices-on-website-or-not">showing prices on your website</a> covers the decision in detail.</p>

<h2 id="landing-vs-service">Is a Landing Page the Same as a Service Page?</h2>
<p>Not quite. A service page is a permanent part of your website, linked from the menu, written to answer questions and to be found in search. A landing page is usually built for a specific campaign, such as a Facebook ad, with one offer and fewer distractions. Many businesses need both. See our landing page cost guide.</p>

<h2 id="common-questions">Which FAQs Belong on a Service Page?</h2>
<p>The questions your staff answer every week on WhatsApp and the phone: timelines, warranty, payment methods, areas served, what happens if something goes wrong. Short, direct answers, ideally under a hundred words each. FAQs also help search engines and AI tools pick up specific answers.</p>

<h2 id="schema">Does a Service Page Need Structured Data?</h2>
<p>Structured data can describe your business, its location and FAQs in a machine-readable way. It must match what is visible on the page. Google limits when some rich results appear, so treat markup as a clarity aid, not a guarantee of special display. Our schema markup guide explains the useful types.</p>

<h2 id="cta">Where Should the Call to Action Go?</h2>
<p>Near the top, after the proof section and at the end. Use the same action throughout, such as "Get a quote on WhatsApp", and pre-fill the message with the service name so you know which page brought the enquiry.</p>

<h2 id="privacy">What About Photos and Reviews of Clients?</h2>
<p>Use project photos and client names only with permission, and avoid showing house numbers, faces or personal details in photos of customers' homes.</p>

<h2 id="build">How We Structure Service Pages</h2>
<p>Our business websites, from {P['business']}, include a separate page for each main service using this structure. See <a href="/digital/business-websites">business websites</a>.</p>
""",
    faqs=[
        ('What is the best service page structure?',
         "Follow the buyer's questions in order: a headline and summary, the problem, what is included, proof, a price signal, the process, FAQs and a clear call to action. This order answers doubts before they stop someone from enquiring, and it works for most service businesses."),
        ('Should each service have its own page?',
         "Yes, for your main services. A separate page can answer specific questions, show relevant proof and match specific searches. Minor services can be grouped on one page, but anything that brings meaningful revenue or enquiries deserves its own detailed page."),
        ('What is the difference between a service page and a landing page?',
         "A service page is a permanent page in your menu, written to answer questions and be found in search. A landing page is usually built for a specific campaign, such as an ad, with one offer and fewer links. Many businesses benefit from having both."),
        ('Should I put prices on service pages?',
         "Where possible, yes. A fixed price, starting price or typical range, with what changes it, filters out poor-fit enquiries and builds trust. When prices vary widely, show two or three example projects with their final costs instead of leaving visitors to guess what they might pay."),
        ('How many FAQs should a service page have?',
         "Usually four to eight, covering the questions customers really ask: timelines, warranty, payment methods, areas served and what happens if something goes wrong. Keep answers short and direct, and update them whenever staff notice new questions being repeated on calls or in WhatsApp chats."),
        ('Does a service page need structured data?',
         "It helps search engines read business details and FAQs reliably, but it must match what is visible on the page, and Google limits some rich results. Treat structured data as a way to make information clearer to machines, not as a guarantee of special display."),
        ('Service page kaise banayein jis se enquiries aayen?',
         "Har bari service ka alag page banayein. Sab se pehle masla aur hal batayein, phir kya shamil hai, apne kaam ki tasveerein aur reviews, qeemat ka andaza, kaam ka tareeqa aur aam sawal likhein. Aakhir mein WhatsApp ya call ka saaf button rakhein."),
    ],
    sources=[('Google Search Central — SEO starter guide', 'https://developers.google.com/search/docs/fundamentals/seo-starter-guide'), ('Google Search Central — Local business structured data', 'https://developers.google.com/search/docs/appearance/structured-data/local-business'), ('Google Search Central — Creating helpful, reliable, people-first content', 'https://developers.google.com/search/docs/fundamentals/creating-helpful-content')],
    method="The section template and advice are editorial. The kitchen renovation example is invented for illustration. Structured data points reflect Google Search Central documentation. Our prices come from the published list.",
    related=['homepage-content-guide', 'show-prices-on-website-or-not', 'about-us-page-that-builds-trust'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/business-websites', 'Business website service')],
    cta='Service pages not bringing enquiries?',
    wa='Hi%2C%20I%20read%20your%20service%20page%20structure%20guide',
)
