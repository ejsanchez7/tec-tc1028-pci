# Crear una lista con 15 números iguales
lista = [10] * 15
# lista = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

#print(lista)

lista2 = []

i = 0

while i < 15 :

    if i % 2 == 0 :
        lista2.append(0)
    else :
        lista2.append(1)

    i = i + 1

# Crear una lista con 15 números iguales
lista = [1,2,3,4,5]

print(lista2)
#print(list(lista))

# Establece el valor de la localidad 9 a la suma de la localidad 7 y la 13.
lista2[9] = lista2[7] + lista2[13]

print(lista2)

# Escribe el ciclo para imprimir la lista la a pantalla y que queden 5 valores 
# por línea. usa end = '' para evitar el salto de línea por default
lista = list(range(1, 16)) # [1,2,3,4,5]

contador = 1

for num in lista :
    print(f"{num}, ", end = '')

    if contador % 5 == 0 :
        print("")
    
    contador = contador + 1
