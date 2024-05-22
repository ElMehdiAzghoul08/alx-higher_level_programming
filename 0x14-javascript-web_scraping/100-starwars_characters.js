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

    urlChar_.forEach((url_) => {
      req_(url_, (erro_, res_, body) => {
        if (erro_) {
          console.error(erro_);
          return;
        }

        if (res_.statusCode === 200) {
          const char_ = JSON.parse(body);
          console.log(char_.name);
        }
      });
    });
  }
});
