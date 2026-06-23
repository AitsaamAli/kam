const fs = require('fs');
const path = require('path');
const BLOGS_DIR = path.join(__dirname, 'blogs');

// ── 150 NEW LAHORE AREAS ──────────────────────────────────────────────────────
const NEW_LAHORE = [
  { slug: 'tax-consultant-gulberg-4-lahore', area: 'Gulberg 4', city: 'Lahore' },
  { slug: 'tax-consultant-johar-town-block-a-lahore', area: 'Johar Town Block A', city: 'Lahore' },
  { slug: 'tax-consultant-johar-town-block-b-lahore', area: 'Johar Town Block B', city: 'Lahore' },
  { slug: 'tax-consultant-johar-town-block-c-lahore', area: 'Johar Town Block C', city: 'Lahore' },
  { slug: 'tax-consultant-johar-town-block-d-lahore', area: 'Johar Town Block D', city: 'Lahore' },
  { slug: 'tax-consultant-johar-town-block-g-lahore', area: 'Johar Town Block G', city: 'Lahore' },
  { slug: 'tax-consultant-johar-town-block-k-lahore', area: 'Johar Town Block K', city: 'Lahore' },
  { slug: 'tax-consultant-johar-town-block-l-lahore', area: 'Johar Town Block L', city: 'Lahore' },
  { slug: 'tax-consultant-model-town-block-d-lahore', area: 'Model Town Block D', city: 'Lahore' },
  { slug: 'tax-consultant-model-town-block-e-lahore', area: 'Model Town Block E', city: 'Lahore' },
  { slug: 'tax-consultant-model-town-block-f-lahore', area: 'Model Town Block F', city: 'Lahore' },
  { slug: 'tax-consultant-model-town-block-g-lahore', area: 'Model Town Block G', city: 'Lahore' },
  { slug: 'tax-consultant-model-town-block-h-lahore', area: 'Model Town Block H', city: 'Lahore' },
  { slug: 'tax-consultant-model-town-block-i-lahore', area: 'Model Town Block I', city: 'Lahore' },
  { slug: 'tax-consultant-model-town-block-j-lahore', area: 'Model Town Block J', city: 'Lahore' },
  { slug: 'tax-consultant-model-town-block-k-lahore', area: 'Model Town Block K', city: 'Lahore' },
  { slug: 'tax-consultant-model-town-block-l-lahore', area: 'Model Town Block L', city: 'Lahore' },
  { slug: 'tax-consultant-askari-2-lahore', area: 'Askari 2', city: 'Lahore' },
  { slug: 'tax-consultant-askari-3-lahore', area: 'Askari 3', city: 'Lahore' },
  { slug: 'tax-consultant-askari-4-lahore', area: 'Askari 4', city: 'Lahore' },
  { slug: 'tax-consultant-askari-5-lahore', area: 'Askari 5', city: 'Lahore' },
  { slug: 'tax-consultant-askari-6-lahore', area: 'Askari 6', city: 'Lahore' },
  { slug: 'tax-consultant-askari-7-lahore', area: 'Askari 7', city: 'Lahore' },
  { slug: 'tax-consultant-askari-8-lahore', area: 'Askari 8', city: 'Lahore' },
  { slug: 'tax-consultant-askari-9-lahore', area: 'Askari 9', city: 'Lahore' },
  { slug: 'tax-consultant-askari-13-lahore', area: 'Askari 13', city: 'Lahore' },
  { slug: 'tax-consultant-askari-14-lahore', area: 'Askari 14', city: 'Lahore' },
  { slug: 'tax-consultant-valencia-block-a-lahore', area: 'Valencia Block A', city: 'Lahore' },
  { slug: 'tax-consultant-valencia-block-b-lahore', area: 'Valencia Block B', city: 'Lahore' },
  { slug: 'tax-consultant-valencia-block-c-lahore', area: 'Valencia Block C', city: 'Lahore' },
  { slug: 'tax-consultant-valencia-block-d-lahore', area: 'Valencia Block D', city: 'Lahore' },
  { slug: 'tax-consultant-valencia-block-e-lahore', area: 'Valencia Block E', city: 'Lahore' },
  { slug: 'tax-consultant-valencia-block-f-lahore', area: 'Valencia Block F', city: 'Lahore' },
  { slug: 'tax-consultant-valencia-phase-2-lahore', area: 'Valencia Phase 2', city: 'Lahore' },
  { slug: 'tax-consultant-bahria-nasheman-lahore', area: 'Bahria Nasheman', city: 'Lahore' },
  { slug: 'tax-consultant-bahria-education-city-lahore', area: 'Bahria Education & Medical City', city: 'Lahore' },
  { slug: 'tax-consultant-central-park-lahore', area: 'Central Park Housing Society', city: 'Lahore' },
  { slug: 'tax-consultant-new-lahore-city', area: 'New Lahore City', city: 'Lahore' },
  { slug: 'tax-consultant-sa-gardens-lahore', area: 'SA Gardens', city: 'Lahore' },
  { slug: 'tax-consultant-lahore-smart-city', area: 'Lahore Smart City', city: 'Lahore' },
  { slug: 'tax-consultant-defence-road-lahore', area: 'Defence Road', city: 'Lahore' },
  { slug: 'tax-consultant-jail-road-lahore', area: 'Jail Road', city: 'Lahore' },
  { slug: 'tax-consultant-davis-road-lahore', area: 'Davis Road', city: 'Lahore' },
  { slug: 'tax-consultant-empress-road-lahore', area: 'Empress Road', city: 'Lahore' },
  { slug: 'tax-consultant-lawrence-road-lahore', area: 'Lawrence Road', city: 'Lahore' },
  { slug: 'tax-consultant-zafar-ali-road-lahore', area: 'Zafar Ali Road', city: 'Lahore' },
  { slug: 'tax-consultant-walton-road-lahore', area: 'Walton Road', city: 'Lahore' },
  { slug: 'tax-consultant-abbot-road-lahore', area: 'Abbot Road', city: 'Lahore' },
  { slug: 'tax-consultant-temple-road-lahore', area: 'Temple Road', city: 'Lahore' },
  { slug: 'tax-consultant-queens-road-lahore', area: 'Queens Road', city: 'Lahore' },
  { slug: 'tax-consultant-nishat-colony-lahore', area: 'Nishat Colony', city: 'Lahore' },
  { slug: 'tax-consultant-saeed-park-lahore', area: 'Saeed Park', city: 'Lahore' },
  { slug: 'tax-consultant-peoples-colony-lahore', area: 'Peoples Colony', city: 'Lahore' },
  { slug: 'tax-consultant-barkat-nagar-lahore', area: 'Barkat Nagar', city: 'Lahore' },
  { slug: 'tax-consultant-islamia-park-lahore', area: 'Islamia Park', city: 'Lahore' },
  { slug: 'tax-consultant-shaheen-park-lahore', area: 'Shaheen Park', city: 'Lahore' },
  { slug: 'tax-consultant-gul-ahmed-colony-lahore', area: 'Gul Ahmed Colony', city: 'Lahore' },
  { slug: 'tax-consultant-farooq-colony-lahore', area: 'Farooq Colony', city: 'Lahore' },
  { slug: 'tax-consultant-noor-colony-lahore', area: 'Noor Colony', city: 'Lahore' },
  { slug: 'tax-consultant-islampura-lahore', area: 'Islampura', city: 'Lahore' },
  { slug: 'tax-consultant-shimla-hill-lahore', area: 'Shimla Hill', city: 'Lahore' },
  { slug: 'tax-consultant-gulshan-park-lahore', area: 'Gulshan Park', city: 'Lahore' },
  { slug: 'tax-consultant-jubilee-town-lahore', area: 'Jubilee Town', city: 'Lahore' },
  { slug: 'tax-consultant-township-sector-a-lahore', area: 'Township Sector A', city: 'Lahore' },
  { slug: 'tax-consultant-township-sector-d-lahore', area: 'Township Sector D', city: 'Lahore' },
  { slug: 'tax-consultant-sabzazar-block-a-lahore', area: 'Sabzazar Block A', city: 'Lahore' },
  { slug: 'tax-consultant-sabzazar-block-b-lahore', area: 'Sabzazar Block B', city: 'Lahore' },
  { slug: 'tax-consultant-sabzazar-block-c-lahore', area: 'Sabzazar Block C', city: 'Lahore' },
  { slug: 'tax-consultant-nishtar-colony-block-a-lahore', area: 'Nishtar Colony Block A', city: 'Lahore' },
  { slug: 'tax-consultant-nishtar-colony-block-b-lahore', area: 'Nishtar Colony Block B', city: 'Lahore' },
  { slug: 'tax-consultant-safari-garden-phase-2-lahore', area: 'Safari Garden Phase 2', city: 'Lahore' },
  { slug: 'tax-consultant-eden-boulevard-lahore', area: 'Eden Boulevard', city: 'Lahore' },
  { slug: 'tax-consultant-eden-residencia-lahore', area: 'Eden Residencia', city: 'Lahore' },
  { slug: 'tax-consultant-eden-orchard-lahore', area: 'Eden Orchard', city: 'Lahore' },
  { slug: 'tax-consultant-pak-arab-housing-lahore', area: 'Pak Arab Housing Society', city: 'Lahore' },
  { slug: 'tax-consultant-al-noor-town-lahore', area: 'Al-Noor Town', city: 'Lahore' },
  { slug: 'tax-consultant-iqbal-avenue-lahore', area: 'Iqbal Avenue', city: 'Lahore' },
  { slug: 'tax-consultant-canal-park-lahore', area: 'Canal Park', city: 'Lahore' },
  { slug: 'tax-consultant-canal-view-lahore', area: 'Canal View Housing Society', city: 'Lahore' },
  { slug: 'tax-consultant-bahria-rafi-block-lahore', area: 'Bahria Town Rafi Block', city: 'Lahore' },
  { slug: 'tax-consultant-bahria-umer-block-lahore', area: 'Bahria Town Umer Block', city: 'Lahore' },
  { slug: 'tax-consultant-bahria-usman-block-lahore', area: 'Bahria Town Usman Block', city: 'Lahore' },
  { slug: 'tax-consultant-bahria-nishtar-block-lahore', area: 'Bahria Town Nishtar Block', city: 'Lahore' },
  { slug: 'tax-consultant-dha-phase-9-prism-lahore', area: 'DHA Phase 9 Prism', city: 'Lahore' },
  { slug: 'tax-consultant-dha-phase-9-town-lahore', area: 'DHA Phase 9 Town', city: 'Lahore' },
  { slug: 'tax-consultant-dha-phase-10-lahore', area: 'DHA Phase 10', city: 'Lahore' },
  { slug: 'tax-consultant-dha-y-block-lahore', area: 'DHA Y Block', city: 'Lahore' },
  { slug: 'tax-consultant-dha-q-block-lahore', area: 'DHA Q Block', city: 'Lahore' },
  { slug: 'tax-consultant-paf-colony-lahore', area: 'PAF Colony', city: 'Lahore' },
  { slug: 'tax-consultant-railways-colony-lahore', area: 'Railways Colony', city: 'Lahore' },
  { slug: 'tax-consultant-sui-gas-society-lahore', area: 'Sui Gas Housing Society', city: 'Lahore' },
  { slug: 'tax-consultant-wapda-officers-colony-lahore', area: 'WAPDA Officers Colony', city: 'Lahore' },
  { slug: 'tax-consultant-state-life-phase-2-lahore', area: 'State Life Housing Phase 2', city: 'Lahore' },
  { slug: 'tax-consultant-punjab-govt-employees-lahore', area: 'Punjab Govt Employees Housing Society', city: 'Lahore' },
  { slug: 'tax-consultant-johar-town-h4-lahore', area: 'Johar Town H4', city: 'Lahore' },
  { slug: 'tax-consultant-johar-town-j5-lahore', area: 'Johar Town J5', city: 'Lahore' },
  { slug: 'tax-consultant-samanabad-block-c-lahore', area: 'Samanabad Block C', city: 'Lahore' },
  { slug: 'tax-consultant-samanabad-block-e-lahore', area: 'Samanabad Block E', city: 'Lahore' },
  { slug: 'tax-consultant-samanabad-block-f-lahore', area: 'Samanabad Block F', city: 'Lahore' },
  { slug: 'tax-consultant-samanabad-block-g-lahore', area: 'Samanabad Block G', city: 'Lahore' },
  { slug: 'tax-consultant-samanabad-block-h-lahore', area: 'Samanabad Block H', city: 'Lahore' },
  { slug: 'tax-consultant-samanabad-block-j-lahore', area: 'Samanabad Block J', city: 'Lahore' },
  { slug: 'tax-consultant-green-town-block-c-lahore', area: 'Green Town Block C', city: 'Lahore' },
  { slug: 'tax-consultant-green-town-block-d-lahore', area: 'Green Town Block D', city: 'Lahore' },
  { slug: 'tax-consultant-green-town-block-e-lahore', area: 'Green Town Block E', city: 'Lahore' },
  { slug: 'tax-consultant-gulshan-ravi-block-e-lahore', area: 'Gulshan-e-Ravi Block E', city: 'Lahore' },
  { slug: 'tax-consultant-gulshan-ravi-block-f-lahore', area: 'Gulshan-e-Ravi Block F', city: 'Lahore' },
  { slug: 'tax-consultant-city-housing-society-lahore', area: 'City Housing Society', city: 'Lahore' },
  { slug: 'tax-consultant-nasheman-e-iqbal-lahore', area: 'Nasheman-e-Iqbal', city: 'Lahore' },
  { slug: 'tax-consultant-river-garden-lahore', area: 'River Garden Housing Society', city: 'Lahore' },
  { slug: 'tax-consultant-near-ittefaq-hospital-lahore', area: 'Near Ittefaq Hospital', city: 'Lahore' },
  { slug: 'tax-consultant-near-doctors-hospital-lahore', area: 'Near Doctors Hospital', city: 'Lahore' },
  { slug: 'tax-consultant-near-jinnah-hospital-lahore', area: 'Near Jinnah Hospital', city: 'Lahore' },
  { slug: 'tax-consultant-near-ganga-ram-lahore', area: 'Near Ganga Ram Hospital', city: 'Lahore' },
  { slug: 'tax-consultant-near-shalamar-hospital-lahore', area: 'Near Shalamar Hospital', city: 'Lahore' },
  { slug: 'tax-consultant-near-sheikh-zayed-lahore', area: 'Near Sheikh Zayed Hospital', city: 'Lahore' },
  { slug: 'tax-consultant-near-gcu-lahore', area: 'Near GCU (Government College)', city: 'Lahore' },
  { slug: 'tax-consultant-near-fast-nuces-lahore', area: 'Near FAST NUCES', city: 'Lahore' },
  { slug: 'tax-consultant-near-ucp-lahore', area: 'Near UCP University', city: 'Lahore' },
  { slug: 'tax-consultant-near-comsats-lahore', area: 'Near COMSATS Lahore', city: 'Lahore' },
  { slug: 'tax-consultant-model-town-commercial-lahore', area: 'Model Town Commercial Market', city: 'Lahore' },
  { slug: 'tax-consultant-garden-town-super-market-lahore', area: 'Garden Town Super Market', city: 'Lahore' },
  { slug: 'tax-consultant-gulberg-main-market-lahore', area: 'Gulberg Main Market', city: 'Lahore' },
  { slug: 'tax-consultant-liberty-chowk-lahore', area: 'Liberty Chowk', city: 'Lahore' },
  { slug: 'tax-consultant-mochi-gate-lahore', area: 'Mochi Gate', city: 'Lahore' },
  { slug: 'tax-consultant-sheranwala-gate-lahore', area: 'Sheranwala Gate', city: 'Lahore' },
  { slug: 'tax-consultant-taxali-gate-lahore', area: 'Taxali Gate', city: 'Lahore' },
  { slug: 'tax-consultant-roshnai-gate-lahore', area: 'Roshnai Gate', city: 'Lahore' },
  { slug: 'tax-consultant-yakki-gate-lahore', area: 'Yakki Gate', city: 'Lahore' },
  { slug: 'tax-consultant-mori-gate-lahore', area: 'Mori Gate', city: 'Lahore' },
  { slug: 'tax-consultant-kashmiri-gate-lahore', area: 'Kashmiri Gate', city: 'Lahore' },
  { slug: 'tax-consultant-sheikhupura-road-lahore', area: 'Sheikhupura Road', city: 'Lahore' },
  { slug: 'tax-consultant-manga-road-lahore', area: 'Manga Road', city: 'Lahore' },
  { slug: 'tax-consultant-thokar-niaz-baig-road-lahore', area: 'Near Thokar Niaz Baig', city: 'Lahore' },
  { slug: 'tax-consultant-khayaban-e-jinnah-lahore', area: 'Khayaban-e-Jinnah Road', city: 'Lahore' },
  { slug: 'tax-consultant-khayaban-e-sir-syed-lahore', area: 'Khayaban-e-Sir Syed', city: 'Lahore' },
  { slug: 'tax-consultant-gulberg-green-lahore', area: 'Gulberg Green', city: 'Lahore' },
  { slug: 'tax-consultant-paragon-city-phase-3-lahore', area: 'Paragon City Phase 3', city: 'Lahore' },
  { slug: 'tax-consultant-green-fort-lahore', area: 'Green Fort Housing Society', city: 'Lahore' },
  { slug: 'tax-consultant-green-acres-lahore', area: 'Green Acres Housing Society', city: 'Lahore' },
  { slug: 'tax-consultant-pak-kisan-town-lahore', area: 'Pak Kisan Town', city: 'Lahore' },
  { slug: 'tax-consultant-ravi-town-lahore', area: 'Ravi Town', city: 'Lahore' },
];

