#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  for (let u = list.length - 1; u >= 0; u--) {
    newList.push(list[u]);
  }
  return newList;
};
