from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # controlador
def root():
    return render_template("base.html" ) # view

@app.route("/index") # controlador
def index():
    base_de_datos = ["jorge", "pepe", "juanito"] # Modelos
    return render_template("index.html", datos=base_de_datos ) # view

@app.route("/home") # controlador
def home():
    return render_template("home.html") # view