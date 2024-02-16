#inscripcion
#fecha,alumno,materia,profesor,curso,division,nota
class Inscripcion:
    def __init__(self, fecha, alumno, materia, profesor, curso, division, nota=-1):
        self._fecha = fecha
        self._alumno = alumno
        self._materia = materia
        self._profesor = profesor
        self._curso = curso
        self._division = division
        self._nota = nota

    def __iter__(self):
        return iter([self._fecha, self._alumno, self._materia, self._profesor, self._curso, self._division, self._nota])
    
    @property
    def fecha(self):
        return self._fecha
    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha
        return
    @property
    def alumno(self):
        return self._alumno
    @alumno.setter
    def alumno(self, alumno):
        self._alumno = alumno
        return
    @property
    def materia(self):
        return self._materia
    @materia.setter
    def materia(self, materia):
        self._materia = materia
        return
    @property
    def profesor(self):
        return self._profesor
    @profesor.setter
    def profesor(self, profesor):
        self._profesor = profesor
        return
    @property
    def curso(self):
        return self._curso
    @curso.setter
    def curso(self, curso):
        self._curso = curso
        return
    @property
    def division(self):
        return self._division
    @division.setter
    def division(self, division):
        self._division = division
        return
    @property
    def nota(self):        
        return self._nota
    @nota.setter
    def nota(self, nota):
        self._nota = nota
        return
    def __str__(self):
        return f"Fecha: {self._fecha}, Alumno: {self._alumno}, Materia: {self._materia}, Profesor: {self._profesor}, Curso: {self._curso}, Division: {self._division}, Nota: {self._nota}"






