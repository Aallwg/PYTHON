def confirmar_contraseña (contraseña):
    if len(contraseña) >= 8 and "123" not in contraseña:
        return True
    else: False

while True:

    contraseña= input("CREA UNA CONTRASEÑA:")
    if confirmar_contraseña(contraseña):
       print("La contraseña es segura")
       break
    else: 
        print("La contraseña NO es segura")