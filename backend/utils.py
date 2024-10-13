import sqlite3
from flask import g

DATABASE = 'mailbox.db'

# Function to get database connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Function to execute and save changes to the database
def save_to_db(query, params=()):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(query, params)
    db.commit()

# Function to retrieve data from the database
def get_from_db(query, params=()):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    return [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in rows]
