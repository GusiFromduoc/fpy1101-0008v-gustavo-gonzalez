libros_disponibles = 120
libros_prestados = 0
prestamos = 0
devoluciones = 0
opc = 0
print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")

while opc != 5:
    try:
        opc = int(input("===MENÚ PRINCIPAL===\n1. Libros disponibles.\n2. Realizar préstamo.\n3. Devolver préstamo.\n4. Historial de préstamos.\n5. Salir\nPor favor ingrese una opción del menú: "))
    except ValueError:
        print("Por favor ingrese una opción valida del menú en número entero. ")
        continue
    if opc == 1:
        print(f"Actualmente hay {libros_disponibles} libros disponibles.")
    elif opc == 2:
        while True:
            try:
                a_prestar = int(input("Ingrese la cantidad de libros a prestar."))
            except ValueError:
                print("Debe ingresar una cantidad de libros valida en números enteros. ")
                continue
            if a_prestar > libros_disponibles:
                print("La cantidad solicitada excede los libros disponibles.")
            elif a_prestar < 1:
                print("Debe ingresar una cantidad valida de libros, mayor a 0. ")
            else:
                print(f"¡Se han prestado con éxito {a_prestar} libros.!")
                libros_disponibles -= a_prestar
                libros_prestados += a_prestar
                prestamos += a_prestar
                break
    elif opc == 3:
        while True:
            try:
                a_devolver = int(input("Ingrese la cantidad de libros a devolver. "))
            except ValueError:
                print("Debe ingresar una cantidad valida de libros en números enteros. ")
                continue
            if a_devolver > libros_prestados:
                print("No puede devolver esa cantidad, excede los libros prestados. ")
            elif a_devolver < 1:
                print("Debe ingresar una cantidad valida de libros, mayor a 0. ")
            else:
                print(f"¡Se han devuelto con éxito {a_devolver} libros, Gracias!")
                libros_disponibles += a_devolver
                libros_prestados -= a_devolver
                devoluciones += a_devolver
                break
    elif opc == 4:
        print(f"Actualmente hay {libros_prestados} libros prestados de forma activa.\n Se han prestado {prestamos} libros hoy.\nSe han devuelto {devoluciones} libros hoy.")
    elif opc == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima")