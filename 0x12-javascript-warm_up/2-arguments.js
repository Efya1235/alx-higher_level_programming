#!/usr/bin/node
function PrintArguments () {
  const Arguments = process.argv.length - 2;

  if (Arguments === 0) {
    console.log('No argument');
  } else if (Arguments === 1) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
}
PrintArguments();
