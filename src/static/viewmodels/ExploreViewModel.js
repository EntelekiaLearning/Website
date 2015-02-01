var ExploreModel = require('../models/ExploreModel');
var ko = require('knockout');
var jQuery = require('jquery');
var _ = require('lodash');
var conf = require('../conf');

module.exports = function() {
    var self = this;

    /**
     * Ctor. Registers observables and pulls
     * down some initial data
     * @return {void}
     */
    self.init = function() {
        //topic area vars
        self.topics = ko.observableArray();

        //learning info area vars
        self.showLearningInfo = ko.observable(false);
        self.resources = ko.observableArray();
        self.opportunities = ko.observableArray();

        //will eventually be determined by the initial
        //search by the user (via passing a keyword param)
        self.getRelatedTopics({
            uid: 'iw4madPIgn'
        });
    };

    /**
     * Informs Knockout to update observables
     * @param  {object} targetObj  observable to mutate
     * @param  {array} newDataSet optional dataset to apply
     * @return {void}
     */
    self.commit = function(targetObj, newDataSet) {
        if (typeof(newDataSet) === 'undefined') {
            newDataSet = targetObj();
        }

        targetObj([]); //disposes old val
        targetObj(newDataSet);
    };

    /**
     * Handles click events for each topic node
     * @param  {object} ref topic
     * @return {void}
     */
    self.topicClick = function(ref) {
        if (ref.activeTopic === true) {
            self.deactivateTopic(ref);
        } else {
            self.activateTopic(ref);

            if (ref.course === true) {
                self.getLearningInfo(ref);
            } else {
                self.getRelatedTopics(ref);
            }
        }

        self.learningInfoVisibility(false);
    };

    /**
     * Asks the model to supply topic data
     * based on the provided topic uid
     * @param  {object} ref topic
     * @return {void}
     */
    self.getRelatedTopics = function(ref) {
        var newDataSet = self.topics(); //base data for appending

        //async series obj
        var series = {
            select: function(uid) {
                return ExploreModel.selectRelatedTopics(uid);
            },

            //ko expects some additional properties on the
            //frontend such as .course and .activeTopic
            sanitize: function(resData) {
                _.each([resData], function(outerVal, outerKey) {
                    _.each(outerVal.rows, function(innerVal, innerKey) {
                        if (typeof(innerVal.activeTopic) === 'undefined') {
                            innerVal.activeTopic = false;
                        }

                        if (typeof(innerVal.course) === 'undefined') {
                            innerVal.course = false;
                        }
                    });

                    newDataSet.push(outerVal);
                });
            },
            commit: function() {
                self.commit(self.topics, newDataSet);
            },
            err: function(err) {
                var msg = '';

                if (typeof(err.responseText) !== 'undefined') {
                    var parsed = JSON.parse(err.responseText);
                    msg = parsed.err;  
                } else {
                    msg = conf.DEF_ERR;
                }

                alert(msg);
            }
        };

        series.select(ref.uid)
            .then(series.sanitize)
            .then(series.commit)
            .fail(series.err);
    };

    /**
     * Disables neighboring active node and
     * removes subsequent topic nodes. Afterwards,
     * renders current active topic.
     * @param  {object} ref topic
     * @return {void}
     */
    self.activateTopic = function(ref) {
        self.deactivateNeighborTopics(ref);
        self.deactivateSubsequentTopics(ref);

        ref.activeTopic = true;
        self.commit(self.topics);
    };

    /**
     * Removes subsequent topic nodes. Afterwards,
     * renders current topic inactive.
     * @param  {object} ref topic
     * @return {void}
     */
    self.deactivateTopic = function(ref) {
        self.deactivateSubsequentTopics(ref);

        ref.activeTopic = false;
        self.commit(self.topics);
    };

    /**
     * Disables neighboring active nodes
     * @param  {object} ref topic
     * @return {void}
     */
    self.deactivateNeighborTopics = function(ref) {
        var newActiveTopic = ref.uid;
        var mutationGroup = [];

        _.each(self.topics(), function(outerVal, outerKey) {
            _.each(outerVal.rows, function(innerVal, innerKey) {
                if (newActiveTopic === innerVal.uid) {
                    mutationGroup = outerVal.rows;
                }
            });
        });

        _.each(mutationGroup, function(val, key) {
            if (val.uid !== newActiveTopic) {
                self.deactivateTopic(val);
            }
        });
    };

    /**
     * Removes subsequent topic nodes.
     * @param  {object} ref topic
     * @return {void}
     */
    self.deactivateSubsequentTopics = function(ref) {
        var curIdx = 1;
        _.each(self.topics(), function(outerVal, outerKey) {
            _.each(outerVal.rows, function(innerVal, innerKey) {
                if (ref.uid === innerVal.uid) {
                    curIdx += outerKey;
                }
            });
        });

        var newDataSet = self.topics().slice(0, curIdx);
        self.commit(self.topics, newDataSet);
    };

    /**
     * Asks the model to supply learning info data
     * based on the provided topic uid
     * @param  {object} ref topic
     * @return {void}
     */
    self.getLearningInfo = function(ref) {
        //async series obj
        var series = {
            select: function(uid) {
                return ExploreModel.selectLearningInfo(uid);
            },
            commit: function(resData) {
                self.commit(self.resources, resData.rows.resources || []);
                self.commit(self.opportunities, resData.rows.opportunities || []);
                self.learningInfoVisibility(true);
            },
            err: function(err) {
                var msg = '';

                if (typeof(err.responseText) !== 'undefined') {
                    var parsed = JSON.parse(err.responseText);
                    msg = parsed.err;  
                } else {
                    msg = conf.DEF_ERR;
                }

                self.learningInfoVisibility(false);
                alert(msg);
            }
        };

        series.select(ref.uid)
            .then(series.commit)
            .fail(series.err);
    };

    /**
     * enables/disables learning info area
     * @param  {boolean} status
     * @return {void}
     */
    self.learningInfoVisibility = function(status) {
        var elem = jQuery('.learning-info-view');
        if (status === true) {
            elem.removeClass('hide');
            self.commit(self.showLearningInfo, true);
        } else {
            elem.addClass('hide');
            self.commit(self.showLearningInfo, false);
        }
    };
};