"""Give weakly linked tax pages two contextual inbound links (owner request, Nov 2026).
A page is weakly linked when no tax page other than the blog listing links to it. For each, the two most similar pages
(slug-word overlap, same topic family) get a 'Related guides' link at the end of their article. Idempotent; hosts get at most 4 added links."""
import collections, glob, html, json, re

ROOT = '/home/user/kam/'
SKIP = ('content/', 'content-batches/', 'reports/', 'seo_output/', 'searchops-team/', 'outreach/', 'project-history/', 'gsc_', 'schema/',
        'node_modules/', 'assets/', 'digital/', '__', 'news/_TEMPLATE')
NOT_HOST = {'index.html', 'blogs.html', 'pricing.html', 'contact.html', 'about.html', 'privacy.html', 'terms.html', 'disclaimer.html', '404.html', 'testimonials.html'}
STOP = set(('pakistan 2026 2027 2025 tax fbr the and for in of a to vs guide how what is are with your on blogs kya kaise karein ke ki ka mein par se aur '
             'consultant consultants best near me service services online filing file return returns income colony town road block phase city sector market '
             'complete step by new top lahore-areas').split())
red = {r['source'] for r in json.load(open(ROOT + 'vercel.json'))['redirects']}


def url(f):
    u = '/' + f[:-5]
    if u.endswith('/index'):
        u = u[:-6] or '/'
    return u


def toks(f):
    return {w for w in re.split(r'[-/]', f[:-5].replace('blogs/', '')) if w and w not in STOP and not w.isdigit()}


pages = {}
for p in glob.glob(ROOT + '**/*.html', recursive=True):
    f = p[len(ROOT):]
    if f.startswith(SKIP) or url(f) in red:
        continue
    t = open(p, encoding='utf-8').read()
    if re.search(r'<meta name="robots"[^>]*noindex', t):
        continue
    pages[f] = t

inbound = collections.defaultdict(set)
for f, t in pages.items():
    if f == 'blogs.html':
        continue
    body = re.sub(r'<nav\b.*?</nav>|<footer\b.*?</footer>', ' ', t, flags=re.S)
    for h in set(re.findall(r'href="(/[^"#?]*)"', body)):
        h = h.rstrip('/') or '/'
        if h != url(f):
            inbound[h].add(f)

weak = [f for f in pages if f not in NOT_HOST and url(f) != '/' and len(inbound[url(f)]) == 0]
hosts = [f for f in pages if f not in NOT_HOST]
added = collections.Counter()
plan = collections.defaultdict(list)
for f in sorted(weak):
    tf = toks(f)
    if not tf:
        continue
    cands = []
    for h in hosts:
        if h == f or added[h] >= 4:
            continue
        th = toks(h)
        inter = len(tf & th)
        if not inter:
            continue
        score = inter / len(tf | th) + (0.05 if h.startswith('blogs/') == f.startswith('blogs/') else 0)
        cands.append((score, h))
    cands.sort(reverse=True)
    for _, h in cands[:2]:
        plan[h].append(f)
        added[h] += 1


def label(t):
    m = re.search(r'<h1[^>]*>(.*?)</h1>', t, re.S) or re.search(r'<title>(.*?)</title>', t, re.S)
    x = html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip()
    x = re.split(r'\s+[|]\s+', x)[0]
    return x if len(x) <= 90 else x[:87].rsplit(' ', 1)[0] + '…'


n = 0
for h, targets in plan.items():
    t = pages[h]
    have = set(re.findall(r'href="(/[^"#?]*)"', t))
    items = [f for f in targets if url(f) not in have]
    if not items:
        continue
    lis = ''.join(f'<li><a href="{url(f)}">{html.escape(label(pages[f]))}</a></li>' for f in items)
    if '<ul class="ka-related-list">' in t:
        t = t.replace('<ul class="ka-related-list">', '<ul class="ka-related-list">' + lis, 1)
    else:
        box = f'<aside class="ka-related" aria-label="Related guides"><p class="ka-related-h">Related guides</p><ul class="ka-related-list">{lis}</ul></aside>\n'
        i = t.find('<footer class="ka-footer"')
        if i < 0:
            continue
        # place it before the closing of the main content: just before the footer, inside a container
        t = t[:i] + '<div class="ka-related-wrap">' + box + '</div>' + t[i:]
    open(ROOT + h, 'w', encoding='utf-8').write(t)
    n += len(items)
print('weak pages', len(weak), 'links added', n, 'hosts', len(plan))
