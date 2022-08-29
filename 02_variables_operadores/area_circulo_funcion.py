"""
Algoritmo para calcular el área de un círculo

Estado inicial

radio = input
PI = 3.1416
area = 0

1.- Pedir radio
2.- area = PI * radio * radio
3.- Mostrar area

"""

PI = 3.1416

# Definición de la función
def area_circulo(radio) :
    area = PI * (radio ** 2)
    return area

#volumen de un cilindro
def volumen_cilindro(radio, altura) :
    volumen = area_circulo(radio) * altura
    return volumen


# Ejecución de la función
radio_input = float(input("Escribe el radio del círculo: "))
area_final = area_circulo(radio_input)
print(f"El área del círculo es {area_final}")

radio_input = float(input("Escribe el radio de la base: "))
altura_input = float(input("Escribe la altura: "))
volumen_final = volumen_cilindro(radio_input, altura_input)
print(f"El volumen del cilindro es {volumen_final}")
    

#volumen_cilindro()