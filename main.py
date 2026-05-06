from flask import Flask, redirect, render_template, request, url_for, abort
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("basedatos.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")  # controlador
def root():
    return render_template("base.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/post/list")
def get_all_posts():
    connection = get_db_connection()
    cur = connection.cursor()
    posts = cur.execute("SELECT * FROM posts;")
    return render_template("post/list.html", post_list=posts)


@app.route("/post/<int:post_id>")
def get_single_post(post_id):
    connection = get_db_connection()
    cur = connection.cursor()
    post = cur.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    print(post)
    if post is None:
        abort(404)
    return render_template("post/single.html", post_single=post)


@app.route("/post/create", methods=("GET", "POST"))
def create_post():
    if request.method == "GET":
        return render_template("post/create.html")
    if request.method == "POST":
        title = request.form["title_title"]
        content = request.form["content_content"]
        connection = get_db_connection()
        cur = connection.cursor()
        cur.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)", (title, content)
        )
        connection.commit()
        return redirect(url_for("get_all_posts"))
