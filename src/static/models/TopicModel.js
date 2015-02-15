var jQuery = require('jquery');
var conf = require('../conf');

module.exports = {
    /**
     * Brings down related topics
     * @param  {string} uid
     * @return {promise}
     */
    selectRelatedTopics: function(uid) {
        return jQuery.get(conf.API_URI + 'explore/topics/' + uid);
    },
};