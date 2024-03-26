#!/usr/bin/node
/**
 * script that writes a string to a file.
 * 1. The first argument is the file path
 * 2. The second argument is the string to write
 * 3. The content of the file must be written in utf-8
 * 4. If an error occurred during while writing, print the error object
 */
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
