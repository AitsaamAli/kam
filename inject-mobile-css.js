const fs = require('fs');
const path = require('path');

const LINK_TAG = '<link rel="stylesheet" href="/mobile-fixes.css">';
const MARKER = '</head>';
let total = 0, injected = 0, skipped = 0;

function processFile(filePath) {
  let html = fs.readFileSync(filePath, 'utf8');
  if (html.includes(LINK_TAG)) { skipped++; return; }
  const idx = html.lastIndexOf(MARKER);
  if (idx === -1) { console.log('NO </head>: ' + filePath); return; }
  html = html.slice(0, idx) + LINK_TAG + '\n' + html.slice(idx);
  fs.writeFileSync(filePath, html, 'utf8');
  injected++;
}

// Root HTML files
const rootFiles = fs.readdirSync('.').filter(f => f.endsWith('.html'));
rootFiles.forEach(f => { processFile(f); total++; });

// Blog HTML files
const blogsDir = path.join('.', 'blogs');
if (fs.existsSync(blogsDir)) {
  const blogFiles = fs.readdirSync(blogsDir).filter(f => f.endsWith('.html'));
  blogFiles.forEach(f => { processFile(path.join(blogsDir, f)); total++; });
}

console.log('Total files: ' + total);
console.log('Injected:    ' + injected);
console.log('Skipped (already had tag): ' + skipped);
