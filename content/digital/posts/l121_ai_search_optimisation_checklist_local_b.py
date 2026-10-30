import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=121,
    slug='ai-search-optimisation-checklist-local-business',
    title='AI Search Optimisation Checklist for Local Businesses',
    h1='A 20-Point AI Search Optimisation Checklist for Local Businesses',
    crumb='AI Search Checklist',
    description='A 20-point AI search optimisation checklist for local firms: consistent details, reviews, citations, structured data, llms.txt status and how to measure results.',
    keyword='ai search optimisation checklist',
    cluster=['geo checklist', 'get recommended by chatgpt', 'local business ai search'],
    category='AI and Automation',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="An AI search optimisation checklist for a local business covers 20 basics: identical name, address and phone everywhere; a complete Google Business Profile; genuine reviews; clear service and price pages; structured data matching the page; mentions on trusted local sites; and measurement. Nobody can guarantee an AI tool will recommend you.",
    takeaways=["AI tools draw on the same public information as search engines, so accuracy and consistency come first.", "Your name, address, phone and hours must match on your site, Google, directories and social pages.", "Specific facts such as prices, areas served and opening hours are easier for AI to quote correctly.", "llms.txt is a proposal, not a standard; adding one is optional and no major engine promises to use it.", "There is no way to guarantee a recommendation from ChatGPT, Gemini or Google AI Mode."],
    body=f"""
<h2 id="why">Why Use an AI Search Optimisation Checklist?</h2>
<p>People now ask ChatGPT, Gemini, Copilot and Google's AI Mode questions like "which tailor in Model Town does alterations on the same day" or "a reliable plumber near DHA Phase 5". These tools build answers from information they can find and trust: your website, your Google listing, reviews, directories and mentions elsewhere. An AI search optimisation checklist turns that into concrete tasks a small business can actually finish. Our background guide on AI search visibility explains the theory; this page is the practical list.</p>
<p>A word of honesty first. No agency, tool or file can make an AI system recommend your business. The list below improves the odds that what AI says about you is accurate and that you are a reasonable candidate to mention.</p>

<h2 id="checklist">What Is on the 20-Point Checklist?</h2>
<table>
<tr><th>#</th><th>Check</th><th>Area</th></tr>
<tr><td>1</td><td>Business name written the same way everywhere</td><td>Entity</td></tr>
<tr><td>2</td><td>Address in one consistent format, including area and city</td><td>Entity</td></tr>
<tr><td>3</td><td>One main phone and WhatsApp number used everywhere</td><td>Entity</td></tr>
<tr><td>4</td><td>Opening hours identical on site, Google and social pages, including Friday and Ramadan changes</td><td>Entity</td></tr>
<tr><td>5</td><td>Google Business Profile complete: category, services, photos, service areas</td><td>Listings</td></tr>
<tr><td>6</td><td>Listed on two or three trusted directories relevant to your trade</td><td>Citations</td></tr>
<tr><td>7</td><td>Genuine reviews requested after every completed job</td><td>Reviews</td></tr>
<tr><td>8</td><td>Every review answered politely, including complaints</td><td>Reviews</td></tr>
<tr><td>9</td><td>An About page with founding year, owners and what you do</td><td>Website</td></tr>
<tr><td>10</td><td>One page per main service, with what is included</td><td>Website</td></tr>
<tr><td>11</td><td>Prices or price ranges published where possible</td><td>Website</td></tr>
<tr><td>12</td><td>Areas served named on the page in plain text</td><td>Website</td></tr>
<tr><td>13</td><td>Short, direct answers to common questions near the top of pages</td><td>Website</td></tr>
<tr><td>14</td><td>Real photos of your premises, team and work</td><td>Website</td></tr>
<tr><td>15</td><td>LocalBusiness structured data matching visible details</td><td>Technical</td></tr>
<tr><td>16</td><td>Pages indexed and allowed to show snippets</td><td>Technical</td></tr>
<tr><td>17</td><td>Fast, readable mobile pages</td><td>Technical</td></tr>
<tr><td>18</td><td>Mentions in local news, associations or supplier pages where genuine</td><td>Citations</td></tr>
<tr><td>19</td><td>Optional llms.txt file summarising your key pages</td><td>Optional</td></tr>
<tr><td>20</td><td>Monthly check of what AI tools say about you, with corrections at the source</td><td>Measurement</td></tr>
</table>

<h2 id="entity">Why Does Consistency Matter So Much?</h2>
<p>AI systems combine information from many places. If your website says "Rehman Electric Works", Google says "Rehman Electrics" and a directory still shows your old phone number, the systems may treat these as different businesses or repeat the wrong details. Fix the sources, starting with your own site and your Google Business Profile, then work through directories one by one.</p>

<h2 id="structured">Does Structured Data Help?</h2>
<p>Structured data describes your business in a format machines read easily: name, address, phone, hours, services. Google says it must match what visitors can see on the page, and it does not by itself guarantee any special display. Our schema markup guide lists the fields that matter for local firms.</p>

<h2 id="llms-txt">What Is llms.txt, and Should You Add One?</h2>
<p>llms.txt is a proposed convention, first published by Jeremy Howard in September 2024, for a plain markdown file at the root of a site that gives AI agents a short overview and links to key pages. The proposal's own site describes it as a proposal open for community input, and at the time of writing it is not a ratified standard. Google says no special file is needed to appear in its AI features. Adding one is harmless and cheap; just do not expect it to change results on its own.</p>

<h2 id="measure">How Do You Check What AI Says About You?</h2>
<p>Once a month, ask two or three AI tools the questions a customer would ask, such as "who repairs inverters in Iqbal Town" or "what does [your business] charge for [service]". Note whether you appear and whether the details are right. If something is wrong, correct it at the source the tool is likely using: your site, your listing or a directory. Track enquiries in parallel, because a mention is only useful if it brings customers.</p>

<h2 id="privacy">What Privacy Points Should You Keep in Mind?</h2>
<p>Everything you publish for AI visibility is public and can be repeated anywhere. Do not publish staff personal phone numbers, home addresses or customer names in case studies without written permission. When replying to reviews, never confirm a customer's order details, health issue or address in public. If you test AI tools with questions about your business, avoid pasting private customer data into them. See our <a href="/digital/blog/website-data-privacy-when-using-ai">AI and privacy guide</a> for more.</p>

<h2 id="help">Where We Fit In</h2>
<p>Our websites, from {P['starter']}, include service pages, matching structured data, consistent contact details and tracking for calls and WhatsApp. We can also review an existing site against this list. See <a href="/digital/business-websites">business websites</a>.</p>
<p>See also <a href="/digital/blog/ai-chatbot-for-business-website-cost-pakistan">AI Chatbot for a Business Website in Pakistan</a>.</p>
""",
    faqs=[
        ('What is an AI search optimisation checklist?',
         "It is a list of practical tasks that make your business information accurate, consistent and easy for AI tools to find: matching contact details everywhere, a complete Google Business Profile, genuine reviews, clear service and price pages, structured data and regular checks of what AI tools say."),
        ('Can I pay to be recommended by ChatGPT?',
         "There is no official way to buy a recommendation in ChatGPT's normal answers, and no agency can guarantee one. What you can do is make your public information accurate and specific, collect genuine reviews and earn real mentions, which improves the odds of being described correctly."),
        ('Is llms.txt required for AI search?',
         "No. llms.txt is a proposal first published in September 2024, not a ratified standard, and Google says no special file is needed for its AI features. You can add one as a short overview of your key pages, but do not expect it to change results alone."),
        ('How often should I check what AI tools say about my business?',
         "Once a month is enough for most small businesses. Ask two or three tools the questions customers ask, note whether you appear and whether the details are correct, and fix wrong information at its source, such as your website, Google listing or a directory."),
        ('Do reviews affect AI search answers?',
         "Reviews are part of the public information AI tools and search engines can see, so they may shape how a business is described. Ask every satisfied customer for an honest review, never buy or write fake ones, and reply politely to all reviews, including complaints."),
        ('Which matters more for local AI search, my website or Google Business Profile?',
         "Both matter, and they must agree. The Google Business Profile drives map and local results, while the website holds the detail: services, prices, areas served and answers. Start by making their names, addresses, phone numbers and hours identical, then improve each."),
        ('ChatGPT ya Google AI mein apna business kaise layein?',
         "Koi bhi guarantee nahin de sakta. Behtar hai ke har jagah naam, pata, phone aur auqaat aik jaise hon, Google Business Profile mukammal ho, asli reviews hon, aur website par services, qeemat aur ilaqe saaf likhe hon. Har mahine check karein ke AI aap ke baare mein kya keh raha hai."),
    ],
    sources=[('llms.txt — The /llms.txt file proposal', 'https://llmstxt.org/'), ('Google Search Central — AI features and your website', 'https://developers.google.com/search/docs/appearance/ai-features'), ('Google Search Central — Local business structured data', 'https://developers.google.com/search/docs/appearance/structured-data/local-business'), ('Google Business Profile Help', 'https://support.google.com/business/'), ('Google Search Central — Using generative AI content', 'https://developers.google.com/search/docs/fundamentals/using-gen-ai-content')],
    method="The llms.txt status comes from llmstxt.org, checked 30 October 2026 (version 2, last modified 10 August 2026). Google statements come from Search Central pages checked the same day. The 20 checks are our editorial list; we make no claim that following them leads to AI recommendations. Our prices come from the published list.",
    related=['ai-chatbot-for-business-website-cost-pakistan', 'google-ai-mode-small-business-website', 'whatsapp-business-api-cost-pakistan'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/business-websites', 'Business website service')],
    cta='Want your details right in AI answers?',
    wa='Hi%2C%20I%20read%20your%20AI%20search%20checklist',
)
