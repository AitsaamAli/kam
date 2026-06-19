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

// ══════════════════════════════════════════════════════════════
// 6. Capital Gains Tax Pakistan 2026
// ══════════════════════════════════════════════════════════════
rewriteArticle('blogs/capital-gains-tax-pakistan-2026.html', `<article class="article-body">
<p class="article-lead">Capital gains tax (CGT) in Pakistan applies to profit earned from selling property, shares, and other assets. The rate depends on how long you held the asset. This complete guide covers CGT rates, exemptions, and how to report capital gains in your FBR income tax return for 2026.</p>

<h2>What is Capital Gains Tax in Pakistan?</h2>
<p>Capital gains tax is levied under Section 37 (immovable property) and Section 37A (securities) of the Income Tax Ordinance 2001. It applies to the profit — sale price minus cost price — when you sell an asset. The key factor is the <strong>holding period</strong>: assets held longer are taxed at lower rates to discourage speculation and encourage long-term investment.</p>

<h2>Capital Gains Tax Rates on Property (Section 37) — 2026</h2>
<table class="data-table">
  <thead><tr><th>Holding Period</th><th>CGT Rate (Open Plot)</th><th>CGT Rate (Constructed Property)</th></tr></thead>
  <tbody>
    <tr><td>Less than 1 year</td><td>15%</td><td>15%</td></tr>
    <tr><td>1 to 2 years</td><td>12.5%</td><td>10%</td></tr>
    <tr><td>2 to 3 years</td><td>10%</td><td>7.5%</td></tr>
    <tr><td>3 to 4 years</td><td>7.5%</td><td>5%</td></tr>
    <tr><td>4 to 5 years</td><td>5%</td><td>0%</td></tr>
    <tr><td>5 to 6 years</td><td>2.5%</td><td>0%</td></tr>
    <tr><td>More than 6 years</td><td>0%</td><td>0%</td></tr>
  </tbody>
</table>
<div class="highlight-box"><p><strong>Good news for long-term holders:</strong> If you sell a constructed property after 4 years or a plot after 6 years, no CGT is payable. This is one reason why long-term real estate investment in Pakistan carries lower tax burden.</p></div>

<h2>How is Property CGT Calculated?</h2>
<p>The capital gain is calculated as:</p>
<p><strong>Capital Gain = Sale Price (or FBR value, whichever higher) − Cost Price (or FBR value at purchase, whichever higher)</strong></p>
<p>Example: You bought a plot in 2023 for Rs. 40 lakh (FBR DC value: Rs. 35 lakh). You sell it in 2025 for Rs. 70 lakh (FBR value: Rs. 65 lakh). Holding period: 2 years.</p>
<ul>
  <li>Sale price for CGT: Rs. 70 lakh (higher of Rs. 70 lakh and Rs. 65 lakh)</li>
  <li>Cost for CGT: Rs. 40 lakh (higher of Rs. 40 lakh and Rs. 35 lakh)</li>
  <li>Capital gain: Rs. 30 lakh</li>
  <li>CGT rate (2–3 years, open plot): 10%</li>
  <li>CGT payable: Rs. 3 lakh</li>
</ul>

<h2>Capital Gains Tax on Shares and Securities (Section 37A) — 2026</h2>
<table class="data-table">
  <thead><tr><th>Security Type</th><th>Holding Period</th><th>CGT Rate</th></tr></thead>
  <tbody>
    <tr><td>Listed company shares (PSX)</td><td>Less than 1 year</td><td>15%</td></tr>
    <tr><td>Listed company shares (PSX)</td><td>1 to 2 years</td><td>12.5%</td></tr>
    <tr><td>Listed company shares (PSX)</td><td>More than 2 years</td><td>0%</td></tr>
    <tr><td>Mutual fund units (equity)</td><td>Less than 1 year</td><td>15%</td></tr>
    <tr><td>Mutual fund units (equity)</td><td>More than 1 year</td><td>0%</td></tr>
    <tr><td>Unlisted company shares</td><td>Any period</td><td>10%</td></tr>
    <tr><td>Government securities, NSCs, DSCs</td><td>Any period</td><td>0% (profit is WHT under Sec 151)</td></tr>
  </tbody>
</table>

<h2>CGT on Sale of Property — Important Rules</h2>
<ul>
  <li><strong>First property exemption:</strong> If you are selling your first-ever property that was self-constructed or self-purchased and you lived in it, you may qualify for principal residence exemption under Section 37(5)</li>
  <li><strong>FBR notified values:</strong> FBR publishes DC (Deputy Commissioner) rates for all areas. If your sale price is lower than the FBR value, the FBR value is used for CGT — so you cannot undervalue a sale to avoid CGT</li>
  <li><strong>WHT at time of sale:</strong> Section 236C requires the buyer to withhold tax at source. Filers: 3%, Non-filers: 6%. This WHT is adjustable against final CGT liability</li>
  <li><strong>Reporting in return:</strong> CGT must be declared in Schedule II of your income tax return, even if WHT was already deducted</li>
</ul>

<h2>CGT Exemptions in Pakistan 2026</h2>
<ul>
  <li>Property held for more than 6 years (open plot) or 4 years (constructed) — fully exempt</li>
  <li>PSX listed shares held more than 2 years — exempt</li>
  <li>Equity mutual fund units held more than 1 year — exempt</li>
  <li>Sale of shares in your own company on dissolution — may be exempt if reinvested</li>
  <li>Agricultural land — CGT does not apply to agricultural land</li>
</ul>

<h2>Frequently Asked Questions</h2>
<div class="faq-list">
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">Do I have to pay CGT if I sell property at a loss? <i class="fas fa-chevron-down"></i></div><div class="faq-a">No. CGT only applies to gains (profit). If you sell at a loss, there is no CGT payable. However, you should still declare the transaction in your wealth statement and return to avoid FBR questions about the sale.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">What if I sell property below FBR DC value? <i class="fas fa-chevron-down"></i></div><div class="faq-a">FBR uses the higher of the actual sale price or the FBR notified DC value for CGT calculation. Selling below DC value does not reduce your CGT — FBR will use the DC value as the deemed sale price.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">Is CGT on property the same as the stamp duty / CVT? <i class="fas fa-chevron-down"></i></div><div class="faq-a">No. CGT (Section 37) is income tax on your profit. Stamp duty is a provincial tax on the transfer document. Capital Value Tax (CVT) is a federal tax at 2% on the buyer's side for certain properties. All three may apply to the same transaction.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">If WHT was deducted at 3% on my property sale, do I still owe more CGT? <i class="fas fa-chevrap-down"></i></div><div class="faq-a">Possibly. The 3% WHT under Section 236C is adjustable against your final CGT liability. Calculate your actual CGT using the correct rate for your holding period. If your CGT rate is higher than 3%, you owe the difference. If lower or zero (held 6+ years), you can claim a refund of the 3% WHT.</div></div>
</div>

<div class="article-cta">
  <h3>Sold Property or Shares? Get Your CGT Filed Correctly</h3>
  <p>Kamboh Associates calculates and files capital gains tax for property and share transactions. Avoid FBR notices — get your CGT right the first time.</p>
  <a href="https://wa.me/923284675162?text=I+need+help+with+capital+gains+tax+on+my+property+or+shares" class="wa-btn"><i class="fab fa-whatsapp"></i> WhatsApp Now — 0328-4675162</a>
</div>
</article>`);

