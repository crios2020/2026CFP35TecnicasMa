# Logica

log1 = True
log2 = False

nro1 = 5
nro2 = 7

print(log1)
print(log2)
print(nro1)
print(nro2)


#       Tabla de verdad
#
#       X               Y               OR              AND
#       F               F               F               F
#       F               V               V               F
#       V               F               V               F
#       V               V               V               V

#       Operadores lógicos y de comparación

#       Operador                Nombre
#       and                     Y
#       or                      O
#       ==                      comparación
#       !=                      distinto
#       not                     negación
#       < <= >= >               comparadores númericos

print(log1 or log2)  # True
print(log1 and log2)  # False

print(nro1==nro2)       #False
print(nro1+2==nro2)     #True

print(nro1!=nro2)       #True
print(nro1+2!=nro2)     #False

print(nro1>=nro2)       #False
print(nro1+2>=nro2)     #True
print(nro1+2>nro2)      #False

print(nro1<nro2)        #True
print(nro1<=nro2)       #True
print(nro1+2<=nro2)     #True
print(nro1+2<nro2)      #False
print(nro1+2<nro2+(10*2-50/3))      #True
#         7 < 7 + (20 - 17)
#         7 < 7 + 3
#         7 < 10

#Operador de negación
print(log1)                         #True
print(not log1)                     #False
print(not not log1)                 #True
print(not not not log1)             #False
print(not not not not log1)         #True

#Operador Binario &(and) |(or)
print("-- Operadores  Bimarios & |")
print(log1 or log2)                 #True
print(log1 | log2)                  #True

print(log2 or log2)                 #False
print(log2 | log2)                  #False

print(log2 and log1)                #False
print(log2 & log1)                  #False

print(log1 or nro1+2<nro2+(10*2-50/3))          #True
print(log1 | nro1+2<nro2+(10*2-50/3))           #True

print(not log1 and nro1+2<nro2+(10*2-50/3))     #False 
print(not log1 & nro1+2<nro2+(10*2-50/3))       #False 

print(nro1+2<nro2+(10*2-50/3) and not not not log2 and (log2 or not log1 or not not log2))
#              True            Y        True        Y  (False    o False  o   False    )
# False


