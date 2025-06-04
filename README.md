# CORTO 2 -  Cálculo numérico para desarrollo de aplicaciones CDA135

**Repositorio:** MM23084/Evaluacion-de-Funciones-Phyton

## Descripción general

Este proyecto contiene una colección de programas en Python desarrollados para resolver distintos problemas de cálculo numérico, como la evaluación de polinomios, determinación de raíces, interpolación y regresión lineal. El objetivo es ofrecer implementaciones didácticas y funcionales de estos algoritmos, facilitando su comprensión y aplicación.

## Contenido y estructura

El proyecto está compuesto por varios módulos, cada uno centrado en un método específico:

- **main.py**: Menú principal que permite al usuario seleccionar y ejecutar los diferentes métodos implementados.
- **horner.py**: Implementa el método de Horner para evaluar polinomios.
- **muller.py**: Implementa el método de Muller para encontrar raíces de polinomios.
- **interpolacion_lineal.py**: Realiza interpolación lineal por tramos.
- **lagrange.py**: Calcula el polinomio interpolante de Lagrange y lo evalúa en un punto dado.
- **regresion.py**: Implementa la regresión lineal por mínimos cuadrados.

## Instrucciones de uso

1. **Requisitos**
   - Python 3.x instalado.
   - No requiere librerías externas, salvo la librería estándar `cmath` (usada en muller.py).
   
2. **Ejecución**
   - Ejecutar el archivo principal:
     ```bash
     python main.py
     ```
   - Seguir las instrucciones del menú para elegir el método deseado e ingresar los datos solicitados.

3. **Opciones del menú**
 A continuación se presentan ejemplos prácticos para comprobar el correcto funcionamiento de cada módulo principal:

### 1. Evaluación polinomial por Horner

- **Entrada:**  
  Coeficientes del polinomio: `[2, -3, 1]` (corresponde a \(2x^2 - 3x + 1\))  
  Valor de \(x\): `4`
- **Salida esperada:**  
  `Resultado: 13`

### 2. Determinación de raíces por el método de Muller

- **Entrada:**  
  Coeficientes del polinomio: `[1, 0, -1]` (corresponde a \(x^2 - 1\))  
  \(x_0 = 0\), \(x_1 = 1\), \(x_2 = 2\)
- **Salida esperada:**  
  `Raíz aproximada: 1.0`  
  *(El método también puede encontrar la raíz -1 dependiendo de los puntos iniciales)*

### 3. Determinación de polinomios por interpolación lineal

- **Entrada:**  
  Lista de \(x\): `[1, 2, 3]`  
  Lista de \(y\): `[2, 3, 5]`
- **Salida esperada:**  
  `Polinomio interpolante: [(1.0, 1.0, 1, 2), (2.0, -1.0, 2, 3)]`  
  *(Cada tupla representa (pendiente, intersección, x_inicio, x_fin))*

### 4. Evaluación polinomial por el método de Lagrange

- **Entrada:**  
  Lista de \(x\): `[0, 1, 2]`  
  Lista de \(y\): `[1, 3, 2]`  
  Valor a evaluar: `1.5`
- **Salida esperada:**  
  `Resultado: 2.375`  
  *(El polinomio de Lagrange evaluado en 1.5)*

### 5. Determinación de polinomios de Lagrange

- **Entrada:**  
  Lista de \(x\): `[0, 1, 2]`  
  Lista de \(y\): `[1, 3, 2]`
- **Salida esperada:**  
  `Polinomio de Lagrange: <function polinomio_lagrange.<locals>.P at 0x...>`  
  *(Se obtiene una función que puede ser evaluada en cualquier valor de x)*

### 6. Regresión lineal por mínimos cuadrados

- **Entrada:**  
  Lista de \(x\): `[1, 2, 3, 4, 5]`  
  Lista de \(y\): `[2, 4, 5, 4, 5]`
- **Salida esperada:**  
  `Recta ajustada: y = 0.7x + 1.7`

---

> **Nota:** Para probar cada función, ejecuta `python main.py` y selecciona la opción correspondiente en el menú. Ingresa los datos de ejemplo y verifica que la salida coincida con lo esperado.


## Créditos y contacto

- Autor: MM23084 - Ricardo Antonio Mora Morales
- Curso: Cálculo numérico

