#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const a = process.argv.length > 2 ? parseInt(process.argv[2]) : Number.NaN;
const b = process.argv.length > 3 ? parseInt(process.argv[3]) : Number.NaN;
console.log(add(a, b));
