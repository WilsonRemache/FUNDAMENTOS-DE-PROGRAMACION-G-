# Programa 1: Búsqueda en Arreglo Multidimensional

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición (fila, columna)
    return None  # Si no se encuentra el valor

# Definimos una matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar
valor_a_buscar = 5
resultado = buscar_valor(matriz, valor_a_buscar)

if resultado:
    print(f"El valor {valor_a_buscar} se encontró en la posición: {resultado}")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
