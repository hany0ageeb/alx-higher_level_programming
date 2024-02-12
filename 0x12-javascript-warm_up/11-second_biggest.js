#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length <= 3) {
  console.log(0);
} else {
  const nums = argv.slice(2).map((x) => parseInt(x)).sort();
  console.log(nums[nums.length - 2]);
}
