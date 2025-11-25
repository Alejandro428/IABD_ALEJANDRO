from flask import Flask, jsonify, url_for, request

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

# NUEVO: Endpoint que devuelve la lista de tareas en JSON
@app.route("/tasks")
def obtener_tareas():
    # jsonify convierte un diccionario o lista en formato JSON
    return jsonify({"tareas": tareas}, 200)


# NUEVO: Endpoint para agregar una tarea
@app.route("/tasks", methods=["POST"])
def agregar_tarea():
    # Obtener los datos JSON enviados
    nueva_tarea = request.get_json()

    # Validar que se envió la clave 'tarea'
    if not nueva_tarea or "tarea" not in nueva_tarea:
        return jsonify({"error": "Se requiere el campo 'tarea'"}), 400

    # Asignar un ID único
    siguiente_id = max(t["id"] for t in tareas) + 1 if tareas else 1
    tarea_creada = {
        "id": siguiente_id,
        "tarea": nueva_tarea["tarea"],
        "completada": False
    }

    # Agregar a la lista
    tareas.append(tarea_creada)

    # Devolver la tarea creada con código 201
    return jsonify(tarea_creada), 201


# Ejecutar la aplicación (modo desarrollo)
if __name__ == "__main__":
    app.run(debug=True)
