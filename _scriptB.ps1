. "c:\Users\786\Desktop\kam\_common.ps1"

# ---- AREA BLOGS: 169 city neighborhoods ----
function MkArea($slug, $city, $area, $cat) {
  $title = "Best Tax Consultant in $area $city 2026 | Kamboh Associates"
  $desc = "Tax consultant in $area $city. Income tax return, NTN registration, FBR compliance from Rs. 3,500. WhatsApp 0328-4675162."
  $kw = "tax consultant $area $city, income tax $area $city 2026, NTN registration $area, FBR consultant $area"
  $h1 = "Best Tax Consultant in $area $city 2026"
  $lead = "Kamboh Associates serves clients in $area, $city with 100% online tax services. Income tax return, NTN registration, and FBR compliance without any office visit."
  $body = '<h2>Tax Services in ' + $area + ' ' + $city + '</h2><ul><li>Income Tax Return from Rs. 3,500</li><li>NTN Registration from Rs. 2,000</li><li>Sales Tax STRN Registration</li><li>Company Registration</li><li>FBR Notice Response</li><li>Active Filer Status Update</li></ul><h2>How to Get Started from ' + $area + '</h2><ul><li>WhatsApp CNIC and income documents to 0328-4675162</li><li>Free consultation - confirm fee before proceeding</li><li>Return filed same day on FBR IRIS</li><li>Receive acknowledgment and filer status within 24 hours</li></ul><div class=''highlight-box''><p><strong>Ready to file from ' + $area + '?</strong> WhatsApp <a href=''https://wa.me/923284675162'' style=''color:#14B8A6;font-weight:600''>0328-4675162</a> - free consultation, 30-minute response.</p></div><h2>Frequently Asked Questions</h2><div class=''faq-list''><div class=''faq-item''><div class=''faq-q''>Can I get tax service online from ' + $area + ' ' + $city + '? <i class=''fas fa-chevron-down''></i></div><div class=''faq-a''>Yes. 100% online. WhatsApp documents and we file on FBR IRIS same day. No office visit needed from ' + $area + '.</div></div><div class=''faq-item''><div class=''faq-q''>What is the fee for income tax return in ' + $area + '? <i class=''fas fa-chevron-down''></i></div><div class=''faq-a''>Individual salaried return from Rs. 3,500. Business return from Rs. 5,000. NTN registration Rs. 2,000. All fees are all-inclusive.</div></div></div>'
  $body2 = $body -replace "''","'"
  $html = MkPage $slug $title $desc $kw "https://kambohassociates.com/blogs/$slug" $cat "fas fa-map-pin" $h1 "5 min read" $lead $body2
  WB $slug $html
}

# Lahore (20)
"shad-bagh|Shad Bagh","ravi-road|Ravi Road","bund-road|Bund Road","data-darbar|Data Darbar","walled-city|Walled City","lda-avenue|LDA Avenue","paragon-city|Paragon City","bahria-orchard|Bahria Orchard","muslim-town|Muslim Town","new-garden-town|New Garden Town","dharampura|Dharampura","qainchi|Qainchi","sanda|Sanda","upper-mall|Upper Mall","canal-road|Canal Road","barkat-market|Barkat Market","wahdat-road|Wahdat Road","circular-road|Circular Road","ferozepur-road|Ferozepur Road","airport-road|Airport Road" | ForEach-Object { $p=$_ -split '\|'; MkArea "tax-consultant-$($p[0])-lahore" "Lahore" $p[1] "Lahore Local" }

# Karachi (20)
"clifton-block-2|Clifton Block 2","clifton-block-5|Clifton Block 5","zamzama|Zamzama","frere-town|Frere Town","defence-phase-2|Defence Phase 2","defence-phase-5|Defence Phase 5","defence-phase-8|Defence Phase 8","gulshan-block-13|Gulshan Block 13","dha-city|DHA City","shahrah-e-faisal|Shahrah-e-Faisal","burns-road|Burns Road","bolton-market|Bolton Market","civil-lines|Civil Lines","seaview|Sea View","hawkes-bay|Hawkes Bay","ranchore-lines|Ranchore Lines","naya-karachi|Naya Karachi","clifton-block-9|Clifton Block 9","korangi-township|Korangi Township","superhighway|Superhighway Area" | ForEach-Object { $p=$_ -split '\|'; MkArea "tax-consultant-$($p[0])-karachi" "Karachi" $p[1] "Karachi Local" }

# Islamabad (15)
"e-9|E-9","i-14|I-14","i-15|I-15","i-16|I-16","faisal-avenue|Faisal Avenue","zero-point|Zero Point","g-12|G-12","h-11|H-11","i-11|I-11","i-12|I-12","f-4|F-4","golra|Golra","police-foundation|Police Foundation","media-town|Media Town","khayaban-e-iqbal|Khayaban-e-Iqbal" | ForEach-Object { $p=$_ -split '\|'; MkArea "tax-consultant-$($p[0])-islamabad" "Islamabad" $p[1] "Islamabad Local" }

