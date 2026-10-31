import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=20,
    slug="web-developer-portfolio-red-flags",
    title="Web Developer Portfolio Red Flags: How to Check Work",
    h1="Web Developer Portfolio Red Flags: How to Check a Developer's Past Work",
    crumb="Portfolio Red Flags",
    description="How to check a web developer portfolio in 15 minutes: eight red flags, free tools to verify who built a site, and the questions that expose borrowed work.",
    keyword="check web developer portfolio",
    cluster=["web developer portfolio red flags", "verify web designer work", "fake website portfolio",
             "how to check developer past work", "web design portfolio review"],
    category="Hiring a Developer",
    published="2026-10-28", published_h="28 October 2026",
    updated="2026-10-28", updated_h="28 October 2026",
    answer=("To check a web developer portfolio, open at least three live sites on your phone, test their speed and forms, confirm the "
            "developer's credit or ask the client, and look at when each site was built. Red flags include screenshots instead of live "
            "links, sites that no longer work, identical templates and no client willing to speak."),
    takeaways=[
        "Live links beat screenshots; anyone can screenshot a site they did not build.",
        "Test portfolio sites on your phone, because that is how your customers will see yours.",
        "Ask what the developer did on each site; \"we worked on it\" can mean a single fix.",
        "Free tools can show a site's speed, its platform and how it looked in the past.",
        "One reference call with a past client is worth more than ten portfolio images.",
    ],
    body="""
<h2 id="why">Why You Need to Check a Web Developer Portfolio</h2>
<p>A portfolio is the main evidence you have before hiring. It can also be misleading: some portfolios include sites the developer only fixed, templates bought from marketplaces, or work done by a previous employer. Checking takes about 15 minutes per developer and can save you from the most expensive mistake in a website project: hiring the wrong team.</p>

<h2 id="red-flags">Which Portfolio Red Flags Should Worry You?</h2>
<table>
<tr><th>Red flag</th><th>Why it matters</th></tr>
<tr><td>Only screenshots or mock-ups, no live links</td><td>Cannot be verified, and may not be their work</td></tr>
<tr><td>Live links that are broken or expired</td><td>Sites may have been abandoned, or clients moved away</td></tr>
<tr><td>Every site looks the same</td><td>One template reused, limited design skill</td></tr>
<tr><td>Sites are very slow or broken on a phone</td><td>Your site will likely have the same problems</td></tr>
<tr><td>No recent work from the last two years</td><td>Skills and tools may be outdated</td></tr>
<tr><td>Famous brands with no detail</td><td>Often a small task presented as the whole site</td></tr>
<tr><td>No client willing to speak to you</td><td>Past clients may not be satisfied</td></tr>
<tr><td>Contact forms that do not work</td><td>Testing is not part of their process</td></tr>
</table>

<h2 id="fifteen-minutes">The 15-Minute Portfolio Check</h2>
<ol>
<li><strong>Pick three live sites</strong> closest to your project type.</li>
<li><strong>Open each on your phone</strong> using mobile data, not Wi-Fi. Does it load quickly? Can you read it without zooming?</li>
<li><strong>Run Google PageSpeed Insights</strong> on each homepage and note the mobile results.</li>
<li><strong>Test a contact form or WhatsApp button</strong> on at least one site.</li>
<li><strong>Look at the footer</strong> for a developer credit, and check whether the business still uses the site.</li>
<li><strong>Check the Wayback Machine</strong> to see when the current design first appeared and whether it matches the developer's timeline.</li>
</ol>

<h2 id="questions">Questions That Expose Borrowed Work</h2>
<ul>
<li>What exactly did you do on this site: design, development, content or only fixes?</li>
<li>Who on your current team worked on it?</li>
<li>What was the hardest part of this project, and how did you solve it?</li>
<li>Can I speak to this client for five minutes?</li>
<li>What results did the site produce for the client?</li>
</ul>
<p>Developers who built a site can answer these in detail without hesitation. Vague answers deserve a follow-up question.</p>

<h2 id="tools">Which Free Tools Help You Check Past Work?</h2>
<table>
<tr><th>Tool</th><th>What it shows</th></tr>
<tr><td>Google PageSpeed Insights</td><td>Speed and user-experience scores on mobile and desktop</td></tr>
<tr><td>Wayback Machine</td><td>How a site looked on earlier dates</td></tr>
<tr><td>ICANN Lookup</td><td>When a domain was registered, for generic domains</td></tr>
<tr><td>Lighthouse in Chrome</td><td>Performance, accessibility and SEO basics</td></tr>
</table>

<h2 id="new-developers">What If the Developer Is New?</h2>
<p>New developers and young agencies may have only a few projects. That is not a red flag on its own. Ask for their best two pieces of work, a short paid test task, or a smaller first milestone so you can judge quality before committing the full budget. Combine this with our <a href="/digital/blog/how-to-choose-web-development-company">20 questions</a> and the advice in <a href="/digital/blog/freelancer-vs-agency-vs-software-house">freelancer vs agency vs software house</a>.</p>

<h2 id="our-work">Checking Our Work</h2>
<p>We share live sites we have built, explain what we did on each, and can put you in touch with past clients on request. You are welcome to run every check on this page against our work before paying anything.</p>
<p>Ask to see live sites we built when you <a href="/digital/contact">request a quote</a>.</p>
""",
    faqs=[
        ("How do I check if a web developer actually built a website?",
         "Ask what they did on that site and who on their team worked on it, look for a developer credit in the footer, check the Wayback Machine to see when the design appeared, and ask to speak to the client. A developer who built the site will answer in detail and usually connect you with the client."),
        ("What are red flags in a web developer portfolio?",
         "Warning signs include screenshots instead of live links, broken or expired sites, every design looking the same, slow or broken mobile pages, no recent work, famous brand names without detail, forms that do not work and no past client willing to speak. Two or more of these deserve serious caution."),
        ("How many portfolio sites should I check?",
         "Check at least three live sites, ideally similar to your project, such as an online store if you need one. Test each on your phone using mobile data, run Google PageSpeed Insights on the homepage and try a contact form or WhatsApp button. This takes about fifteen minutes per developer."),
        ("Is it a red flag if a developer has no portfolio?",
         "Not necessarily, if they are new. Ask for their best one or two projects, consider a short paid test task, or start with a smaller first milestone so you can judge their work before committing the full budget. Be more careful if an experienced firm claims many years but cannot show live work."),
        ("Developer ka portfolio kaise check karein?",
         "Kam az kam teen live websites apne mobile par kholein aur dekhein ke jaldi load hoti hain ya nahi. Contact form ya WhatsApp button try karein. Developer se poochein ke us site par unhon ne khud kya kaam kiya, aur kisi purane client se baat karwane ka kahein. Sirf screenshots par bharosa na karein."),
        ("Can a developer use templates in their portfolio?",
         "Using a good theme or template is normal and can keep costs down. The concern is when a developer presents a template demo as original work, or every site is the same template with little change. Ask which sites used a theme, what they customised, and whether licences were bought in the client's name."),
    ],
    sources=[
        ("Google PageSpeed Insights", "https://pagespeed.web.dev/"),
        ("Chrome for Developers — Lighthouse overview", "https://developer.chrome.com/docs/lighthouse/overview"),
        ("Internet Archive — Wayback Machine", "https://web.archive.org/"),
        ("ICANN Lookup", "https://lookup.icann.org/"),
        ("Nielsen Norman Group — Usability 101", "https://www.nngroup.com/articles/usability-101-introduction-to-usability/"),
    ],
    method=("The red flags come from portfolios clients have shown us after problem projects with other developers. The 15-minute check "
            "uses free, public tools from Google, Chrome, the Internet Archive and ICANN, each linked in the sources. We have not named "
            "any company, because a portfolio problem can have innocent explanations."),
    related=["how-to-choose-web-development-company", "best-web-development-company-lahore", "freelancer-vs-agency-vs-software-house",
             "why-website-quotes-vary"],
    service_links=[("/digital/business-websites", "See our business website service"), ("/digital/contact", "Ask to see our live work")],
    cta="Want to check our past work?",
    wa="Hi%2C%20I%20read%20your%20portfolio%20guide%20and%20want%20to%20see%20your%20live%20work",
)
