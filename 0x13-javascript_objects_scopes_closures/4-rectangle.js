#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && w === parseInt(w) && h > 0 && h === parseInt(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const row = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; ++i) {
      console.log(row);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  getWidth () {
    return this.width;
  }
}
module.exports = Rectangle;
