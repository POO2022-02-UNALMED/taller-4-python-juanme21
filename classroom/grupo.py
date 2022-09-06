from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = None

    def __init__(
        self,
        grupo="grupo predeterminado",
        grado="Grado 12",
        asignaturas=None,
        estudiantes=None,
    ):
        self._grupo = grupo
        self.grado = grado
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):

        if self._asignaturas is None:
            self._asignaturas = []
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            self.listadoAlumnos = [alumno]
        else:
            lista.append(alumno)
            if self.listadoAlumnos is None:
                self.listadoAlumnos = lista
            else:
                self.listadoAlumnos = self.listadoAlumnos.extend(lista)

    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo

    @classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
