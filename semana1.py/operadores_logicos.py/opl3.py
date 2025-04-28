edad= int(input("Ingrese edad: "))
País= input("Ingrese su país de recidencia: ")
documento=(input("Ingrese documento de identidad: "))

try:
   documento= int(documento)
except ValueError:
   documento = 0

if 18 <= edad <= 30 and País.strip().lower() != "antartida" and documento != 0:
   print("CUMPLES LOS REQUISITOS PARA PARTICIPAR EN EL CONCURSO")
else: 
  print("NO CUMPLES CON LOS REQUISITOS")


