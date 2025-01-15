# Definición de la clase base (superclase)
class Animal:
    def __init__(self, nombre, especie):
        self.__nombre = nombre  # Atributo privado
        self.__especie = especie  # Atributo privado

    # Método para obtener el nombre
    def obtener_nombre(self):
        return self.__nombre

    # Método para obtener la especie
    def obtener_especie(self):
        return self.__especie

    # Método polimórfico
    def hacer_sonido(self):
        print(f"{self.__nombre} hace un sonido genérico de acuerdo al animal.")

# Definición de la clase derivada (subclase) que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, especie, color):
        super().__init__(nombre, especie)  # Llamada al constructor de la clase base
        self.color = color

    # Sobrescritura del método hacer_sonido (polimorfismo)
    def hacer_sonido(self):
        print(f"{self.obtener_nombre()} hace: ¡Guau Guau Guauuuuu!")

# Clase derivada que también hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, especie, color):
        super().__init__(nombre, especie)  # Llamada al constructor de la clase base
        self.color = color

    # Sobrescritura del método hacer_sonido (polimorfismo)
    def hacer_sonido(self):
        print(f"{self.obtener_nombre()} hace: ¡Miau Miau Miauuuuu!")

# Clase derivada que también hereda de Animal
class Vaca(Animal):
    def __init__(self, nombre, especie, color):
        super().__init__(nombre, especie)  # Llamada al constructor de la clase base
        self.color = color

    # Sobrescritura del método hacer_sonido (polimorfismo)
    def hacer_sonido(self):
        print(f"{self.obtener_nombre()} hace: ¡Muuu Muuu Muuuuuu!")

# Creación de objetos (instanciación)
animal_generico = Animal("Animal Genérico", "Desconocido")
perro = Perro("Mia", "Canino", "Labrador")
gato = Gato("Felix", "Felino", "Negro")
vaca = Gato("Lola", "Vacuno", "Negro")

# Demostración de encapsulación: acceso a atributos privados mediante métodos
print(f"Nombre del perro: {perro.obtener_nombre()}")  # Accediendo al atributo privado a través de un getter
print(f"Nombre del gato: {gato.obtener_nombre()}")  # Accediendo al atributo privado a través de un getter
print(f"Nombre de la vaca: {vaca.obtener_nombre()}")  # Accediendo al atributo privado a través de un getter

# Demostración de encapsulación: acceso a atributos privados mediante métodos
print(f"Especie del perro: {perro.obtener_especie()}") # Accediendo al atributo privado a través de un getter
print(f"Especie del gato: {gato.obtener_especie()}")  # Accediendo al atributo privado a través de un getter
print(f"Especie de la vaca: {vaca.obtener_especie()}")  # Accediendo al atributo privado a través de un getter



# Demostración de polimorfismo: mismo método, pero comportamiento diferente según la clase
animal_generico.hacer_sonido()  # Método genérico
perro.hacer_sonido()  # Método sobrescrito en la clase Perro
gato.hacer_sonido()  # Método sobrescrito en la clase Gato
vaca.hacer_sonido()  # Método sobrescrito en la clase Vaca