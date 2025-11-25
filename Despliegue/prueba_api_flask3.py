from flask import Flask, jsonify, url_for

# Crear la aplicación Flask
app = Flask(__name__)

# Lista de tareas predefinidas
tareas = [
    {"id": 1, "tarea": "Aprender Flask", "completada": False},
    {"id": 2, "tarea": "Hacer ejercicio", "completada": True},
    {"id": 3, "tarea": "Leer un libro", "completada": False}
]

# Ruta raíz
@app.route("/")
def index():
    return "index"

# Ruta login
@app.route("/login")
def login():
    return "login"

# Ruta de perfil con parámetro dinámico
@app.route("/user/<username>")
def profile(username):
    return f"{username}'s profile"

# Saludo personalizado
@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"Hola, {nombre}!"

# NUEVO: Endpoint que devuelve la lista de tareas en JSON
@app.route("/tareas")
def obtener_tareas():
    # jsonify convierte un diccionario o lista en formato JSON
    return jsonify({"tareas": tareas})


# Ejecutar la aplicación (modo desarrollo)
if __name__ == "__main__":
    app.run(debug=True)
