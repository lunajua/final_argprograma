def validar_acceso(tipo_usuario, nombre, materia=None, curso=None, division=None, dni=None):
    if tipo_usuario == "profesor":
        with open("Profesores.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if datos[0] == nombre and datos[1] == materia and datos[2] == curso and datos[3] == division:                     
                    return True
    elif tipo_usuario == "encargado":
        with open("Encargados.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                
                if datos[0] == nombre and datos[1] == dni:
                    return True
    return False


