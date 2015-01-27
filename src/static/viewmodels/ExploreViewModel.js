module.exports = function() {
    var self = this;

    self.init = function() {
        var ExploreModel = require('../models/ExploreModel');
        ExploreModel.init();
    };
};