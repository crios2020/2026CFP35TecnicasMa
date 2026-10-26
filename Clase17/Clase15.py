print("-- Clase 15 --")

# Vectores - Arreglos - Arrays
print("-- Arrays --")

numeros=[1,2,3,4,5]
nombres=["Juan","Ana","Pedro","Maria","Carolina"]

print(numeros[2]," ",nombres[2])

#       numeros         nombres         indice
#           1           Juan                0
#           2           Ana                 1
#           3           Pedro               2
#           4           Maria               3
#           5           Carolina            4

print("----------------------------------------------------------------------")
#Recorrido por indices
for a in range(0,5):
    print(numeros[a]," ",nombres[a])

#Función len()
print("Longitud numeros: ",len(numeros))

#Recorrido usando length
for a in range(0,len(numeros)):
    print(numeros[a]," ",nombres[a])

print("----------------------------------------------------------------------")
#Recorrido inverso
for a in range(len(numeros)-1,-1,-1):
        print(numeros[a]," ",nombres[a])

print("----------------------------------------------------------------------")
#Recorrido usando while

a=0
while a<len(numeros):
     print(numeros[a]," ",nombres[a])
     a=a+1        

print("----------------------------------------------------------------------")
numeros=[23,26,29,39,38,10,46,65,10,8,72,10,17,45,10,35]

# Recorrido de vector numeros
linea=""
for a in range (0,len(numeros)):
     #print(numeros[a])
     linea+=str(numeros[a])+", "
print(linea)

# Totalizar el vector, promediar el vector
suma=0
for a in range (0,len(numeros)):
     suma+=numeros[a]
print("Total: ",suma)
print("Promedio: ",(suma/len(numeros)))

# Calcular Valor Máximo y Valor Mínimo
min=numeros[0]
max=numeros[0]
for a in range (0,len(numeros)):
    if numeros[a]<min:
        min=numeros[a]
    if numeros[a]>max:
        max=numeros[a]
print("Valor mínimo: ",min)
print("Valor máximo: ",max)

#Contar cantidad de números pares e impares, contar cantidad de veces que se repite el nro 10
pares = 0
impares = 0
contar10 = 0

for a in range(0, len(numeros)):
    if numeros[a] % 2 == 0:
        pares += 1
    else:
        impares += 1
        
    if numeros[a] == 10:
        contar10 += 1

print("Cantidad de pares: ", pares)
print("Cantidad de impares: ", impares)
print("Cantidad de veces que aparece el 10: ", contar10)