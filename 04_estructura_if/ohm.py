def valida(num) :
    return ((num > 1) and (num <= 4))

def calcular_corriente(resistencia, voltaje) :
    """
    if resistencia > 0 :
        return voltaje/resistencia
    return -1
    """
    corriente = -1

    if resistencia > 0 :
        corriente = voltaje / resistencia
    
    return corriente

def calcular_voltaje(corriente, resistencia) :
    return (corriente * resistencia)

def calcular_resistencia(corriente, voltaje) :
    if corriente > 0 :
        return (voltaje / corriente)
    return -1

opcion = int(input("Introduce la opción: "))
resultado = -1

if valida(opcion) != True :
    print("Opción no válida")
elif opcion == 2 :
    resistencia = float(input("Escribe la resistencia: "))
    voltaje = float(input("Escribe el voltaje: "))
    resultado = calcular_corriente(resistencia, voltaje)
elif opcion == 3 :
    resistencia = float(input("Escribe la resistencia: "))
    corriente = float(input("Escribe la corriente: "))
    resultado = calcular_voltaje(corriente, resistencia)
elif opcion == 4 :
    corriente = float(input("Escribe la corriente: "))
    voltaje = float(input("Escribe el voltaje: "))
    resultado = calcular_resistencia(corriente, voltaje)


print(f"El resultado es: {resultado}")

