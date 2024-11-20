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
