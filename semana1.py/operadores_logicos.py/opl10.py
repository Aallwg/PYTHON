def verificar_hora(hora):
    if hora < 0 or hora > 23:
        return "LA HORA INGRESADA NO ES VÁLIDA. DEBE SER UN NUMERO ENTRE EL 0 Y EL 23."
    if 8 <= hora <= 18 and hora != 13:
        return "EL HORARIO PERMITIDO PARA CLASES."
    else: 
        return "NO ES EL HORARIO PERMITIDO EN CLASE."
    

try:
    hora= int(input("INGRESE HORA DEL DÍA (NUMERO ENTRE 0 Y 23)"))
    resultado= verificar_hora(hora)
    print(resultado)
except ValueError: 
    print("Por favor, ingresa un numero válido entre 0 y 23")




