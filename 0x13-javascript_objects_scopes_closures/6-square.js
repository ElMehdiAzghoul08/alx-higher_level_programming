#!/usr/bin/node

const Square_ = require('./5-square.js');

class Square extends Square_ {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let a = 0; a < this.height; a++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
