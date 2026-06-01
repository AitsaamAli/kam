const fs = require('fs');
// Use doctors page as template — replace specific sections per blog

const doctorsHtml = fs.readFileSync('tax-filing-doctors-pakistan.html', 'utf8');

function makeBlog(slug, titleStr, descStr, keywordsStr, imgFile, metaTagIcon, metaTagText, h1Str, leadStr, bodyHtml, tocItems, related1, related2, related3, waText, schemaHeadline) {
  let html = doctorsHtml;

  // Title
  html = html.replace(/Tax Filing for Doctors in Pakistan 2026 — Complete FBR Guide \| Kamboh Associates/, titleStr + ' | Kamboh Associates');

  // Meta desc
  html = html.replace(/content="Complete income tax guide for doctors in Pakistan 2026\. Private practice, hospital salary, clinic expenses, advance tax, FBR IRIS filing — expert guide by Kamboh Associates Lahore\."/, 'content="' + descStr + '"');

  // Meta keywords
  html = html.replace(/content="tax filing for doctors Pakistan, doctor income tax Pakistan, private practice tax Pakistan, FBR tax doctor, doctor NTN registration Pakistan, medical professional tax Lahore"/, 'content="' + keywordsStr + '"');

  // og:title
  html = html.replace(/content="Tax Filing for Doctors in Pakistan 2026 \| Kamboh Associates"/, 'content="' + titleStr + ' | Kamboh Associates"');

  // og:description
  html = html.replace(/content="Complete income tax guide for doctors in Pakistan\. Private practice, hospital salary, clinic expenses, advance tax, FBR IRIS filing 2026\."/, 'content="' + descStr + '"');

  // og:url and og:image
  html = html.replace(/content="https:\/\/kambohassociates\.com\/tax-filing-doctors-pakistan"/, 'content="https://kambohassociates.com/' + slug + '"');
  html = html.replace(/content="https:\/\/kambohassociates\.com\/images\/tax-filing-doctors-pakistan\.png"/, 'content="https://kambohassociates.com/images/' + imgFile + '"');

  // twitter:title
  html = html.replace(/content="Tax Filing for Doctors in Pakistan 2026 \| Kamboh Associates"\s*\/>\s*<link rel="canonical"/, 'content="' + titleStr + ' | Kamboh Associates"/>\n<link rel="canonical"');

  // canonical
  html = html.replace(/href="https:\/\/kambohassociates\.com\/tax-filing-doctors-pakistan"\/>/, 'href="https://kambohassociates.com/' + slug + '"/>');

  // Schema - replace the whole script block (simplified: just change headline and image)
  html = html.replace(/"headline":"Tax Filing for Doctors in Pakistan 2026 — Complete FBR Guide"/, '"headline":"' + schemaHeadline + '"');
  html = html.replace(/"image":"https:\/\/kambohassociates\.com\/images\/tax-filing-doctors-pakistan\.png"/g, '"image":"https://kambohassociates.com/images/' + imgFile + '"');
  html = html.replace(/"@id":"https:\/\/kambohassociates\.com\/tax-filing-doctors-pakistan"/, '"@id":"https://kambohassociates.com/' + slug + '"');
  html = html.replace(/"item":"https:\/\/kambohassociates\.com\/tax-filing-doctors-pakistan"/, '"item":"https://kambohassociates.com/' + slug + '"');
  html = html.replace(/"name":"Tax Filing for Doctors in Pakistan 2026","item"/, '"name":"' + titleStr + '","item"');

  // Breadcrumb span
  html = html.replace(/<span>Tax Filing for Doctors Pakistan<\/span>/, '<span>' + metaTagText + '</span>');

  // Meta tag icon and label
  html = html.replace(/class="fas fa-stethoscope"><\/i> Professional Tax Guide/, 'class="' + metaTagIcon + '"></i> Professional Tax Guide');

  // H1
  html = html.replace(/<h1>Tax Filing for Doctors in Pakistan 2026 — Complete FBR Guide<\/h1>/, '<h1>' + h1Str + '</h1>');

  // Lead paragraph
  html = html.replace(/<p class="article-lead">[\s\S]*?<\/p>/, '<p class="article-lead">' + leadStr + '</p>');

  // Featured image
  html = html.replace(/src="\/images\/tax-filing-doctors-pakistan\.png" alt="Tax Filing for Doctors in Pakistan 2026 — complete FBR income tax guide by Kamboh Associates"/, 'src="/images/' + imgFile + '" alt="' + h1Str + ' — guide by Kamboh Associates"');

  // Article body - replace everything between lead and article-cta
  const bodyStart = html.indexOf('</p>\n\n        <h2 id="who-must-file">');
  const ctaStart = html.indexOf('<div class="article-cta">');
  if (bodyStart > 0 && ctaStart > 0) {
    html = html.substring(0, bodyStart + 5) + '\n\n        ' + bodyHtml;
    // Re-get ctaStart since html changed
  }

  // TOC
  const tocStart = html.indexOf('<li class="toc-item"><a href="#who-must-file">');
  const tocEnd = html.indexOf('</ul>\n      </div>');
  if (tocStart > 0 && tocEnd > 0) {
    html = html.substring(0, tocStart) + tocItems + html.substring(tocEnd);
  }

  // Related posts sidebar
  const relStart = html.indexOf('<div class="related-post" onclick="window.location.href=\'/income-tax-filing\'">');
  const relEnd = html.indexOf('</div>\n      </div>\n      <div class="sidebar-card reveal" style="transition-delay:.25s">');
  if (relStart > 0 && relEnd > 0) {
    html = html.substring(0, relStart) + related1 + related2 + related3 + html.substring(relEnd);
  }

  // WA button text
  html = html.replace(/Hi%20Kamboh%20Associates%2C%20doctor%20tax%20filing%20ke%20bare%20mein%20guide%20chahiye\./, waText);

  // Share title
  html = html.replace(/'Tax Filing for Doctors in Pakistan 2026 — Kamboh Associates'/, "'" + titleStr + " — Kamboh Associates'");

  // Consult card sidebar title
  html = html.replace(/Doctor Tax Expert/, metaTagText);
  html = html.replace(/Kamboh Associates handles complete tax filing for medical professionals\. Private practice, hospital income, wealth statements\./, 'Kamboh Associates handles complete tax filing for professionals across Pakistan — NTN, returns, and wealth statements.');

  return html;
}

