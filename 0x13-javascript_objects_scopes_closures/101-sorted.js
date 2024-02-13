#!/usr/bin/node
const dict = require('./101-data.js').dict;
const occurrences = {};
for (const prop in dict) {
  if (dict[prop] in occurrences) {
    occurrences[dict[prop]].push(prop);
  } else {
    occurrences[dict[prop]] = [prop];
  }
}
console.log(occurrences);
