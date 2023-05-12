def calcular(num1, num2, operacion="suma"):  # si no le paso la operacion por defecto es suma
    def suma(num1, num2):
        return num1 + num2

    def resta(num1, num2):
        return num1 - num2

    def multi(num1, num2):
        return num1 * num2

    def dividir(num1, num2):
        return num1 / num2

    if (operacion == "suma"):
        print(f"{num1} + {num2} = {suma(num1, num2)}")
    elif operacion == "resta":
        print(f"{num1} - {num2} = {resta(num1, num2)}")
    elif operacion == "multiplicacion":
        print(f"{num1} * {num2} = {multi(num1, num2)}")
    elif operacion == "dividir":
        print(f"{num1} / {num2} = {dividir(num1, num2)}")
    return "Resultado devuelvo"
    # si no pongo el retun me sale return none


print(calcular(41, 31, "resta"))
print(calcular(41, 42))
print(calcular(31, 423, "multiplicacion"))
print(calcular(131, 32, "dividir"))
