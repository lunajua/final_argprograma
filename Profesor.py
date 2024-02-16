#nombre, materia, curso, division
class Profesor:
    def __init__(self, nombre, materia, curso = -1, division = -1):
        self._nombre = nombre
        self._materia = materia
        self._curso = curso
        self._division = division
    def __str__(self):
        return f"Nombre: {self._nombre}\nMateria: {self._materia}\nCurso: {self._curso}\nDivision: {self._division}"
    @property
    def nombre(self):
        return self._nombre
    @property
    def materia(self):
        return self._materia
    @property
    def curso(self):
        return self._curso
    @property
    def division(self):
        return self._division
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @materia.setter
    def materia(self, materia):
        self._materia = materia
    @curso.setter
    def curso(self, curso):
        self._curso = curso
    @division.setter
    def division(self, division):
        self._division = division
        







   