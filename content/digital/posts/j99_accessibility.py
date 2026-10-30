import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=99,
    slug="website-accessibility-basics",
    title="Website Accessibility Basics (WCAG) for Business Owners",
    h1="Website Accessibility Basics for Business Owners: A 10-Point WCAG Checklist in Plain English",
    crumb="Website Accessibility Basics",
    description="Website accessibility basics for business owners: what WCAG is, a 10-point checklist in plain English, why it helps customers and search, and Ontario rules.",
    keyword="website accessibility basics",
    cluster=["wcag checklist", "accessible website design", "ada website compliance", "wcag 2.2 aa",
             "alt text and contrast", "screen reader friendly website"],
    category="Planning & Launch",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=("Website accessibility basics mean making your site usable by people with disabilities, following the W3C's Web Content "
            "Accessibility Guidelines (WCAG). Start with 10 checks: alt text, headings, contrast, keyboard use, visible focus, labelled "
            "forms, clear links, captions, readable text sizes and no content that relies on colour alone."),
    takeaways=[
        "WCAG, from the W3C, is the common reference for web accessibility, with levels A, AA and AAA.",
        "Its four principles are that content must be perceivable, operable, understandable and robust.",
        "Ten basic checks catch many common problems and also make sites clearer for everyone.",
        "Accessible sites often work better for search engines, because structure and text alternatives are clearer.",
        "Some laws require it: Ontario sets WCAG 2.0 Level AA for public sector bodies and firms employing 50 or more people.",
    ],
    body=f"""
<h2 id="what-is">What Are Website Accessibility Basics?</h2>
<p>Web accessibility means people with disabilities can perceive, understand, navigate and interact with your website. That includes people who are blind and use screen readers, people with low vision who zoom in, people who cannot use a mouse, people with hearing loss and people with cognitive or learning differences. Many older customers benefit too, as do people on small screens or in bright sunlight.</p>
<p>The W3C, the body that sets web standards, publishes the Web Content Accessibility Guidelines, known as WCAG. The current version is WCAG 2.2. It is organised around four principles, that content must be perceivable, operable, understandable and robust, with success criteria at three levels: A, AA and AAA. Most organisations aim for Level AA.</p>

<h2 id="checklist">What Is the 10-Point Basic Checklist?</h2>
<table>
<tr><th>#</th><th>Check</th><th>What it means in practice</th></tr>
<tr><td>1</td><td>Text alternatives</td><td>Meaningful images have short alt text; decorative images are marked as decorative</td></tr>
<tr><td>2</td><td>Headings in order</td><td>One main heading, then logical subheadings, so screen reader users can skim</td></tr>
<tr><td>3</td><td>Colour contrast</td><td>Text stands out clearly from its background, including on buttons</td></tr>
<tr><td>4</td><td>Not colour alone</td><td>Errors and required fields are shown with text or icons, not only red colour</td></tr>
<tr><td>5</td><td>Keyboard use</td><td>Every menu, button and form works with the Tab and Enter keys</td></tr>
<tr><td>6</td><td>Visible focus</td><td>You can see which element is selected when using the keyboard</td></tr>
<tr><td>7</td><td>Labelled forms</td><td>Each field has a visible label and clear error messages</td></tr>
<tr><td>8</td><td>Descriptive links</td><td>Link text says where it goes, not "click here"</td></tr>
<tr><td>9</td><td>Captions and transcripts</td><td>Videos have captions; audio has a transcript</td></tr>
<tr><td>10</td><td>Resizable text</td><td>Text can be enlarged without breaking the layout or hiding content</td></tr>
</table>
<p>These basics do not make a site fully compliant with WCAG AA, which has many more criteria, but they fix many of the most common barriers.</p>

<h2 id="why-it-helps">Why Does Accessibility Help Customers and Search?</h2>
<p>Accessibility is first about people: customers who cannot use your site cannot buy from you. It also improves usability for everyone, a point the W3C makes in its introduction to accessibility. Several accessible practices help search engines too. Clear headings show page structure, alt text describes images, descriptive links explain where they go, and text content is easier to read than text inside images. Lighthouse, Google's free audit tool, includes an accessibility score alongside performance and SEO.</p>

<h2 id="legal-notes">Is Website Accessibility a Legal Requirement?</h2>
<p>It depends on where you operate and your size. One clear example: the Government of Ontario states that, under the Accessibility for Ontarians with Disabilities Act, designated public sector organisations and businesses or non-profits with 50 or more employees must make public websites meet WCAG 2.0 Level AA, a requirement in force since 1 January 2021. Other countries and regions, including the UK, the US and the EU, have their own laws and guidance, and how they apply to private businesses varies. If you serve customers in those markets, take local legal advice. Our <a href="/digital/blog/small-business-website-canada-offshore">Canadian small business guide</a> covers Ontario in more detail.</p>

<h2 id="testing">How Do You Test Accessibility?</h2>
<ol>
<li>Run Lighthouse in Chrome and review the accessibility findings.</li>
<li>Put the mouse away and use only the keyboard to complete key tasks, such as sending an enquiry.</li>
<li>Zoom the page to 200% and check nothing is cut off.</li>
<li>Try a free screen reader on your phone or computer on the home and contact pages.</li>
<li>Ask someone who uses assistive technology for feedback if you can.</li>
</ol>
<p>Automated tools find only some problems; manual checks matter.</p>

<h2 id="what-we-build">How We Build Accessibility Into Every Site</h2>
<p>We build with these ten basics as standard, test key pages with Lighthouse and keyboard checks, and can test against WCAG AA where clients need it, for example in Ontario. Accessible builds cost the same as any of our sites, from {P['starter']}. See our <a href="/digital/business-websites">business websites</a> service, the <a href="/digital/blog/website-launch-checklist">website launch checklist</a> and the <a href="/digital/blog/get-business-website-on-google">guide to getting found on Google</a>.</p>
""",
    faqs=[
        ("What is WCAG?",
         "WCAG stands for Web Content Accessibility Guidelines, published by the W3C. They set out how to make web content accessible to people with disabilities, organised around four principles, perceivable, operable, understandable and robust, with success criteria at Levels A, AA and AAA. WCAG 2.2 is the current version."),
        ("Which WCAG level should a business website aim for?",
         "Most organisations aim for Level AA, which covers the most important barriers without the very strict requirements of Level AAA. Some laws name a specific version and level; for example, Ontario requires WCAG 2.0 Level AA for covered organisations. Check what applies in your market."),
        ("Does website accessibility help SEO?",
         "Several accessible practices also help search engines understand your pages: clear heading structure, descriptive alt text, meaningful link text and real text instead of text inside images. The main reason to do it is your customers, but better structure benefits search visibility too."),
        ("Is website accessibility required by law?",
         "It depends on your location and size. In Ontario, designated public sector organisations and businesses or non-profits with 50 or more employees must make public websites meet WCAG 2.0 Level AA. Other countries have their own laws and guidance, so take local legal advice for your markets."),
        ("How can I check my website's accessibility quickly?",
         "Run Lighthouse in Chrome for an automated report, then try using the site with only a keyboard, zoom to 200% and test the home and contact pages with a free screen reader. Automated tools catch only some problems, so these manual checks are essential."),
        ("What is alt text and why does it matter?",
         "Alt text is a short written description of an image that screen readers read aloud and that appears if the image fails to load. Meaningful images need it so blind users understand the content; decorative images should be marked so screen readers skip them. Search engines also use alt text."),
    ],
    sources=[
        ("W3C — Web Content Accessibility Guidelines (WCAG) 2.2", "https://www.w3.org/TR/WCAG22/"),
        ("W3C — WCAG overview", "https://www.w3.org/WAI/standards-guidelines/wcag/"),
        ("W3C — Introduction to web accessibility", "https://www.w3.org/WAI/fundamentals/accessibility-intro/"),
        ("Government of Ontario — How to make websites accessible", "https://www.ontario.ca/page/how-make-websites-accessible"),
        ("Chrome for Developers — Lighthouse overview", "https://developer.chrome.com/docs/lighthouse/overview"),
    ],
    method=("WCAG version, principles and levels come from the W3C's WCAG 2.2 and overview pages, and the Ontario requirement from the "
            "Government of Ontario, checked 29 October 2026. The 10-point list is our plain-English selection of common checks, not the "
            "full standard. We state no UK, US or EU legal rules and advise local advice."),
    related=["get-business-website-on-google", "website-launch-checklist", "seo-ready-website-checklist",
             "small-business-website-canada-offshore"],
    service_links=[("/digital/business-websites", "Accessible business websites"), ("/digital/contact", "Get an accessibility check")],
    cta="Want a website everyone can use?",
    wa="Hi%2C%20I%20read%20your%20website%20accessibility%20guide%20and%20need%20a%20check",
)
