import sympy as sym

def newton_raphson(f, x0, tol, max_iter):
    """
    Implementación del método de Newton-Raphson para encontrar la raíz de una función.

    :param f: La función a la que se le buscará la raíz.
    :param x0: Valor inicial para comenzar el método.
    :param tol: La tolerancia o error aceptable para terminar el método.
    :param max_iter: El número máximo de iteraciones permitidas antes de terminar el método.
    :return: La aproximación a la raíz de la función.
    """
    # Simbolizamos la función y obtenemos su derivada
    x = sym.Symbol('x')
    fx = sym.sympify(f)
    dfx = sym.diff(fx, x)
    print(fx)
    print(dfx)

    # Convertimos la función simbolizada y su derivada a funciones numéricas
    f = sym.lambdify(x, fx)
    df = sym.lambdify(x, dfx)

    # Comenzamos el método de Newton-Raphson
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        dfx = df(x)
        if dfx == 0:
            print("Error: la derivada de la función es cero.")
            return None
        x = x - fx / dfx
    print("Error: número máximo de iteraciones alcanzado.")
    return None


if __name__ == "__main__":
    print("Bienvenido al sistema para la raiz de una ecuacion por ----")
  
    print("Ingresa la ecuacion:")
    f=input()

    aux=0

    x0 = 1.5
    tol = 1e-6
    max_iter = 100

    root = newton_raphson(f, x0, tol, max_iter)

    print("La raíz de la función es:", root)
