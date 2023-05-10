number1 = int(input("Enter the first Number:"))
number2 = int(input("Enter the second Number:"))

if (number1 > number2):
    pass  #
    print("The Number 1 is mayor")
elif (number1 == number2):
    print("The number1 is equals number2 ")
else:
    pass
    print("The Second Number 2 is mayor")

age = int(input("Tell me you age and I tell you the tarrif: "))
if age < 5:
    price = 0
elif age < 15:
    price = 5
elif age < 65:
    price = 20
else:
    price = 15
print("you tarrif is: " + str(price))
