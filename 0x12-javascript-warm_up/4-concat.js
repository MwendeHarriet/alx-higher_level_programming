#!/usr/bin/node
const args = process.argv;
const myVar1 = args[2] ? args[2] : 'undefined';
const myVar2 = args[3] ? args[3] : 'undefined';
console.log(myVar1 + ' is ' + myVar2);
