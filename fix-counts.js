const fs = require('fs');
let html = fs.readFileSync('blogs.html', 'utf8');

const fixes = [
  ['Karachi Local <span class="cat-count">74</span>', 'Karachi Local <span class="cat-count">86</span>'],
  ['Islamabad Local <span class="cat-count">66</span>', 'Islamabad Local <span class="cat-count">84</span>'],
  ['Peshawar Local <span class="cat-count">24</span>', 'Peshawar Local <span class="cat-count">37</span>'],
  ['Quetta Local <span class="cat-count">17</span>', 'Quetta Local <span class="cat-count">24</span>'],
  ['Overseas Pakistanis <span class="cat-count">3</span>', 'Overseas Pakistanis <span class="cat-count">39</span>'],
  ['Tax Guides <span class="cat-count">104</span>', 'Tax Guides <span class="cat-count">107</span>'],
  ['All Articles <span class="cat-count">1370</span>', 'All Articles <span class="cat-count">1,373</span>'],
];

fixes.forEach(function(f) {
  if (html.includes(f[0])) {
    html = html.split(f[0]).join(f[1]);
    console.log('✅ Fixed: ' + f[0].substring(0,40));
  } else {
    console.log('skip (already fixed): ' + f[0].substring(0,40));
  }
});

fs.writeFileSync('blogs.html', html, 'utf8');
console.log('Done');
