from flask import Blueprint, render_template

# Definimos el blueprint para posts
base_bp = Blueprint('base', __name__, url_prefix='/')

@base_bp.route("/")
def root():
    return render_template("base.html")

@base_bp.route("/home")
def home():
    return render_template("home.html")