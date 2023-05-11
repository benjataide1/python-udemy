# generator

def impar():
    for number in range(1, 50, 2):
        yield number  # yield retorna un numero dentro del rango que indicamos


generator = impar()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print("End the next")
for number in impar(): #I cant write - for number in generator():
    print(number)
