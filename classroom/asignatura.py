from multimethod import multimethod

class Asignatura:

    @multimethod
    def __init__(self, nombre, salon, tipo = "remoto"):
        self._nombre = nombre
        self._salon = salon
        self._tipo = tipo
    
    @multimethod
    def __init__(self, nombre, tipo = "remoto"):
        self._nombre = nombre
        self._tipo = tipo

    def __str__(self):
        return f"{self._nombre} {self._tipo}"
