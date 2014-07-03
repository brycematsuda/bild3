from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack

# configuration
DATABASE = 'malid3.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


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



"""Display all entries in database"""
@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('SELECT * FROM entries ORDER BY id DESC')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


@app.route('/add')
def add():
	return render_template('add.html')

@app.route('/post', methods=['POST'])
def add_entry():
  if not session.get('logged_in'):
    abort(401)

  db = get_db()
  error = None
  if request.form.get('title', None) == '':
    error = 'Song title cannot be blank.'
  elif all_new_empty() is True:
    error = 'You must fill in at least one tag or notes.'
  elif request.form.get('update') is None:
    error = 'You must note if you\'ve updated the information or not.'
  else:
    db.execute('INSERT INTO entries (title, artist, album, update_status, new_title, new_artist, new_album, notes) VALUES (?, ?, ?, ?, ?, ?, ? ,?)',
    [request.form['title'], request.form['artist'], request.form['album'], request.form['update'],
    request.form['new_title'], request.form['new_artist'], request.form['new_album'], request.form['notes']])
    db.commit()
    flash('Entry was successfully added')
    return redirect(url_for('show_entries'))
  return render_template('add.html', error=error)

def all_new_empty():
  all_empty = False
  if ((request.form.get('new_title', None) == '') and
     (request.form.get('new_artist', None) == '') and
     (request.form.get('new_album', None) == '') and
     (request.form.get('notes', None) == '')):
     all_empty = True
  return all_empty

@app.route('/delete/<int:entry_id>')
def delete(entry_id):
  if not session.get('logged_in'):
    abort(401)

  db = get_db()
  entry_id = str(entry_id)
  db.execute('DELETE from entries WHERE id =' + entry_id)
  db.commit()
  flash('Entry successfully removed')
  return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were successfully logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were successfully logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
	init_db()
	app.run()
