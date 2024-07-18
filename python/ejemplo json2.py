import os
import json

os.system("cls")
with open("Pruebaw.json", "r") as miarchjson:
    dic_json=json.load(miarchjson)
lista_regiones=dic_json.get("Regiones")
lista_regiones_tarapaca=lista_regiones[1]
print(lista_regiones_tarapaca)