def evaluar_polinomio(coefs, x):
    resultado = coefs[0]
    for coef in coefs[1:]:
        resultado = resultado * x + coef
    return resultado