// ══════════════════════════════════════════════════════════════
// 7. Tax on Cryptocurrency Pakistan 2026
// ══════════════════════════════════════════════════════════════
rewriteArticle('blogs/tax-on-cryptocurrency-pakistan-2026.html', `<article class="article-body">
<p class="article-lead">Cryptocurrency transactions in Pakistan are taxable under FBR regulations. Whether you trade Bitcoin, Ethereum, USDT, or any other digital asset, profits are subject to capital gains tax and must be disclosed in your annual wealth statement. Failure to declare crypto can result in Section 111 FBR notices.</p>

<h2>Is Cryptocurrency Legal in Pakistan?</h2>
<p>The legal status of crypto in Pakistan is evolving. The State Bank of Pakistan (SBP) has not declared crypto legal tender, but it has not banned it either. FBR, however, treats crypto as an asset — profits from trading are taxable, and holdings must be declared in the wealth statement. In 2023, Pakistan's Virtual Asset Service Provider (VASP) regulatory framework was announced, bringing exchanges under AML/CFT rules.</p>

<h2>How FBR Taxes Cryptocurrency in Pakistan 2026</h2>
<table class="data-table">
  <thead><tr><th>Activity</th><th>Tax Treatment</th><th>Rate</th></tr></thead>
  <tbody>
    <tr><td>Trading profit (buy low, sell high)</td><td>Capital gain under Section 37 / 37A</td><td>15% (short-term) to 0% (long-term)</td></tr>
    <tr><td>Mining income</td><td>Business income</td><td>Normal income tax slab rates</td></tr>
    <tr><td>Staking / yield farming rewards</td><td>Other income (Section 39)</td><td>Normal income tax slab rates</td></tr>
    <tr><td>Crypto received as payment for services</td><td>Business/professional income</td><td>Normal income tax slab rates</td></tr>
    <tr><td>Crypto received as gift</td><td>Gift — not taxable (but donor must have clean source)</td><td>0% if properly documented</td></tr>
    <tr><td>Crypto holdings at 30 June</td><td>Wealth statement declaration</td><td>No tax on holding — declaration required</td></tr>
  </tbody>
</table>

<h2>Capital Gains Tax on Crypto Trading</h2>
<p>When you sell or convert cryptocurrency for profit, capital gains tax applies under Section 37A (treated similarly to securities):</p>
<ul>
  <li><strong>Held less than 1 year:</strong> 15% CGT on profit</li>
  <li><strong>Held 1–2 years:</strong> 12.5% CGT</li>
  <li><strong>Held more than 2 years:</strong> 0% — fully exempt</li>
</ul>
<p>The gain = PKR equivalent of sale value minus PKR equivalent of cost at time of purchase. Use SBP exchange rate for USD/PKR conversion at each transaction date.</p>
<div class="highlight-box"><p><strong>Key rule:</strong> Crypto-to-crypto swaps (e.g., Bitcoin to USDT) are also taxable events — you have effectively "sold" Bitcoin at its market value and "bought" USDT. Many traders are unaware of this and miss declaring swap profits.</p></div>

<h2>Declaring Crypto in FBR Wealth Statement</h2>
<p>Every taxpayer in Pakistan who holds cryptocurrency must declare it in their wealth statement under "Foreign Assets" or "Other Assets" with the following details:</p>
<ul>
  <li>Name of cryptocurrency (Bitcoin, Ethereum, USDT, etc.)</li>
  <li>Total quantity held at 30 June</li>
  <li>Market value in PKR at 30 June</li>
  <li>Exchange/wallet where held</li>
</ul>
<p>Failure to declare crypto holdings in the wealth statement can result in an FBR Section 111 notice if FBR identifies the holdings through bank transactions, exchange reports, or Binance/Coinbase data sharing agreements.</p>

<h2>What Happens if I Did Not Declare Crypto Previously?</h2>
<p>If you have undisclosed crypto holdings or profits from prior years:</p>
<ul>
  <li><strong>Voluntary disclosure is safer than being caught</strong> — file amended returns for prior years</li>
  <li>FBR is increasingly receiving data on Pakistani users of international exchanges</li>
  <li>Undisclosed crypto profits treated as unexplained income under Section 111 — taxed at full rate + 100% penalty</li>
  <li>You can declare previously undisclosed assets in the current year wealth statement with explanation — consult a tax advisor first</li>
</ul>

<h2>How to Calculate and Pay Crypto Tax in Pakistan</h2>
<ol>
  <li>Export your complete trade history from your exchange (Binance, Kraken, etc.)</li>
  <li>Convert all buy/sell prices to PKR using SBP rate on each transaction date</li>
  <li>Calculate profit/loss per trade: Sale PKR value minus Buy PKR value</li>
  <li>Classify by holding period for CGT rate</li>
  <li>Declare total crypto capital gain in Schedule II of your income tax return</li>
  <li>Declare crypto holdings at 30 June in the wealth statement</li>
  <li>Pay any tax due via PSID before the return deadline</li>
</ol>

<h2>Frequently Asked Questions</h2>
<div class="faq-list">
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">Do I need to pay tax on crypto if I have not sold it yet? <i class="fas fa-chevron-down"></i></div><div class="faq-a">No income tax or CGT is due on unsold crypto holdings — capital gains are only taxed when realized (when you sell or convert). However, you must still declare the current market value of all holdings in your wealth statement each year.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">What if I received crypto as payment for freelance work? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Crypto received as payment for services is treated as business/professional income at the PKR equivalent market value on the date received. Declare it as business income in your tax return. Any subsequent gain when you sell is capital gains on top of the income already declared.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">Can FBR find out about my crypto holdings? <i class="fas fa-chevron-down"></i></div><div class="faq-a">FBR is strengthening its data exchange capabilities. If you withdrew crypto profits to a Pakistani bank account, those bank credits are visible to FBR. International exchanges operating in Pakistan must comply with AML/KYC regulations and may share data. Voluntary disclosure now is far safer than waiting to be discovered.</div></div>
</div>

<div class="article-cta">
  <h3>Need Help With Crypto Tax Filing in Pakistan?</h3>
  <p>Kamboh Associates helps crypto traders and investors file correct FBR returns, declare crypto holdings in wealth statements, and resolve FBR notices related to undisclosed crypto.</p>
  <a href="https://wa.me/923284675162?text=I+need+help+with+cryptocurrency+tax+filing+in+Pakistan" class="wa-btn"><i class="fab fa-whatsapp"></i> WhatsApp Now — 0328-4675162</a>
</div>
</article>`);

