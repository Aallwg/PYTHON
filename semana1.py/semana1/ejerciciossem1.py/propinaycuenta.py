def calcular_valor_cuenta (valor):
    porcentaje_10= valor * 0.10
    porcentaje_15= valor * 0.15
    porcentaje_20= valor * 0.20
    return porcentaje_10, porcentaje_15, porcentaje_20
valor_usurio= float(input("INGRESA EL VALOR: "))

P10, P15, P20= calcular_valor_cuenta(valor_usurio)

print(f"10% de {valor_usurio} es {P10}")
print(f"15% de {valor_usurio} es {P15}")
print(f"20% de {valor_usurio} es {P20}")


