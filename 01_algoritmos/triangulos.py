"""
Para saber si las 3 medidas corresponden a un triángulo
Un lado de un triángulo es menor que la suma de los otros dos y mayor que su diferencia
1.- READ a
2.- READ b
3.- READ c
4.- suma = b + c
5.- resta = b - c
6.- IF suma > a AND resta < a THEN
    6.1- PRINT "Es un triángulo"
7.- ELSE
    7.1.- PRINT "No es un triángulo"
"""
def readData() :
    a = input("Escribe el lado A: ")
    b = input("Escribe el lado B: ")
    c = input("Escribe el lado C: ")

    return [int(a),int(b),int(c)]

def isTriangle(a,b,c) :
    sum = b + c
    diff = abs(b - c) # valor absoluto

    if sum > a and diff < a :
        print("Es un triángulo")
    else :
        print("No es un triángulo")

"""
Para comprobar si es equilátero (asumiendo que se proporciona un triángulo válido)
los 3 lados deben ser iguales

1.- READ a
2.- READ b
3.- READ c
5.- IF a = b AND b = c THEN
    5.1- PRINT "Es equilatero"
6.- ELSE
    6.1.- PRINT "No es equilátero" 
"""
def isEquilateral(a,b,c) :

    if (a == b) and (b == c) :
        print("Es equilátero")
    else :
        print("No es equilátero")

"""
Para comprobar si es isóceles (asumiendo que se proporciona un triángulo válido)
los 2 lados iguales y uno diferente

1.- READ a
2.- READ b
3.- READ c
5.- IF (a = b AND b != c) OR (a = c AND c != b) OR (b = c AND c != a)
    5.1- PRINT "Es isóceles"
6.- ELSE
    6.1.- PRINT "No es isóceles" 
"""
def isIsosceles(a,b,c) :

    if (a == b and b != c) or (a == c and c != b) or (b == c and c != a) :
        print("Es isóceles")
    else :
        print("No es isóceles")

"""
Para comprobar si es escaleno (asumiendo que se proporciona un triángulo válido)
3 lados diferentes

1.- READ a
2.- READ b
3.- READ c
5.- IF a != b AND b != c AND a != c
    5.1- PRINT "Es escaleno"
6.- ELSE
    6.1.- PRINT "No es escaleno" 
"""
def isScalene(a,b,c) :

    if a != b and b != c and a != c :
        print("Es escaleno")
    else :
        print("No es escaleno")

"""
================
    PRUEBAS
================
"""

# isTriangle(10,20,30) # No es
# isTriangle(20,30,10) # No es
# isTriangle(30,10,25) # Sí es (escaleno)
# isTriangle(3,3,3) # Sí es (equilátero)
# isTriangle(6,5,5) # Sí es (isóceles)

# Equilátero
# isEquilateral(3,3,3) # Sí es
# isEquilateral(30,10,25) # Es escaleno
# isEquilateral(6,5,5) # Es isóceles

# Isóceles
# isIsosceles(3,3,3) # Es equilátero
# isIsosceles(30,10,25) # Es escaleno
# isIsosceles(6,5,5) # Sí es

# escaleno
# isScalene(3,3,3) # Es equilátero
# isScalene(30,10,25) # Sí es
# isScalene(6,5,5) # es isóceles

