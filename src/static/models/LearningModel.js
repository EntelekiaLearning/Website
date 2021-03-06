var jQuery = require('jquery');
var conf = require('../conf');

module.exports = {
    /**
     * Brings down related learning items
     * @param  {string} uid
     * @return {promise}
     */
    selectLearningInfo: function(uid) {
        return jQuery.get(conf.API_URI + 'explore/learninginfo/' + uid);
    }
};