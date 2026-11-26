"""DNFBP registration series 2: 10 guides (facts checked 26 November 2026; see ds_common.py)."""
from ds_common import DATE, DLONG, WA
from ds_a import SRO, DEV, CERT, SOLE
from ds_b import DOCS, PEP, UBO
from ds_c import TFS, PEN, NRA

POSTS = [SRO, DEV, CERT, SOLE, DOCS, PEP, UBO, TFS, PEN, NRA]

from ds_common import SL
from ds_boost import BOOST
_K = {v: k for k, v in SL.items()}
for _p in POSTS:
    k = _K[_p["slug"]]
    if k in BOOST:
        sec, fq = BOOST[k]
        _p["body"] = _p["body"].rstrip() + "\n" + sec
        _p["faqs"] = list(_p["faqs"]) + fq
