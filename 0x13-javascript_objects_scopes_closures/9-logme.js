#!/usr/bin/node

let argsPrinted = 0;

exports.logMe = function (item) {
  console.log(`${argsPrinted}: ${item}`);
  argsPrinted++;
};
