import os
import funciones as f

os.system('cls')

# opciones menu lista

def menu(lista):
    while True:
        i=1
        for elem in lista:
            print(i,".-",elem)
            i+=1
            print(i,".- salir")
            opc=input("Ingrese Opcion: ")
            if opc.isdigit():
                opc_int=int(opc)
                if opc_int>=1 and opc_int<=i:
                    return opc_int
                else:
                    print("Debe Ingresar un n umero valido de entre 1 y",i)
            else:
                print("Ingrese solo Numeros")

#programa principal 

opciones=("Ingresar","listar","modificar","eliminar","consultar")
opcion=menu(opciones)

