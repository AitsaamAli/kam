$blogDir = "c:\Users\786\Desktop\kam\blogs"
$sitemapPath = "c:\Users\786\Desktop\kam\sitemap.xml"

# Static pages
$staticUrls = @(
"https://kambohassociates.com/|1.0",
"https://kambohassociates.com/income-tax-filing|0.95",
"https://kambohassociates.com/ntn-registration|0.95",
"https://kambohassociates.com/sales-tax-registration|0.95",
"https://kambohassociates.com/pricing|0.90",
"https://kambohassociates.com/contact|0.85",
"https://kambohassociates.com/blogs|0.90"
)

$xml = '<?xml version="1.0" encoding="UTF-8"?>' + "`n"
$xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "`n"

foreach ($u in $staticUrls) {
    $p = $u -split '\|'
    $xml += "  <url><loc>$($p[0])</loc><lastmod>2026-06-18</lastmod><changefreq>weekly</changefreq><priority>$($p[1])</priority></url>`n"
}

$files = Get-ChildItem $blogDir -Filter "*.html" | Select-Object -ExpandProperty BaseName
foreach ($slug in $files) {
    $xml += "  <url><loc>https://kambohassociates.com/blogs/$slug</loc><lastmod>2026-06-18</lastmod><changefreq>monthly</changefreq><priority>0.80</priority></url>`n"
}

$xml += '</urlset>'
[System.IO.File]::WriteAllText($sitemapPath, $xml, [System.Text.Encoding]::UTF8)
Write-Host "Sitemap regenerated with $($files.Count) blog URLs + $($staticUrls.Count) static pages"
