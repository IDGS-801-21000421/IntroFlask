
from flask import Flask, render_template, request # type: ignore

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
    return render_template("ejemplo2.html",)


@app.route("/operacionesbas", methods=["POST", "GET"])
def operaciones():
    
    resultado = 0

    if request.method == "POST":
        n1 = int(request.form.get("n1"))
        n2 = int(request.form.get("n2"))
        operacion = request.form.get("operacion")

        if operacion == "1":
            resultado = n1 + n2
        elif operacion == "2":
            resultado = n1 - n2
        elif operacion == "3":
            resultado = n1 * n2
        elif operacion == "4":
            resultado = n1 / n2
    else:
        resultado = resultado

    return render_template("OperacionesBas.html", resultado=resultado)


@app.route("/cinepolis", methods=["GET", "POST"])
def cinepolis():
    total = ""
    error = ""
    nombre = ""
    personas = ""
    tarjeta = ""
    boletos = ""
    
    if request.method == "POST":
        nombre = request.form["nombre"]
        personas = request.form["personas"]
        tarjeta = request.form.get("tarjeta", "")
        boletos = request.form["boletos"]

        personas = int(personas)
        boletos = int(boletos)
        precio = 12
        descuento = 0

        if boletos > 7 * personas:
            error = "❌ No puede comprar más de 7 boletos por persona ❌"
            return render_template("cinepolis.html", total=total, error=error,
            nombre=nombre, personas=personas, tarjeta=tarjeta, boletos=boletos)

        if boletos > 5:
            descuento = 0.15
        elif boletos > 2:
            descuento = 0.10

        total = boletos * precio * (1 - descuento)

        if tarjeta == "si":
            total = total * 0.90

        total = round(total, 2)
    
    return render_template("cinepolis.html", total=total, error=error,
    nombre=nombre, personas=personas, tarjeta=tarjeta, boletos=boletos)





# @app.route("/resultado", methods=["POST"])
# def resultado():
    
#     n1 = request.form.get("n1")
#     n2 = request.form.get("n2")    
 
#     return "La suma de {} + {} es {}".format(n1,n2,str(int(n1)+int(n2)))
    
    


@app.route("/default/")
@app.route("/default/<string:param>")
def funcion(param="Juan"):
    return f"<h1>¡Hola, {param}!</h1>"


if __name__ == "__main__":
    app.run(debug=True,port=3000)