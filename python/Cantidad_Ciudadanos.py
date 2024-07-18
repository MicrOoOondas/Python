'''Despliega la cantidad de ciudadanos ingresados según su nacionalidad'''
ciudadanos={}
while True:
    print('1.- Peruano')
    print('2.- Colombiano')
    print('3.- Venezolano')
    print('4.- Otro')
    print('5.- Salir')
    opc=input('Ingrese Opción:= ')
    if opc=='1':
        ciudadanos['Peruanos']=ciudadanos.get('Peruanos',0)+1
    elif opc=='2':
        ciudadanos['Colombianos']=ciudadanos.get('Colombianos',0)+1
    elif opc=='3':
        ciudadanos['Venezolanos']=ciudadanos.get('Venzolanos',0)+1
    elif opc=='4':
        ciudadanos['Otros']=ciudadanos.get('Otros',0)+1
    elif opc=='5':
        break
    else:
        print('Opcion Incorrecta')
for ciudadano,cantidad in ciudadanos.items():
    print(ciudadano,cantidad)
