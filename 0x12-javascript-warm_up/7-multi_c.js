#!/usr/bin/node

const numOccurrences = Number(process.argv[2]);

if (!isNaN(numOccurrences) && Number.isInteger(numOccurrences)) {
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
