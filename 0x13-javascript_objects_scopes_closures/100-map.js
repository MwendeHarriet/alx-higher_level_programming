#!/usr/bin/node
const oldlist = require('./100-data.js').list;

console.log(oldlist);
console.log(oldlist.map((x, index) => x * index));
