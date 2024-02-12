#!/usr/bin/node
const uniqueNums = new Set(process.argv.slice(2).map((x) => parseInt(x)));
if (uniqueNums.size >= 2) {
  const sortedNums = Array.from(uniqueNums).sort((a, b) => a - b);
  console.log(sortedNums[sortedNums.length - 2]);
} else {
  console.log(0);
}
