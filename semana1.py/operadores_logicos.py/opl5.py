protocolo= input("Ingrese el protocolo que usas (http o https):").lower()
puerto=(input("Ingrse el puerto que usas (80 o 445): "))

if protocolo == "https"and puerto == "445":
    print("La conexión es segura")
else:
    print("la conexión NO es segura")