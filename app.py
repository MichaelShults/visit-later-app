import sqlite3
from flask import Flask, render_template, redirect, g
from forms.add_delete_forms import AddItemForm, DeleteItemsForm, MISSING_FIELD_STRINGS
import os

DATABASE = 'database/db.sqlite'

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

######## Database ########################

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def insert_into_db(url, title):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO entries(url, title) VALUES (?, ?)', (url, title))
    conn.commit()
    conn.close()

def delete_from_db(url = None, title = None):
    conn = get_db()
    cur = conn.cursor()
    query = "DELETE FROM entries WHERE "
    if url and title:
        query += 'url = (?) AND title = (?)'
        cur.execute(query, (url, title))
    elif url and not title:
        query += 'url = (?)'
        cur.execute(query, (url,))
    else:
        query += 'title = (?)'
        cur.execute(query, (title,))
    conn.commit()
    conn.close()

def get_entries_from_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT url, title FROM entries')
    entries = cur.fetchall()
    conn.close()
    return entries

def create_entries_table():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS entries (
                        id INTEGER PRIMARY KEY,
                        url TEXT,
                        title TEXT
                        )                       
                ''')
    conn.commit()
    conn.close()

with app.app_context():
    create_entries_table()

########################################


######## Routes ########################

@app.route("/", methods = ["GET"])
def index():
    entries = get_entries_from_db()
    add_item_form = AddItemForm()
    delete_items_form = DeleteItemsForm()
    delete_items_form.by_field.default = 'title'
    delete_items_form.process()
    return render_template("index.html",
                            entries = entries,
                            add_item_form = add_item_form,
                            delete_items_form =  delete_items_form,
                            error_strings={"missing_fields":MISSING_FIELD_STRINGS})


@app.route("/about", methods = ["GET"])
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html")

@app.route("/add", methods=["POST"])
def add_link():
    form = AddItemForm()
    if form.validate_on_submit():
        title = form.title.data
        url = form.url.data
        insert_into_db(url=url, title=title)
    return redirect("/")

@app.route("/delete", methods = ["POST"])
def delete_link():
    form = DeleteItemsForm()
    if form.validate_on_submit():
        title = form.title.data
        url = form.url.data
        by_field = form.by_field.data
        delete_from_db(url=url, title=title)
    return redirect("/")

######################################
 

if __name__ == "__main__":
    app.run(host="localhost", debug=True)



    

