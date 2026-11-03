import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=236,
    slug="add-urdu-to-english-website",
    title="Add Urdu to Your Website Without Breaking It",
    h1="Add Urdu to Your Website: Plugins or Separate Pages, Right-to-Left Layout and Hreflang",
    crumb="Add Urdu to Website",
    description="How to add Urdu to a website that is already in English: plugin or separate pages, right-to-left layout, Nastaliq fonts, hreflang tags and translation quality.",
    keyword="add urdu to website",
    cluster=["translate website to urdu", "urdu version of website", "multilingual wordpress urdu",
             "urdu rtl layout", "hreflang urdu english"],
    category="Planning & Launch",
    published="2026-11-03", published_h="3 November 2026",
    updated="2026-11-03", updated_h="3 November 2026",
    answer=(f"To add Urdu to a website already in English, decide which pages need Urdu, choose a multilingual plugin or separate Urdu pages, set the layout to right-to-left with a readable Nastaliq or Naskh font, add hreflang tags, and have a person, not a machine alone, check every translation. "
            f"Most small sites need 5 to 10 Urdu pages."),
    takeaways=[
        "Translate the pages that bring enquiries first: home, main services, prices and contact.",
        "Plugins such as WPML or Polylang manage language versions on WordPress; custom sites use separate URLs.",
        "Urdu needs right-to-left layout and a font that renders well on phones; test on real Android devices.",
        "Add hreflang tags so Google shows the right language version in search results.",
        "Machine translation is a starting point; a fluent person must review tone, terms and numbers.",
    ],
    body=f"""
<h2 id="why">Why Add Urdu to Your Website?</h2>
<p>Many Pakistani customers are more comfortable reading Urdu than English, especially older buyers, people outside the big cities and customers of trades, clinics, schools and home services. An English-only website can lose these visitors at the first paragraph. Adding Urdu shows respect for them and can improve enquiries from searches written in Urdu script. For a business that already has an English site, the question is how to add Urdu without breaking what works.</p>
<p>If you are planning a bilingual site from scratch rather than adding to an existing one, our guide to <a href="/digital/blog/urdu-english-bilingual-website">Urdu and English bilingual websites</a> covers the full design approach.</p>

<h2 id="which-pages">Which Pages Should You Translate First?</h2>
<p>You do not need to translate everything at once. Start with the pages that lead to enquiries: the homepage, your main service or product pages, prices, the about page and contact. Policy pages such as delivery and refunds matter for stores. Blog posts can follow later, based on which topics Urdu-speaking visitors read. A site with five to ten well-translated Urdu pages is more useful than a full machine-translated copy nobody has checked.</p>

<h2 id="approach">Plugin or Separate Pages?</h2>
<table>
<tr><th>Approach</th><th>How it works</th><th>Best for</th></tr>
<tr><td>Multilingual plugin on WordPress (WPML, Polylang)</td><td>Each page has linked English and Urdu versions, with a language switcher</td><td>WordPress sites with several pages to translate</td></tr>
<tr><td>Separate Urdu section (for example /ur/)</td><td>Urdu pages built as their own pages with their own URLs</td><td>Custom sites and sites translating only a few pages</td></tr>
<tr><td>Automatic translation widgets</td><td>A script translates pages in the browser</td><td>Not recommended; quality is poor and Google may not see the Urdu text</td></tr>
</table>
<p>Whichever you choose, each language version should have its own URL so Google can index it, and a visible language switcher on every page.</p>

<h2 id="rtl">How Do You Handle Right-to-Left Layout and Fonts?</h2>
<p>Urdu is written right to left. The Urdu pages should set the language and direction in the page code, so the browser aligns text, menus and forms correctly. The W3C explains how to declare language and direction in HTML. Check that icons, arrows and form fields flip sensibly. Choose a font designed for Urdu, such as Noto Nastaliq Urdu or a clear Naskh font, and test on mid-range Android phones, since Nastaliq can render small or cramped. Increase line height for Urdu text so it is comfortable to read.</p>

<h2 id="hreflang">What Are Hreflang Tags and Why Do They Matter?</h2>
<p>Hreflang tags tell Google that an English page and an Urdu page are versions of each other, so it can show the right one to each searcher. Each language version lists itself and the other. Multilingual plugins usually add these tags automatically; on custom sites, a developer adds them. Google's documentation on localized versions explains the format. Without hreflang, Google may treat the pages as duplicates or show the wrong language.</p>

<h2 id="translation">Getting Translation Quality Right</h2>
<p>Machine translation can produce a first draft, but it often gets business terms, tone and numbers wrong, and it reads stiffly. Have a fluent person review every page. Decide how to handle technical words: many Pakistani readers expect English words like "website", "online" or "delivery" even in Urdu text. Keep prices, phone numbers and addresses identical in both versions, and update both when anything changes. Our guide to <a href="/digital/blog/website-copywriting-cost-pakistan">website copywriting costs in Pakistan</a> explains how writing and translation work is usually priced.</p>

<h2 id="cost">What Does Adding Urdu Cost?</h2>
<p>The cost depends on the number of pages, the platform and whether translation is included. Adding a multilingual plugin and RTL styling to an existing WordPress site is a moderate job; adding an Urdu section to a custom site takes a little longer. Ongoing updates to both languages can be covered by maintenance from {P['maint']} a month. See our <a href="/digital/business-websites">business website packages</a> or ask us to review your current site.</p>
""",
    faqs=[
        ("How do I add Urdu to an English website?",
         "Choose the pages to translate first, then use a multilingual plugin such as WPML or Polylang on WordPress, or build separate Urdu pages with their own URLs on a custom site. Set right-to-left direction, use an Urdu font, add hreflang tags and have a fluent person review every translation."),
        ("Which pages should be translated into Urdu first?",
         "Start with the pages that bring enquiries: the homepage, main service or product pages, prices, about page and contact. Stores should add delivery and refund policies. Translate blog posts later, based on what Urdu-speaking visitors actually read on the site."),
        ("Is Google Translate good enough for an Urdu website?",
         "Not on its own. Machine translation is useful for a first draft but often gets business terms, tone and numbers wrong, and browser translation widgets may not be visible to Google. Have a fluent person review and correct every page before publishing it."),
        ("What is hreflang and do I need it for Urdu pages?",
         "Hreflang tags tell Google that an English page and an Urdu page are versions of each other, so each searcher sees the right one. Each version lists itself and the other. Multilingual plugins usually add them automatically; custom sites need a developer to add them."),
        ("Which font should I use for Urdu on a website?",
         "Use a font designed for Urdu, such as Noto Nastaliq Urdu or a clear Naskh font, loaded properly on the site. Test on mid-range Android phones, increase line height for comfortable reading, and check that headings and buttons do not get cut off in right-to-left layout."),
        ("How much does it cost to add Urdu to an existing website?",
         f"It depends on the number of pages, the platform and whether translation is included. Adding a plugin and right-to-left styling to a WordPress site is a moderate job, while a custom site takes a little longer. Keeping both languages updated can be part of maintenance from {P['maint']} a month."),
        ("Angrezi website mein Urdu kaise shamil karein?",
         "Pehle woh pages chunein jin se enquiries aati hain, jaise home, services, qeematein aur contact. WordPress par WPML ya Polylang jaisa plugin, ya custom site par alag Urdu pages banayein. Right-to-left layout, Urdu font aur hreflang tags lagayein, aur har tarjuma kisi Urdu jaanne wale se check karwayein."),
    ],
    sources=[
        ("W3C: Structural markup and right-to-left text in HTML", "https://www.w3.org/International/questions/qa-html-dir"),
        ("W3C: Declaring language in HTML", "https://www.w3.org/International/questions/qa-html-language-declarations"),
        ("Google Search Central: Tell Google about localized versions of your page", "https://developers.google.com/search/docs/specialty/international/localized-versions"),
        ("Google Fonts: Noto Nastaliq Urdu", "https://fonts.google.com/noto/specimen/Noto+Nastaliq+Urdu"),
        ("WPML: Multilingual WordPress", "https://wpml.org/"),
        ("WordPress.org: Polylang plugin", "https://wordpress.org/plugins/polylang/"),
    ],
    method="We followed W3C guidance on right-to-left text and language declarations, Google's documentation on localized versions, and the multilingual plugins commonly used on WordPress, then described the steps for an existing site. Prices come from our published packages. Sources checked on 3 November 2026.",
    related=["urdu-english-bilingual-website", "website-copywriting-cost-pakistan", "pages-for-small-business-website", "website-accessibility-basics"],
    service_links=[("/digital/business-websites", "Business website packages"), ("/digital/contact", "Get a written quote")],
    cta="Want your English website to speak to Urdu readers too?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20adding%20Urdu%20to%20a%20website.%20I%20would%20like%20a%20quote.",
)
