"""
Este algoritmo se basa en una operación llamada módulo la cual sirve
para obtener el residuo de una división entera (sin decimales), por
ejemplo:

la división entera de 1234/10 sería 123 con un residuo de 4
la división entera de 2020/25 sería 80 con un residuo de 20

El residuo siempre será menor al divisor.

Considerando que la base de nuestro sistema numérico es 10, podemos
obtener el último dígito de cada número obteniendo el módulo de su
división entre 10, por ejemplo:

1234 mod 10 = 4 ya que el residuo de dividir entre 10 sería 4
2020 mod 10 = 0 ya que el residuo de dividir entre 10 sería 0

Es por ello que cuando dividimos entre 10 cualquier cantidad lo que
comúnmente decimos es que recorremos el punto decimal a la izquierda
y cuando multiplicamos por 10 recorremos el decimal a la derecha o
agregamos un 0 y desplazamos el número a la derecha

Basados en lo anterior, podemos invertir un número de la siguiente manera:

Estado inicial:
digito = 0
numero = proporcionado por el usuario
nuevoNumero = 0

1.- WHILE numero > 0
        1.1.- digito = numero mod 10
        1.2.- nuevoNumero = nuevoNumero * 10
        1.3.- nuevoNumero = nuevoNumero + digito
        1.4.- numero = numero/10
2.- PRINT nuevoNumero

Al multiplicar (nuevoNumero * 10) lo que hacemos es desplazar el número a la 
izquierda para poder agregar el nuevo dígito en las unidades

"""

def invertNumber(number) :
    # Estado inicial
    digit = 0
    newNumber = 0

    while number > 0 :
        # Extraer dígito de las unidades con la operación módulo (%)
        digit = number % 10
        # Desplazar los dígitos del nuevo número a la izquierda
        newNumber = newNumber * 10
        # Agregar el nuevo dígito en la posición de las unidades
        newNumber = newNumber + digit
        # Actualizar el numero viejo para quitar el digito extraido
        # El operador // en python devuelve solo la parte entera
        number = number//10
    
    return digit

"""
===============
    PRUEBAS
===============
"""
print(f"El número invertido es: {invertNumber(1234)}")
print(f"El número invertido es: {invertNumber(2)}")
print(f"El número invertido es: {invertNumber(24)}")