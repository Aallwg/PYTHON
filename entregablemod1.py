def obtener_nombre_producto():
    nombre = input("Ingrese el nombre del producto: ").strip()
    while not nombre:
        print("ES NECESARIO EL NOMBRE DEL PRODUCTO PARA PODER CONTINUAR.")
        nombre = input("Ingrese el nombre del producto: ").strip()
    return nombre


def obtener_precio_unitario():
    while True:
        try:
            precio = float(input("Ingrese el precio unitario del producto: "))
            if precio <= 0:
                print("El precio debe ser un número positivo.")
            else:
                return precio
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")


def obtener_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de productos: "))
            if cantidad <= 0:
                print("La cantidad debe ser un número entero positivo.")
            else:
                return cantidad
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")


def obtener_descuento():
    while True:
        try:
            descuento = float(input("Ingrese el porcentaje de descuento (0-100): "))
            if 0 <= descuento <= 100:
                return descuento
            else:
                print("El descuento debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")


def calcular_total(precio_unitario, cantidad, descuento):
    subtotal = precio_unitario * cantidad
    monto_descuento = subtotal * (descuento / 100)
    total = subtotal - monto_descuento
    return subtotal, monto_descuento, total


def mostrar_resultado(nombre, subtotal, monto_descuento, total):
    print("\nResumen de compra:")
    print(f"Producto: {nombre}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento aplicado: ${monto_descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}")


# Programa principal
def main():
    print("=== Calculadora de compra ===")
    nombre = obtener_nombre_producto()
    precio = obtener_precio_unitario()
    cantidad = obtener_cantidad()
    descuento = obtener_descuento()

    subtotal, monto_descuento, total = calcular_total(precio, cantidad, descuento)
    mostrar_resultado(nombre, subtotal, monto_descuento, total)


if __name__ == "__main__":
    main()

