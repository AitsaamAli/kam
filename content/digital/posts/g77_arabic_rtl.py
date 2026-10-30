import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=77,
    slug="arabic-rtl-website-development",
    title="Arabic Website Development: RTL Done Right for Gulf Firms",
    h1="Arabic Website Development for Gulf Businesses: Right-to-Left Layout, Fonts and SEO Done Right",
    crumb="Arabic RTL Websites",
    description="Arabic website development for Gulf businesses: a right-to-left checklist, W3C direction guidance, hreflang for bilingual sites, Arabic fonts and proper translation.",
    keyword="arabic website development",
    cluster=["rtl website design", "bilingual arabic english website", "arabic website cost", "hreflang arabic english",
             "arabic web fonts", "right to left layout"],
    category="Working With Overseas Clients",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=(f"Arabic website development means more than translating text: the layout must flip right to left, set with the HTML dir "
            f"attribute as W3C advises, use Arabic fonts that render well on phones, and link English and Arabic pages with hreflang. "
            f"A bilingual 10-page business website with us starts from {P['business']} plus translation."),
    takeaways=[
        "Arabic is written right to left, so menus, layouts, icons and forms must mirror, not just the text.",
        "W3C advises setting direction with the dir attribute in HTML rather than with CSS alone.",
        "Bilingual sites should give each language its own URLs and connect them with hreflang annotations.",
        "Choose Arabic web fonts designed for screens, and test them on real phones.",
        "Use a professional Arabic translator for customer-facing text; machine translation alone reads poorly to native speakers.",
    ],
    body=f"""
<h2 id="beyond-translation">What Does Arabic Website Development Involve?</h2>
<p>Businesses in the UAE, Saudi Arabia and the wider Gulf often need a website in both Arabic and English. Arabic website development is not just translating the English pages. Arabic reads right to left, which changes the layout of every page, the order of navigation, the direction of icons and how forms behave. Done badly, an Arabic site feels broken to native readers even if every word is correct.</p>

<h2 id="rtl-checklist">What Is on the Right-to-Left Checklist?</h2>
<table>
<tr><th>Element</th><th>What changes in Arabic</th></tr>
<tr><td>Page direction</td><td>Set dir="rtl" and lang="ar" on the HTML element for Arabic pages</td></tr>
<tr><td>Navigation</td><td>Menu starts on the right; logo usually moves to the right</td></tr>
<tr><td>Layout</td><td>Columns, sidebars and image-text blocks mirror</td></tr>
<tr><td>Icons</td><td>Directional icons such as arrows flip; logos and clocks do not</td></tr>
<tr><td>Forms</td><td>Labels and text align right; phone and email fields often stay left to right</td></tr>
<tr><td>Numbers</td><td>Decide between Western and Arabic-Indic digits and use them consistently</td></tr>
<tr><td>Mixed text</td><td>English brand names inside Arabic sentences must display in the right order</td></tr>
</table>
<p>The W3C, the body that sets web standards, advises declaring the overall direction with the dir attribute on the html element and notes that the lang attribute alone does not set direction. Our <a href="/digital/blog/school-website-design-pakistan">school website guide</a> applies the same rules to Urdu pages.</p>

<h2 id="hreflang">How Should a Bilingual Site Be Structured for Search?</h2>
<p>Google's guidance on multilingual sites recommends giving each language version its own URL, for example /en/ and /ar/, rather than switching language on the same address. Link each page to its equivalent in the other language with hreflang annotations, so Google can show Arabic searchers the Arabic page. Let visitors switch languages with a clear link, and do not redirect them automatically based on location alone.</p>

<h2 id="fonts">Which Fonts Work for Arabic Websites?</h2>
<p>Arabic letters join and change shape depending on their position in a word, so font quality matters. Choose web fonts designed for Arabic screen reading, with a matching style for English, and test them on iPhones and mid-range Android phones. Check line height, because Arabic often needs more vertical space than English. Load only the weights you use, to keep pages fast.</p>

<h2 id="translation">How Should Content Be Translated?</h2>
<p>Use a professional Arabic translator, ideally familiar with your market, for all customer-facing text. Machine translation is useful for drafts but often reads awkwardly to native speakers and can get tone wrong for a premium brand. Gulf audiences may also expect different examples and imagery. Plan time for review by a native speaker in your team before launch.</p>

<h2 id="content-management">How Will Your Team Update Both Languages?</h2>
<p>Decide early who updates each language and how. A good set-up shows editors which pages exist in English only, so Arabic does not fall behind after launch. For WordPress, a multilingual plugin links each page to its translation; for Shopify, translation tools handle products and theme text. Keep a simple rule: no English page goes live without its Arabic version, or a note on when it will follow.</p>

<h2 id="testing">How Do You Test an Arabic Website?</h2>
<ol>
<li>Check every page in Arabic on a phone and a laptop.</li>
<li>Fill in and submit every form, including error messages.</li>
<li>Check emails and notifications are also in Arabic.</li>
<li>Test mixed Arabic and English text, prices and phone numbers.</li>
<li>Verify hreflang links with Google Search Console after launch.</li>
</ol>

<h2 id="what-we-build">How We Build Arabic and Bilingual Websites</h2>
<p>We build bilingual Arabic and English websites with proper right-to-left layouts, separate URLs per language, hreflang set-up and tested Arabic fonts. A bilingual business website of up to 10 pages starts from {P['business']}, with translation quoted separately or supplied by you; online stores begin at {P['store']}. We work with Gulf clients over video calls, with about a full working day of overlap. See our <a href="/digital/business-websites">business websites</a> service, our <a href="/digital/blog/website-cost-dubai">Dubai website cost guide</a> and the <a href="/digital/blog/hire-pakistani-web-developers">guide to hiring Pakistani developers</a>.</p>
""",
    faqs=[
        ("What is an RTL website?",
         "An RTL, or right-to-left, website displays languages such as Arabic and Urdu that read from right to left. The whole layout mirrors: navigation starts on the right, columns swap sides and directional icons flip. The HTML dir attribute tells browsers to display the page right to left."),
        ("Is translating my English website into Arabic enough?",
         "No. Besides translation, the layout must flip right to left, directional icons must mirror, forms must align correctly, Arabic fonts must render well and each language needs its own URLs with hreflang links. Without these, an Arabic site feels broken to native readers even if the words are right."),
        ("How should a bilingual Arabic and English website be set up for Google?",
         "Give each language its own URLs, such as /en/ and /ar/, connect equivalent pages with hreflang annotations, and add a visible language switcher. Google's multilingual guidance advises against automatically redirecting visitors by location. Check the set-up in Google Search Console after launch."),
        ("How much does an Arabic website cost?",
         f"A bilingual Arabic and English business website of up to 10 pages starts from {P['business']} with us, with professional translation quoted separately or supplied by you. Online stores in both languages start from {P['store']}. Prices are invoiced in Pakistani rupees and paid in milestones."),
        ("Should I use machine translation for my Arabic website?",
         "Use it for drafts at most. Machine translation often reads awkwardly to native speakers and can get tone and terminology wrong, which hurts a brand. Use a professional Arabic translator for customer-facing pages and have a native speaker on your team review everything before launch."),
        ("Which numbers should an Arabic website use?",
         "Decide between Western digits and Arabic-Indic digits and use your choice consistently across prices, phone numbers and dates. Many Gulf businesses use Western digits on websites, but follow your brand and audience. Whatever you choose, test that mixed numbers and Arabic text display in the correct order."),
    ],
    sources=[
        ("W3C — Structural markup and right-to-left text in HTML", "https://www.w3.org/International/questions/qa-html-dir"),
        ("Google Search Central — Managing multi-regional and multilingual sites", "https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites"),
        ("Google Search Console Help — About Search Console", "https://support.google.com/webmasters/answer/9128668"),
        ("PageSpeed Insights", "https://pagespeed.web.dev/"),
        ("W3C — Introduction to web accessibility", "https://www.w3.org/WAI/fundamentals/accessibility-intro/"),
    ],
    method=("Right-to-left guidance comes from W3C, and bilingual URL and hreflang guidance from Google Search Central, checked 29 October "
            "2026. The RTL checklist and testing steps reflect how we build Arabic sites. Prices are our own published packages; "
            "translation is quoted separately."),
    related=["hire-pakistani-web-developers", "shopify-developer-uae-saudi", "offshore-team-time-zones-lahore", "website-cost-dubai"],
    service_links=[("/digital/business-websites", "Bilingual Arabic websites"), ("/digital/contact", "Get a quote")],
    cta="Need an Arabic and English website?",
    wa="Hi%2C%20I%20read%20your%20Arabic%20website%20guide%20and%20need%20a%20quote",
)
