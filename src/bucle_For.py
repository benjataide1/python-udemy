# !multiplication table
number = int(input("Enter the number,for multiply: "))

since = 1
until = 11
for count in range(since, until):
    total = number * count
    print(f"{number} * {count}: {total}")

# !List
nombre = ["benjamin", "jazmin", "fran", "lorezno"]
for i in nombre:
    print(f"Nombre:{i}")

# !Reverse Table
reverseNumber = int(input("Please Enter the Number,Reverse Table: "))

since = 10
until = 0

for i in range(since, until, -1):
    total = reverseNumber * i
    print(f"{reverseNumber} * {i}: {total}")
