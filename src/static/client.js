var ExploreViewModel = require('./viewmodels/ExploreViewModel');
var crossroads = require('crossroads');

crossroads.addRoute('/', function(){
  console.log('front end works');
});

crossroads.parse(window.location.pathname);
