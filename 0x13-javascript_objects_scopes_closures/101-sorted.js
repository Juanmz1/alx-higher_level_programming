#!/usr/bin/node
const mydict = require('./101-data').dict;

const totatList = Object.entries(mydict);
const val = Object.values(mydict);
const valUniq = [...new Set(val)];
const newDict = {};
for (const j in valUniq) {
  const list = [];
  for (const k in totatlist) {
    if (totatlist[k][1] === valUniq[j]) {
      list.unshift(totatlist[k][0]);
    }
  }
  newDict[valUniq[j]] = list;
}
console.log(newDict);
