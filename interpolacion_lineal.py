def interpolacion(x, y):
    n = len(x)
    polinomios = []
    for i in range(n-1):
        m = (y[i+1] - y[i]) / (x[i+1] - x[i])
        b = y[i] - m * x[i]
        polinomios.append((m, b, x[i], x[i+1]))
    return polinomios  # Lista de tuplas (m, b, x_inicio, x_fin)