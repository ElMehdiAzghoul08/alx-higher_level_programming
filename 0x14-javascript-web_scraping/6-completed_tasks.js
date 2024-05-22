#!/usr/bin/node
const req_ = require('request');

const urlApI_ = process.argv[2];

req_(urlApI_, (error_, response_, body_) => {
  if (error_) {
    console.error(error_);
    return;
  }

  if (response_.statusCode === 200) {
    const todos_ = JSON.parse(body_);
    const finisheDTasks_ = todos_.reduce((a_, todo_) => {
      if (todo_.completed) {
        a_[todo_.userId] = (a_[todo_.userId] || 0) + 1;
      } else {
        a_[todo_.userId] = a_[todo_.userId] || 0;
      }
      return a_;
    }, {});

    if (Object.keys(finisheDTasks_).length === 0) {
      for (let i = 1; i <= 10; i++) {
        finisheDTasks_[i] = 0;
      }
    }
    console.log(finisheDTasks_);
  }
});
