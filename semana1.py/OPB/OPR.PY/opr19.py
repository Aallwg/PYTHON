num1= int(input("Ingrese un número: "))
num2= int(input("Ingrese otro nuúmero: "))

if num2 != 0 and num1 % num2 != 0:
    print(f"El primer número {num1} NO es multiplo del segundo: {num2}.")
else:
    print(f"El primero número {num1} SÍ es multiplo del segundo: {num2}")