// ── PAGE TEMPLATE ─────────────────────────────────────────────────────────────
const SHARED_STYLE = `<style>:root{--navy:#0F172A;--teal:#14B8A6;--gold-light:#D4AF37;--font-display:'Cinzel',serif;--font-serif:'Cormorant Garamond',Georgia,serif;--font-body:'DM Sans',system-ui,sans-serif;--max-w:1200px}*{box-sizing:border-box;margin:0;padding:0}body{font-family:var(--font-body);background:#fff;color:#0F172A;line-height:1.65;overflow-x:hidden}a{text-decoration:none;color:inherit}ul{list-style:none}.container{max-width:var(--max-w);margin:0 auto;padding:0 24px}.topbar{background:#0F172A;padding:8px 0}.topbar .container{display:flex;justify-content:center;overflow:hidden}.topbar-promo-wrap{display:inline-flex;animation:kascroll 28s linear infinite}.topbar-promo{font-size:.73rem;color:rgba(148,163,184,.9);white-space:nowrap;flex-shrink:0}@keyframes kascroll{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}.navbar{position:sticky;top:0;z-index:1000;background:rgba(255,255,255,.97);backdrop-filter:blur(20px);border-bottom:1px solid #E2E8F0}.navbar .container{display:flex;align-items:center;justify-content:space-between;height:68px}.logo{display:flex;align-items:center;gap:12px}.logo-name{font-family:var(--font-display);font-size:.92rem;font-weight:700;letter-spacing:.07em;line-height:1.2}.logo-sub{font-size:.56rem;letter-spacing:.18em;color:var(--gold-light);text-transform:uppercase}.nav-links{display:flex;align-items:center;gap:4px}.nav-links>li{position:relative;list-style:none}.nav-links>li>a{font-size:.84rem;font-weight:500;color:#1E293B;display:flex;align-items:center;gap:4px;padding:8px 14px;border-radius:8px;transition:all .2s}.nav-links>li>a:hover{color:#14B8A6;background:#F0FDFA}.nav-chevron{font-size:.6rem;opacity:.6}.nav-drop{position:absolute;top:calc(100% + 8px);left:50%;transform:translateX(-50%) translateY(-6px);min-width:200px;background:#fff;border:1px solid #E2E8F0;border-radius:12px;box-shadow:0 8px 32px rgba(15,23,42,.12);padding:8px;opacity:0;visibility:hidden;pointer-events:none;transition:all .2s}.nav-links>li:hover .nav-drop{opacity:1;visibility:visible;pointer-events:auto;transform:translateX(-50%) translateY(0)}.nav-links>li:last-child .nav-drop{left:auto;right:0;transform:translateY(-6px)}.nav-links>li:last-child:hover .nav-drop{transform:translateY(0)}.nav-drop a{display:flex;align-items:center;gap:10px;padding:9px 12px;border-radius:8px;font-size:.82rem;color:#1E293B;transition:all .15s}.nav-drop a:hover{background:#F0FDFA;color:#14B8A6}.nav-drop a i{width:16px;text-align:center;color:#14B8A6}.nav-drop-divider{height:1px;background:#E2E8F0;margin:4px 8px}.nav-actions{display:flex;align-items:center;gap:10px}.nav-phone{font-size:.8rem;color:#64748B;display:flex;align-items:center;gap:6px}.nav-phone i{color:#14B8A6}.nav-phone a{color:#1E293B;font-weight:500}.nav-cta{background:#0F172A;color:#fff!important;padding:8px 18px!important;border-radius:8px!important;font-size:.82rem!important;font-weight:600!important;transition:all .2s!important}.nav-cta:hover{background:#14B8A6!important}.hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;background:none;border:none;padding:4px}.hamburger span{width:22px;height:2px;background:#64748B;border-radius:2px;display:block}.mobile-nav{display:none;flex-direction:column;position:fixed;top:68px;left:0;right:0;z-index:999;background:#fff;border-bottom:3px solid #14B8A6;box-shadow:0 12px 40px rgba(0,0,0,.15)}.mobile-nav.open{display:flex}.mobile-nav a{padding:14px 24px;border-bottom:1px solid #F1F5F9;font-size:.9rem;color:#64748B}.blog-hero{background:linear-gradient(135deg,#0F172A 0%,#1E3A5F 60%,#0F4C5C 100%);padding:64px 0 52px;position:relative;overflow:hidden}.blog-hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 70% 30%,rgba(20,184,166,.1) 0%,transparent 60%)}.blog-hero .container{position:relative;z-index:1}.breadcrumb{display:flex;align-items:center;gap:8px;font-size:.78rem;color:rgba(148,163,184,.7);margin-bottom:20px;flex-wrap:wrap}.breadcrumb a{color:rgba(148,163,184,.7)}.breadcrumb a:hover{color:#14B8A6}.breadcrumb i{font-size:.55rem}.blog-cat{display:inline-flex;align-items:center;gap:5px;background:rgba(20,184,166,.15);border:1px solid rgba(20,184,166,.3);border-radius:100px;padding:4px 14px;font-size:.68rem;color:#14B8A6;font-family:var(--font-display);letter-spacing:.1em;text-transform:uppercase;margin-bottom:14px}.blog-hero h1{font-family:var(--font-serif);font-size:clamp(1.9rem,4vw,3rem);font-weight:700;color:#F1F5F9;line-height:1.15;margin-bottom:16px;max-width:800px}.blog-meta{display:flex;flex-wrap:wrap;gap:18px;font-size:.8rem;color:rgba(148,163,184,.8)}.blog-meta span{display:flex;align-items:center;gap:5px}.blog-meta i{color:#14B8A6}.blog-layout{display:grid;grid-template-columns:1fr 300px;gap:48px;padding:56px 0 80px;align-items:start}.article-body{background:#fff;border:1px solid #E2E8F0;border-radius:20px;padding:40px 44px;box-shadow:0 1px 3px rgba(15,23,42,.08)}.article-lead{font-family:var(--font-serif);font-size:1.15rem;color:#1E293B;line-height:1.8;margin-bottom:32px;padding-bottom:24px;border-bottom:1px solid #E2E8F0}.article-body h2{font-family:var(--font-serif);font-size:1.5rem;font-weight:600;color:#0F172A;margin:36px 0 14px;display:flex;align-items:center;gap:10px}.article-body h2::before{content:'';width:4px;height:24px;background:linear-gradient(135deg,#14B8A6,#0D9488);border-radius:2px;flex-shrink:0}.article-body p{font-size:.96rem;color:#1E293B;line-height:1.82;margin-bottom:16px}.article-body ul{margin:8px 0 16px 20px;display:flex;flex-direction:column;gap:6px}.article-body ul li{font-size:.94rem;color:#1E293B;list-style:disc;line-height:1.7}.article-body table{width:100%;border-collapse:collapse;margin:16px 0}.article-body th{background:#0F172A;color:#fff;padding:10px 14px;font-size:.84rem;text-align:left}.article-body td{padding:10px 14px;border-bottom:1px solid #E2E8F0;font-size:.88rem}.article-body tr:nth-child(even) td{background:#F8FAFC}.highlight-box{background:rgba(20,184,166,.07);border-left:4px solid #14B8A6;border-radius:0 12px 12px 0;padding:16px 20px;margin:20px 0}.highlight-box p{margin:0;font-size:.93rem}.faq-item{border:1px solid #E2E8F0;border-radius:12px;margin-bottom:10px;overflow:hidden}.faq-q{padding:15px 20px;font-weight:600;cursor:pointer;display:flex;justify-content:space-between;align-items:center;font-size:.92rem;background:#F8FAFC}.faq-q:hover{color:#14B8A6}.faq-q i{transition:transform .3s;color:#14B8A6}.faq-a{display:none;padding:14px 20px;border-top:1px solid #E2E8F0;font-size:.88rem;line-height:1.7}.faq-item.open .faq-a{display:block}.faq-item.open .faq-q i{transform:rotate(180deg)}.sidebar-card{background:#fff;border:1px solid #E2E8F0;border-radius:12px;padding:22px;margin-bottom:20px}.sidebar-card h4{font-family:var(--font-serif);font-size:1rem;font-weight:700;margin-bottom:12px;padding-bottom:10px;border-bottom:2px solid #E2E8F0}.consult-card{background:linear-gradient(135deg,#0F172A,#1E3A5F);border-radius:12px;padding:24px;color:#fff;text-align:center;margin-bottom:20px}.consult-card h4{font-family:var(--font-serif);font-size:1.1rem;margin-bottom:8px}.consult-card p{font-size:.83rem;color:#94A3B8;margin-bottom:16px}.wa-btn{display:inline-flex;align-items:center;gap:8px;background:#25D366;color:#fff;padding:11px 22px;border-radius:100px;font-weight:600;font-size:.88rem;width:100%;justify-content:center}.price-badge{background:linear-gradient(135deg,#14B8A6,#0D9488);color:#fff;border-radius:12px;padding:18px;text-align:center;margin-bottom:12px}.price-badge .amount{font-family:var(--font-serif);font-size:1.8rem;font-weight:700}.price-badge .from{font-size:.78rem;opacity:.8}.service-list li{padding:7px 0;border-bottom:1px solid #E2E8F0;font-size:.86rem;display:flex;align-items:center;gap:8px}.service-list li:last-child{border-bottom:none}.service-list li i{color:#14B8A6;width:14px}@media(max-width:900px){.blog-layout{grid-template-columns:1fr}.nav-links,.nav-phone{display:none}.hamburger{display:flex}}@media(max-width:600px){.article-body{padding:24px 20px}.blog-hero{padding:44px 0 36px}}</style>`;

