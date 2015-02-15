### NOTE: this model is simply using hard coded test data
### for purposes of PoC... will eventually be wired up to Neo4J
class LearningModel:
  def selectLearningInfo(self, uid):
    res = {}

    if uid == "iTxRtBW011":
      res["rows"] = {
        "opportunities": [{
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
        }],
        "resources": [{
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
      }
    else:
      return (None, {"err": "No learning data found"})

    return (res, None)