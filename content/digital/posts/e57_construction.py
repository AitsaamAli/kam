import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=57,
    slug="construction-company-website",
    title="Construction Company Website: Projects, Tenders and Trust",
    h1="Construction Company Website: Project Portfolio, Capability Statement and Tender Downloads",
    crumb="Construction Company Website",
    description="A construction company website that wins work: a project portfolio clients can check, a capability statement, tender document downloads and real credentials only.",
    keyword="construction company website",
    cluster=["builder website pakistan", "contractor website", "construction portfolio website", "capability statement page",
             "tender documents download", "construction company ki website"],
    category="Websites by Industry",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=(f"A construction company website wins work with a project portfolio showing scope, client type, value range and photos, a "
            f"downloadable capability statement, genuine registrations such as PEC, and a tender or vendor documents section. A "
            f"construction website of up to 10 pages starts from {P['business']}."),
    takeaways=[
        "Clients and consultants judge contractors on completed projects, capacity and registrations.",
        "Each portfolio project should state scope, sector, location, year and role, with real site photos.",
        "A downloadable capability statement saves time in pre-qualification.",
        "Show only registrations, certifications and safety records you genuinely hold, with numbers that can be checked.",
        "A documents section for tenders and vendor registration keeps files current and easy to find.",
    ],
    body=f"""
<h2 id="what-clients-check">What Should a Construction Company Website Show?</h2>
<p>A developer, consultant, procurement officer or homeowner checking a contractor wants evidence: what you have built, how big, for whom, and whether you are registered and safe to hire. Most contractor sites in Pakistan show a slideshow of generic images and a list of services. The ones that win work show proof.</p>

<h2 id="portfolio">How Should a Project Portfolio Be Structured?</h2>
<table>
<tr><th>Field</th><th>Example</th></tr>
<tr><td>Project name and location</td><td>Commercial plaza, Faisalabad</td></tr>
<tr><td>Sector</td><td>Commercial, residential, industrial, infrastructure</td></tr>
<tr><td>Your role</td><td>Main contractor, civil works, MEP, finishing</td></tr>
<tr><td>Scope</td><td>Covered area, floors, key works</td></tr>
<tr><td>Value range and year</td><td>A range rather than an exact figure, if the client prefers</td></tr>
<tr><td>Client type</td><td>Private developer, factory, public sector, named only with permission</td></tr>
<tr><td>Photos</td><td>Progress and completed photos from your own site visits</td></tr>
</table>
<p>Filters by sector and role help a factory owner find industrial projects quickly. Ask clients before naming them or showing their buildings, and never claim another contractor's work.</p>

<h2 id="capability">What Is a Capability Statement?</h2>
<p>A capability statement is a short document, usually two to six pages, summarising your company, registrations, key projects, equipment, team, safety approach and contact details. Pre-qualification and procurement teams ask for it constantly. Put a current version on the website as a PDF, with the date in the file name, and update it each year or after a major project.</p>

<h2 id="registrations">Which Registrations and Credentials Should You Show?</h2>
<p>The Pakistan Engineering Council, or PEC, registers engineers and engineering firms, and its website states that only PEC-registered firms are authorised to undertake government and public sector engineering projects. If your firm is registered, show the registration number, category and validity so clients can check it. List any other certifications, such as quality or safety management systems, only if you hold them, with the certificate number and issuing body.</p>
<p>Safety records are powerful but must be accurate. If you publish figures such as hours without a lost-time incident, be ready to back them up. Never show a certificate or logo you are not entitled to.</p>

<h2 id="tenders">How Should Tender and Vendor Documents Be Handled?</h2>
<p>Contractors deal with two kinds of documents: those they send, such as company profiles and registrations, and those they receive, such as tenders for subcontractors and suppliers. A documents section can handle both:</p>
<ul>
<li>a public download area for the capability statement and company profile</li>
<li>a page listing open subcontract or supply tenders, with deadlines and downloadable documents</li>
<li>a vendor registration form for suppliers and subcontractors who want to work with you</li>
<li>a restricted area, behind a login, for documents shared only with pre-qualified bidders</li>
</ul>
<p>Remove expired tenders promptly and date every file.</p>

<h2 id="leads">How Should Enquiries Be Handled?</h2>
<p>Separate enquiry routes help: a project enquiry form for clients, with project type, location, size and timeline; a vendor form for suppliers; and a careers form for staff. Each goes to the right person. Clients for residential projects often prefer WhatsApp, while institutional clients expect email and a formal reply.</p>

<h2 id="example">A Worked Example: A Mid-Sized Contractor</h2>
<p>Illustrative example, not a real client. A contractor in Rawalpindi does commercial and industrial civil works.</p>
<ul>
<li>A portfolio of twelve projects, filterable by sector, each with role, scope, year and own photos.</li>
<li>A capability statement PDF, dated, plus PEC registration details shown on the about page.</li>
<li>A tenders page for subcontract packages, with deadlines and downloads.</li>
<li>Separate forms for project enquiries, vendors and careers.</li>
</ul>

<h2 id="what-we-build">What We Would Build for You</h2>
<p>For contractors, we build a site with a filterable portfolio, capability statement download, credentials page, tenders and vendor pages and routed enquiry forms. Up to 10 pages starts from {P['business']}. A bidder portal with logins, document versioning and submission tracking is a web application from {P['app']}. See our <a href="/digital/business-websites">business websites</a> service and our <a href="/digital/blog/clinic-website-design-pakistan">websites by industry hub</a>. Building material makers may also find our <a href="/digital/blog/b2b-catalogue-website-manufacturers">B2B catalogue guide</a> useful.</p>
""",
    faqs=[
        ("What should a contractor's website include?",
         "A filterable project portfolio with scope, role, sector, year and real photos, a dated capability statement to download, registration and certification details you genuinely hold, a tenders and vendor section, and separate enquiry forms for clients, suppliers and job seekers, each routed to the right person."),
        ("Should a contractor show PEC registration on the website?",
         "If your firm is registered, yes. The Pakistan Engineering Council states that only PEC-registered firms are authorised to undertake government and public sector engineering projects, so clients often check. Show the registration number, category and validity exactly as issued, and keep it updated when renewed."),
        ("What is a capability statement for a construction company?",
         "It is a short document, usually two to six pages, summarising your company, registrations, key projects, equipment, team, safety approach and contacts. Procurement and pre-qualification teams ask for it often. Keep a dated PDF on your website and update it yearly or after major projects."),
        ("Can I show client names on my construction portfolio?",
         "Only with the client's permission. Many clients are happy to be named, but some prefer privacy. Without permission, describe the client by type, such as private developer or textile factory, and show your own site photos. Never present another contractor's project as your own."),
        ("How much does a construction company website cost?",
         f"A contractor site with portfolio, capability statement download, credentials, tenders and routed enquiry forms starts from {P['business']} for up to 10 pages. A bidder portal with logins, document versions and submission tracking is a web application starting from {P['app']}. Hosting and a domain are extra."),
        ("Construction company ki website mein kya dikhana chahiye?",
         "Mukammal kiye gaye projects ki asli tasveerein, har project ka scope, saal aur aap ka kirdar, company profile ki PDF, aur PEC registration agar hai to number ke saath. Tenders aur vendors ke liye alag page rakhein. Koi aisa certificate na lagayen jo aap ke paas nahin."),
    ],
    sources=[
        ("Pakistan Engineering Council — Homepage (registration of engineers and firms)", "https://www.pec.org.pk/"),
        ("Google Search Central — Creating helpful, reliable, people-first content", "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"),
        ("Google Business Profile Help — Create and manage your Business Profile", "https://support.google.com/business/answer/7039811"),
        ("WordPress.org — Roles and capabilities", "https://wordpress.org/documentation/article/roles-and-capabilities/"),
        ("OWASP — Top 10 web application security risks", "https://owasp.org/www-project-top-ten/"),
    ],
    method=("PEC's role and its statement on public sector projects come from pec.org.pk, opened 29 October 2026 (a new source, logged "
            "in the part report). Portfolio fields, document sections and the contractor example are our own illustrative templates. "
            "Prices are our own published packages."),
    related=["clinic-website-design-pakistan", "real-estate-website-pakistan", "b2b-catalogue-website-manufacturers", "logistics-company-website"],
    service_links=[("/digital/business-websites", "Construction company websites"), ("/digital/contact", "Discuss your project portfolio")],
    cta="Want a website that proves your track record?",
    wa="Hi%2C%20I%20read%20your%20construction%20company%20website%20guide%20and%20need%20a%20quote",
)
