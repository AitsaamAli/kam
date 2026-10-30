import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=89,
    slug="website-visitors-no-enquiries",
    title="Website Gets Visitors but No Enquiries? 12 Fixes",
    h1="Website Gets Visitors but No Enquiries? A 12-Point Audit and the Fixes That Work",
    crumb="Visitors but No Enquiries",
    description="Website no enquiries despite visitors? Use this 12-point audit: wrong traffic, hidden contact options, weak trust signals, broken forms and the fixes that work.",
    keyword="website no enquiries",
    cluster=["website traffic no leads", "website not converting", "increase website enquiries", "contact form not working",
             "website conversion audit", "website se leads kyun nahin aate"],
    category="Getting Found Online",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=("A website with visitors but no enquiries usually has 1 of 4 problems: the wrong visitors, contact options that are hard to "
            "find, too little trust, or a broken form. Check that forms and WhatsApp links actually work, put a call and WhatsApp button "
            "on every page, show prices and proof, and measure clicks before redesigning."),
    takeaways=[
        "First check whether enquiries are being lost: test every form, email and WhatsApp link yourself.",
        "Visitors from irrelevant searches or cheap traffic will never enquire, however good the page.",
        "Contact options must be visible on every page, especially on phones.",
        "Prices, real photos, reviews and named people build the trust that turns visits into messages.",
        "Measure button clicks and form submissions, so you know what changed after each fix.",
    ],
    body=f"""
<h2 id="first-check">Why Does a Website Get Visitors but No Enquiries?</h2>
<p>Few things frustrate a business owner more than an analytics report showing hundreds of visitors and an inbox showing none. Before redesigning anything, run a simple audit. In our experience, the cause is usually one of four things: enquiries are being lost by a broken form, the visitors are the wrong people, contacting you is harder than it looks, or the page does not earn enough trust.</p>

<h2 id="audit">What Is the 12-Point Audit?</h2>
<table>
<tr><th>#</th><th>Check</th><th>Fix if it fails</th></tr>
<tr><td>1</td><td>Submit every form yourself; does the email arrive?</td><td>Fix email delivery; send a copy to WhatsApp or a second inbox</td></tr>
<tr><td>2</td><td>Tap every WhatsApp and call button on a phone</td><td>Correct the number format and links</td></tr>
<tr><td>3</td><td>Which searches and pages bring visitors?</td><td>Stop paying for irrelevant traffic; target buyer searches</td></tr>
<tr><td>4</td><td>Is contact visible without scrolling on a phone?</td><td>Add a sticky call and WhatsApp bar on mobile</td></tr>
<tr><td>5</td><td>Do pages show prices or price guidance?</td><td>Add starting prices or ranges</td></tr>
<tr><td>6</td><td>Is it clear what you do within five seconds?</td><td>Rewrite the first screen: service, area, benefit</td></tr>
<tr><td>7</td><td>Are there real photos, names and an address?</td><td>Replace stock images; add team and premises</td></tr>
<tr><td>8</td><td>Are there genuine reviews or examples?</td><td>Link to Google reviews; add real project examples</td></tr>
<tr><td>9</td><td>How long is the enquiry form?</td><td>Cut it to name, phone and a short message</td></tr>
<tr><td>10</td><td>Does the page load quickly on mobile data?</td><td>Fix images, hosting and scripts</td></tr>
<tr><td>11</td><td>Is there one clear next step per page?</td><td>One main button, repeated, not five competing ones</td></tr>
<tr><td>12</td><td>Are clicks and submissions measured?</td><td>Set up events in Google Analytics</td></tr>
</table>

<h2 id="lost-enquiries">Are Enquiries Being Lost Without You Knowing?</h2>
<p>Start with checks 1 and 2, because they cost nothing and are common. Website forms often stop sending email after a hosting change or plugin update, and messages land in spam. A WhatsApp link with a number written as 0328-4675162 instead of the international format will not open the right chat. Test from a phone and a computer, and ask a friend to test from their own phone.</p>

<h2 id="wrong-traffic">Are You Attracting the Wrong Visitors?</h2>
<p>Look at Google Search Console's search queries and your analytics traffic sources. A Lahore caterer ranking for "biryani recipe" gets visitors who want to cook, not hire. Cheap advertising clicks and social media visits from outside your service area also inflate numbers without enquiries. Focus on pages and adverts that match buying searches, such as "catering service in Lahore for 200 guests".</p>

<h2 id="trust">How Do You Build Trust on the Page?</h2>
<p>Pakistani buyers are cautious with businesses they find online. Show what they can verify: a real address and map, a landline or a named contact person, photos of your premises and team, prices or starting prices, real project examples, genuine reviews and how long you have been in business. Remove anything that looks copied, such as stock photos of foreign offices.</p>

<h2 id="contact-options">How Should Contact Options Look on Mobile?</h2>
<p>On phones, put a fixed bar at the bottom of the screen with Call and WhatsApp buttons, visible on every page. Many Pakistani customers prefer sending a WhatsApp message to filling in a form. Keep forms short for those who prefer them. Our <a href="/digital/blog/whatsapp-button-website-leads">WhatsApp button guide</a> shows how to set up pre-filled messages and track clicks.</p>

<h2 id="measure">How Do You Know What Worked?</h2>
<p>Set up events in Google Analytics for WhatsApp clicks, call clicks and form submissions. Google's recommended events include one for lead generation. Change one or two things at a time, then compare enquiries over the next few weeks. Without measurement, a redesign is a guess.</p>

<h2 id="what-we-build">How We Turn Visitors Into Enquiries</h2>
<p>We can run this 12-point audit on your existing site and fix what fails, under maintenance at {P['maint']} a month or as a one-off scoped job. If the site needs rebuilding, our websites include mobile call and WhatsApp bars, short forms, trust sections and click tracking as standard, from {P['starter']}. Use our <a href="/digital/contact">contact page</a> to request an audit, and read the <a href="/digital/blog/get-business-website-on-google">guide to getting your website on Google</a>.</p>
""",
    faqs=[
        ("Why does my website get traffic but no leads?",
         "Usually one of four reasons: enquiries are being lost by a broken form or wrong WhatsApp link, the visitors are not potential buyers, contact options are hard to find on phones, or the page does not build enough trust. Test every form and button first, then check traffic sources and trust signals."),
        ("How do I check if my contact form is working?",
         "Submit it yourself from a phone and a computer and confirm the email arrives, including in spam. Ask someone else to test too. Forms often stop sending after hosting changes or plugin updates, so retest after any change, and consider sending a copy of each enquiry to a second inbox."),
        ("Does adding a WhatsApp button increase enquiries?",
         "Often, in Pakistan, because many customers prefer sending a WhatsApp message to filling in a form. Place Call and WhatsApp buttons in a fixed bar on mobile, use the international number format, pre-fill a short message and track clicks in Google Analytics to measure the effect."),
        ("Should I show prices on my website to get more enquiries?",
         "Usually yes. Starting prices or ranges filter out people who cannot afford you and reassure those who can, who are then more likely to contact you. Explain what changes the final price. Hidden prices make many visitors leave rather than ask, especially with businesses they do not know."),
        ("How do I track enquiries from my website?",
         "Set up events in Google Analytics for form submissions, WhatsApp button clicks and call button clicks. Google's recommended events include one for lead generation. Check them in the Realtime or DebugView reports after setting up, then compare enquiry numbers before and after each change you make."),
        ("Website par log aate hain lekin rabta kyun nahin karte?",
         "Pehle khud form aur WhatsApp button test karein ke kaam kar rahe hain ya nahin. Phir dekhein ke sahi log aa rahe hain ya nahin. Har page par call aur WhatsApp button rakhein, qeemat ka andaza dein, asli tasveerein aur reviews dikhayen, aur form chhota rakhein."),
    ],
    sources=[
        ("Google Analytics Help — Recommended events", "https://support.google.com/analytics/answer/9267735"),
        ("Google Search Console Help — About Search Console", "https://support.google.com/webmasters/answer/9128668"),
        ("WhatsApp Help Center — How to use click to chat", "https://faq.whatsapp.com/5913398998672934"),
        ("Nielsen Norman Group — Usability 101", "https://www.nngroup.com/articles/usability-101-introduction-to-usability/"),
        ("Google Search Central — Creating helpful, reliable, people-first content", "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"),
    ],
    method=("Analytics event guidance comes from Google Analytics Help, and search query checks from Search Console Help, checked 29 October "
            "2026. The 12-point audit reflects the problems we most often find on client sites; it is not a published study. The caterer "
            "example is illustrative. Prices are our own packages."),
    related=["get-business-website-on-google", "whatsapp-button-website-leads", "website-speed-pakistan-mobile",
             "seo-ready-website-checklist"],
    service_links=[("/digital/contact", "Request a 12-point audit"), ("/digital/business-websites", "Websites built to convert")],
    cta="Getting visitors but no messages?",
    wa="Hi%2C%20I%20read%20your%20website%20no%20enquiries%20guide%20and%20need%20an%20audit",
)
