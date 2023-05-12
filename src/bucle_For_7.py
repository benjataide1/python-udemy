# !multiplication table
number = int(input("Enter the number,for multiply: "))

since = 1
until = 11
for count in range(since, until):
    total = number * count
    print(f"{number} * {count}: {total}")

print('----------------------------------')

# !List
nombre = ["benjamin", "jazmin", "fran", "lorezno"]
for i in nombre:
    print(f"Nombre:{i}")

print('----------------------------------')

# !Reverse Table
reverseNumber = int(input("Please Enter the Number,Reverse Table: "))

since = 10
until = 0

for i in range(since, until, -1):
    total = reverseNumber * i
    print(f"{reverseNumber} * {i}: {total}")

print('----------------------------------')

# EXTRA

list_colors = ["blue", "red", "green", "blue marine", "pink"]

for color in list_colors:
    if color == 'gray':
        print("Not found the color")
    elif color == 'blue':
        print("color found")
        break
    else:
        print("error")
        break

print('----------------------------------')

range_lenght = range(1, 101)
print(range_lenght)

for number in range_lenght:
    if (number == 21):
        print("your age")
        break
    elif (number == 25):
        print("found it")
        break
