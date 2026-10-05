# Ejercicio 1
# Imprimir los números del 1 al 10 uno abajo del otro.
print("-- Ejercicio 1 --")
for a in range(1, 11):
    print(a)

# Ejercicio 2
# Imprimir los números del 1 al 10 salteando de a dos uno abajo del otro.
print("-- Ejercicio 2 --")
for a in range(1, 11, 2):
    print(a)
# Ejercicio 3
# Imprimir los números del 10 al 1 uno abajo del otro.
print("-- Ejercicio 3 --")
for a in range(10, 0, -1):
    print(a)

# Ejercicio 4
# Imprimir la suma de los números impares del 1 al 10.
print("-- Ejercicio 4 --")
suma = 0
for a in range(1, 11):
    if a % 2 != 0:
        suma += a
print("Total: ", suma)

# Ejercicio 5
# Mostrar la suma de
# la multiplicación de los números del 1 al 5
# con
# la suma de los números del 1 al 5.
print("-- Ejercicio 5 --")
multi = 1
suma = 0
for a in range(1, 6):
    multi *= a
    suma += a
print("Resultado final: ", (multi + suma))


# Ejercicio 6
# Imprimir la siguiente figura utilizando la estructura for:
# @
# @
# @
# @
# @
print("-- Ejercicio 6 --")
for a in range (1, 6):
    print ("@")

# bonus
# Imprimir la siguiente figura utilizando la estructura for:
# @@@@@
print("-- bonus --")
# for a in range (5):
#     print ("@", end="")
# print("")
linea=""
for a in range (5):
    linea+="@"
print(linea)

# Ejercicio 7
# Imprimir la siguiente figura utilizando la estructura for:
# @
# @@
# @
# @@
# @
print("-- Ejercicio 7 --")
for a in range (1, 6):
    if a%2==0:
        print ("@@")
    else: print("@")

# Bonus
# @@@@@
# @@@@@
# @@@@@
# @@@@@
# @@@@@
print("-- bonus --")
# for a in range (1, 6):
#      print ("@@@@@")
for x in range(1, 6):
    linea=""
    for a in range (5):
        linea+="@"
    print(linea)


# Ejercicio 8
# Imprimir la siguiente figura utilizando la estructura for:
# @
# @@
# @@@
# @@@@
# @@@@@
print("-- Ejercicio 8 --")
for x in range(1, 6):
    linea=""
    for a in range (1, x+1):
        linea+="@"
    print(linea)

# Ejercicio 9
# Imprimir la siguiente figura utilizando la estructura for:
# @@@@@
# @@@@
# @@@
# @@
# @
print("-- Ejercicio 9 --")
for x in range(5, 0, -1):
    linea=""
    for a in range (1, x+1):
        linea+="@"
    print(linea)

# Ejercicio 10
# Imprimir la siguiente figura utilizando la estructura for:
# @
# @@
# @@@
# @@@@
# @@@
# @@
# @
print("-- Ejercicio 10 --")
for x in range(1, 5):
    linea=""
    for a in range (1, x+1):
        linea+="@"
    print(linea)
for x in range(3, 0, -1):
    linea=""
    for a in range (1, x+1):
        linea+="@"
    print(linea)

# Ejercicio 11
# Imprimir la siguiente figura utilizando la estructura for:
# @@@@@
# @@@
# @
# @@@
# @@@@@
print("-- Ejercicio 11 --")
for x in range(5, 0, -2):
    linea=""
    for a in range (1, x+1):
        linea+="@"
    print(linea)
for x in range(3, 6, 2):
    linea=""
    for a in range (1, x+1):
        linea+="@"
    print(linea)

# Bonus
# @@@@@@@
# @@@ @@@
# @@   @@
# @     @
# @@   @@
# @@@ @@@
# @@@@@@@

# Bonus 2
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
