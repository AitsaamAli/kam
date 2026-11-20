"""Fixes from the 20 Nov 2026 site-wide mistake audit (owner request). Idempotent.
- testimonials: star-rating number "4.9" removed (owner rule: no rating numbers)
- broken characters (Ã— / Ã·) and double-escaped ampersands (&amp;amp;)
- bank profit rate 15%/30% -> 20%/40% (Section 7B / Division IIIA; ATL vs non-ATL), only where the sentence is about bank profit
- TY2026 deadline pages: 31 October 2026 (extended by FBR) instead of 30 September; countdown now ends on 31 Oct and points late filers to Form ATL-U
- pages with a stray </footer> and no footer: old address lines removed, the standard footer added"""
import glob, json, re, sys
sys.path.insert(0, '/home/user/kam/content/ui-2026')
from apply import FOOTER

ROOT = '/home/user/kam/'
SKIP = ('content/', 'content-batches/', 'reports/', 'seo_output/', 'searchops-team/', 'outreach/', 'project-history/', 'gsc_', 'schema/', 'node_modules/', 'assets/', 'digital/')
changed = set()


def edit(f, fn):
    p = ROOT + f
    t = open(p, encoding='utf-8').read()
    u = fn(t)
    if u != t:
        open(p, 'w', encoding='utf-8').write(u)
        changed.add(f)


# 1. rating number on testimonials
def testi(t):
    t = re.sub(r'\s*<span style="color:#fff;font-weight:700;font-size:1\.2rem">4\.9</span>', '', t)
    return t.replace('<div class="pb-score">4.9 &middot; 5,000+ clients</div>', '<div class="pb-score">5,000+ clients</div>').replace('<div class="pb-score">4.9 · 5,000+ clients</div>', '<div class="pb-score">5,000+ clients</div>')
edit('testimonials.html', testi)

files = [f[len(ROOT):] for f in glob.glob(ROOT + '**/*.html', recursive=True) if not f[len(ROOT):].startswith(SKIP)]
BANK = re.compile(r'(bank profit[^.%]{0,80}?)15%((?:\s|<[^>]+>)*(?:for filers|vs\.?|\(filers?\))[^%]{0,50}?)30%', re.I)
for f in files:
    def fx(t):
        t = t.replace('Ã—', '×').replace('Ã·', '÷').replace('&amp;amp;', '&amp;')
        t = BANK.sub(lambda m: m.group(1) + '20%' + m.group(2) + '40%', t)
        return t
    edit(f, fx)

# 2. TY2026 deadline pages
COUNT_OLD_TXT = 'Filing abhi shuru karo, last-week rush aur IRIS slowdown se bacho.'
COUNT_NEW_TXT = 'Deadline guzar gayi: ab late return file karein aur <a href="/blogs/form-atl-u-fbr-guide-2026" style="color:#5EEAD4;font-weight:600">Form ATL-U</a> se ATL mein wapas aayein.'
def deadline(t):
    t = t.replace("new Date('2026-09-30T23:59:59+05:00')", "new Date('2026-10-31T23:59:59+05:00')")
    t = t.replace('30 September 2026 — Individual/AOP Deadline', '31 October 2026 — TY2026 deadline (extended by FBR)')
    t = t.replace(COUNT_OLD_TXT, COUNT_NEW_TXT)
    t = t.replace('Salam%2C%20deadline%20se%20pehle%20apni%20return%20file%20karwani%20hai', 'Salam%2C%20apni%20late%20return%20file%20karwani%20hai')
    return t
for f in ('blogs/fbr-income-tax-return-deadline-2026-pakistan.html', 'blogs/income-tax-return-deadline-pakistan-2026.html'):
    edit(f, deadline)

def deadline_main(t):
    t = t.replace('is <strong>September 30, 2026</strong> for salaried individuals and AOPs.',
                  'was <strong>31 October 2026</strong> for individuals and AOPs, after FBR extended the usual 30 September due date; that date has now passed.')
    t = t.replace('September 30, 2026 for individuals and AOPs;', '31 October 2026 for individuals and AOPs (extended by FBR from 30 September; now passed);')
    t = t.replace('Yes &mdash; deadline September 30, 2026', 'Yes &mdash; deadline was 31 October 2026 (late now)')
    head, sep, rest = t.partition('</head>')
    def rep(m):
        before = rest[max(0, m.start() - 160):m.start()]
        if re.search(r'Employers|Withholding Agents|extend the|Form 24|Form 149', before):
            return m.group(0)
        return '31 October 2026'
    rest = re.sub(r'September 30, 2026', rep, rest)
    return head + sep + rest
edit('blogs/fbr-income-tax-return-deadline-2026-pakistan.html', deadline_main)

def finance(t):
    return t.replace('Companies and AOPs typically have until December 31, 2026.',
                     'Companies typically have until December 31, 2026. For Tax Year 2026 FBR extended the individual and AOP date to 31 October 2026.')
edit('blogs/finance-act-2026-pakistan-tax-changes.html', finance)

# 3. stray </footer> pages
NAP = re.compile(r'<p class="ka-nap"[^>]*>.*?</p>', re.S)
for f in files:
    p = ROOT + f
    t = open(p, encoding='utf-8').read()
    if 'class="ka-footer"' in t or '</footer>' not in t or re.search(r'<footer\b', t):
        continue
    u = NAP.sub('', t).replace('</footer>', '', 1)
    i = u.find('<div class="ka-mbar"')
    if i < 0:
        i = u.rfind('</body>')
    u = u[:i] + FOOTER + u[i:]
    open(p, 'w', encoding='utf-8').write(u)
    changed.add(f)

print('pages changed', len(changed))
