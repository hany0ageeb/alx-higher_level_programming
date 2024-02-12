#!/usr/bin/node
const { argv } = require('node:process');
const args = argv.slice(2);
if (args.toString() === '') {
  console.log('No argument');
} else {
  console.log(args[0]);
}
