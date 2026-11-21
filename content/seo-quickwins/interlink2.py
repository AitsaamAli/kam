"""Second pass for weak tax pages that interlink.py could not place (owner request, Nov 2026).
interlink.py matches on slug words, so pages whose slug words are unique (small cities, niche topics) got no host.
This pass matches on page text (title, H1, opening text) and, for city pages, prefers hosts in the same province.
Each weak page gets up to two 'Related guides' links; a host carries at most 4 added links in total. Idempotent."""
import collections, glob, html, json, re

ROOT = '/home/user/kam/'
SKIP = ('content/', 'content-batches/', 'reports/', 'seo_output/', 'searchops-team/', 'outreach/', 'project-history/', 'gsc_', 'schema/',
        'node_modules/', 'assets/', 'digital/', '__', 'news/_TEMPLATE')
NOT_HOST = {'index.html', 'blogs.html', 'pricing.html', 'contact.html', 'about.html', 'privacy.html', 'terms.html', 'disclaimer.html', '404.html', 'testimonials.html'}
STOP = set(('the and for in of a to vs is are with your on how what kya kaise karein ke ki ka mein par se aur hai hain ko jo bhi ye yeh tax pakistan fbr 2026 '
            '2027 2025 guide consultant consultants best near service services online filing file return returns income kamboh associates lahore '
            'this that from you our we can will be or as at by an it its not if get all more which when who has have do does').split())
PROV = {'punjab': 'punjab', 'sindh': 'sindh', 'khyber': 'kp', 'pakhtunkhwa': 'kp', 'kpk': 'kp', 'balochistan': 'balochistan',
        'gilgit': 'gb', 'baltistan': 'gb', 'azad': 'ajk', 'ajk': 'ajk'}
red = {r['source'] for r in json.load(open(ROOT + 'vercel.json'))['redirects']}


def url(f):
    u = '/' + f[:-5]
    if u.endswith('/index'):
        u = u[:-6] or '/'
    return u


def plain(t):
    m = re.search(r'<article\b.*?</article>', t, re.S) or re.search(r'<main\b.*?</main>', t, re.S)
    b = m.group(0) if m else t
    b = re.sub(r'<(script|style)\b.*?</\1>', ' ', b, flags=re.S)
    return html.unescape(re.sub(r'<[^>]+>', ' ', b))


def feats(t):
    title = re.search(r'<title>(.*?)</title>', t, re.S)
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', t, re.S)
    head = ' '.join(x.group(1) for x in (title, h1) if x)
    body = plain(t)[:2500]
    words = re.findall(r'[a-z][a-z0-9]+', html.unescape(re.sub(r'<[^>]+>', ' ', head + ' ' + head + ' ' + body)).lower())
    return {w for w in words if w not in STOP and len(w) > 2}


def province(t):
    c = collections.Counter()
    for w in re.findall(r'[a-z]+', plain(t).lower()):
        if w in PROV:
            c[PROV[w]] += 1
    return c.most_common(1)[0][0] if c else None


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

weak = sorted(f for f in pages if f not in NOT_HOST and url(f) != '/' and not inbound[url(f)])
hosts = [f for f in pages if f not in NOT_HOST]
F = {f: feats(pages[f]) for f in pages}
P = {f: province(pages[f]) for f in pages}
TXT = {f: ' ' + re.sub(r'[^a-z]+', ' ', plain(pages[f]).lower()) + ' ' for f in pages}
used = collections.Counter({h: len(re.findall(r'<li><a href=', m.group(0)))
                            for h in hosts for m in [re.search(r'<ul class="ka-related-list">.*?</ul>', pages[h], re.S)] if m})
plan = collections.defaultdict(list)
GENERIC = {'hub', 'tank', 'topi', 'moro', 'kotri'}  # town names that are also common words
SUBAREA = re.compile(r'\S \S*\s*(lahore|islamabad|rawalpindi|karachi|multan|peshawar|quetta) $')
# towns whose pages name no neighbour: their district or nearest district pages
NEAR = {'malikwal': ['mandi-bahauddin', 'phalia'], 'nankana-sahib': ['sheikhupura', 'lahore']}  # neighbourhood pages, not towns


def is_city(f):
    b = f.split('/')[-1]
    return b.startswith('tax-consultant-') and not b.endswith('-pakistan.html')


def town(f):
    return ' ' + f.split('/')[-1][len('tax-consultant-'):-5].replace('-', ' ') + ' '


for f in weak:
    city = is_city(f)
    cands = []
    for h in hosts:
        if h == f or used[h] >= 4 or h in weak or is_city(h) != city:
            continue
        if 'sales-tax' in h or (city and SUBAREA.search(town(h))):
            continue
        inter = len(F[f] & F[h])
        score = inter / len(F[f] | F[h]) if inter else 0
        if city:
            # nearby towns named on either page are the strongest local signal; otherwise same province
            hits = (0 if town(h).strip() in GENERIC else TXT[f].count(town(h))) + (0 if town(f).strip() in GENERIC else TXT[h].count(town(f)))
            near = NEAR.get(town(f).strip().replace(' ', '-'), [])
            if town(h).strip().replace(' ', '-') in near:
                hits += 5
            if hits:
                score += hits
            elif not (P[f] and P[f] == P[h]):
                continue
        elif not inter:
            continue
        cands.append((score, h))
    cands.sort(reverse=True)
    for _, h in cands[:2]:
        plan[h].append(f)
        used[h] += 1


def label(t):
    m = re.search(r'<h1[^>]*>(.*?)</h1>', t, re.S) or re.search(r'<title>(.*?)</title>', t, re.S)
    x = html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip()
    x = re.split(r'\s+[|]\s+', x)[0]
    return x if len(x) <= 90 else x[:87].rsplit(' ', 1)[0] + '…'


n = 0
for h, targets in plan.items():
    t = pages[h]
    body = re.sub(r'<nav\b.*?</nav>|<footer\b.*?</footer>', ' ', t, flags=re.S)
    have = set(re.findall(r'href="(/[^"#?]*)"', body))
    items = [f for f in targets if url(f) not in have and 'sales-tax' not in f]
    if not items:
        continue
    lis = ''.join(f'<li><a href="{url(f)}">{html.escape(label(pages[f]))}</a></li>' for f in items)
    if '<ul class="ka-related-list">' in t:
        t = t.replace('<ul class="ka-related-list">', '<ul class="ka-related-list">' + lis, 1)
    else:
        i = t.find('<footer class="ka-footer"')
        if i < 0:
            continue
        box = f'<aside class="ka-related" aria-label="Related guides"><p class="ka-related-h">Related guides</p><ul class="ka-related-list">{lis}</ul></aside>\n'
        t = t[:i] + '<div class="ka-related-wrap">' + box + '</div>' + t[i:]
    open(ROOT + h, 'w', encoding='utf-8').write(t)
    n += len(items)
left = [f for f in weak if not any(f in v for v in plan.values())]
print('weak pages', len(weak), 'links added', n, 'hosts', len(plan), 'still without host', len(left))
for f in left:
    print('  no host:', f, P[f])
