from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo : str = "grupo ordinado", asignaturas : list = [], estudiantes : list =[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes


    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista
        lista.clear()

    def __str__(self):
        msg = "Grupo de estudiantes: "
        return msg + self._grupo if self._grupo != "grupo ordinado" else msg +"grupo predeterminado"

    """@ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre"""

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    """@ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre"""
