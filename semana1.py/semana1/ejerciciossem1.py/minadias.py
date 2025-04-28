minutos_totales= int(int(input("INGRESE LOS MINUTOS:")))
DIAS= minutos_totales//1440
resto_de_minutos= minutos_totales % 1440
HORAS= resto_de_minutos//60
MINUTOS= resto_de_minutos % 60
print(f"{minutos_totales}minutos son{DIAS} días, {HORAS}, horas y {MINUTOS} minutos")