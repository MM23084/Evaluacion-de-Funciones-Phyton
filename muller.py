import cmath

def evaluar_polinomio(coefs, x):
    """Evalúa un polinomio en x usando Horner."""
    res = coefs[0]
    for coef in coefs[1:]:
        res = res * x + coef
    return res

def metodo_muller(coefs, x0, x1, x2, tol=1e-6, max_iter=100, mostrar_pasos=True):
   
    for it in range(1, max_iter+1):
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

        # Discriminante para la cuadrática
        disc = cmath.sqrt(b**2 - 4*a*c)
        den1 = b + disc
        den2 = b - disc
        if abs(den1) > abs(den2):
            den = den1
        else:
            den = den2

        if den == 0:
            if mostrar_pasos:
                print(f"Iteración {it}: División por cero detectada, el método falla aquí.")
            return x2

        dxr = -2 * c / den
        xr = x2 + dxr

        if mostrar_pasos:
            print(f"\nIteracion {it}:")
            print(f"x0 = {x0}, x1 = {x1}, x2 = {x2}")
            print(f"f(x0) = {f0}, f(x1) = {f1}, f(x2) = {f2}")
            print(f"h0 = {h0}, h1 = {h1}")
            print(f"d0 = {d0}, d1 = {d1}")
            print(f"a = {a}, b = {b}, c = {c}")
            print(f"Discriminante = {disc}")
            print(f"dxr = {dxr}")
            print(f"Nueva aproximacion xr = {xr}")
            print(f"Error estimado: {abs(dxr)}")

        if abs(dxr) < tol:
            if mostrar_pasos:
                print(f"\nConvergencia alcanzada con xr = {xr} (error < {tol}) en {it} iteraciones.")
            return xr

        #aca se actualizan los puntos para el siguiente ejercicio si se requiere
        x0, x1, x2 = x1, x2, xr

    if mostrar_pasos:
        print("\nEl método no convergió después del número máximo de iteraciones.")
    return xr