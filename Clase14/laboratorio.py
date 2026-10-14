# Laboratorio While
# Ejercicio 1
# Imprimir los números del 1 al 10 uno abajo del otro.
print("-- Ejercicio 1 --")
a = 1
while a <= 10:
    print(a)
    a += 1

# Ejercicio 2
# Imprimir los números del 1 al 10 salteando de a 2 uno abajo del otro.
print("-- Ejercicio 2 --")
a = 1
while a <= 10:
    print(a)
    a += 2

# Ejercicio 3
# Imprimir los números del 10 al 1 uno abajo del otro.
print("-- Ejercicio 3 --")
a = 10
while a >= 1:
    print(a)
    a -= 1

# Ejercicio 4
# Imprimir los números del 1 al 10 sin imprimir números 2,5 y 9 uno abajo del otro
# Requisito: se necesita tener conocimiento del operador AND (&&) y del operador NOT (!=).
print("-- Ejercicio 4 --")
a = 1
# while a<=10:
#     if a!=2 and a!=5 and a!=9:
#         print(a)
#     a+=1

a = 0
while a < 10:
    a += 1
    if a == 2 or a == 5 or a == 9:
        continue
    print(a)


# Ejercicio 5
# Imprimir los números del 1 al 30 sin imprimir números entre el 10 y el 20 uno abajo del otro
# Requisito: se necesita tener conocimientos del operador OR (||).
print("-- Ejercicio 5 --")
a = 1
while a <= 30:
    if a <= 10 or a >= 20:
        print(a)
    a += 1

# Ejercicio 6
# Imprimir la suma de los números del 1 al 10.
# print(1+2+3+4+5+6+7+8+9+10)
print("-- Ejercicio 6 --")
a = 1
suma = 0  # sumador o acumulador
while a <= 10:
    suma += a  # suma=suma+a
    a += 1
print("Suma Total: ", suma)

print(15 % 2)  # 1
print(14 % 2)  # 0
print(-14 % 2)  # 0
print(-15 % 2)  # 1

# Ejercicio 7
# Imprimir la suma de los números pares del 1 al 25
# Requisito: se necesita tener conocimientos del operador RESTO (%).
print("-- Ejercicio 7 --")
a = 1
suma = 0
while a <= 25:
    if a % 2 == 0:
        suma += a
    a += 1
print("Total: ", suma)

# Ejercicio 8
# Imprimir la multiplicación de los números impares que se encuentran
# entre -10 y 10.
print("-- Ejercicio 8 --")
a = -10
multi = 1
while a <= 10:
    if a % 2 != 0:
        multi *= a
    a += 1
print("Total: ", multi)

# Ejercicio 9
# Una persona desea invertir $1000 en un banco, el
# cual le otorga un 2% de interés mensual ¿Cuál
# será la cantidad de dinero que esta persona
# tendrá al cabo de un año?
# En el primer mes tendrá acumulado 1000 $ más
# 20 $ de interés ( 2% de 1000 ). En el segundo
# mes se le sumará un 2% a la base de 1020 $ del
# mes anterior y así sucesivamente.
print("-- Ejercicio 9 --")
mes = 1
inversion = 1000
while mes <= 12:
    inversion *= 1.02
    mes += 1
print(f"Al cabo de un año la inversion final sera {inversion:.2f}$")
