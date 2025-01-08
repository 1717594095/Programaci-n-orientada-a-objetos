# Herencia

class animal:
    def __init__(self, nombre,peso):
        self.nombre = nombre
        self.peso = peso

    def eat(self):
        self.peso +=1

class dog(animal):
    def __init__(self, nombre,peso,sonido):
        super().__init__(nombre,peso)
        self.sonido = sonido

class cat(animal):
    def __init__(self, nombre,peso,sonido):
        super().__init__(nombre,peso)
        self.sonido = sonido

mi_perro = dog("chimuelo", 5, "Guuuaaa")

print(mi_perro.nombre)
print(mi_perro.peso)
print(mi_perro.sonido)
mi_perro.eat()
print(mi_perro.peso)
