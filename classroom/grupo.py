from classroom.asignatura import Asignatura

"""
    Taller 4 Python

    Realizado el 29 de febrero del 2024
    Desarrollado por Carlos Yazid Padilla
    Topico: Sobrecarga y Destructores

    Dependencias: 
    
        - classroom > grupo
        - classroom > asignatura
    
"""

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo : str = "grupo predeterminado", asignaturas : list = [], estudiantes : list =[]):
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
        return msg + self._grupo

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

# Anti-Copy: Carlos Padilla