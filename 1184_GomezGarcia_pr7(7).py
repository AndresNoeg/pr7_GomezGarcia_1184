class Universidad():
    def __init__(self, nombre):
        self.nombre = nombre

class Carrera():
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def __init__(self, universidad, nombre, edad):
        Universidad.__init__(self, universidad)
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Estudiante: {self.nombre}, Edad: {self.edad}, Especialidad: {self.especialidad}, Universidad: {self.nombre}")

persona = Estudiante("Harvard", "Mike", 19)
persona.carrera("Ingeniería Mecatrónica")
persona.mostrar_informacion()
