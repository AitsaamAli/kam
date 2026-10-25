"""Helper for town data files: one call registers a town's tax-consultant, NTN and filing pages."""


def town(pages, slug, tax=None, ntn=None, inc=None):
    for kind, spec in (("tax-consultant", tax), ("ntn-registration", ntn), ("income-tax-filing", inc)):
        if spec:
            lead, desc, body, faq = spec
            pages[f"blogs/{kind}-{slug}.html"] = {"lead": lead, "desc": desc, "body": body, "faq": faq, "drop_all": True,
                                                   "faq_skip_all": True}
