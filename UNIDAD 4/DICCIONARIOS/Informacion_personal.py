# Crear un Diccionario
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniero"
}

# Acceder y Modificar Valores
print("Ciudad original:", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Barcelona"  # Modificar la ciudad
print("Ciudad modificada:", informacion_personal["ciudad"])

# Agregar una nueva clave-valor
informacion_personal["telefono"] = "123-456-7890"  # Agregar número de teléfono

# Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "098-765-4321"  # No debería entrar aquí ya que ya existe

# Eliminar una Clave
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminar la clave "edad"

# Imprimir el Diccionario Final
print("Diccionario final:", informacion_personal)
