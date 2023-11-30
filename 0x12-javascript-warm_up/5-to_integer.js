#!/usr/bin/node
const args = process.argv;
const myVar1 = args[2] ? args[2] : 'Not a number';
const myVar2 = parseInt(myVar1, 10);
if (myVar2) {
  console.log('My number: ' + myVar2);
} else {
  console.log('Not a number');
}
