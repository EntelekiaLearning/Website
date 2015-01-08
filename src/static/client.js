var ExploreViewModel = require('./viewmodels/ExploreViewModel');
var crossroads = require('crossroads');

crossroads.addRoute('/explore', function(){
  var explore = new ExploreViewModel();
  explore.test();
});

crossroads.parse(window.location.pathname);
