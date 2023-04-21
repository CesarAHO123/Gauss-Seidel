def lagrange_interpolation(x, y, xi):
    """
    Implementación del método de interpolación de Lagrange para encontrar el valor
    de una función en un punto específico.

    :param x: Lista con los valores de x conocidos.
    :param y: Lista con los valores de y conocidos correspondientes a los valores de x.
    :param xi: Valor de x para el cual se quiere conocer el valor de la función.
    :return: El valor de la función en el punto xi.
    """
    # Verificamos que los valores de x no se repitan
    if len(set(x)) != len(x):
        raise ValueError("Los valores de x no pueden estar repetidos.")

    # Verificamos que los tamaños de las listas de x e y sean iguales
    if len(x) != len(y):
        raise ValueError("Las listas de x e y deben tener el mismo tamaño.")

    # Definimos la función de interpolación de Lagrange
    n = len(x)
    result = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (xi - x[j]) / (x[i] - x[j])
        result += term

    return result
if __name__=="__main__":
    print("Bienvenido al sistema de interpolacion de Lagrange.")
    print("Ingrese los valores de X en los puntos separados con un ','")
    aux=input()
    aux=aux.split(',')
    x=[float(x) for x in aux]
    print("Ingrese los valores de Y en los puntos separados con un ','")
    aux=input()
    aux=aux.split(',')
    y=[float(y) for y in aux]
    print("Ingrese el valor de X")
    aux=input()
    xi = float(aux)
    result = lagrange_interpolation(x, y, xi)
    print("El valor de y es: "+ str(result))
