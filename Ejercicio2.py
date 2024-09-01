# Programa 2: Ordenación de Arreglo Multidimensional

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]  # Intercambiar

# Definimos una matriz 3x3
matriz = [
    [3, 1, 2],
    [6, 5, 4],
    [9, 7, 8]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila (índice 1)
bubble_sort(matriz[1])

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la segunda fila ordenada:")
for fila in matriz:
    print(fila)
