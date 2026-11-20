"""Country / visa guides: make clear that Kamboh Associates provides tax services only, not visa services (owner request 20 Nov 2026).
Adds a notice near the top of the article and one line before the closing call-to-action. Idempotent.
Pages: tax pages whose visible text mentions "visa" three or more times. No titles, meta, H1s or URLs change."""
import glob, html, re

TOP = ('<div class="ka-visa-note" role="note"><i class="fas fa-circle-info" aria-hidden="true"></i><div>'
       '<strong>Please note: we provide tax services only.</strong> Kamboh Associates prepares NTN registration, income tax returns, '
       'wealth statements and FBR records that visa applicants often need. We do <strong>not</strong> provide visa, immigration or travel '
       'services, and we cannot apply for, arrange or guarantee any visa. For visa requirements, contact the embassy or its official visa centre.'
       '<span class="ka-visa-ur">Hum sirf tax ka kaam karte hain (NTN, tax return, wealth statement). Visa, immigration ya travel ki koi service nahi dete.</span>'
       '</div></div>\n')
BOTTOM = ('<p class="ka-visa-line"><i class="fas fa-circle-info" aria-hidden="true"></i> Tax services only: we prepare your FBR documents; '
          'we do not apply for or arrange visas.</p>\n')
SKIP = ('content/', 'digital/', 'assets/')


def visa_count(t):
    body = re.sub(r'<script.*?</script>|<style.*?</style>', '', t, flags=re.S)
    return len(re.findall(r'\bvisa\b', html.unescape(re.sub(r'<[^>]+>', ' ', body)), re.I))


def apply(f):
    t = open(f, encoding='utf-8').read()
    if 'ka-visa-note' in t or visa_count(t) < 3:
        return False
    # top: before the "On this page" box, else before the first H2 of the article
    i = t.find('<details class="ka-toc"')
    if i < 0:
        a = -1
        for mark in ('class="article-body', 'class="article', 'class="ar"', '<article'):
            a = t.find(mark)
            if a > -1:
                break
        i = t.find('<h2', a) if a > -1 else -1
    if i < 0:
        return False
    t = t[:i] + TOP + t[i:]
    # bottom: before the last call-to-action box in the article
    j = max(t.rfind('<div class="ct">'), t.rfind('<div class="cta-box'), t.rfind('<div class="article-cta'))
    if j > i:
        t = t[:j] + BOTTOM + t[j:]
    open(f, 'w', encoding='utf-8').write(t)
    return True


if __name__ == '__main__':
    files = [f for f in glob.glob('**/*.html', recursive=True) if not f.startswith(SKIP)]
    print('pages', sum(apply(f) for f in files))
