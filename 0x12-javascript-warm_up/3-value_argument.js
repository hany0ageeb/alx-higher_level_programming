#!/usr/bin/node
const { argv } = require('node:process');
const args = argv.slice(2);
if (args.toString() === '') {
  console.log('No argument');
} else {
  args.forEach((val) => {
    console.log(val);
  });
}
