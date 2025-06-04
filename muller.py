import cmath

def evaluar_polinomio(coefs, x):
    resultado = coefs[0]
    for coef in coefs[1:]:
        resultado = resultado * x + coef
    return resultado

def metodo_muller(coefs, x0, x1, x2, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        f0 = evaluar_polinomio(coefs, x0)
        f1 = evaluar_polinomio(coefs, x1)
        f2 = evaluar_polinomio(coefs, x2)
        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (f1 - f0) / h0
        d1 = (f2 - f1) / h1
        a = (d1 - d0) / (h1 + h0)
        b = a * h1 + d1
        c = f2
        disc = cmath.sqrt(b**2 - 4*a*c)
        if abs(b + disc) > abs(b - disc):
            den = b + disc
        else:
            den = b - disc
        if den == 0:
            return x2
        dxr = -2 * c / den
        xr = x2 + dxr
        if abs(dxr) < tol:
            return xr
        x0, x1, x2 = x1, x2, xr
    return xr