#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (w <= 0 || h <= 0) {
      const emptyObj_ = {};
      console.log(emptyObj_);
    }
  }
}

module.exports = Rectangle;
