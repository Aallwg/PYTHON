edad1= int(input("Ingrese edad del prospecto#1: "))
edad2= int(input("Ingrese edad del prospecto#2:"))
edad3= int(input("Ingrese edad del prospecto#2:"))

if ( edad1 < 18 and edad2 > 60) or (edad2 < 18 and edad1 > 60):
    print("Una de las edades es menor que 18 y la otra es mayor que 60")
else: 
    print("No se cumple la condición")