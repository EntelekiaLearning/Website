import json

class Conf:
  @staticmethod
  def get(key):
    with open('./conf.json') as jsonDataFile:
      c = json.load(jsonDataFile)
       
    return c[key]