from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    """Sirve la página principal de la calculadora."""
    return render_template("index.html")


# TODO (equipo): esta ruta es donde va a vivir la lógica de cálculo real.
# Cuando los botones de números y operadores estén conectados en el JS,
# esta ruta recibe la operación y devuelve el resultado.
@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.get_json()
    # TODO (equipo): leer data["num1"], data["num2"], data["operacion"]
    #                 y devolver el resultado calculado en Python.
    return jsonify({"resultado": None})


if __name__ == "__main__":
    app.run(debug=True)
