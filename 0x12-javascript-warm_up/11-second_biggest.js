#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let nums = process.argv.slice(2);
  if (nums.length >= 2) {
    nums = nums.map((x) => parseInt(x));
    nums.sort();
    console.log(nums[nums.length - 2]);
  }
}
