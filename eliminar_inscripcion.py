def elimina():
    nombre = input("Ingrese el nombre del alumno a dar de baja: ")
    confirmar = input(f"¿Confirma la baja del alumno {nombre}? (s/n): ")
    if confirmar.lower() == "s":
        encontrado = False
        with open('Inscripciones.txt', 'r') as archivo:
            lineas = archivo.readlines()
        with open('Inscripciones.txt', 'w') as archivo:
            for linea in lineas:
                if nombre not in linea:
                    archivo.write(linea)
                else:
                    encontrado = True
        if not encontrado:
            print(f"No se encontro al alumno {nombre} en el archivo Inscripciones.")
        else:
            print(f"El alumno {nombre} fue dado de baja con éxito")         
    else:
        print("Operación cancelada.")
    