# pr7_GomezGarcia_1184

class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre} \nNota: {self.nota}")

    def resultados(self):
        if self.nota >= 7:
            print(f"{self.nombre}, ¡Felicidades! Has aprobado.")
        else:
            print(f"{self.nombre}, no has aprobado. ¡Ánimo!")

estudiante1 = Estudiante("Pedro", 5)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2 = Estudiante("Elizabeth", 7)
estudiante2.imprimir()
estudiante2.resultados()

![image](https://github.com/user-attachments/assets/5ec738f4-3ec1-4622-b314-63312e1a317c)

![image](https://github.com/user-attachments/assets/4e0acdfe-44f3-453c-8a22-a6db851ccac6)

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumpleaños(self):
        self.edad += 1

p = Persona(input("Ingrese su nombre: "), int(input("Ingrese su edad: ")))
p.cumpleaños()
print(f"¡Feliz cumpleaños, {p.nombre}! Ahora tienes {p.edad} años.")

![image](https://github.com/user-attachments/assets/98e2f310-93bc-415a-ac2b-9a04ec68b657)

![image](https://github.com/user-attachments/assets/f74dbf08-7652-4647-951d-921ace81844f)

class Calculadora():
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def realizar_suma(self):
        resultado = self._num1 + self._num2
        print(f"Resultado de la suma: {self._num1} + {self._num2} = {resultado}")

    def realizar_resta(self):
        resultado = self._num1 - self._num2
        print(f"Resultado de la resta: {self._num1} - {self._num2} = {resultado}")

    def realizar_division(self):
        resultado = self._num1 / self._num2
        print(f"Resultado de la división: {self._num1} / {self._num2} = {resultado}")

    def realizar_multiplicacion(self):
        resultado = self._num1 * self._num2
        print(f"Resultado de la multiplicación: {self._num1} * {self._num2} = {resultado}")

operacion = Calculadora(10, 5)
operacion.realizar_suma()
operacion.realizar_resta()
operacion.realizar_division()
operacion.realizar_multiplicacion()

![image](https://github.com/user-attachments/assets/b9975d47-e55c-4a9e-86df-e96f517851d4)

![image](https://github.com/user-attachments/assets/9f6dc237-7269-4625-ba49-df8875070f55)

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

![image](https://github.com/user-attachments/assets/e02ddb02-b581-491a-93ad-fe543686ee25)

![image](https://github.com/user-attachments/assets/3972457a-5d0b-4584-b30d-39b2169caea8)

class Fabrica():
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio

class Moto(Fabrica):
    def mostrar_informacion(self):
        print(f"Moto: {self._llantas} llantas, Color: {self._color}, Precio: {self._precio}")

class Carro(Fabrica):
    def mostrar_informacion(self):
        print(f"Carro: {self._llantas} llantas, Color: {self._color}, Precio: {self._precio}")

moto = Moto(2, "Gris", "$200")
moto.mostrar_informacion()

carro = Carro(4, "Negro", "$600")
carro.mostrar_informacion()

![image](https://github.com/user-attachments/assets/d345f742-9841-4fe1-8fa3-5f3ed4c81cfa)

![image](https://github.com/user-attachments/assets/4d60c7bb-138e-4766-9c68-41a79810a3da)

class Marino():
    def hablar(self):
        print("¡Hola! Soy un animal marino.")

class Pulpo(Marino):
    def hablar(self):
        print("¡Hola! Soy un pulpo.")

class Foca(Marino):
    def hablar(self, mensaje):
        print(mensaje)

marino = Marino()
marino.hablar()

pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar("¡Hola! Soy una foca.")

![image](https://github.com/user-attachments/assets/ee65dd4e-be37-477c-bc6c-30401feb1275)

![image](https://github.com/user-attachments/assets/1ce67e11-0625-43da-8dc6-8405455967f5)

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

![image](https://github.com/user-attachments/assets/7472dd34-318c-46ed-b5ff-acdfbb87d615)

![image](https://github.com/user-attachments/assets/65856a22-7133-4f7e-9cc4-02ecf6a1df81)
















