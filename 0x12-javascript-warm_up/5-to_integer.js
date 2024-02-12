#!/usr/bin/node
const { argv } = require('node:process');
const arg = argv.length > 2 ? argv[2] : undefined;
if (arg && !Number.isNaN(arg)) {
  console.log(`My number: ${parseInt(arg)}`);
} else {
  console.log('Not a number');
}
