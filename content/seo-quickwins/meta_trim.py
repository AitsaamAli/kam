"""Trim meta descriptions longer than 160 characters to at most 155, at a sentence or clause boundary (owner request, Nov 2026).
og:description and twitter:description are updated only where they equal the old description. Idempotent."""
import glob, html, re, sys

SKIP = ('content/', 'content-batches/', 'reports/', 'seo_output/', 'searchops-team/', 'outreach/', 'project-history/', 'gsc_', 'schema/', 'node_modules/', 'assets/', '__', 'news/_TEMPLATE')
MAX = 155


BOILER = re.compile(r"\s*(?:Expert FBR tax help\s*[—-]\s*Kamboh Associa.*|Complete (?:FBR )?guide\s*[—-]\s*Kamboh Associates\.?|[—-]?\s*complete FBR guide\.?|By Kamboh Associates.*|[—-]\s*Kamboh Associates[^.]*\.?|WhatsApp:?\s*0328-?4675162\.?|Starting Rs\.?\s?[\d,]+\.?|Full online process\.?|[—-]\s*guide\.?)\s*$", re.I)


STOP = {'as', 'the', 'and', 'of', 'for', 'to', 'with', 'in', 'on', 'by', 'a', 'an', 'or', 'from', 'at', 'is', 'are', 'how', 'why',
        'what', 'kaise', 'aur', 'ke', 'ki', 'ka', 'ko', 'se', 'mein', 'par', 'jo', 'which', 'that', 'your', 'their', 'its'}


def tidy(x):
    words = x.rstrip(' ,;:—-.').split(' ')
    while len(words) > 3 and words[-1].lower().strip(',;:') in STOP:
        words.pop()
    return ' '.join(words).rstrip(' ,;:—-') + '.'


def trim(d):
    if len(d) <= 160:
        return d
    x = d
    for _ in range(3):
        y = BOILER.sub('', x).rstrip(' ,;:—-')
        if y == x:
            break
        x = y if y.endswith(('.', '?', '!')) else y + '.'
        if len(x) <= MAX:
            return x
    # whole sentences that fit
    out = ''
    for s in re.split(r'(?<=[.!?])\s+', x):
        cand = (out + ' ' + s).strip()
        if len(cand) <= MAX:
            out = cand
        else:
            break
    if len(out) >= 110:
        return out
    # clause boundary between 110 and MAX characters, preferring stronger separators
    base = x[:MAX]
    for sep in ['; ', ' — ', ' - ', ', and ', ' and ', ', ']:
        k = base.rfind(sep)
        if k >= 110:
            return tidy(base[:k])
    k = base.rfind(' ')
    return tidy(base[:k])


def main(dry):
    n = 0
    for f in sorted(glob.glob('**/*.html', recursive=True)):
        if f.startswith(SKIP):
            continue
        t = open(f, encoding='utf-8').read()
        m = re.search(r'<meta name="description" content="([^"]*)"', t)
        if not m:
            continue
        raw = m.group(1)
        d = html.unescape(raw)
        nd = trim(d)
        if nd == d:
            continue
        nraw = html.escape(nd, quote=True)
        n += 1
        if dry:
            print(f'{f}\n  OLD({len(d)}): {d}\n  NEW({len(nd)}): {nd}')
            continue
        t = t.replace(f'<meta name="description" content="{raw}"', f'<meta name="description" content="{nraw}"', 1)
        for p in ('property="og:description"', 'name="twitter:description"'):
            t = t.replace(f'<meta {p} content="{raw}"', f'<meta {p} content="{nraw}"')
        open(f, 'w', encoding='utf-8').write(t)
    print('descriptions trimmed', n)


if __name__ == '__main__':
    main('--dry' in sys.argv)
