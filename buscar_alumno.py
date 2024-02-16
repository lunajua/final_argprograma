import Inscripcion

def buscaAlumno():
    nombre_alumno = input("Ingrese el nombre del alumno a buscar: ")
    with open('Inscripciones.txt', 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            dato = linea.strip().split(',')
            inscripto = Inscripcion.Inscripcion(*dato)
            if inscripto.alumno == nombre_alumno:
                print(f"Fecha: {inscripto.fecha}")
                print(f"Nombre: {inscripto.alumno}")
                print(f"Materia: {inscripto.materia}")
                print(f"Curso: {inscripto.curso}")
                print(f"División: {inscripto.division}")
                print(f"Nota: {inscripto.nota}")