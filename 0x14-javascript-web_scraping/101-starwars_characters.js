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
function printCharacterNames (urls) {
  for (let index = 0; index < urls.length; index++) {
    request.get(urls[index], (error, response, body) => {
      if (!error && response && response.statusCode === 200 && body) {
        console.log(JSON.parse(body).name);
      }
    });
  }
}
request.get(url, (error, response, body) => {
  if (!error && response && response.statusCode === 200 && body) {
    printCharacterNames(JSON.parse(body).characters);
  }
});
