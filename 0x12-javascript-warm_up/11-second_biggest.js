#!/usr/bin/node
const nums = process.argv.slice(2).filter((x) => x && !Number.isNaN(x)).map((x) => parseInt(x));
if (nums.length >= 2) {
  nums.sort();
  console.log(nums[nums.length - 2]);
} else {
  console.log('0');
}
