import os
'''import funciones as f'''
os.system('cls')
#aqui vendrian las funciones
# 1er ejemplo de funcion
'''def sumar():
    num1=5
    num2=7
    return num1+num2'''

#2do ejemplo de funcion
'''#funcion suma
def sumar(num1,num2):
    return num1 + num2
#funcion resta
def restar(num1,num2):
    return num1 - num2
#funcion multiplicacion
def multi(num1,num2):
    return num1 * num2
#funcion divicion
def divi(num1,num2):
    return num1 / num2'''

#ejemplo de funcion 3

def ingreso_num(mensaje):
    while True:
        num=input(mensaje+": ")
        if num.isdigit():
            return int(num)
        else:
            print("Ingrese numero")
def ingreso_texto(mensaje):
    while True:
        texto=input(mensaje+": ")
        if texto.isalpha():
            return texto
        else:
            print("Ingrese solo texto")
def validar_rango(numero,valor_inferior,valor_superior):
    if numero>=valor_inferior and numero<=valor_superior:
        return True
    else:
        return False

# programa ejemplo funciones
'''n1=2
n2=3
print("la suma es= ",f.sumar(n1,n2))
print("la resta es= ",f.restar(n1,n2))
print("la multi es= ",f.multi(n1,n2))
print("la divi es= ",f.divi(n1,n2))'''

# programa ejemplo ingreso nombres y numeros

nombre= ingreso_texto("Ingrese Nombre de la Persona")
apellido= ingreso_texto("Ingrese Apellido de la Persona")
edad= ingreso_num("Ingresar Edad de la Persona")