$pages = @(
    "c:\Users\786\Desktop\kam\fbr-notice-defense.html",
    "c:\Users\786\Desktop\kam\wealth-statement.html",
    "c:\Users\786\Desktop\kam\withholding-tax.html",
    "c:\Users\786\Desktop\kam\corporate-tax-return.html",
    "c:\Users\786\Desktop\kam\sales-tax-return.html",
    "c:\Users\786\Desktop\kam\eobi-registration.html"
)

foreach ($path in $pages) {
    $c = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)

    # Fix all garbled em-dash variants
    $c = $c.Replace('â€&rdquo;', '&mdash;')
    $c = $c.Replace('â€&ldquo;', '&mdash;')
    $c = $c.Replace('â€œ', '&ldquo;')
    $c = $c.Replace('â€', '&mdash;')   # catch any remaining

    [System.IO.File]::WriteAllText($path, $c, [System.Text.Encoding]::UTF8)
    Write-Host "Fixed: $([System.IO.Path]::GetFileName($path))"
}
