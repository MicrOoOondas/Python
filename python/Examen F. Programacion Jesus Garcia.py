import random
import csv

# Lista de empleados
empleados = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Soto", 
             "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

# Asignar sueldos aleatorios
def asignar_sueldos_aleatorios():
    sueldos = [random.randint(300000, 2500000) for _ in range(len(empleados))]
    return dict(zip(empleados, sueldos))

# Clasificar sueldos
def clasificar_sueldos(sueldos):
    menores_800k = {k: v for k, v in sueldos.items() if v < 800000}
    entre_800k_2m = {k: v for k, v in sueldos.items() if 800000 <= v <= 2000000}
    superiores_2m = {k: v for k, v in sueldos.items() if v > 2000000}
    return menores_800k, entre_800k_2m, superiores_2m

# Ver estadísticas
def ver_estadisticas(sueldos):
    sueldos_valores = list(sueldos.values())
    sueldo_mas_alto = max(sueldos_valores)
    sueldo_mas_bajo = min(sueldos_valores)
    promedio_sueldos = int(sum(sueldos_valores) / len(sueldos_valores))
    media_geometrica = int((sueldo_mas_alto * sueldo_mas_bajo) ** 0.5)
    return sueldo_mas_alto, sueldo_mas_bajo, promedio_sueldos, media_geometrica

# Reporte de sueldos
def reporte_sueldos(sueldos):
    reportes = {}
    for empleado, sueldo in sueldos.items():
        descuento_salud = int(sueldo * 0.07)
        descuento_afp = int(sueldo * 0.12)
        sueldo_liquido = sueldo - descuento_salud - descuento_afp
        reportes[empleado] = {
            "Sueldo Base": sueldo,
            "Descuento Salud": descuento_salud,
            "Descuento AFP": descuento_afp,
            "Sueldo Líquido": int(sueldo_liquido)
        }
    return reportes

# Guardar reporte en CSV
def guardar_reporte_csv(reportes, filename="reporte_sueldos.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre Empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for empleado, datos in reportes.items():
            writer.writerow([empleado, datos["Sueldo Base"], datos["Descuento Salud"], datos["Descuento AFP"], datos["Sueldo Líquido"]])

# Menú principal
def menu():
    sueldos = {}
    while True:
        print("\nMenu:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            sueldos = asignar_sueldos_aleatorios()
            print("Sueldos asignados:", sueldos)
        elif opcion == "2":
            if sueldos:
                menores_800k, entre_800k_2m, superiores_2m = clasificar_sueldos(sueldos)
                print("Sueldos menores a 800k:", menores_800k)
                print("Sueldos entre 800k y 2M:", entre_800k_2m)
                print("Sueldos superiores a 2M:", superiores_2m)
            else:
                print("Debe asignar sueldos primero.")
        elif opcion == "3":
            if sueldos:
                sueldo_mas_alto, sueldo_mas_bajo, promedio_sueldos, media_geometrica = ver_estadisticas(sueldos)
                print(f"Sueldo más alto: {sueldo_mas_alto}")
                print(f"Sueldo más bajo: {sueldo_mas_bajo}")
                print(f"Promedio de sueldos: {promedio_sueldos}")
                print(f"Media geométrica: {media_geometrica}")
            else:
                print("Debe asignar sueldos primero.")
        elif opcion == "4":
            if sueldos:
                reportes = reporte_sueldos(sueldos)
                guardar_reporte_csv(reportes)
                print("Reporte guardado en reporte_sueldos.csv")
                for empleado, datos in reportes.items():
                    print(f"{empleado}: {datos}")
            else:
                print("Debe asignar sueldos primero.")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()