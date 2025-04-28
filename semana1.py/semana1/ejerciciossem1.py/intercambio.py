numero=int(input("INGRESE UN NUMERO ENTERO DE TRES DIGITOS:"))
Digito1= numero %10
DIgito2= (numero // 10)% 10
Digito3= numero // 100
numero_invertido= Digito1 * 100 + DIgito2 * 10 + Digito3
print("El numero invertido es:", numero_invertido)