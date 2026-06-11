#precios de los rolls
precio_pikachu = 4500
precio_otaku = 5000
precio_pulpo = 5200
precio_anguila = 4800

#contadores
cant_pikachu=0
cant_otaku=0
cant_pulpo=0
cant_anguila=0

subtotal=0
descuento=0
total=0

#Para el menu se necesita un menu con un while 
while True:
    print("---MENU SUSHI---")
    print("1.Pikachu Roll $4500")
    print("2.Otaku Roll $5000")
    print("3.Pulpo Venenoso Roll $5200")
    print("4.Anguila Eléctrica Roll $4800")
    print("5.Salir")

    op= input("Elige una opcion: ")

    if op == 1:
        cant_otaku +=1
        subtotal += precio_pikachu
        print("Pikachu Roll agregado.")

    elif op == "2":
        cant_otaku += 1
        subtotal += precio_otaku
        print("Otaku Roll agregado.")

    elif op == "3":
        cant_pulpo += 1
        subtotal += precio_pulpo
        print("Pulpo Venenoso Roll agregado.")

    elif op == "4":
        cant_anguila += 1
        subtotal += precio_anguila
        print("Anguila Eléctrica Roll agregado.")

    elif op == "5":
        break

    else:
        print("Opción no válida.")

descuento=input("¿Tiene codigo de descuento? S/N: ").upper()

if descuento=="S":
    while True:
        codigo=input("Ingrese codigo de descuento o X para salir ")
        if codigo == "soyotaku":
            descuento=subtotal * 0.10
            print("Codigo valido. Se aplico 10 % de descuento.")
            break
        elif codigo == "x":
            print("No se aplicó descuento.")
            break
        else:
            print("Código no válido.")
             



