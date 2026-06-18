# Script A: income-tax-filing + ntn-registration for 100 cities
. "c:\Users\786\Desktop\kam\_common.ps1"

$cities = @(
"attock|Attock|Punjab","badin|Badin|Sindh","bannu|Bannu|KPK","bhakkar|Bhakkar|Punjab",
"bhimber|Bhimber|AJK","chakwal|Chakwal|Punjab","chaman|Chaman|Balochistan",
"charsadda|Charsadda|KPK","chiniot|Chiniot|Punjab","chitral|Chitral|KPK",
"dadu|Dadu|Sindh","daska|Daska|Punjab","ghotki|Ghotki|Sindh","gilgit|Gilgit|GB",
"gojra|Gojra|Punjab","gujrat|Gujrat|Punjab","gwadar|Gwadar|Balochistan",
"hafizabad|Hafizabad|Punjab","hangu|Hangu|KPK","haripur|Haripur|KPK",
"hub|Hub|Balochistan","hunza|Hunza|GB","jacobabad|Jacobabad|Sindh",
"jhang|Jhang|Punjab","jhelum|Jhelum|Punjab","kamalia|Kamalia|Punjab",
"kamoke|Kamoke|Punjab","karak|Karak|KPK","kasur|Kasur|Punjab",
"khairpur|Khairpur|Sindh","khanewal|Khanewal|Punjab","kharian|Kharian|Punjab",
"khushab|Khushab|Punjab","khuzdar|Khuzdar|Balochistan","kohat|Kohat|KPK",
"kotli|Kotli|AJK","lakki-marwat|Lakki Marwat|KPK","lalamusa|Lalamusa|Punjab",
"layyah|Layyah|Punjab","lodhran|Lodhran|Punjab","loralai|Loralai|Balochistan",
"mansehra|Mansehra|KPK","mandi-bahauddin|Mandi Bahauddin|Punjab","matiari|Matiari|Sindh",
"mingora|Mingora|KPK","mirpur|Mirpur|AJK","mirpurkhas|Mirpurkhas|Sindh",
"muzaffarabad|Muzaffarabad|AJK","muzaffargarh|Muzaffargarh|Punjab",
"narowal|Narowal|Punjab","nawabshah|Nawabshah|Sindh","nowshera|Nowshera|KPK",
"okara|Okara|Punjab","pakpattan|Pakpattan|Punjab","rajanpur|Rajanpur|Punjab",
"rahim-yar-khan|Rahim Yar Khan|Punjab","rawalakot|Rawalakot|AJK",
"sanghar|Sanghar|Sindh","sheikhupura|Sheikhupura|Punjab","shikarpur|Shikarpur|Sindh",
"sibi|Sibi|Balochistan","skardu|Skardu|GB","swabi|Swabi|KPK",
"tando-adam|Tando Adam|Sindh","tando-allahyar|Tando Allahyar|Sindh",
"thatta|Thatta|Sindh","toba-tek-singh|Toba Tek Singh|Punjab","turbat|Turbat|Balochistan",
"vehari|Vehari|Punjab","wah-cantt|Wah Cantt|Punjab","wazirabad|Wazirabad|Punjab",
"zhob|Zhob|Balochistan","jaranwala|Jaranwala|Punjab","sammundri|Sammundri|Punjab",
"burewala|Burewala|Punjab","mian-channu|Mian Channu|Punjab",
"ahmedpur-east|Ahmedpur East|Punjab","sadiqabad|Sadiqabad|Punjab",
"khanpur|Khanpur|Punjab","bhawalnagar|Bhawalnagar|Punjab",
"haroonabad|Haroonabad|Punjab","arifwala|Arifwala|Punjab",
"renala-khurd|Renala Khurd|Punjab","depalpur|Depalpur|Punjab",
"phalia|Phalia|Punjab","malakwal|Malakwal|Punjab","dinga|Dinga|Punjab",
"zafarwal|Zafarwal|Punjab","shakargarh|Shakargarh|Punjab",
"talagang|Talagang|Punjab","dina|Dina|Punjab","sambrial|Sambrial|Punjab",
"pasrur|Pasrur|Punjab","timergara|Timergara|KPK","pishin|Pishin|Balochistan",
"mastung|Mastung|Balochistan","mailsi|Mailsi|Punjab","kabirwala|Kabirwala|Punjab",
"liaquatpur|Liaquatpur|Punjab","chishtian|Chishtian|Punjab","fort-abbas|Fort Abbas|Punjab",
"haveli-lakha|Haveli Lakha|Punjab","lasbela|Lasbela|Balochistan","kalat|Kalat|Balochistan"
)

