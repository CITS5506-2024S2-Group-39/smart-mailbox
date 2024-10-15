import sqlite3
from flask import g
from config import DATABASE
import json


# Function to get database connection
def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# Function to execute and save changes to the database
def save_to_db(query, params=()):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(query, params)
    db.commit()
    return cursor.lastrowid


# Function to retrieve data from the database
def get_from_db(query, params=()):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    return [
        dict((cursor.description[i][0], value) for i, value in enumerate(row))
        for row in rows
    ]


def get_events_from_db():
    events = get_from_db("SELECT * FROM events ORDER BY id DESC")
    for event in events:
        data = event["data"]
        data = json.loads(data)
        event["data"] = data
    return events


def get_events_after_id_from_db(id: int):
    events = get_from_db("SELECT * FROM events WHERE id > ? ORDER BY id DESC", (id,))
    for event in events:
        data = event["data"]
        data = json.loads(data)
        event["data"] = data
    return events


def get_event_from_db(id: int):
    events = get_from_db("SELECT * FROM events WHERE id=?", (id,))
    (event,) = events
    data = event["data"]
    data = json.loads(data)
    event["data"] = data
    return event


def update_event_to_db(id: int, data: dict):
    data = json.dumps(data)
    save_to_db("UPDATE events SET data=? WHERE id=?", (data, id))


def save_event_to_db(type: str, time: str, data: dict):
    data = json.dumps(data)
    return save_to_db(
        "INSERT INTO events (time, type, data) VALUES (?, ?, ?)", (time, type, data)
    )


def get_setting_item(key, default):
    rows = get_from_db(f"SELECT * FROM settings WHERE key = '{key}'")
    if not rows:
        return default
    (row,) = rows
    return row["value"]
