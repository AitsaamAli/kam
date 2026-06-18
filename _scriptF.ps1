. "c:\Users\786\Desktop\kam\_common.ps1"

function MkArea($slug, $city, $area, $cat) {
  $title = "Best Tax Consultant in $area $city 2026 | Kamboh Associates"
  $desc = "Tax consultant in $area $city. Income tax return, NTN registration, FBR compliance from Rs. 3,500. WhatsApp 0328-4675162."
  $kw = "tax consultant $area $city, income tax $area $city 2026, NTN registration $area"
  $h1 = "Best Tax Consultant in $area $city 2026"
  $lead = "Kamboh Associates serves clients in $area, $city with 100% online tax services. Income tax return, NTN registration, and FBR compliance without any office visit."
  $body = '<h2>Tax Services in ' + $area + ' ' + $city + '</h2><ul><li>Income Tax Return from Rs. 3,500</li><li>NTN Registration from Rs. 2,000</li><li>Sales Tax STRN Registration</li><li>Company Registration</li><li>FBR Notice Response</li></ul><div class=''highlight-box''><p><strong>Ready to file from ' + $area + '?</strong> WhatsApp <a href=''https://wa.me/923284675162'' style=''color:#14B8A6;font-weight:600''>0328-4675162</a></p></div><h2>FAQ</h2><div class=''faq-list''><div class=''faq-item''><div class=''faq-q''>Can I get tax service online from ' + $area + '? <i class=''fas fa-chevron-down''></i></div><div class=''faq-a''>Yes. 100% online. WhatsApp documents and we file on FBR IRIS same day.</div></div></div>'
  $body2 = $body -replace "''","'"
  $html = MkPage $slug $title $desc $kw "https://kambohassociates.com/blogs/$slug" $cat "fas fa-map-pin" $h1 "4 min read" $lead $body2
  WB $slug $html
}

MkArea "tax-consultant-jhang-city-centre" "Jhang" "City Centre" "Other Cities"
MkArea "tax-consultant-layyah-city-centre" "Layyah" "City Centre" "Other Cities"
MkArea "tax-consultant-bhakkar-city-centre" "Bhakkar" "City Centre" "Other Cities"
MkArea "tax-consultant-chiniot-city-centre" "Chiniot" "City Centre" "Other Cities"
MkArea "tax-consultant-mandi-bahauddin-city" "Mandi Bahauddin" "City Centre" "Other Cities"
MkArea "tax-consultant-daska-city-centre" "Daska" "City Centre" "Other Cities"

Write-Host "Done. Created: $($script:created) | Skipped: $($script:skipped)"
