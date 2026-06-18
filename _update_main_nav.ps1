$dir = "c:\Users\786\Desktop\kam"

$oldDrop = '<div class="nav-drop">' + "`n" + '          <a href="/income-tax-filing"><i class="fas fa-file-invoice-dollar"></i> Income Tax Filing</a>' + "`n" + '          <a href="/ntn-registration"><i class="fas fa-id-card"></i> NTN Registration</a>' + "`n" + '          <a href="/sales-tax-registration"><i class="fas fa-percent"></i> Sales Tax Registration</a>' + "`n" + '          <a href="/business-advisory"><i class="fas fa-chart-line"></i> Business Advisory</a>' + "`n" + '        </div>'

$newDrop = '<div class="nav-drop">' + "`n" + '          <a href="/income-tax-filing"><i class="fas fa-file-invoice-dollar"></i> Income Tax Filing</a>' + "`n" + '          <a href="/ntn-registration"><i class="fas fa-id-card"></i> NTN Registration</a>' + "`n" + '          <a href="/sales-tax-registration"><i class="fas fa-percent"></i> Sales Tax Registration</a>' + "`n" + '          <a href="/sales-tax-return"><i class="fas fa-file-alt"></i> Sales Tax Return</a>' + "`n" + '          <a href="/corporate-tax-return"><i class="fas fa-building"></i> Corporate Tax Return</a>' + "`n" + '          <a href="/fbr-notice-defense"><i class="fas fa-shield-alt"></i> FBR Notice Defense</a>' + "`n" + '          <a href="/wealth-statement"><i class="fas fa-wallet"></i> Wealth Statement</a>' + "`n" + '          <a href="/withholding-tax"><i class="fas fa-hand-holding-usd"></i> Withholding Tax</a>' + "`n" + '          <a href="/eobi-registration"><i class="fas fa-users"></i> EOBI Registration</a>' + "`n" + '          <a href="/secp-vs-sole-proprietorship-pakistan"><i class="fas fa-building-columns"></i> SECP Registration</a>' + "`n" + '          <a href="/business-advisory"><i class="fas fa-chart-line"></i> Business Advisory</a>' + "`n" + '          <a href="/pricing"><i class="fas fa-tags"></i> Pricing &amp; Fees</a>' + "`n" + '        </div>'

$files = Get-ChildItem $dir -Filter "*.html" -File
$fixed = 0; $skipped = 0

foreach ($f in $files) {
    $c = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
    if ($c.Contains($oldDrop)) {
        $newC = $c.Replace($oldDrop, $newDrop)
        [System.IO.File]::WriteAllText($f.FullName, $newC, [System.Text.Encoding]::UTF8)
        $fixed++
    } else {
        $skipped++
    }
}
Write-Host "Navbar updated in $fixed files. Skipped: $skipped"
