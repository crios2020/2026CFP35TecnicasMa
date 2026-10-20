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