const NAV = `<div class="topbar"><div class="container"><div class="topbar-promo-wrap"><span class="topbar-promo">KAMBOH ASSOCIATES LAHORE — ALLAMA IQBAL TOWN, OPP. SHELL PUMP, MAIN BOULEVARD &nbsp;&bull;&nbsp; 0328-4675162 &nbsp;&bull;&nbsp; TAX CONSULTANT LAHORE &nbsp;&bull;&nbsp; 18+ YEARS EXPERIENCE &nbsp;&bull;&nbsp;</span></div></div></div>
<nav class="navbar"><div class="container"><a href="/" class="logo"><div><svg width="44" height="44" viewBox="0 0 46 46" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="g1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1a3a1a"/><stop offset="100%" stop-color="#0d2a0d"/></linearGradient><linearGradient id="g2" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#F0CF6B"/><stop offset="100%" stop-color="#D4AF37"/></linearGradient></defs><circle cx="23" cy="23" r="23" fill="url(#g1)"/><circle cx="23" cy="23" r="21" fill="none" stroke="url(#g2)" stroke-width="1.5"/><text x="23" y="27" font-family="Cinzel,serif" font-size="13" font-weight="700" fill="url(#g2)" text-anchor="middle" letter-spacing="1">KA</text><path id="cp" d="M 23,23 m -17,0 a 17,17 0 1,1 34,0 a 17,17 0 1,1 -34,0" fill="none"/><text font-family="Cinzel,serif" font-size="3.8" fill="#D4AF37" letter-spacing="1.8"><textPath href="#cp" startOffset="3%">KAMBOH ASSOCIATES &bull; TAX CONSULTANT &bull;</textPath></text></svg></div><div><div class="logo-name">KAMBOH ASSOCIATES</div><div class="logo-sub">Tax &amp; Regulatory Excellence</div></div></a>
<ul class="nav-links"><li><a href="/">Home</a></li><li><a href="/income-tax-filing">Services <i class="fas fa-chevron-down nav-chevron"></i></a><div class="nav-drop"><a href="/income-tax-filing"><i class="fas fa-file-invoice-dollar"></i> Income Tax Filing</a><a href="/ntn-registration"><i class="fas fa-id-card"></i> NTN Registration</a><a href="/sales-tax-registration"><i class="fas fa-percent"></i> Sales Tax Registration</a><a href="/secp-vs-sole-proprietorship-pakistan"><i class="fas fa-building"></i> Company Registration</a><div class="nav-drop-divider"></div><a href="/fbr-notice-defense"><i class="fas fa-shield-alt"></i> FBR Notice Defense</a><a href="/wealth-statement"><i class="fas fa-wallet"></i> Wealth Statement</a><a href="/withholding-tax"><i class="fas fa-hand-holding-usd"></i> Withholding Tax</a><a href="/aop-tax-return"><i class="fas fa-handshake"></i> AOP Tax Return</a><div class="nav-drop-divider"></div><a href="/pricing"><i class="fas fa-tags"></i> Pricing &amp; Fees</a></div></li><li><a href="/pricing">Pricing</a></li><li><a href="/contact">Contact</a></li><li><a href="/blogs">Blog</a></li></ul>
<div class="nav-actions"><span class="nav-phone"><i class="fas fa-phone"></i><a href="tel:03284675162">0328-4675162</a></span><a href="/contact" class="nav-cta">Get Started</a><button class="hamburger" id="hamburger" onclick="this.classList.toggle('open');document.getElementById('mobileNav').classList.toggle('open')" aria-label="Menu"><span></span><span></span><span></span></button></div></div></nav>
<div class="mobile-nav" id="mobileNav"><a href="/">Home</a><a href="/income-tax-filing">Services</a><a href="/pricing">Pricing</a><a href="/blogs">Blog</a><a href="/contact">Contact</a><a href="https://wa.me/923284675162" target="_blank" style="color:#25D366"><i class="fab fa-whatsapp" style="margin-right:8px"></i>WhatsApp</a></div>`;

