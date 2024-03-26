#!/usr/bin/node
/**
 * script that reads and prints the content of a file.
 * 1. The first argument is the file path
 * 2. The content of the file must be read in utf-8
 * 3. If an error occurred during the reading, print the error object
 */
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
