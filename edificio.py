depto=int(input("Ingrese numero del departamento: "))
piso=depto//100
posicion=depto%100

if depto==807:
    precio=500
elif piso==1:
    precio=100
elif piso==25:
    precio=400
else:
    precio=245
    if posicion==7 or posicion==8:
        precio=precio *1.13
    elif posicion==1 or posicion==2:
        precio=precio*0.83 #100% - 17% = 83% #descuento = precio * 0.17#precio = precio - descuento

    precio=int(precio)

print("El precio del departamento es: ",precio)

