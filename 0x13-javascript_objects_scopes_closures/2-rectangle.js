#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined) {
      return 'Rectangle {}';
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
