# Exercise

def menu():
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    print("5.Exit")
    opcion = int(input("?_"))
    return opcion


def solicitarDatos():
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))
    if (num2 == 0):
        print("El numero no puede ser 0\n")
        num2 = int(input("Enter the Second Number: "))
    return num1, num2


def operation(operator, num1, num2):
    if (operator == 1):
        total = num1 + num2
    elif (operator == 2):
        total = num1 - num2
    elif (operator == 3):
        total = num1 * num2
    elif (operator == 4):
        total = num1 / num2
    return total


boleano = True

while (boleano):
    opcion = menu()
    if opcion == 1:
        num1, num2 = solicitarDatos()
        print(f"Suma:{num1} + {num2} = {operation(1, num1, num2)}")
    elif opcion == 2:
        num1, num2 = solicitarDatos()
        print(f"Resta:{num1} - {num2} = {operation(2, num1, num2)}")
    elif opcion == 3:
        num1, num2 = solicitarDatos()
        print(f"Multiplicacion:{num1} * {num2} = {operation(3, num1, num2)}")
    elif opcion == 4:
        num1, num2 = solicitarDatos()
        print(f"Dividir:{num1} / {num2} = {operation(4, num1, num2)}")
    elif opcion == 5:
        boleano = False
    else:
        print("Introduza una opcion valida")
        print("\n")
