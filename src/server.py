from flask import Flask, jsonify
from controllers.HomepageController import HomepageController
from controllers.ExploreController import ExploreController

app = Flask(__name__)
app.debug = True
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

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

if __name__ == '__main__':
  app.run()
