const fs = require('fs');
function rewriteArticle(filepath, newContent) {
  let c = fs.readFileSync(filepath, 'utf8');
  const start = c.indexOf('<article');
  const end = c.indexOf('</article>') + 10;
  if (start === -1 || end === 9) { console.log('SKIP:', filepath); return; }
  c = c.substring(0, start) + newContent + c.substring(end);
  fs.writeFileSync(filepath, c, 'utf8');
  const wc = newContent.replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').split(' ').filter(w=>w.length>2).length;
  console.log('✓', filepath.split('/').pop(), '—', wc, 'words');
}

// 11. Income Tax Exemptions Pakistan 2026
rewriteArticle('blogs/income-tax-exemptions-pakistan-2026.html', `<article class="article-body">
<p class="article-lead">Not all income in Pakistan is taxable. The Income Tax Ordinance 2001 provides a range of exemptions and zero-rate treatments for specific types of income. Understanding which exemptions apply to you can legally reduce or eliminate your tax liability.</p>

<h2>Complete List of Income Tax Exemptions in Pakistan 2026</h2>

<h3>1. Agricultural Income</h3>
<p>Agricultural income is completely exempt from federal income tax under Article 142 and the Fourth Schedule of the ITO 2001. This includes income from crops, livestock reared on agricultural land, and forestry. However, provincial agricultural income tax may still apply (Punjab, Sindh, KP, and Balochistan each have their own agricultural tax). Agricultural income must still be declared in the return to explain source of funds.</p>

<h3>2. IT Exports and Freelancer Income (Section 65F / Part I, Second Schedule)</h3>
<p>Registered IT companies and freelancers who earn foreign exchange through export of IT services enjoy a <strong>zero-rated or reduced tax</strong> regime:</p>
<ul>
  <li>IT companies registered with PSEB: 0% income tax on IT export income (foreign exchange remitted through banking channels)</li>
  <li>Freelancers receiving foreign remittance via banking channel: 0.25% final WHT on remittance (no income tax return liability if remittance is the only income)</li>
  <li>Applicable until June 30, 2026 — extended in Finance Act 2026</li>
</ul>

<h3>3. Zakat Deduction (Section 60)</h3>
<p>Zakat paid during the tax year to authorised institutions is 100% deductible from taxable income. For 2026: If your taxable income is Rs. 2 million and you paid Rs. 200,000 as Zakat to an approved institution, your taxable income becomes Rs. 1.8 million. Keep receipts from authorised zakat institutions.</p>

<h3>4. Charitable Donations (Section 61)</h3>
<p>Donations to approved nonprofit organisations (NPOs) under Section 61 are deductible up to 30% of taxable income. The NPO must be registered under Section 2(36) and approved by FBR. Political donations are not eligible. Always obtain Form NPO-1 receipt from the organisation.</p>

<h3>5. Basic Exemption Threshold — Salaried Persons</h3>
<p>Income up to Rs. 600,000 per year is completely exempt from income tax for salaried individuals. No return obligation if total income is below this amount and you do not own property or vehicles.</p>

<h3>6. Provident Fund Receipts (Section 156A)</h3>
<p>Payments from approved provident funds (GPF for government employees, Statutory Provident Funds) are exempt from income tax when withdrawn under the normal conditions. However, premature withdrawals within 5 years may become taxable.</p>

<h3>7. Gratuity Payments</h3>
<p>Gratuity received from an approved gratuity fund is exempt up to Rs. 300,000 per year per the Second Schedule. Excess above Rs. 300,000 is taxable as salary income.</p>

<h3>8. Long-Term Capital Gains</h3>
<ul>
  <li>Property held more than 6 years (open plot) or 4 years (constructed): 0% CGT</li>
  <li>PSX listed shares held more than 2 years: 0% CGT</li>
  <li>Equity mutual fund units held more than 1 year: 0% CGT</li>
</ul>

<h3>9. Prize Bonds Below Rs. 40,000</h3>
<p>Prize bond winnings of Rs. 40,000 or less are exempt from WHT and income tax. Above Rs. 40,000, WHT at 15% (filer) or 25% (non-filer) applies as final tax.</p>

<h3>10. Foreign Remittances (Section 111(4))</h3>
<p>Foreign exchange remitted into Pakistan through normal banking channels cannot be asked about under Section 111 — FBR cannot question the source of remittance received through official banking channels. This is a significant protection for overseas Pakistanis and exporters.</p>

<h3>11. Senior Citizens and Disabled Persons</h3>
<p>Persons above 60 years of age or persons with disability certificates: 50% reduction in income tax liability under Clause 1A of Part III, Second Schedule.</p>

<h3>12. Dividend from Listed Companies (for Individual Investors)</h3>
<p>Dividend WHT of 15% (filer) is a final tax — no further income tax is due on dividend income for resident individual shareholders. The 15% WHT at source fully discharges the tax liability on dividends.</p>

<h2>How to Claim Exemptions in Your FBR Return</h2>
<table class="data-table">
  <thead><tr><th>Exemption</th><th>Where to Declare in IRIS</th><th>Document Required</th></tr></thead>
  <tbody>
    <tr><td>Zakat</td><td>Deductions section — Zakat</td><td>Receipt from approved institution</td></tr>
    <tr><td>Charitable donations</td><td>Deductions section — Charitable Donations</td><td>NPO-1 receipt, NPO's FBR registration number</td></tr>
    <tr><td>Agricultural income</td><td>Income from Agriculture section</td><td>Land ownership documents, crop records</td></tr>
    <tr><td>IT/Freelancer exemption</td><td>Exempt income section</td><td>PSEB certificate (companies), bank remittance advice</td></tr>
    <tr><td>Provident fund</td><td>Exempt income section</td><td>Fund payment certificate</td></tr>
  </tbody>
</table>

<h2>Frequently Asked Questions</h2>
<div class="faq-list">
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">Is freelancer income from Upwork/Fiverr tax-free in Pakistan? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Freelancer foreign income received through banking channels is subject to 0.25% WHT on the remittance amount as a final tax — effectively making it almost tax-free. However, you must still file an income tax return to declare this income and appear on the Active Taxpayer List for filer benefits.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">Can I claim Zakat and charitable donation deductions together? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Yes. Zakat (Section 60) and charitable donations (Section 61) are separate deductions and can both be claimed in the same return. Zakat is fully deductible from taxable income; charitable donations are deductible up to 30% of taxable income.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">Is the Rs. 600,000 exemption limit the same for business and salaried persons? <i class="fas fa-chevron-down"></i></div><div class="faq-a">The Rs. 600,000 basic exemption applies to salaried persons. For non-salaried business persons and AOPs, the threshold is also Rs. 600,000 but the tax slabs are different. Always check the current Finance Act for the applicable slabs for each category.</div></div>
</div>

<div class="article-cta">
  <h3>Maximise Your Legal Tax Savings</h3>
  <p>Kamboh Associates identifies every applicable exemption and deduction for your situation, ensuring you pay the minimum legal tax. WhatsApp us for a free review.</p>
  <a href="https://wa.me/923284675162?text=I+want+to+know+what+income+tax+exemptions+I+qualify+for+in+Pakistan" class="wa-btn"><i class="fab fa-whatsapp"></i> WhatsApp Now — 0328-4675162</a>
</div>
</article>`);

