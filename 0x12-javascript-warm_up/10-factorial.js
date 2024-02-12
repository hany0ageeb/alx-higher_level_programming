#!/usr/bin/node
function factorial (n) {
  if (Number.isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const n = process.argv.length > 2 ? parseInt(process.argv[2]) : Number.NaN;
console.log(factorial(n));
