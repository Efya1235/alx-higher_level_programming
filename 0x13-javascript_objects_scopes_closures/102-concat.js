#!/usr/bin/node
const fs = require('fs');

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

function concatenateFiles () {
  const fileContents1 = fs.readFileSync(sourceFilePath1, 'utf8');
  const fileContents2 = fs.readFileSync(sourceFilePath2, 'utf8');
  const concatenatedContents = fileContents1 + fileContents2;

  fs.writeFileSync(destinationFilePath, concatenatedContents);
}

if (sourceFilePath1 && sourceFilePath2 && destinationFilePath) {
  concatenateFiles();
  console.log(`Files concatenated and saved to ${destinationFilePath}`);
} else {
  console.error('Usage: node concat.js <sourceFilePath1> <sourceFilePath2> <destinationFilePath>');
}
