#!/usr/bin/node

exports.converter = function (base) {
  function Convert2Base (n) {
    return n.toString(base);
  }

  return Convert2Base;
};
