ganador=""
mejor_puntaje=0

while True:

    nombre=input("Nombre: ")
    if nombre.upper()=="FIN":
        break
    dificultad=float(input("Grado de dificultad: "))
    suma=0
    nota=float(input("Juez 1: "))
    mayor=nota
    menor=nota
    suma=suma+nota
    for i in range(2,8):
        nota=float(input(f"Juez {i}: "))
        suma=suma+nota
        if nota >mayor:
            mayor=nota
        if nota<menor:
            menor=nota
    suma_final=suma-mayor-menor
    puntaje_total=suma_final *(3/5)*dificultad
    print("El puntajes total es", puntaje_total)

    if puntaje_total>mejor_puntaje:
        mejor_puntaje=puntaje_total
        ganador=nombre
print("El ganador es:",ganador)
print("Con puntaje:",mejor_puntaje)






