#!/usr/bin/env python3
"""P1 fix: correct outdated TY2026 deadline statements and unsupported 24hr / 100% claims (5 Nov 2026).
Only <body> text and JSON-LD answers are changed; titles, meta descriptions and canonicals are left as published."""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NOTE = ('<div class="info-box" style="border-left:4px solid #D4AF37;background:#fffbea;padding:12px 16px;margin:0 0 18px">'
        '<p><strong>Update, 5 November 2026:</strong> FBR later extended the Tax Year 2026 deadline to 31 October 2026, and that date has now passed. '
        'Returns can still be filed late; see <a href="/blogs/tax-return-deadline-passed-31-october-2026-next-steps">what to do after the 31 October deadline</a>.</p></div>')
NOTE_PAGES = ["blogs/fbr-extends-tax-return-deadline-october-15-2026", "blogs/salaried-employees-file-before-october-15-deadline-pakistan",
              "blogs/freelancers-extra-15-days-file-tax-return-pakistan", "blogs/shopkeepers-traders-october-15-deadline-still-not-enough-time-pakistan",
              "blogs/7-mistakes-last-minute-tax-filers-before-october-15-pakistan", "will-fbr-extend-deadline-again-after-october-15-pakistan",
              "blogs/fbr-new-tax-return-form-2026-pakistan", "blogs/income-tax-return-2026-iris-live-pakistan"]
BODY_RULES = [
    (r"were due by 15 October 2026 after the extension", "were due by 31 October 2026 after two extensions"),
    (r"\(30 September, extended to 15 October 2026\)", "(30 September, extended first to 15 October and then to 31 October 2026)"),
    (r"\(30 September 2026, extended to 15 October 2026\)", "(30 September 2026, extended first to 15 October and then to 31 October 2026)"),
    (r"30 September 2026, extended to 15 October 2026;", "30 September 2026, extended first to 15 October and then to 31 October 2026;"),
    (r"September 30, 2026 \(extended to 15 October 2026\)", "September 30, 2026 (extended first to 15 October and then to 31 October 2026)"),
    (r"FBR Deadline: 15 October 2026 \(extended\)", "FBR Deadline: 31 October 2026 (extended)"),
    (r"With (the|FBR's) deadline now 15 October 2026,", r"With \1 deadline then set at 15 October 2026 (FBR later extended it to 31 October 2026),"),
    (r"Last date 30 September 2026\.", "Last date pehle 30 September 2026 thi, phir 31 October 2026 tak barhai gayi, aur ab guzar chuki hai."),
    (r"sab ke liye last date 30 September 2026 hai\.", "sab ke liye last date 31 October 2026 thi (pehle 30 September, phir extend hui), jo ab guzar chuki hai."),
]
CLAIMS = {
    "fbr-notice-defense.html": [('<div class="stat-num">24hr</div><div class="stat-lbl">Response Time</div>', '<div class="stat-num">Mon&ndash;Sat</div><div class="stat-lbl">Office Hours</div>'),
                                ('<div class="stat-num">100%</div><div class="stat-lbl">Legal Compliance</div>', '<div class="stat-num">IRIS</div><div class="stat-lbl">Replies Filed Online</div>')],
    "aop-tax-return.html": [('<div class="stat-num">24hr</div><div class="stat-lbl">Turnaround</div>', '<div class="stat-num">Mon&ndash;Sat</div><div class="stat-lbl">Office Hours</div>'),
                            ('<div class="stat-num">100%</div><div class="stat-lbl">FBR Acceptance</div>', '<div class="stat-num">IRIS</div><div class="stat-lbl">Filed Online</div>')],
    "testimonials.html": [('<div class="highlight-num">24hr</div><div class="highlight-label">Average Filing Time</div>', '<div class="highlight-num">Mon&ndash;Sat</div><div class="highlight-label">Office Hours, 9 to 6</div>'),
                          ("100% FBR Compliant", "Filed on FBR IRIS")],
    "pricing.html": [("100% Satisfaction Guarantee", "Written Fee Quote First")],
    "blogs/24-hour-tax-consultant-support-pakistan.html": [
        ("Yes — WhatsApp 0328-4675162 anytime, as a real communication commitment rather than a marketing phrase.",
         "You can WhatsApp 0328-4675162 at any time; we reply during office hours, Monday to Saturday 9:00 AM to 6:00 PM and Friday until 12:30 PM."),
        ("commitment, not a marketing phrase. WhatsApp 0328-4675162, anytime.", "commitment we can keep: messages sent outside office hours are answered the next working morning."),
        ("Available anytime", "Message anytime, reply in office hours")],
}


def main():
    os.chdir(ROOT)
    changed = set()
    for f in [x for x in glob.glob("**/*.html", recursive=True) if not x.startswith(("content/", "node_modules/", "digital/"))]:
        t = open(f, encoding="utf-8").read()
        b = t.find("<body")
        head, body = t[:b], t[b:]
        nb = body
        for pat, rep in BODY_RULES:
            nb = re.sub(pat, rep, nb)
        if f[:-5] in NOTE_PAGES and "Update, 5 November 2026" not in nb:
            a = nb.find('class="article-body')
            a = nb.find("<h2", a if a > 0 else nb.find("<article"))
            nb = nb[:a] + NOTE + nb[a:]
        n = head + nb
        for old, new in CLAIMS.get(f, []):
            assert old in n or new in n, (f, old[:50])
            n = n.replace(old, new)
        if n != t:
            open(f, "w", encoding="utf-8").write(n)
            changed.add(f)
    print("files changed", len(changed))


if __name__ == "__main__":
    main()
