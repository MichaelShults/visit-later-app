import sqlite3
from flask import Flask, render_template, g, current_app

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

######################
 

if __name__ == "__main__":
    app.run(host="localhost", debug=True)



    

