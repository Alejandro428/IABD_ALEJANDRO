import requests

url_subs = "http://localhost:1026/v2/subscriptions"
headers = {"Content-Type": "application/json"}

subscription = {
    "description": "Suscripción para entidades Agua, CO2 y Temperatura",
    "subject": {
        "entities": [
            {"idPattern": ".*", "type": "AguaAg"},
            {"idPattern": ".*", "type": "MedidorCO2"},
            {"idPattern": ".*", "type": "MedidorTemperatura"}
        ],
        "condition": {
            "attrs": ["temperatura", "cloro", "co2", "humedad", "localizacion"]
        }
    },
    "notification": {
        "attrs": ["id", "temperatura", "cloro", "co2", "humedad", "localizacion"],
        "http": {"url": "http://quantumleap:8668/v2/notify"},
        "metadata": ["dateCreated", "dateModified"]
    }
}

# Crear la suscripción directamente
response = requests.post(url_subs, headers=headers, json=subscription)
if response.status_code == 201:
    print(" Suscripción creada correctamente.")
    print("Location:", response.headers.get("Location"))
else:
    print(f" Error creando suscripción: {response.status_code} - {response.text}")