# Rawalpindi (10)
"pindora|Pindora","liaquat-bagh|Liaquat Bagh","askari-14|Askari 14","murree-road|Murree Road","new-lalazar|New Lalazar","rwp-civil-lines|Civil Lines","kallar-syedan|Kallar Syedan","rwp-airport|Airport Area","kohat-road-rwp|Kohat Road","gunjmandi|Gunjmandi" | ForEach-Object { $p=$_ -split '\|'; MkArea "tax-consultant-$($p[0])-rawalpindi" "Rawalpindi" $p[1] "Islamabad Local" }

# Faisalabad (10)
"clock-tower|Clock Tower","batala-colony|Batala Colony","ghulam-muhammad-abad|Ghulam Muhammad Abad","industrial-estate|Industrial Estate","american-chowk|American Chowk","katchery-road|Katchery Road","dijkot|Dijkot","sargodha-road-fsd|Sargodha Road","railway-road-fsd|Railway Road","nishatabad|Nishatabad" | ForEach-Object { $p=$_ -split '\|'; MkArea "tax-consultant-$($p[0])-faisalabad" "Faisalabad" $p[1] "Faisalabad Local" }

# Multan (10)
"hussain-agahi|Hussain Agahi","chungi-no9|Chungi No 9","multan-garden-town|Garden Town","mda-chowk|MDA Chowk","vehari-road|Vehari Road","shershah|Shershah","sabzazar|Sabzazar","multan-nishatabad|Nishatabad","hafeezabad|Hafeezabad","bohar-gate|Bohar Gate" | ForEach-Object { $p=$_ -split '\|'; MkArea "tax-consultant-$($p[0])-multan" "Multan" $p[1] "Multan Local" }

# Peshawar (10)
"ring-road-psh|Ring Road","dalazak-road|Dalazak Road","warsak-road|Warsak Road","charsadda-road-psh|Charsadda Road","kohat-road-psh|Kohat Road","jamrud-road|Jamrud Road","bara-road|Bara Road","pishtakhara|Pishtakhara","mattni|Mattni","faqirabad|Faqirabad" | ForEach-Object { $p=$_ -split '\|'; MkArea "tax-consultant-$($p[0])-peshawar" "Peshawar" $p[1] "Peshawar Local" }

# Quetta (10)
"zarghoon-road|Zarghoon Road","adalat-road|Adalat Road","brewery-road|Brewery Road","kirani-road|Kirani Road","spini-road|Spini Road","new-sariab|New Sariab","baleli|Baleli","kuchlak-road|Kuchlak Road","double-road|Double Road","quetta-city-centre|City Centre" | ForEach-Object { $p=$_ -split '\|'; MkArea "tax-consultant-$($p[0])-quetta" "Quetta" $p[1] "Quetta Local" }

# Gujranwala (10)
"trust-colony|Trust Colony","rahwali|Rahwali","shaheenabad|Shaheenabad","jinnah-colony|Jinnah Colony","farid-town|Farid Town","ali-pur-chatha|Ali Pur Chatha","gondlanwala|Gondlanwala","khiali|Khiali","nowshera-virkan|Nowshera Virkan","kamoke-road-gwl|Kamoke Road" | ForEach-Object { $p=$_ -split '\|'; MkArea "tax-consultant-$($p[0])-gujranwala" "Gujranwala" $p[1] "Gujranwala Local" }

# Hyderabad (10)
"unit-1-hyd|Unit 1","unit-6-hyd|Unit 6","unit-9-hyd|Unit 9","auto-bhan-road|Auto Bhan Road","market-quarter|Market Quarter","hali-road|Hali Road","hussainabad-hyd|Hussainabad","sindhi-muslim-colony|Sindhi Muslim Colony","tando-road|Tando Road","shahi-bazar-hyd|Shahi Bazar" | ForEach-Object { $p=$_ -split '\|'; MkArea "tax-consultant-$($p[0])-hyderabad" "Hyderabad" $p[1] "Hyderabad Local" }

# Extra 4
MkArea "tax-consultant-iqbal-town-sialkot" "Sialkot" "Iqbal Town" "Sialkot Local"
MkArea "tax-consultant-shahabpura-sialkot" "Sialkot" "Shahabpura" "Sialkot Local"
MkArea "tax-consultant-saddar-bahawalpur" "Bahawalpur" "Saddar" "Other Cities"
MkArea "tax-consultant-mardan-city-centre" "Mardan" "City Centre" "Other Cities"

Write-Host "Area blogs done. Created: $($script:created) | Skipped: $($script:skipped)"
