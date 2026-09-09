#!/usr/bin/env node
/**
 * wire-snippets.js — batch ke liye blogs.html + sitemap.xml wiring snippets print karta hai.
 *
 * Usage: node wire-snippets.js batch-C1.js
 *
 * Yaad rahe: blogs.html mein DO alag mechanism hain aur dono update karne parte hain —
 *   (1) JS blogPosts array
 *   (2) neeche wali static, slug ke lehaaz se ALPHABETICAL <a href> list
 * Static list mein entry alphabetical jagah par insert karni hai, aakhir mein append NAHI karni.
 */
const path = require('path');

const files = process.argv.slice(2);
if (!files.length) { console.error('Usage: node wire-snippets.js batch-C1.js'); process.exit(2); }

let posts = [];
files.forEach(f => {
  const batch = require(path.resolve(f));
  (Array.isArray(batch) ? batch : [batch]).forEach(p => posts.push(p));
});

let startId = Number(process.env.START_ID || 0);

console.log('\n/* ============ 1) blogs.html — JS blogPosts array entries ============ */\n');
posts.forEach((p, i) => {
  console.log(`  {
    id: ${startId ? startId + i : 'NEXT_ID'},
    featured: false,
    link: "/blogs/${p.slug}",
    title: ${JSON.stringify(p.title)},
    excerpt: ${JSON.stringify(p.description)},
    date: ${JSON.stringify(p.datePublished)},
    category: "Income Tax",
    readTime: ${JSON.stringify(p.readTime)},
    author: "Aitsaam Ali",
    icon: "fa-file-invoice-dollar"
  },`);
});

console.log('\n/* ==== 2) blogs.html — static list anchors (ALPHABETICAL jagah par insert karein) ==== */\n');
[...posts].sort((a, b) => a.slug.localeCompare(b.slug)).forEach(p => {
  console.log(`<a href="/blogs/${p.slug}">${p.title}</a>`);
});

console.log('\n<!-- ============ 3) sitemap.xml — <url> blocks ============ -->\n');
posts.forEach(p => {
  console.log(`  <url>
    <loc>https://kambohassociates.com/blogs/${p.slug}</loc>
    <lastmod>${p.dateModified}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>`);
});

console.log('\n/* ============ 4) Internal links jo in posts se bahar ki taraf jate hain ============ */');
console.log('/* Inhein site-health-check.js se verify karein — target file ka apna canonical dekhein,');
console.log('   kyunke kuch pages site ROOT par hain, /blogs/ ke neeche nahi. */\n');
const outbound = new Set();
posts.forEach(p => {
  (p.related || []).forEach(r => outbound.add(r.href));
  if (p.ctaSecondaryHref) outbound.add(p.ctaSecondaryHref);
});
const internalSlugs = new Set(posts.map(p => '/blogs/' + p.slug));
[...outbound].sort().forEach(h => {
  console.log(`${internalSlugs.has(h) ? '[in-batch] ' : '[verify]   '}${h}`);
});
console.log('');
