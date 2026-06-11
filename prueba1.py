

while True:
    try:
        cantidad_pilotos=int(input("Ingrese la cantidad de pilotos a registrar"))

        if cantidad_pilotos <= 0:
            print("Numero invalido ingresa un entero postivo para continuar...")
        else:
            break
    except ValueError:
        print("Numero invalido ingresa un entero postivo para continuar...")
contador_comandantes=0
contador_cadetes=0
for i in range(cantidad_pilotos):
    while True:
        nombre_piloto=input(f"Ingrese nombre piloto: {i+1}/{cantidad_pilotos}")
        if len(nombre_piloto) > 6 or " " in nombre_piloto:
            print("Error el nombre no puede tener espacios o tener mas de 6 caracteres de largo")
        else:
            break
    while True:
        try:
            nivel_vuelo=int(input(f"Ingrese nivel de vuelo del piloto {i+1}/{cantidad_pilotos}"))
            if nivel_vuelo <= 0:
                print("error debe ingresar un nivle de vuelo valido")
            else:
                if nivel_vuelo > 40:
                    contador_comandantes+=1
                else:
                    contador_cadetes+=1
                break
        except ValueError:
            print("error debe ingresar un nivle de vuelo valido")

print(f"La flota estelar cuenta con {contador_comandantes} Conandantes galacticos y {contador_cadetes} cadetes estelares preparense")
        