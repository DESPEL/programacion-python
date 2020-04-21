

def float_input(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Ingrese un número válido")


# uso
valor = float_input("Ingrese un número")


x1 = float_input("ingrese x1")
x2 = float_input("ingrese x2")
producto = x2 - x1
while round(producto, 5) == 0:
    print("no sea malo, ingrese bien los números")
    x1 = float_input("ingrese x1")
    x2 = float_input("ingrese x2")
    producto = x2 - x1
