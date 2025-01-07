class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        print("Ingrese las temperaturas de los 7 días de la semana:")
        for i in range(7):
            temp = float(input(f"Día {i + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Programa principal
def main():
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal del clima es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
