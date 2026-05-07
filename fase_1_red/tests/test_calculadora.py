"""
============================================================
FASE 1 - RED
============================================================
Se escriben los tests ANTES de implementar el codigo.
La clase Calculadora existe pero sus metodos solo tienen pass.
Resultado esperado: TODOS LOS TESTS FALLAN  (ROJO)
============================================================
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.calculadora import Calculadora


class TestSuma(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_sumar_dos_positivos(self):
        self.assertEqual(self.calc.sumar(3, 5), 8)

    def test_sumar_dos_negativos(self):
        self.assertEqual(self.calc.sumar(-3, -5), -8)

    def test_sumar_positivo_y_negativo(self):
        self.assertEqual(self.calc.sumar(10, -3), 7)

    def test_sumar_con_cero(self):
        self.assertEqual(self.calc.sumar(7, 0), 7)

    def test_sumar_decimales(self):
        self.assertAlmostEqual(self.calc.sumar(1.5, 2.5), 4.0)


class TestResta(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_restar_dos_positivos(self):
        self.assertEqual(self.calc.restar(10, 4), 6)

    def test_restar_resultado_negativo(self):
        self.assertEqual(self.calc.restar(3, 8), -5)

    def test_restar_mismo_numero(self):
        self.assertEqual(self.calc.restar(5, 5), 0)

    def test_restar_con_cero(self):
        self.assertEqual(self.calc.restar(9, 0), 9)

    def test_restar_decimales(self):
        self.assertAlmostEqual(self.calc.restar(5.5, 2.2), 3.3, places=5)


class TestMultiplicacion(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_multiplicar_dos_positivos(self):
        self.assertEqual(self.calc.multiplicar(4, 3), 12)

    def test_multiplicar_por_cero(self):
        self.assertEqual(self.calc.multiplicar(100, 0), 0)

    def test_multiplicar_por_uno(self):
        self.assertEqual(self.calc.multiplicar(7, 1), 7)

    def test_multiplicar_negativos(self):
        self.assertEqual(self.calc.multiplicar(-4, -3), 12)

    def test_multiplicar_positivo_por_negativo(self):
        self.assertEqual(self.calc.multiplicar(5, -3), -15)

    def test_multiplicar_decimales(self):
        self.assertAlmostEqual(self.calc.multiplicar(2.5, 4.0), 10.0)


class TestDivision(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_dividir_dos_positivos(self):
        self.assertEqual(self.calc.dividir(10, 2), 5.0)

    def test_dividir_resultado_decimal(self):
        self.assertAlmostEqual(self.calc.dividir(7, 2), 3.5)

    def test_dividir_negativos(self):
        self.assertEqual(self.calc.dividir(-10, -2), 5.0)

    def test_dividir_positivo_por_negativo(self):
        self.assertEqual(self.calc.dividir(10, -2), -5.0)

    def test_dividir_cero_entre_numero(self):
        self.assertEqual(self.calc.dividir(0, 5), 0.0)

    def test_dividir_entre_cero_lanza_excepcion(self):
        with self.assertRaises(ValueError) as ctx:
            self.calc.dividir(10, 0)
        self.assertIn("cero", str(ctx.exception).lower())


class TestPotencia(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_potencia_base_positiva(self):
        self.assertEqual(self.calc.potencia(2, 3), 8)

    def test_potencia_exponente_cero(self):
        self.assertEqual(self.calc.potencia(99, 0), 1)

    def test_potencia_base_cero(self):
        self.assertEqual(self.calc.potencia(0, 5), 0)

    def test_potencia_exponente_negativo(self):
        self.assertAlmostEqual(self.calc.potencia(2, -1), 0.5)

    def test_potencia_base_negativa(self):
        self.assertEqual(self.calc.potencia(-2, 3), -8)


class TestRaizCuadrada(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_raiz_cuadrada_numero_positivo(self):
        self.assertAlmostEqual(self.calc.raiz_cuadrada(9), 3.0)

    def test_raiz_cuadrada_de_cero(self):
        self.assertEqual(self.calc.raiz_cuadrada(0), 0.0)

    def test_raiz_cuadrada_decimal(self):
        self.assertAlmostEqual(self.calc.raiz_cuadrada(2), 1.41421, places=4)

    def test_raiz_cuadrada_negativo_lanza_excepcion(self):
        with self.assertRaises(ValueError) as ctx:
            self.calc.raiz_cuadrada(-4)
        self.assertIn("negativo", str(ctx.exception).lower())


class TestModulo(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_modulo_basico(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_divisible_exacto(self):
        self.assertEqual(self.calc.modulo(9, 3), 0)

    def test_modulo_numero_menor_que_divisor(self):
        self.assertEqual(self.calc.modulo(3, 10), 3)

    def test_modulo_cero_dividido(self):
        self.assertEqual(self.calc.modulo(0, 5), 0)

    def test_modulo_divisor_cero_lanza_excepcion(self):
        with self.assertRaises(ValueError) as ctx:
            self.calc.modulo(10, 0)
        self.assertIn("cero", str(ctx.exception).lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
