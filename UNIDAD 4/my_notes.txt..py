# Escritura de Archivo de Texto
# Creamos un nuevo archivo llamado my_notes.txt
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales
    file.write("Esta es mi primera nota.\n")
    file.write("Aquí está mi segunda nota.\n")
    file.write("Y esta es mi tercera nota.\n")

# Lectura de Archivo de Texto
# Abrimos el archivo my_notes.txt
with open('my_notes.txt', 'r') as file:
    # Leemos el contenido del archivo línea por línea
    for line in file:
        # Mostramos cada línea leída en la consola
        print(line.strip())  # strip() elimina los saltos de línea

# No es necesario cerrar el archivo manualmente al usar 'with', se cierra automáticamente.
