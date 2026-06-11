print("Bienvenido al sistema de gestion del gimnacio")
cupos_maximos=75
cupos_disponibles=75
cantidad_reservas = 0
while True:
    while True:
        try:
            print("MENU PRINCIPAL")
            print("1 - Cupos disponibles")
            print("2 - Realizar Reserva")
            print("3 - Cancelar Reserva")
            print("4 - Historial de reservas")
            print("5 - Salir")
            opcion_menu=int(input("Escoga una opcion"))
            if opcion_menu<1 or opcion_menu > 5:
                print("Opcion invalida")
            else:
                break
        except ValueError:
            print("Opcion invalida")
    if opcion_menu==1:
        print(f"Hay  {cupos_disponibles} de {cupos_maximos} cupos disponibles")
    elif opcion_menu==2:
        while True:
            try:
                cupos_reservar = int(input("Ingrese la cantidad de cupos a llenar"))
                if cupos_reservar <= 0 or cupos_reservar > cupos_disponibles:
                    print("La cantida de cupos a reservar no debe ser negativa o superar la cantidad total de cupos disponibles")
                else:
                    cupos_disponibles-=cupos_reservar
                    cantidad_reservas+=cupos_reservar
                    break
            except ValueError:
                print("Error al ingresar valor")
    elif opcion_menu == 3:
        if cupos_disponibles == cupos_maximos:
            print("Actualmente no hay reservas realizadas para cancelar")
        else:
            while True:
                try:
                    cupos_cancelar = int(input("Ingrese la cantidad de cupos a cancelar"))
                    if cupos_cancelar <= 0 or cupos_cancelar > cupos_maximos:
                        print(f"La cantida de cupos a cancelar no debe ser negativa o superar la cantidad maxima de {cupos_maximos} cupos")
                    else:
                        if cupos_cancelar > cupos_disponibles:
                            print("No se pueden cancelar mas cupos de los que hay reservados")
                        else:
                            cupos_disponibles+=cupos_cancelar
                            cantidad_reservas-=cupos_cancelar
                            break
                except ValueError:
                    print("Error al ingresar valor")
    elif opcion_menu==4:
        print(f"La antidad de reservas realizadas han sido: {cantidad_reservas}")
    elif opcion_menu==5:
        print("Gracias por utilizar nuestro software, hasta la proxima")
        break

