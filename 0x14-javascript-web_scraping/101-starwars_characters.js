#!/usr/bin/node
const request = require('request');
/**
 * script that prints all characters of a Star Wars movie:
 *  1. The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 *  2. Display one character name by line in the same order of the list “characters” in the /films/ response
 *  3. You must use the Star wars API
 *  4. You must use the module request
 */

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  if (response && response.statusCode === 200 && body) {
    JSON.parse(body).characters.forEach((characterUrl) => {
      request.get(characterUrl, (error1, response1, body1) => {
        if (error1) {
          console.log(error1);
        }
        if (response1 && response1.statusCode === 200 && body1) {
          const character = JSON.parse(body1);
          console.log(character.name);
        }
      });
    });
  }
});
