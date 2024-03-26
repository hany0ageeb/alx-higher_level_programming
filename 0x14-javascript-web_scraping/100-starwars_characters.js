#!/usr/bin/node
const request = require('request');
/**
 * script that prints all characters of a Star Wars movie
 * 1. The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * 2. Display one character name by line
 * 3. You must use the Star wars API
 * 4. You must use the module request
 */

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
request.get(url, (error, response, body) => {
  if (!error && response && response.statusCode === 200 && body) {
    JSON.parse(body).characters.forEach((characterUrl) => {
      request.get(characterUrl, (error2, response2, body2) => {
        if (!error2 && response2 && response2.statusCode === 200 && body2) {
          console.log(JSON.parse(body2).name);
        }
      });
    });
  }
});
