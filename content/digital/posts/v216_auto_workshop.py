import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=216,
    slug="auto-workshop-website",
    title="Car Workshop Website: Service Booking and Price Lists",
    h1="Car Workshop Website: Service Menu, Online Booking and Pick-and-Drop",
    crumb="Car Workshop Website",
    description="How to plan a car workshop website: a clear service menu with prices, online booking, pick-and-drop requests, before-and-after photos and honest estimates.",
    keyword="car workshop website",
    cluster=["auto repair website lahore", "car service booking website", "car maintenance price list",
             "pick and drop car service", "car repair estimate form"],
    category="Websites by Profession",
    published="2026-11-03", published_h="3 November 2026",
    updated="2026-11-03", updated_h="3 November 2026",
    answer=(f"Drivers choose a workshop they trust not to overcharge. A car workshop website should show a service menu with starting prices for common jobs, let owners book a slot or request pick-and-drop, and show real before-and-after work. "
            f"Our starter package at {P['starter']} covers booking and these pages."),
    takeaways=[
        "A service menu with starting prices for oil changes, tuning, brakes and AC service builds trust before the first visit.",
        "Online booking should ask for the car model, year and the problem, so the workshop can prepare parts.",
        "Pick-and-drop is a strong selling point for busy owners; state the areas and the charge.",
        "Before-and-after photos of dent, paint and detailing work sell those services better than any description.",
        "Send a written estimate before starting work, and say on the website that you always do.",
    ],
    body=f"""
<h2 id="trust">Why Does Trust Decide Which Workshop Gets the Car?</h2>
<p>Most car owners have a story about a workshop that charged for parts it never changed. When they search for a new one, they look for signs of honesty: clear prices, named mechanics, a clean workshop and reviews from other owners. A car workshop website that shows these signs gets the first booking, and a good first service earns the next one. Flashy designs matter much less than plain, specific information.</p>

<h2 id="menu">What Should a Car Workshop Website Show in Its Service Menu?</h2>
<table>
<tr><th>Service</th><th>What to state</th></tr>
<tr><td>Periodic maintenance</td><td>Oil and filter change, by engine size, with oil brands offered</td></tr>
<tr><td>Tuning and diagnostics</td><td>Scanner diagnosis, what is checked, starting price</td></tr>
<tr><td>Brakes and suspension</td><td>Pad replacement, disc skimming, shock absorbers</td></tr>
<tr><td>AC service</td><td>Gas refill, leak test, cooling check</td></tr>
<tr><td>Denting and painting</td><td>Per panel, with photos of finished work</td></tr>
<tr><td>Detailing</td><td>Interior cleaning, polish, ceramic coating options</td></tr>
</table>
<p>Prices should be "starting from" figures with a note that the final price depends on the car and parts, confirmed in a written estimate. Review them every few months, because parts and oil prices change.</p>

<h2 id="booking">Online Booking for Workshops</h2>
<p>The booking form should ask for the car make, model and year, the registration number, the service needed or a short description of the problem, and a preferred date and drop-off time. Knowing the car in advance lets the workshop arrange parts and avoid a second visit. Confirm on WhatsApp and send updates during the job: received, diagnosed with estimate, work approved, ready for collection. These updates reduce phone calls and make the workshop feel organised. Our guide to <a href="/digital/blog/booking-system-development-cost">booking system costs</a> explains when a simple form is enough.</p>

<h2 id="pickdrop">Does Offering Pick-and-Drop Help?</h2>
<p>For busy professionals, a driver who collects the car from home or office and returns it after the service removes the biggest barrier to booking. Give pick-and-drop its own section with the areas covered, the charge and how the handover works, including photos of the car's condition at pick-up. This protects both sides if a scratch is later disputed.</p>

<h2 id="photos">Before-and-After Photos and Videos</h2>
<p>For dent, paint and detailing work, a good set of before-and-after photos is the best sales page. Photograph the same angle in the same light before and after, and blur number plates unless the owner agrees. A short video of a diagnostic scan or a brake inspection also shows customers that the workshop explains its work.</p>

<h2 id="estimates">How Should Estimates and Approvals Work?</h2>
<p>State on the website that no work starts without the customer's approval of a written estimate, and stick to it. Send the estimate by WhatsApp with parts and labour listed separately. If additional faults are found, send a new estimate. Offer to return replaced parts on request. This one policy, written clearly, answers the biggest fear owners have about workshops.</p>

<h2 id="reminders">Service Reminders That Bring Cars Back</h2>
<p>Most cars need an oil change every few thousand kilometres, and owners forget. When a car leaves the workshop, record the mileage and the date, and with the owner's permission send a WhatsApp reminder when the next service is likely due. Keep the message short and useful, with a booking link. A record of past services also helps the mechanic spot recurring faults. Over a year, reminders like these turn one-time customers into regulars, which is cheaper than finding new customers through ads.</p>

<h2 id="package">Which Package Suits a Car Workshop?</h2>
<p>A single workshop fits our starter package at {P['starter']}: service menu, booking form, pick-and-drop section, gallery and WhatsApp updates. Workshops with several branches or a customer area showing service history fit the business package at {P['business']}. See our <a href="/digital/business-websites">business website packages</a>. Showrooms that sell cars as well should read our guide to <a href="/digital/blog/car-showroom-used-car-dealer-website">car dealer websites in Pakistan</a>.</p>
""",
    faqs=[
        ("Should a car workshop publish service prices online?",
         "Yes, as starting prices for common jobs such as oil changes by engine size, AC service and brake pads, with a note that the final price depends on the car and parts. Confirm every job with a written estimate and review the listed prices every few months."),
        ("What should a car service booking form ask?",
         "Ask for the car make, model, year and registration number, the service needed or a short description of the problem, and a preferred date and drop-off time. Knowing the car in advance lets the workshop arrange parts and avoid asking the owner to come back."),
        ("Is pick-and-drop worth offering for a car workshop?",
         "For many busy owners it is the main reason to book. Show the areas covered, the charge and how handover works, and photograph the car's condition at pick-up. Those photos protect both the owner and the workshop if a scratch or dent is disputed later."),
        ("How can a workshop website prove it does not overcharge?",
         "State that no work starts without approval of a written estimate listing parts and labour, send updated estimates if more faults are found, and offer to return replaced parts. Publish starting prices and reviews from real customers who agreed to share them."),
        ("What does a car workshop website cost?",
         f"A single workshop with a service menu, booking form, pick-and-drop section, gallery and WhatsApp updates fits our starter package at {P['starter']}. Workshops with several branches or a customer area showing service history fit the business package at {P['business']}. Maintenance starts at {P['maint']} a month."),
        ("What photos should a denting and painting workshop show?",
         "Show before-and-after photos of the same panel from the same angle and in similar light, with number plates blurred unless the owner agrees. Add detailing results and short videos of inspections. Consistent, real photos are far more persuasive than stock images of luxury cars."),
        ("Workshop ki website par customer ka bharosa kaise jeetein?",
         "Aam kaam ki shuruati qeematein likhein, likhit estimate ke baghair kaam shuru na karne ka wada karein, purane parts wapas dene ki peshkash karein, aur asal kaam ki pehle aur baad ki tasveerein lagayein. Booking ke baad WhatsApp par kaam ki update dete rahein."),
    ],
    sources=[
        ("Schema.org: AutoRepair", "https://schema.org/AutoRepair"),
        ("Google Business Profile Help: Tips to improve your local ranking", "https://support.google.com/business/answer/7091"),
        ("WhatsApp Business: Business platform", "https://business.whatsapp.com/products/business-platform"),
        ("Google Search Central: Creating helpful, reliable, people-first content", "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"),
    ],
    method="We listed what car owners look for when choosing a workshop and the steps of a typical service job, reviewed local listing guidance, and priced the build from our published packages. Sources checked on 3 November 2026.",
    related=["car-showroom-used-car-dealer-website", "booking-system-development-cost", "show-prices-on-website-or-not", "reviews-testimonials-on-website"],
    service_links=[("/digital/business-websites", "Business website packages"), ("/digital/contact", "Get a written quote")],
    cta="Want car owners to book your workshop with confidence?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20car%20workshop%20websites.%20I%20would%20like%20a%20quote.",
)
