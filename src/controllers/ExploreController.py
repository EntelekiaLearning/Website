from flask import render_template
import os
import sys
import inspect

curDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parDir = os.path.dirname(curDir)
sys.path.insert(0, parDir) 

import conf
from models.LearningModel import LearningModel
from models.TopicModel import TopicModel

class ExploreController:
  def index(self):
    c = conf.Conf()
    vars = c.get('tmplVars')

    vars["title"] += "Explore"

    return render_template('explore.jade', **vars)

  def getTopics(self, uid):
    e = TopicModel()
    res, err = e.selectTopics(uid)

    if err != None:
      return (500, err)

    return (200, res)

  def getLearningInfo(self, uid):
    e = LearningModel()
    res, err = e.selectLearningInfo(uid)

    if err != None:
      return (500, err)

    return (200, res)