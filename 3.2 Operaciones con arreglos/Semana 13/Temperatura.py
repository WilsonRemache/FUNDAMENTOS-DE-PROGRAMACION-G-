# Definir los datos
ciudades = ["Ambato", "Salcedo", "Quito"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 4

# Crear una matriz 3D para almacenar las temperaturas
# Inicializamos con valores aleatorios para el ejemplo (temperaturas entre -10°C y 35°C)
temperaturas = [[[random.uniform(-10, 35) for _ in range(num_semanas)] for _ in range(len(dias_semana))] for _ in
                range(len(ciudades))]


# Función para calcular los promedios de temperatura por ciudad
def calcular_promedio_total_ciudades(temperaturas, ciudades, dias_semana, num_semanas):
    promedios_totales = {}

    for i, ciudad in enumerate(ciudades):
        suma_total_temperaturas = 0
        num_datos = len(dias_semana) * num_semanas  # Número total de temperaturas registradas por ciudad

        for semana in range(num_semanas):
            for dia in range(len(dias_semana)):
                suma_total_temperaturas += temperaturas[i][dia][semana]

        # Calcular el promedio total de la ciudad
        promedio_total = suma_total_temperaturas / num_datos
        promedios_totales[ciudad] = promedio_total

    return promedios_totales


# Calcular el promedio total de temperaturas por ciudad
promedios_ciudades = calcular_promedio_total_ciudades(temperaturas, ciudades, dias_semana, num_semanas)

# Imprimir los resultados
print("\nPromedio total de temperaturas por ciudad:")
for ciudad, promedio in promedios_ciudades.items():
    print(f"{ciudad}: {promedio:.2f}°C")