// ══════════════════════════════════════════════════════════════
// 8. How to Become Active Filer Pakistan 2026
// ══════════════════════════════════════════════════════════════
rewriteArticle('blogs/how-to-become-active-filer-pakistan-2026.html', `<article class="article-body">
<p class="article-lead">Becoming an active filer in Pakistan — getting on FBR's Active Taxpayer List (ATL) — gives you lower withholding tax rates on banking, property, and vehicle transactions, potentially saving you lakhs of rupees per year. Here is the exact step-by-step process to become a filer in 2026.</p>

<h2>What Does Being an Active Filer Mean?</h2>
<p>An active filer is a person who has filed their income tax return for the previous year and appears on FBR's Active Taxpayer List (ATL). The ATL is published weekly on FBR's website and is checked by banks, property registrars, and vehicle registration offices to determine which withholding tax rate to apply to your transactions.</p>
<p>Being on ATL means you pay filer rates — often half or less of what non-filers pay on the same transactions.</p>

<h2>Step 1 — Get an NTN (National Tax Number)</h2>
<p>You need an NTN before you can file a return. To register:</p>
<ul>
  <li>Go to <strong>iris.fbr.gov.pk</strong></li>
  <li>Click on "Registration for Unregistered Person"</li>
  <li>Enter your CNIC and mobile number</li>
  <li>OTP will be sent to your mobile — verify it</li>
  <li>Complete the online form with your name, address, and income type</li>
  <li>Your NTN (same as CNIC for individuals) is activated immediately</li>
</ul>
<p>Alternatively, WhatsApp your CNIC to Kamboh Associates at <strong>0328-4675162</strong> — we register your NTN same day for Rs. 2,000.</p>

<h2>Step 2 — Login to FBR IRIS</h2>
<p>After NTN registration, log in at <strong>iris.fbr.gov.pk</strong> using your CNIC as username and the password set during registration. If you forgot your password, click "Forgot Password" — a reset link is sent to your registered mobile number.</p>

<h2>Step 3 — File Your Income Tax Return</h2>
<p>Once logged in:</p>
<ol>
  <li>Go to <strong>Declaration → Income Tax Return</strong></li>
  <li>Select the current Tax Year (Tax Year 2026 covers July 2025 to June 2026)</li>
  <li>Choose your return type (Salaried, Non-Salaried, or Both)</li>
  <li>Fill in all income details — salary, business income, rent, bank profit, etc.</li>
  <li>Fill in the Wealth Statement (assets and liabilities)</li>
  <li>Pay any balance tax due via PSID</li>
  <li>Submit the return and download the Acknowledgement Form</li>
</ol>

<h2>Step 4 — Check Your ATL Status</h2>
<p>After submitting your return, your name will appear on the Active Taxpayer List within 24–72 hours. Check your status at:</p>
<ul>
  <li><strong>atl.fbr.gov.pk</strong> — enter your CNIC and click Search</li>
  <li>FBR mobile app — search "FBR Pakistan" in Google Play or App Store</li>
  <li>SMS: Send your CNIC to 9966 (ATL verification service)</li>
</ul>

<h2>Timeline to Get on ATL</h2>
<table class="data-table">
  <thead><tr><th>Action</th><th>Time Required</th></tr></thead>
  <tbody>
    <tr><td>NTN registration online</td><td>Immediate</td></tr>
    <tr><td>Filing income tax return (with all docs ready)</td><td>1–2 hours (DIY) or same day via consultant</td></tr>
    <tr><td>Appearing on ATL after filing</td><td>24–72 hours (next weekly ATL update)</td></tr>
    <tr><td>Total time from start to active filer status</td><td>1–3 days</td></tr>
  </tbody>
</table>

<h2>What if I Missed the September 30 Deadline?</h2>
<p>You can still become a filer after the deadline by:</p>
<ol>
  <li>Filing your return late (penalty: Rs. 1,000/day, max Rs. 50,000)</li>
  <li>Paying the ATL surcharge under Section 182A (Rs. 1,000 for individuals, Rs. 20,000 for companies)</li>
  <li>After late filing + surcharge payment, your name appears on ATL</li>
</ol>
<p>Filing late is always better than not filing. The surcharge is one-time and far less than the WHT savings from being on ATL.</p>

<h2>Documents Needed to Become a Filer</h2>
<table class="data-table">
  <thead><tr><th>Document</th><th>Purpose</th></tr></thead>
  <tbody>
    <tr><td>CNIC (Computerised National Identity Card)</td><td>Identity and NTN number</td></tr>
    <tr><td>Mobile number registered with NADRA</td><td>OTP verification for IRIS</td></tr>
    <tr><td>Salary slips or employer tax certificate (Form 16)</td><td>Salary income declaration</td></tr>
    <tr><td>Bank statement (July 2025 – June 2026)</td><td>Income and wealth reconciliation</td></tr>
    <tr><td>Property documents (if any)</td><td>Wealth statement</td></tr>
  </tbody>
</table>

<h2>Frequently Asked Questions</h2>
<div class="faq-list">
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">Can I file the income tax return online myself? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Yes. The FBR IRIS portal is available 24/7 at iris.fbr.gov.pk. However, the wealth statement reconciliation and correct classification of income can be tricky. Many people file incorrectly and later receive Section 111 notices. For Rs. 3,500, a professional consultant ensures it is done right.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">If I became a filer today, when will I get filer WHT rates? <i class="fas fa-chevron-down"></i></div><div class="faq-a">ATL is updated every Sunday. Once your name appears on ATL, filer rates apply immediately to all future transactions. For the current week's transactions (before ATL update), non-filer rates may still apply.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">My employer deducts tax from salary — do I still need to file? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Yes, absolutely. Employer salary tax deduction does not fulfill your personal filing obligation. You must still file a personal return. Only after filing a personal return will you appear on ATL and get filer benefits on banking and property transactions.</div></div>
</div>

<div class="article-cta">
  <h3>Become a Tax Filer in 24 Hours</h3>
  <p>Kamboh Associates handles NTN registration and income tax return filing for salaried persons starting from Rs. 5,500 total. WhatsApp your CNIC now.</p>
  <a href="https://wa.me/923284675162?text=I+want+to+become+an+active+filer+on+FBR+ATL" class="wa-btn"><i class="fab fa-whatsapp"></i> WhatsApp Now — 0328-4675162</a>
</div>
</article>`);

