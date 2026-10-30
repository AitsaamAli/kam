import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=180,
    slug='website-testing-before-sign-off',
    title='Website User Acceptance Testing: A 30-Minute Owner Check',
    h1="Website User Acceptance Testing: An Owner's 30-Minute Check Before Sign-Off",
    crumb='Website Testing Before Sign-Off',
    description='Website user acceptance testing for owners: a 30-minute check of phone layout, forms, payments, speed and content before you sign off and make the final payment.',
    keyword='website user acceptance testing',
    cluster=['uat checklist website', 'test website before launch', 'website sign off'],
    category='Hiring a Developer',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="Website user acceptance testing is the owner's final check that the site works as agreed before sign-off. In about 30 minutes, test it on your own phone, submit every form, place a test order, click every button and link, read every page for errors and check contact details. Report issues in one list, then sign off in writing.",
    takeaways=["Acceptance testing checks the site against the agreed scope, from a customer's point of view.", "Test on your own phone first, then a computer.", "Submit every form and place a real test order or booking.", "Read every page for wrong prices, numbers and addresses.", "Report issues in one numbered list, and sign off in writing once fixed."],
    body=f"""
<h2 id="what">What Is Website User Acceptance Testing?</h2>
<p>Developers test as they build, but the owner knows the business best: the right prices, the correct phone number, how customers actually behave. Website user acceptance testing, often shortened to UAT, is the stage where you check that the site does what was agreed before you sign it off and make the final payment. It does not need technical skills. It needs about half an hour, your phone and a checklist.</p>
<p>Testing is the last step in the hiring journey that begins with selecting a web development company. It complements our full website launch checklist.</p>

<h2 id="checklist">What Is in the 30-Minute Check?</h2>
<table>
<tr><th>Minutes</th><th>Check</th><th>What to look for</th></tr>
<tr><td>0 to 8</td><td>Phone layout</td><td>Every page on your own phone: readable text, tappable buttons, no sideways scrolling</td></tr>
<tr><td>8 to 13</td><td>Forms</td><td>Submit each form; confirm the email arrives and the visitor sees a thank-you message</td></tr>
<tr><td>13 to 18</td><td>WhatsApp and calls</td><td>Tap every WhatsApp and phone button; check the number and pre-filled message</td></tr>
<tr><td>18 to 23</td><td>Payments or bookings</td><td>Place a test order or booking with each payment method; check confirmations</td></tr>
<tr><td>23 to 27</td><td>Content</td><td>Read prices, addresses, hours, names and spelling on every page</td></tr>
<tr><td>27 to 30</td><td>Speed and links</td><td>Open pages on mobile data; click menu items and footer links</td></tr>
</table>

<h2 id="phone">Why Start on a Phone?</h2>
<p>Most of your visitors will use phones, often mid-range Android models on mobile data. Test on your own phone using mobile data rather than office Wi-Fi to see what customers see. Rotate the screen, try the menu, and check that pop-ups can be closed easily.</p>

<h2 id="forms">How Do You Test Forms and Orders Properly?</h2>
<p>Use realistic details. For forms, check where the email goes, whether it reaches the inbox rather than spam, and whether the person filling it in gets a confirmation. For stores, place an order with each payment method, including cash on delivery, and check order emails, stock reduction and the admin view. Ask the developer how to cancel test orders afterwards. Our guide to <a href="/digital/blog/email-going-to-spam-fix">emails going to spam</a> helps if notifications are missing.</p>

<h2 id="content">What Content Errors Are Most Common?</h2>
<ul>
<li>Old or placeholder prices.</li>
<li>Wrong phone numbers, especially one digit off.</li>
<li>Placeholder text such as "Lorem ipsum" left on inner pages.</li>
<li>Outdated hours, including Friday or Ramadan timings.</li>
<li>Staff or services that no longer exist.</li>
<li>Broken or missing images.</li>
</ul>

<h2 id="report">How Should You Report Issues?</h2>
<p>Make one numbered list with the page, the device, what you expected and what happened, plus a screenshot. Mark each issue as blocking (must fix before launch) or minor. Send the list once, not piece by piece. Items that were never in scope are change requests, not defects; our <a href="/digital/blog/website-change-requests-cost">change requests guide</a> explains the difference.</p>

<h2 id="signoff">When Should You Sign Off?</h2>
<p>Sign off in writing once blocking issues are fixed and you have rechecked them. At handover, confirm you have all logins, that the domain and hosting are in your name and that you have a backup. Our handover checklist lists everything to collect. Sign-off usually triggers the final milestone payment, after which, in our projects, the code becomes yours.</p>

<h2 id="overseas">What If You Are Testing From Abroad?</h2>
<p>Overseas owners should also ask someone in the target market to test, because speed, payment methods and phone formats differ. Share a short checklist and ask for screenshots.</p>

<h2 id="privacy">What About Test Data?</h2>
<p>Use your own details or clearly fake ones for tests, never real customers' data. Ask the developer to remove test orders and form entries before launch.</p>

<h2 id="ours">How We Handle Acceptance</h2>
<p>Every project we deliver, from {P['starter']}, includes an acceptance checklist and a fix round before final payment. See our <a href="/digital/contact">contact page</a>.</p>
""",
    faqs=[
        ('What is website user acceptance testing?',
         "It is the owner's final check that a website works as agreed before signing it off and making the final payment. It focuses on what customers experience: layout on phones, forms, buttons, payments or bookings, content accuracy, links and speed. No technical skills are needed."),
        ('How long does website acceptance testing take?',
         "For a typical small business website, a focused check takes about 30 minutes using a checklist: phone layout, forms, WhatsApp and call buttons, payments or bookings, content accuracy, speed and links. Larger stores or web apps need longer and more structured testing."),
        ('What should I test before signing off my website?',
         "Check every page on your own phone, submit every form and confirm the emails arrive, tap every WhatsApp and phone button, place test orders or bookings with each payment method, read all prices, addresses and hours, and click menu and footer links."),
        ('How should I report problems found during testing?',
         "Make one numbered list showing the page, device, what you expected and what happened, with a screenshot for each item. Mark each issue as blocking or minor, and send the list once. Items that were never in scope should be treated as change requests."),
        ('When should I make the final payment for my website?',
         "After blocking issues found in acceptance testing are fixed and rechecked, and you have confirmed you hold all logins, the domain and hosting are in your name, and a backup exists. Sign off in writing at that point, which usually triggers the final milestone."),
        ('Should I use real customer data when testing?',
         "No. Use your own details or clearly fake ones for test forms and orders, never real customers' information. Ask the developer to remove test orders, bookings and form entries before launch, so reports and inboxes start clean and no test data is left behind."),
        ('Website sign off se pehle kya check karein?',
         "Apne phone par har page dekhein, har form bhej kar dekhein ke email aati hai, WhatsApp aur call ke button dabayein, test order ya booking karein, aur qeematein, pata aur auqaat ghaur se parhein. Masail aik list mein bhejein aur theek hone ke baad likh kar sign off karein."),
    ],
    sources=[('web.dev — Core Web Vitals', 'https://web.dev/articles/vitals'), ('W3C WAI — Easy checks: a first review of web accessibility', 'https://www.w3.org/WAI/test-evaluate/preliminary/'), ('Google Search Central — Mobile site and mobile-first indexing', 'https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing')],
    method="The 30-minute checklist and reporting method are editorial; timings are a guide. Code ownership after final payment is an approved business fact about our projects. Our prices come from the published list.",
    related=['website-change-requests-cost', 'website-discovery-meeting-what-to-expect', 'how-to-give-website-design-feedback'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/contact', 'Get a written quote')],
    cta='About to sign off a new website?',
    wa='Hi%2C%20I%20read%20your%20website%20testing%20guide',
)
