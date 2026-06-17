$blogsHtmlPath = "C:\Users\786\Desktop\kam\blogs.html"

$slugs = @(
  "tax-consultant-attock-city","tax-consultant-b-17-islamabad","tax-consultant-badin-city",
  "tax-consultant-baghbanpura-lahore","tax-consultant-bahria-precinct-karachi","tax-consultant-bahria-town-rawalpindi",
  "tax-consultant-bannu-city","tax-consultant-bhakkar-city","tax-consultant-bhimber-city",
  "tax-consultant-cavalry-ground-lahore-area","tax-consultant-chaklala-rawalpindi","tax-consultant-chakwal-city",
  "tax-consultant-chaman-city","tax-consultant-charsadda-city","tax-consultant-chiniot-city",
  "tax-consultant-chitral-city","tax-consultant-d-12-islamabad","tax-consultant-dadu-city",
  "tax-consultant-dera-ghazi-khan-city","tax-consultant-dera-ismail-khan-city","tax-consultant-dha-lahore-area",
  "tax-consultant-dha-phase-2-karachi","tax-consultant-dha-phase-6-karachi","tax-consultant-f-9-islamabad",
  "tax-consultant-g-14-islamabad","tax-consultant-g-15-islamabad","tax-consultant-gadap-town-karachi",
  "tax-consultant-garhi-shahu-lahore","tax-consultant-ghotki-city","tax-consultant-gilgit-city",
  "tax-consultant-gujrat-city","tax-consultant-gulshan-e-maymar-karachi","tax-consultant-gulshan-ravi-lahore-area",
  "tax-consultant-gwadar-city","tax-consultant-h-10-islamabad","tax-consultant-h-9-islamabad",
  "tax-consultant-hafizabad-city","tax-consultant-hangu-city","tax-consultant-harbanspura-lahore",
  "tax-consultant-haripur-city","tax-consultant-hub-city","tax-consultant-hunza-city",
  "tax-consultant-ichra-lahore","tax-consultant-jacobabad-city","tax-consultant-jhang-city",
  "tax-consultant-jhelum-city","tax-consultant-johar-town-lahore-area","tax-consultant-karak-city",
  "tax-consultant-kasur-city","tax-consultant-khairpur-city","tax-consultant-khanewal-city",
  "tax-consultant-kharan-city","tax-consultant-khushab-city","tax-consultant-khuzdar-city",
  "tax-consultant-kohat-city","tax-consultant-kot-lakhpat-lahore","tax-consultant-kotli-city",
  "tax-consultant-krishan-nagar-lahore","tax-consultant-lakki-marwat-city","tax-consultant-landhi-industrial-karachi",
  "tax-consultant-layyah-city","tax-consultant-lodhran-city","tax-consultant-loralai-city",
  "tax-consultant-malir-city-karachi","tax-consultant-mandi-bahauddin-city","tax-consultant-manga-mandi-lahore",
  "tax-consultant-manghopir-karachi","tax-consultant-mansehra-city","tax-consultant-matiari-city",
  "tax-consultant-mingora-swat","tax-consultant-mirpurkhas-city","tax-consultant-mozang-lahore",
  "tax-consultant-mughalpura-lahore","tax-consultant-muzaffargarh-city","tax-consultant-narowal-city",
  "tax-consultant-nishtar-colony-lahore","tax-consultant-north-karachi-karachi","tax-consultant-nowshera-city",
  "tax-consultant-okara-city","tax-consultant-pakpattan-city","tax-consultant-raiwind-lahore",
  "tax-consultant-rajanpur-city","tax-consultant-rawalakot-city","tax-consultant-samanabad-lahore-area",
  "tax-consultant-sanghar-city","tax-consultant-satellite-town-rawalpindi","tax-consultant-scheme-33-karachi",
  "tax-consultant-scheme-45-karachi","tax-consultant-shadman-lahore-area","tax-consultant-shah-latif-town-karachi",
  "tax-consultant-shahdara-lahore","tax-consultant-shalamar-lahore","tax-consultant-sheikhupura-city",
  "tax-consultant-shikarpur-city","tax-consultant-sibi-city","tax-consultant-skardu-city",
  "tax-consultant-sundar-lahore","tax-consultant-swabi-city","tax-consultant-tando-adam-city",
  "tax-consultant-tando-allahyar-city","tax-consultant-tank-city","tax-consultant-taxila-rawalpindi",
  "tax-consultant-thatta-city","tax-consultant-toba-tek-singh-city","tax-consultant-turbat-city",
  "tax-consultant-umerkot-city","tax-consultant-vehari-city","tax-consultant-wah-cantt-rawalpindi",
  "tax-consultant-westridge-rawalpindi","tax-consultant-zhob-city"
)

