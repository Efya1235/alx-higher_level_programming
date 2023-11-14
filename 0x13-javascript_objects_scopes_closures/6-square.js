#!/usr/bin/node

const MainSquare = require('./5-square');

class Square extends MainSquare {
  charPrint (c = 'X') {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let space = '';
      for (let j = 0; j < this.width; j++) {
        space += c;
      }
      console.log(space);
    }
  }
}
module.exports = Square;
