$blogDir = "c:\Users\786\Desktop\kam\blogs"

# CSS to inject before </style> in old blog files
$dropCss = '.nav-links>li{position:relative}.nav-chevron{font-size:.6rem;opacity:.6}.nav-drop{position:absolute;top:calc(100% + 8px);left:50%;transform:translateX(-50%) translateY(-6px);min-width:200px;background:#fff;border:1px solid #E2E8F0;border-radius:12px;box-shadow:0 8px 32px rgba(15,23,42,.12);padding:8px;opacity:0;visibility:hidden;pointer-events:none;transition:all .2s}.nav-links>li:hover .nav-drop{opacity:1;visibility:visible;pointer-events:auto;transform:translateX(-50%) translateY(0)}.nav-links>li:last-child .nav-drop{left:auto;right:0;transform:translateY(-6px)}.nav-links>li:last-child:hover .nav-drop{transform:translateY(0)}.nav-drop a{display:flex;align-items:center;gap:10px;padding:9px 12px;border-radius:8px;font-size:.82rem;color:#1E293B;transition:all .15s}.nav-drop a:hover{background:#F0FDFA;color:#14B8A6}.nav-drop a i{width:16px;text-align:center;color:#14B8A6}.nav-drop-divider{height:1px;background:#E2E8F0;margin:4px 8px}'

$files = Get-ChildItem $blogDir -Filter "*.html"
$fixed = 0
$skipped = 0

foreach ($f in $files) {
    $content = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)

    # Skip files that already have nav-drop CSS
    if ($content -like '*nav-drop{position:absolute*') {
        $skipped++
        continue
    }

    # Find </style> and inject before it
    $styleEnd = $content.IndexOf('</style>')
    if ($styleEnd -lt 0) { $skipped++; continue }

    $newContent = $content.Substring(0, $styleEnd) + $dropCss + $content.Substring($styleEnd)
    [System.IO.File]::WriteAllText($f.FullName, $newContent, [System.Text.Encoding]::UTF8)
    $fixed++
}

Write-Host "Old files CSS fixed: $fixed | Skipped: $skipped"
