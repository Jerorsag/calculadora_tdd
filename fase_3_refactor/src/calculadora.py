# ============================================================
# FASE 3 - REFACTOR
# ============================================================
# Se mejora el codigo sin romper ningun test existente.
# Cambios aplicados en el refactor:
#   1. Type hints en todos los metodos
#   2. Docstrings descriptivos
#   3. Metodo privado _validar_numeros() para eliminar duplicacion
#   4. Mensajes de error mas descriptivos y consistentes
# Resultado esperado al ejecutar: TODOS LOS TESTS PASAN (VERDE)
#   Incluye los nuevos tests de TestValidaciones agregados en esta fase.
# ============================================================


class Calculadora:
    """
    Calculadora con operaciones aritmeticas basicas.
    Valida los tipos de entrada y lanza excepciones descriptivas.
    """

    def sumar(self, a: float, b: float) -> float:
        """Retorna la suma de dos numeros."""
        self._validar_numeros(a, b)
        return a + b

    def restar(self, a: float, b: float) -> float:
        """Retorna la diferencia entre dos numeros (a - b)."""
        self._validar_numeros(a, b)
        return a - b

    def multiplicar(self, a: float, b: float) -> float:
        """Retorna el producto de dos numeros."""
        self._validar_numeros(a, b)
        return a * b

    def dividir(self, a: float, b: float) -> float:
        """
        Retorna el cociente de dos numeros (a / b).

        Raises:
            ValueError: Si el divisor b es cero.
        """
        self._validar_numeros(a, b)
        if b == 0:
            raise ValueError("Error: No se puede dividir entre cero.")
        return a / b

    def potencia(self, base: float, exponente: float) -> float:
        """Retorna base elevada al exponente."""
        self._validar_numeros(base, exponente)
        return base**exponente

    def raiz_cuadrada(self, numero: float) -> float:
        """
        Retorna la raiz cuadrada de un numero.

        Raises:
            ValueError: Si el numero es negativo.
        """
        self._validar_numeros(numero)
        if numero < 0:
            raise ValueError(
                "Error: No se puede calcular la raiz cuadrada de un numero negativo."
            )
        return numero**0.5

    def modulo(self, a: float, b: float) -> float:
        """
        Retorna el residuo de la division entera (a % b).

        Raises:
            ValueError: Si el divisor b es cero.
        """
        self._validar_numeros(a, b)
        if b == 0:
            raise ValueError("Error: El divisor no puede ser cero.")
        return a % b

    # ----------------------------------------------------------
    # Metodo privado extraido en el REFACTOR para evitar
    # repetir la misma logica de validacion en cada metodo.
    # ----------------------------------------------------------
    def _validar_numeros(self, *args) -> None:
        """
        Valida que todos los argumentos sean numericos (int o float).

        Raises:
            TypeError: Si algun argumento no es un numero.
        """
        for valor in args:
            if not isinstance(valor, (int, float)):
                raise TypeError(
                    f"Error: Se esperaba un numero, pero se recibio '{type(valor).__name__}'."
                )
