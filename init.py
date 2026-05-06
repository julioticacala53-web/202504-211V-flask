import sqlite3

connection = sqlite3.connect("basedatos.db")

with open("schema.sql", "w") as f:
    f.write("""
DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
""")

with open("schema.sql", "r") as f:
    connection.executescript(f.read())


def insert_data(title, content):
    connection = sqlite3.connect("basedatos.db")
    cur = connection.cursor()

    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
    connection.commit()
    connection.close()


insert_data("primer post", "content del primer post")
insert_data("primer post", "content del primer post")
