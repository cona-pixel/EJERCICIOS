hora=int(input("Ingrese hora: "))
minuto=int(input("Ingrese minuto: "))

tiempo=hora*60+minuto

inicio_servicio=6+60+30
fin_servicio=22*60+30

punta_mañana_inicio=7*60+30
punta_mañana_fin=9*60

punta_tarde_inicio=18*60
punta_tarde_fin=19*60

if tiempo < inicio_servicio or tiempo >fin_servicio:
    print("No hay servicio.")
elif (tiempo>=punta_mañana_fin) or (tiempo>=punta_tarde_inicio and tiempo<=punta_tarde_fin):
    print("Horario punta:")
    if tiempo>=punta_mañana_inicio and tiempo<=punta_tarde_fin:
        inicio_punta=punta_mañana_inicio
    else:
        inicio