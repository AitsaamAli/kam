"""Second pass of the 27 Nov 2026 fact fix: rupee examples and 'double/half' wording that followed from the old
off-ATL rates. New arithmetic: 236C off-ATL 11.5% vs 2.75% (extra 8.75% of the sale price); 236K off-ATL 10.5% to Rs 50m vs 1.25%
(extra 9.25% of FMV). Bank profit (s.151) 20% on the ATL / 40% off it. Literal pairs; a miss is reported, never guessed."""
import sys
R = "/home/user/kam/"
P = {
"blogs/atl-surcharge-2026-pakistan.html": [("+1.25% of property value", "+9.25% of property value (to Rs 50m)"),
    ("<td>11.5%</td><td>Double rate</td>", "<td>11.5%</td><td>+8.75% of sale price</td>"),
    ("Rs.125,000", "Rs.925,000"), ("15% vs 30%", "20% vs 40%")],
"blogs/germany-after-moving-tax-filing-ntn-fbr-status-pakistan-2026.html": [("yeh farq tagreeban 2.75 lakh rupay ka hai", "yeh farq tagreeban 8.75 lakh rupay ka hai")],
"blogs/germany-blue-card-ntn-tax-returns-pakistan-2026.html": [("non-filer ko 11.5%, yani double", "non-filer ko 11.5%, yani chaar guna se zyada")],
"blogs/germany-student-visa-fbr-blocked-account-pakistan-2026.html": [("11.5%</strong> — poora double", "11.5%</strong> — chaar guna se zyada"),
    ("yeh farq 2.75 lakh aur 5.5 lakh ka hai", "filer 2.75 lakh aur non-filer 11.5 lakh deta hai, yani 8.75 lakh ka farq"),
    ("tagreeban 2.75 lakh rupay ki bachat", "tagreeban 8.75 lakh rupay ki bachat")],
"blogs/germany-visa-fbr-tax-return-pakistan-2026.html": [("11.5% — yani double", "11.5% — yani chaar guna se zyada"),
    ("yeh farq 2.75 lakh aur 5.5 lakh ka hai", "filer 2.75 lakh aur non-filer 11.5 lakh deta hai, yani 8.75 lakh ka farq")],
"blogs/income-tax-filing-islamabad.html": [("that is a Rs. 500,000 difference", "that is a Rs. 4,625,000 difference")],
"blogs/income-tax-filing-lahore.html": [("halves the WHT on both sides", "cuts the WHT sharply on both sides"),
    ("this is a difference of Rs. 375,000 saved", "this is a difference of Rs. 2,775,000 saved")],
"blogs/income-tax-filing-peshawar.html": [("filer status saves Rs. 100,000-200,000 per transaction", "filer status saves Rs. 875,000-1,750,000 per transaction")],
"blogs/income-tax-return-2026-iris-live-pakistan.html": [("<td>10.5%&ndash;18.5%</td><td>Double bachat</td>", "<td>10.5%&ndash;18.5%</td><td>8x se zyada bachat</td>"),
    ("<td>11.5%</td><td>Double bachat</td>", "<td>11.5%</td><td>4x se zyada bachat</td>")],
"blogs/italy-se-pakistan-remittance-property-tax-guide-2026.html": [("tagreeban 4 lakh 30 hazar rupay", "tagreeban 17 lakh 90 hazar rupay")],
"blogs/italy-seasonal-work-visa-182-day-rule-pakistan-tax-2026.html": [("yeh farq 62,500 rupay ka hai", "yeh farq 4,62,500 rupay ka hai")],
"blogs/italy-work-visa-quota-2026-pakistani-workers-fbr-guide.html": [("11.5% — poora double", "11.5% — chaar guna se zyada")],
"blogs/nicop-holder-tax-obligations-pakistan.html": [("Rs 125,000 against Rs 250,000", "Rs 125,000 against Rs 1,050,000")],
"blogs/non-filer-consequences-pakistan-2026.html": [("deducts double advance tax", "deducts far higher advance tax"),
    ("costs Rs. 62,500 extra in advance tax alone", "costs Rs. 4,62,500 extra in advance tax alone")],
"blogs/ntn-registration-before-buying-property-lahore.html": [("exactly double", "more than eight times as much"),
    ("between Rs. 125,000 and Rs. 250,000", "between Rs. 125,000 and Rs. 1,050,000"),
    ("double the withholding tax on the same transaction value", "more than eight times the withholding tax on the same value (up to Rs 50m)")],
"blogs/ntn-registration-online-pakistan.html": [("Rs 62,500 per Rs 50 lakh deal", "Rs 4,62,500 per Rs 50 lakh deal"),
    ("Rs 1,37,500 per Rs 50 lakh sale", "Rs 4,37,500 per Rs 50 lakh sale")],
"blogs/olx-property-car-seller-tax-pakistan-2026.html": [("Rs 50L sale par Rs 1.37 lakh extra tax", "Rs 50L sale par Rs 4.37 lakh extra tax"),
    ("2.75% vs 11.5% — half tax", "2.75% vs 11.5% — chauthai se bhi kam tax"),
    ("Rs 62,500 per Rs 50L", "Rs 4,62,500 per Rs 50L"), ("Rs 1,37,500 per Rs 50L", "Rs 4,37,500 per Rs 50L")],
"blogs/overseas-pakistani-property-tax-pakistan.html": [("filer status saves Rs 187,500", "filer status saves Rs 1,387,500")],
"blogs/property-purchase-pakistan-dubai-pakistanis.html": [("Rs 250,000 as an active filer and Rs 500,000 otherwise", "Rs 250,000 as an active filer and Rs 2,100,000 otherwise")],
"blogs/property-stamp-duty-tax-pakistan-2026.html": [("10.5% (to Rs 50m; 14.5% to Rs 100m, 18.5% above) &times; Rs.&nbsp;10 million = Rs.&nbsp;250,000", "10.5% &times; Rs.&nbsp;10 million = Rs.&nbsp;1,050,000"),
    ("Saving from being an ATL filer: Rs.&nbsp;750,000", "Saving from being an ATL filer: Rs.&nbsp;925,000"),
    ("(3% vs 10.5%) saves 7.5 percentage points on both the purchase (Section 236K) and the sale (Section 236C). On a Rs.&nbsp;20 million property, this is Rs.&nbsp;1.5 million saved in WHT alone", "(1.25% vs 10.5% on a purchase up to Rs 50m; 2.75% vs 11.5% on a sale) saves 9.25 and 8.75 percentage points. On a Rs.&nbsp;20 million property, this is Rs.&nbsp;1.85 million on the purchase and Rs.&nbsp;1.75 million on the sale")],
"blogs/salary-person-tax-return-pakistan.html": [("bank profit WHT doubles from 15% to 30%, property purchase WHT doubles from", "bank profit WHT doubles from 20% to 40%, property purchase WHT rises from"),
    ("an entire year of doubled WHT rates", "an entire year of higher WHT rates")],
"blogs/same-day-income-tax-return-filing-pakistan.html": [("bank profit WHT from 30% to 15%", "bank profit WHT from 40% to 20%"),
    ("this saves Rs. 1,37,500", "this saves Rs. 4,37,500"), ("this saves Rs. 62,500", "this saves Rs. 4,62,500"),
    ("On Rs. 5 lakh profit, this saves Rs. 75,000 per year", "On Rs. 5 lakh profit, this saves Rs. 1,00,000 per year")],
"blogs/tax-consultant-defence-view-karachi.html": [("Rs 100,000 against Rs 200,000", "Rs 100,000 against Rs 840,000"),
    ("so on Rs 8 million you save Rs 100,000", "so on Rs 8 million you save Rs 740,000")],
"blogs/tax-consultant-dha-phase-9-lahore.html": [("is double for buyers not on the Active Taxpayer List", "is far higher for buyers not on the Active Taxpayer List")],
"blogs/tax-consultant-zhob.html": [("15% vs 35%", "20% vs 40%")],
"blogs/tax-for-property-investors-pakistan-2026.html": [("10.5%&ndash;18.5% (above Rs. 5 million)", "10.5%&ndash;18.5%"),
    ("Rs. 1,25,000 (10.5% (to Rs 50m; 14.5% to Rs 100m, 18.5% above))", "Rs. 5,25,000 (10.5%)"), ("Rs. 4,12,500 (11.5%)", "Rs. 8,62,500 (11.5%)")],
"blogs/usa-after-moving-tax-filing-ntn-fbr-status-pakistan-2026.html": [("tagreeban 8 lakh 25 hazar rupay", "tagreeban 26 lakh 25 hazar rupay")],
"blogs/usa-h1b-employment-visa-ntn-tax-returns-pakistan-2026.html": [("yeh farq 2.75 lakh rupay ka hai", "yeh farq 8.75 lakh rupay ka hai")],
"blogs/wht-rate-card-2026-27-pakistan.html": [("Bank profit 15%/35%", "Bank profit 20%/40%"), ("bank profit — 15%/35%", "bank profit — 20%/40%")],
"blogs/check-filer-status-atl-online-pakistan.html": [("<td>15%</td><td>35%</td>", "<td>20%</td><td>40%</td>")],
}
APPLY = "--apply" in sys.argv
miss = 0
for f, pairs in P.items():
    t = open(R + f, encoding="utf-8").read()
    for o, n in pairs:
        c = t.count(o)
        if not c:
            print("MISS", f, "|", o); miss += 1
        t = t.replace(o, n)
    if APPLY:
        open(R + f, "w", encoding="utf-8").write(t)
print("misses", miss)
