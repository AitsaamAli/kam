import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=274,
    slug="website-support-in-urdu",
    title="Website Support in Urdu and Punjabi: Talk in Your Language",
    h1="Website Support in Urdu: Meetings, Training and Written Scopes in the Language You Prefer",
    crumb="Website Support in Urdu",
    description="Website support in Urdu from our Lahore team: which languages we use, how scopes are written in English and Urdu, and admin training in plain Urdu.",
    keyword="website support urdu",
    cluster=["urdu speaking web developer", "web designer urdu support", "punjabi speaking developer lahore",
             "website training in urdu", "bilingual project scope"],
    category="Working With Us",
    published="2026-11-04", published_h="4 November 2026",
    updated="2026-11-04", updated_h="4 November 2026",
    answer=("Yes, we offer website support in Urdu. Meetings, WhatsApp messages and admin training can be in Urdu, Punjabi or English, whichever you prefer. "
            "Written quotes and scopes are prepared in English, with an Urdu summary of the 5 or 6 most important points on request, so nothing is lost in translation."),
    takeaways=[
        "You can speak with us in Urdu, Punjabi or English, in meetings and on WhatsApp.",
        "Admin training for your staff can be given in plain Urdu.",
        "Quotes and scopes are written in English, with an Urdu summary of key points on request.",
        "Technical terms are explained in simple words instead of being left as jargon.",
        "For other regional languages, we say honestly whether a translator is needed.",
    ],
    body=f"""
<h2 id="languages">Which Languages Do We Use for Website Support in Urdu and Other Languages?</h2>
<p>Many business owners are more comfortable discussing their business in Urdu or Punjabi than in English, especially when the topic is technical. Our team in Lahore works in Urdu, Punjabi and English, and you can switch between them freely in the same conversation. If you need another regional language, such as Pashto or Sindhi, tell us at the start and we will say honestly whether we can handle it directly or would involve a translator.</p>

<h2 id="where">Where Can You Use Urdu With Us?</h2>
<table>
<tr><th>Part of the project</th><th>Urdu available?</th><th>Note</th></tr>
<tr><td>First meeting and calls</td><td>Yes</td><td>Urdu, Punjabi or English, as you prefer</td></tr>
<tr><td>WhatsApp messages and voice notes</td><td>Yes</td><td>Urdu script, Roman Urdu or English all work</td></tr>
<tr><td>Written quote and scope</td><td>English, with an Urdu summary</td><td>The English version is the reference document</td></tr>
<tr><td>Admin panel training</td><td>Yes</td><td>Recorded on request so staff can watch again</td></tr>
<tr><td>Website content</td><td>Urdu, English or both</td><td>Urdu pages built with right-to-left layout</td></tr>
</table>

<h2 id="scope">Why Is the Scope Written in English With an Urdu Summary?</h2>
<p>A scope lists exactly what the project includes: pages, features, timeline and payment stages. Technical terms, plugin names and platform settings are clearest in English, and the document may be shared with other developers later. To make sure nothing is misunderstood, we add a short Urdu summary of the most important points on request: what you are getting, what you need to provide, the price and the timeline. If anything in either version is unclear, ask before signing.</p>

<h2 id="training">How Does Training in Urdu Work?</h2>
<p>When your website or store is ready, we show you or your staff how to update it: adding a product, changing a price, posting an article or reading form enquiries. Training can be in Urdu, at our office or on a video call, and we can record it so staff can watch again. We explain each step in simple words, and write short notes for the tasks you will do most often.</p>

<h2 id="jargon">How Do We Avoid Technical Jargon?</h2>
<ul>
<li>Domain is explained as your website's address, and hosting as the place its files live.</li>
<li>Every option is described by what it does for your business, not by its technical name.</li>
<li>Prices are explained in terms of what is included and what costs extra later.</li>
<li>If we use an English term, we explain it once in Urdu and use it consistently.</li>
</ul>
<p>Our Roman Urdu guides, such as <a href="/digital/blog/website-kaise-banwayein">website kaise banwayein</a> and <a href="/digital/blog/domain-kya-hota-hai">domain kya hota hai</a>, are written in the same plain style.</p>

<h2 id="urdu-site">Do You Also Build Urdu Websites?</h2>
<p>Yes. Talking to us in Urdu and having an Urdu website are separate choices. We build Urdu and bilingual pages with right-to-left layout, readable fonts and language tags for search engines. Our guide on <a href="/digital/blog/urdu-english-bilingual-website">Urdu and English bilingual websites</a> explains the options, and our guide on <a href="/digital/blog/website-urdu-translation-charges">website translation to Urdu</a> covers the cost.</p>

<h2 id="voice">Voice Notes and Written Follow-Up</h2>
<p>Many clients prefer sending a voice note in Urdu instead of typing. That is welcome. For any change that affects the price, timeline or content, we reply with a short written summary, so there is a clear record of what was agreed. This avoids the common problem of two people remembering a voice conversation differently weeks later. Written summaries can be in Urdu or English, whichever you prefer to keep on record.</p>

<h2 id="with-us">Working With Us in Urdu</h2>
<p>Message us on WhatsApp at 0328-4675162 in Urdu, Roman Urdu or English, during our office hours: Monday to Saturday, 9:00 AM to 6:00 PM, Friday until 12:30 PM, closed on Sunday. Our <a href="/digital/business-websites">business website packages</a> start from {P['starter']}.</p>
""",
    faqs=[
        ("Can I discuss my website project in Urdu?",
         "Yes. Meetings, calls and WhatsApp messages can be in Urdu, Punjabi or English, whichever you prefer, and you can switch between them freely. Many of our clients find it easier to explain their business in Urdu, and we explain technical points in plain words."),
        ("Is the quote available in Urdu?",
         "Quotes and scopes are written in English, because technical terms and platform names are clearest that way and the document may be shared with other developers. On request, we add a short Urdu summary of the key points: what you get, what you provide, the price and the timeline."),
        ("Can my staff be trained in Urdu?",
         "Yes. Admin training can be given in Urdu at our office or on a video call, and recorded on request so staff can watch it again. We cover the tasks they will do most often, such as adding products, changing prices or reading form enquiries, with short written notes."),
        ("Can I send voice notes instead of typing?",
         "Yes, voice notes in Urdu or Punjabi are welcome on WhatsApp. For any change that affects the price, timeline or content, we reply with a short written summary of what was agreed, so both sides have a clear record to refer back to later."),
        ("Do you support languages other than Urdu and Punjabi?",
         "Our team works in Urdu, Punjabi and English. If you need another regional language, such as Pashto or Sindhi, for meetings or website content, tell us at the start and we will say honestly whether we can handle it directly or would involve a translator."),
        ("Does Kamboh Associates Digital build Urdu-language websites?",
         f"Yes. We build Urdu and bilingual pages with correct right-to-left layout, readable fonts and language tags for search engines, as part of our business website packages from {P['starter']}. Translation, if needed, is quoted separately after we see your pages."),
    ],
    sources=[
        ("W3C: Structural markup and right-to-left text in HTML", "https://www.w3.org/International/questions/qa-html-dir"),
        ("Google Search Central: Managing multi-regional and multilingual sites", "https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites"),
        ("Google Fonts: Noto Nastaliq Urdu", "https://fonts.google.com/noto/specimen/Noto+Nastaliq+Urdu"),
    ],
    method="This guide describes how we work with clients in Urdu, Punjabi and English, consistent with the languages stated on our contact page. Technical references for Urdu pages come from W3C and Google's official guidance. Our own price comes from our published packages. Checked on 4 November 2026.",
    related=["urdu-english-bilingual-website", "website-urdu-translation-charges", "website-kaise-banwayein", "online-meeting-or-office-visit"],
    service_links=[("/digital/business-websites", "Business website packages"), ("/digital/contact", "Contact us")],
    cta="Prefer to talk about your website in Urdu?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20website%20support%20in%20Urdu.%20Mujhe%20website%20ke%20baare%20mein%20baat%20karni%20hai.",
)
