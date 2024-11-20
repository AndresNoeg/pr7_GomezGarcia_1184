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


