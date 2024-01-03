#!/usr/bin/node
const request = require('request');
const APIurl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(APIurl, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printstarwarsCharacters(characters, 0);
  }
});

function printstarwarsCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printstarwarsCharacters(characters, index + 1);
      }
    }
  });
}
