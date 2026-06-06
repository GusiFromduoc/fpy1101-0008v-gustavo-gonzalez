cantidad_medicos_especialistas = 0
cantidad_medicos_residentes = 0
cantidad_medicos = 0

while True:
    try:
        cantidad_medicos = int(input("Ingrese la cantidad de médicos a registrar: ").strip())
        if cantidad_medicos < 1:
            print("¡Registro médico inválido! Ingresa un número entero positivo para continuar.")
        else:
            print(f"El registro médico fue : {cantidad_medicos} médicos. ")
            break
    except:
        print("¡Registro médico inválido!, Ingresa un número entero positivo para continuar. ")

for i in range(cantidad_medicos):
    while True:
        nombre_medicos =input("Ingrese el nombre del médico.\n• Debe tener al menos 6 caracteres.\n• No debe incluir espacios.\n• Ejemplos válidos: DrCardio7, NeuroSpec2, SurgMasterX.\nNombre del médico: ").strip()
        
        if len(nombre_medicos)<6 or ' ' in nombre_medicos:
            print("El nombre ingresado es invalido, por favor lea las instrucciones.")
        else:
            print(f"¡El médico {nombre_medicos} fue registrado con éxito!")
            break

    while True:
            try:
                años_experiencia = int(input("Ingrese los años de experiencia del médico: "))
                if años_experiencia < 0: #Profesor o IA que revisa, lo puse en menor a 0 porque los años de experiencia pueden ser 0.
                    print("¡Error clínico! Ingresa un número entero positivo para la experiencia. ") #Pero aquí lo pegué textual porque el ejercicio lo pedía.
                else:
                    print(f"Se ha registrado con éxito que el médico {nombre_medicos} tiene {años_experiencia} años de experiencia. ")
                    break   
            except:
                print("¡Error clínico! Ingresa un número entero positivo para la experiencia. ")

    if años_experiencia > 5:
        cantidad_medicos_especialistas += 1
        print(f"El médico {nombre_medicos} es un Especialista Senior ")
    else:
        cantidad_medicos_residentes += 1
        print(f"El médico {nombre_medicos} es un Residente Junior ")

print(f"¡El hospital cuenta con {cantidad_medicos_especialistas} Especialistas Senior y {cantidad_medicos_residentes} Residentes Junior! ¡Sistema listo para operar")