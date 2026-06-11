
def validar_lista_numeros():
    while True:
        entrada = input("Ingresa números enteros separados por espacios: ")

        try:
            numeros = entrada.split()
            lista_numeros = []

            for numero in numeros:
                lista_numeros.append(int(numero))

            return lista_numeros

        except ValueError:
            print("Error: debes ingresar solo números enteros. Intenta nuevamente.")


def separar_pares_impares(lista):
    pares = []
    impares = []

    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    return pares, impares


numeros = validar_lista_numeros()
pares, impares = separar_pares_impares(numeros)

print("Números pares:", pares)
print("Números impares:", impares)