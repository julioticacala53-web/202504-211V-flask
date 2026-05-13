import sqlite3
from flask import g

def get_db_connection():
    if 'db' not in g:
        g.db = sqlite3.connect("basedatos.db")
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db_connection(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    conn = sqlite3.connect("basedatos.db")
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
        """
    )
    conn.commit()
    conn.close()