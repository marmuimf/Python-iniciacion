#separar datos para convertirlo en listas


#leer el archivo
archivo = open("agenda.txt",'r')

linea = archivo.read()
print(linea)


# vamos a usar la coma para "partir" para convertirlo en lista
partido = linea.split(",")
print(partido)
