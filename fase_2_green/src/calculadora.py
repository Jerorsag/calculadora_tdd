# ============================================================
# FASE 2 - GREEN
# ============================================================
# Se escribe el MINIMO codigo necesario para que los tests pasen.
# Sin documentacion, sin validaciones extras, sin type hints.
# Solo la logica justa y necesaria.
# Resultado esperado al ejecutar: TODOS LOS TESTS PASAN (VERDE)
# ============================================================


class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero.")
        return a / b

    def potencia(self, base, exponente):
        return base**exponente

    def raiz_cuadrada(self, numero):
        if numero < 0:
            raise ValueError("El numero no puede ser negativo.")
        return numero**0.5

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("El divisor no puede ser cero.")
        return a % b
