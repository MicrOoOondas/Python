lista=[6,4,1,2,9,'Salomon']
for elemto in lista:
    print(elemto)
lista.append(12)
print(lista)
#lista.insert(2,'Sebastian')
for i in range(len(lista)):
    print(lista[i])
lista.remove('Salomon')
print(lista)
lista.reverse()
print(lista)
lista.sort()
print(lista)