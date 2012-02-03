# vim:fileencoding=utf-8:

from flask import Flask, render_template, redirect
app = Flask(__name__)
app.debug = True

from google.appengine.api import users
from google.appengine.ext import db

import functools

def login_required(func):
  @functools.wraps(func)
  def decorated(*args, **kw):
    user = users.get_current_user()
    if user:
      return func(*args, **kw)
    return redirect(users.create_login_url())
  return decorated

def render(template, **kw):
  kw['user'] = users.get_current_user()
  kw['logout'] = users.create_logout_url('/')
  return render_template(template, **kw)

@app.route('/')
@login_required
def top():
  return render('top.html')
