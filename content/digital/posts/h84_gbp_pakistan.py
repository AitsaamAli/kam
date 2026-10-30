import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=84,
    slug="google-business-profile-pakistan",
    title="Google Business Profile Pakistan: Setup and Verification",
    h1="Google Business Profile in Pakistan: Setup, Verification and Fixing Common Local Problems",
    crumb="Google Business Profile",
    description="Google Business Profile in Pakistan: step-by-step setup and verification, writing local addresses correctly, phone numbers, reviews and common fixes.",
    keyword="google business profile pakistan",
    cluster=["google my business pakistan", "verify business on google maps", "google maps listing", "add business to google maps",
             "google maps par dukan kaise dalein", "business profile verification video"],
    category="Getting Found Online",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=("A Google Business Profile in Pakistan is free and controls how your shop, clinic or office appears on Google Maps and Search. "
            "Sign in, add or claim the business, verify it by the method Google offers, such as a phone code or video, then add hours, "
            "photos and your website. Google says review usually takes up to 5 business days."),
    takeaways=[
        "Business Profiles are for businesses that meet customers in person, at a location or in a service area, not online-only shops.",
        "Google chooses which verification methods you can use, such as phone or text, email, video or postcard.",
        "Write Pakistani addresses in one consistent format with block, sector or phase, and put the map pin on your entrance.",
        "Use a phone number that is answered during your listed hours.",
        "Keep yourself as owner and add staff or your developer as managers.",
    ],
    body=f"""
<h2 id="what-it-is">What Is a Google Business Profile in Pakistan?</h2>
<p>A Google Business Profile is the free listing that controls how your business appears on Google Maps and in Google Search: name, location, hours, phone, photos, reviews and a link to your website. For a Pakistani clinic, restaurant, shop, school or service company, it is often the first thing customers see, before the website.</p>
<p>Google's help pages say profiles are for storefront businesses and service-area businesses that meet customers in person. Online-only businesses are not eligible, and Google directs them to Google Ads instead.</p>

<h2 id="setup-steps">How Do You Set Up the Profile?</h2>
<ol>
<li><strong>Sign in</strong> with a Google account you control, ideally one for the business, not a staff member's personal account.</li>
<li><strong>Search for your business</strong> on Google Maps. If it already exists, claim it; if someone else has verified it, request ownership.</li>
<li><strong>Add the business</strong> if it does not exist: name, category, location or service area, phone and website.</li>
<li><strong>Verify</strong> using the method Google offers you.</li>
<li><strong>Complete the profile:</strong> hours, photos, services or menu, and a short description.</li>
</ol>

<h2 id="verification">How Does Verification Work?</h2>
<p>According to Google's help page, Google decides which verification options you get. They may include a phone call or text with a code, an email, a live video call during business hours, or a postcard with a code. Google recommends video verification where available. Review usually takes up to five business days, and Google will never ask you to share your verification code with anyone.</p>
<p>For video verification, be ready to show the street outside with your signboard, the entrance, the inside of the business, and proof that you manage it, such as unlocking the door or showing equipment, depending on Google's instructions at the time.</p>

<h2 id="pakistan-issues">Which Problems Are Common in Pakistan?</h2>
<table>
<tr><th>Problem</th><th>Fix</th></tr>
<tr><td>Address written several ways</td><td>Choose one format, such as "Shop 12, Block H, Johar Town, Lahore", and use it everywhere</td></tr>
<tr><td>Map pin in the wrong place</td><td>Drag the pin to your actual entrance, not the middle of the block</td></tr>
<tr><td>Duplicate listings created by others</td><td>Claim them or ask Google to merge or remove duplicates</td></tr>
<tr><td>Profile owned by a former employee or agency</td><td>Request ownership through Google; keep yourself as primary owner in future</td></tr>
<tr><td>Phone number not answered</td><td>List a number staffed during your hours; add WhatsApp details on the website</td></tr>
<tr><td>Hours wrong in Ramadan or holidays</td><td>Set special hours in advance</td></tr>
<tr><td>Keywords stuffed into the name</td><td>Use your real business name only; stuffing can get the profile suspended</td></tr>
</table>

<h2 id="owners-managers">Who Should Own the Profile?</h2>
<p>You, the business owner, should be the primary owner. Google lets owners add other owners and managers; managers can do most tasks but cannot remove users or delete the profile. Add staff or your developer as managers and remove them when they leave. Our guide on <a href="/digital/blog/who-owns-your-website">who owns your website</a> explains why this matters for every account.</p>

<h2 id="reviews">How Should You Handle Reviews?</h2>
<p>Ask every customer for an honest review with a direct link, and reply to all reviews politely. Google's review policy forbids offering rewards for reviews and asking only satisfied customers, and does not allow reviews from staff or family because of conflicts of interest. For clinics, never mention a patient's medical details in a reply. Our <a href="/digital/blog/clinic-website-lahore">Lahore clinics guide</a> shows this in practice.</p>

<h2 id="link-website">How Should the Profile Connect to Your Website?</h2>
<p>Link the profile to the most useful page, such as the booking or contact page, and make sure the name, address, phone and hours match the website exactly. Add the same details to your website's structured data. Our <a href="/digital/blog/schema-markup-business-websites">schema markup guide</a> explains how.</p>

<h2 id="what-we-build">How We Set Up Your Business Profile</h2>
<p>We set up or clean up Business Profiles with you as owner, alongside every website we build: a 5-page site starts from {P['starter']}, and Lahore businesses can meet our team in person. For existing businesses, profile set-up and fixes can be included in maintenance at {P['maint']} a month. See our <a href="/digital/web-development-lahore">Lahore team page</a> and the <a href="/digital/blog/get-business-website-on-google">guide to getting your website on Google</a>.</p>
""",
    faqs=[
        ("Is Google Business Profile free in Pakistan?",
         "Yes. Creating and managing a Google Business Profile is free. It controls how your business appears on Google Maps and Search. Google's help pages say profiles are for businesses that meet customers in person, at a location or in a service area; online-only businesses are not eligible."),
        ("How do I verify my business on Google Maps in Pakistan?",
         "After adding or claiming your business, choose from the verification options Google offers, which may include a phone or text code, email, a live video call or a postcard. Google recommends video where available. Review usually takes up to five business days, and you should never share your code."),
        ("How should I write my Pakistani address on Google?",
         "Choose one format and use it everywhere, for example shop or house number, street, block, sector or phase, area and city, with a nearby landmark in the description if helpful. Drag the map pin to your actual entrance. Consistent details help customers and Google trust your listing."),
        ("Someone else controls my Google listing. What can I do?",
         "Request ownership through Google Business Profile; Google contacts the current owner and may let you verify if they do not respond. In future, keep yourself as the primary owner and add staff, agencies or developers as managers, so you can remove them when they leave."),
        ("Can I offer a discount for Google reviews?",
         "No. Google's review policy does not allow reviews posted because of an incentive, such as discounts or free services, and forbids asking only happy customers. Ask every customer for an honest review, reply politely to all reviews, and do not let staff or family review your business."),
        ("Google Maps par apni dukan kaise dalein?",
         "Apne Google account se Google Business Profile kholen, dukan ka naam, category, pata aur phone number daalein, aur Google jo tareeqa de, jaise phone code ya video, us se verify karein. Map ka pin apne darwaze par rakhein, timings aur asli tasveerein lagayen, aur website ka link dein."),
    ],
    sources=[
        ("Google Business Profile Help — Create and manage your Business Profile", "https://support.google.com/business/answer/7039811"),
        ("Google Business Profile Help — Verify your business", "https://support.google.com/business/answer/7107242"),
        ("Google Business Profile Help — Add or remove owners and managers", "https://support.google.com/business/answer/3403100"),
        ("Google Maps — Prohibited and restricted content (review policy)", "https://support.google.com/contributionpolicy/answer/7400114"),
        ("Google Search Central — Local business structured data", "https://developers.google.com/search/docs/appearance/structured-data/local-business"),
    ],
    method=("Eligibility, setup, verification options and timing, and owner and manager roles come from Google Business Profile help pages; "
            "review rules from Google's contribution policy, all checked 29 October 2026. The Pakistan problems table reflects issues we fix "
            "for clients. Prices are our own published packages."),
    related=["get-business-website-on-google", "schema-markup-business-websites", "seo-ready-website-checklist", "clinic-website-lahore"],
    service_links=[("/digital/web-development-lahore", "Get help from our Lahore team"), ("/digital/business-websites", "Business websites")],
    cta="Need your Google Business Profile set up properly?",
    wa="Hi%2C%20I%20read%20your%20Google%20Business%20Profile%20guide%20and%20need%20help",
)
