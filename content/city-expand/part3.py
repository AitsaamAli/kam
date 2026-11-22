"""Part 3 of the city pages programme (owner, 22 Nov 2026): Punjab towns L-Z. Same method and sources as part2.py (imported).
Non-Punjab pages found in this part (loralai, zhob -> part 4; timergara, upper-dir -> part 5) and new-jersey-pakistanis (overseas
topic, not a town) are not touched here."""
import json, re, sys
sys.path.insert(0, "/home/user/kam/content/city-expand")
import part2 as P

C = P.CENSUS
ROOT = P.ROOT
DIST_FIX = {"Tala Gang": "Talagang", "Tandlian Wala": "Tandlianwala", "Noor Pur": "Noorpur Thal", "Malakwal": "Malikwal", "Taunsa": "Taunsa Sharif"}
TOWNS_ONLY = {"tulamba": ("Khanewal", "Tulamba"), "uch-sharif": ("Bahawalpur", "Uch Sharif"), "wah-cantt": ("Rawalpindi", "Wah Cantt")}
ROW = {"malikwal": "MALAKWAL TEHSIL", "noorpur-thal": "NOOR PUR TEHSIL", "taunsa-sharif": "TAUNSA TEHSIL", "talagang": "TALA GANG TEHSIL",
       "tandlianwala": "TANDLIAN WALA TEHSIL", "pindigheb": "PINDI GHEB TEHSIL", "multan": "MULTAN CITY TEHSIL"}
SKIP = {"loralai", "zhob", "timergara", "upper-dir", "new-jersey-pakistanis"}


def build():
    d = json.load(open(ROOT + "content/city-expand/batches.json"))
    T = {}
    for s in d["parts"][2]["pages"]:
        t = s.replace("tax-consultant-", "")
        if t in SKIP:
            continue
        if t in TOWNS_ONLY:
            dist, name = TOWNS_ONLY[t]
            T[t] = (dist.upper() + " DISTRICT", dist, name)
            continue
        row = ROW.get(t) or t.replace("-", " ").upper() + " TEHSIL"
        if row not in C:
            print("no census row", t)
            continue
        dist = C[row]["district"].title()
        name = DIST_FIX.get(row.rsplit(" ", 1)[0].title(), row.rsplit(" ", 1)[0].title())
        name = {"Multan City": "Multan"}.get(name, name)
        T[t] = (row, dist, name)
    return T


def main():
    P.T = build()
    P.MERGE = {}
    done = [s for s in P.T if P.apply(s)]
    print("pages updated", len(done))


if __name__ == "__main__":
    main()
