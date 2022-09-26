"""
Escribe una función que reciba una lista de números y devuelva el 
promedio de los elementos en la lista
"""
def promedio(numeros) :

    sum = 0

    for num in numeros :
        sum = sum + num
    
    prom = sum / len(numeros)

    return prom

nums = []

cant_nums = int(input("Introduce la cantidad de números: "))
contador = 0

while contador < cant_nums :
    x = float(input("Escribe un número: "))
    nums.append(x)
    contador = contador + 1

print(f"El promedio es: {promedio(nums)}")