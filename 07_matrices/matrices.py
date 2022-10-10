def imprime_matriz(matrix) :

    for lista in matrix :
        for elemento in lista :
            print(elemento, end = ", ")
        print("")

def promediar_matriz(matrix) :
    suma = 0
    cantidad = 0
    for fila in range(len(matrix)) :
        for columna in range(len(matrix[fila])) :
            suma += matrix[fila][columna]
            cantidad += 1
    return (suma / cantidad)

def multiplica_columna(matrix, columna, valor) :

    fila = 0

    for lista in matrix :
        col = 0
        for elemento in lista :
            if col == columna :
                matrix[fila][col] = matrix[fila][col] * valor
            col += 1
        fila += 1
    
    return matrix

matrix = [
    [96, 14, 22],
    [42, 26, 13],
    [17, 90, 99]
]

imprime_matriz(matrix)
print(f"El promedio es: {promediar_matriz(matrix)}")
valor = 4
matrix = multiplica_columna(matrix, 1, valor)
imprime_matriz(matrix)