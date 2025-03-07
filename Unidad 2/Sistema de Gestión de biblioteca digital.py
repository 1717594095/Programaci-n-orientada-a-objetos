class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor  # Autor como cadena
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = {}  # Diccionario para almacenar usuarios con su ID como clave
        self.historial_prestamos = []  # Historial de préstamos (tupla de usuario y libro)

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.id_usuario] = usuario

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        if isbn not in self.libros:
            print("Libro no disponible.")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]
        usuario.prestar_libro(libro)
        self.historial_prestamos.append((usuario, libro))

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        if isbn not in self.libros:
            print("Libro no disponible.")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]
        usuario.devolver_libro(libro)
        self.historial_prestamos = [h for h in self.historial_prestamos if h != (usuario, libro)]

    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if getattr(libro, criterio).lower() == valor.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return []
        usuario = self.usuarios[id_usuario]
        return usuario.libros_prestados


# Prueba del sistema

# Crear libros
libro1 = Libro("El Quijote", "Miguel de Cervantes", "Ficción", "978-3-16-148410-0")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "978-0-06-088328-7")

# Crear usuarios
usuario1 = Usuario("Juan Pérez", "001")
usuario2 = Usuario("Ana Gómez", "002")

# Crear la biblioteca y registrar usuarios y libros
biblioteca = Biblioteca()
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("001", "978-3-16-148410-0")
biblioteca.prestar_libro("002", "978-0-06-088328-7")

# Listar libros prestados por el usuario1
libros_prestados = biblioteca.listar_libros_prestados("001")
print("Libros prestados a Juan Pérez:")
for libro in libros_prestados:
    print(libro)

# Buscar libros por autor
resultados = biblioteca.buscar_libros("autor", "Gabriel García Márquez")
print("\nResultados de búsqueda por autor (Gabriel García Márquez):")
for libro in resultados:
    print(libro)

# Devolver un libro
biblioteca.devolver_libro("001", "978-3-16-148410-0")

# Listar libros prestados por el usuario1 después de la devolución
libros_prestados = biblioteca.listar_libros_prestados("001")
print("\nLibros prestados a Juan Pérez después de la devolución:")
for libro in libros_prestados:
    print(libro)
