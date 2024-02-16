import tkinter as tk
import Inscripcion  # Asumiendo que tienes un módulo Inscripcion con la definición de la clase Inscripcion

def buscaAlumno():
    
    nombre_alumno = nombre_alumno_entry.get()  # Obtener el valor del Entry
    encontrado = False  # Variable para controlar si se encontró el alumno

    with open('Inscripciones.txt', 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            dato = linea.strip().split(',')
            inscripto = Inscripcion.Inscripcion(*dato)
            if inscripto.alumno == nombre_alumno:
                encontrado = True
                mostrarResultado(inscripto)
                break  # Salir del bucle si se encuentra el alumno
    
    if not encontrado:
        mostrarMensaje("Alumno no encontrado")

def mostrarResultado(inscripto):
    resultado_window = tk.Toplevel(root)
    resultado_window.title("Resultado de la búsqueda")
    resultado_window.geometry("400x200")

    # Mostrar los datos del alumno encontrado
    resultado_label = tk.Label(resultado_window, text=f"Nombre: {inscripto.alumno}\n"
                                                     f"Materia: {inscripto.materia}\n"
                                                     f"Curso: {inscripto.curso}\n"
                                                     f"División: {inscripto.division}\n"
                                                     f"Nota: {inscripto.nota}")
    resultado_label.pack()

def mostrarMensaje(mensaje):
    mensaje_window = tk.Toplevel(root)
    mensaje_window.title("Mensaje")
    mensaje_window.geometry("300x100")

    mensaje_label = tk.Label(mensaje_window, text=mensaje)
    mensaje_label.pack()

# Crear la ventana principal
root = tk.Tk()
root.title("Buscar alumno")
root.geometry("400x200")
root.resizable(False, False)

# Crear el Entry para ingresar el nombre del alumno
nombre_alumno_entry = tk.Entry(root)
nombre_alumno_entry.pack()

# Crear el botón para buscar al alumno
buscar_button = tk.Button(root, text="Buscar Alumno", command=buscaAlumno)
buscar_button.pack()

root.mainloop()


