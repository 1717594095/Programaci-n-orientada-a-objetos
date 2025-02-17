import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

    @staticmethod
    def from_string(data):
        id_producto, nombre, cantidad, precio = data.strip().split(",")
        return Producto(id_producto, nombre, int(cantidad), float(precio))


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo al iniciar el programa."""
        if not os.path.exists(self.archivo):
            print(f"Archivo '{self.archivo}' no encontrado. Se creará uno nuevo.")
            open(self.archivo, "w").close()  # Crear el archivo si no existe
            return

        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    producto = Producto.from_string(linea)
                    self.productos[producto.id_producto] = producto
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print(f"Error: El archivo '{self.archivo}' no existe.")
        except PermissionError:
            print(f"Error: No tienes permisos para leer el archivo '{self.archivo}'.")
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda los productos en el archivo."""
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos.values():
                    file.write(str(producto) + "\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print(f"Error: No tienes permisos para escribir en el archivo '{self.archivo}'.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        """Añade un nuevo producto al inventario."""
        if id_producto in self.productos:
            print(f"Error: El producto con ID '{id_producto}' ya existe.")
            return

        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos[id_producto] = nuevo_producto
        self.guardar_inventario()
        print(f"Producto '{nombre}' añadido exitosamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o el precio de un producto existente."""
        if id_producto not in self.productos:
            print(f"Error: El producto con ID '{id_producto}' no existe.")
            return

        producto = self.productos[id_producto]
        if cantidad is not None:
            producto.cantidad = cantidad
        if precio is not None:
            producto.precio = precio

        self.guardar_inventario()
        print(f"Producto '{producto.nombre}' actualizado exitosamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario."""
        if id_producto not in self.productos:
            print(f"Error: El producto con ID '{id_producto}' no existe.")
            return

        eliminado = self.productos.pop(id_producto)
        self.guardar_inventario()
        print(f"Producto '{eliminado.nombre}' eliminado exitosamente.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
            return

        print("Inventario actual:")
        for producto in self.productos.values():
            print(f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")


# Interfaz de usuario en la consola
def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Mostrar inventario")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inventario.mostrar_inventario()
        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            inventario.agregar_producto(id_producto, nombre, cantidad, precio)
        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje vacío para no cambiar): ")
            precio = input("Ingrese el nuevo precio (deje vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == "4":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()