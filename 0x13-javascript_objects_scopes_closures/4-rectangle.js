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

  rotate () {
    const tempo_ = this.width;
    this.width = this.height;
    this.height = tempo_;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
