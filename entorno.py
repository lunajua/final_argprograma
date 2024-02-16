from tkinter import *
from tkinter import messagebox
from validar_acceso import validar_acceso
from Encargado import Encargado
from Profesor import Profesor
from Inscripcion import Inscripcion
from tabulate import tabulate

def abrir_menu_encargado():
    menu_encargado_ventana = Toplevel(ventana)
    menu_encargado_ventana.geometry("400x300")
    menu_encargado_ventana.title("Acceso Encargado")
    etiqueta = Label(menu_encargado_ventana, text="=====================================================================").pack()
    etiqueta2 = Label(menu_encargado_ventana, text=" Bienvenido al sistema de inscripciones de la Universidad de San Luis").pack()
    etiqueta3 = Label(menu_encargado_ventana, text="=====================================================================").pack()
    nombre_label = Label(menu_encargado_ventana, text="Ingrese su nombre y apellido:").pack()
    nombre_entry = Entry(menu_encargado_ventana)
    nombre_entry.pack()
    dni_label = Label(menu_encargado_ventana, text="Ingrese su DNI:").pack()
    dni_entry = Entry(menu_encargado_ventana)
    dni_entry.pack()
        
    def validar_acceso_encargado():
        nombre = nombre_entry.get()
        dni = dni_entry.get()
        if nombre == "" or dni == "":
            messagebox.showerror("Error", "Ingrese datos válidos")
        else:
        # Aquí debes realizar la validación de acceso para el encargado
            if validar_acceso("encargado", nombre, dni=dni):
                messagebox.showinfo(f"{nombre}Acceso concedido", "Bienvenido al sistema de inscripciones de la Universidad de San Luis")
                 
                menu_encargado()
            else:
                messagebox.showwarning(f"{nombre} no tiene acceso. Vuelva a intentar por favor")
                      #
            
    boton_validar = Button(menu_encargado_ventana, text="Validar Acceso", command=validar_acceso_encargado).pack()
    boton_exit= Button(menu_encargado_ventana, text="Salir", command=menu_encargado_ventana.destroy).pack()


 
def menu_encargado():
    menu_ventana = Toplevel(ventana)
    menu_ventana.geometry("640x480")
    menu_ventana.title("Menu Encargado")
    etiqueta = Label(menu_ventana, text="=====================================================================").pack()
    etiqueta2 = Label(menu_ventana, text=" Bienvenido al sistema de inscripciones de la Universidad de San Luis").pack()
    etiqueta3 = Label(menu_ventana, text="=====================================================================").pack()
    boton_alumno = Button(menu_ventana, text="Inscribir Alumno", command=inscribeAlumno)
    Label(menu_ventana, text="Inscribir un alumno a una materia").pack()
    boton_alumno.pack()
    boton_eliminar = Button(menu_ventana, text="Eliminar Inscripción", command=eliminarInscripcion)
    boton_eliminar.config(bg="red", fg="black")
    Label(menu_ventana, text="Eliminar una inscripción de un alumno").pack() 
    boton_eliminar.pack()
    boton_imprimir = Button(menu_ventana, text="Imprimir Alumno", command=imprimeAlumno)
    Label(menu_ventana, text="Imprimir Inscripciones").pack()
    boton_imprimir.pack()
    boton_exit = Button(menu_ventana, text="Salir", command=menu_ventana.destroy)
    boton_exit.pack()

fecha_entry = None
alumno_entry = None
materia_entry = None
profesor_entry = None
curso_entry = None
division_entry = None

def realizarInscripcion(): 
    global fecha_entry, alumno_entry, materia_entry, profesor_entry, curso_entry, division_entry
           
    fecha = fecha_entry.get()
    alumno = alumno_entry.get().lower()
    materia = materia_entry.get().lower()
    profesor = profesor_entry.get().lower()
    curso = curso_entry.get()
    division = division_entry.get().lower()    
    try:
        #Intenta convertir el curso a un entero
        curso = int(curso)
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido para el curso.")
        return

    nota = -1
    linea = f"{fecha},{alumno},{materia},{profesor},{curso},{division},{nota}\n"
    with open('Inscripciones.txt','a', encoding="UTF-8") as archivo:
        archivo.write(linea)

        messagebox.showinfo("Éxito", "Inscripción realizada con éxito.")

    inscripto = Inscripcion(fecha, alumno, materia, profesor, curso, division, nota)
     
