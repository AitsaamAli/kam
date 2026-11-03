"""Build tools/late-filing-penalty-calculator.html from the filer vs non-filer calculator page (same shell)."""
import json, re

ROOT = "/home/user/kam"
SLUG = "late-filing-penalty-calculator"
URL = f"https://kambohassociates.com/tools/{SLUG}"
TITLE = "Late Filing Penalty and ATL Surcharge Calculator Pakistan 2026"
DESC = "Work out the Section 182 late filing penalty and the Section 182A ATL surcharge for a late income tax return in Pakistan, by filing date and tax payable."
t = open(f"{ROOT}/tools/filer-vs-non-filer-calculator.html", encoding="utf-8").read()

t = re.sub(r"<title>[^<]*</title>", f"<title>{TITLE} | Kamboh Associates</title>", t, count=1)
t = re.sub(r'<meta name="description" content="[^"]*"\s*/?>', f'<meta name="description" content="{DESC}"/>', t, count=1)
t = re.sub(r'<link rel="canonical" href="[^"]*"\s*/?>', f'<link rel="canonical" href="{URL}"/>', t, count=1)
t = re.sub(r'<meta property="og:title" content="[^"]*"\s*/?>', f'<meta property="og:title" content="{TITLE} | Kamboh Associates"/>', t, count=1)
t = re.sub(r'<meta property="og:description" content="[^"]*"\s*/?>', f'<meta property="og:description" content="{DESC}"/>', t, count=1)
t = re.sub(r'<meta property="og:url" content="[^"]*"\s*/?>', f'<meta property="og:url" content="{URL}"/>', t, count=1)
for name in ("twitter:title", "twitter:description"):
    val = TITLE if name.endswith("title") else DESC
    t = re.sub(rf'<meta name="{name}" content="[^"]*"\s*/?>', f'<meta name="{name}" content="{val}"/>', t, count=1)
t = re.sub(r'<meta name="keywords" content="[^"]*"\s*/?>',
           '<meta name="keywords" content="late filing penalty calculator pakistan, section 182 penalty, atl surcharge calculator, late tax return penalty 2026"/>', t, count=1)

FAQS = [
    ("How is the late filing penalty calculated in Pakistan?",
     "Under Section 182 as published by FBR, the penalty is 0.1% of the tax payable for each day of default, capped at 50% of the tax payable. If that works out below Rs 40,000, or no tax is payable, the penalty is Rs 40,000. Where at least 75% of income is salary below Rs 5 million, the minimum is Rs 5,000."),
    ("What is the ATL surcharge for late filers in 2026?",
     "Under Section 182A, as amended by the Finance Act 2026, a person who files after the due date is placed on the Active Taxpayers List only after paying a surcharge: Rs 25,000 for individuals, Rs 50,000 for associations of persons and Rs 100,000 for companies."),
    ("Is the ATL surcharge the same as the late filing penalty?",
     "No. The surcharge is paid to be placed on the Active Taxpayers List after a late return. The Section 182 penalty is a separate penalty for the delay and is imposed by an order of the tax officer, normally after a notice."),
    ("What does tax payable mean in the penalty formula?",
     "It means the tax chargeable on your taxable income for the year, under the assessment made or treated as made, not only the unpaid balance. Tax already deducted by an employer or bank still counts as tax payable for this formula."),
    ("Does the calculator give the final penalty FBR will charge?",
     "No. It applies the published formula to the figures you enter. The penalty is imposed by an order after a notice, where a genuine reason for the delay can be explained, and the order can be appealed. Confirm the current law at fbr.gov.pk."),
]
APP = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": TITLE, "applicationCategory": "FinanceApplication",
       "operatingSystem": "Web", "description": DESC, "url": URL, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "PKR"},
       "creator": {"@type": "Organization", "name": "Kamboh Associates", "url": "https://kambohassociates.com", "@id": "https://kambohassociates.com/#organization"}}
