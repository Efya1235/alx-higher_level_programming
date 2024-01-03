#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, (error, response, body) => {
  if (!error) {
    const res = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < res.length; i++) {
      for (let j = 0; j < res[i].characters.length; j++) {
        if (res[i].characters[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log(error);
  }
});
