import Inscripcion 

def modificar_nota():
    validar = False #Validación para saber si un alumno está o no en el archivo Inscripciones
    nombre_alumno = input("Ingrese el nombre del alumno a buscar: ")
    #Abro el archivo inscripciones en modo lectura y lo leo línea x línea almacenando todo en la variable lineas
    with open('Inscripciones.txt', 'r') as archivo:
        lineas = archivo.readlines()
    #Pido el nuevo valor para el campo nota
    nueva_nota = input(f'Ingresa la nueva nota para el alumno {nombre_alumno}: ')
    #Abro el archivo en modo escritura e itero con un bucle for
    with open('Inscripciones.txt', 'w') as archivo:
        for linea in lineas:
            dato = linea.strip().split(',') #Utilizo strip para eliminar espacios en blanco al principio y al final y con el split convierto en una lista separadas por comas 
            if dato[1] == nombre_alumno: #Pregunto si la variable dato en la posición 1 es igual al nombre ingresado por el usuario
                validar = True #Si es igual validar pasa a ser verdadera
                inscripcion = Inscripcion.Inscripcion(*dato) #Creo una instancia de la clase Inscripcion. Uso el operador * para desempaquetar lo que tiene dato.
                inscripcion.nota = nueva_nota #Llamo al setter de nota dandole como parametro todo lo que tiene la clase Inscripcion y el valor de la nueva nota que ingresó el usuario.
                dato = [inscripcion.fecha,
                        inscripcion.alumno,
                        inscripcion.materia,
                        inscripcion.profesor,
                        inscripcion.curso,
                        inscripcion.division,
                        str(inscripcion.nota)]
            archivo.write(','.join(dato) + '\n') #Escribo la nota actualizada y uno con el método join separado por comas
    if validar:
        print(f"La nota para el alumno {nombre_alumno} fue cargada con éxito")
    else:
        print(f"No se encontró al alumno {nombre_alumno} en el archivo inscripciones")
