import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=48,
    slug="school-website-design-pakistan",
    title="School Website Design in Pakistan: Admissions to Portal",
    h1="School Website Design in Pakistan: Admissions, Fee Schedules, Notices and a Parent Portal",
    crumb="School Website Design",
    description="School website design in Pakistan: online admission forms, fee schedule pages, notices, an Urdu option, student photo consent and what a parent portal really costs.",
    keyword="school website design pakistan",
    cluster=["academy website", "online admission form school", "parent portal pakistan", "school management system website",
             "tuition academy website", "school ki website banwana"],
    category="Websites by Industry",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=(f"Good school website design in Pakistan puts admissions, fee schedules, timings, notices and contact details where parents "
            f"find them on a phone, with an Urdu option if your parents prefer it. A 10-page school website starts from {P['business']}; "
            f"a parent portal with attendance, results and fee status is a web app from {P['app']}."),
    takeaways=[
        "Parents visit a school website for admissions, fees, timings, notices and contact; make these one tap away.",
        "An online admission form saves queues, but collect only what you need and protect it.",
        "Publish fee schedules clearly, with what is included, to cut repeated phone calls.",
        "Never publish children's photos or names without written parental consent.",
        "Start with a strong website; add a parent portal when you are ready to keep its data updated daily.",
    ],
    body=f"""
<h2 id="what-parents-need">What Should School Website Design in Pakistan Include?</h2>
<p>Parents use a school website at two moments: when choosing a school, and every week after enrolling. A prospective parent wants to know the curriculum, campus, fees and admission dates. A current parent wants the latest notice, the holiday schedule or the exam date sheet, usually on a phone during a busy morning. Good school website design in Pakistan serves both without making either group search.</p>

<h2 id="pages">Which Pages Does a School or Academy Need?</h2>
<table>
<tr><th>Page</th><th>For</th><th>Contents</th></tr>
<tr><td>Admissions</td><td>New parents</td><td>Classes open, age criteria, dates, documents, test details, online form</td></tr>
<tr><td>Fee schedule</td><td>New and current parents</td><td>Fees per class, admission and security charges, payment methods and deadlines</td></tr>
<tr><td>Academics</td><td>New parents</td><td>Curriculum, board affiliation, subjects, class sizes</td></tr>
<tr><td>Notices and calendar</td><td>Current parents</td><td>Holidays, exams, events, uniform changes</td></tr>
<tr><td>Campus and facilities</td><td>New parents</td><td>Photos of classrooms, labs, transport routes</td></tr>
<tr><td>Contact</td><td>Everyone</td><td>Address, map, timings, WhatsApp, phone for each campus</td></tr>
</table>
<p>For academies and tuition centres, swap academics for course pages with batch timings, teachers and results policy, and put enrolment front and centre.</p>

<h2 id="admissions">How Should an Online Admission Form Work?</h2>
<ol>
<li><strong>Parent fills a short form:</strong> child's name, date of birth, class applied for, parent's name, phone and email.</li>
<li><strong>Documents are uploaded</strong> only if needed at this stage, such as a birth certificate or previous result, through a secure upload.</li>
<li><strong>The school receives a notification</strong> and the parent gets an automatic acknowledgement with next steps.</li>
<li><strong>Staff schedule the test or interview</strong> and confirm by WhatsApp or email.</li>
<li><strong>Admission fee is paid</strong> by bank transfer, Raast or at the school, with the payment linked to the application.</li>
</ol>
<p>Keep the form short, and do not ask for information you will not use. Children's data deserves extra care: limit who can see applications, use HTTPS, and delete applications that do not proceed after a set period.</p>

<h2 id="fees">How Should You Present Fee Schedules?</h2>
<p>A clear fee page saves the front office hours of calls. Show fees by class in a table, list one-time charges separately, explain sibling discounts if offered, and state accepted payment methods and due dates. Date the page, for example "Fee schedule for session 2026–27", so parents know it is current. If fees differ by campus, use one table per campus.</p>

<h2 id="urdu">Should a School Website Be in Urdu?</h2>
<p>If many of your parents read Urdu more comfortably than English, add Urdu versions of the key pages: admissions, fees, notices and contact. Urdu is written right to left. The W3C, the body that sets web standards, advises setting the page direction with the <em>dir</em> attribute in the HTML rather than with styling, so text, menus and forms display correctly. Use a proper Urdu web font, such as a Nastaliq or Naskh style, and test on phones, because some fonts render poorly on older Android devices.</p>

<h2 id="photos">How Should Schools Handle Student Photos?</h2>
<p>Event galleries are popular with parents and powerful for admissions, but they involve children. Get written consent from parents at enrolment for website and social media use, with an option to say no. Do not caption photos with full names and classes together. Remove any photo promptly if a parent asks. Results and position-holder lists should only show what parents have agreed to publish.</p>

<h2 id="parent-portal">When Is a Parent Portal Worth It?</h2>
<p>A parent portal is a private area where each parent logs in to see their child's attendance, results, homework, notices and fee status. It reduces calls and paper, but only if staff update it every day. Before building one, check whether your school management software already offers a parent app; connecting the website to it may be cheaper than building a new portal.</p>
<table>
<tr><th>Portal feature</th><th>Who updates it</th></tr>
<tr><td>Attendance</td><td>Class teacher, daily</td></tr>
<tr><td>Results and report cards</td><td>Exam office, each term</td></tr>
<tr><td>Homework and diary</td><td>Subject teachers, daily</td></tr>
<tr><td>Fee status and vouchers</td><td>Accounts office, monthly</td></tr>
</table>

<h2 id="what-we-build">What We Would Build for You</h2>
<p>A tuition academy usually needs up to 5 pages, from {P['starter']}. A school with admissions, fee schedules, notices and a gallery typically needs up to 10 pages, from {P['business']}, including an online admission form and an Urdu version of key pages if required. Parent portals and school management features are web applications, from {P['app']} and within {P['app_range']} depending on modules. See our <a href="/digital/web-app-development">web app development</a> service. Other sectors are covered in our <a href="/digital/blog/clinic-website-design-pakistan">websites by industry hub</a>, and NGOs running schools may find our <a href="/digital/blog/ngo-donation-website-pakistan">NGO website guide</a> useful.</p>
""",
    faqs=[
        ("How much does a school website cost in Pakistan?",
         f"A small academy website of up to 5 pages starts from {P['starter']}, and a school website with admissions, fee schedules, notices and a gallery of up to 10 pages starts from {P['business']}. A parent portal with attendance, results and fee status is a web application starting from {P['app']}."),
        ("Can parents apply for admission online?",
         "Yes. A short online admission form can collect the child's details, class applied for and parent contact details, send the school a notification and give parents an automatic acknowledgement. Staff then schedule the test or interview. Collect only what you need and protect applications from public access."),
        ("Should a school publish fees on its website?",
         "Yes, most parents expect it, and it saves the front office many calls. Show fees by class in a clear table, list one-time charges separately, explain discounts, and state payment methods and due dates. Date the page by session so parents know the figures are current."),
        ("Is it safe to post student photos on a school website?",
         "Only with written parental consent, ideally collected at enrolment with a clear option to decline. Avoid captions that combine full names with classes, remove photos promptly when a parent asks, and publish results or position lists only where parents have agreed. Children's information deserves extra care."),
        ("Do schools need a parent portal?",
         "Only if staff will update it every day. A portal showing attendance, results, homework and fee status reduces calls and paperwork, but an outdated portal frustrates parents. First check whether your school management software already offers a parent app that the website can link to."),
        ("School ki website mein kya kya hona chahiye?",
         "School ki website mein admission ka tareeqa aur form, har class ki fees, school timings, notices aur chhuttiyon ka calendar, campus ki tasveerein aur WhatsApp ke saath rabte ki maloomat honi chahiye. Agar walidain Urdu behtar parhte hain to aham pages Urdu mein bhi banayein."),
    ],
    sources=[
        ("W3C — Structural markup and right-to-left text in HTML", "https://www.w3.org/International/questions/qa-html-dir"),
        ("W3C — Web Content Accessibility Guidelines (WCAG) 2.2", "https://www.w3.org/TR/WCAG22/"),
        ("Google Business Profile Help — Create and manage your Business Profile", "https://support.google.com/business/answer/7039811"),
        ("State Bank of Pakistan — Press release on Raast P2M, 6 December 2023", "https://www.sbp.org.pk/press/2023/Pr-06-Dec-2023.pdf"),
        ("OWASP — Top 10 web application security risks", "https://owasp.org/www-project-top-ten/"),
    ],
    method=("Right-to-left guidance for Urdu pages comes from W3C, checked 29 October 2026. Page lists, admission flow and portal tables "
            "reflect how we scope school projects. We state no specific education or child-data regulation because we could not source "
            "one; consent advice is good practice. Prices are our own published packages."),
    related=["clinic-website-design-pakistan", "ngo-donation-website-pakistan", "gym-website-pakistan", "web-app-development-cost-in-pakistan"],
    service_links=[("/digital/web-app-development", "Parent portals and school systems"), ("/digital/business-websites", "School and academy websites")],
    cta="Planning a website for your school?",
    wa="Hi%2C%20I%20read%20your%20school%20website%20guide%20and%20need%20a%20quote",
)
