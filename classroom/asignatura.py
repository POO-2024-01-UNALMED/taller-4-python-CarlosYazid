from multimethod import multimethod

class Asignatura:

    @multimethod
    def __init__(self, nombre, salon, salon = "remoto"):
        self._nombre = nombre
        self._salon = salon
        self._salon = salon
    
    @multimethod
    def __init__(self, nombre, salon = "remoto"):
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        return f"{self._nombre} {self._salon}"
