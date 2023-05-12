text = "This is a text for exercise "
# start and end with?
print("La cadena start with :", text.startswith("This"))
print("La cadena end with:", text.lower().endswith("Exercise".lower()))  # la convierto a miniscula

# aling text
# center
print(text.center(80, "*"))  # quiero centrarlo entre 80 caracteres,paso que dicho caracter
print(text.ljust(80, "-"))  # characters at side left
print(text.rjust(50, "/"))  # is the same characters at side right

# long the text
print(len(text))

# delete spaces in white
text = " hola esto es una  cadena con espacios    en   blanco   /52"
print(text.strip())  # only delte spaces al princio

# sustituir caracter
print(text.replace("blanco", "transparante"))  # le digo a quien quiero sustituir y por quien lo quiero sustituir
