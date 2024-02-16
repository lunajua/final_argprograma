
import Inscripcion

def modificar():
    validar = False
    nombre_alumno = input("Ingrese el nombre del alumno a buscar: ")

    # Abro el archivo en modo lectura
    with open('Inscripciones.txt', 'r') as archivo:
        # Leo todas las líneas del archivo
        lineas = archivo.readlines()

    # Pregunto al usuario qué campo desea modificar
    print("Los campos a modificar pueden ser: ")
    print("Fecha, Nombre, Materia, Profesor, Curso, División")
    pregunta = input('¿Qué campo deseas modificar?: ').lower()

    # Valido que el campo ingresado sea válido
    if pregunta not in ['fecha', 'nombre', 'materia', 'profesor', 'curso', 'división']:
        print(f"El campo {pregunta} no es válido.")
        return
    
    # Pregunto al usuario el nuevo valor para el campo elegido
    nuevo_valor = input(f'Ingresa el nuevo valor para el campo {pregunta}: ')
    with open('Inscripciones.txt', 'w') as archivo:        
        for linea in lineas:
            #Utilizo strip para eliminar espacios en blanco al principio y al final y con el split convierto en una lista separadas por comas 
            dato = linea.strip().split(',') 
            #Pregunto si la variable dato en la posición 1 es igual al nombre ingresado por el usuario
            if dato[1] == nombre_alumno: 
                #Si es igual validar pasa a ser verdadera
                validar = True 
                #Creo una instancia de la clase Inscripcion. Uso el operador * para desempaquetar lo que tiene dato.
                inscripcion = Inscripcion.Inscripcion(*dato)
                # Modifico el campo elegido por el usuario con el nuevo valor
                if pregunta == 'fecha':
                    inscripcion.fecha = nuevo_valor
                elif pregunta == 'nombre':
                    inscripcion.alumno = nuevo_valor
                elif pregunta == 'materia':
                    inscripcion.materia = nuevo_valor
                elif pregunta == 'profesor':
                    inscripcion.profesor = nuevo_valor
                elif pregunta == 'curso':
                    inscripcion.curso = nuevo_valor
                elif pregunta == 'división':
                    inscripcion.division = nuevo_valor
                elif pregunta == 'nota':
                    inscripcion.nota = nuevo_valor
                dato = [inscripcion.fecha,
                        inscripcion.alumno,
                        inscripcion.materia,
                        inscripcion.profesor,
                        inscripcion.curso,
                        inscripcion.division,
                        inscripcion.nota]
            ## Escribo la línea modificada en el archivo
            archivo.write(','.join(dato) + '\n')       
             
    if validar:
        print(f"La modificación para el alumno {nombre_alumno} fue realizada con éxito")
    else:
        print(f"No se encontró al alumno {nombre_alumno} en el archivo Inscripciones.")
