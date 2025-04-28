nota1=float(input("INGRESE NOTA; "))
nota2=float(input("INGRESE NOTA: "))
nota3=float(input("INGRESE NOTA: "))

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10: 
    promedio= (nota1 + nota2 + nota3) / 3
    print(f"PROMEDIO: {promedio: .2f}")
if promedio >= 6:
    print(f"EL ESTUDIANTE APRUEBA CON:{promedio}: ")
else: 
    print(f"EL ESTUADIANTE REPRUEBA CON: {promedio}: ")