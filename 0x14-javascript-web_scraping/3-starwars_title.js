#!/usr/bin/node
/**
 * script that prints the title of a Star Wars movie where the episode number matches a given integer.
 * 1. The first argument is the movie ID
 * 2. You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
 * 3. You must use the module request
 */
const request = require('request');

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  if (response && response.statusCode === 200) {
    const film = JSON.parse(body);
    console.log(film.title);
  }
});
