#!/usr/bin/node
const request = require('request');
/**
 * script that prints the number of movies where the character “Wedge Antilles” is present.
 * 1. The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
 * 2. Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
 * 3. You must use the module request
 */

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    return;
  }
  console.log(JSON.parse(body).results.reduce((count, movie) => {
    if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      return count + 1;
    } else {
      return count;
    }
  }, 0));
});
