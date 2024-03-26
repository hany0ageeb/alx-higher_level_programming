#!/usr/bin/node
const request = require('request');
/**
 * script that computes the number of tasks completed by user id.
 * 1. The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 * 2. Only print users with completed task
 * 3. You must use the module request
 */

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  if (response && response.statusCode === 200 && body) {
    const data = {};
    JSON.parse(body).filter((todo) => todo.completed).map((todo) => todo.userId).forEach(userId => {
      if (Object.prototype.hasOwnProperty.call(data, userId)) {
        data[userId] += 1;
      } else {
        data[userId] = 1;
      }
    });
    console.log(data);
  }
});
