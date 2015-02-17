from flask import Flask, jsonify
from controllers.HomepageController import HomepageController
from controllers.ExploreController import ExploreController
import argparse

parser = argparse.ArgumentParser(description='Entelekia')
parser.add_argument('-t','--use_test_data', help='builds up initial test data', required=False)
args = parser.parse_args()

app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

if args.use_test_data != None:
  #TODO should point to a test model that builds up the neo4j data
  from neo4jrestclient.client import GraphDatabase
  gdb = GraphDatabase("http://localhost:7474/db/data/")
  print "building up graph db test data..."

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
