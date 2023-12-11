#Conexion a una base de datos

##Importo modulos de SQlite Para poder trabajar con bases de datos
import sqlite3 as lite #as alias, lite es el alias
import sys #comandos para leer y escribir archivos del disco duro

##Me conecto a una base de datos llamada agenda
#si el archivo no existe, lo crea
conexion = lite.connect("agenda.sqlite")
##Establezco un cursor para saber en que punto de la base de datos voy a trabajar
cursor = conexion.cursor()
##Le pido algo a la base de datos en lenguaje SQL
cursor.execute("SELECT SQLITE_VERSION()")
##Datos contiene lo que me devuelve la base de datos
datos = cursor.fetchone() #fetchone solo el primer registro
print("La versión de SQLite es:",datos)
