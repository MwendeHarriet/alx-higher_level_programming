#!/usr/bin/node
const { argv } = require('process');
const myVar1 = parseInt(argv[2]);
const myVar2 = parseInt(argv[3]);
console.log(add(myVar1, myVar2));

function add (a, b) {
  return a + b;
}
