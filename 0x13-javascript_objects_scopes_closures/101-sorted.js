#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};

for (const userID in dict) {
  const occurrences = dict[userID];

  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }

  newDict[occurrences].push(userID);
}

console.log(newDict);
