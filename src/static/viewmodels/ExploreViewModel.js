var jQuery = require('jquery');

module.exports = function() {
  this.test = function() {
    //should be a template
    jQuery('.test').text('dynamic content!');
  };
};
