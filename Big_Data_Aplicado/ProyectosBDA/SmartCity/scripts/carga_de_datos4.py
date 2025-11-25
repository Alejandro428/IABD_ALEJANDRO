import requests
import random
import time

# URL de Orion Context Broker
url_entities = "http://localhost:1026/v2/entities"
headers = {
    "Content-Type": "application/json"
}

# Entidades que vamos a actualizar
entidades = [
    "Agua01",
    "MedidorCO201",
    "MedidorTemp01"
]

# Número de actualizaciones por atributo
num_updates = 400

# Función para enviar actualización PATCH a Orion
def actualizar_entidad(entidad_id, atributos):
    url_patch = f"{url_entities}/{entidad_id}/attrs"
    response = requests.patch(url_patch, headers=headers, json=atributos)
    if response.status_code == 204:
        print(f"{entidad_id} actualizado correctamente.")
    else:
        print(f"Error actualizando {entidad_id}: {response.status_code} - {response.text}")

# Loop para enviar actualizaciones masivas
for entidad_id in entidades:
    for i in range(num_updates):
        if entidad_id == "Agua01":
            atributos = {
                "temperatura": {"type": "Number", "value": round(random.uniform(0, 50), 2)},
                "cloro": {"type": "Number", "value": round(random.uniform(0, 10), 2)}
            }
        elif entidad_id == "MedidorCO201":
            atributos = {
                "co2": {"type": "Number", "value": round(random.uniform(300, 1000), 2)}
            }
        elif entidad_id == "MedidorTemp01":
            atributos = {
                "temperatura": {"type": "Number", "value": round(random.uniform(0, 50), 2)},
                "humedad": {"type": "Number", "value": round(random.uniform(0, 100), 2)}
            }
        actualizar_entidad(entidad_id, atributos)
        time.sleep(0.05)  # Pausa pequeña para no saturar el broker
