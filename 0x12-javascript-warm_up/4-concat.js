#!/usr/bin/node
const arg1 = process.argv.length > 2 ? process.argv[2] : undefined;
const arg2 = process.argv.length > 3 ? process.argv[3] : undefined;
console.log(`${arg1} is ${arg2}`);
