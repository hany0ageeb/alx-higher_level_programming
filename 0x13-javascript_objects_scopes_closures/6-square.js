#!/usr/bin/node
const Square0 = require('./5-square.js');
class Square extends Square0 {
  charPrint (c) {
    c = c || 'X';
    const row = c.repeat(super.size);
    for (let i = 0; i < super.size; ++i) {
      console.log(row);
    }
  }
}
module.exports = Square;
