#!/usr/bin/node
const { argv } = require('node:process');
const arg1 = argv.length > 2 ? argv[2] : undefined;
const arg2 = argv.length > 3 ? argv[3] : undefined;
console.log(`${arg1} is ${arg2}`);
