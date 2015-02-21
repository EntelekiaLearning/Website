from flask import Flask, jsonify
from controllers.HomepageController import HomepageController
from controllers.ExploreController import ExploreController
from controllers.TestDatabaseBuilderController import TestDatabaseBuilderController
import argparse

parser = argparse.ArgumentParser(description='Entelekia')
parser.add_argument('--devel', help='development mode', required=False)
args = parser.parse_args()

app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

if args.devel != None and args.devel.lower() != "false":
  print "enabling debug / live reload mode..."
  app.debug = True

  print "building up test data..."
  TestDatabaseBuilderController().build()

@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
  return app.send_static_file(path)

@app.route('/api/v1/test', methods=['GET'])
def test():
  return jsonify(status=1)

@app.route('/', methods=['GET'])
def homepage():
  return HomepageController().index()

@app.route('/explore', methods=['GET'])
def explore():
  return ExploreController().index()

@app.route('/api/v1/explore/topics/<uid>', methods=['GET'])
def apiExploreTopics(uid):
  code, res = ExploreController().getTopics(uid)
  return jsonify(res), code

@app.route('/api/v1/explore/learninginfo/<uid>', methods=['GET'])
def apiExploreLearningInfo(uid):
  code, res = ExploreController().getLearningInfo(uid)
  return jsonify(res), code

if __name__ == '__main__':
  app.run()
