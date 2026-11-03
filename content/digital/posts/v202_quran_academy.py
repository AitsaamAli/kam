import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=202,
    slug="online-quran-academy-website",
    title="Online Quran Academy Website for Students Abroad",
    h1="Online Quran Academy Website: Trial Classes, Time Zones and Fees From Abroad",
    crumb="Online Quran Academy Website",
    description="How to plan an online Quran academy website for overseas students: free trial booking, class times in the student's time zone, tutor pages and fee payments.",
    keyword="online quran academy website",
    cluster=["quran teaching website", "online quran classes website design", "quran academy for overseas students",
             "quran trial class booking", "female quran tutor page"],
    category="Websites by Profession",
    published="2026-11-03", published_h="3 November 2026",
    updated="2026-11-03", updated_h="3 November 2026",
    answer=(f"An online Quran academy website mainly serves families abroad, so it must show class times in the visitor's own time zone, "
            f"offer a free trial class in two or three clicks, introduce tutors (including female tutors) and accept fees from the UK, Gulf or North America. "
            f"A booking-ready site starts from {P['business']}."),
    takeaways=[
        "Most students of a Pakistani online Quran academy live abroad, so design every page for parents in the UK, Gulf, USA and Canada.",
        "Show timetables in the visitor's own time zone; a Pakistan-time schedule causes missed trials and refund requests.",
        "A free trial booking that takes under a minute is the single most important feature.",
        "Female tutor profiles, with first names and qualifications, answer a question many parents ask first.",
        "Plan international payments before launch: card payments, PayPal, Payoneer or bank transfer, each with clear fee terms.",
    ],
    body=f"""
<h2 id="who-visits">Who Visits an Online Quran Academy Website?</h2>
<p>Parents usually choose the academy, not the student. They are often in Manchester, Dubai, Houston or Toronto, searching on a phone in the evening, and comparing three or four academies at once. They want to know who will teach their child, when classes happen in their own time, how much it costs per month in their currency, and whether they can try a class first. The site should answer those four questions above the fold, in that order.</p>

<h2 id="pages">Pages an Online Quran Academy Website Needs</h2>
<table>
<tr><th>Page</th><th>Content</th><th>Parent's question it answers</th></tr>
<tr><td>Courses</td><td>Noorani Qaida, Nazra, Hifz, Tajweed, Islamic studies, with levels and ages</td><td>Is there a course for my child's level?</td></tr>
<tr><td>Tutors</td><td>Male and female tutors, qualifications, languages spoken</td><td>Who will teach, and can my daughter have a female tutor?</td></tr>
<tr><td>Timetable</td><td>Slots shown in the visitor's time zone</td><td>Can classes fit around school hours here?</td></tr>
<tr><td>Fees</td><td>Monthly plans by days per week, family discounts</td><td>What will it cost in pounds, dirhams or dollars?</td></tr>
<tr><td>Free trial</td><td>Short booking form with time-zone picker</td><td>Can we try before paying?</td></tr>
<tr><td>Safety and policies</td><td>How classes run, recording policy, parent supervision</td><td>Is the online classroom safe for children?</td></tr>
</table>

<h2 id="time-zones">How Do You Handle Time Zones on the Timetable?</h2>
<p>Store every slot in one reference time zone and display it in the visitor's local time, detected from the browser, with a manual selector in case the guess is wrong. Show both times in confirmation emails and WhatsApp messages ("5:00 pm London / 9:00 pm Pakistan"). Daylight saving changes in the UK, Europe and North America move class times twice a year, so the booking system must recalculate slots automatically rather than relying on staff to remember. This one detail prevents most no-shows in the first month.</p>

<h2 id="trial">Designing the Free Trial Booking</h2>
<ol>
<li>Ask for the student's age and level, the parent's name, a WhatsApp number with country code and preferred days.</li>
<li>Show available trial slots in local time and let the parent pick one.</li>
<li>Send an instant confirmation with the class link, the tutor's first name and both time zones.</li>
<li>Send a reminder a few hours before, and a follow-up after the trial with the fee plans.</li>
</ol>
<p>Our guide to <a href="/digital/blog/booking-system-development-cost">booking system development costs</a> explains when a ready-made scheduler is enough and when a custom one pays off.</p>

<h2 id="payments">Which Payment Options Work for Overseas Families?</h2>
<p>Parents abroad expect to pay by card, and many prefer monthly subscriptions. Options for a Pakistani academy include an international payment provider that supports your business, PayPal where available to you, Payoneer invoices, and bank transfer. Each has different fees and payout times, so check the current terms directly with each provider before you publish fee plans. Show prices in the parent's currency where possible and state clearly what happens to missed classes. For the wider picture, read our comparison of <a href="/digital/blog/stripe-paypal-pakistan-website">international payment options for Pakistani websites</a>.</p>

<h2 id="trust">Trust Signals Parents Look For</h2>
<ul>
<li>Tutor profiles with real qualifications and the languages each tutor speaks (Urdu, English, Arabic).</li>
<li>A clear statement on recording, screen sharing and whether a parent can sit in.</li>
<li>Reviews from parents in named countries, published with their permission.</li>
<li>A real contact route: WhatsApp, email and the hours when someone replies.</li>
</ul>
<p>Avoid promises such as "Hifz guaranteed in one year". Progress depends on the student, and parents trust academies that describe their method instead of guaranteeing results.</p>

<h2 id="package">Which Package Fits an Online Quran Academy?</h2>
<p>A small academy with one or two tutors can start with our starter site at {P['starter']} and a simple scheduling tool. Academies with ten or more tutors, multiple time zones and monthly subscriptions need booking, reminders and a parent area, which usually starts from {P['business']}. A full student portal with attendance and progress reports is a web app project; see our <a href="/digital/web-app-development">web app development service</a>.</p>
""",
    faqs=[
        ("How should an online Quran academy show class times to overseas parents?",
         "Store slots in one reference time zone and display them in the visitor's local time, detected automatically with a manual selector as backup. Confirmation messages should show both the local and Pakistan time. The system must handle daylight saving changes in the UK, Europe and North America automatically."),
        ("Is a free trial class necessary for a Quran academy website?",
         "Yes. Parents comparing several academies rarely pay before seeing a tutor teach their child. A trial booking that takes under a minute, with instant confirmation and a reminder, usually converts better than any discount. Follow up after the trial with fee plans and the next available slots."),
        ("Should the website list female Quran tutors separately?",
         "Many parents, especially of girls, ask for a female tutor before anything else. Show female tutors clearly on the tutors page with first names, qualifications and languages spoken, and let parents choose a female tutor during trial booking. This answers the question early and reduces back-and-forth on WhatsApp."),
        ("How can a Pakistani Quran academy accept fees from the UK or USA?",
         "Common options are an international card payment provider that supports your business, PayPal where it is available to you, Payoneer invoices and bank transfer. Fees and payout times differ, so confirm current terms with each provider. Show prices in the parent's currency and state your missed-class policy clearly."),
        ("What does an online Quran academy website cost?",
         f"A small academy can start with our starter site at {P['starter']} plus a scheduling tool. Larger academies with many tutors, time zones and monthly subscriptions usually need booking, reminders and a parent area, which starts from {P['business']}. A full student portal with attendance tracking is priced as a web app."),
        ("What safety information should a Quran teaching website include?",
         "Explain how online classes run, whether sessions are recorded, how recordings are stored, and whether a parent can sit in. Describe how tutors are selected. Parents of young children read this page closely, and a clear, honest policy builds more trust than general claims about safety."),
        ("Online Quran academy ki website mein sab se zaroori cheez kya hai?",
         "Sab se zaroori free trial class ki booking hai jo walidain ke apne time zone mein slots dikhaye. Is ke baad tutors ka page, khaas tor par female tutors, mahana fees unki currency mein, aur payment ka asaan tareeqa. WhatsApp par confirmation aur reminder zaroor bhejein."),
    ],
    sources=[
        ("Stripe: Global availability", "https://stripe.com/global"),
        ("PayPal Pakistan", "https://www.paypal.com/pk/home"),
        ("Payoneer", "https://www.payoneer.com/"),
        ("Google Calendar", "https://calendar.google.com/"),
        ("W3C: Declaring language in HTML", "https://www.w3.org/International/questions/qa-html-language-declarations"),
    ],
    method="We mapped the questions overseas parents ask when choosing an online Quran academy, reviewed scheduling and international payment options, and priced the build from our published packages. Payment provider terms change, so we link to each provider. Sources checked on 3 November 2026.",
    related=["booking-system-development-cost", "stripe-paypal-pakistan-website", "tuition-academy-website", "lms-for-academies-pakistan", "website-for-solar-installers-pakistan"],
    service_links=[("/digital/web-app-development", "Web app development"), ("/digital/pricing", "Our published prices")],
    cta="Planning a Quran academy website for students abroad?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20online%20Quran%20academy%20websites.%20I%20need%20a%20quote.",
)
