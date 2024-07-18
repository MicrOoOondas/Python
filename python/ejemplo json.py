import json # Datos JSON


datos = {
    "nombre": "esteban",
    "edad": 25,
    "comuna": "santiago",
    "estudios": ["Duoc Uc"]
}

Regiones = {
    "Region": "arica y parinacota",
    "Comunas": ["iquique", "alto hospicio"],
}


with open("Pruebaw.json","w") as archjson:
    json.dump(datos, archjson)
    json.dump(Regiones, archjson)