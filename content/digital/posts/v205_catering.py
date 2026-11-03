import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=205,
    slug="catering-company-website",
    title="Catering Website in Pakistan: Menus and Per-Head Rates",
    h1="Catering Company Website in Pakistan: Menus, Per-Head Pricing and Event Enquiries",
    crumb="Catering Company Website",
    description="What a catering website in Pakistan needs: a per-head menu builder, event types, tasting bookings and food-safety details that help families and offices decide.",
    keyword="catering website pakistan",
    cluster=["caterers website lahore", "catering business website design", "event catering menu website",
             "per head menu builder", "food tasting booking form"],
    category="Websites by Profession",
    published="2026-11-03", published_h="3 November 2026",
    updated="2026-11-03", updated_h="3 November 2026",
    answer=(f"A catering website in Pakistan should let a family or office build a menu, see an estimated per-head cost and send the event date and guest count in one go. "
            f"Add event types, real food photos, a tasting booking and food-safety details. "
            f"Our starter package at {P['starter']} covers a caterer's core pages and enquiry form."),
    takeaways=[
        "A menu builder that shows an estimated per-head cost turns browsing into specific enquiries.",
        "Separate wedding, corporate, dawat and boxed-meal catering; each buyer looks for different things.",
        "Real photos of your own dishes and set-ups matter more than any design choice.",
        "Offer a tasting booking for large events; it is often the step that wins the order.",
        "Show your Punjab Food Authority licence and hygiene practice if you operate in Punjab.",
    ],
    body=f"""
<h2 id="buyers">Who Uses a Catering Website in Pakistan?</h2>
<p>Three types of buyer reach a caterer through search. Families planning a wedding function, a mehndi or a large dawat want menus, per-head rates and a tasting. Offices want lunch boxes, seminar catering and monthly contracts with invoices. Event planners want reliable partners who deliver on time and can handle 1,000 guests. A catering website in Pakistan that serves all three needs a clear path for each, rather than one long menu page.</p>

<h2 id="menu-builder">How Does a Per-Head Menu Builder Work?</h2>
<p>The visitor picks a base package (for example, one rice dish, one curry, one barbecue item, naan, salad and a dessert), swaps or adds items, and the page shows an estimated per-head cost and a total for their guest count. The estimate is labelled clearly as an estimate, because final prices depend on the date, venue and quantities. When they submit, you receive the full menu, date, guest count and location, which is exactly what you need to quote. This is far more useful than a contact form that says "Please send rates".</p>
<table>
<tr><th>Approach</th><th>What the visitor gets</th><th>What you receive</th></tr>
<tr><td>Static PDF menu</td><td>A list to read and a phone number</td><td>A call asking for rates</td></tr>
<tr><td>Fixed packages on the page</td><td>Per-head prices for set menus</td><td>Enquiries for a named package</td></tr>
<tr><td>Menu builder with estimate</td><td>Their own menu with an estimated cost</td><td>Full menu, date, guests and location</td></tr>
</table>
<p>The builder needs maintenance when ingredient costs change, so date it and assign someone to update the prices. Our guide on <a href="/digital/blog/show-prices-on-website-or-not">whether to show prices on a website</a> explains how to label estimates.</p>

<h2 id="event-pages">Pages for Each Event Type</h2>
<ul>
<li><strong>Weddings and functions:</strong> menus by function, live counters, service staff, crockery and table setup.</li>
<li><strong>Corporate catering:</strong> lunch boxes, hi-tea, seminar and conference packages, invoicing and monthly contracts.</li>
<li><strong>Home dawats:</strong> smaller minimums, delivery areas, reheating guidance.</li>
<li><strong>Boxed meals and bulk orders:</strong> minimum quantities, lead time, delivery slots.</li>
</ul>
<p>Each page should have its own enquiry button that tells you which event type the lead came from.</p>

<h2 id="tasting">Why Offer Tasting Bookings?</h2>
<p>For large functions, families want to taste before committing to a menu for hundreds of guests. A tasting booking form with available days, the number of people attending and the dishes they want to try makes the process feel professional. State whether tastings are free, charged, or adjusted against the final bill. Confirm on WhatsApp and remind them the day before.</p>

<h2 id="hygiene">What Food-Safety Information Should a Catering Website Show?</h2>
<p>In Punjab, food businesses are licensed by the Punjab Food Authority. If you hold a licence, mention it and show it on an "About our kitchen" page alongside photos of the kitchen, storage and staff in uniform. Describe how food is transported and kept hot at venues. Buyers rarely ask about this directly, but a clean kitchen page often decides between two caterers with similar prices. Do not claim certifications you do not hold.</p>

<h2 id="corporate">Winning Corporate Clients</h2>
<p>Office managers search during working hours and often need a quotation on letterhead for approval. Offer a downloadable sample quotation, state your invoicing terms and list the delivery areas you cover reliably. Logos of corporate clients can be shown only with their permission. A separate corporate page usually ranks for searches such as "office lunch catering Lahore" better than a general homepage.</p>

<h2 id="package">Which Package Fits a Caterer?</h2>
<p>Most caterers start with our starter package at {P['starter']}: event pages, menus, gallery, tasting booking and enquiry routing to WhatsApp. A live menu builder with per-head estimates and several branches fits the business package at {P['business']}. See <a href="/digital/business-websites">what each package includes</a>. Caterers that also run a venue should read our guide to <a href="/digital/blog/marquee-wedding-hall-website">marquee and wedding hall websites</a>.</p>
""",
    faqs=[
        ("Should a caterer publish per-head prices on the website?",
         "Publishing per-head prices for set packages, or an estimate from a menu builder, usually brings better enquiries than hiding prices. Label figures as estimates that depend on date, venue and guest count, and update them when ingredient costs change. The written quotation still confirms the final price."),
        ("What is a menu builder on a catering website?",
         "It lets visitors choose dishes for their event, enter the guest count and see an estimated per-head cost and total. When they submit, the caterer receives the full menu, date, guests and location, which makes quoting quick. It needs regular price updates to stay accurate."),
        ("Do catering websites need separate pages for corporate clients?",
         "Yes. Office managers want lunch boxes, hi-tea and seminar packages, invoices and monthly contracts, while families want wedding menus and tastings. A separate corporate page answers those needs, ranks for office catering searches and can offer a sample quotation that managers forward for approval."),
        ("Should a catering company website mention food licences?",
         "If you hold a licence, such as one from the Punjab Food Authority, mention it and show it with real photos of your kitchen and storage. Describe how food is transported and kept hot. Never claim certifications you do not hold, because buyers and authorities can check."),
        ("How much does a catering company website cost?",
         f"Most caterers fit our starter package at {P['starter']}, which covers event pages, menus, a gallery, tasting booking and WhatsApp enquiry routing. A live menu builder with per-head estimates, or several branches, fits the business package at {P['business']}. Maintenance for menu and price updates starts at {P['maint']} a month."),
        ("How can a caterer handle tasting requests online?",
         "Add a tasting form with available days, the number of people attending and the dishes they want to try. State whether tastings are free, charged or adjusted against the final bill. Confirm the booking on WhatsApp and send a reminder the day before, so families arrive prepared."),
        ("Catering ki website se zyada orders kaise milenge?",
         "Har event ke liye alag page banayein, jaise shadi, office lunch aur ghar ki dawat. Per head rates ya menu builder rakhein, asal khane ki tasveerein lagayein aur tasting booking ka form dein. Food Authority ka license ho to zaroor dikhayein, aur har enquiry WhatsApp par foran pohanchni chahiye."),
    ],
    sources=[
        ("Punjab Food Authority", "https://pfa.gop.pk/"),
        ("Schema.org: FoodEstablishment", "https://schema.org/FoodEstablishment"),
        ("Google Search Central: Creating helpful, reliable, people-first content", "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"),
        ("WhatsApp Business: Business platform", "https://business.whatsapp.com/products/business-platform"),
    ],
    method="We mapped how families, offices and event planners look for caterers, reviewed the Punjab Food Authority's role for food businesses, and priced the build from our published packages. Sources checked on 3 November 2026.",
    related=["marquee-wedding-hall-website", "restaurant-website-online-ordering-pakistan", "show-prices-on-website-or-not", "home-bakery-cafe-website"],
    service_links=[("/digital/business-websites", "Business website packages"), ("/digital/contact", "Get a written quote")],
    cta="Want catering enquiries that arrive with the menu already chosen?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20catering%20websites.%20I%20would%20like%20a%20quote.",
)
