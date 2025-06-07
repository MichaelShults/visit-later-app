import sqlite3
from flask import Flask, render_template, request, redirect

DATABASE = 'database/db.sqlite'


app = Flask(__name__)

# Database
#####################


def insert_into_db(url, title):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('INSERT INTO entries(url, title) VALUES (?, ?)', (url, title))
    conn.commit()
    conn.close()

def delete_from_db(url = None, title = None):
    if url or title:
        conn = sqlite3.connect(DATABASE)
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
        return True
    else:
        return False

def get_entries_from_db():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('SELECT url, title FROM entries')
    entries = cur.fetchall()
    conn.close()
    return entries   


def create_database():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('''
                Create TABLE IF NOT EXISTS entries (
                        id INTEGER PRIMARY KEY,
                        url TEXT,
                        title TEXT
                        )                       
                ''')
    conn.commit()
    conn.close()

create_database()
#########################


#### Routes

@app.route("/", methods = ["GET"])
def index():
    entries = get_entries_from_db()
    return render_template("index.html", entries = entries)


@app.route("/about", methods = ["GET"])
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html")

@app.route("/add", methods=["POST"])
def add_link():
    title = request.form.get("title")
    url = request.form.get("url")
    if title and not title.isspace() and url and not url.isspace():
        insert_into_db(url, title)
    else:
        print("Error, some fields are empty")
    return redirect("/")

@app.route("/delete", methods = ["POST"])
def delete_link():
    title = request.form.get("title")
    url = request.form.get("url")
    print("url = '", url, "' ")
    by_field = request.form.get("delete-by-field")
    if by_field == "url":
        title = None
    elif by_field == "title":
        url = None
    if url and url.isspace():
        url = "None"
    if title and title.isspace():
        title = "None"
    if delete_from_db(url=url, title=title):
        print("deletion operation successfull!")
    else:
        print("No arguments passed. Nothing deleted")
    return redirect("/")

######################
 

if __name__ == "__main__":
    app.run(host="localhost", debug=True)



    

