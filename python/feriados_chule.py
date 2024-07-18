import os
import json

os.system("cls")
with open("feriados_chile.json",endcoding="utf-8") as arch:
    lista_datos=json.load(arch)
p={}
for elem in lista_datos:
    elem.pop("comentarios")
    if"leyes" in elem.keys():
        elem.pop("leyes")
for elem in lista_datos:
    for clave,valor in elem.item():