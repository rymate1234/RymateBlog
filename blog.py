import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/admin/post_create')
def make_post():
    return render_template("create_post.html")
    
@app.route('/')
def homepage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
