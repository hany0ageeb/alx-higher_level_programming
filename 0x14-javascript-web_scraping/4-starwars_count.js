#!/usr/bin/node
const request = require('request');
/**
 * script that prints the number of movies where the character “Wedge Antilles” is present.
 * 1. The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
 * 2. Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
 * 3. You must use the module request
 */

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  if (response && response.statusCode === 200) {
    if (response.headers['content-type'] === 'application/json') {
      const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
      const films = JSON.parse(body).results.filter((film) => film.characters.includes(characterUrl));
      console.log(films.length);
    }
  }
});
