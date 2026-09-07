# https://github.com/crios2020/2026CFP35TecnicasMa
# Ejercicio 1 - Asignación básica
# Analice el código a continuación y complete la tabla correspondiente. Luego realice la codificación
# para confirmar que ha completado la tabla correctamente.
print("Ejercicio 1")
print("A")
x = 10                                                       
y = 20                             
print(x)                                        # 10                        
print(y)                                        # 20

print("B")
x = x + 5                        
y = y + 10                      
print(x)                                        # 15
print(y)                                        # 30

print("C")
x = x - 5                                                                      
y = y - 10                                      
print(x)                                        # 10
print(y)                                        # 20

print("D")
x = x * 3                                 
y = y * 5                                     
print(x)                                        # 30
print(y)                                        #100

print("E")
x = x / 2                                  
y = y / 4                              
print(x)                                        # 15
print(y)                                        # 25

# Tabla para completar:

#              X           Y
#A            10          20   
#B            15          30  
#C            10          20 
#D            30         100      
#E            15          25


# Ejercicio 2 - Asignación compacta
# Analice el código a continuación y complete la tabla correspondiente. Luego realice la codificación
# para confirmar que ha completado la tabla correctamente.
print("Ejercicio 2")
print("A")
x = 10                                
y = 20                               
print(x)                        # 10                                    
print(y)                        # 20
print("B")
x += 5                          
y -= 15                         
print(x)                        # 15 
print(y)                        #  5  
print("C")
x+=1               
y-=1
print(x)                        # 16      
print(y)                        #  4  
print("D")
x *= 4                             
y *= -3                            
print(x)                        # 64  
print(y)                        #-12  
print("E")
x /= 2                         
y /= 4                             
print(x)                        # 32  
print(y)                        # -3  

# Tabla para completar:

#              X           Y
#A            10          20
#B            15           5
#C            16           4
#D            64         -12
#E            32          -3


#Ejercicio 3 - Operadores aritméticos
print("Ejercicio 3")
print("A")
x = 10                                                  
y = 20                              
print(x)                        # 10
print(y)                        # 20

print("B")
x = x + y                             
y = y + x                      
print(x)                        # 30
print(y)                        # 50

print("C")
x= x - y                        
y= y - x                        
print(x)                        #-20
print(y)                        #70

print("D")
x=x * y                                    
y=x * x                       
print(x)                        #-1400
print(y)                        #1960000

print("E")                
x= y / x                    
y= x / y                  
print(x)                        #-1400
print(y)                        #-0.00071

# Tabla para completar:

#              X           Y
#A            10          20
#B            30          50
#C           -20          70
#D         -1400     1960000
#E         -1400          -0.00071


#Ejercicio 4- Operadores aritméticos con asignación compacta
print("Ejercicio 4")
print("A")
x = 5                    
y = 10                 
print(x)                        #  5        
print(y)                        # 10

print("B")
x += y            
y += x               
print(x)                        # 15
print(y)                        # 25


print("C")
x -= y           
y -= x               
print(x)                        #-10
print(y)                        # 35

print("D")
x *= y                  
y *= x              
print(x)                        #-350
print(y)                        #-12250


print("E")
x /= y                                        
y /= y                   
print(x)                        #0.028
print(y)                        #1

# Tabla para completar:

#              X           Y
#A             5          10 
#B            15          25
#C           -10          30
#D          -350       -1250
#E             0.028       1 

#Ejercicio 5- Operadores Aritméticos con asignación múltiple (suma y resta)
print("Ejercicio 5")
print("A")
x = 5
y = 10
suma = 0
resta = 0
print(x)                                #  5               
print(y)                                # 10
print(suma)                             #  0
print(resta)                            #  0


print("B")
suma = x + y                           
resta = x - y                          
print(x)                                #  5
print(y)                                # 10
print(suma)                             # 15
print(resta)                            #  5

print("C")
suma = x + x                           
resta = y - y                          
print(x)                                #  5
print(y)                                # 10
print(suma)                             # 10
print(resta)                            #  0

print("D")
suma = x + y + x                       
resta = x - x - 20                     
print(x)                                #  5
print(y)                                # 10
print(suma)                             # 20
print(resta)                            #-20

print("E")
suma = y + x + x                      
resta = -x - y -y                      
print(x)                                #  5
print(y)                                # 10
print(suma)                             # 20   
print(resta)                            #-25

# Tabla para completar:

#              X           Y           suma        resta
#A             5          10              0            0
#B             5          10             15            5
#C             5          10             10            0    
#D             5          10             20          -20   
#E             5          10             20          -25 



#Ejercicio 6- Operadores Aritméticos con asignación múltiple (producto y división)
print("Ejercicio 6")
print("A")
x = 5
y = 10
multi = 1
division = 1
print(x)                        #   5           
print(y)                        #  10
print(multi)                    #   1
print(division)                 #   1

print("B")
multi = x * y
division = x / y
print(multi)                    # 50
print(division)                 #  0.5

print("C")
multi = x * x
division = y / y
print(multi)                    # 25
print(division)                 #  1

print("D")
multi = x * y * x                      
division = y / x                       
print(multi)                    #250
print(division)                 #  2

print("E")
multi= x * (-y)                       
division= y / (-x)                     
print(multi)                    #-50
print(division)                 # -2

# Tabla para completar:

#              X           Y           multi       division
#A             5          10               1            1
#B             5          10              50            0.5
#C             5          10              25            1
#D             5          10             250            2
#E             5          10             -50           -2

print("-- Operador Resto % --")
print(15%2)             #  1
print(14%2)             #  0
print(-14%2)            #  0
print(-15%2)            #  1
print(28%5)             #  3          

#Ejercicio 7- Operador Resto   %
print("Ejercicio 7")
print("A")
n1 = 20
n2 = 2
n3 = n1 % n2
print(n3)                       # 0

print("A")
n1 = 15
n2 = 2
n3 = n1 % n2
print(n3)                       # 1

print("C")
n1 = 3
n2 = 20
n3 = n2 % n1
print(n3)                       #2

print("D")
n1 = 3
n2 = 15
n3 = n2 % n1    
print(n3)                       # 0  

        # Tabla para completar:

#             n1       n2      n3
#A            20       2        0
#B            15       2        1
#C             3       20       2
#D             3       15       0

#Ejercicio 8 - Cadenas de Caracteres
print("A")
palabra_1 = "Hola"
palabra_2 = "Mundo"
frase = ""
print(palabra_1)         # Hola 
print(palabra_2)         # Mundo
print(frase)             # 

print("B")
frase = palabra_1 + palabra_2          
print(palabra_1)        # Hola
print(palabra_2)        # Mundo
print(frase)            # HolaMundo

print("C")
frase=palabra_1+" "+palabra_2
print(frase)

# Tabla para completar:

#             palabra1         palabra2        frase
#A             Hola             Mundo         
#B             Hola             Mundo           HolaMundo    
#C             Hola             Mundo           Hola Mundo