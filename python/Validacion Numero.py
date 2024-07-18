import os
os.system('cls')
total=0
while True:
    cantidad=input('Ingrese cantidad: ')
    if cantidad.isdigit():
          cant=int(cantidad)
          if 1<=cant<=100: #Equivalente a: if cant>=1 and cant<=100:
            total+=cant # Equivalente a: total=total+cant
            print(total*5)
            break
          else:
              print('No cumple valores')
    else:
        print('Por favor un número')