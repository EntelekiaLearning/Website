import json
import os
import sys
import inspect

class Conf:
  @staticmethod
  def get(key):
    with open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/conf.json') as jsonDataFile:
      c = json.load(jsonDataFile)
       
    return c[key]