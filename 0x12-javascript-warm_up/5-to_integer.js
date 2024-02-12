#!/usr/bin/node
const arg = process.argv.length > 2 ? parseInt(process.argv[2]) : undefined;
if (arg && !Number.isNaN(arg)) {
  console.log(`My number: ${arg}`);
} else {
  console.log('Not a number');
}
