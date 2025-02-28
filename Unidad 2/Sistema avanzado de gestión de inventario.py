import json

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos (ID como clave)

    # Añadir un nuevo producto
    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: Ya existe un producto con este ID.")
        else:
            self.productos[producto.id_producto] = producto
            print(f"Producto '{producto.nombre}' añadido correctamente.")

    # Eliminar un producto por ID
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            eliminado = self.productos.pop(id_producto)
            print(f"Producto '{eliminado.nombre}' eliminado correctamente.")
        else:
            print("Error: No se encontró un producto con este ID.")

    # Actualizar cantidad o precio de un producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print(f"Producto '{producto.nombre}' actualizado correctamente.")
        else:
            print("Error: No se encontró un producto con este ID.")

    # Buscar y mostrar productos por nombre
    def buscar_producto_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            print("Productos encontrados:")
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    # Mostrar todos los productos
    def mostrar_todos_los_productos(self):
        if self.productos:
            print("Inventario completo:")
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    # Guardar inventario en un archivo
    def guardar_en_archivo(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id: vars(p) for id, p in self.productos.items()}, f)
        print(f"Inventario guardado en '{archivo}'.")

    # Cargar inventario desde un archivo
    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
                self.productos = {id: Producto(**info) for id, info in datos.items()}
            print(f"Inventario cargado desde '{archivo}'.")
        except FileNotFoundError:
            print(f"Error: El archivo '{archivo}' no existe.")
        except json.JSONDecodeError:
            print(f"Error: El archivo '{archivo}' está corrupto o vacío.")

def menu():
    inventario = Inventario()
    archivo = "inventario.json"

    # Intentar cargar el inventario desde el archivo al iniciar
    inventario.cargar_desde_archivo(archivo)

    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos_los_productos()

        elif opcion == "6":
            inventario.guardar_en_archivo(archivo)

        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()