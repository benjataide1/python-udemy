# table for multiply
number = int(input("Enter the number to multiply: "))

count = 1
#
while (count <= 10):
    if (count == 10):
        break
    total = number * count  # print(number * count)
    print(f"{number} * {count}:{total}")
    count += 1  # increment the count

#reverse Table
reverseNumber = int(input("Please Enter the Number,Reverse Table: "))

count2 = 10

while (0 <= count2):
    total = reverseNumber * count2
    print(f"{reverseNumber} * {count2}: {total}")
    count2 -= 1
