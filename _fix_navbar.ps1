$blogDir = "c:\Users\786\Desktop\kam\blogs"

# Correct navbar - same as old blogs
$correctNav = @'
<div class="topbar"><div class="container"><div class="topbar-left"><div class="topbar-promo-wrap"><span class="topbar-promo">FBR NOTICE? CALL KAMBOH ASSOCIATES NOW &nbsp;&bull;&nbsp; 0328-4675162 &nbsp;&bull;&nbsp; EXPERT NOTICE RESPONSE &nbsp;&bull;&nbsp; FBR NOTICE DEFENSE &nbsp;&bull;&nbsp; DON'T IGNORE &mdash; CALL NOW 0328-4675162 &nbsp;&bull;&nbsp;</span></div></div></div></div>
<nav class="navbar" id="navbar">
  <div class="container">
    <a href="/" class="logo">
      <div><svg width="44" height="44" viewBox="0 0 46 46" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1a3a1a"/><stop offset="100%" stop-color="#0d2a0d"/></linearGradient><linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#F0CF6B"/><stop offset="100%" stop-color="#D4AF37"/></linearGradient></defs><circle cx="23" cy="23" r="23" fill="url(#logoGrad)"/><circle cx="23" cy="23" r="21" fill="none" stroke="url(#goldGrad)" stroke-width="1.5"/><text x="23" y="27" font-family="Cinzel,serif" font-size="13" font-weight="700" fill="url(#goldGrad)" text-anchor="middle" letter-spacing="1">KA</text><path id="circle-path" d="M 23,23 m -17,0 a 17,17 0 1,1 34,0 a 17,17 0 1,1 -34,0" fill="none"/><text font-family="Cinzel,serif" font-size="3.8" fill="#D4AF37" letter-spacing="1.8"><textPath href="#circle-path" startOffset="3%">KAMBOH ASSOCIATES &bull; TAX CONSULTANT &bull;</textPath></text></svg></div>
      <div><div class="logo-name">KAMBOH ASSOCIATES</div><div class="logo-sub">Tax &amp; Regulatory Excellence</div></div>
    </a>
    <ul class="nav-links">
      <li><a href="/">Home</a></li>
      <li>
        <a href="/income-tax-filing">Services <i class="fas fa-chevron-down nav-chevron"></i></a>
        <div class="nav-drop">
          <a href="/income-tax-filing"><i class="fas fa-file-invoice-dollar"></i> Income Tax Filing</a>
          <a href="/ntn-registration"><i class="fas fa-id-card"></i> NTN Registration</a>
          <a href="/sales-tax-registration"><i class="fas fa-percent"></i> Sales Tax Registration</a>
          <a href="/secp-vs-sole-proprietorship-pakistan"><i class="fas fa-building"></i> SECP Company Registration</a>
          <div class="nav-drop-divider"></div>
          <a href="/business-advisory"><i class="fas fa-chart-line"></i> Business Advisory</a>
          <div class="nav-drop-divider"></div>
          <a href="/pricing"><i class="fas fa-tags"></i> Pricing &amp; Fees</a>
        </div>
      </li>
      <li>
        <a href="/#tools">Tools <i class="fas fa-chevron-down nav-chevron"></i></a>
        <div class="nav-drop">
          <a href="/tax-calculator"><i class="fas fa-calculator"></i> Tax Calculator</a>
          <a href="/salary-calculator"><i class="fas fa-user-tie"></i> Salary Calculator</a>
          <a href="/gst-calculator"><i class="fas fa-percent"></i> GST Calculator</a>
          <a href="/income-estimator"><i class="fas fa-chart-bar"></i> Income Estimator</a>
        </div>
      </li>
      <li><a href="/#deadlines">Deadlines</a></li>
      <li><a href="/pricing">Pricing</a></li>
      <li><a href="/contact">Contact</a></li>
      <li>
        <a href="/blogs">Blog <i class="fas fa-chevron-down nav-chevron"></i></a>
        <div class="nav-drop">
          <a href="/blogs"><i class="fas fa-landmark"></i> FBR &amp; Tax Guides</a>
          <a href="/blogs"><i class="fas fa-user-clock"></i> Freelancer Tax</a>
          <a href="/blogs"><i class="fas fa-store"></i> E-Commerce Tax</a>
          <a href="/blogs"><i class="fas fa-building"></i> Business &amp; SECP</a>
        </div>
      </li>
    </ul>
    <div class="nav-actions">
      <span class="nav-phone"><i class="fas fa-phone"></i><a href="tel:03284675162">0328-4675162</a></span>
      <a href="/contact" class="nav-cta">Get Started</a>
      <button class="hamburger" id="hamburger" onclick="this.classList.toggle('open');document.getElementById('mobileNav').classList.toggle('open')" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>
<div class="mobile-nav" id="mobileNav">
  <a href="/">Home</a>
  <a href="/income-tax-filing">Services</a>
  <a href="/#tools">Tools</a>
  <a href="/#deadlines">Tax Deadlines</a>
  <a href="/pricing">Pricing &amp; Fees</a>
  <a href="/blogs">Blog</a>
  <a href="/contact">Contact</a>
  <a href="https://wa.me/923284675162" target="_blank" style="color:#25D366"><i class="fab fa-whatsapp" style="margin-right:8px"></i>WhatsApp Advisory</a>
</div>

'@

$files = Get-ChildItem $blogDir -Filter "*.html"
$fixed = 0
$skipped = 0

foreach ($f in $files) {
    $content = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)

    # Only fix files that have our simple navbar (missing Tools/tax-calculator)
    if ($content -notlike '*href="/tax-calculator"*') {
        # Find <body> end tag position
        $bodyIdx = $content.IndexOf('<body>')
        if ($bodyIdx -lt 0) { $skipped++; continue }
        $afterBody = $bodyIdx + 6  # length of '<body>'

        # Find where blog-hero section starts
        $heroIdx = $content.IndexOf('<section class="blog-hero">')
        if ($heroIdx -lt 0) { $skipped++; continue }

        # Replace everything between <body> and <section class="blog-hero">
        $newContent = $content.Substring(0, $afterBody) + "`n" + $correctNav + $content.Substring($heroIdx)
        [System.IO.File]::WriteAllText($f.FullName, $newContent, [System.Text.Encoding]::UTF8)
        $fixed++
    } else {
        $skipped++
    }
}

Write-Host "Navbar fixed in $fixed files. Skipped (already correct): $skipped"
