#!/usr/bin/node

exports.esrever = function (list) {
    const reversed_ = [];

    for (let idx = list.length -1; idx >= 0; idx--) {
        reversed_.push(list[idx]);
    }

    return reversed_;
};