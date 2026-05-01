from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index") # controlador
def hello():
    base_de_datos = ["jorge", "pepe", "juanito"] # Modelos
    return render_template(template_name_or_list="index.html", datos=base_de_datos ) # view
