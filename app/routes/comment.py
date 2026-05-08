from flask import Blueprint, render_template

# Definimos el blueprint para posts
comments_bp = Blueprint('comments', __name__, url_prefix='/comments')


@comments_bp.route("/list")
def get_all_comments():
    return render_template("comment/list.html")

