#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const { argv } = require('node:process');
const a = argv.length > 2 ? parseInt(argv[2]) : Number.NaN;
const b = argv.length > 3 ? parseInt(argv[3]) : Number.NaN;
console.log(add(a, b));