FAQ = {"@context": "https://schema.org", "@type": "FAQPage",
       "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
BC = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://kambohassociates.com/"},
    {"@type": "ListItem", "position": 2, "name": "Calculators", "item": "https://kambohassociates.com/tools"},
    {"@type": "ListItem", "position": 3, "name": "Late Filing Penalty Calculator", "item": URL}]}
lds = list(re.finditer(r'<script type="application/ld\+json">[\s\S]*?</script>', t))
assert len(lds) == 2, len(lds)
new_ld = "".join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + "</script>\n" for x in (APP, FAQ, BC))
t = t[:lds[1].start()] + t[lds[1].end():]
t = t[:lds[0].start()] + new_ld + t[lds[0].end():]

faq_html = "".join(f'<div class="faq-item"><h3 style="font-size:1rem;margin:14px 0 6px">{q}</h3><p>{a}</p></div>' for q, a in FAQS)
BODY = f'''<section class="blog-post-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a><i class="fas fa-chevron-right"></i><a href="/tools">Calculators</a><i class="fas fa-chevron-right"></i><span>Late Filing Penalty</span></div>
    <h1>Late Filing Penalty and ATL Surcharge Calculator Pakistan 2026</h1>
    <div class="blog-hero-meta">
      <span class="blog-meta-tag"><i class="fas fa-calendar-times"></i> Sections 182 and 182A</span>
      <span class="blog-meta-item"><i class="fas fa-check-circle" style="color:#10B981"></i> Rules checked 4 November 2026</span>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="warn-box"><i class="fas fa-info-circle"></i><p>The Tax Year 2026 return deadline for individuals and AOPs was extended to <strong>31 October 2026</strong>. This calculator applies the Section 182 penalty formula as published on fbr.gov.pk and the Section 182A surcharge as amended by the Finance Act 2026. It is an estimate, not an order.</p></div>
    <div class="calc-wrap">
      <h2 style="font-family:var(--font-serif);font-size:1.5rem;margin-bottom:6px;color:var(--text)">Estimate Your Late Return Cost</h2>
      <p style="font-size:.87rem;color:var(--text-3);margin-bottom:28px">Enter your details to see the days late, the Section 182 penalty and the ATL surcharge to rejoin the Active Taxpayers List.</p>
      <div class="calc-section">
        <label class="calc-label" for="lpType">Taxpayer</label>
        <select class="calc-input" id="lpType">
          <option value="individual">Individual (salaried, business, freelancer)</option>
          <option value="aop">Association of persons (AOP / partnership)</option>
          <option value="company">Company</option>
        </select>
      </div>
      <div class="calc-section" id="lpSalRow">
        <label class="calc-label" for="lpSal"><input type="checkbox" id="lpSal" style="margin-right:8px;vertical-align:middle"/>At least 75% of my income is salary, and my salary is below Rs 5 million</label>
      </div>
      <div class="calc-section">
        <label class="calc-label" for="lpDue">Due date of the return</label>
        <input type="date" class="calc-input" id="lpDue" value="2026-10-31"/>
      </div>
      <div class="calc-section">
        <label class="calc-label" for="lpFiled">Date you file (or expect to file)</label>
        <input type="date" class="calc-input" id="lpFiled"/>
      </div>
      <div class="calc-section">
        <label class="calc-label" for="lpTax">Tax payable for the year (PKR), including tax already deducted</label>
        <input type="number" class="calc-input" id="lpTax" placeholder="e.g. 150000" min="0" step="1000" inputmode="numeric"/>
      </div>
      <p id="lpErr" style="color:#B91C1C;font-size:.88rem;margin:-6px 0 14px" role="alert"></p>
      <button class="calc-btn" id="lpBtn" type="button"><i class="fas fa-calculator"></i> &nbsp;Calculate</button>
      <div class="calc-result" id="lpResult" aria-live="polite">
        <h3 style="font-family:var(--font-serif);font-size:1.3rem;color:var(--text);margin-bottom:18px">Your Late Return Estimate</h3>
        <div class="result-grid">
          <div class="result-card"><div class="result-label">Days late</div><div class="result-value" id="lpDays">0</div></div>
          <div class="result-card" style="border-top:3px solid #EF4444"><div class="result-label">Section 182 penalty</div><div class="result-value" style="color:#EF4444" id="lpPen">0</div><div class="result-note" id="lpPenNote"></div></div>
          <div class="result-card" style="border-top:3px solid #F59E0B"><div class="result-label">ATL surcharge (182A)</div><div class="result-value" style="color:#B45309" id="lpSur">0</div><div class="result-note" id="lpSurNote"></div></div>
          <div class="result-card"><div class="result-label">Total estimate</div><div class="result-value" id="lpTot">0</div></div>
        </div>
        <p id="lpExplain" style="font-size:.88rem;color:var(--text-2);margin-top:16px"></p>
        <div class="verify-note"><i class="fas fa-exclamation-triangle"></i> The penalty is imposed by an order after a notice; a genuine reason for delay can be explained, and the order can be appealed. Confirm the law at fbr.gov.pk.</div>
      </div>
    </div>
    <div style="margin-top:48px">
      <h2 style="font-family:var(--font-serif);font-size:1.6rem;color:var(--text);margin-bottom:12px">Rules the Calculator Uses</h2>
      <table class="data-table">
        <thead><tr><th>Item</th><th>Rule</th><th>Source</th></tr></thead>
        <tbody>
          <tr><td>Daily penalty</td><td>0.1% of tax payable for each day of default</td><td>Section 182, entry 1</td></tr>
          <tr><td>Maximum penalty</td><td>50% of tax payable</td><td>Section 182, entry 1</td></tr>
          <tr><td>Minimum penalty</td><td>Rs 40,000, also when no tax is payable</td><td>Section 182, entry 1</td></tr>
          <tr><td>Salaried minimum</td><td>Rs 5,000 where 75%+ of income is salary below Rs 5 million</td><td>Section 182, proviso</td></tr>
          <tr><td>ATL surcharge, individual</td><td>Rs 25,000</td><td>Section 182A (Finance Act 2026)</td></tr>
          <tr><td>ATL surcharge, AOP</td><td>Rs 50,000</td><td>Section 182A (Finance Act 2026)</td></tr>
          <tr><td>ATL surcharge, company</td><td>Rs 100,000</td><td>Section 182A (Finance Act 2026)</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0"><div class="container" style="max-width:820px"><h2 style="margin-bottom:12px">How to Use This Late Filing Penalty Calculator</h2><p style="margin-bottom:12px">Choose the taxpayer type, tick the salaried box if it applies to you, and check the due date. For Tax Year 2026 returns of individuals and AOPs the extended due date was 31 October 2026; companies usually file by 31 December for a June year-end. Enter the date you filed or expect to file, and the tax payable for the year as shown in your return, including tax already deducted at source.</p><p style="margin-bottom:12px">The result shows the Section 182 penalty that the published formula produces and the Section 182A surcharge needed to be placed on the Active Taxpayers List after a late return. For individuals, FBR published draft rules in October 2026 for a Form ATL-U undertaking that would replace the surcharge with a six-month promise not to acquire property; check IRIS for whether it is available when you file. Our guide to <a href="/blogs/tax-return-deadline-passed-31-october-2026-next-steps" style="color:#0D9488;font-weight:600">what to do after the 31 October deadline</a> explains each step, and our comparison of <a href="/blogs/late-filer-atl-surcharge-or-form-atl-u-undertaking-2026" style="color:#0D9488;font-weight:600">the ATL surcharge and Form ATL-U</a> helps you choose.</p><h2 style="margin:24px 0 12px">Frequently Asked Questions</h2>{faq_html}</div></section>
<section class="cta-strip">
  <div class="container">
    <h2>Late Return? We File It and Handle the ATL Step</h2>
    <p>Fixed, published fees from Rs. 3,500 for salaried returns. Penalties and surcharges are paid to FBR, not to us.</p>
    <div class="btns">
      <a href="https://wa.me/923284675162?text=Hi%2C%20I%20used%20your%20late%20filing%20penalty%20calculator%20and%20need%20help%20filing%20a%20late%20return." class="btn-primary" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp"></i> File My Late Return</a>
      <a href="/income-tax-filing" class="btn-ghost">Income Tax Filing</a>
    </div>
  </div>
</section>
<script>
(function(){{
  var SURCHARGE={{individual:25000,aop:50000,company:100000}};
  var LABEL={{individual:'individual',aop:'AOP',company:'company'}};
  function rs(n){{return 'Rs. '+Math.round(n).toLocaleString('en-PK');}}
  function $(id){{return document.getElementById(id);}}
  function pad(n){{return (n<10?'0':'')+n;}}
  var d=new Date(); $('lpFiled').value=d.getFullYear()+'-'+pad(d.getMonth()+1)+'-'+pad(d.getDate());
  function syncType(){{
    var ty=$('lpType').value; $('lpSalRow').style.display=(ty==='individual')?'':'none';
    if(ty!=='individual') $('lpSal').checked=false;
    if(ty==='company' && $('lpDue').value==='2026-10-31') $('lpDue').value='2026-12-31';
    if(ty!=='company' && $('lpDue').value==='2026-12-31') $('lpDue').value='2026-10-31';
  }}
  $('lpType').addEventListener('change',syncType);
  function days(a,b){{var x=Date.UTC(+a.slice(0,4),+a.slice(5,7)-1,+a.slice(8,10));var y=Date.UTC(+b.slice(0,4),+b.slice(5,7)-1,+b.slice(8,10));return Math.round((y-x)/86400000);}}
  $('lpBtn').addEventListener('click',function(){{
    var err=$('lpErr'); err.textContent='';
    var ty=$('lpType').value, due=$('lpDue').value, filed=$('lpFiled').value, taxRaw=$('lpTax').value;
    if(!due||!filed){{err.textContent='Please enter both the due date and the filing date.';return;}}
    if(taxRaw===''||isNaN(parseFloat(taxRaw))||parseFloat(taxRaw)<0){{err.textContent='Please enter the tax payable for the year (enter 0 if no tax is payable).';return;}}
    var tax=parseFloat(taxRaw), n=days(due,filed);
    var pen=0, sur=0, note='', explain='';
    if(n<=0){{
      note='Filed on time'; explain='The return is on or before the due date, so no Section 182 late filing penalty or ATL surcharge applies.';
    }} else {{
      var min=$('lpSal').checked?5000:40000;
      var raw=tax*0.001*n, cap=tax*0.5, worked=Math.min(raw,cap);
      if(tax<=0||worked<min){{pen=min; note='Minimum penalty applies';}}
      else {{pen=worked; note=(raw>cap)?'Capped at 50% of tax payable':'0.1% × '+rs(tax)+' × '+n+' days';}}
      sur=SURCHARGE[ty];
      explain='Filed '+n+' day'+(n===1?'':'s')+' after the due date. Formula: 0.1% of tax payable per day ('+rs(raw)+'), capped at 50% ('+rs(cap)+'), with a minimum of '+rs(min)+'. To be placed on the Active Taxpayers List, a late-filing '+LABEL[ty]+' pays a surcharge of '+rs(sur)+'.'+(ty==='individual'?' If FBR finalises Form ATL-U, an individual may instead give a six-month no-property undertaking.':'');
    }}
    $('lpDays').textContent=Math.max(n,0);
    $('lpPen').textContent=rs(pen); $('lpPenNote').textContent=note;
    $('lpSur').textContent=rs(sur); $('lpSurNote').textContent=sur?('Section 182A, '+LABEL[ty]):'';
    $('lpTot').textContent=rs(pen+sur); $('lpExplain').textContent=explain;
    $('lpResult').classList.add('show');
  }});
  syncType();
}})();
</script>
'''
a = t.index('<section class="blog-post-hero">')
b = t.index("<footer>")
t = t[:a] + BODY + t[b:]
open(f"{ROOT}/tools/{SLUG}.html", "w", encoding="utf-8").write(t)
print("written", len(t))
