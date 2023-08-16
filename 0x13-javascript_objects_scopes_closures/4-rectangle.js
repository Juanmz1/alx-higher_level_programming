#!/usr/bin/node
class Rectangle {
  width;
  height;
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = 'X';
    let i;
    if (!(isNaN(this.width))) {
      for (i = 1; i < this.width; i++) {
        row += 'X';
      }
      for (i = 0; i < this.height; i++) {
        console.log(row);
      }
    }
  }

  double () {
    if (!(isNaN(this.width))) {
      this.width *= 2;
      this.height *= 2;
    }
  }

  rotate () {
    const coln = this.width;
    const heig = this.height;
    if (!(isNaN(this.width))) {
      this.width = heig;
      this.height = coln;
    }
  }
};
module.exports = Rectangle;
