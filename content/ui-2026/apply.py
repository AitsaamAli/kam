"""Design refresh, phase 1-2 (owner approved 20 Nov 2026). Idempotent. Tax pages only; /digital untouched.
- one top menu on every page (Web Development kept only on the homepage, owner's decision)
- still trust strip instead of the scrolling ticker
- one action bar on phones (floating circles hidden there by /assets/ka-ui.js + css)
- "On this page" table of contents on guides, "Short answer" label instead of "TL;DR"
- shared /assets/ka-ui.css and /assets/ka-ui.js
No titles, meta descriptions, canonicals, robots tags, H1s or URLs are changed."""
import glob, html, re, sys

V = "3"
CSS = f'<link rel="stylesheet" href="/assets/ka-ui.css?v={V}"/>'
JS = f'<script src="/assets/ka-ui.js?v={V}" defer></script>'
SKIP = ('content/', 'content-batches/', 'reports/', 'seo_output/', 'searchops-team/', 'outreach/', 'project-history/',
        'gsc_', 'schema/', 'digital/', 'node_modules/', 'assets/')

def A(href, icon, label):
    return f'<a href="{href}"><i class="fas {icon}"></i> {label}</a>'
DIV = '<div class="nav-drop-divider"></div>'

def services(home=False):
    items = [A("/income-tax-filing", "fa-file-invoice-dollar", "Income Tax Filing"),
             A("/ntn-registration", "fa-id-card", "NTN Registration"),
             A("/blogs/sole-proprietor-tax-services-fees-pakistan", "fa-user-tie", "Sole Proprietor Services"),
             A("/dnfbp-compliance-services", "fa-shield-halved", "DNFBP &amp; AML Compliance"),
             A("/secp-vs-sole-proprietorship-pakistan", "fa-building", "SECP Company Registration"), DIV,
             A("/wealth-statement", "fa-wallet", "Wealth Statement"),
             A("/fbr-notice-defense", "fa-shield-alt", "FBR Notice Defense"),
             A("/aop-tax-return", "fa-handshake", "AOP Tax Return"),
             A("/corporate-tax-return", "fa-building-columns", "Corporate Tax Return"),
             A("/withholding-tax", "fa-hand-holding-usd", "Withholding Tax"),
             A("/sales-tax-registration", "fa-percent", "Sales Tax Registration"),
             A("/sales-tax-return", "fa-file-alt", "Sales Tax Return"),
             A("/eobi-registration", "fa-users", "EOBI Registration"),
             A("/tax-exemption-certificate", "fa-certificate", "Tax Exemption Cert"),
             A("/import-export-registration", "fa-ship", "Import / Export"), DIV,
             A("/business-advisory", "fa-chart-line", "Business Advisory")]
    if home:
        items += [DIV, A("/digital", "fa-globe", "Web Development")]
    items += [DIV, A("/pricing", "fa-tags", "Pricing &amp; Fees"), A("/testimonials", "fa-comment-dots", "Client Reviews")]
    return "".join(items)

def tools(home=False):
    return "".join([A("/tools", "fa-toolbox", "All Calculators"),
                    A("/tools/late-filing-penalty-calculator", "fa-hourglass-half", "Late Filing Penalty"),
                    A("/tax-calculator", "fa-calculator", "Tax Calculator"),
                    A("/salary-calculator", "fa-user-tie", "Salary Calculator"),
                    A("/gst-calculator", "fa-percent", "GST Calculator"),
                    A("/income-estimator", "fa-chart-bar", "Income Estimator"), DIV,
                    A("#deadlines" if home else "/#deadlines", "fa-calendar-days", "Tax Deadlines")])

BLOG = "".join([A("/blogs", "fa-newspaper", "All Articles"),
                A("/income-tax-filing-guide-pakistan", "fa-file-invoice-dollar", "Income Tax Filing Guide"),
                A("/property-tax-guide-pakistan", "fa-building", "Property Tax Guide"),
                A("/fbr-notice-guide-pakistan", "fa-shield-alt", "FBR Notice &amp; Audit Guide"),
                A("/freelancer-overseas-tax-guide-pakistan", "fa-globe", "Freelancer &amp; Overseas Guide"),
                A("/sales-tax-guide-pakistan", "fa-receipt", "Sales Tax &amp; STRN Guide")])
CHEV = ' <i class="fas fa-chevron-down nav-chevron"></i>'

def nav(home=False):
    act = ' class="active"' if home else ''
    li = [f'<li><a href="{"#home" if home else "/"}"{act}>Home</a></li>',
          f'<li><a href="{"#services" if home else "/income-tax-filing"}">Services{CHEV}</a><div class="nav-drop">{services(home)}</div></li>']
    if home:
        li.append('<li><a href="/digital">Web Development</a></li>')
    li += [f'<li><a href="/tools">Tools{CHEV}</a><div class="nav-drop">{tools(home)}</div></li>',
           '<li><a href="/pricing">Pricing</a></li>',
           f'<li><a href="/blogs">Blog{CHEV}</a><div class="nav-drop">{BLOG}</div></li>',
           '<li><a href="/contact">Contact</a></li>']
    return '<ul class="nav-links" data-ka="nav1">' + "".join(li) + '</ul>'