// 12. Tax Planning Tips Pakistan 2026
rewriteArticle('blogs/tax-planning-tips-pakistan-2026.html', `<article class="article-body">
<p class="article-lead">Legal tax planning in Pakistan can significantly reduce your annual income tax liability. Using available deductions, exemptions, and investment incentives under the Income Tax Ordinance 2001, you can lower your effective tax rate — often by 20 to 40 percent — without any risk of FBR penalties.</p>

<h2>What is Tax Planning?</h2>
<p>Tax planning means structuring your income, investments, and expenses within the law to minimise your tax liability. It is completely legal and different from tax evasion (hiding income) or tax avoidance (aggressive schemes that may be challenged by FBR). Good tax planning happens before the tax year ends — not after.</p>

<h2>Top Tax Planning Strategies for Individuals in Pakistan 2026</h2>

<h3>1. Maximise Zakat Contributions (Section 60)</h3>
<p>Zakat paid to FBR-approved institutions is 100% deductible from taxable income. If you are in the 25% tax bracket and pay Rs. 200,000 in Zakat, your tax saving is Rs. 50,000. Make Zakat payments before June 30 each year and get receipts from approved institutions.</p>

<h3>2. Charitable Donations to Approved NPOs (Section 61)</h3>
<p>Donations to approved nonprofits are deductible up to 30% of taxable income. Pakistan's major approved NPOs include Shaukat Khanum Cancer Hospital, Akhuwat Foundation, and others with FBR-approved status. Donate before June 30 and keep the NPO-1 receipt.</p>

<h3>3. Invest in Life Insurance (Section 62)</h3>
<p>Premiums paid on life insurance for yourself, spouse, or minor children give a tax credit under Section 62. The credit is the lower of: actual premium paid, 20% of taxable income, or Rs. 2 million. At 25% tax rate, Rs. 500,000 in premium saves Rs. 125,000 in tax.</p>

<h3>4. Invest in Pension Fund / Voluntary Pension Scheme (Section 63)</h3>
<p>Contributions to an approved Voluntary Pension Scheme (VPS) are deductible from taxable income up to 20% of your taxable income (higher for persons above 40 years). VPS with FBR-approved fund managers (Meezan Bank, NBP, UBL, HBL fund managers) qualify. This is particularly effective for business owners and high-income earners.</p>

<h3>5. Invest in NIT/Mutual Fund Units (Clause 57A, Second Schedule)</h3>
<p>NIT (National Investment Trust) and FBR-approved equity mutual fund investments held more than 1 year generate capital gains that are fully exempt from tax. Returns from mutual funds in the form of capital appreciation for filers holding long-term are tax-free.</p>

<h3>6. Claim Housing Loan Profit Deduction (Section 64A)</h3>
<p>If you have a bank mortgage on your self-occupied home, the profit (interest) paid on the loan is deductible up to Rs. 2 million per year. This is a significant deduction for people with large housing loans — at 25% tax rate, a Rs. 1 million interest deduction saves Rs. 250,000 in tax.</p>

<h3>7. Timing of Asset Sales — Hold Assets Longer</h3>
<p>Capital gains tax rates fall significantly with holding period. A property sold before 1 year: 15% CGT. Same property after 6 years: 0% CGT. If you are planning to sell, holding slightly longer can eliminate CGT entirely on plots (6 years) and constructed property (4 years).</p>

<h3>8. Business Expense Deductions (Section 20)</h3>
<p>For business owners, ensure all legitimate business expenses are claimed: rent, utilities, salaries, professional fees, depreciation on assets, vehicle expenses (proportional to business use), travel and entertainment (subject to limits). Many business owners miss significant deductions by not maintaining proper records.</p>

<h3>9. Salary Restructuring for Employees</h3>
<p>If you are a business owner who pays yourself a salary, restructure your salary package to include tax-exempt components:</p>
<ul>
  <li>Medical allowance: exempt up to 10% of basic salary</li>
  <li>Conveyance allowance: exempt up to a specified limit</li>
  <li>House rent allowance: partially exempt with specific caps</li>
</ul>

<h3>10. Become a Tax Filer — Save on Every Transaction</h3>
<p>The simplest tax planning tool: file your return and get on ATL. Savings across banking, property, and vehicles can easily exceed Rs. 50,000–500,000 annually depending on your transaction volume.</p>

<h2>Tax Planning Calendar — What to Do Each Month</h2>
<table class="data-table">
  <thead><tr><th>Month</th><th>Action</th></tr></thead>
  <tbody>
    <tr><td>July–August</td><td>Review prior year return, identify missed deductions, plan investment decisions for new tax year</td></tr>
    <tr><td>January–April</td><td>Make charitable donations and Zakat payments, make pension fund contributions</td></tr>
    <tr><td>May–June</td><td>Final review of deductions, ensure all expenses are documented, plan timing of asset sales</td></tr>
    <tr><td>July–September</td><td>File income tax return before September 30 deadline</td></tr>
  </tbody>
</table>

<h2>Frequently Asked Questions</h2>
<div class="faq-list">
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">Is tax planning legal in Pakistan? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Yes. Using deductions, exemptions, and incentives provided under the Income Tax Ordinance is completely legal. FBR itself designed these provisions to encourage charitable giving, savings, and investment. Tax planning is different from tax evasion (hiding income) which is a criminal offense.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">How much can I save through tax planning? <i class="fas fa-chevron-down"></i></div><div class="faq-a">It depends on your income and situation. A salaried person earning Rs. 3 million with good planning (Zakat, insurance, housing loan deduction) can reduce their tax liability by 25–40%. Business owners have even more options through legitimate business deductions and timing of income recognition.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">When should I start tax planning for 2026? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Tax planning works best when done at the start of the tax year (July) or mid-year. Planning done after June 30 is too late for most strategies — investments and donations must be made during the tax year to be deductible. Start your 2027 tax planning in July 2026.</div></div>
</div>

<div class="article-cta">
  <h3>Get a Personal Tax Planning Review</h3>
  <p>Kamboh Associates provides tax planning consultations for individuals and businesses. We identify every legal deduction and exemption to minimize your tax bill. WhatsApp for a free initial review.</p>
  <a href="https://wa.me/923284675162?text=I+want+tax+planning+advice+to+reduce+my+income+tax+in+Pakistan" class="wa-btn"><i class="fab fa-whatsapp"></i> WhatsApp Now — 0328-4675162</a>
</div>
</article>`);

