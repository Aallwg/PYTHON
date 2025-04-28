def  convertir(f):
    c =(f-32) * 5/9
    return c
f= float(input("Ingresa los grados en Fahrenheit: "))
print(f"La conversion a c es: {convertir(f)}")