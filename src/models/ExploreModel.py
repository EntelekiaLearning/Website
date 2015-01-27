class ExploreModel:
  def selectTopics(self, uid):
    if uid == "":
      return (None, {"err": "No topic found"})
    else:
      return ({"test": "data"}, None)