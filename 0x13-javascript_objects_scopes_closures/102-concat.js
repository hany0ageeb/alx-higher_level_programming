#!/usr/bin/node
const src1 = process.argv[2];
const src2 = process.argv[3];
const dest = process.argv[4];
if (dest) {
  const fs = require('fs');
  try {
    const data1 = fs.readFileSync(src1, 'utf8');
    const data2 = fs.readFileSync(src2, 'utf8');
    fs.writeFileSync(dest, data1 + data2);
  } catch (err) {
    console.error(err);
  }
}
