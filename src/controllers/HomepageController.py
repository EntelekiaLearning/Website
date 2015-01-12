from flask import render_template

class HomepageController:
  def index(self):
    return render_template('homepage.jade', title='homepage')