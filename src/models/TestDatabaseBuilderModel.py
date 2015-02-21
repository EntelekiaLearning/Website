from neo4jrestclient.client import GraphDatabase
import os
import inspect
import sys

curDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parDir = os.path.dirname(curDir)
sys.path.insert(0, parDir) 

import conf

class TestDatabaseBuilderModel:
  def build(self):
    c = conf.Conf()
    vars = c.get('db') 
    
    gdb = GraphDatabase(vars["url"] + str(vars["port"]) + vars["dir"])