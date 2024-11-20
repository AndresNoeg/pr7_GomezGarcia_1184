class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumpleaños(self):
        self.edad += 1

p = Persona(input("Ingrese su nombre: "), int(input("Ingrese su edad: ")))
p.cumpleaños()
print(f"¡Feliz cumpleaños, {p.nombre}! Ahora tienes {p.edad} años.")