def inscribeAlumno():
    global fecha_entry, alumno_entry, materia_entry, profesor_entry, curso_entry, division_entry
    #Obtén los datos de las entradas
    menu_ventana = Toplevel(ventana)
    menu_ventana.geometry("400x300")
    menu_ventana.title("Inscripción") 
    fecha = Label(menu_ventana, text="Fecha (dd/mm/yyyy):")
    fecha.pack()
    fecha_entry = Entry(menu_ventana)
    fecha_entry.pack()
    alumno = Label(menu_ventana, text="Nombre del alumno:")
    alumno.pack()
    alumno_entry = Entry(menu_ventana)
    alumno_entry.pack()
    materia =Label(menu_ventana, text="Materia:")
    materia.pack()
    materia_entry = Entry(menu_ventana)
    materia_entry.pack()
    profesor= Label(menu_ventana, text="Nombre del profesor:")
    profesor.pack()
    profesor_entry = Entry(menu_ventana)
    profesor_entry.pack()
    curso = Label(menu_ventana, text="Curso:")
    curso.pack()
    curso_entry = Entry(menu_ventana)
    curso_entry.pack()
    division =Label(menu_ventana, text="División:")
    division.pack()
    division_entry = Entry(menu_ventana)
    division_entry.pack()     
    boton_inscribir = Button(menu_ventana, text="Inscribir Alumno", command=realizarInscripcion)
    boton_inscribir.pack()
    boton_salir = Button(menu_ventana, text="Salir", command=menu_ventana.destroy)
    boton_salir.pack()

def eliminarInscripcion():
    global alumno_entry      
    
    def confirmar_eliminar(nombre):
        confirmar = messagebox.askquestion("Confirmar Eliminación", f"¿Confirma la baja del alumno {nombre}?")
        if confirmar == "yes":
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
                messagebox.showinfo("Eliminación", f"No se encontró al alumno {nombre} en el archivo Inscripciones.")                  
            else:
                messagebox.showinfo("Eliminación", f"El alumno {nombre} fue dado de baja con éxito")
            menu_ventana.destroy()
        else:
            messagebox.showinfo("Eliminación", "Operación cancelada.")
    
    menu_ventana = Toplevel(ventana)
    menu_ventana.geometry("400x300")
    menu_ventana.title("Elimina Inscripción") 
    nombre_alumno_label = Label(menu_ventana, text = "Ingrese el nombre del alumno a eliminar: ")
    nombre_alumno_label.pack()
    nombre_alumno_entry = Entry(menu_ventana)
    nombre_alumno_entry.pack()
    # Crear un botón para confirmar la eliminación
    boton_confirmar = Button(menu_ventana, text="Confirmar Eliminación", command=lambda: confirmar_eliminar(nombre_alumno_entry.get()))
    boton_confirmar.pack()     
    boton_salir = Button(menu_ventana, text="Salir", command=menu_ventana.destroy)
    boton_salir.pack()
    
def imprimeAlumno():
    def imprime():
        with open('Inscripciones.txt', encoding="UTF-8") as f:
            inscripciones = f.readlines()
        dato = [inscripcion.strip().split(",") for inscripcion in inscripciones]
        cabeceras = ["Fecha", "Nombre", "Materia", "Profesor", "Curso", "Division", "Nota"]
        resultado = tabulate(dato, headers=cabeceras, tablefmt="grid")
        # Crear un widget de texto y mostrar el resultado
        texto_widget = Text(menu_ventana, font=("Courier", 9), bd=2,  bg="lightblue")                
        texto_widget.insert('end', resultado)
        texto_widget.pack()
    # Crear una ventana de Tkinter
    menu_ventana = Toplevel(ventana)
    menu_ventana.geometry("640x480")
    menu_ventana.title("Datos de Inscripciones")
    imprime_alumno_label = Label(menu_ventana, text="Datos de Inscripciones")
    imprime_alumno_label.pack()
    boton_imprimir = Button(menu_ventana, text="Imprimir", command=imprime)
    boton_imprimir.pack()
    boton_salir = Button(menu_ventana, text="Salir", command=menu_ventana.destroy)
    boton_salir.pack() 


