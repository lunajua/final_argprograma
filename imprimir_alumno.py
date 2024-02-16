from tabulate import tabulate

def imprimeAlumno():
    with open ('Inscripciones.txt', encoding="UTF-8") as f:
        inscripciones = f.readlines()         
        dato = [inscripcion.strip().split(",") for inscripcion in inscripciones]
        cabeceras = ["Fecha", "Nombre", "Materia", "Profesor", "Curso", "Division", "Nota"]
        print (tabulate(dato, headers=cabeceras, tablefmt="grid"))      
