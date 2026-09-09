#Estructuras condicionales
print("-- Estructura condicional IF --")
temperatura=10
llueve=False

#Estructura if
if llueve:
    print("Usar Paraguas!!")

if llueve==True:
    #código esta indentado
    print("Esta lloviendo!!")
    print("Usar Paraguas!!")

if temperatura<=15:
    print("Hace Frio!!!")

print("---------------------------------------------------")
if temperatura<=15 and llueve:
    print("- Ideal para hacer tortafritas!!!")
print("-- Fin del programa --")

print("-- Estructura condicional IF ELSE --")
if llueve:
    print("Usar Paraguas!")
else:
    print("No Usar Paraguas!")
print("-----------------------------------")
if llueve:
    print("Esta Lloviendo!")
    print("Usar Paraguas!")
else:
    print("No esta lloviendo!")
    print("No Usar Paraguas!")
    
#Estructura switch
opcion = 1

match opcion:
    case 1:
        print("Elegiste la opción 1")
    case 2:
        print("Elegiste la opción 2")
    case 3:
        print("Elegiste la opción 3")
    case _:
        print("Opción no válida")
    
dia="sábado"
match dia:
    case "lunes":
        print("Comienza la semana")
    case "viernes":
        print("¡Por fin viernes!")
    case "sábado" | "domingo":
        print("Fin de semana")
    case _:
        print("Día normal")
        
#TODO Armar fecha y hora usando if y match
#TODO Armar Estación de año usando if y match
