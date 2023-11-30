#!/usr/bin/node
const { argv } = require('process');
const num = parseInt(argv[2]);
console.log(computeFactorial(num));

function computeFactorial (num) {
  if (!num) {
    return 1;
  }
  return num * computeFactorial(num - 1);
}
