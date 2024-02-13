#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w && w > 0 && h && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return {};
    }
  }
}
module.exports = Rectangle;