MINI = ('<nav class="ka-mini-nav" aria-label="Main menu"><ul><li><a href="/">Home</a></li><li><a href="/#services">Services</a></li>'
        '<li><a href="/tools">Tools</a></li><li><a href="/pricing">Pricing</a></li><li><a href="/blogs">Blog</a></li>'
        '<li><a href="/contact">Contact</a></li></ul></nav>')
STRIP = ('<div class="ka-strip"><span><b>FBR Registered</b></span>'
         '<span class="ka-s-addr">Shop 34, Rizwan Block Market, Awan Town, Lahore</span>'
         '<span class="ka-s-hours">Mon&ndash;Sat 9:00&ndash;18:00 &middot; Fri 9:00&ndash;12:30</span>'
         '<span><a href="tel:+923284675162">0328-4675162</a></span></div>')
MBAR = ('<div class="ka-mbar" role="region" aria-label="Contact Kamboh Associates">'
        '<a class="ka-call" href="tel:+923284675162"><i class="fas fa-phone" aria-hidden="true"></i> Call</a>'
        '<a class="ka-wa" href="https://wa.me/923284675162" target="_blank" rel="noopener"><i class="fab fa-whatsapp" aria-hidden="true"></i> WhatsApp</a></div>')

UL_RE = re.compile(r'<ul class="nav-links"[^>]*>.*?</ul>(?=\s*(?:<div|</div|<button|<a))', re.S)
NL_RE = re.compile(r'<ul class="nl">.*?</ul>(?=<div class="na">)', re.S)
TP_RE = re.compile(r'<div class="(?:tbi|topbar-inner)">(?:\s*<span class="tp"[^>]*>.*?</span>)+\s*</div>', re.S)
TICK_RE = re.compile(r'<div class="topbar-promo-wrap">(?:\s*<span[^>]*>.*?</span>)+\s*</div>', re.S)
H2_RE = re.compile(r'<h2\b([^>]*)\bid="([^"]+)"([^>]*)>(.*?)</h2>', re.S)
ENDS = ('<aside', 'class="sidebar', '<section class="cta-strip"', '<footer', 'class="related-posts', 'class="blog-sidebar')


def toc(t):
    if 'class="ka-toc"' in t:
        return t
    start = -1
    for mark in ('class="article-body', 'class="article', 'class="prose', '<article'):
        start = t.find(mark)
        if start > -1:
            break
    if start < 0:
        return t
    end = len(t)
    for m in ENDS:
        k = t.find(m, start + 10)
        if -1 < k < end:
            end = k
    hs = [m for m in H2_RE.finditer(t, start, end)]
    rows = []
    for m in hs:
        txt = re.sub(r'<[^>]+>', '', m.group(4))
        txt = re.sub(r'\s+', ' ', html.unescape(txt)).strip()
        if not txt or len(txt) > 110:
            continue
        rows.append((m.group(2), txt))
    if len(rows) < 4:
        return t
    lis = "".join(f'<li><a href="#{html.escape(i, quote=True)}">{html.escape(x)}</a></li>' for i, x in rows)
    box = f'<details class="ka-toc" open><summary>On this page</summary><ol>{lis}</ol></details>\n'
    pos = hs[0].start()
    return t[:pos] + box + t[pos:]


def apply(f):
    t = open(f, encoding='utf-8').read()
    o = t
    home = f == 'index.html'
    # menu
    if 'data-ka="nav1"' not in t:
        if UL_RE.search(t):
            t = UL_RE.sub(lambda m: nav(home), t, count=1)
        elif NL_RE.search(t):
            t = NL_RE.sub(lambda m: nav(False).replace('class="nav-links"', 'class="nl"'), t, count=1)
        elif '<nav class="navbar' in t and 'ka-mini-nav' not in t:
            k = t.find('</nav>', t.find('<nav class="navbar'))
            if k > -1:
                t = t[:k + 6] + MINI + t[k + 6:]
    # ticker -> still strip
    t = TICK_RE.sub(STRIP, t, count=1)
    t = TP_RE.sub(STRIP, t, count=1)
    # label
    t = t.replace('>TL;DR</div>', '>Short answer</div>').replace('>TL;DR</span>', '>Short answer</span>')
    # guides: table of contents
    if f.startswith('blogs/') or re.search(r'class="(?:article-body|article|prose)[ "]', t):
        if not home and f not in ('blogs.html',):
            t = toc(t)
    # shared assets + phone bar
    if CSS not in t and '</head>' in t:
        t = t.replace('</head>', CSS + '\n</head>', 1)
    if JS not in t and '</body>' in t:
        bar = '' if ('mobile-cta-bar' in t or 'class="ka-mbar"' in t) else MBAR
        i = t.rfind('</body>')
        t = t[:i] + bar + JS + '\n' + t[i:]
    if t != o:
        open(f, 'w', encoding='utf-8').write(t)
        return True
    return False


if __name__ == '__main__':
    files = sys.argv[1:] or [f for f in glob.glob('**/*.html', recursive=True) if not f.startswith(SKIP)]
    n = sum(apply(f) for f in files)
    print('pages changed', n, 'of', len(files))
