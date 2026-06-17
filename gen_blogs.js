const fs = require("fs");
const template = fs.readFileSync("blogs/tax-consultant-askari-lahore.html","utf8");
const areas = [
  ["johar-town-lahore-area","Johar Town","Lahore","2026-11-07"],
  ["shadman-lahore-area","Shadman","Lahore","2026-11-08"],
  ["cavalry-ground-lahore-area","Cavalry Ground","Lahore","2026-11-09"],
  ["dha-lahore-area","DHA","Lahore","2026-11-10"],
  ["gulshan-ravi-lahore-area","Gulshan Ravi","Lahore","2026-11-11"],
  ["samanabad-lahore-area","Samanabad","Lahore","2026-11-12"],
  ["shahdara-lahore","Shahdara","Lahore","2026-11-13"],
  ["kot-lakhpat-lahore","Kot Lakhpat","Lahore","2026-11-14"],
  ["raiwind-lahore","Raiwind","Lahore","2026-11-15"],
  ["harbanspura-lahore","Harbanspura","Lahore","2026-11-16"],
  ["mughalpura-lahore","Mughalpura","Lahore","2026-11-17"],
  ["ichra-lahore","Ichra","Lahore","2026-11-18"],
  ["mozang-lahore","Mozang","Lahore","2026-11-19"],
  ["garhi-shahu-lahore","Garhi Shahu","Lahore","2026-11-20"],
  ["baghbanpura-lahore","Baghbanpura","Lahore","2026-11-21"],
  ["nishtar-colony-lahore","Nishtar Colony","Lahore","2026-11-22"],
  ["krishan-nagar-lahore","Krishan Nagar","Lahore","2026-11-23"],
  ["sundar-lahore","Sundar","Lahore","2026-11-24"],
  ["manga-mandi-lahore","Manga Mandi","Lahore","2026-11-25"],
  ["shalamar-lahore","Shalamar","Lahore","2026-11-26"],
  ["gulshan-e-maymar-karachi","Gulshan-e-Maymar","Karachi","2026-11-27"],
  ["north-karachi-karachi","North Karachi","Karachi","2026-11-28"],
  ["scheme-33-karachi","Scheme 33","Karachi","2026-11-29"],
  ["gadap-town-karachi","Gadap Town","Karachi","2026-11-30"],
  ["manghopir-karachi","Manghopir","Karachi","2026-12-01"],
  ["shah-latif-town-karachi","Shah Latif Town","Karachi","2026-12-02"],
  ["scheme-45-karachi","Scheme 45","Karachi","2026-12-03"],
  ["dha-phase-2-karachi","DHA Phase 2","Karachi","2026-12-04"],
  ["dha-phase-6-karachi","DHA Phase 6","Karachi","2026-12-05"],
  ["bahria-precinct-karachi","Bahria Precinct","Karachi","2026-12-06"],
  ["malir-city-karachi","Malir City","Karachi","2026-12-07"],
  ["landhi-industrial-karachi","Landhi Industrial Area","Karachi","2026-12-08"],
  ["f-9-islamabad","F-9","Islamabad","2026-12-09"],
  ["g-14-islamabad","G-14","Islamabad","2026-12-10"],
  ["g-15-islamabad","G-15","Islamabad","2026-12-11"],
  ["h-9-islamabad","H-9","Islamabad","2026-12-12"],
  ["h-10-islamabad","H-10","Islamabad","2026-12-13"],
  ["d-12-islamabad","D-12","Islamabad","2026-12-14"],
  ["b-17-islamabad","B-17","Islamabad","2026-12-15"],
  ["satellite-town-rawalpindi","Satellite Town","Rawalpindi","2026-12-16"],
  ["chaklala-rawalpindi","Chaklala","Rawalpindi","2026-12-17"],
  ["westridge-rawalpindi","Westridge","Rawalpindi","2026-12-18"],
  ["bahria-town-rawalpindi","Bahria Town","Rawalpindi","2026-12-19"],
  ["wah-cantt-rawalpindi","Wah Cantt","Rawalpindi","2026-12-20"],
  ["taxila-rawalpindi","Taxila","Rawalpindi","2026-12-21"],
  ["gujrat-city","City Centre","Gujrat","2026-12-22"],
  ["sheikhupura-city","City Centre","Sheikhupura","2026-12-23"],
  ["jhang-city","City Centre","Jhang","2026-12-24"],
  ["okara-city","City Centre","Okara","2026-12-25"],
  ["kasur-city","City Centre","Kasur","2026-12-26"],
  ["narowal-city","City Centre","Narowal","2026-12-27"],
  ["hafizabad-city","City Centre","Hafizabad","2026-12-28"],
  ["chiniot-city","City Centre","Chiniot","2026-12-29"],
  ["khushab-city","City Centre","Khushab","2026-12-30"],
  ["mandi-bahauddin-city","City Centre","Mandi Bahauddin","2026-12-31"],
  ["attock-city","City Centre","Attock","2027-01-01"],
  ["chakwal-city","City Centre","Chakwal","2027-01-02"],
  ["jhelum-city","City Centre","Jhelum","2027-01-03"],
  ["khanewal-city","City Centre","Khanewal","2027-01-04"],
  ["pakpattan-city","City Centre","Pakpattan","2027-01-05"],
  ["vehari-city","City Centre","Vehari","2027-01-06"],
  ["lodhran-city","City Centre","Lodhran","2027-01-07"],
  ["toba-tek-singh-city","City Centre","Toba Tek Singh","2027-01-08"],
  ["layyah-city","City Centre","Layyah","2027-01-09"],
  ["bhakkar-city","City Centre","Bhakkar","2027-01-10"],
  ["muzaffargarh-city","City Centre","Muzaffargarh","2027-01-11"],
  ["rajanpur-city","City Centre","Rajanpur","2027-01-12"],
  ["dera-ghazi-khan-city","City Centre","Dera Ghazi Khan","2027-01-13"],
  ["swabi-city","City Centre","Swabi","2027-01-14"],
  ["nowshera-city","City Centre","Nowshera","2027-01-15"],
  ["kohat-city","City Centre","Kohat","2027-01-16"],
  ["bannu-city","City Centre","Bannu","2027-01-17"],
  ["dera-ismail-khan-city","City Centre","Dera Ismail Khan","2027-01-18"],
  ["mansehra-city","City Centre","Mansehra","2027-01-19"],
  ["haripur-city","City Centre","Haripur","2027-01-20"],
  ["mingora-swat","City Centre Mingora","Swat","2027-01-21"],
  ["charsadda-city","City Centre","Charsadda","2027-01-22"],
  ["karak-city","City Centre","Karak","2027-01-23"],
  ["hangu-city","City Centre","Hangu","2027-01-24"],
  ["chitral-city","City Centre","Chitral","2027-01-25"],
  ["tank-city","City Centre","Tank","2027-01-26"],
  ["lakki-marwat-city","City Centre","Lakki Marwat","2027-01-27"],
  ["mirpurkhas-city","City Centre","Mirpurkhas","2027-01-28"],
  ["tando-allahyar-city","City Centre","Tando Allahyar","2027-01-29"],
  ["tando-adam-city","City Centre","Tando Adam","2027-01-30"],
  ["sanghar-city","City Centre","Sanghar","2027-01-31"],
  ["badin-city","City Centre","Badin","2027-02-01"],
  ["thatta-city","City Centre","Thatta","2027-02-02"],
  ["dadu-city","City Centre","Dadu","2027-02-03"],
  ["jacobabad-city","City Centre","Jacobabad","2027-02-04"],
  ["shikarpur-city","City Centre","Shikarpur","2027-02-05"],
  ["khairpur-city","City Centre","Khairpur","2027-02-06"],
  ["umerkot-city","City Centre","Umerkot","2027-02-07"],
  ["ghotki-city","City Centre","Ghotki","2027-02-08"],
  ["matiari-city","City Centre","Matiari","2027-02-09"],
  ["turbat-city","City Centre","Turbat","2027-02-10"],
  ["khuzdar-city","City Centre","Khuzdar","2027-02-11"],
  ["hub-city","City Centre","Hub","2027-02-12"],
  ["chaman-city","City Centre","Chaman","2027-02-13"],
  ["zhob-city","City Centre","Zhob","2027-02-14"],
  ["gwadar-city","City Centre","Gwadar","2027-02-15"],
  ["sibi-city","City Centre","Sibi","2027-02-16"],
  ["loralai-city","City Centre","Loralai","2027-02-17"],
  ["kharan-city","City Centre","Kharan","2027-02-18"],
  ["rawalakot-city","City Centre","Rawalakot","2027-02-19"],
  ["kotli-city","City Centre","Kotli","2027-02-20"],
  ["bhimber-city","City Centre","Bhimber","2027-02-21"],
  ["gilgit-city","City Centre","Gilgit","2027-02-22"],
  ["skardu-city","City Centre","Skardu","2027-02-23"],
  ["hunza-city","City Centre","Hunza","2027-02-24"],
];

