#!/usr/bin/node
let nargv = 0;

exports.logMe = function (item) {
  console.log(nargv + ': ' + item);
  nargv++;
};
