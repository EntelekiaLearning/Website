### NOTE: this model is simply using hard coded test data
### for purposes of PoC... will eventually be wired up to Neo4J
class ExploreModel:
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

  def selectLearningInfo(self, uid):
    res = {}

    if uid == "iTxRtBW011":
      res["rows"] = {
        "opportunities": [{
          "uid": "o0W4uoIP",
          "title": "Intro to Nietzsche",
          "description": "Learn about the German philologist, philosopher, cultural critic, poet and composer.",
          "locations": ["New York", "Pittsburgh", "Portland"],
          "imgUrl": "http://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Friedrich_Nietzsche_drawn_by_Hans_Olde.jpg/800px-Friedrich_Nietzsche_drawn_by_Hans_Olde.jpg"
        }, {
          "uid": "e8fEoR9P",
          "title": "All Too Human, A Survey",
          "description": "Learn about Nietzsche's book of aphorisms ranging from metaphysics to morality to religion to gender studies.",
          "locations": ["Chicago", "Pittsburgh"],
          "imgUrl": "http://thumbs.dreamstime.com/x/diverse-population-people-group-8177274.jpg"
        }],
        "resources": [{
          "uid": "ifEr83a",
          "title": "Beyond Good and Evil",
          "url": "http://philosophy.lander.edu/intro/articles/nietzsche-a.pdf",
          "imgUrl": "http://www.keepitmovingblog.com/wp-content/uploads/2014/03/broken-chain.jpg"
        }]
      }
    else:
      return (None, {"err": "No learning data found"})

    return (res, None)