palabra=input('Ingrese Palabra: ')
print(palabra)
lista=list(palabra)
lista2=lista.copy()
lista.reverse()
print(lista)
print(lista2)
if lista==lista2:
    print('Es palindromo')
else:
    print('No es palindromo')