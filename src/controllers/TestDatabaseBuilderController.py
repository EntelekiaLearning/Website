from models.TestDatabaseBuilderModel import TestDatabaseBuilderModel

class TestDatabaseBuilderController:
  def build(self):
    t = TestDatabaseBuilderModel()
    t.build()
    