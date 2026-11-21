"""PRA registration series: 10 guides (facts checked 21 November 2026; see pra_common.py)."""
from pra_common import DATE, DLONG, WA
from pra_a import PROC, DOCS, FEE_P, CERT, VER
from pra_b import WHO, COMP, SOLE, FBR, CHG

from pra_more import merge, merge2, merge3

POSTS = [merge3(merge2(merge(p))) for p in [PROC, DOCS, FEE_P, CERT, VER, WHO, COMP, SOLE, FBR, CHG]]
