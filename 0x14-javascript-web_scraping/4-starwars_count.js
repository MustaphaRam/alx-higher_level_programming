#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let num = 0;

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    if (response.statusCode === 200) {
      const content = JSON.parse(body);
      content.results.forEach((film) => {
        film.characters.forEach((character) => {
          if (character.includes(18)) {
              num += 1;
          }
        });
      });
      console.log(num);
    } else {
        console.log('code err '+ response.statusCode);
    }
  }
});
