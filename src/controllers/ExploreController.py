from flask import render_template

class ExploreController:
  def index(self):
    return render_template('explore.jade', title='Explore Page', msg='test')
