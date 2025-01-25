class Archivo:
    def __init__(self, nombre_archivo):
        # Constructor: inicializa el nombre del archivo
        self.nombre_archivo = nombre_archivo
        self.archivo = None
        print(f"Constructor: Se ha creado un objeto para el archivo {self.nombre_archivo}.")

    def abrir(self):
        # Método para abrir el archivo (simulado)
        self.archivo = open(self.nombre_archivo, 'w')
        print(f"Archivo {self.nombre_archivo} abierto para escritura.")

    def escribir(self, texto):
        # Método para escribir en el archivo
        if self.archivo:
            self.archivo.write(texto)
            print(f"Escribiendo en {self.nombre_archivo}: {texto}")
        else:
            print("El archivo no está abierto.")

    def __del__(self):
        # Destructor: cierra el archivo al eliminar el objeto
        if self.archivo:
            self.archivo.close()
            print(f"Destructor: Se ha cerrado el archivo {self.nombre_archivo}.")
        else:
            print("Destructor: El archivo no estaba abierto.")

# Crear y utilizar el objeto
archivo_obj = Archivo("mi_archivo.txt")
archivo_obj.abrir()
archivo_obj.escribir("Este es un ejemplo de uso de constructores y destructores.")
# El objeto será destruido aquí y el destructor se llamará
del archivo_obj