const SIDEBAR = `<aside><div class="consult-card"><h4>Free Consultation</h4><p>Expert reply within 30 minutes</p><a href="https://wa.me/923284675162?text=I+need+tax+help+in+Lahore" class="wa-btn"><i class="fab fa-whatsapp"></i> WhatsApp Now</a></div><div class="sidebar-card"><h4>Our Services</h4><ul class="service-list"><li><i class="fas fa-file-invoice-dollar"></i><a href="/income-tax-filing" style="color:#0D9488"> Income Tax Return</a></li><li><i class="fas fa-id-card"></i><a href="/ntn-registration" style="color:#0D9488"> NTN Registration</a></li><li><i class="fas fa-building"></i><a href="/secp-vs-sole-proprietorship-pakistan" style="color:#0D9488"> Company Registration</a></li><li><i class="fas fa-percent"></i><a href="/sales-tax-registration" style="color:#0D9488"> Sales Tax (STRN)</a></li><li><i class="fas fa-shield-halved"></i><a href="/fbr-notice-defense" style="color:#0D9488"> FBR Notice Defense</a></li><li><i class="fas fa-wallet"></i><a href="/wealth-statement" style="color:#0D9488"> Wealth Statement</a></li></ul></div><div class="sidebar-card"><div class="price-badge"><div class="from">Starting From</div><div class="amount">Rs. 3,500</div><div class="from">Income Tax Return</div></div><a href="/pricing" style="display:block;text-align:center;color:#14B8A6;font-size:.85rem;font-weight:600;margin-top:8px"><i class="fas fa-tags"></i> View All Pricing</a></div><div class="sidebar-card" style="background:#FFF7ED;border-color:#FED7AA"><h4 style="color:#9A3412">📍 Our Office</h4><p style="font-size:.82rem;color:#7C3306;line-height:1.6">Allama Iqbal Town<br>Opp. Shell Pump<br>Main Boulevard, Lahore</p><a href="tel:03284675162" style="display:block;margin-top:10px;color:#0D9488;font-weight:600;font-size:.85rem"><i class="fas fa-phone"></i> 0328-4675162</a></div></aside>`;

