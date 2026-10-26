# Ejericio 1
#     Dado el vector {10,20,5,15,30,20}
#     1. Informar el vector de la forma:
#     "Índice: X, Valor: Y".
#     2. Totalizar el vector e informar el total.
#     3. Informar el contenido de las posiciones
#     impares (por ejemplo, posiciones 1,3,5, etc.)
#     4. Informar el mayor número.
#     5. Informar cuántas veces aparece el
#     número 20
print("-- Ejercicio 1 --")
vector=[10,20,5,15,30,20]
total=0
max=vector[0]
cont20=0
# 1
for x in range(len(vector)):
    print("Indice: ",x,", Valor: ",vector[x])
    total+=vector[x]
    if vector[x]>max:
        max=vector[x]
    if vector[x]==20:
        cont20+=1
#2
print("Total: ",total)
#3
for x in range(len(vector)):
    if x%2!=0:
        print("Posición Impar, valor: ",vector[x])
#4
print("Valor máximo: ",max)
#5
print("Cantidad de 20: ",cont20)

# Ejercicio 2
#     Considerar el vector de inflación:
#         {0.8, 0.1, 0.3, 0.4, 0.3, 0.6, 0.5, 0.3, 0.7, 0.3, 0.2, 0.9}
#         Cada ítem del vector representa la inflación
#         de un mes, de tal manera que el primer ítem
#         del vector, que es 0.8, representa la inflación
#         de enero y el último ítem del vector, que es 0.9,
#         representa la inflación de diciembre.
    
#         1. Informar la inflación anual.
#         2. Informar la inflación más baja junto con el
#         número de mes. Por ejemplo: Mes 2 = 0.1
#         3. Informar la inflación más alta junto con el
#         número de mes. Por ejemplo: Mes 12 = 0.9
#         4. Informar el promedio de inflación
#         (inflación total / 12).
print("-- Ejercicio 2 --")
inflacion=[0.8, 0.1, 0.3, 0.4, 0.3, 0.6, 0.5, 0.3, 0.7, 0.3, 0.2, 0.9]
inflacionTotal=0
inflacionMin=inflacion[0]
inflacionMinMes=0
inflacionMax=inflacion[0]
inflacionMaxMes=0
for mes in range (len(inflacion)):
    inflacionTotal+=inflacion[mes]
    if inflacion[mes]<inflacionMin:
        inflacionMin=inflacion[mes]
        inflacionMinMes=mes
    if inflacion[mes]>inflacionMax:
        inflacionMax=inflacion[mes]
        inflacionMaxMes=mes
#1
print("Inflación anual: ",inflacionTotal)
#2
print("Inflación más baja: ",inflacionMin," mes: ",inflacionMinMes)
#3
print("Inflación más alta: ",inflacionMax," mes: ",inflacionMaxMes)
#4
print("Inflación promedio: ",(inflacionTotal/12))