// ══════════════════════════════════════════════════════════════
// 9. FBR Audit Pakistan 2026
// ══════════════════════════════════════════════════════════════
rewriteArticle('blogs/fbr-audit-pakistan-2026.html', `<article class="article-body">
<p class="article-lead">An FBR tax audit in Pakistan means FBR has selected your return for detailed examination of income, expenses, and assets. This guide explains how FBR selects taxpayers for audit, what documents you need, and how to handle the audit process to protect yourself.</p>

<h2>How Does FBR Select Taxpayers for Audit?</h2>
<p>FBR uses two main selection methods under Section 214C:</p>
<ol>
  <li><strong>Computer ballot (random selection):</strong> FBR's CREST system randomly selects a percentage of all filers each year. If you are selected, you receive a notice regardless of whether your return was correct or not.</li>
  <li><strong>Risk-based selection:</strong> FBR's systems identify high-risk returns where data mismatches are detected — significant unexplained income, wealth increase inconsistent with declared income, third-party data (banks, NADRA, property registrar) not matching the return.</li>
</ol>
<p>In addition, FBR officers can initiate audits based on specific intelligence or complaints under Section 177.</p>

<h2>Types of FBR Audits in Pakistan</h2>
<table class="data-table">
  <thead><tr><th>Audit Type</th><th>Legal Basis</th><th>Scope</th></tr></thead>
  <tbody>
    <tr><td>Desk audit</td><td>Section 177(1)</td><td>FBR reviews documents at their office — you submit records, no visit required</td></tr>
    <tr><td>Field audit</td><td>Section 177(2)</td><td>FBR officer visits your business premises or home to verify records</td></tr>
    <tr><td>Special audit</td><td>Section 177(6)</td><td>Conducted by a firm of Chartered Accountants appointed by FBR in complex cases</td></tr>
    <tr><td>Sales tax audit</td><td>Section 25 of Sales Tax Act</td><td>Examination of GST returns, purchase/sales records, and input tax credits</td></tr>
    <tr><td>Benami proceedings</td><td>Benami Transactions Prohibition Act 2017</td><td>Assets suspected to be held in someone else's name on behalf of actual owner</td></tr>
  </tbody>
</table>

<h2>What Documents FBR Typically Asks For in an Audit</h2>
<ul>
  <li>Income tax returns and wealth statements for last 3–5 years</li>
  <li>Bank statements for all accounts (personal and business)</li>
  <li>Salary slips and employer tax certificates</li>
  <li>Business books of accounts (ledger, cash book, purchase/sales register)</li>
  <li>Rental income agreements</li>
  <li>Property purchase and sale documents</li>
  <li>Vehicle purchase documents</li>
  <li>Investment certificates (NSC, DSC, prize bonds, mutual fund statements)</li>
  <li>Loan agreements (money you borrowed or lent)</li>
  <li>Gift deeds for gifts received or given</li>
</ul>

<h2>Step-by-Step: How to Handle an FBR Audit</h2>

<h3>Step 1 — Do Not Ignore the Notice</h3>
<p>When you receive an audit notice under Section 177, you have a specified time to respond (usually 30 days). Ignoring it gives FBR the right to make an ex-parte assessment — they can determine your tax liability without your input, typically resulting in a much higher demand.</p>

<h3>Step 2 — Engage a Qualified Tax Consultant Immediately</h3>
<p>An FBR audit is not something to handle alone. A qualified tax consultant or lawyer who knows FBR audit procedures can: identify what FBR is actually looking for, prepare the right documents, communicate professionally with the audit officer, and significantly reduce any potential demand.</p>

<h3>Step 3 — Gather and Organise All Required Documents</h3>
<p>Compile all documents listed in the notice. Ensure your bank statements reconcile with declared income. If there are discrepancies, prepare explanations with supporting evidence before submitting anything to FBR.</p>

<h3>Step 4 — Submit Documents and Attend Hearings</h3>
<p>Submit documents within the deadline specified. If FBR calls you for a hearing, attend with your consultant. Stay factual, provide documents for every questioned item, and do not make oral commitments without written records.</p>

<h3>Step 5 — Respond to the Draft Assessment Order</h3>
<p>After the audit, FBR issues a Draft Assessment Order showing proposed additional tax. You have the right to show cause against this order — submit your objections within the given time. The Commissioner must consider your response before finalising the assessment.</p>

<h3>Step 6 — Appeal if Assessment is Unreasonable</h3>
<p>If the final assessment is still excessive, file an appeal to the Commissioner (Appeals) under Section 127 within 30 days. You can also use Alternative Dispute Resolution (ADR) under Section 134A for faster settlement.</p>

<h2>Frequently Asked Questions</h2>
<div class="faq-list">
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">Can FBR audit me even if I filed correctly? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Yes. Computer ballot selection is random — any filer can be selected regardless of whether their return is accurate. If selected, you simply need to produce your supporting documents to confirm what you declared. An accurate return with proper records makes the audit straightforward.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">How many years back can FBR audit me? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Under Section 122, FBR can amend an assessment within 5 years for normal cases. For fraud or tax evasion, there is no limitation period under Section 122(5A). In practice, most audits cover the last 3 years.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">What is the penalty if FBR finds unreported income in an audit? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Tax on the unreported income plus a penalty of up to 100% of the tax short paid under Section 182, plus default surcharge at KIBOR+3% per annum from the date tax was due. In serious fraud cases, criminal prosecution under Section 192 is possible.</div></div>
</div>

<div class="article-cta">
  <h3>Facing an FBR Audit? We Handle It</h3>
  <p>Kamboh Associates represents clients in FBR audits across Pakistan. We review your case, prepare documents, attend hearings, and minimise your audit risk. WhatsApp us today.</p>
  <a href="https://wa.me/923284675162?text=I+am+facing+an+FBR+audit+and+need+professional+help" class="wa-btn"><i class="fab fa-whatsapp"></i> WhatsApp Now — 0328-4675162</a>
</div>
</article>`);

