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

  print () {
    for (let a = 0; a < this.height; a++) {
      let printLine_ = '';
      for (let b = 0; b < this.width; b++) {
        printLine_ = printLine_ + 'X';
      }
      console.log(printLine_);
    }
  }
}

module.exports = Rectangle;
