from flask import Flask, url_for

# Crear la aplicación Flask
app = Flask(__name__)

# Definir rutas
@app.route("/")
def index():
    return "index"

@app.route("/login")
def login():
    return "login"

@app.route("/user/<username>")
def profile(username):
    return f"{username}'s profile"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"Hola, {nombre}!"

# Usar contexto de prueba para url_for
with app.test_request_context():
    print(url_for("index"))                       # Output: /
    print(url_for("login"))                       # Output: /login
    print(url_for("login", next="/"))             # Output: /login?next=/
    print(url_for("profile", username="Alexander AJ PRIME"))  
    print(url_for("saludo", nombre="Alexander AJ PRIME"))  

    # Output: /user/Alexander%20AJ%20PRIME

# Ejecutar la aplicación (modo desarrollo)
if __name__ == "__main__":
    app.run(debug=True)