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

MkArea "tax-consultant-kot-addu" "Muzaffargarh" "Kot Addu" "Other Cities"
MkArea "tax-consultant-taunsa-sharif" "Dera Ghazi Khan" "Taunsa Sharif" "Other Cities"
MkArea "tax-consultant-mian-channu-city" "Khanewal" "Mian Channu" "Other Cities"
MkArea "tax-consultant-kamalia-city" "Toba Tek Singh" "Kamalia" "Other Cities"
MkArea "tax-consultant-pakpattan-city" "Pakpattan" "City Area" "Other Cities"
MkArea "tax-consultant-okara-city" "Okara" "City Area" "Other Cities"
MkArea "tax-consultant-vehari-city" "Vehari" "City Area" "Other Cities"
MkArea "tax-consultant-khanewal-city" "Khanewal" "City Area" "Other Cities"
MkArea "tax-consultant-lodhran-city" "Lodhran" "City Area" "Other Cities"
MkArea "tax-consultant-rajanpur-city" "Rajanpur" "City Area" "Other Cities"

Write-Host "Done. Created: $($script:created) | Skipped: $($script:skipped)"
