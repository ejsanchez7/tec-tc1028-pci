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

