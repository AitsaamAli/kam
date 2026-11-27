"""27 Nov 2026 fact fix, part 3.
Deadline: the TY2026 statutory due date was 30 September 2026; FBR extended it to 31 October 2026, which has passed (owner-confirmed,
CLAUDE.md). Current-tense mentions of 30 September 2026 as the deadline become '31 October 2026 (extended from 30 September 2026)';
'statutory'/'original'/'missed' mentions and dated news posts keep the date. Pages get a short dated update note.
7E: omitted by the Finance Act 2026 (ITO amended to 30.06.2026, footnote to s.7E). Pages that describe 7E without saying so get a note.
Idempotent (marker ka-update)."""
import glob, json, re
R = "/home/user/kam/"
ITO = "https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf"
L = 'style="color:#B45309;font-weight:600;text-decoration:underline"'
red = {r["source"] for r in json.load(open(R + "vercel.json"))["redirects"]}
EX = ("content", "outreach", "reports", "seo_output", "searchops-team", "project-history", "schema", "content-batches", "digital")
SKIP7 = {"blogs/section-7e-abolished-fcc-ruling-2026-pakistan.html"}
BOX = ('<div class="ka-update" style="background:#FFFBEB;border:1px solid #F59E0B;border-radius:10px;padding:10px 14px;margin:12px 0 18px;'
       'color:#1E293B;font-size:.9rem;line-height:1.6"><strong>Update, 27 November 2026:</strong> {}</div>\n')
D_MSG = (f'FBR extended the Tax Year 2026 deadline from 30 September to 31 October 2026, and it has passed. You can still file late: '
         f'<a href="/blogs/tax-return-deadline-passed-31-october-2026-next-steps" {L}>next steps</a>, '
         f'<a href="/blogs/late-filing-penalty-income-tax-pakistan" {L}>section 182 penalty</a>.')
E_MSG = (f'Section 7E (deemed income on property) was omitted by the Finance Act 2026 (<a href="{ITO}" {L} target="_blank" rel="noopener">ITO to 30 June 2026</a>); '
         f'7E below refers to the earlier law. <a href="/blogs/section-7e-abolished-fcc-ruling-2026-pakistan" {L}>7E after 2026</a>.')
DATE = re.compile(r"(30 September 2026|September 30, 2026)")
KEEP = re.compile(r"statutory|Statutory|original|missed|Missed|extended|extension", re.I)


def text(t):
    return re.sub(r"<[^>]+>", " ", t)


def place(t, box):
    for pat in (r'<p class="article-lead">.*?</p>\n?', r"<article[^>]*>\n?", r"</h1>\n?"):
        m = re.search(pat, t, re.S)
        if m:
            return t[:m.end()] + box + t[m.end():]
    return None


n_d = n_e = n_rep = 0
for f in sorted(glob.glob(R + "**/*.html", recursive=True)):
    rel = f[len(R):]
    if rel.startswith(EX) or "/" + rel[:-5] in red or rel.endswith("_TEMPLATE.html"):
        continue
    t = open(f, encoding="utf-8").read()
    if 'class="ka-update"' in t:
        continue
    x = text(t)
    msgs = []
    if DATE.search(x) and not re.search(r"31 October 2026|October 31, 2026|31 Oct 2026", x):
        if not rel.startswith("news/") and "missed-september-30" not in rel:
            def rep(m):
                global n_rep
                if KEEP.search(t[max(0, m.start() - 70):m.start()]):
                    return m.group(0)
                n_rep += 1
                return "31 October 2026 (extended from 30 September 2026)"
            t = DATE.sub(rep, t)
        msgs.append(D_MSG); n_d += 1
    if rel not in SKIP7 and re.search(r"[Ss]ection 7E|\b7E\b", x) and not re.search(r"omit", x, re.I):
        msgs.append(E_MSG); n_e += 1
    if not msgs:
        continue
    new = place(t, BOX.format(" ".join(msgs)))
    if new is None:
        print("NO PLACE", rel); continue
    open(f, "w", encoding="utf-8").write(new)
print("deadline pages", n_d, "date replacements", n_rep, "7E pages", n_e)
