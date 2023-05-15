from random import randint as azar

# from random import* #here import all

# import random

continua = "y"

while (continua == "y" or continua == "Y"):
    throwDado = azar(1, 6)  # genereta number random from 1 ,until 6
    print(f"You pulled out, the number:{throwDado} ")
    continua = input("Continuamos(y/n)?")
print("Stop")
