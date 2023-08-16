#!/usr/bin/node
class Rectangle {
  width;
  height;
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    };
  };

  print () {
    let row = 'X';
    let i;
    if (!(isNaN(this.width))) {
      for (i = 1; i < this.width; i++) {
        row += 'X';
     };
      for (i = 0; i < this.height; i++) {
        console.log(row);
      };
    };
  };
};

module.exports = Rectangle;
