import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=179,
    slug='website-change-requests-cost',
    title='Website Change Requests: Why They Cost and How to Plan',
    h1='Website Change Requests During a Project: Why They Cost Extra and How to Plan for Them',
    crumb='Website Change Requests',
    description='Why a website change request mid-project costs extra, how scope creep happens, a worked example, and how owners and developers can handle changes fairly.',
    keyword='website change request',
    cluster=['scope creep website', 'extra pages cost', 'website project changes'],
    category='Hiring a Developer',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="A website change request is anything added or altered after the scope was agreed: a new page, a new feature, a redesign of an approved section. It costs extra because it adds work and can delay launch. Agree a written process: describe the change, get a quote and new date, approve in writing, then build, with 1 small contingency budget.",
    takeaways=["Changes are normal; unmanaged changes are what cause disputes.", "Fixed prices cover the agreed scope only; new work needs its own quote.", "Changes after design approval or build often cost more than the same change earlier.", "A simple written change process protects both owner and developer.", "Group small changes into a single request where possible."],
    body=f"""
<h2 id="what">What Counts as a Website Change Request?</h2>
<p>Every project changes a little as it takes shape. You see the design and realise a page is missing, a competitor launches a feature you want too, or a partner asks for a booking form. A website change request is any addition or alteration to the agreed scope after it was signed off. Changes are normal and often sensible. The trouble starts when they are added informally, through WhatsApp messages and phone calls, without anyone agreeing what they cost or how they affect the launch date. That slow drift is called scope creep.</p>
<p>Scope is easier to protect when you start with the right partner; see our guide to choosing a developer.</p>

<h2 id="types">Which Changes Usually Cost Extra?</h2>
<table>
<tr><th>Usually included</th><th>Usually a change request</th></tr>
<tr><td>Fixing errors against the agreed scope</td><td>Adding new pages or sections</td></tr>
<tr><td>Text edits within agreed revision rounds</td><td>New features such as booking, payments or login areas</td></tr>
<tr><td>Small layout fixes during agreed revisions</td><td>Redesigning a section already approved</td></tr>
<tr><td>Bugs found during testing</td><td>Switching to a different platform or theme mid-project</td></tr>
<tr><td>Agreed content placed on agreed pages</td><td>New integrations with other systems</td></tr>
</table>
<p>Exactly what is included depends on your contract; our contract checklist explains how to word it.</p>

<h2 id="why-cost">Why Do Changes Cost More Later?</h2>
<p>A change costs least before design starts, more after design approval and most after building, because finished work must be undone, redone and retested. Adding a page during planning is a line on a list. Adding the same page after launch preparation may mean new design, new content, navigation changes, new testing and an updated launch plan.</p>

<h2 id="example">What Does a Worked Example Look Like?</h2>
<p>An illustrative case: a clinic agrees a six-page business website. After design approval, the owner asks for an online appointment form linked to doctors' calendars. The developer explains this is a new feature: it needs design for the form, calendar logic, email and WhatsApp notifications and testing. They quote the extra work separately and estimate the launch moves by about a week. The owner can approve it now, or launch on time and add booking in a second phase. Either choice is fine; what matters is that it is a decision, not an assumption. The figures and timings are invented to show the process.</p>

<h2 id="process">What Is a Fair Change Process?</h2>
<ol>
<li><strong>Describe</strong> the change in writing: what, where and why.</li>
<li><strong>Estimate:</strong> the developer replies with cost and effect on the timeline.</li>
<li><strong>Decide:</strong> approve, defer to a later phase or drop it.</li>
<li><strong>Record:</strong> keep approved changes in one list with dates and prices.</li>
<li><strong>Build</strong> only after written approval.</li>
</ol>
<p>Fixed-price and hourly projects handle changes differently; our comparison of fixed price vs hourly explains the trade-offs.</p>

<h2 id="avoid">How Can Owners Reduce Change Requests?</h2>
<ul>
<li>Spend more time on the brief and discovery meeting.</li>
<li>Agree a full page list and feature list before design.</li>
<li>Involve every decision-maker early, not after design.</li>
<li>Keep a "phase two" list for ideas that can wait.</li>
<li>Hold a small contingency budget for genuine surprises.</li>
<li>Review the scope document once more, line by line, before signing it.</li>
<li>Ask the developer which parts of the scope they see as most likely to change.</li>
</ul>

<h2 id="developer">What Should a Developer Do?</h2>
<p>Flag a change as soon as it is requested, before doing the work, and never surprise a client with charges at the end. Our <a href="/digital/blog/how-to-give-website-design-feedback">design feedback guide</a> explains how revision rounds differ from changes.</p>

<h2 id="privacy">Do Changes Affect Data or Privacy?</h2>
<p>New features that collect personal data, such as booking forms or logins, also need privacy policy updates and security checks. Include these in the change estimate.</p>

<h2 id="ours">How We Price Changes</h2>
<p>Our packages, from {P['starter']}, list exactly what is included, and we quote any change in writing before starting it. See our <a href="/digital/pricing">pricing page</a>.</p>
<p>See also <a href="/digital/blog/website-discovery-meeting-what-to-expect">Your First Website Discovery Meeting</a>.</p>
""",
    faqs=[
        ('What is a website change request?',
         "It is any addition or alteration to a website project after the scope was agreed, such as a new page, a new feature, a redesign of an approved section or a new integration. Fixing errors against the agreed scope is not a change request; adding new work is."),
        ('Why do website changes cost extra?',
         "Because they add work beyond what the agreed price covered, and changes made after design approval or building often mean undoing, redoing and retesting finished work. The later a change comes, the more it usually costs and the more it can delay the launch."),
        ('How should change requests be handled?',
         "Describe the change in writing, get a written estimate of cost and timeline impact, decide whether to approve, defer or drop it, record approved changes in one list, and only then let building start. This simple process prevents surprises and disputes at the end."),
        ('What is scope creep in web development?',
         "Scope creep is the gradual growth of a project through small, informal additions that nobody formally prices or schedules. Each request seems minor, but together they delay launch and cause disagreements about cost. A written change process and a phase two list help prevent it."),
        ('How can I avoid change requests on my website project?',
         "Invest time in the brief and discovery meeting, agree full page and feature lists before design, involve all decision-makers early, keep a phase two list for ideas that can wait, and hold a small contingency budget for genuine surprises during the project."),
        ('Are text edits a change request?',
         "Usually not, if they fall within the agreed revision rounds and apply to pages already in scope. Adding new sections, rewriting pages after approval or adding new content types may count as changes. Check what your contract says about revisions and content."),
        ('Website project ke dauran tabdeeli ka kharch kyun lagta hai?',
         "Jo kaam pehle tay hua tha qeemat sirf usi ki hoti hai. Naya page ya feature baad mein maangne se naya kaam aur waqt lagta hai, khaas taur par design approve hone ke baad. Har tabdeeli likh kar bhejein, qeemat aur nayi tareekh poochein, aur approve karne ke baad hi kaam shuru karwayen."),
    ],
    sources=[('W3C WAI — WCAG overview', 'https://www.w3.org/WAI/standards-guidelines/wcag/'), ('ICO — UK GDPR guidance and resources', 'https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/'), ('OWASP — Top 10 web application security risks', 'https://owasp.org/www-project-top-ten/')],
    method="The clinic example is invented and labelled illustrative, as the plan requires. The included-versus-change table and change process are editorial, based on common contract practice. Our prices come from the published list.",
    related=['how-to-give-website-design-feedback', 'website-discovery-meeting-what-to-expect', 'website-testing-before-sign-off'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/contact', 'Get a written quote')],
    cta='Project scope getting out of hand?',
    wa='Hi%2C%20I%20read%20your%20change%20requests%20guide',
)
