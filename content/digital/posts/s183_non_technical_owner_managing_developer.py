import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=183,
    slug='non-technical-owner-managing-developer',
    title='How to Manage a Web Developer When You Are Not Technical',
    h1='How to Manage a Web Developer When You Are Not Technical: Demos, Previews and Plain Reports',
    crumb='Manage a Web Developer',
    description='How to manage a web developer when you are not technical: weekly demos, staging links, plain-language progress reports, milestone payments and the warning signs.',
    keyword='manage web developer',
    cluster=['working with developers non technical', 'how to manage software project', 'check developer progress'],
    category='Hiring a Developer',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="To manage a web developer without technical knowledge, judge progress by what you can see: a weekly demo or staging link, a short plain-language report, and milestones tied to visible results and payments. Ask what was done, what is next and what is blocked. Keep 1 shared task list and insist that accounts are in your name.",
    takeaways=["You do not need to read code; you need to see working results regularly.", "A staging link shows real progress better than any status message.", "Short weekly reports should answer three questions: done, next, blocked.", "Tie payments to milestones you can see and test.", "Keep domain, hosting and code accounts in your business's name."],
    body=f"""
<h2 id="problem">Can You Manage a Web Developer Without Technical Skills?</h2>
<p>Many business owners feel at the mercy of their developer: they cannot judge the code, do not understand the jargon and only find out about problems when deadlines pass. You do not need to become technical to manage a web developer well. You need a simple routine that makes progress visible, a few plain questions, and payments tied to results you can see. This works for websites, stores and web apps alike.</p>
<p>Management starts with hiring well, which our developer selection guide covers.</p>

<h2 id="routine">What Weekly Routine Works?</h2>
<table>
<tr><th>Item</th><th>Frequency</th><th>What you get</th></tr>
<tr><td>Staging or preview link</td><td>Always available</td><td>The work in progress, viewable on your phone</td></tr>
<tr><td>Short written report</td><td>Weekly</td><td>Done, next, blocked, in plain words</td></tr>
<tr><td>Demo call</td><td>Weekly or fortnightly, 15 to 30 minutes</td><td>The developer shows new features working</td></tr>
<tr><td>Shared task list</td><td>Ongoing</td><td>Every task with status and owner</td></tr>
<tr><td>Milestone review</td><td>At each milestone</td><td>You test and approve before payment</td></tr>
</table>

<h2 id="questions">Which Questions Should You Ask?</h2>
<ul>
<li>What did you complete this week, and where can I see it?</li>
<li>What will you work on next week?</li>
<li>Is anything blocked, and do you need something from me?</li>
<li>Are we still on track for the next milestone date?</li>
<li>What are the biggest risks you see right now?</li>
</ul>
<p>Ask the developer to explain any technical term in one sentence. A good developer can.</p>

<h2 id="staging">Why Is a Staging Link So Useful?</h2>
<p>A staging site is a private copy of the website in progress. It lets you see real pages, click buttons and test forms on your phone, rather than relying on descriptions. If weeks pass with nothing new on staging, that is a clear signal to ask questions. Make sure staging is password-protected and hidden from search engines.</p>

<h2 id="milestones">How Should Payments Follow Milestones?</h2>
<p>Tie each payment to something you can see and test: approved designs, key pages built on staging, features working, final launch. We work with a 30 to 40 percent deposit and milestone payments, which keeps both sides committed. Our guide to milestone payments explains typical structures.</p>

<h2 id="warning">Which Warning Signs Should You Watch For?</h2>
<ul>
<li>No preview link, or one that rarely changes.</li>
<li>Reports full of jargon that never say what is finished.</li>
<li>Repeated missed dates without explanation.</li>
<li>Requests for more money before the next milestone is delivered.</li>
<li>Reluctance to put accounts in your name.</li>
<li>Long silences followed by a rush near the deadline.</li>
</ul>
<p>Our guide to <a href="/digital/blog/website-project-delays-why">website project delays</a> explains common causes on both sides.</p>

<h2 id="ownership">Why Must Accounts Be in Your Name?</h2>
<p>Domain, hosting, code repository, analytics and any app store accounts should belong to your business, with the developer given access. If you part ways, you keep everything. Ask for this at the start, not at the end.</p>

<h2 id="second-opinion">When Should You Get a Second Opinion?</h2>
<p>If you are unsure whether progress or quality is reasonable, a short independent review by another developer can help, especially before a large payment. Our guide to <a href="/digital/blog/taking-over-website-from-old-developer">taking over from a previous developer</a> lists what an audit checks.</p>

<h2 id="tools">Which Simple Tools Help?</h2>
<p>A shared task board or even a shared spreadsheet, a single chat group for the project with only the people who need to be there, and a shared folder for content and logos are usually enough. Avoid scattering decisions across personal WhatsApp chats, emails and calls; write important decisions in one place so nobody has to remember who said what.</p>

<h2 id="privacy">How Should Logins Be Shared?</h2>
<p>Share passwords through a password manager or secure method, not plain WhatsApp messages, and give the developer their own accounts rather than yours.</p>

<h2 id="ours">How We Report</h2>
<p>Our projects, from {P['starter']}, include a staging link, weekly plain-language updates and milestone reviews. See our <a href="/digital/contact">contact page</a>.</p>
""",
    faqs=[
        ('How do I manage a web developer if I am not technical?',
         "Judge progress by what you can see: a staging link, weekly plain-language reports saying what is done, next and blocked, regular short demos, a shared task list, and milestones tied to visible results and payments. Insist that all accounts are in your business's name."),
        ("How can I check my developer's progress?",
         "Ask for a staging or preview link you can open on your phone, and look for visible changes each week. Combine this with a short written report and a brief demo call. If weeks pass with nothing new on staging, ask direct questions straight away."),
        ('What should a weekly developer report include?',
         "Three things in plain words: what was completed and where you can see it, what will be worked on next, and anything blocked, including what the developer needs from you. It should also say whether the next milestone date is still realistic."),
        ('What is a staging site?',
         "A staging site is a private copy of your website in progress, where you can see real pages, click buttons and test forms before launch. It should be password-protected and hidden from search engines, and it is the best way for non-technical owners to track progress."),
        ('What are the warning signs of a bad developer?',
         "No preview link or one that rarely changes, jargon-heavy reports that never say what is finished, repeated missed dates, requests for money before milestones are delivered, reluctance to put accounts in your name, and long silences followed by a rush near deadlines."),
        ('Should I pay my developer upfront?',
         "Usually a deposit, then payments tied to milestones you can see and test, such as approved designs, pages built on staging, working features and launch. Paying everything upfront removes your leverage; paying nothing upfront makes it hard for developers to commit time."),
        ('Developer se kaam kaise lein agar mujhe technical samajh nahin?',
         "Code samajhna zaroori nahin. Developer se staging link lein jo aap phone par dekh sakein, har hafte saada report lein ke kya hua, aage kya hai aur kahan rukawat hai. Payment sirf nazar aane wale kaam par dein, aur domain, hosting aur code ke accounts apne naam par rakhein."),
    ],
    sources=[('Google Search Central — Block search indexing with noindex', 'https://developers.google.com/search/docs/crawling-indexing/block-indexing'), ('OWASP — Authentication Cheat Sheet', 'https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html'), ('W3C WAI — Easy checks: a first review of web accessibility', 'https://www.w3.org/WAI/test-evaluate/preliminary/')],
    method="The routine, questions and warning signs are editorial, based on common project management practice. Our deposit and milestone terms are approved business facts. Our prices come from the published list.",
    related=['website-project-delays-why', 'taking-over-website-from-old-developer', 'website-discovery-meeting-what-to-expect'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/contact', 'Get a written quote')],
    cta='Not sure how your project is going?',
    wa='Hi%2C%20I%20read%20your%20guide%20on%20managing%20a%20developer',
)
