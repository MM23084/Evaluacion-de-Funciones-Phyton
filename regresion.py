def regresion_lineal(x, y):
    n = len(x)
    sumx = sum(x)
    sumy = sum(y)
    sumxy = sum(xi*yi for xi, yi in zip(x, y))
    sumx2 = sum(xi*xi for xi in x)
    m = (n*sumxy - sumx*sumy) / (n*sumx2 - sumx*sumx)
    b = (sumy - m*sumx) / n
    return m, b