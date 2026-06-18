. "c:\Users\786\Desktop\kam\_common.ps1"

function MkArea($slug, $city, $area, $cat) {
  $title = "Best Tax Consultant in $area $city 2026 | Kamboh Associates"
  $desc = "Tax consultant in $area $city. Income tax return, NTN registration, FBR compliance from Rs. 3,500. WhatsApp 0328-4675162."
  $kw = "tax consultant $area $city, income tax $area $city 2026, NTN registration $area"
  $h1 = "Best Tax Consultant in $area $city 2026"
  $lead = "Kamboh Associates serves clients in $area, $city with 100% online tax services. Income tax return, NTN registration, and FBR compliance without any office visit."
  $body = '<h2>Tax Services in ' + $area + ' ' + $city + '</h2><ul><li>Income Tax Return from Rs. 3,500</li><li>NTN Registration from Rs. 2,000</li><li>Sales Tax STRN Registration</li><li>Company Registration</li><li>FBR Notice Response</li><li>Active Filer Status Update</li></ul><h2>How to Get Started from ' + $area + '</h2><ul><li>WhatsApp CNIC and income documents to 0328-4675162</li><li>Free consultation - confirm fee before proceeding</li><li>Return filed same day on FBR IRIS</li><li>Receive acknowledgment and filer status within 24 hours</li></ul><div class=''highlight-box''><p><strong>Ready to file from ' + $area + '?</strong> WhatsApp <a href=''https://wa.me/923284675162'' style=''color:#14B8A6;font-weight:600''>0328-4675162</a> - free consultation, 30-minute response.</p></div><h2>Frequently Asked Questions</h2><div class=''faq-list''><div class=''faq-item''><div class=''faq-q''>Can I get tax service online from ' + $area + ' ' + $city + '? <i class=''fas fa-chevron-down''></i></div><div class=''faq-a''>Yes. 100% online. WhatsApp documents and we file on FBR IRIS same day. No office visit needed from ' + $area + '.</div></div><div class=''faq-item''><div class=''faq-q''>What is the fee for income tax return in ' + $area + '? <i class=''fas fa-chevron-down''></i></div><div class=''faq-a''>Individual salaried return from Rs. 3,500. Business return from Rs. 5,000. NTN registration Rs. 2,000.</div></div></div>'
  $body2 = $body -replace "''","'"
  $html = MkPage $slug $title $desc $kw "https://kambohassociates.com/blogs/$slug" $cat "fas fa-map-pin" $h1 "5 min read" $lead $body2
  WB $slug $html
}

# Lahore more areas (10)
"johar-town-j3|J-3 Block","johar-town-j2|J-2 Block","johar-town-h3|H-3 Block","wapda-town-lahore|Wapda Town","eden-value-homes|Eden Value Homes","alt-buksh-colony|Alt Buksh Colony","younas-colony|Younas Colony","samnabad|Samnabad","mughalpura|Mughalpura","shadbagh-east|Shadbagh East" | ForEach-Object { $p=$_ -split '\|'; MkArea "tax-consultant-$($p[0])-lahore" "Lahore" $p[1] "Lahore Local" }

# Karachi more (8)
"gulshan-block-6|Gulshan Block 6","gulshan-block-7|Gulshan Block 7","saddar-karachi|Saddar","nazimabad-4|Nazimabad 4","nazimabad-5|Nazimabad 5","federal-b-area|Federal B Area","maripur|Maripur","site-industrial|SITE Industrial Area" | ForEach-Object { $p=$_ -split '\|'; MkArea "tax-consultant-$($p[0])-karachi" "Karachi" $p[1] "Karachi Local" }

# Islamabad more (5)
"g-13|G-13","g-14|G-14","b-17|B-17","c-18|C-18","pwd-islamabad|PWD Colony" | ForEach-Object { $p=$_ -split '\|'; MkArea "tax-consultant-$($p[0])-islamabad" "Islamabad" $p[1] "Islamabad Local" }

# Other cities (23 - various)
MkArea "tax-consultant-abbottabad-city" "Abbottabad" "City Area" "Other Cities"
MkArea "tax-consultant-abbottabad-havelian" "Abbottabad" "Havelian" "Other Cities"
MkArea "tax-consultant-dera-ghazi-khan-city" "Dera Ghazi Khan" "City Centre" "Other Cities"
MkArea "tax-consultant-bahawalpur-model-town" "Bahawalpur" "Model Town" "Other Cities"
MkArea "tax-consultant-sargodha-university-road" "Sargodha" "University Road" "Other Cities"
MkArea "tax-consultant-sargodha-lyon-colony" "Sargodha" "Lyon Colony" "Other Cities"
MkArea "tax-consultant-sahiwal-city" "Sahiwal" "City Centre" "Other Cities"
MkArea "tax-consultant-sahiwal-model-colony" "Sahiwal" "Model Colony" "Other Cities"
MkArea "tax-consultant-larkana-city" "Larkana" "City Area" "Other Cities"
MkArea "tax-consultant-sukkur-new-sukkur" "Sukkur" "New Sukkur" "Other Cities"
MkArea "tax-consultant-mardan-industrial-estate" "Mardan" "Industrial Estate" "Other Cities"
MkArea "tax-consultant-swat-mingora-road" "Swat" "Mingora Road" "Other Cities"
MkArea "tax-consultant-dera-ismail-khan-city" "Dera Ismail Khan" "City Centre" "Other Cities"
MkArea "tax-consultant-hyderabad-latifabad" "Hyderabad" "Latifabad" "Hyderabad Local"
MkArea "tax-consultant-hyderabad-qasimabad" "Hyderabad" "Qasimabad" "Hyderabad Local"
MkArea "tax-consultant-kasur-city-centre" "Kasur" "City Centre" "Other Cities"
MkArea "tax-consultant-sheikhupura-city-centre" "Sheikhupura" "City Centre" "Other Cities"
MkArea "tax-consultant-narowal-city-centre" "Narowal" "City Centre" "Other Cities"
MkArea "tax-consultant-hafizabad-city-centre" "Hafizabad" "City Centre" "Other Cities"
MkArea "tax-consultant-gujrat-city-centre" "Gujrat" "City Centre" "Other Cities"
MkArea "tax-consultant-jhelum-city-centre" "Jhelum" "City Centre" "Other Cities"
MkArea "tax-consultant-chakwal-city-centre" "Chakwal" "City Centre" "Other Cities"
MkArea "tax-consultant-attock-city-centre" "Attock" "City Centre" "Other Cities"

Write-Host "Script D done. Created: $($script:created) | Skipped: $($script:skipped)"
