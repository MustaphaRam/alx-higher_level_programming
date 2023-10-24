#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];


function displayCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        displayCharacters(characters, index + 1);
      }
    }
  });
}

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    if (response.statusCode === 200) {
      const content = JSON.parse(body);
      const characters = content.characters;
      displayCharacters(characters, 0);
    } else {
      console.log('code err ' + response.statusCode);
    }
  }
});
