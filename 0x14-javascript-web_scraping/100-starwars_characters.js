#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/'+process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    if (response.statusCode === 200){
      const content = JSON.parse(body);
      const characters = content.characters;
      // console.log(characters);
      for (const character of characters) {
        request.get(character, (error, response, body) => {
          if (error) {
            console.log(error);
          } else {
            const names = JSON.parse(body);
            console.log(names.name);
          }
        });
      }
    } else {
      console.log('code err ' + response.statusCode);
    }
  }
});