def abrir_menu_profesor():
    menu_profesor_ventana = Toplevel(ventana)
    menu_profesor_ventana.geometry("400x300")
    menu_profesor_ventana.title("Acceso Profesor")
    etiqueta = Label(menu_profesor_ventana, text="=====================================================================")
    etiqueta.pack()
    etiqueta2 = Label(menu_profesor_ventana, text=" Bienvenido al sistema de inscripciones de la Universidad de San Luis")
    etiqueta2.pack()
    etiqueta3 = Label(menu_profesor_ventana, text="=====================================================================")
    etiqueta3.pack()
    nombre_label = Label(menu_profesor_ventana, text="Ingrese su nombre y apellido:")
    nombre_label.pack()
    nombre_entry = Entry(menu_profesor_ventana)
    nombre_entry.pack()
    materia_label = Label(menu_profesor_ventana, text="Ingrese la materia que dicta:")
    materia_label.pack()
    materia_entry = Entry(menu_profesor_ventana)
    materia_entry.pack()
    curso_label = Label(menu_profesor_ventana, text="Ingrese el curso:")
    curso_label.pack()
    curso_entry = Entry(menu_profesor_ventana)
    curso_entry.pack()
    division_label = Label(menu_profesor_ventana, text="Ingrese la división:")
    division_label.pack()
    division_entry = Entry(menu_profesor_ventana)
    division_entry.pack()
    
    def validar_acceso_profesor():
        nombre = nombre_entry.get()
        materia = materia_entry.get()
        curso = curso_entry.get()
        division = division_entry.get()
        if nombre == "" or materia == "" or curso == "" or division == "":
            messagebox.showerror("Error", "Ingrese datos válidos")
        else:
            #Aquí debes realizar la validación de acceso para el profesor
            if validar_acceso("profesor", nombre, materia=materia, curso=curso, division=division):
                messagebox.showinfo(f"{nombre}Acceso concedido", "Bienvenido al sistema de inscripciones de la Universidad de San Luis")
            
                abm_profesor()
            else:
                messagebox.showwarning(f"{nombre} no tiene acceso. Vuelva a intentar por favor")
                       
    
    boton_validar = Button(menu_profesor_ventana, text="Validar Acceso", command=validar_acceso_profesor)
    boton_validar.pack()
    boton_exit= Button(menu_profesor_ventana, text="Salir", command=menu_profesor_ventana.destroy)
    boton_exit.pack()

def abm_profesor():  # sourcery skip: extract-duplicate-method
    menu_ventana = Toplevel(ventana)
    menu_ventana.geometry("640x480")
    menu_ventana.title("Menu Profesor")
    etiqueta = Label(menu_ventana, text="=====================================================================").pack()
    etiqueta2 = Label(menu_ventana, text=" Bienvenido al sistema de inscripciones de la Universidad de San Luis").pack()
    etiqueta3 = Label(menu_ventana, text="=====================================================================").pack()
    boton_alumno = Button(menu_ventana, text="Buscar Alumno", command=buscaAlumno)
    Label(menu_ventana, text="Buscar un alumno por nombre").pack()
    boton_alumno.pack()
    boton_notas = Button(menu_ventana, text="Cargar/Modificar Notas", command=cargaNota)
    Label(menu_ventana, text="Cargar o modificar notas de un alumno").pack()
    boton_notas.pack()
    boton_imprimir = Button(menu_ventana, text="Imprimir Alumno", command=imprimeAlumno)
    Label(menu_ventana, text="Imprimir un alumno por nombre").pack()
    boton_imprimir.pack()
    boton_salir = Button(menu_ventana, text="Salir", command=menu_ventana.destroy)
    boton_salir.pack()


def buscaAlumno():    
    global alumno_entry
    
    menu_ventana = Toplevel(ventana)
    menu_ventana.geometry("640x480")
    menu_ventana.title("Sistema de Inscripciones")
    etiqueta = Label(menu_ventana, text="=====================================================================").pack()
    etiqueta2 = Label(menu_ventana, text=" Bienvenido al sistema de inscripciones de la Universidad de San Luis").pack()
    etiqueta3 = Label(menu_ventana, text="=====================================================================").pack()  
    busca_alumno_label = Label(menu_ventana, text="Busqueda de Alumno")
    busca_alumno_label.pack()
    alumno_entry = Entry(menu_ventana)
    alumno_entry.pack()
    boton_buscar = Button(menu_ventana, text="Buscar Alumno", command=buscaAlumnoEnArchivo)
    boton_buscar.pack()
    boton_salir = Button(menu_ventana, text="Salir", command=menu_ventana.destroy)
    boton_salir.pack() 

