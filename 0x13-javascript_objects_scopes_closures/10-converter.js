#!/usr/bin/node
exports.converter = function (base) {
  function myConvertor (n) {
    return n.toString(base);
  }
  return myConvertor;
};
