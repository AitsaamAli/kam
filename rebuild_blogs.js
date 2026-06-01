// This script just helps verify files exist
const files = [
  'tax-filing-consultants-pakistan.html',
  'tax-filing-engineers-pakistan.html', 
  'tax-filing-architects-pakistan.html',
  'tax-filing-traders-pakistan.html',
  'tax-filing-exporters-pakistan.html',
  'tax-filing-importers-pakistan.html',
  'tax-benefits-filer-pakistan.html'
];
const fs = require('fs');
files.forEach(f => console.log(f, fs.existsSync('c:\Users\786\Desktop\kam\' + f) ? 'EXISTS' : 'MISSING'));