$itfBody = '<h2>Who Needs to File Income Tax in CITY?</h2><p>FBR requires filing if annual income exceeds Rs. 600,000, or if you want filer status to reduce withholding tax on property, banking, and vehicles.</p><ul><li>Salaried employees - government and private</li><li>Business owners and traders</li><li>Freelancers and consultants</li><li>Landlords with rental income</li><li>Anyone wanting filer benefits on ATL</li></ul><h2>Documents Required</h2><ul><li>CNIC copy (both sides)</li><li>Salary slips or bank statement (12 months)</li><li>NTN number if already registered</li><li>Business income records if applicable</li><li>Any rental, investment, or foreign income details</li></ul><h2>Fee in CITY</h2><table><tr><th>Return Type</th><th>Fee</th><th>Timeline</th></tr><tr><td>Salaried Individual</td><td>Rs. 3,500</td><td>Same day</td></tr><tr><td>Business / Freelancer</td><td>Rs. 5,000</td><td>Same day</td></tr><tr><td>AOP / Partnership</td><td>Rs. 10,000</td><td>1-2 days</td></tr><tr><td>Company Return</td><td>Rs. 15,000+</td><td>2-3 days</td></tr></table><h2>Frequently Asked Questions</h2><div class="faq-list"><div class="faq-item"><div class="faq-q">How to file income tax from CITY? <i class="fas fa-chevron-down"></i></div><div class="faq-a">WhatsApp your CNIC and income documents to 0328-4675162. We file on FBR IRIS same day and send you the filed acknowledgment. No office visit needed from CITY.</div></div><div class="faq-item"><div class="faq-q">What is the penalty for late filing? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Rs. 1,000 per week late, or 0.1% of tax due per day. Non-filers also pay double withholding tax on all major transactions.</div></div></div><div class="highlight-box"><p><strong>File today from CITY.</strong> WhatsApp <a href="https://wa.me/923284675162" style="color:#14B8A6;font-weight:600">0328-4675162</a> - free consultation, response in 30 minutes.</p></div>'

$ntnBody = '<h2>What is NTN and Why Do You Need It?</h2><p>National Tax Number (NTN) is your FBR tax identity. Required for filing tax returns, opening business accounts, property transactions, import/export, and government tenders.</p><h2>Documents for NTN Registration in CITY</h2><ul><li>CNIC copy (both sides)</li><li>Mobile number on your CNIC</li><li>Email address</li><li>Business address (for business NTN)</li><li>SECP certificate for companies</li></ul><h2>NTN Fee in CITY</h2><table><tr><th>Type</th><th>Fee</th><th>Timeline</th></tr><tr><td>Individual NTN</td><td>Rs. 2,000</td><td>Same day</td></tr><tr><td>Company NTN</td><td>Rs. 3,000</td><td>Same day</td></tr><tr><td>NTN + First Tax Return</td><td>Rs. 5,000</td><td>Same day</td></tr></table><h2>Filer Benefits After NTN</h2><ul><li>Bank profit tax: 15% vs 30% (non-filer)</li><li>Property WHT: 3% vs 6%</li><li>Vehicle registration WHT: 2% vs 4%</li><li>Cash withdrawal tax: 0% vs 0.6%</li></ul><h2>Frequently Asked Questions</h2><div class="faq-list"><div class="faq-item"><div class="faq-q">Can I get NTN online from CITY? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Yes. 100% online process. WhatsApp your CNIC copy to 0328-4675162 and your NTN is registered same day on FBR IRIS. No office visit needed from CITY.</div></div><div class="faq-item"><div class="faq-q">How to check NTN status? <i class="fas fa-chevron-down"></i></div><div class="faq-a">SMS your CNIC to 9966 or check iris.fbr.gov.pk. You can also WhatsApp us to verify your NTN status.</div></div></div><div class="highlight-box"><p><strong>Get NTN today from CITY.</strong> WhatsApp <a href="https://wa.me/923284675162" style="color:#14B8A6;font-weight:600">0328-4675162</a> - same day registration.</p></div>'

foreach ($line in $cities) {
  $p = $line -split '\|'; $cslug=$p[0]; $city=$p[1]; $prov=$p[2]

  # income-tax-filing
  $slug = "income-tax-filing-$cslug"
  $title = "Income Tax Return Filing in $city 2026 - Online FBR | Kamboh Associates"
  $desc = "Online income tax return filing in $city 2026 from Rs. 3,500. Salaried, business, freelancer returns. WhatsApp 0328-4675162. Same-day service."
  $kw = "income tax return filing $city, income tax $city 2026, FBR tax filing $city, tax consultant $city income tax"
  $h1 = "Income Tax Return Filing in $city 2026 - 100% Online"
  $lead = "File your income tax return online from $city, $prov without visiting any FBR office. Kamboh Associates handles everything via WhatsApp - salaried, business, and freelancer returns from Rs. 3,500."
  $body = $itfBody -replace 'CITY',$city
  $html = MkPage $slug $title $desc $kw "https://kambohassociates.com/blogs/$slug" "Tax Filing 2026" "fas fa-file-invoice-dollar" $h1 "6 min read" $lead $body
  WB $slug $html

  # ntn-registration
  $slug2 = "ntn-registration-$cslug"
  $title2 = "NTN Registration in $city 2026 - Online FBR NTN | Kamboh Associates"
  $desc2 = "Get NTN number online from $city 2026. Individual Rs. 2,000, Company Rs. 3,000. WhatsApp 0328-4675162. Same-day processing."
  $kw2 = "NTN registration $city, NTN number $city 2026, FBR NTN $city, how to get NTN $city online"
  $h12 = "NTN Registration in $city 2026 - Online Same Day"
  $lead2 = "Get your National Tax Number (NTN) registered online from $city, $prov. Kamboh Associates processes your NTN on FBR IRIS same day via WhatsApp - no office visit required."
  $body2 = $ntnBody -replace 'CITY',$city
  $html2 = MkPage $slug2 $title2 $desc2 $kw2 "https://kambohassociates.com/blogs/$slug2" "FBR Registration" "fas fa-id-card" $h12 "5 min read" $lead2 $body2
  WB $slug2 $html2
}

Write-Host "Script A done. Created: $($script:created) | Skipped: $($script:skipped)"
