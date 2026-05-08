# Calculadora TDD — Python

[![CI — Calculadora TDD](https://github.com/TU_USUARIO/calculadora_tdd/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/TU_USUARIO/calculadora_tdd/actions/workflows/ci.yml)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/tested%20with-pytest-orange)](https://pytest.org)
[![TDD](https://img.shields.io/badge/metodología-TDD-green)](https://en.wikipedia.org/wiki/Test-driven_development)

> Prototipo académico de calculadora en Python desarrollado bajo la metodología
> **Test-Driven Development (TDD)** con integración continua automatizada mediante **GitHub Actions**.

---

## Tabla de contenidos

1. [¿Qué es TDD?](#qué-es-tdd)
2. [Estructura del proyecto](#estructura-del-proyecto)
3. [Fases del ciclo TDD](#fases-del-ciclo-tdd)
4. [Operaciones implementadas](#operaciones-implementadas)
5. [Cómo ejecutar los tests](#cómo-ejecutar-los-tests)
6. [CI/CD con GitHub Actions](#cicd-con-github-actions)
7. [Cómo interpretar el pipeline](#cómo-interpretar-el-pipeline)
8. [Cómo activar el pipeline](#cómo-activar-el-pipeline)
9. [Mejoras futuras del pipeline](#mejoras-futuras-del-pipeline)

---

## ¿Qué es TDD?

TDD es una metodología donde **los tests se escriben antes del código**.
El ciclo se repite de forma iterativa en 3 fases:

```
🔴 RED      →  Escribe un test que FALLA (el código aún no existe)
🟢 GREEN    →  Escribe el MÍNIMO código para que el test pase
🔵 REFACTOR →  Mejora el código sin romper ningún test
```

---

## Estructura del proyecto

```
calculadora_tdd/
│
├── .github/
│   └── workflows/
│       └── ci.yml              ← Pipeline de CI/CD (GitHub Actions)
│
├── fase_1_red/
│   ├── src/
│   │   ├── __init__.py
│   │   └── calculadora.py      ← Métodos stub (solo pass)
│   └── tests/
│       ├── __init__.py
│       └── test_calculadora.py ← 36 tests → TODOS FALLAN
│
├── fase_2_green/
│   ├── src/
│   │   ├── __init__.py
│   │   └── calculadora.py      ← Lógica mínima implementada
│   └── tests/
│       ├── __init__.py
│       └── test_calculadora.py ← 36 tests → TODOS PASAN
│
├── fase_3_refactor/
│   ├── src/
│   │   ├── __init__.py
│   │   └── calculadora.py      ← Código limpio + validaciones
│   └── tests/
│       ├── __init__.py
│       └── test_calculadora.py ← 43 tests → TODOS PASAN
│
├── pytest.ini                  ← Configuración de pytest
├── requirements.txt            ← Dependencias del proyecto
└── README.md
```

---

## Fases del ciclo TDD

### 🔴 Fase 1 — RED

Los métodos de la calculadora existen pero solo contienen `pass`.
Los tests se escriben primero y **todos fallan**.

```
FAILED test_sumar_dos_positivos  → AssertionError: None != 8
FAILED test_dividir_dos_positivos → AssertionError: None != 5.0
...
FAILED (failures=29, errors=7)
```

### 🟢 Fase 2 — GREEN

Se implementa la lógica **mínima necesaria** para que los tests pasen.
Sin docstrings, sin type hints, sin validación de tipos.

```
test_sumar_dos_positivos   PASSED
test_dividir_dos_positivos PASSED
...
36 passed in 0.01s
```

### 🔵 Fase 3 — REFACTOR

Se mejora el código sin romper ningún test:
- Type hints en todos los métodos
- Docstrings descriptivos
- Método privado `_validar_numeros()` para eliminar duplicación
- 7 tests nuevos de `TestValidaciones` agregados en esta fase

```
test_sumar_dos_positivos              PASSED
...
test_sumar_con_string_lanza_type_error PASSED
43 passed in 0.01s
```

---

## Operaciones implementadas

| Iteración | Operación      | Método              | Casos especiales       |
|-----------|----------------|---------------------|------------------------|
| 1         | Suma           | `sumar(a, b)`       | Decimales, negativos   |
| 2         | Resta          | `restar(a, b)`      | Resultado negativo     |
| 3         | Multiplicación | `multiplicar(a, b)` | Por cero, negativos    |
| 4         | División       | `dividir(a, b)`     | ValueError si b == 0   |
| 5         | Potencia       | `potencia(b, e)`    | Exponente negativo     |
| 6         | Raíz cuadrada  | `raiz_cuadrada(n)`  | ValueError si n < 0    |
| 7         | Módulo         | `modulo(a, b)`      | ValueError si b == 0   |

---

## Cómo ejecutar los tests

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar fase específica

```bash
# Fase RED — todos deben fallar
python -m pytest fase_1_red/tests/ -v

# Fase GREEN — todos deben pasar
python -m pytest fase_2_green/tests/ -v

# Fase REFACTOR — todos deben pasar (por defecto con pytest.ini)
python -m pytest fase_3_refactor/tests/ -v
```

### Ejecutar con cobertura de código

```bash
python -m pytest fase_3_refactor/tests/ \
  --cov=fase_3_refactor/src \
  --cov-report=term-missing
```

---

## CI/CD con GitHub Actions

### ¿Qué es CI/CD?

**CI (Continuous Integration)** es la práctica de integrar y validar
automáticamente cada cambio de código mediante un pipeline que ejecuta
tests, análisis y otras verificaciones sin intervención humana.

**CD (Continuous Delivery/Deployment)** extiende la CI para publicar
o desplegar el software automáticamente si todas las validaciones pasan.

### Arquitectura del pipeline

```
 Push / Pull Request → rama main
          │
          ▼
 ┌──────────────────────────────────────────┐
 │   JOB 1: pruebas-unitarias               │
 │   runs-on: ubuntu-latest / Python 3.11   │
 │                                          │
 │   STEP 1 → Checkout del repositorio      │
 │   STEP 2 → Configurar Python 3.11        │
 │   STEP 3 → Instalar dependencias         │
 │   STEP 4 → Verificar entorno             │
 │   STEP 5 → Ejecutar pytest (43 tests)    │
 │   STEP 6 → Reporte de cobertura (≥ 80%)  │
 │   STEP 7 → Publicar artefacto XML        │
 └────────────────────┬─────────────────────┘
                      │  needs (solo si Job 1 es exitoso)
                      ▼
 ┌──────────────────────────────────────────┐
 │   JOB 2: validacion-ciclo-tdd            │
 │   runs-on: ubuntu-latest / Python 3.11   │
 │                                          │
 │   STEP 1 → Checkout + setup + deps       │
 │   STEP 2 → [RED]     Fase 1 (falla OK)   │
 │   STEP 3 → [GREEN]   Fase 2 (debe pasar) │
 │   STEP 4 → [REFACTOR]Fase 3 (debe pasar) │
 │   STEP 5 → Resumen del ciclo TDD         │
 └──────────────────────────────────────────┘
```

### Beneficios de CI en proyectos TDD

| Beneficio | Descripción |
|---|---|
| **Detección inmediata** | Si un commit rompe un test, el pipeline falla antes de que el código llegue a main |
| **Feedback rápido** | El desarrollador sabe en minutos si su cambio es correcto |
| **Historial de calidad** | Cada ejecución queda registrada con su resultado en GitHub |
| **Cobertura automática** | El pipeline mide y exige un mínimo de cobertura (80%) en cada push |
| **Integración continua** | Garantiza que el código siempre está en un estado funcional y testeable |
| **Documentación viva** | El badge en el README refleja en tiempo real el estado del proyecto |

---

## Cómo interpretar el pipeline

### Ver los workflows en GitHub

1. Ir al repositorio en GitHub
2. Hacer clic en la pestaña **Actions**
3. Seleccionar el workflow **CI — Calculadora TDD**
4. Hacer clic en cualquier ejecución para ver el detalle

### Pipeline exitoso ✅

```
CI — Calculadora TDD
│
├── ✅  pruebas-unitarias          (45s)
│   ├── ✅  Checkout del repositorio
│   ├── ✅  Configurar Python 3.11
│   ├── ✅  Instalar dependencias
│   ├── ✅  Verificar entorno Python
│   ├── ✅  Ejecutar pruebas unitarias — Fase REFACTOR
│   ├── ✅  Reporte de cobertura de codigo
│   └── ✅  Publicar reporte de cobertura como artefacto
│
└── ✅  validacion-ciclo-tdd       (30s)
    ├── ✅  [RED]      Fase 1 — falla correctamente
    ├── ✅  [GREEN]    Fase 2 — 36 tests pasan
    ├── ✅  [REFACTOR] Fase 3 — 43 tests pasan
    └── ✅  Resumen del ciclo TDD completado
```

El badge del README mostrará: `CI — passing`

### Pipeline fallido ❌

```
CI — Calculadora TDD
│
├── ❌  pruebas-unitarias
│   ├── ✅  Checkout del repositorio
│   ├── ✅  Configurar Python 3.11
│   ├── ✅  Instalar dependencias
│   ├── ✅  Verificar entorno Python
│   └── ❌  Ejecutar pruebas unitarias — Fase REFACTOR
│           AssertionError: 8 != 9
│
└── ⏭️  validacion-ciclo-tdd  ← OMITIDO (Job 1 falló)
```

El badge mostrará: `CI — failing`

**Pasos para diagnosticar un fallo:**
1. Clic en el job fallido → clic en el step rojo
2. Leer el traceback en el log (pytest lo muestra con `--tb=short`)
3. Corregir el código localmente, hacer commit y push
4. El pipeline se re-ejecuta automáticamente

---

## Cómo activar el pipeline

### Método 1 — Push directo a main

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/calculadora_tdd.git
cd calculadora_tdd

# 2. Crear o modificar cualquier archivo
# (Por ejemplo, agregar un comentario en calculadora.py)

# 3. Hacer commit y push → el pipeline se dispara automáticamente
git add .
git commit -m "feat: agregar comentarios en calculadora"
git push origin main
```

### Método 2 — Pull Request

```bash
# 1. Crear una rama de trabajo
git checkout -b feature/nueva-operacion

# 2. Hacer cambios y commit
git add .
git commit -m "feat: agregar operacion logaritmo"
git push origin feature/nueva-operacion

# 3. Abrir Pull Request hacia main en GitHub
# → El pipeline se ejecuta automáticamente sobre el PR
# → GitHub bloquea el merge si el pipeline falla
```

### Método 3 — Ejecución manual desde GitHub UI

1. Ir a **Actions** → **CI — Calculadora TDD**
2. Hacer clic en **Run workflow**
3. Seleccionar rama `main` → **Run workflow**

---

## Resumen de tests

| Clase de test        | Tests | Fase       | Descripción                         |
|----------------------|-------|------------|-------------------------------------|
| `TestSuma`           | 5     | RED→REFACTOR | Positivos, negativos, decimales   |
| `TestResta`          | 5     | RED→REFACTOR | Resultado negativo, decimales     |
| `TestMultiplicacion` | 6     | RED→REFACTOR | Por cero, negativos, decimales    |
| `TestDivision`       | 6     | RED→REFACTOR | Decimales, ValueError por cero    |
| `TestPotencia`       | 5     | RED→REFACTOR | Exponente cero/negativo           |
| `TestRaizCuadrada`   | 4     | RED→REFACTOR | Decimal, ValueError en negativos  |
| `TestModulo`         | 5     | RED→REFACTOR | Exacto, divisor cero              |
| `TestValidaciones`   | 7     | REFACTOR     | TypeError con tipos inválidos     |
| **TOTAL**            | **43**|              |                                   |

---

## Mejoras futuras del pipeline

Las siguientes mejoras están preparadas como comentarios en `ci.yml`
y pueden activarse descomentando el bloque correspondiente:

| Mejora | Herramienta | Descripción |
|---|---|---|
| **Linting** | `flake8` | Verifica estilo PEP8 y errores de sintaxis |
| **Formato** | `black` | Formatea el código automáticamente |
| **Tipos** | `mypy` | Análisis estático de type hints |
| **Seguridad** | `bandit` | Detecta vulnerabilidades en el código |
| **Matrix testing** | pytest + matrix | Ejecuta los tests en Python 3.10, 3.11 y 3.12 |
| **Cobertura online** | Codecov | Publica el reporte de cobertura en codecov.io |
| **Docker** | Docker Build | Empaqueta la aplicación en una imagen Docker |
| **Despliegue** | GitHub Releases | Publica releases automáticos al pasar todos los checks |

---

> Proyecto académico — Ingeniería de Software | Metodología TDD + DevOps
