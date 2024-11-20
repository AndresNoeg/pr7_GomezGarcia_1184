class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_nombre_completo(self):
        print(f"Nombre completo: {self.nombre} {self.apellido}")

class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, carrera):
        super().__init__(nombre, apellido)
        self.edad = edad
        self.carrera = carrera

    def mostrar_informacion(self):
        print(f"Carrera: {self.carrera}")
        print(f"Edad: {self.edad}")

estudiante = Estudiante("Juan", "Pérez", 22, "Ingeniería")
estudiante.mostrar_nombre_completo()
estudiante.mostrar_informacion()