// Engineers
const engBody = `<h2 id="who-must-file">Who Must File?</h2>
        <p>All engineers earning above <strong>Rs 600,000 annually</strong> must file an income tax return with FBR — including salaried engineers, freelancers, and those running consulting firms.</p>
        <div class="info-box"><i class="fas fa-lightbulb"></i><p><strong>Software engineers:</strong> If you earn in foreign currency through Upwork or direct client payments, you may qualify for the <strong>0.25% fixed income tax on foreign remittances</strong> — a major saving versus normal slab rates up to 35%.</p></div>
        <h2 id="income-types">Income Types for Engineers</h2>
        <ul>
          <li><strong>Salary income:</strong> Monthly pay from employer — employer deducts tax at source</li>
          <li><strong>Consultancy fees:</strong> Project-based income — 7.5% WHT deducted by corporate clients</li>
          <li><strong>Freelance contracts:</strong> Direct client payments via bank or digital transfer</li>
          <li><strong>Foreign remittances:</strong> Overseas payments — potentially 0.25% final tax</li>
        </ul>
        <h2 id="deductions">Deductible Expenses for Engineers</h2>
        <ul>
          <li><strong>Laptop and workstation:</strong> 30% annual depreciation on IT equipment</li>
          <li><strong>Engineering software:</strong> AutoCAD, MATLAB, SolidWorks, VS Code paid plans</li>
          <li><strong>PEC registration:</strong> Pakistan Engineering Council annual membership fee</li>
          <li><strong>Home office:</strong> Proportionate share of rent and utilities if working from home</li>
          <li><strong>Professional development:</strong> Engineering certifications, courses, seminars</li>
          <li><strong>Vehicle and travel:</strong> Site visits and client meetings (maintain mileage log)</li>
        </ul>
        <h2 id="tax-slabs">The 0.25% Foreign Income Benefit</h2>
        <p>Engineers (especially software engineers) who receive foreign currency via official banking channels can opt for <strong>0.25% income tax as a final tax</strong> on those remittances — far lower than normal slab rates. Requirements: payment via Pakistani bank, from overseas client, registered NTN, service exported.</p>
        <h2 id="how-to-file">How to File Your Return</h2>
        <ol>
          <li>Register on FBR IRIS (iris.fbr.gov.pk) — get your NTN</li>
          <li>Collect salary certificates, client invoices, and WHT certificates</li>
          <li>Open IRIS → Declaration → Income Tax Return (Form IT-2)</li>
          <li>Enter all income heads — salary and/or business/freelance income</li>
          <li>Claim deductible expenses under business income section</li>
          <li>Apply all WHT credits and complete wealth statement</li>
          <li>Pay balance tax via PSID and submit before September 30</li>
        </ol>
        <div class="article-cta">
          <h3>Need Help Filing Your Engineer Tax Return?</h3>
          <p>Kamboh Associates helps engineers with NTN registration, freelance income declarations, and foreign income claims.</p>
          <div class="cta-btns">
            <a href="https://wa.me/923284675162?text=Hi%2C%20I%20am%20an%20engineer%20and%20need%20help%20with%20tax%20filing." class="cta-btn-white" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp"></i> Free Consultation</a>
            <a href="tel:03284675162" class="cta-btn-ghost"><i class="fas fa-phone"></i> Call: 0328-4675162</a>
          </div>
        </div>
        <h2 id="faqs">Frequently Asked Questions</h2>
        <div class="faq-list">
          <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">Do engineers need to file income tax in Pakistan?<i class="fas fa-plus"></i></div><div class="faq-a">Yes. All engineers earning above Rs 600,000 annually must file with FBR. Salaried engineers use salary certificate; freelance engineers file under business income.</div></div>
          <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">What is the 0.25% tax for software engineers?<i class="fas fa-plus"></i></div><div class="faq-a">IT engineers receiving foreign currency via Pakistani banks can pay just 0.25% as final income tax on those remittances under SRO 1487(I)/2022 — instead of normal slab rates up to 35%.</div></div>
          <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">Can engineers deduct PEC membership fees?<i class="fas fa-plus"></i></div><div class="faq-a">Yes. PEC annual membership and renewal fees are deductible as professional expenses for engineers running a private practice or consultancy.</div></div>
        </div>`;

