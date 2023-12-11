
#escribir algo en un archivo

archivo = open("miarchivo.txt",'a') #añadir
archivo.write("Este es un texto que estoy escribiendo")
archivo.close()


#leer archivo
archivo = open("miarchivo.txt",'r')

##print(archivo.readline()) #solo lee una linea
##print(archivo.readline())

contador = 0
for i in range(0,10):
    contador += 1
    print(archivo.readline())
    if archivo.readline() == "" and contador > 5: 
        break #para parar la ejecucion de un bucle


##print(archivo.read()) #lee todo el documento