// 13. Minimum Tax Section 113 Pakistan
rewriteArticle('blogs/minimum-tax-section-113-pakistan.html', `<article class="article-body">
<p class="article-lead">Minimum tax under Section 113 of the Income Tax Ordinance 2001 applies to companies and certain individuals in Pakistan that declare zero profit or a tax loss but still have significant turnover. If you run a business and claim losses every year, FBR may still require you to pay minimum tax. Here is everything you need to know.</p>

<h2>What is Minimum Tax Under Section 113?</h2>
<p>Section 113 provides that if a company's normal income tax liability (after all deductions and exemptions) is less than 1.5% of its gross turnover, the company must pay a minimum tax equal to 1.5% of its turnover. This prevents businesses from permanently declaring losses to avoid tax while reporting high revenue.</p>

<h2>Who Does Minimum Tax Apply To?</h2>
<table class="data-table">
  <thead><tr><th>Taxpayer Type</th><th>Applies?</th><th>Rate</th></tr></thead>
  <tbody>
    <tr><td>Private limited companies</td><td>Yes</td><td>1.5% of gross turnover</td></tr>
    <tr><td>Public limited companies</td><td>Yes</td><td>1.5% of gross turnover</td></tr>
    <tr><td>AOPs with turnover above Rs. 100 million</td><td>Yes</td><td>1.5% of gross turnover</td></tr>
    <tr><td>Individual business owners (non-corporate)</td><td>Only if notified by FBR</td><td>1.5% of gross turnover</td></tr>
    <tr><td>Banks and financial institutions</td><td>Yes (higher rates apply)</td><td>Different rate under Sec 113(1)(b)</td></tr>
    <tr><td>Service sector companies (specific sectors)</td><td>Yes</td><td>Sector-specific rates</td></tr>
  </tbody>
</table>

<h2>How Minimum Tax is Calculated</h2>
<p><strong>Step 1:</strong> Calculate normal income tax liability based on taxable profit.</p>
<p><strong>Step 2:</strong> Calculate 1.5% of gross turnover (total revenue, not profit).</p>
<p><strong>Step 3:</strong> Pay whichever is higher.</p>
<p><strong>Example:</strong> A private limited company with Rs. 50 million turnover and Rs. 2 million declared loss:</p>
<ul>
  <li>Normal tax on loss: Rs. 0</li>
  <li>Minimum tax: 1.5% × Rs. 50 million = Rs. 750,000</li>
  <li>Tax payable: Rs. 750,000 (the minimum tax)</li>
</ul>

<h2>Can Minimum Tax be Carried Forward?</h2>
<p>Yes. If minimum tax paid in a year exceeds the normal tax liability, the excess can be carried forward and adjusted against normal tax liability in the next 5 tax years. This is called the <strong>excess minimum tax credit</strong> under Section 113(2). So if your business becomes profitable in future years, you get credit for the minimum tax you paid during loss years.</p>

<h2>Exemptions from Minimum Tax</h2>
<p>Certain businesses are exempt from minimum tax under the Second Schedule:</p>
<ul>
  <li>New businesses in their first year of operation</li>
  <li>Companies in Special Economic Zones (SEZs)</li>
  <li>Certain IT and export companies with approved exemptions</li>
  <li>Non-profit organisations with approved tax-exempt status</li>
  <li>Companies whose turnover falls below the prescribed threshold</li>
</ul>

<h2>Minimum Tax vs Turnover Tax — What is the Difference?</h2>
<p>Section 113 (minimum tax) applies when normal tax is below 1.5% of turnover. Section 113A (turnover tax) applied to specific sectors. Both are variations of the same concept — ensuring companies with significant revenue pay some minimum level of tax regardless of declared profits.</p>

<h2>How to File Minimum Tax in FBR Return</h2>
<p>Minimum tax is calculated and declared in the company's annual income tax return (Form IT-2 for companies). The return must show: total gross turnover, normal tax liability, minimum tax calculation (1.5% of turnover), and the higher of the two amounts as tax payable.</p>

<h2>Frequently Asked Questions</h2>
<div class="faq-list">
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">If our company made a loss, do we still have to pay income tax? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Yes, if you are a company with significant turnover. Minimum tax at 1.5% of gross turnover applies even in loss years under Section 113. The logic is that a company cannot have significant revenue without some income, and declaring a loss every year is a common tax planning technique FBR aims to prevent through minimum tax.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">Does minimum tax apply to small businesses? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Section 113 primarily targets companies (Pvt Ltd, Public Ltd) and large AOPs. Individual proprietors and small AOPs below the threshold may not be subject to minimum tax. However, FBR can bring any business person under Section 113 through a notification. Consult a tax advisor to check your specific situation.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">Can WHT deposits be offset against minimum tax? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Yes. Adjustable withholding taxes paid during the year are first credited against the normal tax liability. If the normal tax (or minimum tax) is still due after WHT credits, the balance must be paid. Minimum tax cannot be reduced below zero by WHT credits, but excess WHT is refundable.</div></div>
</div>

<div class="article-cta">
  <h3>Need Help With Company Tax Return and Minimum Tax?</h3>
  <p>Kamboh Associates files corporate income tax returns and handles minimum tax calculations for private limited companies across Pakistan.</p>
  <a href="https://wa.me/923284675162?text=I+need+help+with+company+income+tax+return+and+minimum+tax" class="wa-btn"><i class="fab fa-whatsapp"></i> WhatsApp Now — 0328-4675162</a>
</div>
</article>`);