const engTOC = `<li class="toc-item"><a href="#who-must-file"><i class="fas fa-circle"></i> Who Must File?</a></li>
          <li class="toc-item"><a href="#income-types"><i class="fas fa-circle"></i> Income Types</a></li>
          <li class="toc-item"><a href="#deductions"><i class="fas fa-circle"></i> Deductible Expenses</a></li>
          <li class="toc-item"><a href="#tax-slabs"><i class="fas fa-circle"></i> 0.25% Foreign Benefit</a></li>
          <li class="toc-item"><a href="#how-to-file"><i class="fas fa-circle"></i> How to File</a></li>
          <li class="toc-item"><a href="#faqs"><i class="fas fa-circle"></i> FAQs</a></li>`;

const engR1 = `<div class="related-post" onclick="window.location.href='/tax-filing-consultants-pakistan'"><div class="related-post-icon">💼</div><div><div class="related-post-title">Tax Filing for Consultants</div><div class="related-post-cat">Professional Tax</div></div></div>`;
const engR2 = `<div class="related-post" onclick="window.location.href='/tax-filing-architects-pakistan'"><div class="related-post-icon">🏗️</div><div><div class="related-post-title">Tax Filing for Architects</div><div class="related-post-cat">Professional Tax</div></div></div>`;
const engR3 = `<div class="related-post" onclick="window.location.href='/tax-benefits-filer-pakistan'"><div class="related-post-icon">✅</div><div><div class="related-post-title">Tax Benefits of Being a Filer</div><div class="related-post-cat">Tax Guide</div></div></div>`;

const engHtml = makeBlog('tax-filing-engineers-pakistan','Tax Filing for Engineers in Pakistan 2026 — Complete FBR Guide','Complete income tax guide for engineers in Pakistan 2026. Civil, mechanical, electrical, software engineers — salaried vs freelance, deductions, 0.25% foreign tax, FBR IRIS filing.','tax filing for engineers Pakistan, engineer income tax Pakistan, software engineer tax Pakistan, FBR tax engineers, 0.25% foreign income tax Pakistan','tax-filing-engineers-pakistan.png','fas fa-cogs','Tax Filing for Engineers','Tax Filing for Engineers in Pakistan 2026 — Complete FBR Guide','Engineers in Pakistan span multiple disciplines — civil, mechanical, electrical, software, and more. Whether you work for a multinational, a government department, or you freelance internationally, your tax obligations depend on your income type and employment structure. This guide covers everything for 2026.',engBody,engTOC,engR1,engR2,engR3,'Hi%20Kamboh%20Associates%2C%20engineer%20tax%20filing%20ke%20bare%20mein%20guide%20chahiye.','Tax Filing for Engineers in Pakistan 2026 — Complete FBR Guide');
fs.writeFileSync('tax-filing-engineers-pakistan.html', engHtml);
console.log('Engineers written:', fs.statSync('tax-filing-engineers-pakistan.html').size, 'bytes');
