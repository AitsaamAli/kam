$sitemapPath = "c:\Users\786\Desktop\kam\sitemap.xml"
$content = [System.IO.File]::ReadAllText($sitemapPath, [System.Text.Encoding]::UTF8)

# Get all blog HTML files and build URLs
$blogDir = "c:\Users\786\Desktop\kam\blogs"
$files = Get-ChildItem $blogDir -Filter "*.html" | Select-Object -ExpandProperty BaseName

# Get existing URLs from sitemap
$existingSlugs = [System.Collections.Generic.HashSet[string]]::new()
$matches = [System.Text.RegularExpressions.Regex]::Matches($content, 'kambohassociates\.com/blogs/([^<]+)')
foreach ($m in $matches) { $existingSlugs.Add($m.Groups[1].Value) | Out-Null }

Write-Host "Existing slugs in sitemap: $($existingSlugs.Count)"
Write-Host "Total blog files: $($files.Count)"

$newUrls = ""
foreach ($slug in $files) {
    if (-not $existingSlugs.Contains($slug)) {
        $newUrls += "`n  <url><loc>https://kambohassociates.com/blogs/$slug</loc><lastmod>2026-06-18</lastmod><changefreq>monthly</changefreq><priority>0.80</priority></url>"
    }
}

$replacement = $newUrls + "`n</urlset>"
$newContent = $content.Replace('</urlset>', $replacement)
[System.IO.File]::WriteAllText($sitemapPath, $newContent, [System.Text.Encoding]::UTF8)
Write-Host "Sitemap updated with new URLs"
