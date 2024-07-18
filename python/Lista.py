milista=[1,2,3,4,5,6]
#print(milista[3])
"""for elemento in milista:
    print(elemento)"""
milista2=['oscar','maria','jose','paz']
"""for elemento in milista2:
    print(elemento)"""
milista3=[milista,milista2]
#print(milista3[1][2])
"""for elem in milista3:
    print(elem)"""
for i in range(len(milista3)):
    for j in range(len(milista3[i])):
        print(milista3[i][j])
