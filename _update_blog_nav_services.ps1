# Update Services dropdown in blogs.html AND all 1000 blog files
# The blog nav-drop for Services has these old links — we add new ones after SECP

$dirs = @("c:\Users\786\Desktop\kam", "c:\Users\786\Desktop\kam\blogs")

# Pattern present in blog files (includes SECP and business-advisory)
$oldBlock = '<a href="/secp-vs-sole-proprietorship-pakistan"><i class="fas fa-building"></i> SECP Company Registration</a>' + "`n" + '          <div class="nav-drop-divider"></div>' + "`n" + '          <a href="/business-advisory"><i class="fas fa-chart-line"></i> Business Advisory</a>' + "`n" + '          <div class="nav-drop-divider"></div>' + "`n" + '          <a href="/pricing"><i class="fas fa-tags"></i> Pricing &amp; Fees</a>'

$newBlock = '<a href="/secp-vs-sole-proprietorship-pakistan"><i class="fas fa-building"></i> SECP Company Registration</a>' + "`n" + '          <div class="nav-drop-divider"></div>' + "`n" + '          <a href="/sales-tax-return"><i class="fas fa-file-alt"></i> Sales Tax Return</a>' + "`n" + '          <a href="/corporate-tax-return"><i class="fas fa-building"></i> Corporate Tax Return</a>' + "`n" + '          <a href="/fbr-notice-defense"><i class="fas fa-shield-alt"></i> FBR Notice Defense</a>' + "`n" + '          <a href="/wealth-statement"><i class="fas fa-wallet"></i> Wealth Statement</a>' + "`n" + '          <a href="/withholding-tax"><i class="fas fa-hand-holding-usd"></i> Withholding Tax</a>' + "`n" + '          <a href="/eobi-registration"><i class="fas fa-users"></i> EOBI Registration</a>' + "`n" + '          <div class="nav-drop-divider"></div>' + "`n" + '          <a href="/business-advisory"><i class="fas fa-chart-line"></i> Business Advisory</a>' + "`n" + '          <div class="nav-drop-divider"></div>' + "`n" + '          <a href="/pricing"><i class="fas fa-tags"></i> Pricing &amp; Fees</a>'

$fixed = 0; $skipped = 0

foreach ($dir in $dirs) {
    $files = Get-ChildItem $dir -Filter "*.html" -File
    foreach ($f in $files) {
        $c = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
        if ($c.Contains($oldBlock)) {
            $newC = $c.Replace($oldBlock, $newBlock)
            [System.IO.File]::WriteAllText($f.FullName, $newC, [System.Text.Encoding]::UTF8)
            $fixed++
        } else {
            $skipped++
        }
    }
}

Write-Host "Services nav updated in $fixed files. Skipped: $skipped"
