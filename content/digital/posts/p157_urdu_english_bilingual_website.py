import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=157,
    slug='urdu-english-bilingual-website',
    title='Bilingual Website in Urdu and English: Cost, Setup, SEO',
    h1='Bilingual Website in Urdu and English: Cost, Right-to-Left Setup, Fonts and SEO',
    crumb='Urdu and English Website',
    description='A bilingual website in Urdu and English: right-to-left layout, Nastaliq vs Naskh fonts and page speed, hreflang for search, translation quality and cost.',
    keyword='bilingual website urdu english',
    cluster=['urdu website design', 'urdu font website', 'hreflang urdu'],
    category='Content and Conversion',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="A bilingual website in Urdu and English needs a right-to-left layout for Urdu pages, a carefully chosen Urdu font, separate URLs for each language with hreflang tags, and properly written Urdu text. Nastaliq fonts look traditional but are heavier; Naskh is lighter. Expect bilingual work to add 2 language versions of every page to the scope.",
    takeaways=["Urdu pages must use a right-to-left layout, not just Urdu text in an English layout.", "Nastaliq looks natural to most Urdu readers but web fonts can be large; test speed on phones.", "Each language needs its own URL and hreflang tags so search engines show the right version.", "Machine translation is a draft at best; have a fluent writer check every Urdu page.", "Many businesses need full Urdu only on key pages, with English elsewhere."],
    body=f"""
<h2 id="who">Who Needs a Bilingual Website in Urdu and English?</h2>
<p>Most Pakistani business websites are in English, yet many customers are more comfortable reading Urdu, especially outside major cities and in sectors such as health, education, agriculture, government services and religious organisations. A bilingual website in Urdu and English serves both groups. It is also more work than translating a few headings, because Urdu reads right to left, uses a different script and has its own font challenges on the web.</p>
<p>This guide belongs to our content series led by the <a href="/digital/blog/homepage-content-guide">homepage content guide</a>. For Arabic sites, see our Arabic RTL guide, which covers similar technical ground.</p>

<h2 id="options">Full Urdu, Partial Urdu or Roman Urdu?</h2>
<table>
<tr><th>Approach</th><th>Suits</th><th>Effort</th></tr>
<tr><td>Full bilingual site</td><td>Audiences split between Urdu and English readers</td><td>Every page in both languages</td></tr>
<tr><td>Key pages in Urdu</td><td>Mostly English audience with an Urdu-reading segment</td><td>Homepage, main services, contact, FAQs in Urdu</td></tr>
<tr><td>English with Roman Urdu touches</td><td>Urban audiences who chat in Roman Urdu</td><td>A few phrases, FAQs, WhatsApp messages</td></tr>
</table>
<p>Roman Urdu is not a substitute for Urdu script for readers who prefer Urdu, but it is how many people type on WhatsApp and search. Choose based on who your customers are, not on what looks impressive.</p>

<h2 id="rtl">What Does Right-to-Left Layout Involve?</h2>
<p>Urdu pages need the HTML direction set to right-to-left, so text, menus, columns and alignment flip. The W3C's internationalisation guidance explains setting the direction on the page and handling mixed text, such as English brand names or numbers inside Urdu sentences. Icons with direction, such as arrows, must also flip, while logos and phone numbers should not. Forms need right-aligned labels and correct input direction. Test every page type in Urdu, not only the homepage.</p>

<h2 id="fonts">Nastaliq or Naskh: Which Urdu Font?</h2>
<p>Nastaliq is the traditional script style most Urdu readers expect in newspapers and books, and many find Naskh-style Urdu text unfamiliar. Nastaliq web fonts, however, are complex and can be large files, which slows pages on mobile data, and their tall letterforms need extra line height. Naskh-style fonts are lighter and simpler to set but look less natural to many readers. Practical steps: use a well-supported Nastaliq web font with only the weights you need, load it efficiently, increase line height, and test on mid-range Android phones over mobile data before deciding.</p>

<h2 id="seo">How Should Search Be Set Up?</h2>
<p>Give each language its own URL, for example /en/services and /ur/services, rather than switching language on the same address. Google's documentation on localized versions explains using hreflang annotations so search engines know the pages are equivalents and can show the right one; the language code for Urdu is "ur". Each version should be fully translated, with its own title and description. Search behaviour also differs: some customers search in Urdu script, many in Roman Urdu, so check Search Console to see which terms bring visitors.</p>

<h2 id="translation">How Do You Get Good Urdu Content?</h2>
<p>Machine translation gives a rough draft but often produces stiff or wrong Urdu, especially for technical or legal terms. Ask a fluent writer to adapt the content, not translate word for word, and to keep terms consistent. Decide which English terms stay in English, such as "website" or "AC", because that is how customers actually talk. Have someone from your target audience read it before launch.</p>

<h2 id="cost">What Does a Bilingual Site Cost?</h2>
<p>Bilingual work adds design for right-to-left layouts, font set-up, a language switcher, separate URLs and content entry in two languages. We scope it on top of our base packages: starter websites from {P['starter']} and business websites from {P['business']}. Translation or writing is quoted separately unless you supply the Urdu text. Our <a href="/digital/blog/website-copywriting-cost-pakistan">content writing guide</a> covers who writes it.</p>

<h2 id="privacy">Are There Privacy Considerations?</h2>
<p>Your privacy policy and form notices should exist in both languages, so Urdu readers understand what they are agreeing to when they submit details.</p>

<h2 id="build">Building in Two Languages</h2>
<p>See <a href="/digital/business-websites">business websites</a> for our bilingual builds.</p>
""",
    faqs=[
        ('How do I make a bilingual website in Urdu and English?',
         "Use a right-to-left layout for Urdu pages, choose and test an Urdu web font, give each language its own URLs with hreflang tags, add a language switcher that keeps visitors on the same page, and have a fluent writer prepare the Urdu content rather than relying on machine translation."),
        ('Which Urdu font is best for websites, Nastaliq or Naskh?',
         "Nastaliq looks natural to most Urdu readers but its web fonts can be large and need extra line height. Naskh-style fonts are lighter and simpler but look less familiar to many readers. Test a Nastaliq font on mid-range phones over mobile data before deciding."),
        ('What is hreflang and do I need it for an Urdu site?',
         "Hreflang annotations tell search engines that pages in different languages are equivalents, so the right version appears for each searcher. Google's documentation on localized versions explains the set-up. Urdu uses the language code ur, and each version should have its own URL."),
        ('Can I use Google Translate for my Urdu website?',
         "Machine translation can give a rough draft, but it often produces stiff or incorrect Urdu, especially for technical, legal or medical terms. Ask a fluent writer to adapt the content, keep terms consistent and have someone from your target audience read it before launch."),
        ('Do I need my whole website in Urdu?',
         "Not always. Many businesses translate only key pages, such as the homepage, main services, contact and FAQs. A full bilingual site suits audiences genuinely split between Urdu and English readers. Choose based on who your customers are and how they search."),
        ('How much does an Urdu and English website cost?',
         f"Bilingual work is scoped on top of our base packages, with starter websites from {P['starter']} and business websites from {P['business']}. It adds right-to-left design, font set-up, separate URLs and content entry in two languages. Translation is quoted separately unless you supply the text."),
        ('Website Urdu aur English dono mein kaise banayein?',
         "Urdu pages ka layout daayen se baayen hona chahiye, sirf Urdu text daal dena kaafi nahin. Achha Urdu font chunein aur mobile par speed check karein. Har zaban ka alag link ho aur hreflang tag lagayen. Machine translation ke bajaye kisi achhi Urdu likhne wale se mawaad tayyar karwayen."),
    ],
    sources=[('W3C — Structural markup and right-to-left text in HTML', 'https://www.w3.org/International/questions/qa-html-dir'), ('Google Search Central — Localized versions of your pages', 'https://developers.google.com/search/docs/specialty/international/localized-versions'), ('Google Fonts — Noto Nastaliq Urdu', 'https://fonts.google.com/noto/specimen/Noto+Nastaliq+Urdu'), ('web.dev — Best practices for fonts', 'https://web.dev/articles/font-best-practices')],
    method="Right-to-left and hreflang guidance reflect W3C and Google Search Central documentation. Font advice on Nastaliq and Naskh is editorial, based on common experience with Urdu web fonts; no file sizes are quoted because they vary by font and subset. Our prices come from the published list.",
    related=['homepage-content-guide', 'website-copywriting-cost-pakistan', 'about-us-page-that-builds-trust'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/business-websites', 'Business website service')],
    cta='Need your site in Urdu too?',
    wa='Hi%2C%20I%20read%20your%20Urdu%20English%20website%20guide',
)
