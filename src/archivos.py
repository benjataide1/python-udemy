# guardar datos en archivo
# abrir arhivo

escritura = open("archivo.txt", "w")  # "w"(escribir)si el archivo no esta creado,se crea
escritura.write(
    "Esto se escribe en el archivo \ny esto en la linea siguiente \n\t\ty esto en otra linea tabulado")  # escribomos dentro de ese archivo
escritura.close()  # cerramos ese archivo

# *puedo poner el nombre que quiera a la variable
# Siempre cerra el archivo

# Lectura de Una Linea
lectura = open("archivo.txt", "r")  # "r"(read)
leelinea = lectura.readline()
print("Leyendo una linea: \n" + leelinea)
lectura.close()

#Lecuta de todo el txt
lectura = open("archivo.txt","r")
leetodo = lectura.read()
print(type(leetodo))
print("leeo todo: \n"+leetodo)
lectura.close()
