ingrsos=float(input("ANEXE LOS INGRESOS MENSUALES:"))
deudas= input ("¿Tiene deudas responda con (si o no):").lower

if ingrsos>2500 or (ingrsos > 1500 and deudas == "no"):
    print("Es apto")
else:
    print("NO es apto")