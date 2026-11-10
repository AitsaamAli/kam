"""Merges extra depth sections for the DNFBP and sole proprietor guides (see build.py apply_extra)."""
import importlib

EXTRA = {}
for _m in ("extras_sole", "extras_sole2", "extras_sole3", "extras_sole4", "extras_sole5", "extras_dnfbp", "extras_dnfbp2", "extras_city", "extras_city2"):
    try:
        mod = importlib.import_module(_m)
    except ModuleNotFoundError:
        continue
    for k, (h, f) in mod.EXTRA.items():
        if k in EXTRA:
            EXTRA[k] = (EXTRA[k][0] + h, EXTRA[k][1] + list(f))
        else:
            EXTRA[k] = (h, list(f))
