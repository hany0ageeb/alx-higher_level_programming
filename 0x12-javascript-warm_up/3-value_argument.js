#!/usr/bin/node
const args = process.argv.slice(2);
if (args.toString() === '') {
  console.log('No argument');
} else {
  console.log(args[0]);
}
