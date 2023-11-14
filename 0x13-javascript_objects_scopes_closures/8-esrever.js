#!/usr/bin/node
exports.esrever = function (list) {
  const occurence = [];
  for (let i = list.length - 1; i !== -1; i--) {
    occurence.push(list[i]);
  }
  return (occurence);
};
