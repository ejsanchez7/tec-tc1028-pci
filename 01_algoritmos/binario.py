"""
Este algoritmo se basa en las propiedades de los sistemas numéricos.
En todo sistema numérico cada "dígito" representa, de derecha a 
izquierda, una potencia de la base del sistema partiendo desde 0.
El sistema decimal es de base 10 por lo que el dígito de las 
unidades representa al resultado de multiplicarlo por 10^0 (1), el de
las decenas por 10^1 (10), el de las centenas por 10^2 (100) y así
sucesivamente.

Ejemplo:

El número 1987 es igual a la siguiente suma:

7 * 10⁰ = 7
8 * 10¹ = 80
9 * 10² = 900
1 * 10³ = 1000

7 + 80 + 900 + 1000 = 1987

Lo mismo sucede con los números binarios, los dígitos del sistema
binario son 0 y 1 e igual que en el decimal, sus valores se multiplican
por la potencia correspondiente a su posición

Ejemplo

123 es en binario 1111011 lo que correspondería a la siguiente suma:

1 * 2⁰ = 1
1 * 2¹ = 2
0 * 2² = 0
1 * 2³ = 8
1 * 2⁴ = 16
1 * 2⁵ = 32
1 * 2⁶ = 64

1 + 2 + 0 + 8 + 16 + 32 + 64 = 123

De manera inversa, para convertir un número decimal a binario, lo que 
se debe hacer es dividir repetidamente el número a convertir entre 2
almacenando el residuo (el cual solo podrá ser 0 o 1), cada dígito 
generado por el módulo será un dígito binario a la izquierda del 
anterior

Ejemplo

para transformar 123 en su respectivo binario 1111011 las operaciones
serían las siguientes:

123/2 = 61  residuo = 1
61/2 = 30   residuo = 1
30/2 = 15   residuo = 0
15/2 = 7    residuo = 1
7/2 = 3     residuo = 1
3/2 = 1     residuo = 1
1/2 = 0     residuo = 1

Resultado: 1111011

Por lo tanto, un posible algoritmo para transformar un número decimal
a binario sería el siguiente:

Estado inicial:

decNum = proporcionado por el usuario
binNum = ""

1.- WHILE decNum > 0
    1.1.- remainder = decNum mod 2
    1.2.- PREPEND remainder ON binNum
    1.3.- decNum = decNum/2
2.- PRINT binNum

"""
def dec2bin(decNum) :

    # El estado inicial es una cadena donde se almacenará el binario
    # es cadena dado que no es un número del sistema decimal
    binNum = ""

    # se repite hasta que la división entera del número sea 0
    while decNum > 0 :
        # Obtener el dígito binario con la operación módulo (residuo)
        remainder = decNum % 2
        # Concatenar el dígito obtenido a la izquierda del valor 
        # almacenado en binNum
        binNum = f"{remainder}{binNum}"
        # Recalcular decNum como el resultado de la división entera
        # entre 2
        decNum = decNum // 2

    # Mostrar el valor final
    print(f"El número binario es: {binNum}")


"""
================
    PRUEBAS
================
"""

dec2bin(123) # 1111011
dec2bin(17) # 10001
dec2bin(9) # 1001
