import Inscripcion

def inscribeAlumno():
    try:
        fecha = input("Ingrese la fecha (dd/mm/yyyy): ")
        alumno = input("Ingrese el nombre del alumno: ").lower()
        materia = input("Ingrese la materia: ").lower()
        profesor = input("Ingrese el nombre del profesor: ").lower()
        curso = int(input("Ingrese el curso: "))
        division = input("Ingrese la división: ").lower()
        nota = -1
        linea = f"{fecha},{alumno},{materia},{profesor},{curso},{division},{nota}\n"
        with open('Inscripciones.txt','a', encoding="UTF-8") as archivo:
            archivo.write(linea)
        print("Inscripcion realizada con éxito.")
    except ValueError:
            print("Ingrese un dato válido.")
    inscripto = Inscripcion.Inscripcion(fecha, alumno, materia, profesor, curso, division, nota) 
    print(inscripto)
    