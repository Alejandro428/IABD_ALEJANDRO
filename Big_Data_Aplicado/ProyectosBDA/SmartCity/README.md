# TAREA 1

# SENSORES:

* SENSORES 1:

    [
    {
        "id": {
            "type": "Number",
            "value": 1
        },
        "tipo": {
            "type": "String",
            "value": "medidor temperatura"
        },
        "atributos": {
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
    },
    {
        "id": {
            "type": "Number",
            "value": 2
        },
        "tipo": {
            "type": "String",
            "value": "medidor temperatura"
        },
        "atributos": {
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
    },
    {
        "id": {
            "type": "Number",
            "value": 3
        },
        "tipo": {
            "type": "String",
            "value": "medidor temperatura"
        },
        "atributos": {
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
    },
    {
        "id": {
            "type": "Number",
            "value": 4
        },
        "tipo": {
            "type": "String",
            "value": "medidor temperatura"
        },
        "atributos": {
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
    }
]


* SENSORES 2:

  [
    {
        "id": {
            "type": "Number",
            "value": 4
        },
        "tipo": {
            "type": "String",
            "value": "medidor co2"
        },
        "atributos": {
            "co2": {
                "type": "Number",
                "value": 5
            },
            "localizacion": {
                "type": "String",
                "value": "Valencia"
            }
        }
    },
    {
        "id": {
            "type": "Number",
            "value": 5
        },
        "tipo": {
            "type": "String",
            "value": "medidor co2"
        },
        "atributos": {
            "co2": {
                "type": "Number",
                "value": 5
            },
            "localizacion": {
                "type": "String",
                "value": "Valencia"
            }
        }
    },
    {
        "id": {
            "type": "Number",
            "value": 6
        },
        "tipo": {
            "type": "String",
            "value": "medidor co2"
        },
        "atributos": {
            "co2": {
                "type": "Number",
                "value": 5
            },
            "localizacion": {
                "type": "String",
                "value": "Valencia"
            }
        }
    }
]

* SENSORES 3:

  [
     {
        "id": {
            "type": "Number",
            "value": 7
        },
        "tipo": {
            "type": "String",
            "value": "medidor agua"
        },
        "atributos": {
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
        }
    },
     {
        "id": {
            "type": "Number",
            "value": 8
        },
        "tipo": {
            "type": "String",
            "value": "medidor agua"
        },
        "atributos": {
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
        }
    },
     {
        "id": {
            "type": "Number",
            "value": 9
        },
        "tipo": {
            "type": "String",
            "value": "medidor agua"
        },
        "atributos": {
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
        }
    }
]


TAREA 2

1. Creación de las 3 entidades:

Usando la API REST de Orion Context Broker, crearemos las 3 entidades que definimos en la Tarea
1: Diseño del ADN de los Sensores.

La llamada API enviará un POST a /v2/entities con el JSON de cada entidad.

############################################################################
############Esta actividad se encuentra en scripts/entidades1.py############
############################################################################

2. Creación de una suscripción:

Esta es la parte clave para el histórico. Crearemos una suscripción en Orion que "escucha" cualquier
cambio en nuestras entidades.

Cuando Orion detecte una actualización, enviará automáticamente una copia de la entidad
modificada al servicio QuantumLeap.

La suscripción se crea con un POST a /v2/subscriptions .

############################################################################
#########Esta actividad se encuentra en scripts/suscripciones2.py###########
############################################################################

############################################################################
######"EXTRA". HAY UNA PRUEBA DEL PATCH EN scripts/actualizacion3.py:#######
############################################################################

3. Carga de datos:

Ahora viene la carga de los datos masivos. Utilizaremos un script de Python con la API de Orion.

El script deberá enviar 400 actualizaciones por atributo a la API de Orion para cada una de
nuestras 3 entidades.

Cada vez que el script envíe una actualización, Orion hará dos cosas:
Actualizará el documento en MongoDB con el nuevo estado.
1 / 2
Debido a la suscripción, enviará una copia de los datos a QuantumLeap, que a su vez los
insertará en CrateDB como una nueva entrada de serie de tiempo.

########################################################################
######Esta actividad se encuentra en scripts/actualizacion3.py##########
########################################################################

4. Consulta Mongodb

Realiza una captura de pantalla con la consulta Mongodb a la coleccion de entidades en la que se
vean todos los atributos de las tres entidades

########################################################################
Esta actividad se encuentra en scripts/carga_de_datos4.py
########################################################################

5. Guarda toda la información en tu Repositorio de GitHub

Al final de la práctica, tendrás un sistema funcional donde puedes ver el estado actual de tus entidades en
MongoDB y consultar el historial completo en CrateDB.

########################################################################
Todas las imagenes de las pruebas se encuentran en imagenes_resultados
########################################################################




