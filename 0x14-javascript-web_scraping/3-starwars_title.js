#!/usr/bin/node

const request = require('request');
const episodenum = process.argv[2];
const APIurl = 'https://swapi-api.hbtn.io/api/films/';

request(APIurl + episodenum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
