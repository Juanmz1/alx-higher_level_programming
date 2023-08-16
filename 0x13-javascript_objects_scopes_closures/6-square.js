#!/usr/bin/node
const square = require('./5-square');

const Square = class extends square {
  charPrint (c) {
    let i;
    let chara_c = 'X';
    let C = 'X';
    if (!(c === undefined)) {
      chara_c = c;
      C = c;
    }
    if (!(isNaN(this.width))) {
      for (i = 1; i < this.width; i++) {
        chara_c += C;
      }
      for (i = 0; i < this.width; i++) {
        console.log(chara_c);
      }
    }
  }
};

module.exports = Square;
