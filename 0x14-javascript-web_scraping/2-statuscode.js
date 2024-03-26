#!/usr/bin/node
/**
 * script that display the status code of a GET request.
 *  1. The first argument is the URL to request (GET)
 *  2. The status code must be printed like this: code: <status code>
 *  3. You must use the module request
 */
const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  if (response) {
    console.log(`code: ${response.statusCode}`);
  }
});