function Get-Category($slug) {
  if ($slug -match "lahore|baghbanpura|cavalry-ground|dha-lahore|garhi-shahu|gulshan-ravi|harbanspura|ichra|johar-town-lahore|kot-lakhpat|krishan-nagar|manga-mandi|mozang|mughalpura|nishtar-colony|raiwind|samanabad|shadman|shalamar|shahdara|sundar-lahore") { return "Lahore Local" }
  if ($slug -match "karachi|bahria-precinct|dha-phase|gadap|gulshan-e-maymar|landhi|malir|manghopir|north-karachi|scheme-33|scheme-45|shah-latif") { return "Karachi Local" }
  if ($slug -match "b-17|d-12|f-9|g-14|g-15|h-10|h-9") { return "Islamabad Local" }
  if ($slug -match "rawalpindi|chaklala|satellite-town|taxila|wah-cantt|westridge") { return "Islamabad Local" }
  if ($slug -match "bannu|charsadda|chitral|hangu|haripur|karak|kohat|lakki-marwat|mansehra|mingora|nowshera|swabi|tank") { return "Peshawar Local" }
  if ($slug -match "chaman|kharan|khuzdar|loralai|sibi|turbat|zhob") { return "Quetta Local" }
  if ($slug -match "badin|dadu|ghotki|jacobabad|khairpur|matiari|mirpurkhas|sanghar|shikarpur|tando-adam|tando-allahyar|thatta|umerkot") { return "Hyderabad Local" }
  return "Other Cities"
}

function Get-Title($slug) {
  $name = $slug -replace "^tax-consultant-",""
  $name = $name -replace "-city$",""
  $name = $name -replace "-lahore-area$"," Lahore"
  $name = $name -replace "-lahore$"," Lahore"
  $name = $name -replace "-karachi$"," Karachi"
  $name = $name -replace "-rawalpindi$"," Rawalpindi"
  $name = $name -replace "-islamabad$"," Islamabad"
  $name = $name -replace "-swat$"," Swat"
  $name = $name -replace "-industrial$"," Industrial"
  $words = ($name -replace "-"," ").Split(" ") | ForEach-Object {
    if ($_.Length -gt 0) { $_.Substring(0,1).ToUpper() + $_.Substring(1).ToLower() } else { $_ }
  }
  $cityName = ($words -join " ").Trim()
  return "Best Tax Consultant in $cityName 2026"
}

$d = [DateTime]"2027-05-02"
$entries = [System.Collections.Generic.List[string]]::new()

foreach ($slug in $slugs) {
  $title = Get-Title $slug
  $cat = Get-Category $slug
  $cityDisplay = $title -replace "Best Tax Consultant in ","" -replace " 2026",""
  $excerpt = "Trusted tax consultant in $cityDisplay. NTN registration, income tax filing, FBR compliance, active filer status. Remote service available via WhatsApp."
  $dateStr = $d.ToString("yyyy-MM-dd")
  $entry = "  { id:""$slug"", title:""$title"", excerpt:""$excerpt"", date:""$dateStr"", category:""$cat"", readTime:""7 min read"", author:""Kamboh Associates"", icon:""&#x1F4CD;"", link:""/blogs/$slug"" },"
  $entries.Add($entry)
  $d = $d.AddDays(1)
}

$content = [System.IO.File]::ReadAllText($blogsHtmlPath)
$block = $entries -join "`n"
$updated = $content.Replace("`n];", "`n$block`n];")
[System.IO.File]::WriteAllText($blogsHtmlPath, $updated, [System.Text.Encoding]::UTF8)

Write-Host "Added $($entries.Count) entries to blogs.html"
$newCount = ([System.Text.RegularExpressions.Regex]::Matches([System.IO.File]::ReadAllText($blogsHtmlPath), 'link:"/blogs/')).Count
Write-Host "Total entries in blogs.html: $newCount"
