#!/usr/bin/node
const request = require('request');
const fs = require('fs');
/**
 * script that gets the contents of a webpage and stores it in a file.
 * 1. The first argument is the URL to request
 * 2. The second argument the file path to store the body response
 * 3. The file must be UTF-8 encoded
 * 4. You must use the module request
 */

request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
