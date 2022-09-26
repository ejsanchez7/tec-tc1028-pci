def calcular_ciclo(ropa, lavar, enjuagar, exprimir) :

    tiempo_agua = (ropa * 3)/10
    tiempo = 0

    if (ropa > 0) and (ropa <= 5) :

        if lavar :
            tiempo = tiempo + 15 + tiempo_agua
        if enjuagar :
            tiempo = tiempo + 10 + tiempo_agua
        if exprimir :
            tiempo = tiempo + 5
    
    elif (ropa > 5) and (ropa <= 10) :

        if lavar :
            tiempo = tiempo + 25 + tiempo_agua
        if enjuagar :
            tiempo = tiempo + 15 + tiempo_agua
        if exprimir :
            tiempo = tiempo + 10
    
    else :

        if lavar :
            tiempo = tiempo + 35 + tiempo_agua
        if enjuagar :
            tiempo = tiempo + 20 + tiempo_agua
        if exprimir :
            tiempo = tiempo + 15
    
    return tiempo


# Pedir cantidad de ropa
ropa = float(input("¿Cuánta ropa vas a lavar (kg)?"))

# Evaluar si la cantidad de ropa es válida
if ropa > 0 and ropa <= 15 :
    # Cantidad válida

    # Preguntar las fases que se ejecutarán
    lavar = (input("¿Lavar (s/n)?") == "s")
    enjuagar = (input("enjuagar (s/n)?") == "s")
    exprimir = (input("exprimir (s/n)?") == "s")

    tiempo_ciclo = calcular_ciclo(ropa, lavar, enjuagar, exprimir)

    print(f"El tiempo total del ciclo de lavado es: {tiempo_ciclo}")
    
else :
    print("La cantidad de ropa debe ser menor a 15kg")