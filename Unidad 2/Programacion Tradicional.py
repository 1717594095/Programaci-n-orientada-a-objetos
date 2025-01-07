# Función para obtener temperaturas diarias
def obtener_temperaturas():
    temperaturas = []
    print("Ingrese las temperaturas de los 7 días de la semana:")
    for i in range(7):
        temp = float(input(f"Día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Programa principal
def main():
    temperaturas = obtener_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal del clima es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
