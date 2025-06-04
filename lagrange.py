def polinomio_lagrange(x, y):
    n = len(x)
    def L(k, X):
        resultado = 1
        for i in range(n):
            if i != k:
                resultado *= (X - x[i]) / (x[k] - x[i])
        return resultado
    def P(X):
        return sum(y[k] * L(k, X) for k in range(n))
    return P  # Retorna la función polinómica

def evaluar_lagrange(x, y, valor):
    P = polinomio_lagrange(x, y)
    return P(valor)