// 14. Sales Tax Registration Guide Pakistan
rewriteArticle('blogs/sales-tax-registration-guide-pakistan.html', `<article class="article-body">
<p class="article-lead">Sales tax registration (STRN — Sales Tax Registration Number) in Pakistan is mandatory for businesses above the threshold, and voluntary for others who want to claim input tax credits. This guide covers who must register, the step-by-step registration process, and how to file monthly returns.</p>

<h2>What is Sales Tax Registration (STRN) in Pakistan?</h2>
<p>Sales Tax Registration gives your business an STRN (Sales Tax Registration Number) also known as GSTIN or STRN. It authorizes you to collect 17% General Sales Tax (GST) on taxable supplies, claim input tax credit on purchases, and file monthly returns with FBR. The GST registered business is listed on the FBR ACTIVE taxpayer list for sales tax purposes.</p>

<h2>Who Must Register for Sales Tax in Pakistan?</h2>
<table class="data-table">
  <thead><tr><th>Business Type</th><th>Registration Requirement</th><th>Threshold</th></tr></thead>
  <tbody>
    <tr><td>Manufacturers</td><td>Mandatory</td><td>Annual turnover above Rs. 10 million</td></tr>
    <tr><td>Importers (commercial)</td><td>Mandatory</td><td>Any amount — all importers must register</td></tr>
    <tr><td>Exporters</td><td>Mandatory (for zero-rated status)</td><td>Any amount — to claim zero-rating</td></tr>
    <tr><td>Retailers</td><td>Mandatory if Tier-1</td><td>Annual turnover above Rs. 100 million, or large integrated chains, or located in commercial areas with specific criteria</td></tr>
    <tr><td>Wholesalers/distributors</td><td>Mandatory</td><td>Annual turnover above Rs. 10 million</td></tr>
    <tr><td>Service providers</td><td>Voluntary (federal) or provincial</td><td>Services GST is provincial — PRA (Punjab), SRB (Sindh), KPRA (KP), BRA (Balochistan)</td></tr>
  </tbody>
</table>

<h2>Documents Required for GST/STRN Registration</h2>
<ul>
  <li>CNIC of proprietor/partners/directors</li>
  <li>NTN (must already be registered with FBR)</li>
  <li>Business registration documents (SECP certificate for Pvt Ltd, or business address proof for proprietorship)</li>
  <li>Business bank account details</li>
  <li>Utility bill for business premises (electricity or gas — last 3 months)</li>
  <li>Lease agreement for business premises</li>
  <li>Photographs of business premises (front and interior)</li>
</ul>

<h2>Step-by-Step: How to Register for GST on FBR IRIS</h2>
<ol>
  <li>Log in to <strong>iris.fbr.gov.pk</strong> with your NTN credentials</li>
  <li>Go to <strong>Registration → Sales Tax Registration</strong></li>
  <li>Select your registration type: Manufacturer, Importer, Exporter, or Retailer</li>
  <li>Enter business details: name, address, NTN, bank account</li>
  <li>Upload required documents (CNIC, utility bill, business proof)</li>
  <li>Submit the application</li>
  <li>FBR may conduct a physical verification of your business premises</li>
  <li>STRN is issued within 3–15 working days if documents are complete</li>
</ol>
<div class="highlight-box"><p><strong>Fast-track option:</strong> Kamboh Associates completes GST registration in 5–7 working days for Rs. 5,000, handling all document preparation, submission, and FBR follow-up.</p></div>

<h2>Monthly GST Return Filing Obligations</h2>
<p>Once registered, you must file a monthly GST return by the <strong>18th of the following month</strong>:</p>
<ul>
  <li><strong>Sales (Output Tax):</strong> 17% GST collected from customers on taxable supplies</li>
  <li><strong>Purchases (Input Tax):</strong> 17% GST paid to suppliers — claimable as credit</li>
  <li><strong>Net payable:</strong> Output Tax minus Input Tax = Amount payable to FBR</li>
</ul>

<h2>Common GST Registration Rejections — Avoid These</h2>
<ul>
  <li>Utility bill not in business owner's name or at a different address</li>
  <li>Business premises not verifiable (virtual office not accepted)</li>
  <li>NTN not active or not filed for prior year</li>
  <li>Business bank account not yet opened</li>
  <li>Photographs of premises missing or unclear</li>
</ul>

<h2>Frequently Asked Questions</h2>
<div class="faq-list">
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">Can I register for GST before my business starts earning revenue? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Yes. Pre-registration is possible if you can show business setup (office, machinery, initial purchases). Pre-registration allows you to claim input tax on setup costs before your first sale. This is beneficial for manufacturers and importers with high initial capital expenditure.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">What is the penalty for not registering for GST when required? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Failure to register when required makes you liable for all GST that should have been collected, plus a penalty of Rs. 10,000 per month of default under Section 33 of the Sales Tax Act. FBR can also impose additional penalty for tax evasion equal to the tax not paid.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">What is the difference between GST and PRA/SRB registration? <i class="fas fa-chevron-down"></i></div><div class="faq-a">GST on goods is administered by FBR (federal). GST on services is administered by provincial authorities: PRA for Punjab, SRB for Sindh, KPRA for KP, BRA for Balochistan, AJK Revenue for AJK. Many businesses need both FBR-STRN (for goods) and PRA/SRB registration (for services).</div></div>
</div>

<div class="article-cta">
  <h3>Get GST/STRN Registration Done in 7 Days</h3>
  <p>Kamboh Associates handles complete GST registration with FBR for manufacturers, importers, exporters, and retailers across Pakistan. Starting from Rs. 5,000.</p>
  <a href="https://wa.me/923284675162?text=I+need+GST+STRN+sales+tax+registration+in+Pakistan" class="wa-btn"><i class="fab fa-whatsapp"></i> WhatsApp Now — 0328-4675162</a>
</div>
</article>`);

