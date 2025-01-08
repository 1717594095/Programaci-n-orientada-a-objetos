# Ejemplo de Buenos Identificadores en Python

# Buen identificador para una variable que almacena la cantidad de vehiculos en un parqueadero
cantidad_tiempo = 8

# Buen identificador para una función que crea un nuevo ingreso
def crear_ingreso(modelo, hora):
    nuevo_ingreso = {'modelo': modelo, 'hora': hora}
    return nuevo_ingreso

# Buen identificador para una variable que almacena el precio total del parqueadero
precio_total = 20

# Uso de los identificadores en un contexto de código
print(f"Cantidad de tiempo: {cantidad_tiempo}")
usuario = crear_ingreso("toyota", 5)
print(f"Usuario creado: {usuario['modelo']} con hora {usuario['hora']}")
print(f"Precio total del parqueadero: {precio_total}")