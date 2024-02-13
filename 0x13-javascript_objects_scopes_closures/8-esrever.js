#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  for (let i = 0, j = list.length - 1; i < list.length && j >= 0; ++i, --j) {
    reversed[i] = list[j];
  }
  return reversed;
};
