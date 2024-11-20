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
