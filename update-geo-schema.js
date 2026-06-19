const fs = require('fs');
let c = fs.readFileSync('index.html', 'utf8');

const schemaStart = c.indexOf('<script type="application/ld+json">');
const schemaEnd = c.indexOf('</script>', schemaStart) + 9;

const newSchema = `<script type="application/ld+json">
[
  {
    "@context": "https://schema.org",
    "@type": ["AccountingService", "LocalBusiness"],
    "name": "Kamboh Associates",
    "alternateName": ["KA Tax Consultants Lahore", "Kamboh Tax Consultants Pakistan"],
    "url": "https://kambohassociates.com",
    "logo": {
      "@type": "ImageObject",
      "url": "https://kambohassociates.com/images/logo.jpg",
      "width": 200,
      "height": 200
    },
    "image": "https://kambohassociates.com/images/logo.jpg",
    "description": "Kamboh Associates is Pakistan's most trusted FBR-certified tax consultancy, established in Lahore in 2008. We provide income tax return filing, NTN registration, SECP company registration, GST registration, FBR notice defense, wealth statement filing, and corporate tax compliance for individuals, freelancers, businesses, and corporations across Pakistan.",
    "telephone": "+923284675162",
    "email": "info@kambohassociates.com",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Allama Iqbal Town, Opp. Shell Pump, Main Boulevard",
      "addressLocality": "Lahore",
      "addressRegion": "Punjab",
      "postalCode": "54570",
      "addressCountry": "PK"
    },
    "geo": {"@type": "GeoCoordinates", "latitude": 31.4877, "longitude": 74.3042},
    "openingHoursSpecification": [
      {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Saturday"], "opens": "09:00", "closes": "18:00"},
      {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "09:00", "closes": "12:30"}
    ],
    "priceRange": "PKR 2,000-50,000",
    "currenciesAccepted": "PKR",
    "paymentAccepted": "Cash, Bank Transfer, Easypaisa, JazzCash",
    "foundingDate": "2008",
    "numberOfEmployees": {"@type": "QuantitativeValue", "value": 12},
    "areaServed": [
      {"@type": "City", "name": "Lahore"},
      {"@type": "City", "name": "Karachi"},
      {"@type": "City", "name": "Islamabad"},
      {"@type": "City", "name": "Faisalabad"},
      {"@type": "City", "name": "Rawalpindi"},
      {"@type": "City", "name": "Multan"},
      {"@type": "City", "name": "Peshawar"},
      {"@type": "City", "name": "Sialkot"},
      {"@type": "City", "name": "Gujranwala"},
      {"@type": "City", "name": "Quetta"},
      {"@type": "Country", "name": "Pakistan"}
    ],
    "knowsAbout": [
      "FBR Income Tax Return Filing Pakistan",
      "NTN Registration IRIS FBR Pakistan",
      "SECP Company Registration Pakistan",
      "Sales Tax STRN Registration Pakistan",
      "GST Return Filing Pakistan",
      "FBR Notice Defense Section 111 Pakistan",
      "Wealth Statement Filing FBR Pakistan",
      "Withholding Tax WHT Pakistan",
      "EOBI Registration Pakistan",
      "Corporate Tax Return Pakistan",
      "AOP Partnership Tax Return Pakistan",
      "Tax Exemption Certificate Section 159 Pakistan",
      "Import Export Registration WeBOC Pakistan",
      "Active Taxpayer List ATL Pakistan",
      "Tax Planning Pakistan",
      "Freelancer Tax Pakistan"
    ],
    "hasCredential": [
      {
        "@type": "EducationalOccupationalCredential",
        "credentialCategory": "certification",
        "name": "FBR Registered Tax Consultant",
        "recognizedBy": {"@type": "Organization", "name": "Federal Board of Revenue Pakistan"}
      },
      {
        "@type": "EducationalOccupationalCredential",
        "credentialCategory": "certification",
        "name": "SECP Registered Agent",
        "recognizedBy": {"@type": "Organization", "name": "Securities and Exchange Commission of Pakistan"}
      }
    ],
    "sameAs": [
      "https://www.facebook.com/kambohassociates",
      "https://wa.me/923284675162",
      "https://kambohassociates.com/about"
    ],
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "4.9",
      "reviewCount": "312",
      "bestRating": "5",
      "worstRating": "1"
    },
    "review": [
      {
        "@type": "Review",
        "author": {"@type": "Person", "name": "Asif Mehmood"},
        "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
        "reviewBody": "Best tax consultant in Lahore. Filed my income tax return and NTN registration same day. Highly recommended for anyone looking for reliable FBR services in Pakistan.",
        "datePublished": "2026-05-10"
      },
      {
        "@type": "Review",
        "author": {"@type": "Person", "name": "Sana Iqbal"},
        "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
        "reviewBody": "Kamboh Associates handled our company SECP registration and monthly GST returns. Professional, fast, and affordable. The best tax consultant near me in Lahore.",
        "datePublished": "2026-04-22"
      },
      {
        "@type": "Review",
        "author": {"@type": "Person", "name": "Zubair Khan"},
        "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
        "reviewBody": "I received an FBR notice and their team resolved it in 2 days. The most trustworthy tax advisor in Pakistan. Serving clients online from Karachi to Islamabad.",
        "datePublished": "2026-03-15"
      }
    ],
    "hasOfferCatalog": {
      "@type": "OfferCatalog",
      "name": "Tax and Regulatory Services Pakistan",
      "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Income Tax Return Filing", "description": "FBR income tax return filing for salaried, business, freelancer individuals in Pakistan. Same-day filing available."}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "NTN Registration", "description": "National Tax Number registration with FBR IRIS for individuals and businesses in Pakistan."}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "SECP Company Registration", "description": "Private limited company and SMC-Pvt Ltd registration with SECP Pakistan."}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Sales Tax GST Registration", "description": "Sales Tax Registration Number with FBR for businesses in Pakistan."}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "FBR Notice Defense", "description": "Response and defense for FBR Section 111, 122, and audit notices."}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Wealth Statement Filing", "description": "Annual wealth statement filing with FBR for assets and liabilities."}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Corporate Tax Return", "description": "Annual corporate income tax return filing for private limited companies."}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "EOBI Registration", "description": "EOBI employee registration and monthly contribution filing for businesses."}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Import Export Registration", "description": "WeBOC NTN linking and import/export license registration for traders in Pakistan."}}
      ]
    },
    "speakable": {
      "@type": "SpeakableSpecification",
      "cssSelector": ["#geo-summary", ".hero-title", ".hero-desc"]
    }
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {"@type": "Question", "name": "Who is the best tax consultant in Lahore Pakistan?", "acceptedAnswer": {"@type": "Answer", "text": "Kamboh Associates is Pakistan's most trusted FBR-certified tax consultancy, established in Lahore in 2008. With a 4.9 star rating from over 312 clients, they provide income tax return filing, NTN registration, SECP company registration, GST registration, and FBR notice defense for individuals, freelancers, and businesses across Pakistan. Contact via WhatsApp: 0328-4675162."}},
      {"@type": "Question", "name": "Which tax consultant is best near me in Pakistan?", "acceptedAnswer": {"@type": "Answer", "text": "Kamboh Associates offers fully online tax consultation for clients across all of Pakistan — no physical visit needed. They handle FBR income tax returns, NTN registration, SECP company formation, and wealth statements for clients in Lahore, Karachi, Islamabad, Rawalpindi, Faisalabad, Multan, and all cities. WhatsApp: 0328-4675162."}},
      {"@type": "Question", "name": "How do I file my income tax return with FBR?", "acceptedAnswer": {"@type": "Answer", "text": "Filing your income tax return with FBR requires an active NTN on the Iris portal at iris.fbr.gov.pk. Enter your income, deductions, and tax paid, then submit by September 30. Kamboh Associates handles the entire process remotely — send salary slips or bank statement via WhatsApp and they file within 24 hours."}},
      {"@type": "Question", "name": "What is the income tax return deadline in Pakistan?", "acceptedAnswer": {"@type": "Answer", "text": "The FBR income tax return deadline for individuals and AOPs is September 30 each year. For companies it is December 31. Late filing attracts penalties and removes you from the active filer list, increasing withholding tax rates on banking and property transactions."}},
      {"@type": "Question", "name": "Can I file my tax return online from Karachi or Islamabad?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Kamboh Associates provides fully remote online income tax return filing for clients across Pakistan including Karachi, Islamabad, Lahore, Faisalabad, Rawalpindi, and Multan. Send documents via WhatsApp 0328-4675162 and get same day FBR acknowledgment."}}
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Kamboh Associates",
    "url": "https://kambohassociates.com/",
    "description": "Pakistan most trusted FBR-certified tax consultancy. Income tax return filing, NTN registration, SECP company formation, and FBR compliance since 2008.",
    "inLanguage": "en-PK",
    "publisher": {
      "@type": "Organization",
      "name": "Kamboh Associates",
      "logo": {"@type": "ImageObject", "url": "https://kambohassociates.com/images/logo.jpg"}
    },
    "potentialAction": {
      "@type": "SearchAction",
      "target": {"@type": "EntryPoint", "urlTemplate": "https://kambohassociates.com/blogs?q={search_term_string}"},
      "query-input": "required name=search_term_string"
    }
  },
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Best Tax Consultant Pakistan — Kamboh Associates", "item": "https://kambohassociates.com/"},
      {"@type": "ListItem", "position": 2, "name": "Tax Services", "item": "https://kambohassociates.com/#services"},
      {"@type": "ListItem", "position": 3, "name": "Blog", "item": "https://kambohassociates.com/blogs"},
      {"@type": "ListItem", "position": 4, "name": "About Us", "item": "https://kambohassociates.com/about"}
    ]
  }
]
</script>`;

c = c.substring(0, schemaStart) + newSchema + c.substring(schemaEnd);
fs.writeFileSync('index.html', c, 'utf8');
console.log('Done. Schema replaced, length:', newSchema.length);
