import os
import sys
import numpy as np

def imprimir_matriz(m, n):

    for i in range(0, n):

        print("|", end=" ")
        
        for j in range (0, n + 1):

            print("%8d" % m[i][j], end=" ")

        print("|")

    print("")

def met_montante(A, n):
    p = 1.0
    #Elemento de la diagonal actual. Nos sirve para saber que elementos no se cambian
    for k in range(0, n):
        #Columnas
        for i in range(0, n):
            #Filas.
            for j in range(0, n + 1):
                #Checamos que no estemos en la linea o columna k.
                if j != k and i != k:
                    A[i][j] = (A[k][k] * A[i][j] - A[i][k] * A[k][j]) / p
            if i != k:
                A[i][k] = 0
        print("Pivote anterior: " + str(p))
        p = A[k][k]
        print("Pivote actual: "+str(p))

        if (p == 0):

            return 1 

        imprimir_matriz(A, n)

    return 0
       
if __name__ == "__main__":
    print("Bienvenido al sistema para obtener soluciones de sistemas de ecuaciones por medio de el metodo Montante.")
    print("Ingresa el numero de ecuaciones:")
    n=int(input())
    A=np.zeros((n,n+1))
    for i in range(n):
        for j in range(n):
            print("Ingrese el coeficiente de la incognita "+ str(j+1) + " en la ecuacion "+ str(i+1) +": [" + str(i+1) +"," + str(j+1) + "]:")
            A[i][j]=float(input())
            if j+1==n:
                print("Ingrese el termino independiente de la ecuacion "+ str(i+1) +" [" + str(i+1) +"," + str(j+2) + "]:")
                A[i][j+1]=float(input())
    #Imprimimos la matriz inicial
    print("\nMatriz inicial.")
    imprimir_matriz(A, n)
    temp=met_montante(A, n)
    if (temp==1):
        print("El sistema de ecuaciones no tiene solución.")
        sys.exit()

    results = []

    for i in range(n):

        results.append(A[i][n] / A[i][i])

    print("\nDeterminante = " + str(A[1][1]))

    for i in range(n):
        print("\nx" + str(i + 1) + "= " + str(results[i]))

    print("\n")
    os.system("pause")