const FOOTER = `<a href="https://wa.me/923284675162" target="_blank" aria-label="WhatsApp" style="position:fixed;bottom:24px;right:24px;z-index:9999;display:flex;align-items:center;justify-content:center;width:58px;height:58px;background:#25D366;border-radius:50%;box-shadow:0 4px 16px rgba(37,211,102,0.5)"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="30" height="30" fill="#fff"><path d="M16 0C7.163 0 0 7.163 0 16c0 2.822.736 5.476 2.027 7.785L0 32l8.469-2.001A15.93 15.93 0 0016 32c8.837 0 16-7.163 16-16S24.837 0 16 0zm0 29.333a13.27 13.27 0 01-6.77-1.855l-.485-.288-5.024 1.188 1.228-4.893-.317-.502A13.267 13.267 0 012.667 16C2.667 8.636 8.636 2.667 16 2.667S29.333 8.636 29.333 16 23.364 29.333 16 29.333zm7.27-9.862c-.398-.199-2.354-1.162-2.72-1.294-.365-.133-.631-.199-.897.199-.265.398-1.029 1.294-1.261 1.56-.232.265-.465.299-.863.1-.398-.199-1.681-.619-3.202-1.977-1.183-1.057-1.981-2.362-2.213-2.76-.232-.398-.025-.613.175-.811.179-.179.398-.465.597-.698.199-.232.265-.398.398-.664.133-.265.066-.498-.033-.697-.1-.199-.897-2.163-1.229-2.96-.324-.777-.653-.672-.897-.684l-.764-.013c-.265 0-.697.1-1.062.498-.365.398-1.394 1.362-1.394 3.322s1.428 3.853 1.627 4.119c.199.265 2.808 4.287 6.804 6.014.951.411 1.693.656 2.271.84.954.304 1.823.261 2.509.158.765-.114 2.354-.962 2.686-1.891.333-.929.333-1.726.233-1.891-.1-.165-.365-.265-.764-.464z"/></svg></a>
<footer style="background:#0F172A;border-top:1px solid rgba(255,255,255,.06);padding:28px 0;text-align:center"><p style="font-size:.82rem;color:#64748B">&#169; 2026 Kamboh Associates — Tax Consultant Lahore &nbsp;|&nbsp;<a href="/contact" style="color:#14B8A6">Contact</a> &nbsp;|&nbsp;<a href="/pricing" style="color:#14B8A6">Pricing</a> &nbsp;|&nbsp;<a href="/blogs" style="color:#14B8A6">Blog</a></p></footer>
<script>document.querySelectorAll('.faq-q').forEach(q=>q.addEventListener('click',()=>q.parentElement.classList.toggle('open')))</script>`;