def buscaAlumnoEnArchivo():    
    nombre_alumno = alumno_entry.get()  # Obtener el valor del Entry
    encontrado = False  # Variable para controlar si se encontró el alumno
    with open('Inscripciones.txt', 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            dato = linea.strip().split(',')
            inscripto = Inscripcion(*dato)
            if inscripto.alumno == nombre_alumno:
                encontrado = True
                mostrarResultado(inscripto)
                break  # Salir del bucle si se encuentra el alumno
    
    if not encontrado:
        messagebox.showerror("Advertencia",f"El Alumno {nombre_alumno} no se encuentra en el listado de Inscripciones")

def mostrarResultado(inscripto):
    resultado_window = Toplevel(ventana)
    resultado_window.title("Resultado de la búsqueda")
    resultado_window.geometry("400x200")
    # Mostrar los datos del alumno encontrado
    resultado_label = Label(resultado_window, text=f"Nombre: {inscripto.alumno}\n"
                                                     f"Materia: {inscripto.materia}\n"
                                                     f"Curso: {inscripto.curso}\n"
                                                     f"División: {inscripto.division}\n"
                                                     f"Nota: {inscripto.nota}")
    resultado_label.pack()


    

def cargaNota():
    global alumno_entry, nota_entry
    
    menu_ventana = Toplevel(ventana)
    menu_ventana.geometry("640x480")
    menu_ventana.title("Sistema de Inscripciones")
    etiqueta = Label(menu_ventana, text="=====================================================================").pack()
    etiqueta2 = Label(menu_ventana, text=" Bienvenido al sistema de inscripciones de la Universidad de San Luis").pack()
    etiqueta3 = Label(menu_ventana, text="=====================================================================").pack()  
    busca_alumno_label = Label(menu_ventana, text="Ingrese el nombre del alumno que desea cargar/modificar su nota")
    busca_alumno_label.pack()
    alumno_entry = Entry(menu_ventana)
    alumno_entry.pack()
    nota_label = Label(menu_ventana, text="Ingrese la nueva nota para el alumno")
    nota_label.pack()
    nota_entry = Entry(menu_ventana)
    nota_entry.pack()
    boton_buscar = Button(menu_ventana, text="Buscar Alumno", command=cargaNotaEnArchivo)
    boton_buscar.pack()
    boton_salir = Button(menu_ventana, text="Salir", command=menu_ventana.destroy)
    boton_salir.pack() 

def cargaNotaEnArchivo():    
    validar = False # Variable para controlar si se encontró el alumno 
    nombre_alumno = alumno_entry.get()  # Obtener el valor del Entry    
    #Abro el archivo inscripciones en modo lectura y lo leo línea x línea almacenando todo en la variable lineas
    with open('Inscripciones.txt', 'r') as archivo:
        lineas = archivo.readlines()
    #Pido el nuevo valor para el campo nota
    nueva_nota = nota_entry.get()
    #Abro el archivo en modo escritura e itero con un bucle for
    with open('Inscripciones.txt', 'w') as archivo:
        for linea in lineas:
            dato = linea.strip().split(',') #Utilizo strip para eliminar espacios en blanco al principio y al final y con el split convierto en una lista separadas por comas 
            if dato[1] == nombre_alumno: #Pregunto si la variable dato en la posición 1 es igual al nombre ingresado por el usuario
                validar = True #Si es igual validar pasa a ser verdadera 
                messagebox.showinfo("Exito",f"La nota para el alumno {nombre_alumno} fue modificada con éxito")               
                inscripcion = Inscripcion(*dato) #Creo una instancia de la clase Inscripcion. Uso el operador * para desempaquetar lo que tiene dato.
                inscripcion.nota = nueva_nota #Llamo al setter de nota dandole como parametro todo lo que tiene la clase Inscripcion y el valor de la nueva nota que ingresó el usuario.
                dato = [inscripcion.fecha,
                        inscripcion.alumno,
                        inscripcion.materia,
                        inscripcion.profesor,
                        inscripcion.curso,
                        inscripcion.division,
                        str(inscripcion.nota)]
            archivo.write(','.join(dato) + '\n') #Escribo la nota actualizada y uno con el método join separado por comas
            
    if not validar:
        messagebox.showerror("Advertencia",f"El alumno {nombre_alumno} no se encuentra en el archivo Inscripciones")

def abrir_menu():
    menu_ventana = Toplevel(ventana)
    menu_ventana.geometry("640x480")
    menu_ventana.title("Menu Principal")
    etiqueta = Label(menu_ventana, text="=====================================================================").pack()
    etiqueta2 = Label(menu_ventana, text=" Bienvenido al sistema de inscripciones de la Universidad de San Luis", fg="Blue").pack()
    etiqueta3 = Label(menu_ventana, text="=====================================================================").pack()  
    boton_encargado = Button(menu_ventana, text="Encargado", command=abrir_menu_encargado)
    boton_encargado.pack()   
    boton_profesor = Button(menu_ventana, text="Profesor", command=abrir_menu_profesor)
    boton_profesor.pack()
    boton_exit= Button(menu_ventana, text="Salir", command=menu_ventana.destroy)
    boton_exit.pack()


def salir():
    ventana.destroy()


ventana = Tk()
ventana.geometry("640x480")
ventana.title("Sistema de Inscripciones")
ventana.config(bg="lightblue")
ventana.config(bd=2)


etiqueta = Label (ventana, text="=====================================================================").pack()
etiqueta2 = Label (ventana, text=" Bienvenido al sistema de inscripciones de la Universidad de San Luis", fg="blue", font=("Ariel", 12))
etiqueta2.pack()
etiqueta3 = Label(ventana, text="=====================================================================").pack()

boton_acceso = Button(ventana, text="Acceso al sistema", command=abrir_menu)
boton_acceso.config(bg="green", fg="white")
boton_acceso.pack()

boton_salir = Button(ventana, text="Salir", command=salir)
boton_salir.config(bg="green", fg="white")
boton_salir.pack()

ventana.mainloop()
