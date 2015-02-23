from py2neo import Graph
import os
import inspect
import sys

curDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parDir = os.path.dirname(curDir)
sys.path.insert(0, parDir)

import conf

class TestDatabaseBuilderModel:
  def getOpportunities(self):
    data = [{
      "uid": "o0W4uoIP",
      "title": "Nietzsche and the Tragic Form",
      "desc": "In this course we will read and respond to Nietzsche's first primary work, \"The Birth of Tragedy\". This section should have a character limit of some kind. In this course we will read and respond to Nietzsche's first primary work.",
      "url": "http://learnpgh.org/course/nietzsche-tragic-form",
      "author": "Tyke Nunez",
      "addedBy": "Pittsburgh Nietzsche Scholars",
      "addedByUrl": "http://nietzschescholars.com/pittsburgh",
      "time": "05/06/2015",
      "type": "Course",
      "isPrivate": False,
      "isChildFriendly": False,
      "isNonFree": True,
      "relationships": []
    }, {
      "uid": "e8fEoR9P",
      "title": "All Too Human, A Survey",
      "desc": "Learn about Nietzsche's book of aphorisms ranging from metaphysics to morality to religion to gender studies.",
      "url": "http://learnpgh.org/course/nietzsche-all-too-soon",
      "author": "John Douglas",
      "addedBy": "Pittsburgh Nietzsche Scholars",
      "addedByUrl": "http://nietzschescholars.com/pittsburgh",
      "time": "04/24/2015",
      "type": "Course",
      "isPrivate": True,
      "isChildFriendly": True,
      "isNonFree": False,
      "relationships": []
    }]

    checkForDupsQuery = []
    checkForDupsQuery.append("MATCH")
    checkForDupsQuery.append("  (c:opportunity)")
    checkForDupsQuery.append("WHERE")
    checkForDupsQuery.append("  c.uid={uid}")
    checkForDupsQuery.append("RETURN")
    checkForDupsQuery.append("  COUNT(c) AS cnt")

    createOppQuery = []
    createOppQuery.append("CREATE")
    createOppQuery.append("  (c: opportunity {")
    createOppQuery.append("    uid:{uid},")
    createOppQuery.append("    title:{title},")
    createOppQuery.append("    desc:{desc},")
    createOppQuery.append("    url:{url},")
    createOppQuery.append("    author:{author},")
    createOppQuery.append("    addedBy:{addedBy},")
    createOppQuery.append("    addedByUrl:{addedByUrl},")
    createOppQuery.append("    time:{time},")
    createOppQuery.append("    type:{type},")
    createOppQuery.append("    isPrivate:{isPrivate},")
    createOppQuery.append("    isChildFriendly:{isChildFriendly},")
    createOppQuery.append("    isNonFree:{isNonFree}")
    createOppQuery.append("  })")

    return (data, {
      "checkForDupsQuery": "\n".join(checkForDupsQuery),
      "createOppQuery": "\n".join(createOppQuery)
    })

  def getResources(self):
    data = [{
      "uid": "ifEr83a",
      "title": "Beyond Good and Evil",
      "desc": "In Beyond Good and Evil, Nietzsche accuses past philosophers of lacking critical sense and blindly accepting dogmatic premises in their consideration of morality. Specifically, he accuses them of founding grand metaphysical systems upon the faith that the good man is the opposite of the evil man, rather than just a different expression of the same basic impulses that find more direct expression in the evil man.",
      "url": "http://philosophy.lander.edu/intro/articles/nietzsche-a.pdf",
      "author": "Friedrich Nietzsche",
      "addedBy": "Tara David",
      "addedByUrl": "http://nietzschescholars.com/pittsburgh",
      "time": "1886",
      "type": "Book",
      "isPrivate": True,
      "isChildFriendly": True,
      "isNonFree": True,
      "relationships": []
    }]

    checkForDupsQuery = []
    checkForDupsQuery.append("MATCH")
    checkForDupsQuery.append("  (c:resource)")
    checkForDupsQuery.append("WHERE")
    checkForDupsQuery.append("  c.uid={uid}")
    checkForDupsQuery.append("RETURN")
    checkForDupsQuery.append("  COUNT(c) AS cnt")

    createResQuery = []
    createResQuery.append("CREATE")
    createResQuery.append("  (c: resource {")
    createResQuery.append("    uid:{uid},")
    createResQuery.append("    title:{title},")
    createResQuery.append("    desc:{desc},")
    createResQuery.append("    url:{url},")
    createResQuery.append("    author:{author},")
    createResQuery.append("    addedBy:{addedBy},")
    createResQuery.append("    addedByUrl:{addedByUrl},")
    createResQuery.append("    time:{time},")
    createResQuery.append("    type:{type},")
    createResQuery.append("    isPrivate:{isPrivate},")
    createResQuery.append("    isChildFriendly:{isChildFriendly},")
    createResQuery.append("    isNonFree:{isNonFree}")
    createResQuery.append("  })")

    return (data, {
      "checkForDupsQuery": "\n".join(checkForDupsQuery),
      "createResQuery": "\n".join(createResQuery)
    })

  def getTopics(self):
    data = [{
      "uid": "AqJmuGPTOS",
      "title": "Philosophy",
      "relationships": []
    }, {
      "uid": "tdN2eOgzP8",
      "title": "Existentialism",
      "relationships": []
    }, {
      "uid": "jHH0GP3zPj",
      "title": "Ethics",
      "relationships": []
    }, {
      "uid": "6cWUTstiib",
      "title": "Logic",
      "relationships": []
    }, {
      "uid": "iTxRtBW011",
      "title": "Nietzsche",
      "course": True,
      "relationships": []
    }, {
      "uid": "XUMEQd9Ash",
      "title": "Absurdism",
      "course": True,
      "relationships": []
    }, {
      "uid": "PiKeHsRS2V",
      "title": "History of Existentialism",
      "course": True,
      "relationships": []
    }]

    checkForDupsQuery = []
    checkForDupsQuery.append("MATCH")
    checkForDupsQuery.append("  (c:topic)")
    checkForDupsQuery.append("WHERE")
    checkForDupsQuery.append("  c.uid={uid}")
    checkForDupsQuery.append("RETURN")
    checkForDupsQuery.append("  COUNT(c) AS cnt")

    createTopQuery = []
    createTopQuery.append("CREATE")
    createTopQuery.append("  (c: topic {")
    createTopQuery.append("    uid:{uid},")
    createTopQuery.append("    title:{title},")
    createTopQuery.append("    course:{course}")
    createTopQuery.append("  })")

    return (data, {
      "checkForDupsQuery": "\n".join(checkForDupsQuery),
      "createTopQuery": "\n".join(createTopQuery)
    })

  def build(self):
    c = conf.Conf()
    vars = c.get('db') 
    g = Graph(vars["url"] + str(vars["port"]) + vars["dir"])

    opportunitiesData, opportunitiesQueries = self.getOpportunities()
    for o in opportunitiesData:
      res = g.cypher.execute(opportunitiesQueries["checkForDupsQuery"], {
        "uid": o["uid"]
      })

      if res[0].cnt != 0:
        continue

      g.cypher.execute(opportunitiesQueries["createOppQuery"], {
        "uid": o["uid"],
        "title": o["title"],
        "desc": o["desc"],
        "url": o["url"],
        "author": o["author"],
        "addedBy": o["addedBy"],
        "addedByUrl": o["addedByUrl"],
        "time": o["time"],
        "type": o["type"],
        "isPrivate": o["isPrivate"],
        "isChildFriendly": o["isChildFriendly"],
        "isNonFree": o["isNonFree"]
      })

    resourcesData, resourcesQueries = self.getResources()
    for r in resourcesData:
      res = g.cypher.execute(resourcesQueries["checkForDupsQuery"], {
        "uid": r["uid"]
      })

      if res[0].cnt != 0:
        continue

      g.cypher.execute(resourcesQueries["createResQuery"], {
        "uid": r["uid"],
        "title": r["title"],
        "desc": r["desc"],
        "url": r["url"],
        "author": r["author"],
        "addedBy": r["addedBy"],
        "addedByUrl": r["addedByUrl"],
        "time": r["time"],
        "type": r["type"],
        "isPrivate": r["isPrivate"],
        "isChildFriendly": r["isChildFriendly"],
        "isNonFree": r["isNonFree"]
      })

    topicsData, topicsQueries = self.getTopics()
    for t in topicsData:
      res = g.cypher.execute(topicsQueries["checkForDupsQuery"], {
        "uid": t["uid"]
      })

      if res[0].cnt != 0:
        continue

      g.cypher.execute(topicsQueries["createTopQuery"], {
        "uid": t["uid"],
        "title": t["title"],
        "course": t.get("course")
      })