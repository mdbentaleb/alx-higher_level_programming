#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let u = 0; u < x; u++) theFunction();
};
