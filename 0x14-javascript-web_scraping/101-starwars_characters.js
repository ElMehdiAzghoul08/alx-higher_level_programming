#!/usr/bin/node
const req_ = require('request');

const idMov_ = process.argv[2];
const urlApI_ = `https://swapi-api.hbtn.io/api/films/${idMov_}/`;

req_(urlApI_, (erro_, res_, body) => {
  if (erro_) {
    console.error(erro_);
    return;
  }

  if (res_.statusCode === 200) {
    const film_ = JSON.parse(body);
    const urlChar_ = film_.characters;

    const promisChar_ = urlChar_.map(url_ => {
      return new Promise((resolve, reject) => {
        req_(url_, (erro_, res_, body) => {
          if (erro_) {
            reject(erro_);
          } else if (res_.statusCode === 200) {
            const char_ = JSON.parse(body);
            resolve(char_.name);
          }
        });
      });
    });

    Promise.all(promisChar_)
      .then(a_ => {
        a_.forEach(name_ => console.log(name_));
      })
      .catch(erro_ => console.error(erro_));
  }
});
