promedio= float(input("INGRESE SU PROMEDIO: "))
ingresos= float(input("INGRESE SUS INGRESOS: "))
materias= int(input("INGRESE LA CANTIDAD DE MATERIAS APROBADAS:"))

if promedio >= 8 and materias < 3 and ingresos <= ingresos <= 1500:
    print("ERES BENEFICIARIO DE LA BECA")
else:
    print("LO SIENTO, NO APLICAS AL PROYECTO DE BENEFICIENCIA") 