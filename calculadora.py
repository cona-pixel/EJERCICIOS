def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a, b):
    if b ==0:
     return a / b 

while True:
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = input("Elige una opción: ")  

    if opcion not in ["1", "2", "3", "4"]:
        print("Opción no válida, intenta de nuevo")
        continue
    
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    if opcion=="1":
            resultado=sumar(num1,num2)
            print("Resultado:", resultado)
    elif opcion == "2":
        resultado=restar(num1, num2)
        print("Resultado:", resultado)
    elif opcion == "3":
        resultado=multiplicar(num1, num2)
        print("Resultado:", resultado)
    elif opcion == "4":
        resultado=dividir(num1, num2)
        print("Resultado:", resultado)
    else:
        print("Opción no válida")
    if opcion == "5":
            print("Chao calculadora 👋")
    break

  







