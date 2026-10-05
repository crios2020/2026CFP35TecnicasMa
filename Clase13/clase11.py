print("-- Estructuras de repetición --")
print("- Estructura While -")
a=1
print("- Inicia la estructura while --")
while a<=10:
    print(a)
    a+=1
print("- Fin de Estructura while -")
print(a)

print("-- Sentencia break --")
a=1
while a<=10:
    print(a)
    a+=1
    if a==5:
        break
print("-- Sentencia break --")
a=1
while a<=10:
    a+=1
    if a==5:
        continue
    print(a)

# print("-- loop infinito --")
# a=1
# while True:
#     print(a)
#     a+=1

# print("-- loop infinito --")
# a=1
# while a<=10 or True:
#     print(a)
#     a+=1

# print("-- loop infinito --")
# a=1
# while a<=10 or a>=1:
#     print(a)
#     a+=1

# print("-- loop infinito --")
# a=1
# while a<=10:
#     print(a)

print("-- loop infinito --")
a=1
while a>=1:
    print(a)
    a+=1
