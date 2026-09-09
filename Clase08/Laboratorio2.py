#Ejercicio 1
#Dado el siguiente código:
nro1 = 100
nro2 = 500
nro3 = 250
#Informar cuál de los tres números es mayor.
#No hay números iguales
print ("Ejercicio 1")
#Informar cuál de los tres números es mayor.
#No hay números iguales
# if nro1 > nro2 and nro1 > nro3:
#     print ("El numero más grande es el primero:", nro1)
# if nro2 > nro1 and nro2 > nro3:
#     print ("El numero más grande es el segundo:", nro2)
# if nro3 > nro2 and nro3 > nro1:
#     print ("El numero más grande es el tercero:", nro3)
    
if nro1>nro2:
    if nro1>nro3:
        print ("El numero más grande es el primero:", nro1)
    else:
        print ("El numero más grande es el tercero:", nro3)
else:
    if nro2>nro3:
        print ("El numero más grande es el segundo:", nro2)
    else:
        print ("El numero más grande es el tercero:", nro3)

   
#Ejercicio 2
#A partir del siguiente código:
a=10
b=-2
c=5
#siempre hay 2 números positivos y 1 negativo.
#Informar la multiplicación de los dos números positivos.
print ("Ejercicio 2")
if a < 0:
    print (f"El - a - es negativo, la multiplicacion entre b ({b}) y c ({c}) es {b*c}")
if b < 0:
    print (f"El - b - es negativo, la multiplicacion entre a ({a}) y c ({c}) es {a*c}")
if c < 0:
    print (f"El - c - es negativo, la multiplicacion entre a ({a}) y b ({b}) es {a*b}")

#Ejercicio 3
#Tomando el siguiente código:
#usuario = "Pepito"
#clave = "1234"
#Informar los siguientes casos:
#1. Si el usuario es ”pepito” y la clave es ”1234” informar “¡Bienvenido pepito!”.
#2. Si el usuario es ”pepito” y la clave no es “1234” informar “Contraseña incorrecta”.
#3. Si el usuario no es “pepito” y la clave es “1234” informar “Usuario incorrecto”.


print ("Ejercicio 3")
#Tomando el siguiente código:
#usuario = "Pepito"
#clave = "1234"
#Informar los siguientes casos:
#1. Si el usuario es ”pepito” y la clave es ”1234” informar “¡Bienvenido pepito!”.
#2. Si el usuario es ”pepito” y la clave no es “1234” informar “Contraseña incorrecta”.
#3. Si el usuario no es “pepito” informar “Usuario incorrecto”.

# usuario=input("Ingrese su nombre de usuario:")
# if usuario == "Pepito":
#     clave=input("Ingrese la contraseña:")
#     if clave == "1234":
#         print("Bienvenido")
#     else:
#         print ("Contraseña erronea")
# else:
#     print("ususario incorrecto")
    
usuario=input("Ingrese su nombre de usuario: ")
clave=input("Ingrese su clave: ")
if usuario=="Pepito" and clave=="1234":
    print("¡Bienvenido Pepito!")
if usuario=="Pepito" and clave!="1234":
    print("Contraseña incorrecta")
if usuario!="Pepito":
    print("Usuario incorrecto")