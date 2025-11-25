import requests
url = "http://localhost:1026/v2/entities"

headers = {
    "Content-Type": "application/json"
}

entidades = [
    {
        "id": "Agua01",   
        "type": "AguaAg",       
        "temperatura": {        
            "type": "Number",
            "value": 4
        },
        "cloro": {           
            "type": "Number",
            "value": 4
        },
        "localizacion": {       
            "type": "String",
            "value": "Valencia"
        }
    },
    {
        "id": "MedidorCO201",  
        "type": "MedidorCO2",
        "co2": {                 
            "type": "Number",
            "value": 5
        },
        "localizacion": {      
            "type": "String",
            "value": "Valencia"
        }
    },
    {
        "id": "MedidorTemp01",  
        "type": "MedidorTemperatura",
        "temperatura": {      
            "type": "Number",
            "value": 5
        },
        "humedad": {           
            "type": "Number",
            "value": 5
        },
        "localizacion": {       
            "type": "String",
            "value": "Valencia"
        }
    }
]

def crear_entidad_si_no_existe(entidad):
    try:
        response_get = requests.get(f"{url}/{entidad['id']}")
    except requests.exceptions.RequestException as e:
        print(f" No se pudo conectar a Orion para comprobar {entidad['id']}: {e}")
        return 

    if response_get.status_code == 404:
        try:
            response_post = requests.post(url, headers=headers, json=entidad)
        except requests.exceptions.RequestException as e:
            print(f" No se pudo crear la entidad {entidad['id']}: {e}")
            return
        
        if response_post.status_code == 201:
            print(f" Entidad {entidad['id']} creada correctamente.")
        else:
            print(f"Error creando entidad {entidad['id']}: {response_post.status_code} - {response_post.text}")
    
    elif response_get.status_code == 200:
        print(f"Entidad {entidad['id']} ya existe, no se crea de nuevo.")
    
    else:
        print(f"Error comprobando entidad {entidad['id']}: {response_get.status_code} - {response_get.text}")

for entidad in entidades:
    crear_entidad_si_no_existe(entidad)
