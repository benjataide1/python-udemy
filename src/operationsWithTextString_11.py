# TEXT for examples
text = "Example: Hi!,I'm lorenzo and I from cordoba"

# Convertir a minisculas
print(text.lower())  # all text in miniscules

# Convertir Mayusculas
print(text.upper())  # all text in capital letter

# Primera letra a mayuscula
print(text.capitalize())  # first letter in capital letter
print(text.title())  #all the first letter in capital letter

#Reverse/capital letter at miniscules and miniscules at capital letter
print(text.swapcase())

#Capital Letter? return bolean
print(text.isupper())

#Miniscules? return bolean
print(text.islower())

#es numerico el texto?
print(text.isnumeric())#si contiene numeros
#es alfanumerica?
print(text.isalnum()) #si tiene caracteres no numericos

cadena = "Hola"

#Es un titulo?
print(cadena.istitle())