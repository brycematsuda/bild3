from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack
import requests, os
from bs4 import BeautifulSoup

# configuration
try:
	DATABASE = 'simply-billboard.db'
	DEBUG = True
	SECRET_KEY = 'development key'
	USERNAME = 'admin'
	PASSWORD = 'default'
except ImportError:
	SECRET_KEY = os.environ.get('SECRET_KEY') 
	USERNAME = os.environ.get('USERNAME')
	PASSWORD = os.environ.get('PASSWORD')
	DEBUG = False

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

def init_db():
    """Creates the database tables."""
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        import billboard
        chart = billboard.ChartData('hot-100', None, True, True)
        for x in range(0, 100):
          db.execute('INSERT INTO billboard100 (title, artist, album, peakPos, lastPos, weeks, rankChange) VALUES (?, ?, ?, ?, ?, ?, ?)',
          [chart[x].title, chart[x].artist, chart[x].album, chart[x].peakPos, chart[x].lastPos, chart[x].weeks, chart[x].change])
        db.commit()


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        sqlite_db = sqlite3.connect(app.config['DATABASE'])
        sqlite_db.row_factory = sqlite3.Row
        top.sqlite_db = sqlite_db

    return top.sqlite_db


@app.teardown_appcontext
def close_db_connection(exception):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()

@app.route('/')
def billboard():
  db = get_db()
  cur = db.execute('SELECT * FROM billboard100 ORDER BY rank')
  entries = cur.fetchall()
  return render_template('billboard.html', entries=entries)

if __name__ == '__main__':
	init_db()
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
