# hotel.py

# Clase que representa una habitación en el hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        """Inicializa los atributos de la habitación"""
        self.numero = numero
        self.tipo = tipo  # Ej: 'individual', 'doble'
        self.precio = precio  # Precio por noche
        self.reservada = False  # Indicador de si la habitación está reservada

    def reservar(self):
        """Reserva la habitación, si no está ya reservada"""
        if not self.reservada:
            self.reservada = True
            print(f"Habitación {self.numero} reservada con éxito.")
        else:
            print(f"Lo siento, la habitación {self.numero} ya está reservada.")

    def cancelar_reserva(self):
        """Cancela la reserva de la habitación"""
        if self.reservada:
            self.reservada = False
            print(f"Reserva de la habitación {self.numero} cancelada.")
        else:
            print(f"La habitación {self.numero} no tiene reserva activa.")

    def __str__(self):
        """Devuelve una representación de la habitación"""
        estado = "reservada" if self.reservada else "disponible"
        return f"Habitación {self.numero} ({self.tipo}) - Precio: ${self.precio} - Estado: {estado}"

# Clase que maneja la reserva de habitaciones
class Hotel:
    def __init__(self, nombre):
        """Inicializa el hotel con un nombre y una lista de habitaciones"""
        self.nombre = nombre
        self.habitaciones = []  # Lista de habitaciones disponibles

    def agregar_habitacion(self, habitacion):
        """Agrega una habitación al hotel"""
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        """Muestra todas las habitaciones disponibles y su estado"""
        for habitacion in self.habitaciones:
            print(habitacion)

    def reservar_habitacion(self, numero_habitacion):
        """Reserva una habitación por número"""
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion:
                habitacion.reservar()
                return
        print(f"Lo siento, no encontramos la habitación {numero_habitacion}.")

# ejemplo del uso

# main.py


def main():
    # Crear una instancia del hotel
    mi_hotel = Hotel("Hotel Paraíso")

    # Crear algunas habitaciones
    habitacion1 = Habitacion(101, "Individual", 50)
    habitacion2 = Habitacion(102, "Doble", 80)
    habitacion3 = Habitacion(103, "Suite", 120)

    # Agregar habitaciones al hotel
    mi_hotel.agregar_habitacion(habitacion1)
    mi_hotel.agregar_habitacion(habitacion2)
    mi_hotel.agregar_habitacion(habitacion3)

    # Mostrar habitaciones disponibles
    print("Habitaciones disponibles:")
    mi_hotel.mostrar_habitaciones()

    # Intentar reservar algunas habitaciones
    print("\nIntentando reservar habitación 101...")
    mi_hotel.reservar_habitacion(101)

    print("\nIntentando reservar habitación 102...")
    mi_hotel.reservar_habitacion(102)

    # Mostrar habitaciones después de realizar reservas
    print("\nEstado de las habitaciones después de las reservas:")
    mi_hotel.mostrar_habitaciones()

    # Intentar cancelar una reserva
    print("\nIntentando cancelar reserva de habitación 101...")
    habitacion1.cancelar_reserva()

    # Mostrar estado final de las habitaciones
    print("\nEstado final de las habitaciones:")
    mi_hotel.mostrar_habitaciones()

if __name__ == "__main__":
    main()
