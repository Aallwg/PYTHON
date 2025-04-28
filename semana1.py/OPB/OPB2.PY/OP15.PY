num1= int(input("INGRESE UN NUMERO"))
num2= int(input("INGRESE UN NUMERO"))

if num1> 10 and num2 > 10:
    print("AMBOS NUMEROS SON MAYORES QUE 1O.")
elif num1 >10  and num2 <= 10:
    print ("SOLO EL PRIMERO NUMERO ES MAYOR QUE 10.")
elif num1 <= 10 and num2 >10:
    print("SOLO EL SEGUNDO NUMERO ES MAYOR QUE 10")
else: 
    print("NINGUNO DE LOS DOS ES MAYOR QUE 10.")