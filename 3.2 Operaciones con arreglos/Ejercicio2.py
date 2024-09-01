# Programa 2: Ordenación de Arreglo Multidimensional

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambiar


def ordenar_fila(matriz, fila_a_ordenar):
    print("Matriz original:")
    for fila in matriz:
        print(fila)

    bubble_sort(matriz[fila_a_ordenar])

    print("\nMatriz después de ordenar la fila:")
    for fila in matriz:
        print(fila)


# Matriz de ejemplo 3x3
matriz = [
    [9, 2, 3],
    [4, 5, 1],
    [7, 8, 6]
]

# Fila a ordenar (0, 1 o 2)
fila_a_ordenar = 1
ordenar_fila(matriz, fila_a_ordenar)
