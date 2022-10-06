def calcular_promedio(calificaciones) :

    suma = 0

    for cal in calificaciones :

        suma += cal

    return (suma / len(calificaciones))

def calcular_promedio_grupal(alumnos) :

    suma = 0

    for matricula in alumnos :

        calificaciones = alumnos[matricula]["calificaciones"]
        promedio_alumno = calcular_promedio(calificaciones)
        suma += promedio_alumno
    
    return suma / len(alumnos)

def agregar_alumno(matricula, nombre, calificaciones, alumnos) :

    if matricula in alumnos :
        print("El alumno ya existe")
    else :
        alumnos[matricula] = {
            "nombre": nombre,
            "calificaciones": calificaciones
        }

    return alumnos

def imprimir_alumnos(alumnos) :

    for matricula in alumnos :

        calificaciones = alumnos[matricula]["calificaciones"]
        promedio_alumno = calcular_promedio(calificaciones)
        
        print(f"Matrícula: {matricula}")
        print(f"Nombre: {alumnos[matricula]['nombre']}")
        print(f"Calificaciones: {alumnos[matricula]['calificaciones']}")
        print(f"Promedio: {promedio_alumno}")
        print("******************************")

alumnos = {
    "A00888867": {
        "nombre": "Erik",
        "calificaciones": [70, 50, 100, 85]
    },
    "A01710711": {
        "nombre": "Emiliano",
        "calificaciones": [80, 85, 90, 100]
    }
}

"""
matricula = input("Escribe la matrícula del alumno: ")
alumno = alumnos[matricula]
calificaciones = alumno["calificaciones"] # alumnos[matricula]["calificaciones"]
print(calcular_promedio(calificaciones))
"""

# print(calcular_promedio_grupal(alumnos))

imprimir_alumnos(alumnos)
alumnos = agregar_alumno("A01709885", "Paul", [60, 40, 80, 30], alumnos)
imprimir_alumnos(alumnos)



