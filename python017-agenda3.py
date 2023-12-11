##Programa agenda con split

agenda = [["nombre","telefono","email"]]

#leer estado anterior
archivo = open("agenda.txt",'r')
for i in range(1,10): #10 lineas
    nuevalinea = archivo.readline().split(",") #separar por comas para hacer lista
    agenda.append(nuevalinea)

#imprimimos agenda para ver el estado
print(agenda)

def miAgenda():
    #Menu inicial
    print("Escoge tu opcion")
    print("1.-Introduce nuevo registro")
    print("2.-Listar registros")
    print("3.-Buscar registro")
    opcion = input()

    if opcion == "1":
        print("Introduce el nuevo nombre en la agenda")
        nombre = input()
        print("Introduce el numero de telefono")
        telefono = input()
        print("Introduce el correo")
        correo = input()
        # antes de hacer nada mas, lo metemos en la lista, y sacamos la lista
        agenda.append([nombre,telefono,correo])
        ##    print(agenda)
        # Guardo en archivo
        archivo = open("agenda.txt",'a')
        pepino = nombre+","+telefono+","+correo+"\n"
        archivo.write(str(pepino))
        archivo.close()

    if opcion == "2":
        for i in range(1,len(agenda)): #hasta la longitud del archivo
            print(agenda[i])

    #ejecucion recursiva
    miAgenda()

miAgenda()
