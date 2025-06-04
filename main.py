import horner
import muller
import interpolacion_lineal
import lagrange
import regresion

def pedir_coeficientes():
    coefs = []
    print("Introduce los coeficientes del polinomio (de mayor a menor grado). Escribe 'fin' para terminar:")
    while True:
        entrada = input(f"Coeficiente {len(coefs)+1}: ")
        if entrada.lower() == "fin":
            break
        try:
            coefs.append(float(entrada))
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")
    return coefs

def pedir_lista_datos(nombre="valor"):
    datos = []
    print(f"Introduce los {nombre}s. Escribe 'fin' para terminar:")
    while True:
        entrada = input(f"{nombre.title()} {len(datos)+1}: ")
        if entrada.lower() == "fin":
            break
        try:
            datos.append(float(entrada))
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")
    return datos

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Evaluación polinomial por Horner")
        print("2. Determinación de raíces por el método de Muller")
        print("3. Determinación de polinomios por interpolación lineal")
        print("4. Evaluación polinomial por el método de LaGrange")
        print("5. Determinación de polinomios de LaGrange")
        print("6. Regresión lineal por mínimos cuadrados")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            coefs = pedir_coeficientes()
            x = float(input("Introduce el valor de x: "))
            resultado = horner.evaluar_polinomio(coefs, x)
            print(f"Resultado: {resultado}")

        elif opcion == '2':
            coefs = pedir_coeficientes()
            x0 = float(input("Introduce x0: "))
            x1 = float(input("Introduce x1: "))
            x2 = float(input("Introduce x2: "))
            raiz = muller.metodo_muller(coefs, x0, x1, x2)
            print(f"Raíz aproximada: {raiz}")

        elif opcion == '3':
            x = pedir_lista_datos("x")
            y = pedir_lista_datos("y")
            polinomio = interpolacion_lineal.interpolacion(x, y)
            print(f"Polinomio interpolante: {polinomio}")

        elif opcion == '4':
            x = pedir_lista_datos("x")
            y = pedir_lista_datos("y")
            valor = float(input("Introduce el valor de x a evaluar: "))
            resultado = lagrange.evaluar_lagrange(x, y, valor)
            print(f"Resultado: {resultado}")

        elif opcion == '5':
            x = pedir_lista_datos("x")
            y = pedir_lista_datos("y")
            polinomio = lagrange.polinomio_lagrange(x, y)
            print(f"Polinomio de Lagrange: {polinomio}")

        elif opcion == '6':
            x = pedir_lista_datos("x")
            y = pedir_lista_datos("y")
            m, b = regresion.regresion_lineal(x, y)
            print(f"Recta ajustada: y = {m}x + {b}")

        elif opcion == '0':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()