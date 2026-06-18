$dirs = @("c:\Users\786\Desktop\kam", "c:\Users\786\Desktop\kam\blogs")

$fixed = 0
foreach ($dir in $dirs) {
    $files = Get-ChildItem $dir -Filter "*.html" -File
    foreach ($f in $files) {
        $c = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
        $orig = $c

        # Use [string] cast to force string overload of Replace
        $c = $c.Replace([string][char]0x2014, '&mdash;')  # em dash
        $c = $c.Replace([string][char]0x2013, '&ndash;')  # en dash
        $c = $c.Replace([string][char]0x2018, '&lsquo;')  # left single quote
        $c = $c.Replace([string][char]0x2019, '&rsquo;')  # right single quote
        $c = $c.Replace([string][char]0x201C, '&ldquo;')  # left double quote
        $c = $c.Replace([string][char]0x201D, '&rdquo;')  # right double quote
        $c = $c.Replace([string][char]0x00A0, '&nbsp;')   # non-breaking space
        $c = $c.Replace([string][char]0x2022, '&bull;')   # bullet

        if ($c -ne $orig) {
            [System.IO.File]::WriteAllText($f.FullName, $c, [System.Text.Encoding]::UTF8)
            $fixed++
        }
    }
}

Write-Host "Encoding fixed in $fixed files"