function generatePage({ slug, area, city }) {
  const areaLabel = `${area}, ${city}`;
  const canonical = `https://kambohassociates.com/blogs/${slug}`;
  const waMsg = encodeURIComponent(`I need a tax consultant in ${area}, Lahore. Please help.`);
  const schema = JSON.stringify({"@context":"https://schema.org","@type":"BlogPosting","headline":`Best Tax Consultant in ${areaLabel} 2026 — FBR Filing, NTN Registration`,"datePublished":"2026-06-23","dateModified":"2026-06-23","author":{"@type":"Organization","name":"Kamboh Associates","url":"https://kambohassociates.com"},"publisher":{"@type":"Organization","name":"Kamboh Associates","url":"https://kambohassociates.com","logo":{"@type":"ImageObject","url":"https://kambohassociates.com/logo.png"}},"mainEntityOfPage":{"@type":"WebPage","@id":canonical}});
  const faqSchema = JSON.stringify({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":`Who is the best tax consultant in ${areaLabel}?`,"acceptedAnswer":{"@type":"Answer","text":`Kamboh Associates — FBR-registered tax consultancy based in Lahore (Allama Iqbal Town, Opp. Shell Pump, Main Boulevard). We serve clients in ${areaLabel} 100% online via WhatsApp 0328-4675162. Income tax filing, NTN, company registration, FBR notice defense.`}},{"@type":"Question","name":`Is there a tax consultant near me in ${area} Lahore?`,"acceptedAnswer":{"@type":"Answer","text":`Yes — Kamboh Associates serves ${areaLabel} clients online. WhatsApp documents to 0328-4675162, return filed same day. No office visit needed.`}},{"@type":"Question","name":`What is the fee for income tax return in ${area} Lahore?`,"acceptedAnswer":{"@type":"Answer","text":`Income tax return filing starts from Rs. 3,500 for salaried individuals. Business/freelancer returns from Rs. 5,000. Full pricing at kambohassociates.com/pricing.`}}]});

  return `<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Best Tax Consultant in ${areaLabel} 2026 — FBR Filing, NTN &amp; Company Registration</title>
<meta name="description" content="Tax consultant in ${areaLabel}? Kamboh Associates — FBR registered, 18+ years experience. Income tax return from Rs. 3,500. NTN same day. 100% online. WhatsApp 0328-4675162."/>
<meta name="keywords" content="tax consultant ${area.toLowerCase()} Lahore, best tax consultant ${area.toLowerCase()}, tax consultant near me ${area.toLowerCase()}, FBR filing ${area.toLowerCase()} Lahore, NTN registration ${area.toLowerCase()} Lahore, income tax return ${area.toLowerCase()}"/>
<link rel="canonical" href="${canonical}"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700&family=DM+Sans:wght@400;500;600&family=Cinzel:wght@600;700&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
${SHARED_STYLE}
<script type="application/ld+json">${schema}</script>
<script type="application/ld+json">${faqSchema}</script>
<meta property="og:type" content="article"/><meta property="og:locale" content="en_PK"/>
<meta property="og:title" content="Best Tax Consultant in ${areaLabel} 2026 — Kamboh Associates"/>
<meta property="og:description" content="Tax return, NTN registration, company registration in ${areaLabel}. FBR registered. Rs. 3,500 starting fee. WhatsApp 0328-4675162."/>
<meta property="og:url" content="${canonical}"/>
</head><body>
${NAV}
<section class="blog-hero"><div class="container">
<nav class="breadcrumb"><a href="/"><i class="fas fa-home"></i> Home</a><i class="fas fa-chevron-right"></i><a href="/blogs">Blog</a><i class="fas fa-chevron-right"></i><a href="/blogs/tax-consultant-lahore">Tax Consultant Lahore</a><i class="fas fa-chevron-right"></i><span>${area}</span></nav>
<div class="blog-cat"><i class="fas fa-map-marker-alt"></i> Lahore — Local Tax Guide</div>
<h1>Best Tax Consultant in ${areaLabel} — Income Tax, NTN &amp; FBR Filing 2026</h1>
<div class="blog-meta"><span><i class="fas fa-calendar"></i> June 2026</span><span><i class="fas fa-user"></i> Kamboh Associates</span><span><i class="fas fa-map-marker-alt"></i> ${area}, Lahore</span><span><i class="fas fa-clock"></i> 6 min read</span></div>
</div></section>

<div class="blog-layout container"><article class="article-body">
<p class="article-lead">Looking for a professional tax consultant in <strong>${areaLabel}</strong>? Kamboh Associates is Lahore's trusted FBR-registered tax consultancy with 18+ years of experience. Based at Allama Iqbal Town, Main Boulevard Lahore — we serve clients across <strong>${area}</strong> and all of Lahore completely online via WhatsApp. Income tax return filing, NTN registration, company registration, or FBR notice response — all done same day from your home.</p>

<h2>Tax Services Available in ${areaLabel}</h2>
<table>
<tr><th>Service</th><th>Starting Fee</th><th>Delivery</th></tr>
<tr><td>Salaried Individual Tax Return</td><td>Rs. 3,500</td><td>Same day</td></tr>
<tr><td>Business / Freelancer Tax Return</td><td>Rs. 5,000</td><td>1–2 days</td></tr>
<tr><td>NTN Registration</td><td>Rs. 2,000</td><td>Same day</td></tr>
<tr><td>Sales Tax Registration (STRN)</td><td>Rs. 3,000</td><td>2–3 days</td></tr>
<tr><td>Company Registration (SECP Pvt Ltd)</td><td>Rs. 15,000</td><td>7–10 days</td></tr>
<tr><td>FBR Notice Response</td><td>Rs. 5,000</td><td>1–3 days</td></tr>
<tr><td>Wealth Statement</td><td>Rs. 2,500</td><td>Same day</td></tr>
<tr><td>AOP / Partnership Return</td><td>Rs. 8,000</td><td>2–3 days</td></tr>
</table>

<h2>Why ${area} Residents Choose Kamboh Associates</h2>
<ul>
<li><strong>FBR Registered</strong> — authorized to file income tax returns on your behalf on IRIS portal</li>
<li><strong>18+ Years in Lahore</strong> — serving Punjab clients since 2008 from Allama Iqbal Town office</li>
<li><strong>5,000+ Lahore Returns Filed</strong> — salaried workers, businesses, freelancers, landlords</li>
<li><strong>Same-Day Salaried Filing</strong> — receive FBR acknowledgment receipt the same day you send documents</li>
<li><strong>100% Online via WhatsApp</strong> — no need to visit any office; share documents digitally</li>
<li><strong>Fixed Transparent Fees</strong> — no hidden charges, fee confirmed before work begins</li>
</ul>
<div class="highlight-box"><p><strong>Simple 3-step process from ${area}:</strong> 1️⃣ WhatsApp your CNIC + documents to <strong>0328-4675162</strong> → 2️⃣ We verify and file on FBR IRIS portal → 3️⃣ You receive the official FBR receipt on WhatsApp — same day.</p></div>

<h2>Documents Required for Tax Filing from ${area}, Lahore</h2>
<table>
<tr><th>Your Situation</th><th>Documents Needed</th></tr>
<tr><td>Salaried employee</td><td>Annual salary certificate from employer + CNIC copy</td></tr>
<tr><td>Freelancer / IT exporter</td><td>Bank statement (Wise/Payoneer/local bank) + CNIC</td></tr>
<tr><td>Business owner / shopkeeper</td><td>Revenue & expense summary or business bank statement</td></tr>
<tr><td>Property owner / landlord</td><td>Property documents + rent agreement + bank statement</td></tr>
<tr><td>All taxpayers</td><td>List of all assets (property, vehicles, savings) + any loans</td></tr>
</table>

<h2>FBR Notices — Immediate Help for ${area} Residents</h2>
<p>FBR sends notices to Lahore taxpayers for unexplained income, property transactions, and large bank deposits. Do not ignore any FBR notice — respond before the deadline shown on the notice. Common notices received by Lahore residents:</p>
<ul>
<li><strong>Section 111:</strong> Unexplained income or wealth — very common in Lahore</li>
<li><strong>Section 122:</strong> Amendment to tax assessment</li>
<li><strong>Section 176:</strong> Request for information or records</li>
<li><strong>Section 114:</strong> Notice to file income tax return</li>
</ul>
<div class="highlight-box"><p>Got an FBR notice? WhatsApp a clear photo to <strong>0328-4675162</strong> right now. Free initial review — we advise you on exactly what to do within 30 minutes, no charge for the assessment.</p></div>

<h2>Frequently Asked Questions — Tax Consultant in ${area}, Lahore</h2>
<div class="faq-list">
<div class="faq-item"><div class="faq-q">Who is the best tax consultant in ${areaLabel}? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Kamboh Associates — based at Allama Iqbal Town, Main Boulevard Lahore — is one of Lahore's most trusted FBR-registered tax consultancies. With 18+ years of experience and 5,000+ clients, we serve ${area} and all Lahore areas 100% online. WhatsApp: 0328-4675162.</div></div>
<div class="faq-item"><div class="faq-q">Is there a tax consultant near ${area} in Lahore? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Yes — Kamboh Associates serves the entire Lahore including ${area} online. No office visit required. WhatsApp your documents to 0328-4675162 and your tax return is filed and receipted the same day.</div></div>
<div class="faq-item"><div class="faq-q">How much does income tax filing cost in ${area}, Lahore? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Salaried individual returns start from Rs. 3,500. Business/freelancer returns from Rs. 5,000. NTN registration Rs. 2,000. All fees are fixed and confirmed upfront before work begins. Full fee list: kambohassociates.com/pricing.</div></div>
<div class="faq-item"><div class="faq-q">Can I file my tax return without visiting your office? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Absolutely. Our entire process is 100% online. WhatsApp your documents from ${area} Lahore, we file on FBR IRIS portal, and you receive the official FBR acknowledgment receipt on WhatsApp — all same day. No office visit ever needed.</div></div>
</div>

<div style="background:linear-gradient(135deg,#0F172A,#1E3A5F);border-radius:16px;padding:28px 32px;margin-top:32px;text-align:center">
<h3 style="font-family:'Cormorant Garamond',serif;color:#fff;font-size:1.4rem;margin-bottom:8px">Tax Consultant ${area}, Lahore — Get Started</h3>
<p style="color:#94A3B8;font-size:.9rem;margin-bottom:18px">WhatsApp documents → Filed same day → FBR receipt on WhatsApp. 18+ years trusted service.</p>
<a href="https://wa.me/923284675162?text=${waMsg}" style="display:inline-flex;align-items:center;gap:8px;background:#25D366;color:#fff;padding:12px 28px;border-radius:100px;font-weight:600;font-size:.92rem"><i class="fab fa-whatsapp"></i> WhatsApp 0328-4675162</a>
</div>
</article>
${SIDEBAR}
</div>
${FOOTER}
</body></html>`;
}

// ── STEP 1: Create new HTML pages ─────────────────────────────────────────────
let htmlCreated = 0;
const createdSlugs = [];
for (const loc of NEW_LAHORE) {
  const fp = path.join(BLOGS_DIR, `${loc.slug}.html`);
  if (fs.existsSync(fp)) { process.stdout.write('.'); continue; }
  fs.writeFileSync(fp, generatePage(loc), 'utf8');
  createdSlugs.push(loc.slug);
  htmlCreated++;
}
console.log(`\n✅ Created ${htmlCreated} new HTML pages`);

// ── STEP 2: Build JS entries for missing pages ────────────────────────────────
let blogsContent = fs.readFileSync(path.join(__dirname, 'blogs.html'), 'utf8');
const existingIds = new Set([...blogsContent.matchAll(/id:"([^"]+)"/g)].map(m => m[1]));

// All Lahore HTML files
const lahoreFiles = fs.readdirSync(BLOGS_DIR).filter(f => f.includes('lahore') && f.endsWith('.html'));

const newJsEntries = [];

function slugToTitle(slug) {
  return slug
    .replace(/-lahore$/, '')
    .replace(/-/g, ' ')
    .replace(/\b\w/g, c => c.toUpperCase());
}

function slugToArea(slug) {
  return slug
    .replace(/^tax-consultant-/, '')
    .replace(/-lahore$/, '')
    .replace(/-/g, ' ')
    .replace(/\b\w/g, c => c.toUpperCase());
}

// Add missing existing Lahore pages
for (const f of lahoreFiles) {
  const id = f.replace('.html', '');
  if (existingIds.has(id)) continue;
  const area = slugToArea(id);
  const title = `Best Tax Consultant in ${area} Lahore 2026 — FBR Filing, NTN Registration`;
  const excerpt = `Expert tax consultant serving ${area} Lahore. Income tax filing, NTN registration, FBR notices. FBR registered, 18+ years. Rs. 3,500 starting fee. WhatsApp 0328-4675162.`;
  newJsEntries.push(`  { id:"${id}", title:"${title}", excerpt:"${excerpt}", date:"2026-06-23", category:"Lahore Local", readTime:"6 min read", author:"Kamboh Associates", icon:"📍", link:"/blogs/${id}" }`);
}

console.log(`✅ Built ${newJsEntries.length} new JS entries`);

// ── STEP 3: Insert JS entries into blogs.html ─────────────────────────────────
if (newJsEntries.length > 0) {
  // Find the end of the JS array — find last entry and insert before closing ];
  const insertMarker = '  { id:"fbr-consultant-near-me-lahore"';
  const insertPos = blogsContent.indexOf(insertMarker);
  if (insertPos !== -1) {
    blogsContent = blogsContent.slice(0, insertPos) + newJsEntries.join(',\n') + ',\n' + blogsContent.slice(insertPos);
    console.log(`✅ Inserted ${newJsEntries.length} JS entries`);
  } else {
    // fallback: insert before const posts = [
    console.log('Marker not found, trying fallback...');
    const fallbackMarker = '  { id:"tax-consultant-johar-town-lahore"';
    const fpos = blogsContent.indexOf(fallbackMarker);
    if (fpos !== -1) {
      blogsContent = blogsContent.slice(0, fpos) + newJsEntries.join(',\n') + ',\n' + blogsContent.slice(fpos);
      console.log(`✅ Inserted via fallback marker`);
    }
  }
}

// ── STEP 4: Update stat counts ────────────────────────────────────────────────
const totalBlogFiles = fs.readdirSync(BLOGS_DIR).filter(f => f.endsWith('.html')).length;
const nonBlogPages = 10; // approx service pages in blogs dir
const totalArticles = totalBlogFiles;

// Count Lahore Local entries in updated content
const lahoreCount = (blogsContent.match(/category:"Lahore Local"/g) || []).length;
const pakLocalCount = (blogsContent.match(/category:"Pakistan Local"/g) || []).length;
const totalJsEntries = (blogsContent.match(/{ id:"/g) || []).length;

// Update hero stats
blogsContent = blogsContent.replace(
  '<div class="bhs-n">1000</div><div class="bhs-l">Articles</div>',
  `<div class="bhs-n">${totalArticles}+</div><div class="bhs-l">Articles</div>`
);

// Update sidebar category counts
blogsContent = blogsContent.replace(
  'All Articles <span class="cat-count">1000</span>',
  `All Articles <span class="cat-count">${totalJsEntries}</span>`
);
blogsContent = blogsContent.replace(
  'Lahore Local <span class="cat-count">29</span>',
  `Lahore Local <span class="cat-count">${lahoreCount}</span>`
);
blogsContent = blogsContent.replace(
  'All Cities <span class="cat-count">29</span>',
  `All Cities <span class="cat-count">${pakLocalCount}</span>`
);

fs.writeFileSync(path.join(__dirname, 'blogs.html'), blogsContent, 'utf8');

// ── STEP 5: Add static links to blogs.html for new HTML pages ────────────────
const finalContent = fs.readFileSync(path.join(__dirname, 'blogs.html'), 'utf8');
const staticLinks = createdSlugs.filter(s => !finalContent.includes(`href="/blogs/${s}"`));
if (staticLinks.length > 0) {
  let c2 = finalContent;
  const linkHtml = staticLinks.map(s => {
    const area = slugToArea(s);
    return `      <a href="/blogs/${s}" style="display:block;padding:8px 0;font-size:.83rem;color:#334155;border-bottom:1px solid #E2E8F0;transition:color .15s" onmouseover="this.style.color='#14B8A6'" onmouseout="this.style.color='#334155'">Tax Consultant ${area}, Lahore</a>`;
  }).join('\n');
  c2 = c2.replace('      <a href="/blogs/income-tax-slab-pakistan-2026"', linkHtml + '\n      <a href="/blogs/income-tax-slab-pakistan-2026"');
  fs.writeFileSync(path.join(__dirname, 'blogs.html'), c2, 'utf8');
  console.log(`✅ Added ${staticLinks.length} static links`);
}

// Final report
const finalJs = (fs.readFileSync(path.join(__dirname, 'blogs.html'), 'utf8').match(/{ id:"/g) || []).length;
const finalLahore = (fs.readFileSync(path.join(__dirname, 'blogs.html'), 'utf8').match(/category:"Lahore Local"/g) || []).length;
console.log(`\n📊 FINAL STATS:`);
console.log(`   Total HTML files: ${fs.readdirSync(BLOGS_DIR).filter(f=>f.endsWith('.html')).length}`);
console.log(`   JS array entries: ${finalJs}`);
console.log(`   Lahore Local in JS: ${finalLahore}`);
