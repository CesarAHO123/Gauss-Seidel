import sympy as sym

def bisection_method(f, xi, xu, tol, max_iter):
    # Simbolizamos la función
    x = sym.Symbol('x')
    fx = sym.sympify(f)
    tol=tol/100
    # Convertimos la función simbolizada a una función numérica
    f = sym.lambdify(x, fx)
    # Comprobamos que la función tenga signos diferentes en los extremos del intervalo
    if f(xi) * f(xu) >= 0:
        print("Error: la función no cambia de signo en el intervalo dado.")
        return None
    # Inicializamos los valores iniciales para el método
    i = 1
    xr = (xi + xu) / 2
    xr_old = xr
    # Comenzamos el método de bisección
    while i <= max_iter:
        xr = (xi + xu) / 2
        fxr = f(xr)
        if i==1:
            ea = 100.00
        else:
            ea = abs((xr - xr_old) / xr) if xr != 0 else float('inf')
        print("Iteración {}: xr = {}, error aproximado = {}%".format(i, xr, ea*100))
        if ea < tol:
            return xr
        if f(xi) * fxr < 0:
            xu = xr
        elif f(xi) * fxr > 0:
            xi = xr
        else:
            return xr
        xr_old = xr
        i += 1
    print("Error: número máximo de iteraciones alcanzado.")
    return None


if __name__ == "__main__":
    print("Bienvenido al sistema para encontrar la raíz de una función por el método de bisección.")
    while True:
        print("Ingrese la función:")
        f = input()
        print("Ingrese el extremo izquierdo del intervalo:")
        xi = float(input())
        print("Ingrese el extremo derecho del intervalo:")
        xu = float(input())
        print("Ingrese la tolerancia:")
        tol = float(input())
        max_iter = 1000

        root = bisection_method(f, xi, xu, tol, max_iter)

        if root is not None:
            print("La raíz de la función es:", root)

        print("¿Desea ingresar otra ecuación? (s/n)")
        answer = input().lower()
        if answer != 's':
            break