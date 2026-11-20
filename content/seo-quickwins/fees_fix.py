"""Align every fee claim with the fees published on /pricing (owner request, 20 Nov 2026). Idempotent.
Published: NTN Rs 2,000 (individual or business); salaried/pensioner return Rs 3,500; freelancer or sole proprietor return Rs 5,000;
overseas return Rs 6,000; AOP Rs 8,000; company return from Rs 18,000; company registration from Rs 15,000; wealth statement Rs 2,000;
Form ATL-U Rs 2,000; STRN Rs 3,000; notice reply from Rs 5,000. Anything not published becomes "fixed fee confirmed before work starts".
Service-page price tiers (fbr-notice-defense, corporate-tax-consultant-lahore) are left to the owner.
Only body text, FAQ text and JSON-LD answer text change; no titles, meta descriptions, H1s or URLs."""
import glob, re

RS = r'Rs\.?\s?'
FIX = 'Fixed fee, confirmed first'
RULES = [
    (rf'charges {RS}2,500\s?(?:[–-]|&ndash;)\s?5,000 for simple salaried (?:employee )?returns', 'charges Rs 3,500 for a salaried return and Rs 5,000 for a business or freelancer return'),
    (rf'([Ww]ealth statement,? ){RS}2,500', r'\1Rs 2,000'),
    (rf'Business owners from {RS}7,000, Property investors with wealth statement from {RS}8,000', 'Business owners and freelancers from Rs 5,000, wealth statement Rs 2,000'),
    (rf'{RS}3,000\s?(?:[–-]|&ndash;)\s?5,000 mein complete return service', 'Rs 3,500 mein complete return service'),
    (rf'{RS}2,500 for business/AOP NTN', 'Rs 2,000 for business/AOP NTN'),
    (rf'(Business / AOP / Partnership</div>\s*<div[^>]*>){RS}2,500', r'\1Rs. 2,000'),
    (rf'{RS}2,000 for individuals, {RS}3,000 for businesses', 'Rs. 2,000 for individuals and businesses'),
    (r'<td>Rs\. 1,500&ndash;3,000</td>', '<td>Rs. 2,000</td>'),
    (r'<td>Rs\. 2,000&ndash;4,000</td>', '<td>Rs. 2,000</td>'),
    (r'<td>Rs\. 3,000&ndash;6,000</td>', '<td>Rs. 2,000</td>'),
    (r'<td>Rs\. 4,000&ndash;8,000</td>', f'<td>{FIX}</td>'),
    (rf"Standalone NTN for existing company: {RS}4,000\s?(?:[–-]|&ndash;)\s?8,000 consultant fee\.", 'Standalone NTN for an existing company: a fixed fee confirmed before work starts.'),
    (rf'(<td>Company NTN</td><td>SECP registered companies</td><td>){RS}3,500', r'\1Rs. 2,000'),
    (rf'(<td>Company NTN</td><td>){RS}2,500', r'\1Rs. 2,000'),
    (rf'(<td>NTN Registration \(Company\)</td><td>){RS}3,000', r'\1Rs 2,000'),
    (rf'(<td>Bank Account Opening Assistance</td><td>){RS}2,000', r'\1Included with registration'),
    (r'(<td>Annual SECP Filing \(Ongoing\)</td><td>)[^<]*', rf'\1{FIX}'),
    (rf'for {RS}2,500, using CNIC', 'for Rs 2,000, using CNIC'),
    (rf'Kamboh Associates charges {RS}2,500, with the certificate', 'Kamboh Associates charges Rs 2,000, with the certificate'),
    (rf'\(starting from {RS}2,500\)', '(Rs 2,000, as published on our pricing page)'),
    (rf'for {RS}3,000 \(STRN\) or {RS}4,000 \(SRB\)', 'for Rs 3,000 (STRN), with SRB at a fixed fee confirmed before work starts'),
    (rf'charges {RS}3,000 for FBR STRN, {RS}4,000 for SRB registration, or {RS}6,000 for combined registration if your business needs both',
     'charges Rs 3,000 for FBR STRN; SRB or combined registration, if your business needs both, is a fixed fee confirmed before work starts'),
    (rf'review available for {RS}4,000 if', 'review available at a fixed fee confirmed before work starts if'),
    (rf'available separately for {RS}2,500 if', 'available separately at a fixed fee confirmed before work starts if'),
    (rf'a monthly retainer starting from {RS}12,000 covers', 'a monthly retainer, at a fixed fee confirmed before work starts, covers'),
    (rf'Retainers start from {RS}12,000/month depending on company complexity', 'Retainers are a fixed monthly fee confirmed before work starts, depending on company complexity'),
    (rf'prepares legal objections to Section 122 notices at {RS}12,000\.', 'prepares legal objections to Section 122 notices; notice replies start from Rs 5,000 (published fee), and the final fee is confirmed before work starts.'),
    (r'(<td>Salary Slip Tax Review \(Exemptions Check\)</td><td>)[^<]*', rf'\1{FIX}'),
    (r'(<td>Employer Withholding Discrepancy Resolution</td><td>)[^<]*', rf'\1{FIX}'),
    (r'(<td>Quarterly Advance Tax Estimate &amp; PSID</td><td>)[^<]*', rf'\1{FIX}'),
    (r'(<td>Annual Advance Tax Planning \(4 Quarters\)</td><td>)[^<]*', rf'\1{FIX}'),
    (r'(<td>Underpayment Surcharge Resolution</td><td>)[^<]*', rf'\1{FIX}'),
    (r'(<td>Rent Agreement Review &amp; WHT Setup</td><td>)[^<]*', rf'\1{FIX}'),
    (r'(<td>Rental Income Return Filing</td><td>)[^<]*', r'\1From Rs 3,500'),
]
SKIP = ('content/', 'content-batches/', 'reports/', 'seo_output/', 'searchops-team/', 'outreach/', 'project-history/', 'gsc_', 'schema/', 'digital/', 'node_modules/', 'assets/')
HEAD_RE = re.compile(r'(<title>.*?</title>|<meta name="description"[^>]*>|<meta property="og:[^>]*>|<meta name="twitter:[^>]*>|<h1[^>]*>.*?</h1>)', re.S)

if __name__ == '__main__':
    tot = 0; pages = 0
    for f in glob.glob('**/*.html', recursive=True):
        if f.startswith(SKIP) or f in ('pricing.html', 'corporate-tax-consultant-lahore.html', 'fbr-notice-defense.html'):
            continue
        t = open(f, encoding='utf-8').read()
        # protect titles, meta and H1 from any change
        keep = {}
        def stash(m):
            k = f'\x00{len(keep)}\x00'; keep[k] = m.group(0); return k
        u = HEAD_RE.sub(stash, t)
        n = 0
        for pat, rep in RULES:
            u, c = re.subn(pat, rep, u); n += c
        for k, v in keep.items():
            u = u.replace(k, v)
        if n:
            open(f, 'w', encoding='utf-8').write(u); tot += n; pages += 1
    print('replacements', tot, 'pages', pages)
