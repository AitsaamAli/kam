"""Tell Bing, Yandex and other IndexNow engines about new or changed pages (Nov 2026).
The key is public by design: it is served at https://kambohassociates.com/e33a3a1dc82729ad40ff90b6f962ce05.txt to prove site ownership.
Usage after a deploy is live:
  python3 content/geo/indexnow.py /blogs/new-page /pricing        # specific paths
  python3 content/geo/indexnow.py --sitemap                       # every URL in sitemap.xml (max 10,000 per call)"""
import json, re, sys, urllib.request

HOST = "kambohassociates.com"
KEY = "e33a3a1dc82729ad40ff90b6f962ce05"
SITE = "https://" + HOST


def urls_from_args(args):
    if args == ["--sitemap"]:
        return re.findall(r"<loc>([^<]+)</loc>", open("/home/user/kam/sitemap.xml", encoding="utf-8").read())
    return [a if a.startswith("http") else SITE + ("" if a.startswith("/") else "/") + a for a in args]


def main():
    urls = [u for u in urls_from_args(sys.argv[1:]) if u.startswith(SITE)][:10000]
    if not urls:
        print(__doc__); return
    body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"{SITE}/{KEY}.txt", "urlList": urls}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=60) as r:
        print("IndexNow", r.status, len(urls), "URLs")


if __name__ == "__main__":
    main()
