#!/usr/bin/node
class Rectangle {
  #width;
  #height;
  constructor (w, h) {
    if (w > 0 && w === parseInt(w) && h > 0 && h === parseInt(h)) {
      this.#width = w;
      this.#height = h;
    }
  }

  get width () {
    return this.#width;
  }

  set width (w) {
    this.#width = w;
  }

  get height () {
    return this.#height;
  }

  set height (h) {
    this.#height = h;
  }

  print () {
    const row = 'X'.repeat(this.#width);
    for (let i = 0; i < this.#height; ++i) {
      console.log(row);
    }
  }

  rotate () {
    [this.#width, this.#height] = [this.#height, this.#width];
  }

  double () {
    this.#width *= 2;
    this.#height *= 2;
  }
}
module.exports = Rectangle;
