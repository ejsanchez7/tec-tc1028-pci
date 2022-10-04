def imprimeMenu() :
    print("Selecciona la opción: ")
    print("1.- Crear lista")
    print("2.- Inicializar lista")
    print("3.- Contar impares")
    print("4.- Invertir lista")
    print("5.- Obtener mayor")
    print("6.- Salir")
    opcion = int(input("Opción --> "))
    return opcion

def crea_lista(tam) :

    contador = 0
    lista = []

    while contador < tam :
        num = float(input("Introduce un número: "))
        lista.append(num)
        contador += 1
    
    return lista

def inicializa_lista(lista, valor) :

    tam = len(lista)

    for index in range(tam) :
        lista[index] = valor
    
    return lista

def cuenta_impares(lista) :

    contador = 0

    for elemento in lista :

        if (elemento % 2) != 0 :
            contador += 1

    return contador

def invierte_lista(lista) :

    cont = 0
    inv = len(lista) - 1

    while inv >= cont :
        aux = lista[cont]
        lista[cont] = lista[inv]
        lista[inv] = aux
        cont += 1
        inv -= 1
    
    return lista

def mayor_valor(lista) :

    mayor = lista[0]

    for elemento in lista :
        if elemento > mayor :
            mayor = elemento
    
    return mayor


opcion = imprimeMenu()

while opcion != 6 :

    if opcion == 1 :
        tam = int(input("Introduce el tamaño de la lista: "))
        lista = crea_lista(tam)
        print(f"La lista creada es: {lista}")
    elif opcion == 2 :
        tam = int(input("Introduce el tamaño de la lista: "))
        valor = int(input("Escribe el valor para inicializar: "))
        lista = crea_lista(tam)
        inicializa_lista(lista, valor)
        print(f"La lista creada es: {lista}")
    elif opcion == 3 :
        tam = int(input("Introduce el tamaño de la lista: "))
        lista = crea_lista(tam)
        impares = cuenta_impares(lista)
        print(f"La cantidad de impares {impares}")
    elif opcion == 4 :
        tam = int(input("Introduce el tamaño de la lista: "))
        lista = crea_lista(tam)
        lista_inv = invierte_lista(lista)
        print(f"La lista invertida es {lista_inv}")
        # print(f"La lista invertida es {invierte_lista(crea_lista(tam))}")
    elif opcion == 5 :
        tam = int(input("Introduce el tamaño de la lista: "))
        # lista = crea_lista(tam)
        # mayor = mayor_valor(lista)
        print(f"El mayor es {mayor_valor(crea_lista(tam))}")
        # print(f"La lista invertida es {invierte_lista(crea_lista(tam))}")
    else :
        print("Opción no válida")
    
    opcion = imprimeMenu()
