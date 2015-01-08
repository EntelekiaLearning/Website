from flask import Flask, jsonify
from controllers.ExploreController import ExploreController

app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
  return app.send_static_file(path)

@app.route('/api/v1/test', methods=['GET'])
def test():
  return jsonify(status=1)

@app.route('/explore', methods=['GET'])
def index():
  return ExploreController().index()

if __name__ == '__main__':
  app.run()
