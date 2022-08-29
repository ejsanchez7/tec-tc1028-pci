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
radio = float(input("Escribe el radio: "))
area = PI * (radio ** 2)
print(f"El área del círculo es {area}")