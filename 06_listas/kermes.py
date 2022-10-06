def calcular_boletos(cantidad, denominaciones) :

    boletos = []
    resto = cantidad

    for denominacion in denominaciones :

        cantidad_boletos = resto // denominacion
        resto = resto % denominacion
        boletos.append(cantidad_boletos)

    return boletos

def imprimir_boletos(boletos, denominaciones) :

    for indice in range(len(boletos)) :
        
        if boletos[indice] > 0 :
            print(f"Billetes de {denominaciones[indice]}: {boletos[indice]}")


denominaciones = [100, 50, 20, 10, 5, 1]
boletos = calcular_boletos(187, denominaciones)
imprimir_boletos(boletos, denominaciones)