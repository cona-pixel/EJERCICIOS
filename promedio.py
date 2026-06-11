def validar_notas():
    while True:
        datos=input("Ingresa las notas separadas por espacios: ")
        try:
            notas = []
            for notas in datos.split():
                notas.append(float(notas))
            return notas
        except ValueError:
            print("Error: debes ingresar solo numeros. Usa punto para decimales, ejemplo: 4.")

def separar_notas(lista):
    aprobadas =[]
    reprobadas =[]

    for nota in lista:
        if nota >= 4.0:
            aprobadas.append(nota)
        else:
            reprobadas.append(nota)
    return aprobadas, reprobadas

def calcular_promedio(lista):
    suma =0
    for nota in lista:
        suma = suma + nota
    promedio = suma / len(lista)
    return promedio

notas = validar_notas()

aprobadas, reprobadas = separar_notas(notas)

promedio = calcular_promedio(notas)

print("Notas aprobadas: ", aprobadas)
print("Notas reprobadas: ", reprobadas)
print("Promedio general: ", promedio)

