import os
os.system('cls')
dic_region={'Tarapacá':'Norte',
            'Antofagasta':'Norte',
            'Atacama':'Norte',
            'Coquimbo':'Norte',
            'Valparaíso':'Central',
            'Libertador General Bernardo OHiggins':'Central',
            'Maule':'Central',
            'Biobío':'Central',
            'La Araucanía':'Sur',
            'Los Lagos':'Sur',
            'Aysén del General Carlos Ibáñez del Campo':'Sur',
            'Magallanes y de la Antártica Chilena':'Sur',
            'Metropolitana de Santiago':'Central',
            'Los Ríos':'Sur',
            'Arica y Parinacota':'Norte',
            'Ñuble':'Sur'}
lis_region=list(dic_region)
dic_zona={"Norte":0,"Central":0,"Sur":0}
dic_est_civil={'Soltera':0,'Casada':0,'Divorciada':0,'Viuda':0}
while True:
    i=1
    for reg in lis_region:
        print(i,'.-',reg)
        i+=1
    print(i,'.- Terminar')
    opc=input('Ingrese Opcion: ')
    if opc.isdigit():
        indice=int(opc)-1
        if 0<= indice <=15:
            while True:
                i=1
                for estc in dic_est_civil.keys():
                    print(i,'.-',estc)
                    i+=1
                opc1=input('Ingrese Opcion: ')
                if opc1 in ['1','2','3','4']:
                    while True:
                        try:
                            cantidad=int(input('Ingrese Cantidad de Personas: '))
                            if cantidad>=0 and cantidad<=5000:
                                break
                            else:
                                print('Cantidad entre 0 y 5000')
                        except:
                            print('La cantidad debe ser un número')
                    if opc1=='1':
                        dic_est_civil['Soltera']=dic_est_civil.get('Soltera')+cantidad
                    elif opc1=='2':
                        dic_est_civil['Casada']=dic_est_civil.get('Casada')+cantidad
                    elif opc1=='3':
                        dic_est_civil['Divorciada']=dic_est_civil.get('Divorciada')+cantidad
                    elif opc1=='4':
                        dic_est_civil['Viuda']=dic_est_civil.get('Viuda')+cantidad
                else:
                    print('Opción entre 1 y 4')
            v_zona=dic_region.get(lis_region[indice])
            dic_zona[v_zona]=dic_zona.get(v_zona)+1
            print(dic_zona.get(v_zona))
        elif indice==16:
            break
        else:
            print('Debe digitar nùmero entre 1 y 17')
    else:
        print('Ingrese un número')