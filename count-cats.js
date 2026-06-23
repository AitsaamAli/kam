const fs = require('fs');
const html = fs.readFileSync('blogs.html','utf8');
const re = /category:"([^"]+)"/g;
const counts = {};
let m;
while ((m = re.exec(html)) !== null) {
  const cat = m[1];
  counts[cat] = (counts[cat] || 0) + 1;
}
const sorted = Object.entries(counts).sort(function(a,b){ return b[1]-a[1]; });
let total = 0;
sorted.forEach(function(e){ total += e[1]; });
console.log('Total blogs:', total);
sorted.forEach(function(e){ console.log(String(e[1]).padStart(4), e[0]); });
