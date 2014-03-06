 from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'rymate_blog.db'),
    DEBUG=True,
    SECRET_KEY='wow, much secure, such develop'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# DATABASE STUFF
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Creates the database tables."""
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/admin/post_create')
def make_post():
    return render_template("create_post.html")
    
@app.route('/')
def homepage():
    if os.path.isfile('rymate_blog.db'):
        init_db()
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
