from cmath import isnan
import math

def average() :
    # Pedir datos al usuario hasta que introduzca un valor especial
    number = 0
    count = 0
    sum = 0
    stop = False

    while stop == False :
        number = input("Introduce un número: ")
        
        if number.isnumeric() :
            number = float(number)
            count = count + 1
            sum = sum + number
        else :
            stop = True
    
    return sum/count

print(f"El promedio es: {average()}")