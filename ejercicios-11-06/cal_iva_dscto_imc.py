def calcular_iva(precio):
    precio=precio * 0.19
    return precio

def calculo_descuento(precio,descuento):
    total = (precio - (precio * (descuento/100)))
    print("El total a pagar con un descuento del ",descuento,"% es: $",total)

def calculo_imc(peso,estatura):
    imc = (peso/estatura**2)

    if imc <18.5:
        print("Bajo peso")
    else:
        if imc >=18 and imc < 24.9:
            print("Peso adecuado")
        else:
            if imc >=25 and imc <=29.9:
                print("Sobrepeso")
            else:
                if imc >=30 and imc <=34.9:
                    print("Obesidad grado 1")
                else:
                    if imc >=35 and imc <=39.9:
                        print("Obesidad grado 2")
                    else:
                        if imc >40:
                            print("Obesidad grado 3")




op =3

while op !=4:
    print("----MENU---")
    print("*"*10)
    print("1.Calcular IVA")
    print("2.Descuento")
    print("3.Calculo IMC")
    print("4.Salir")

    op=int(input("Ingrese opción: (1-4)"))

    if op ==1:
        precio=int(input("Ingrese el precio del producto: "))
        iva = calcular_iva(precio)
        print("El iva del precio $: ",precio,"es $",iva)

    if op==2:
        precio=int(input("Ingrese el precio del productos:"))
        descuento=int(input("Ingrese el % de descuento (0-100)"))
        calculo_descuento(precio,descuento)
    
    if op ==3:
        peso=float(input("Ingrese el peso kg :"))
        estatura=float(input("Ingrese estatura en metros : "))
        calculo_imc(peso,estatura)
