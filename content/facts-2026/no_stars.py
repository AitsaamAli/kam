"""27 Nov 2026: standing rule 'never show a review count or star rating'. Removes star-glyph ratings (★★★★★, &#9733;) shown next to
testimonials, replaces the 'Reviews on Google' star header with a link to the Google Business Profile, and drops 'Rated 5 stars' text.
Testimonial wording is kept. Idempotent."""
import glob, re
R = "/home/user/kam/"
GBP = "https://g.page/r/CYzrn3EEiZVwEBM"
EX = ("content", "outreach", "reports", "seo_output", "searchops-team", "project-history", "schema", "content-batches")
STAR = r"(?:★|&#9733;|&#x2605;|&starf;)"
HDR = re.compile(r'<span[^>]*>\s*' + STAR + r'{3,5}\s*</span>\s*<span[^>]*>\s*Reviews on Google\s*</span>')
ONLY = re.compile(r'<(div|span|p)[^>]*>\s*' + STAR + r'{3,5}\s*</\1>\s*')
LINK = f'<a href="{GBP}" target="_blank" rel="noopener" style="font-size:.75rem;color:#0D9488;font-weight:600">Read our reviews on Google</a>'
pages = edits = 0
for f in glob.glob(R + "**/*.html", recursive=True):
    rel = f[len(R):]
    if rel.startswith(EX):
        continue
    t = open(f, encoding="utf-8").read()
    o = t
    t = HDR.sub(LINK, t)
    t = ONLY.sub("", t)
    t = t.replace(" Rated 5 stars.", "").replace("Rated 5 stars.", "")
    if t != o:
        pages += 1; edits += o.count("★") - t.count("★") + o.count("Rated 5 stars")
        open(f, "w", encoding="utf-8").write(t)
print("pages", pages, "star glyphs/ratings removed", edits)
