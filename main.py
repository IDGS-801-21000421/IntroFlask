
from flask import Flask, render_template # type: ignore

app = Flask(__name__)

@app.route("/")
def index():
    
    titulo="Curso de flask"
    lista=["Luis","Juan","Pedro"]
    
    return render_template("index.html", titulo=titulo, lista=lista)


@app.route("/user/<string:user>")
def user(user):
    return f"<h1>¡Hola, {user}!</h1>"


@app.route("/numero/<int:n>")
def numero(n):
    return f"<h1>¡El número es, {n}!</h1>"


@app.route("/suma/<int:n1>/<int:n2>")
def suma(n1, n2):
    return f"<h1>¡La suma es, {n1 + n2}!</h1>"

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")


@app.route("/default/")
@app.route("/default/<string:param>")
def funcion(param="Juan"):
    return f"<h1>¡Hola, {param}!</h1>"


if __name__ == "__main__":
    app.run(debug=True,port=3000)