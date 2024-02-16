def mostrarResultado(inscripto):
        menu_ventana = Toplevel(ventana) 
        menu_ventana.title("Resultado de la búsqueda")
        menu_ventana.geometry("400x200")
        #inscripto = Inscripcion(Inscripcion.fecha,Inscripcion.alumno,Inscripcion.materia,Inscripcion.profesor,Inscripcion.curso,Inscripcion.division,Inscripcion.nota)

    # Mostrar los datos del alumno encontrado
        resultado_label = Label(menu_ventana, text=f"Nombre: {inscripto.alumno}\n"
                                                     f"Materia: {inscripto.materia}\n"
                                                     f"Curso: {inscripto.curso}\n"
                                                     f"División: {inscripto.division}\n"
                                                     f"Nota: {inscripto.nota}")
        resultado_label.pack()

        
def buscarAlumno():
    alumno_entry = Entry(ventana)  # Crear un Entry
    nombre_alumno = alumno_entry.get()  # Obtener el valor del Entry
    #inscriptos = {}
    encontrado = False  # Variable para controlar si se encontró el alumno
    with open('Inscripciones.txt', 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            dato = linea.strip().split(',')
            inscripto = Inscripcion(*dato)
            #inscriptos[inscripto.alumno] = inscripto
            if inscripto.alumno == nombre_alumno:
                encontrado = True
                mostrarResultado(inscripto)
                #break  # Salir del bucle si se encuentra el alumno in inscriptos:
            
                #break  # Salir del bucle si se encuentra el alumno
        
    if not encontrado:
            messagebox.showwarning("Alumno no encontrado")
