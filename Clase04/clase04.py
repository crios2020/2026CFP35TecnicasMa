import math

#Linea de comentarios

"""
    Bloque 
    de 
    Comentarios
"""

# Lenguaje: Python          (Descargamos el interprete Python "python.org")

# IDE (Integrated Development Enviroment) (Entorno de Desarrollo Integrado)
# IDE: VsCode
# Extensión: Python Extension Pack, Don Jayamanne

print("Hola Mundo!") #Imprime en consola
print("Hoy es lunes!")
print("Centro de Formación Profesional Nro 35")
print("Curso: Técnicas de programación")

# Variables
# Almacenan datos en memoria RAM

#   Memoria RAM:        Volatil         Costosa(Cara)       Veloz       
#   Disco Duro HD:      Persistente     Ecónomico           Lento

#   Lenguajes de Tipados Fuerte: JAVA, C, C++, C#, Kotlin, Visual Basic
#   Lenguajes de Tipados Debil:  Python, PHP, JavaScript

# Declaración y asignación de variable
#print(a)           # Error no esta declarada la variable
a=2                 # asignamos un valor entero
print(a)
print("Variable a =",a)             #2
print(f"Variable a = {a}")          #Forma Optimizada

# Azúcar sintáctico (syntactic sugar) - dos códigos distintos que hace lo mismo
a=a+1           #Reasignación de valor
print("Variable a =",a)             #3

# los comentarios TODO: significan tarea pendiente
# Extensión Todo Tree Gruntfuggly Muestra la lista de tareas pendientes del proyecto
# Mutación de variable

# Variable String (cadena de texto)
a="Miércoles"
print("Variable a =",a)  
#a=a+1  #Error: no puedo operar matemáticamente un texto
print("Variable a =",a)  

p="perro"
l="ladra"
#frase=p+l
print(p+l)                      #perroladra
print(p+" "+l)                  #perro ladra
print(p+" que "+l)              #perro que ladra


# Otros tipos de datos

#Tipo de datos boolean
x=True                  #1
print(x)
x=False                 #0
print(x)

#Tipo de datos de Punto Flotantes, o decimales
n=10
print(n/3) 

#   EEUU:               1,000,000.50
#   Argentina:          1.000.000,50
n=3.65
print(n)

#por que se dice punto flotante
print(1/3)
print(10/3)
print(100/3)
print(1000/3)
print(10000/3)

pi = 3.14159265
pi = math.pi

print(pi)
print(f"{pi:.2f}")

#Identificadores de variables (Nombres de variables permitidos)
a=2
numero=2
numero1=2
n1umero=2
#1numero=2       #error
#PI=3.14             #no da error de sintaxis, vamos a usar las mayusculas para constantes
#numero#=1      #error

numero_1=2      #permitido

#indicadores de varias palabras
temperaturaMaxima=30                #camel case - Letra Camello
temperatura_maxima=30

#Constantes una variable que no debe modificarse
PI=3.14

# TODO:  = operador de asignación
nro1=5
nro2=7

nro1=nro2
# <===

print(nro1)         #7
print(nro2)         #7

#ingreso de valores por consola
#print("ingrese su nombre: ")
nombre=input("ingrese su nombre: ")
print("hola "+nombre)

#Desafio
# El programa debe ingresar por consola (teclado), el valor de 
# la base y el valor de la altura de un rectangulo.
# El programa debe calcular e imprimir la superficie y el perimetro del rectangulo.
