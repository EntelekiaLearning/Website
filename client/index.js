var Foo = require('./ViewModels/TestViewModel');
var crossroads = require('crossroads');

crossroads.addRoute('/', function(){
  var test = new Foo();
  test.foo();
});

crossroads.parse(window.location.pathname);