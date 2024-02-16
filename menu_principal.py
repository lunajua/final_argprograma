import os
import time
from validar_acceso import validar_acceso
from modificarInscripcion import modificar
from modificarNota import modificar_nota 
from buscar_alumno import buscaAlumno
from imprimir_alumno import imprimeAlumno
from inscribir_alumno import inscribeAlumno
from eliminar_inscripcion import elimina


def clear():
    time.sleep(1)
    os.system('cls')

def menuPrincipal():
    clear()
    print("======================================================")
    print("------Bienvenido a la Universidad de San Luis---------")
    print("----------------Sistema de Inscripciones--------------")
    print("======================================================")
    print("01 -> Acceso a Sistema ")
    print("03 -> Salir ")
    return
def menuAdministrativo():
    clear()
    salir = False
    while not salir:
        print("======================================================")         
        print("------Bienvenido a la Universidad de San Luis---------")
        print("---------------Sistema de Inscripciones---------------")
        print("--------------------Menu de ABM-----------------------")
        print("======================================================")
        print("01 -> Ingreso de modificación por alumno.")
        print("02 -> Volver al menu principal")
        opcion = input("Ingrese la opción deseada: ")
        if opcion == "01":
            modificar()      
        elif opcion == "02":
            print("Volver al menú anterior.")
            salir = True
        else:
            print("Opción incorrecta.")
def menuProfesor():
    clear()
    salir = False
    while not salir:
        print("======================================================")
        print("------Bienvenido a la Universidad de San Luis---------")
        print("----------------Menú de Profesores--------------------")
        print("======================================================")
        print("01 -> Buscar alumno.")
        print("02 -> Cargar/Modificar Nota.")
        print("03 -> Imprimir listado de alumnos.")
        print("04 -> Volver al menu anterior.")
        opcion = input("Ingrese la opción deseada: ")
        if opcion == "01":     
            buscaAlumno()             
        elif opcion == "02":
            modificar_nota()
        elif opcion == "03":
            imprimeAlumno()                          
        elif opcion == "04":
            print("Volver al menú anterior")
            salir = True
        else:
            print("Opción Incorrecta.")
def menuEncargado():
    clear()
    salir = False
    while not salir:
        print("======================================================")
        print("------Bienvenido a la Universidad de San Luis---------")
        print("----------------Menú de Encargados--------------------")
        print("======================================================")
        print("01 -> Inscribir Alumno")
        print("02 -> Modificar Inscripción")
        print("03 -> Eliminar Inscripción")
        print("04 -> Imprimir las Inscripciones")
        print("05 -> Volver al menú anterior")
        opcion = input("Ingrese la opción deseada: ")
        if opcion == "01":
            inscribeAlumno()
        elif opcion == "02":
            menuAdministrativo()            
        elif opcion == "03":
            elimina()            
        elif opcion == "04":
            imprimeAlumno()                           
        elif opcion == "05":
            print("Volver al menú")
            salir = True
        else:
            print("Opción Incorrecta.")
opcion = "0"
while opcion != "03":
    menuPrincipal()    
    opcion = input("Ingrese la opción deseada: ")
    if opcion == "01":        
        tipo_usuario = input("Ingrese el tipo de usuario (Profesor/Encargado): ").lower()
        nombre = input("Ingrese su nombre y apellido: ")
        try:    
            if tipo_usuario == "profesor":
                materia = input("Ingrese la materia que dicta: ").lower()
                curso = input("Ingrese el curso: ").lower()
                division = input("Ingrese la división: ").lower()
                if not validar_acceso(
                    tipo_usuario,
                    nombre,
                    materia=materia,
                    curso=curso,
                    division=division,
                ):
                    raise ValueError("Acceso denegado")
                print(f"{nombre}, acceso concedido")
                menuProfesor()
            elif tipo_usuario == "encargado":            
                dni = input("Ingrese su DNI: ")
                if validar_acceso(tipo_usuario, nombre, dni=dni):
                    print(f"{nombre}, acceso concedido")
                    menuEncargado()
                else:
                    raise ValueError("Acceso denegado")
        except ValueError as e:
            print(e)
            print("Por favor, inténtelo nuevamente. Gracias.")
    elif opcion == "03":
        print("Este programa fue realizado por Tato Company and Co para la Universidad Nacional de San Luis")
    else:
        print("Opción Inválida")
