#!/usr/bin/node

function printArguments () {
  if (process.argv[2]) {
    if (process.argv[3]) {
      console.log(process.argv[2] + ' is ' + process.argv[3]);
    } else {
      console.log(process.argv[2] + ' is undefined');
    }
  } else {
    console.log('undefined is undefined');
  }
}

printArguments();
