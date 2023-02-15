import numpy as np



def gauss_seidel(A, b, x0, max_iter, min_error):
    """Resuelve un sistema de ecuaciones lineales utilizando el método de Gauss-Seidel."""
    n = len(b)
    x = x0.copy()
    iter_count = 0
    error = 1
    
    while iter_count < max_iter and error > min_error:
        x_prev = x.copy()
        x_error = np.zeros(n)
        
        for i in range(n):
            # Calcula la suma de los términos de la fila i que ya han sido actualizados
            s1 = np.dot(A[i, :i], x[:i])
            
            # Calcula la suma de los términos de la fila i que aún no se han actualizado
            s2 = np.dot(A[i, i+1:], x_prev[i+1:])
            
            # Calcula el nuevo valor para x[i] a partir de las sumas y el término independiente
            x[i] = (b[i] - s1 - s2) / A[i, i]
            
            # Calcula el error relativo de la variable x[i]
            x_error[i] = np.abs((x[i] - x_prev[i]) / x[i])
        
        # Calcula el error máximo entre los errores relativos de las variables
        error = np.max(x_error)
        iter_count += 1
        
        # Imprime el número de iteración, la solución actual y el error
        print("\nIteracion: "+ str(iter_count)+ " Valores: "+ str(x) + "  Error: "+ str(error*100)+"%")
              
    # Verifica si se ha alcanzado el umbral de error mínimo
    if error <= min_error:
        print("\nEl método ha obtenido un resultado con un error menor al "+ str(min_error*100) +"% después de "+str(iter_count) +" iteraciones.")
        print("Resultado: "+ str(x) + ". En la iteracion "+ str(iter_count)+" con un error de " + str(error*100) + "%")
        return x, iter_count
    else:
        print("\nEl método de Gauss-Seidel no llega a ningún resultado antes de " +str(iter_count) + " iteraciones.")
        return None




print("Bienvenido al sistema para obtener soluciones de sistemas de ecuaciones por medio de el metodo Gauss-Seidel")
print("Ingresa el numero de ecuaciones:")
n=int(input())
print("Ingrese el porcentaje de error aceptable:")
min_error=float(input())/100
A=np.zeros((n,n))
b = np.zeros(n)
for i in range(n):
    aux_j=[]
    for j in range(n):
        print("Ingrese el valor de la incognita "+ str(j+1) + " en la ecuacion "+ str(i+1) +": [" + str(i+1) +"," + str(j+1) + "]:")
        A[i][j]=float(input())
        if j+1==n:
            print("Ingrese el resultado de la ecuacion "+ str(i+1) +" [" + str(i+1) +"," + str(j+2) + "]:")
            b[i]=float(input())
x0 = np.zeros_like(b)

solucion = gauss_seidel(A, b, x0,100,min_error)
