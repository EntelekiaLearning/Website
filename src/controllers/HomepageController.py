from flask import render_template
import os
import sys
import inspect

curDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parDir = os.path.dirname(curDir)
sys.path.insert(0, parDir) 

import conf

class HomepageController:
  def index(self):
    c = conf.Conf()
    vars = c.get('tmplVars')

    #one may override or add more
    #content to base conf values
    vars["baseTitle"] += 'Home'

    return render_template('homepage.jade', **vars)