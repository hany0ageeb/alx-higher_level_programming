#!/usr/bin/node
const { argv } = require('node:process');
const size = argv.length === 3 ? parseInt(argv[2]) : undefined;
if (size && !Number.isNaN(size)) {
  if (size > 0) {
    for (let i = 0; i < size; ++i) {
      console.log('X'.repeat(size));
    }
  }
} else {
  console.log('Missing size');
}
