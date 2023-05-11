# functions
def isPar(number):
    if (number % 2 == 0):
        # print("the number is Par")
        return True
    else:
        # print("the number is Impar")
        return False


number = int(input("enter the numer to know if is Par or Impar: "))
total = isPar(number)

if total:
    print(total)
else:
    print(total)


# isPar(45)
# isPar(943)


# SUMA
def suma(a, b):
    result = a + b
    return result


num = int(input("Please Enter the Number to add: "))
num2 = int(input("Enter the Second Number to add: "))

result = suma(num, num2)
print(f"total:{result}")
#print("total:"+str(result))