let blogEntries = "";
let sitemapEntries = "";
let created = 0;

areas.forEach(function(row) {
  var slug = row[0], short = row[1], city = row[2], date = row[3];
  var display = (short === "City Centre") ? city : (short + " " + city);
  var shortName = (short === "City Centre") ? city : short;

  var outPath = "blogs/tax-consultant-" + slug + ".html";
  if (fs.existsSync(outPath)) { console.log("SKIP: " + slug); return; }

  var out = template
    .replace(/tax-consultant-askari-lahore/g, slug)
    .replace(/Best Tax Consultant in Askari Lahore/g, "Best Tax Consultant in " + display)
    .replace(/Askari Lahore/g, display)
    .replace(/Askari, Lahore/g, shortName + ", " + city)
    .replace(/addressLocality":"Lahore"/g, "addressLocality\":\"" + city + "\"")
    .replace(/addressRegion":"Punjab"/g, "addressRegion\":\"Pakistan\"")
    .replace(/Lahore Local Tax Guide/g, city + " Local Tax Guide")
    .replace(/Why Askari Residents Need/g, "Why " + shortName + " Residents Need")
    .replace(/Key Insight for Askari Residents/g, "Key Insight for " + shortName + " Residents")
    .replace(/Our Services for Askari Clients/g, "Our Services for " + shortName + " Clients")
    .replace(/Benefits of Being a Filer in Askari/g, "Benefits of Being a Filer in " + shortName)
    .replace(/Get Expert Tax Help in Askari Today/g, "Get Expert Tax Help in " + shortName + " Today")
    .replace(/serves all Askari clients remotely/g, "serves all " + shortName + " clients remotely")
    .replace(/Tax Consultant in Askari/g, "Tax Consultant in " + shortName)
    .replace(/I\+need\+tax\+help\+in\+Askari\./g, "I+need+tax+help+in+" + display.replace(/ /g, "+") + ".")
    .replace(/Who needs to file income tax in Askari, Lahore/g, "Who needs to file income tax in " + shortName + ", " + city)
    .replace(/Any Askari resident/g, "Any " + shortName + " resident")
    .replace(/How much does tax filing cost in Askari/g, "How much does tax filing cost in " + shortName)
    .replace(/We serve all Askari clients/g, "We serve all " + shortName + " clients")
    .replace(/NTN registration for Askari clients/g, "NTN registration for " + shortName + " clients")
    .replace(/all Lahore areas remotely/g, "all " + city + " areas remotely")
    .replace(/all areas of Lahore, Pakistan/g, "all areas of " + city + ", Pakistan")
    .replace(/2026-07-07/g, date)
    .replace(/July 7, 2026/g, date);

  fs.writeFileSync(outPath, out);
  created++;

  var cat = "Other Cities";
  if (city === "Lahore") cat = "Lahore Local";
  else if (city === "Karachi") cat = "Karachi Local";
  else if (city === "Islamabad" || city === "Rawalpindi") cat = "Islamabad Local";

  blogEntries += "  { id:\"tax-consultant-" + slug + "\", title:\"Best Tax Consultant in " + display + " 2026\", excerpt:\"Top tax consultant in " + display + ". NTN registration, income tax filing, FBR compliance.\", date:\"" + date + "\", category:\"" + cat + "\", readTime:\"7 min read\", author:\"Kamboh Associates\", icon:\"📍\", link:\"/blogs/tax-consultant-" + slug + "\" },\n";

  sitemapEntries += "\n  <url>\n    <loc>https://kambohassociates.com/blogs/tax-consultant-" + slug + "</loc>\n    <lastmod>" + date + "</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n  </url>";
});

fs.writeFileSync("C:/tmp/blog_entries.txt", blogEntries);
fs.writeFileSync("C:/tmp/sitemap_entries.txt", sitemapEntries);
console.log("Created: " + created + " files");