// ══════════════════════════════════════════════════════════════
// 10. Withholding Tax Pakistan 2026
// ══════════════════════════════════════════════════════════════
rewriteArticle('blogs/withholding-tax-pakistan-2026.html', `<article class="article-body">
<p class="article-lead">Withholding tax (WHT) is the most common form of tax collection in Pakistan — deducted at source from payments before the recipient gets them. This complete guide covers WHT rates for 2026, who deducts it, how to claim credit, and how being a filer saves you money on every transaction.</p>

<h2>What is Withholding Tax in Pakistan?</h2>
<p>Withholding tax is an advance collection mechanism under the Income Tax Ordinance 2001 where a person making a payment (the withholding agent) deducts tax at a specified rate before handing over the amount to the recipient. The recipient can then adjust this WHT against their final annual tax liability when filing their return.</p>
<p>Pakistan has one of the most extensive WHT systems in the world — covering over 60 different payment types under Sections 148 to 236U of the ITO 2001.</p>

<h2>Filer vs Non-Filer WHT Rates — Key Comparison 2026</h2>
<table class="data-table">
  <thead><tr><th>Section</th><th>Transaction</th><th>Filer Rate</th><th>Non-Filer Rate</th></tr></thead>
  <tbody>
    <tr><td>231A</td><td>Cash withdrawal above Rs. 50,000/day</td><td>0%</td><td>0.6%</td></tr>
    <tr><td>151</td><td>Bank profit / savings interest</td><td>15%</td><td>30%</td></tr>
    <tr><td>150</td><td>Dividend from company</td><td>15%</td><td>30%</td></tr>
    <tr><td>236C</td><td>Sale of immovable property</td><td>3%</td><td>6%</td></tr>
    <tr><td>236K</td><td>Purchase of immovable property</td><td>3%</td><td>6%</td></tr>
    <tr><td>231B</td><td>Vehicle registration (1001–1800cc)</td><td>Rs. 25,000</td><td>Rs. 75,000</td></tr>
    <tr><td>148</td><td>Imports (commercial)</td><td>2.5–5.5%</td><td>Up to 9%</td></tr>
    <tr><td>156</td><td>Prize bond / lottery winnings above Rs. 40,000</td><td>15%</td><td>25%</td></tr>
    <tr><td>233</td><td>Commission income</td><td>12%</td><td>15%</td></tr>
    <tr><td>236A</td><td>Sale of goods by auction</td><td>10%</td><td>12%</td></tr>
    <tr><td>153(1)(a)</td><td>Sale of goods (by company)</td><td>4%</td><td>8%</td></tr>
    <tr><td>153(1)(b)</td><td>Rendering of services</td><td>8%</td><td>16%</td></tr>
    <tr><td>155</td><td>Rent of immovable property</td><td>15%</td><td>30%</td></tr>
  </tbody>
</table>

<h2>Who is a Withholding Agent in Pakistan?</h2>
<p>A withholding agent is any person required by law to deduct WHT before making a payment. This includes:</p>
<ul>
  <li>All companies (private limited, public limited)</li>
  <li>AOPs (associations of persons) with annual turnover above Rs. 100 million</li>
  <li>Federal and provincial government departments and agencies</li>
  <li>Banks and financial institutions</li>
  <li>Individuals who are company directors or partners in a large firm</li>
</ul>
<p>If you are a withholding agent, you must deduct WHT, deposit it to FBR by the 15th of the following month, and file a monthly WHT statement (Form 165) by the 15th.</p>

<h2>How to Claim WHT Credit in Your Tax Return</h2>
<p>Every WHT deducted from your income is a prepaid tax that you can adjust against your final annual tax liability:</p>
<ol>
  <li>Collect WHT certificates from every deductor (bank, employer, buyer, etc.)</li>
  <li>Enter each WHT amount in the Tax Already Paid section of your IRIS return</li>
  <li>IRIS calculates: Final Tax Liability minus Total WHT Paid = Balance payable or refundable</li>
  <li>If WHT exceeds your final liability, claim a refund under Section 170</li>
</ol>

<h2>Adjustable vs Final WHT in Pakistan</h2>
<p>Not all WHT is creditable against your annual tax:</p>
<table class="data-table">
  <thead><tr><th>WHT Type</th><th>Examples</th><th>Adjustable?</th></tr></thead>
  <tbody>
    <tr><td>Adjustable WHT</td><td>Salary WHT, bank profit WHT, rent WHT, commission WHT</td><td>Yes — credit against annual tax</td></tr>
    <tr><td>Final WHT (minimum tax)</td><td>WHT on imports (Section 148), WHT on sale of goods (153), certain dividend WHT</td><td>No — this is the final tax, no further liability</td></tr>
    <tr><td>Fixed tax</td><td>Vehicle registration WHT (Section 231B)</td><td>No — fixed amount, not refundable</td></tr>
  </tbody>
</table>

<h2>Frequently Asked Questions</h2>
<div class="faq-list">
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">Can I get a refund if too much WHT was deducted? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Yes, if your total adjustable WHT paid exceeds your final income tax liability calculated in your annual return, the excess is refundable. File your return, and if a refund is due, apply to the Commissioner via IRIS. Refunds are typically processed within 3–6 months.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">What if my employer deducted wrong WHT from salary? <i class="fas fa-chevron-down"></i></div><div class="faq-a">The employer's WHT deduction is reflected in your annual return. If it was too high, you receive a refund when you file. If too low, you must pay the shortfall. Always verify your employer's tax certificate (Form 16) against your actual salary before filing your return.</div></div>
  <div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">Is WHT on bank profit the final tax or can I get it back? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Bank profit WHT under Section 151 is an adjustable advance tax for filers — you can credit it against your annual tax and claim a refund if excess. For non-filers, it becomes a final tax at 30% — no refund, no credit. This is why becoming a filer significantly reduces effective bank tax.</div></div>
</div>

<div class="article-cta">
  <h3>Questions About Withholding Tax in Pakistan?</h3>
  <p>Kamboh Associates helps businesses comply with WHT deduction and filing obligations, and helps individuals claim WHT refunds in their annual returns. WhatsApp us for a free consultation.</p>
  <a href="https://wa.me/923284675162?text=I+need+help+with+withholding+tax+in+Pakistan" class="wa-btn"><i class="fab fa-whatsapp"></i> WhatsApp Now — 0328-4675162</a>
</div>
</article>`);

console.log('\nBatch 2 complete — 5 blogs rewritten');
