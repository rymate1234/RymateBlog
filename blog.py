import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)

@app.route('/admin/post_create')
def make_post():
    return render_template("create_post.html")
    
@app.route('/')
def homepage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
