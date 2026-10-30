import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=198,
    slug='website-roi-small-business',
    title='Website ROI: Is Your Website Paying for Itself?',
    h1='Website ROI for a Small Business: A Simple Check of Whether Your Website Pays for Itself',
    crumb='Website ROI',
    description='Website ROI made simple: leads times close rate times order value, an illustrative worked example, what to track in GA4, and counting WhatsApp and calls.',
    keyword='website roi',
    cluster=['website return on investment', 'measure website success', 'website leads value'],
    category='Planning & Launch',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="Website ROI compares what the website earns with what it costs. A simple check: enquiries from the website, multiplied by the share that become customers, multiplied by average order value or profit, compared with the yearly cost of the site. Track calls, WhatsApp clicks and forms, not just visits, for at least 3 months.",
    takeaways=["Visits alone say little; count enquiries, sales and their value.", "WhatsApp clicks and calls are leads too, and need tracking.", "Ask every new customer how they found you, to fill tracking gaps.", "Use profit, not revenue, when judging whether the site pays for itself.", "Measure over months, because a single week is too noisy."],
    body=f"""
<h2 id="question">How Do You Work Out Website ROI?</h2>
<p>Many business owners pay for a website and never know whether it was worth it. Visitor numbers go up and down, but nobody connects them to sales. Website ROI, return on investment, simply compares what the website brings in with what it costs. For a small business, a rough but honest calculation is far more useful than none, and it shows where to improve.</p>
<p>This guide belongs to our planning series, which opens with getting your website found on Google.</p>

<h2 id="formula">What Is the Simple Formula?</h2>
<p>Website value per month = enquiries from the website × share that become customers × average profit per customer.</p>
<p>Website ROI = (value over a year − yearly website cost) ÷ yearly website cost.</p>
<p>Use profit rather than revenue where you can, because a sale of Rs 10,000 that costs Rs 8,000 to deliver brings in only Rs 2,000.</p>

<h2 id="example">What Does a Worked Example Look Like?</h2>
<table>
<tr><th>Item</th><th>Illustrative figure</th></tr>
<tr><td>Website enquiries per month (forms, WhatsApp, calls)</td><td>30</td></tr>
<tr><td>Share that become customers</td><td>20%, so 6 customers</td></tr>
<tr><td>Average profit per customer</td><td>Rs 6,000</td></tr>
<tr><td>Monthly value from the website</td><td>6 × Rs 6,000 = Rs 36,000</td></tr>
<tr><td>Yearly value</td><td>Rs 432,000</td></tr>
<tr><td>Yearly website cost (build spread over 3 years, hosting, care)</td><td>Your own figure</td></tr>
</table>
<p>Every number here is invented to show the method; your figures will differ. If yearly value comfortably exceeds yearly cost, the site pays for itself. If not, look at which factor is weakest: too few enquiries, too few become customers, or profit per customer is low.</p>

<h2 id="track">What Should You Track?</h2>
<ul>
<li><strong>Form submissions,</strong> counted in your analytics and inbox.</li>
<li><strong>WhatsApp clicks,</strong> tracked as events on the button; our WhatsApp button guide explains how.</li>
<li><strong>Phone taps</strong> on mobile.</li>
<li><strong>Online orders and revenue,</strong> through GA4 ecommerce events.</li>
<li><strong>Source of each new customer,</strong> by asking "how did you find us?"</li>
</ul>
<p>Google Analytics 4 can record these actions as key events, and our <a href="/digital/blog/ga4-ecommerce-tracking-setup">GA4 tracking guide</a> covers online stores. Asking customers directly fills gaps that tracking misses, such as people who saw the site and then visited your shop.</p>

<h2 id="improve">How Do You Improve Each Factor?</h2>
<p><strong>More enquiries:</strong> better search visibility, clearer calls to action, faster pages. <strong>Higher conversion:</strong> faster replies, clearer prices, stronger reviews. <strong>Higher value:</strong> packages, upsells, repeat customers. Our guide to visitors who do not enquire covers the most common leaks.</p>

<h2 id="limits">What Are the Limits of This Check?</h2>
<p>Websites also build trust for customers who never click a tracked button: someone checks your site after a referral, then calls from a printed card. These contributions are real but hard to count. Treat the formula as a floor, not the whole story, and combine it with what customers tell you.</p>

<h2 id="timeframe">How Long Should You Measure?</h2>
<p>At least three months, and ideally compare the same season year on year, because many Pakistani businesses are seasonal. One busy or quiet week tells you little.</p>

<h2 id="costs">Which Costs Belong in the Calculation?</h2>
<p>Spread the build cost over the years you expect to use the site, often three, then add yearly hosting, domain, email, maintenance and any paid tools. If you advertise, judge ads separately, because ad spend can make a good website look unprofitable or a weak one look busy. Our <a href="/digital/blog/website-budget-planner-first-year">first-year budget planner</a> lists each line.</p>

<h2 id="review">How Often Should You Review the Numbers?</h2>
<p>A quarterly review is enough for most small businesses: update the table, compare with the same quarter last year, and choose one improvement to try next.</p>

<h2 id="privacy">What Privacy Rules Apply to Tracking?</h2>
<p>Track actions, not identities: never send names or phone numbers to analytics tools. Mention analytics in your privacy policy and handle cookie consent for overseas visitors.</p>

<h2 id="help">How We Help</h2>
<p>Our websites, from {P['starter']}, include tracking for forms, WhatsApp and calls, so you can run this check from the first month. See our <a href="/digital/contact">contact page</a>.</p>
""",
    faqs=[
        ('How do I calculate website ROI?',
         "Multiply monthly enquiries from the website by the share that become customers and by average profit per customer to get monthly value. Then compare a year's value with the yearly cost of the website. Use profit rather than revenue for an honest picture."),
        ('What should I track to measure website success?',
         "Form submissions, WhatsApp button clicks, phone taps on mobile, online orders and revenue, and the source of each new customer. Visits alone say little about value. Google Analytics 4 can record these actions as key events, and asking customers fills the remaining gaps."),
        ('How do I track WhatsApp enquiries from my website?',
         "Set up a click event on the WhatsApp button in your analytics, and use a pre-filled message that mentions the page or offer, so you can see which pages bring chats. Ask new customers how they found you to confirm what the tracking shows."),
        ('How long should I measure before judging my website?',
         "At least three months, and ideally compare the same season year on year, because many businesses in Pakistan are seasonal. A single week is too noisy to judge, and short periods can make a good website look poor or a weak one look good."),
        ('What if my website ROI looks low?',
         "Find the weakest factor. Too few enquiries suggests visibility, speed or calls to action. Low conversion suggests slow replies, unclear prices or weak reviews. Low value suggests pricing, packages or repeat business. Improve one factor at a time and measure again."),
        ('Does a website have value beyond tracked enquiries?',
         "Yes. People often check a website after a referral or before visiting a shop, then call or walk in without clicking anything tracked. That trust-building value is real but hard to measure, so treat the simple ROI formula as a minimum estimate."),
        ('Website ka faida kaise naapein?',
         "Har mahine website se aane wali enquiries ginein, jaise form, WhatsApp aur call. Phir dekhein unmein se kitne customer bane aur har customer se kitna munafa hua. Saal bhar ka faida website ke salana kharch se milayen. Kam az kam teen mahine tak hisaab rakhein."),
    ],
    sources=[('Google Analytics Help — Measure ecommerce', 'https://support.google.com/analytics/answer/12200568'), ('Google Ads Help — About conversion tracking', 'https://support.google.com/google-ads/answer/1722022'), ('Google Analytics Help — Best practices to avoid sending PII', 'https://support.google.com/analytics/answer/6366371')],
    method="The formula is standard ROI arithmetic; the worked example uses invented figures and is labelled illustrative, as the plan requires. Tracking references come from Google Analytics and Google Ads help pages checked 30 October 2026. Our prices come from the published list.",
    related=['ga4-ecommerce-tracking-setup', 'when-to-upgrade-your-website', 'website-budget-planner-first-year'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/contact', 'Get a written quote')],
    cta='Not sure your website is paying off?',
    wa='Hi%2C%20I%20read%20your%20website%20ROI%20guide',
)
