$blogDir = "c:\Users\786\Desktop\kam\blogs"

$oldCss = '.nav-links>li:hover .nav-drop{opacity:1;visibility:visible;pointer-events:auto;transform:translateX(-50%) translateY(0)}'
$newCss = '.nav-links>li:hover .nav-drop{opacity:1;visibility:visible;pointer-events:auto;transform:translateX(-50%) translateY(0)}.nav-links>li:last-child .nav-drop{left:auto;right:0;transform:translateY(-6px);}.nav-links>li:last-child:hover .nav-drop{transform:translateY(0);}'

$files = Get-ChildItem $blogDir -Filter "*.html"
$fixed = 0
$skipped = 0

foreach ($f in $files) {
    $content = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)

    if ($content -like '*nav-links>li:last-child .nav-drop*') {
        $skipped++
        continue
    }

    if ($content -like '*nav-links>li:hover .nav-drop*') {
        $newContent = $content.Replace($oldCss, $newCss)
        [System.IO.File]::WriteAllText($f.FullName, $newContent, [System.Text.Encoding]::UTF8)
        $fixed++
    } else {
        $skipped++
    }
}

Write-Host "CSS fixed in $fixed files. Skipped: $skipped"
