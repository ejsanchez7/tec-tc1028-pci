from time import sleep

glucosa = int(input("Introduce la medición de glucosa: "))
tiempo = 0
espera = 5#60 * 15

if glucosa < 70 :
    # Hay hipoglucemia
    while glucosa < 70 :
        diff = 70 - glucosa
        print(f"El paciente está {diff} mg/dl por debajo del nivel normal")
        print("Administrar 10 a 15 gramos de carbohidratos")
        print("Esperar 15 minutos...")
        sleep(espera)
        print("Han pasado 15 minutos")
        tiempo = tiempo + 15
        glucosa = int(input("Introduce la medición de glucosa: "))
    
    print(f"El paciente se estabilizó en {tiempo} minutos")

    if glucosa <= 100 :
        print("Existe riesgo de recaída y se debe consumir alimentos en los próximos 30 minutos")
    else :
        print("El riesgo de recaída es bajo, consumir alimentos en cuanto sea posible")

else :
    print("El paciente se encuentra en un rango normal de glucosa")