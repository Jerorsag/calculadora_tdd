# Calculadora TDD en Python

Prototipo de calculadora construido siguiendo la metodología **Test-Driven Development (TDD)**.

---

## ¿Qué es TDD?

TDD es una metodología de desarrollo de software donde **los tests se escriben ANTES que el código**.
El ciclo se repite en 3 fases:

```
🔴 RED    →  Escribe un test que FALLA (porque el código aún no existe)
🟢 GREEN  →  Escribe el MÍNIMO código para que el test pase
🔵 REFACTOR → Mejora el código sin romper los tests
```

---

## Estructura del Proyecto

```
calculadora_tdd/
│
├── src/
│   ├── __init__.py
│   └── calculadora.py       # 🟢 Implementación de la Calculadora
│
├── tests/
│   ├── __init__.py
│   └── test_calculadora.py  # 🔴 Tests escritos ANTES del código
│
└── README.md
```

---

## Operaciones Implementadas

| Iteración | Operación       | Método              | Casos especiales           |
|-----------|-----------------|---------------------|----------------------------|
| 1         | Suma            | `sumar(a, b)`       | Decimales, negativos        |
| 2         | Resta           | `restar(a, b)`      | Resultado negativo          |
| 3         | Multiplicación  | `multiplicar(a, b)` | Por cero, negativos         |
| 4         | División        | `dividir(a, b)`     | ❌ División entre cero      |
| 5         | Potencia        | `potencia(b, e)`    | Exponente negativo/cero     |
| 6         | Raíz cuadrada   | `raiz_cuadrada(n)`  | ❌ Número negativo          |
| 7         | Módulo          | `modulo(a, b)`      | ❌ Divisor cero             |

---

## Cómo ejecutar los tests

### Ejecutar todos los tests con detalle:
```
python -m pytest tests/ -v
```

### Ejecutar con unittest directamente:
```
python -m unittest discover -s tests -v
```

### Ver cobertura de código:
```
pip install pytest-cov
python -m pytest tests/ --cov=src --cov-report=term-missing
```

---

## Ciclo TDD Aplicado — Ejemplo con Suma

### 🔴 Paso 1 — RED: Escribir el test PRIMERO
```python
# tests/test_calculadora.py
def test_sumar_dos_positivos(self):
    self.assertEqual(self.calc.sumar(3, 5), 8)
# ❌ FALLA → AttributeError: 'Calculadora' object has no attribute 'sumar'
```

### 🟢 Paso 2 — GREEN: Escribir el mínimo código
```python
# src/calculadora.py
def sumar(self, a, b):
    return a + b
# ✅ PASA
```

### 🔵 Paso 3 — REFACTOR: Mejorar sin romper
```python
# src/calculadora.py
def sumar(self, a: float, b: float) -> float:
    """Retorna la suma de dos números."""
    self._validar_numeros(a, b)   # ← validación reutilizable añadida
    return a + b
# ✅ PASA con código más robusto y documentado
```

---

## Resumen de Tests

| Clase de Test        | Cantidad de Tests | Descripción                        |
|----------------------|-------------------|------------------------------------|
| `TestSuma`           | 5                 | Positivos, negativos, decimales    |
| `TestResta`          | 5                 | Resultado negativo, decimales      |
| `TestMultiplicacion` | 6                 | Por cero, negativos, decimales     |
| `TestDivision`       | 6                 | Decimales, división entre cero     |
| `TestPotencia`       | 5                 | Exponente cero, negativo           |
| `TestRaizCuadrada`   | 4                 | Decimales, número negativo         |
| `TestModulo`         | 5                 | Exacto, menor que divisor          |
| `TestValidaciones`   | 5                 | TypeError con strings, None, listas|
| **TOTAL**            | **41**            |                                    |

---

## Principios TDD aplicados en este proyecto

1. **Un test a la vez** → Cada iteración agrega una nueva operación.
2. **Mínimo código** → Se escribe solo lo necesario para pasar el test.
3. **Refactor constante** → El método `_validar_numeros()` se extrajo para eliminar duplicación.
4. **Tests independientes** → `setUp()` recrea la instancia antes de cada test.
5. **Nombres descriptivos** → `test_<operacion>_<escenario>` hace los tests autodocumentados.
