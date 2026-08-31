print("-- Clase05 --")

print("Ingrese su nombre: ")
nombre=input()
print("Hola "+nombre)

print("2"+"2")              #22
print(2+2)                  #4

# Ingresar por consola el valor de la base y altura de un rectangulo.
# Calcular e imprimir el perímetro y la superficie de la figura geometrica.
print("-- Restángulo --")
base=float(input("Ingrese el valor de la base del rectángulo (cms): "))
altura=float(input("Ingrese el valor de la altura del rectángulo (cms): "))
superficie=base*altura
perimetro=(base+altura)*2
print("La superficie es: ",superficie)
print("El perímetro es: ",perimetro)

import math
# Ingresar por consola el valor de la base y altura de un triángulo rectángulo.
# Calcular e imprimir el perímetro y la superficie de la figura geometrica.
print("-- Triángulo --")
base=float(input("Ingrese el valor de la base del triángulo rectángulo (cms): "))
altura=float(input("Ingrese el valor de la altura del triángulo rectángulo (cms): "))
superficie=base*altura/2
perimetro=base+altura+math.hypot(base,altura)
print("La superficie es: ",superficie)
print("El perímetro es: ",f"{perimetro:.4f}")

# Ingresar por consola el valor del radio de 1 círculo.
# Calcular e imprimir el perímetro y la superficie de la figura geometrica.
print("-- Círculo --")
radio=float(input("Ingrese el valor del radio del círculo (cms): "))
perimetro=math.pi*radio*2
superficie=math.pi*radio*radio
#superficie=math.pi*math.pow(radio,2)
print("La superficie es: ",f"{superficie:.4f}")
print("El perímetro es: ",f"{perimetro:.4f}")
