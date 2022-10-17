def encontrar_pizza(nombre, menu) :
    
    for datos_pizza in menu :

        if nombre == datos_pizza[0] :
            return datos_pizza

def calcular_pedido(pedido, menu) :

    total = 0

    for pizza in pedido : # ["Vegetariana", "Chica", 2]
        # paso 1: encontrar pizza
        datos_pizza = encontrar_pizza(pizza[0], menu) # ["Hawaiana", 80, 150, 290]
        #paso 2: encontrar precio (de acuerdo al tamaño)
        tamanio = pizza[1]
        precio = 0

        if tamanio == "Chica" :
            precio = datos_pizza[1]
        if tamanio == "Mediana" :
            precio = datos_pizza[2]
        if tamanio == "Grande" :
            precio = datos_pizza[3]

        # paso 3: calcular subtotal de pizza
        total += (precio * pizza[2])

    return total

menu = [
    ["Pepperoni", 70, 130, 250],
    ["Hawaiana", 80, 150, 290],
    ["Mexicana", 85, 160,310],
    ["Vegetariana", 90, 170, 330],
    ["Superultrespecial", 120, 230, 450]
]

#print(encontrar_pizza("Mexicana", menu))
pedido = [
    ["Vegetariana", "Chica", 2],
    ["Pepperoni", "Chica", 3],
    ["Hawaiana", "Grande", 1]
]

print(calcular_pedido(pedido, menu))