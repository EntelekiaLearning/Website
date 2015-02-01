var crossroads = require('crossroads');
var jQuery = require('jquery');
var ko = require('knockout');

crossroads.addRoute('/', function() {
  console.log('front end works');
});

crossroads.addRoute('/explore', function() {
    var ExploreViewModel = require('./viewmodels/ExploreViewModel');
    var e = new ExploreViewModel();
    e.init();

    ko.applyBindings(e, $('explore-namespace')[0]);
});

crossroads.parse(window.location.pathname);
