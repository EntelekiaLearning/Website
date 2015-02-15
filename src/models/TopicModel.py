### NOTE: this model is simply using hard coded test data
### for purposes of PoC... will eventually be wired up to Neo4J
class TopicModel:
  def selectTopics(self, uid):
    res = {}

    if uid == "iw4madPIgn":
      res["rows"] = [{
        "uid": "AqJmuGPTOS",
        "title": "Philosophy"
      }]
    elif uid == "AqJmuGPTOS":
      res["rows"] = [{
        "uid": "tdN2eOgzP8",
        "title": "Existentialism"
      }, {
        "uid": "jHH0GP3zPj",
        "title": "Ethics"
      }, {
        "uid": "6cWUTstiib",
        "title": "Logic"
      }]
    elif uid == "tdN2eOgzP8":
      res["rows"] = [{
        "uid": "iTxRtBW011",
        "title": "Nietzsche",
        "course": True
      }, {
        "uid": "XUMEQd9Ash",
        "title": "Absurdism",
        "course": True
      }, {
        "uid": "PiKeHsRS2V",
        "title": "History of Existentialism",
        "course": True
      }]
    else:
      return (None, {"err": "No topic data found"})

    return (res, None)