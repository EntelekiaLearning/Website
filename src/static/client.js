var crossroads = require('crossroads');

crossroads.addRoute('/', function() {
  console.log('front end works');
});

crossroads.addRoute('/explore', function() {
    var ExploreViewModel = require('./viewmodels/ExploreViewModel');
    var e = new ExploreViewModel();
    e.init();
});

crossroads.parse(window.location.pathname);
