"""Adds the full NAP, office hours and Google Business Profile link to footers of tax pages that lack the address (Nov 2026).
Idempotent: skips footers that already contain 'Rizwan' or the ka-nap marker. /digital is left alone."""
import glob
NAP = ('<p class="ka-nap" style="font-size:.78rem;color:#94A3B8;margin:10px auto 0;max-width:900px;padding:0 16px;line-height:1.6;text-align:center">'
       'Kamboh Associates &middot; Shop No 34, Rizwan Block Market, opposite Rizwan Park, Awan Town, Lahore 54660 &middot; '
       '<a href="tel:+923284675162" style="color:#D4AF37">0328-4675162</a> &middot; Mon&ndash;Sat 9:00&ndash;18:00, Fri 9:00&ndash;12:30, Sun closed &middot; '
       '<a href="https://g.page/r/CYzrn3EEiZVwEBM" target="_blank" rel="noopener" style="color:#14B8A6">Google Business Profile</a></p>')
SKIP = ('content/', 'content-batches/', 'reports/', 'seo_output/', 'searchops-team/', 'outreach/', 'project-history/', 'gsc_', 'schema/', 'digital/', 'node_modules/')
n = 0
for f in glob.glob('**/*.html', recursive=True):
    if f.startswith(SKIP):
        continue
    t = open(f, encoding='utf-8').read()
    e = t.rfind('</footer>')
    if e < 0:
        continue
    s = t.rfind('<footer', 0, e)
    ft = t[s:e]
    if 'Rizwan' in ft or 'ka-nap' in ft:
        continue
    t = t[:e] + NAP + t[e:]
    open(f, 'w', encoding='utf-8').write(t)
    n += 1
print('footers updated', n)
