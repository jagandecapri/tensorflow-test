var createObject = require('bindings')('api');

var obj = createObject(10);
console.log( obj.createSession() ); // 11