// 15. FBR Notice Response Guide Pakistan
rewriteArticle('blogs/fbr-notice-response-guide-pakistan.html', `<article class="article-body">
<p class="article-lead">FBR sends various types of notices to taxpayers in Pakistan — for verification, audit, unpaid tax demands, or Section 111 unexplained income. Ignoring any FBR notice is dangerous. This guide explains every type of FBR notice and exactly how to respond to each one correctly.</p>

<h2>Types of FBR Notices in Pakistan</h2>
<table class="data-table">
  <thead><tr><th>Notice Type</th><th>Section</th><th>What It Means</th><th>Response Time</th></tr></thead>
  <tbody>
    <tr><td>Unexplained income notice</td><td>111</td><td>FBR cannot explain your wealth increase with declared income</td><td>21–30 days</td></tr>
    <tr><td>Audit notice (desk/field)</td><td>177</td><td>Your return has been selected for detailed examination</td><td>30 days</td></tr>
    <tr><td>Amendment of assessment</td><td>122</td><td>FBR wants to change a previous assessment</td><td>30 days</td></tr>
    <tr><td>Non-filing notice</td><td>114(4)</td><td>You have not filed a return despite obligation</td><td>15–30 days</td></tr>
    <tr><td>Demand notice</td><td>137</td><td>Tax demand is pending payment</td><td>30 days or payment</td></tr>
    <tr><td>WHT default notice</td><td>161/162</td><td>You failed to deduct/deposit WHT as a withholding agent</td><td>30 days</td></tr>
    <tr><td>GST show-cause notice</td><td>Sales Tax Act Sec 11</td><td>FBR alleges incorrect GST return or missing GST</td><td>15–30 days</td></tr>
    <tr><td>Penalty notice</td><td>182/183</td><td>Penalty being imposed for late filing or other default</td><td>30 days</td></tr>
  </tbody>
</table>

<h2>General Rules for Responding to Any FBR Notice</h2>
<ul>
  <li><strong>Never ignore it:</strong> Ignoring a notice allows FBR to pass an ex-parte order (against you without your input)</li>
  <li><strong>Note the deadline:</strong> Mark it in your calendar immediately. Request an extension in writing if you need more time</li>
  <li><strong>Respond in writing:</strong> All responses must be in writing with supporting documents. Oral responses have no legal weight</li>
  <li><strong>Keep copies:</strong> Keep a copy of your response with the receiving stamp or registered mail receipt</li>
  <li><strong>Engage a consultant early:</strong> The earlier a qualified tax consultant reviews the notice, the better the outcome</li>
</ul>

<h2>How to Respond to an FBR Section 111 Notice (Unexplained Income)</h2>
<p>This is the most common serious notice. Respond by:</p>
<ol>
  <li>Identifying which amount FBR is questioning</li>
  <li>Gathering documentary evidence for the source: salary certificate, loan agreement, gift deed, property sale proceeds</li>
  <li>Filing any missing returns for the years in question</li>
  <li>Drafting a point-by-point reply addressing each questioned amount with attached evidence</li>
  <li>Submitting to the relevant Commissioner before the deadline</li>
</ol>

<h2>How to Respond to an FBR Audit Notice (Section 177)</h2>
<ol>
  <li>Identify the scope: which tax years are included and what specifically is being examined</li>
  <li>Compile all documents: returns, wealth statements, bank statements, business records</li>
  <li>Do not submit anything before your consultant reviews it — once submitted, it becomes the official record</li>
  <li>Attend hearings with complete documentation and your consultant</li>
  <li>Respond to the draft order within the deadline given</li>
</ol>

<h2>How to Respond to a Non-Filing Notice (Section 114)</h2>
<p>The simplest response: file your income tax return immediately. Once the return is filed, the non-filing notice is resolved automatically. File late returns with payment of late filing penalty (Rs. 1,000/day, max Rs. 50,000 for individuals).</p>

<h2>What if FBR Issues a Tax Demand You Disagree With?</h2>
<p>You have the right to appeal within 30 days:</p>
<ul>
  <li><strong>First appeal:</strong> Commissioner Inland Revenue (Appeals) — Section 127</li>
  <li><strong>Second appeal:</strong> Appellate Tribunal Inland Revenue — Section 131</li>
  <li><strong>High Court:</strong> Reference on points of law only — Section 133</li>
  <li><strong>ADR:</strong> Alternative Dispute Resolution under Section 134A — faster settlement</li>
</ul>

<h2>Frequently Asked Questions</h2>
<div class="faq-list">
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">What should I do if I receive an FBR notice but I have already paid all my taxes? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Respond to the notice by submitting your filed returns, payment receipts, and any other evidence showing compliance. Even correctly filed taxpayers get selected for audit. Your clean records will resolve the matter. Never ignore a notice even if you are fully compliant.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">Can I hire a lawyer or consultant to respond to an FBR notice on my behalf? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Yes. You can authorize a tax consultant or lawyer through a signed Power of Attorney to represent you before FBR. They can appear at hearings, submit documents, and file appeals on your behalf. This is highly recommended for Section 111 notices and audit proceedings.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">How long does FBR take to close a notice after I respond? <i class="fas fa-chevron-down"></i></div><div class="faq-a">It depends on the notice type. Simple non-filing notices close within days of filing the return. Audit proceedings can take 3–6 months. Section 111 cases vary — with a strong response and proper documentation, many are resolved within 60–90 days. Complex cases may go to appeal and take longer.</div></div>
</div>

<div class="article-cta">
  <h3>Received an FBR Notice? Act Within 48 Hours</h3>
  <p>WhatsApp Kamboh Associates a photo of your FBR notice. We review it for free and tell you exactly how to respond. Our team has resolved hundreds of FBR notices across Pakistan.</p>
  <a href="https://wa.me/923284675162?text=I+received+an+FBR+notice+and+need+urgent+help" class="wa-btn"><i class="fab fa-whatsapp"></i> WhatsApp Now — 0328-4675162</a>
</div>
</article>`);

console.log('\nBatch 3 complete — 5 blogs rewritten');
