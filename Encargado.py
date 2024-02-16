#nombre DNI
#{"nombre":nombre, "dni":dni }
class Encargado:
    def __init__(self, nombre, dni = 1):
        self._nombre = nombre
        self._dni = dni
    def __str__(self):
        return f"Nombre: {self._nombre}\nDNI: {str(self._dni)}"

@property
def nombre(self):
    return self._nombre
@nombre.setter    
def nombre(self, nombre):
    self._nombre = nombre
    return
@property
def dni(self):
    return self._dni
@dni.setter    
def dni(self, dni):
    self._dni = dni
    return

tda_encargado = Encargado("nombre", "dni")
    