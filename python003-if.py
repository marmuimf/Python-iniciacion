#entradas, introducir info en el programa

print("Dime tu nombre")
nombre = input()
#el sistema esta guardando esa informacion en una variable
print("Hola,",nombre)

print("Dime tu edad")
edad = input()
print("Tu nombre es",nombre,",Tu edad es de",edad,"años")

edad = 15
print("---------------")

#estructura de control if
if edad < 30:
    print("Eres una persona joven")#sangria
else:
    print("Ya no eres tan joven como antes")
    print("Esta linea no la va a imprimir")

print("---------------")

#if anidado
edad = 25
if edad < 20:
    if edad < 10:
        print("Eres un niño")
    else:
        print("Eres un adolescente")
else:
    if edad < 30:
        print("Eres un joven")
    else:
        print("definitivamente se te ha acabado lo bueno")
print("---------------")
#forzado de tipo
print("Dime la edad")
edad = int(input()) #convierte en int lo que introduzcamos
print("El doble de tu edad es",(edad*2))
