import requests

url_entities = "http://localhost:1026/v2/entities"
headers = {
    "Content-Type": "application/json"
}

# Valores a actualizar en cada entidad
updates = {
    "Agua01": {
        "temperatura": {"type": "Number", "value": 12},
        "cloro": {"type": "Number", "value": 9}
    },
    "MedidorCO201": {
        "co2": {"type": "Number", "value": 6}
    },
    "MedidorTemp01": {
        "temperatura": {"type": "Number", "value": 8},
        "humedad": {"type": "Number", "value": 10}
    }
}

# Hacemos PATCH directamente a cada entidad
for entidad_id, attrs in updates.items():
    url_patch = f"{url_entities}/{entidad_id}/attrs"
    response = requests.patch(url_patch, headers=headers, json=attrs)
    if response.status_code == 204:
        print(f" Entidad {entidad_id} actualizada correctamente.")
    else:
        print(f" Error actualizando entidad {entidad_id}: {response.status_code} - {response.text}")
