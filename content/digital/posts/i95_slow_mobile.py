import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=95,
    slug="website-slow-on-mobile",
    title="Website Slow on Mobile? Causes and Fixes That Work",
    h1="Website Slow on Mobile? How to Find the Cause and Fix It, Step by Step",
    crumb="Website Slow on Mobile",
    description="Website slow on mobile? Find the cause with a few quick tests, then fix it: images, hosting, plugins, fonts and scripts, with a before-and-after example.",
    keyword="website slow on mobile",
    cluster=["website slow kyun hai", "slow website fix", "website loading slow", "speed up wordpress site",
             "heavy images slow website", "too many plugins slow"],
    category="Fix a Problem",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=("If your website is slow on mobile, run PageSpeed Insights on the mobile setting and test on a real Android phone over mobile "
            "data. The usual causes, in order, are oversized images, weak hosting without caching, too many plugins or scripts, and heavy "
            "fonts. Aim for main content within 2.5 seconds; fixing images alone often halves page weight."),
    takeaways=[
        "Diagnose before changing anything: PageSpeed Insights plus a real phone test over mobile data.",
        "Oversized images are the most common cause and the cheapest to fix.",
        "Slow server response points to hosting, caching or database problems rather than design.",
        "Every plugin, widget and tracking script adds weight; remove what you do not use.",
        "Fix one thing at a time and retest, so you know what worked.",
    ],
    body=f"""
<h2 id="diagnose">Why Is My Website Slow on Mobile?</h2>
<p>A site that feels fine on a laptop can crawl on a phone. Phones have slower processors, mobile data has more delay than fibre, and pages built for big screens often send phones far more than they need. Before fixing anything, find out where the time goes. Our <a href="/digital/blog/website-speed-pakistan-mobile">website speed strategy guide</a> explains Core Web Vitals; this guide is the practical troubleshooting list.</p>
<ol>
<li>Run <strong>PageSpeed Insights</strong> on the mobile setting for your home page and one key inner page.</li>
<li>Note the Largest Contentful Paint time and the top suggestions, such as "properly size images" or "reduce unused JavaScript".</li>
<li>Check the <strong>server response time</strong> warning; if it is flagged, hosting is part of the problem.</li>
<li>Open the page on a mid-range Android phone using mobile data, with the cache cleared, and time it.</li>
</ol>

<h2 id="causes-fixes">Which Causes Are Most Common, and How Do You Fix Them?</h2>
<table>
<tr><th>Cause</th><th>How to spot it</th><th>Fix</th></tr>
<tr><td>Oversized images</td><td>"Properly size images" or "serve images in modern formats" warnings; photos several MB each</td><td>Resize to display size, compress, use WebP or AVIF, lazy-load images below the first screen</td></tr>
<tr><td>Slow hosting or no caching</td><td>Slow server response warning; slow even on simple pages</td><td>Turn on page caching, use a CDN, upgrade or move hosting</td></tr>
<tr><td>Too many plugins</td><td>Dozens of plugins, many loading scripts on every page</td><td>Remove unused ones; replace several small plugins with one good one</td></tr>
<tr><td>Third-party scripts</td><td>"Reduce the impact of third-party code"; chat widgets, pixels, embeds</td><td>Remove unused tags; load chat widgets only after interaction</td></tr>
<tr><td>Heavy theme or page builder</td><td>Large CSS and JavaScript files on every page</td><td>Switch to a lighter theme, or rebuild key templates</td></tr>
<tr><td>Web fonts</td><td>Several font families and weights; text appears late</td><td>Use one or two families and only needed weights</td></tr>
<tr><td>Sliders and autoplay video</td><td>Large media above the fold</td><td>Replace with one optimised image and a clear button</td></tr>
</table>

<h2 id="example">What Can the Results Look Like? A Before-and-After Example</h2>
<p>Illustrative example, not a real client. A restaurant home page built with a page builder had a full-width slider of five phone photos, a chat widget, three tracking scripts and four font weights.</p>
<table>
<tr><th>Measure</th><th>Before</th><th>After</th></tr>
<tr><td>Home page weight</td><td>About 6 MB</td><td>About 1.2 MB</td></tr>
<tr><td>Images</td><td>Five photos straight from a phone</td><td>One compressed WebP hero image, menu photos lazy-loaded</td></tr>
<tr><td>Scripts</td><td>Chat widget and three trackers on load</td><td>Chat on tap only; one analytics tag</td></tr>
<tr><td>Largest Contentful Paint on mobile</td><td>Around 7 seconds</td><td>Under 2.5 seconds</td></tr>
</table>
<p>Your numbers will differ, but the pattern is typical: images and scripts made up most of the weight.</p>

<h2 id="wordpress">What Are the Quick Wins on WordPress?</h2>
<ul>
<li>Install one reputable image optimisation tool and compress existing images.</li>
<li>Turn on page caching, through your host or a single caching plugin.</li>
<li>Deactivate and delete plugins you do not use, then test.</li>
<li>Check that the PHP version is current; WordPress.org recommends PHP 8.3 or newer.</li>
<li>Avoid stacking several "speed" plugins that do the same job; they can conflict.</li>
</ul>
<p>Take a backup first, and change one thing at a time.</p>

<h2 id="when-to-rebuild">When Is a Rebuild Better Than Fixing?</h2>
<p>If the theme or page builder itself is the main weight, and key pages cannot pass Core Web Vitals after images, hosting and plugins are fixed, rebuilding the main templates on a lighter base is often cheaper than endless tuning. Our <a href="/digital/blog/new-website-without-losing-google-traffic">guide to redesigning without losing traffic</a> covers doing that safely.</p>

<h2 id="what-we-offer">How We Fix Slow Mobile Websites</h2>
<p>We run a speed diagnosis on your key pages, fix images, caching, plugins and scripts, and retest on a mid-range Android phone over 4G. Ongoing speed checks are part of maintenance at {P['maint']} a month; rebuilds start from {P['starter']} for small sites. See our <a href="/digital/business-websites">business websites</a> service and the <a href="/digital/blog/get-business-website-on-google">guide to getting found on Google</a>.</p>
""",
    faqs=[
        ("Why is my website slow on mobile but fine on desktop?",
         "Phones have slower processors and mobile data has more delay than office broadband, so heavy pages hurt more. Many sites also send phones large desktop images, sliders and scripts. Test with PageSpeed Insights on the mobile setting and on a real phone over mobile data to see what is slowing it."),
        ("Do too many plugins slow down WordPress?",
         "They can. Each plugin may add scripts, styles or database queries to every page, and poorly built plugins add more. Delete plugins you do not use, replace several small ones with one well-built plugin where possible, and retest after each change to see the effect."),
        ("How do I make images load faster on my website?",
         "Resize images to the size they are displayed, compress them, use modern formats such as WebP or AVIF, and lazy-load images below the first screen. Photos taken on phones are often several megabytes each and should never be uploaded directly without resizing."),
        ("Will better hosting make my website faster?",
         "If the server response is slow, yes. PageSpeed Insights flags slow server response times. Turning on caching, adding a CDN, or moving to a better plan or host near your visitors can help significantly. If the problem is large images or scripts, hosting alone will not fix it."),
        ("How fast should my website load on mobile?",
         "Google's Core Web Vitals treat a Largest Contentful Paint of 2.5 seconds or less as good, measured across real page loads. In practice, aim for the main content to appear within about two and a half seconds on a mid-range phone over mobile data."),
        ("Website slow kyun hai aur kaise theek karein?",
         "Aam tor par wajah bari tasveerein, kamzor hosting, zyada plugins aur chat ya tracking scripts hoti hain. Pehle PageSpeed Insights aur apne phone par mobile data se test karein. Tasveerein compress karein, caching lagayen, faltu plugins aur scripts hatayen aur har tabdeeli ke baad dobara test karein."),
    ],
    sources=[
        ("PageSpeed Insights", "https://pagespeed.web.dev/"),
        ("web.dev — Largest Contentful Paint", "https://web.dev/articles/lcp"),
        ("Chrome for Developers — Lighthouse overview", "https://developer.chrome.com/docs/lighthouse/overview"),
        ("WordPress.org — Server requirements", "https://wordpress.org/about/requirements/"),
        ("Cloudflare — Network and CDN, including a free plan", "https://www.cloudflare.com/"),
    ],
    method=("Testing tools and the LCP threshold follow PageSpeed Insights, Lighthouse and web.dev, and the PHP recommendation follows "
            "WordPress.org, checked 29 October 2026. The cause table reflects what we most often find. The restaurant before-and-after "
            "example is illustrative, not a real client. Prices are our own packages."),
    related=["get-business-website-on-google", "website-speed-pakistan-mobile", "best-hosting-for-pakistan-websites",
             "website-down-check"],
    service_links=[("/digital/business-websites", "Fast, lightweight websites"), ("/digital/pricing", "Maintenance and speed fixes")],
    cta="Is your website slow on phones?",
    wa="Hi%2C%20I%20read%20your%20slow%20on%20mobile%20guide%20and%20need%20a%20speed%20fix",
)
