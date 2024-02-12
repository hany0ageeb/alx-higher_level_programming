#!/usr/bin/node
const { argv } = require('node:process');
const arg = argv.length > 2 ? argv[2] : undefined;
const message = 'C is fun';
if (arg && !Number.isNaN(arg)) {
  let x = parseInt(arg);
  while (x > 0) {
    console.log(message);
    x--;
  }
} else {
  console.log('Missing number of occurrences');
}
