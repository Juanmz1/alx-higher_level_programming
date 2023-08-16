#!/usr/bin/node
const dict = require('./101-data').dict;

const totatList = Object.entries(dict);
const valu = Object.values(dict);
const valUniq = [...new Set(valu)];
const newDict = {};
for (const j in valUniq) {
  const list = [];
  for (const k in totatlist) {
    if (totatlist[k][1] === valUniq[j]) {
      list.unshift(totatlist[k][0]);
    }
  }
  newDict[valUniq[j]] = list;
};
console.log(newDict);
