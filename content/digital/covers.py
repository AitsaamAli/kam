"""Generate a unique 1200x630 cover (JPG for social, WebP for the page) for every blog post."""
import glob, importlib.util, os, textwrap
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "digital", "images", "blog")
FONT = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
FONT_M = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
NAVY, TEAL, GOLD = (15, 23, 42), (20, 184, 166), (212, 175, 55)
ACCENTS = [GOLD, TEAL]  # the two brand accents used across kambohassociates.com


def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.POST


def cover(p):
    W, H = 1200, 630
    acc = ACCENTS[p["order"] % len(ACCENTS)]
    im = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(im)
    for y in range(H):  # vertical gradient navy -> slate
        t = y / H
        d.line([(0, y), (W, y)], fill=(int(15 + 15 * t), int(23 + 18 * t), int(42 + 30 * t)))
    for i in range(6):  # decorative rings, offset per post so each cover differs
        r = 120 + i * 60
        cx, cy = 1050 + (p["order"] % 3) * 30, 120 + (p["order"] % 4) * 40
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=tuple(int(c * 0.35) for c in acc), width=2)
    d.rectangle([0, 0, 14, H], fill=acc)
    f_tag, f_title, f_foot = ImageFont.truetype(FONT_M, 30), ImageFont.truetype(FONT, 72), ImageFont.truetype(FONT_M, 28)
    tag = p["category"].upper() + "  ·  2026 GUIDE"
    tw = d.textlength(tag, font=f_tag)
    d.rounded_rectangle([80, 80, 80 + tw + 40, 132], 26, fill=tuple(int(c * 0.25) for c in acc), outline=acc, width=2)
    d.text((100, 89), tag, font=f_tag, fill=acc)
    y = 180
    for line in textwrap.wrap(p["crumb"], 22)[:3]:
        d.text((80, y), line, font=f_title, fill=(255, 255, 255)); y += 88
    d.line([(80, y + 20), (260, y + 20)], fill=acc, width=6)
    d.text((80, H - 90), "Kamboh Associates Digital  ·  Lahore, Pakistan", font=f_foot, fill=(203, 213, 225))
    os.makedirs(OUT, exist_ok=True)
    im.save(os.path.join(OUT, p["slug"] + ".jpg"), "JPEG", quality=82, optimize=True, progressive=True)
    im.resize((800, 420), Image.LANCZOS).save(os.path.join(OUT, p["slug"] + ".webp"), "WEBP", quality=78, method=6)


if __name__ == "__main__":
    n = 0
    for f in sorted(glob.glob(os.path.join(HERE, "posts", "*.py"))):
        cover(load(f)); n += 1
    print("covers", n)
