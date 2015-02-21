from py2neo import Graph
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
    g = Graph(vars["url"] + str(vars["port"]) + vars["dir"])

    opportunities = [{
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
      "isNonFree": True
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
      "isNonFree": False
    }]

    resources = [{
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
      "isNonFree": True
    }]

    topics = [{
      "uid": "AqJmuGPTOS",
      "title": "Philosophy"
    }, {
      "uid": "tdN2eOgzP8",
      "title": "Existentialism"
    }, {
      "uid": "jHH0GP3zPj",
      "title": "Ethics"
    }, {
      "uid": "6cWUTstiib",
      "title": "Logic"
    }, {
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
  
    q0 = []
    q0.append("MATCH")
    q0.append("  (c:opportunity)")
    q0.append("WHERE")
    q0.append("  c.uid={uid}")
    q0.append("RETURN")
    q0.append("  COUNT(c) AS cnt")

    q1 = []
    q1.append("CREATE")
    q1.append("  (c: opportunity {")
    q1.append("    uid:{uid},")
    q1.append("    title:{title},")
    q1.append("    desc:{desc},")
    q1.append("    url:{url},")
    q1.append("    author:{author},")
    q1.append("    addedBy:{addedBy},")
    q1.append("    addedByUrl:{addedByUrl},")
    q1.append("    time:{time},")
    q1.append("    type:{type},")
    q1.append("    isPrivate:{isPrivate},")
    q1.append("    isChildFriendly:{isChildFriendly},")
    q1.append("    isNonFree:{isNonFree}")
    q1.append("  })")

    q2 = []
    q2.append("CREATE")
    q2.append("  (c: resource {")
    q2.append("    uid:{uid},")
    q2.append("    title:{title},")
    q2.append("    desc:{desc},")
    q2.append("    url:{url},")
    q2.append("    author:{author},")
    q2.append("    addedBy:{addedBy},")
    q2.append("    addedByUrl:{addedByUrl},")
    q2.append("    time:{time},")
    q2.append("    type:{type},")
    q2.append("    isPrivate:{isPrivate},")
    q2.append("    isChildFriendly:{isChildFriendly},")
    q2.append("    isNonFree:{isNonFree}")
    q2.append("  })")

    q3 = []
    q3.append("CREATE")
    q3.append("  (c: topic {")
    q3.append("    uid:{uid},")
    q3.append("    title:{title},")
    q3.append("    course:{course}")
    q3.append("  })")

    for o in opportunities:
      res = g.cypher.execute("\n".join(q0), {
        "uid": o["uid"]
      })

      if res[0].cnt != 0:
        continue

      g.cypher.execute("\n".join(q1), {
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

    for r in resources:
      res = g.cypher.execute("\n".join(q0), {
        "uid": r["uid"]
      })

      if res[0].cnt != 0:
        continue

      g.cypher.execute("\n".join(q2), {
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

    for t in topics:
      res = g.cypher.execute("\n".join(q0), {
        "uid": t["uid"]
      })

      if res[0].cnt != 0:
        continue

      g.cypher.execute("\n".join(q3), {
        "uid": t["uid"],
        "title": t["title"],
        "course": t.get("course")
      })