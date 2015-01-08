var jQuery = require('jquery');

module.exports = function() {
    this.foo = function() {
        jQuery('.view-area').text('It works!');
    };
};