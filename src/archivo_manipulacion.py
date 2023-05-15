import os  # me permite manipular directorios,etc.

# create folder or directory
os.makedirs("MyCarpeta")

# list of the content
print(os.listdir("./"))

# show the directory actual
print(os.getcwd())
# show tamanio de carpeta or directory
print(os.path.getsize("MyCarpeta"))
# comprobar si es un archivo
print(os.path.isfile("MyCarpeta"))
# comprobar si es un directorio
print(os.path.isdir("MyCarpeta"))

# cambiamos de directorio
os.chdir("Mycarpeta")
print(os.getcwd())
print(os.listdir("./"))
os.chdir("../")
print(os.getcwd())

# renombrar la carpeta
os.rename("MyCarpeta", "MyFolder")

# borrar archivo
os.remove(os.getcwd() + "/archivo.txt")
print(os.listdir("./"))

# borrar carpeta
os.rmdir("MyFolder")
os.chdir("../")
print(os.listdir("./"))
