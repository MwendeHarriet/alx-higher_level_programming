#!/usr/bin/node
const args = process.argv;
const myVar1 = args[2] ? args[2] : 'NaN';
const myVar3 = args[3] ? args[3] : 'NaN';
const myVar2 = parseInt(myVar1, 10);
const myVar4 = parseInt(myVar3, 10);

if (!myVar2) {
  console.log(0);
} else if (!myVar4) {
  console.log(0);
} else {
  const newarray = [];
  for (let i = 2; i < args.length; i++) {
    newarray.push(parseInt(args[i], 10));
  }
  newarray.sort((a, b) => a - b);
  console.log(newarray[newarray.length - 2]);
}
