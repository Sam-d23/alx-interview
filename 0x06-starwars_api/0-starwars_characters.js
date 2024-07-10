#!/usr/bin/node

const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) return console.log(err);
    
    const charactersURL = JSON.parse(body).characters;
    const characterPromises = charactersURL.map(url => new Promise((resolve, reject) => {
      request(url, (promiseErr, __, charactersReqBody) => {
        if (promiseErr) return reject(promiseErr);
        resolve(JSON.parse(charactersReqBody).name);
      });
    }));

    Promise.all(characterPromises)
      .then(names => console.log(names.join('\n')))
      .catch(console.log);
  });
}
