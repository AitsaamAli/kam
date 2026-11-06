#!/usr/bin/env python3
"""P3 fix (6 Nov 2026): one extra, page-specific section for the light pages that receive Search Console
impressions. Inserted before the 'Official sources' line (or the FAQ heading). Idempotent via data-p3 markers."""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ADD = {
    "professional-tax-pakistan-2026": ("Paying Professional Tax in Punjab and Keeping Proof",
        "<p>In Punjab, professional tax is collected by the Excise, Taxation and Narcotics Control Department, and can be paid online through the province's e-payment system. Keep the paid challan or receipt for each year: licence renewals, tenders, bank facilities and some registrations ask for proof that the business or professional has paid it. Professional tax is a provincial levy and is separate from federal income tax, so paying one does not settle the other. If you work from more than one province, check whether each province where you are registered or practise expects its own payment.</p>"),
    "private-limited-company-tax-return-pakistan": ("What Goes Into a Company's Tax Return",
        "<ul><li><strong>Financial statements</strong> for the year, with the tax computation reconciling accounting profit to taxable income.</li>"
        "<li><strong>Corporate tax</strong> at the rate for companies (29% for most companies), compared with the <strong>minimum tax on turnover under Section 113</strong>; the higher amount is payable.</li>"
        "<li><strong>Super tax under Section 4C</strong> where taxable income is above the thresholds in the law.</li>"
        "<li><strong>Withholding tax</strong> deducted from the company's receipts, claimed as a credit, and the company's own withholding statements for tax it deducted from others.</li></ul>"
        "<p>For a 30 June year end, the return is due by 31 December. Filing late brings the Section 182 penalty and, to rejoin the Active Taxpayers List, the Rs 100,000 Section 182A surcharge for companies.</p>"),
    "education-expense-tax-credit-pakistan": ("Records Rakhein: Fee Receipts Aur Bachon Ki Tafseel",
        "<p>Claim karne se pehle har bache ki fee ki asal receipts sambhal kar rakhein, jin par school ya college ka naam aur tafseel likhi ho, aur saath mein bank ya online payment ka record. Agar fee kisi aur ne adaa ki ho to claim usi ka banta hai jis ne asal mein payment ki. Return mein wohi raqam likhein jo receipts se saabit ho sake, kyun ke FBR notice ki soorat mein yahi kaghzaat maange jaate hain. Shuroot aur had har saal ke qanoon ke mutabiq hoti hain, is liye apne tax saal ki shuroot FBR ki site par dekh lein.</p>"),
    "business-expense-deductible-pakistan": ("Section 21 Ke Aam Masail Jo Kharcha Nakaam Kar Dete Hain",
        "<ul><li>Zaati ya ghar ke kharche jo business ke liye na hon.</li><li>Jurmane aur penalties jo kisi qanoon ki khilaf warzi par lagen.</li>"
        "<li>Aisi payment jis par withholding tax kaatna zaroori tha magar kata ya jama nahi hua.</li>"
        "<li>Bare kharche jo qanoon ki had se zyada naqad (cash) mein diye gaye, bank ke zariye nahi.</li></ul>"
        "<p>Har kharche ka bill, payment ka saboot aur, jahan zaroori ho, withholding tax ki challan sambhal kar rakhein. Yeh teen cheezein mil kar hi kharche ko qabil-e-qubool banati hain.</p>"),
    "tax-consultant-faisalabad": ("Power-Loom and Weaving Units",
        "<p>Faisalabad's power-loom owners often weave on conversion, earning a rate per metre for yarn supplied by a mill or trader. That conversion income is business income, and the yarn and cloth belonging to the customer are not part of the weaver's stock. Electricity is usually the largest cost, and advance tax charged on commercial and industrial electricity bills is claimed in the return when the bills are kept. Weaving units supplying registered mills and exporters are often asked for sales tax registration, so check whether your buyers require it before you invoice.</p>"),
    "tax-consultant-okara": ("Selling Land or a House in Okara",
        "<p>When agricultural land, a plot or a house in Okara is sold, the seller pays advance tax under Section 236C and the buyer under Section 236K, at lower rates for those on the Active Taxpayers List. Any capital gain is declared in the return for the year of sale. Keep the registry or mutation, the original purchase papers and proof of payment, because the gain is worked out from the original cost. Farmland sold by a farmer can raise questions about agricultural versus capital income, so record what was sold and when.</p>"),
    "tax-consultant-nazimabad-karachi": ("Inherited Houses and Portions on Rent",
        "<p>Many Nazimabad families hold older houses inherited by several heirs, often with one portion let out. Rent is property income of the owner or owners who receive it, each declaring their share; where the tenant is a company or other prescribed person, it deducts tax under Section 155 and the certificate is claimed in the return. Keep the succession or mutation documents showing who owns what share, because they decide whose return the rent and any later sale belong in.</p>"),
}


def main():
    os.chdir(ROOT)
    for slug, (h2, body) in ADD.items():
        f = f"blogs/{slug}.html"
        t = open(f, encoding="utf-8").read()
        if f'data-p3="{slug}"' in t:
            continue
        sec = f'<h2 id="p3-{slug[:20]}" data-p3="{slug}">{h2}</h2>{body}'
        a = t.find("<article")
        i = t.find('<p class="official-sources"', a)
        if i < 0:
            m = re.compile(r"<h2[^>]*>[^<]*(?:Frequently Asked|FAQ|Aksar Puchhe)", re.I).search(t, a)
            i = m.start() if m else t.find("</article>", a)
        t = t[:i] + sec + t[i:]
        open(f, "w", encoding="utf-8").write(t)
        print("added", f)


if __name__ == "__main__":
    main()
