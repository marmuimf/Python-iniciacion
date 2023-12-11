##Programa agenda con persistencia de datos

agenda = [["nombre","telefono","email"]]


def miAgenda():
    print("Introduce el nuevo nombre en la agenda")
    nombre = input()
    print("Introduce el numero de telefono")
    telefono = input()
    print("Introduce el correo")
    correo = input()
    # antes de hacer nada mas, lo metemos en la lista, y sacamos la lista
    agenda.append([nombre,telefono,correo])
    print(agenda)
    # Guardo en archivo
    archivo = open("agenda.txt",'a')
    pepino = nombre+","+telefono+","+correo+"\n"
    archivo.write(str(pepino))
    archivo.close()
    # ejecucion recursiva
    miAgenda()

miAgenda()
