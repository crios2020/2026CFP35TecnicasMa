print("-- Clase09 --")
from datetime import datetime
ahora = datetime.now()

print("Año: ",ahora.year)
print("Mes: ",ahora.month)
print("Día: ",ahora.day)
print("Hora: ",ahora.hour)
print("Minutos: ",ahora.minute)
print("Segundos: ",ahora.second)
print("Día de semana: ",ahora.weekday())        
# Weekday:  0: Lunes    1: Martes ...... 6: Domingo

anio=ahora.year
mes=ahora.month
dia=ahora.day
hora=ahora.hour
minutos=ahora.minute
diaSemana=ahora.weekday()

#Versión 1
diaSemNombre=""
if diaSemana==0:
    diaSemNombre="Lunes"
elif diaSemana==1:
    diaSemNombre="Martes"
elif diaSemana==2:
    diaSemNombre="Miércoles"
elif diaSemana==3:
    diaSemNombre="Jueves"
elif diaSemana==4:
    diaSemNombre="Viernes"
elif diaSemana==5:
    diaSemNombre="Sábado"
elif diaSemana==6:
    diaSemNombre="Domingo"

print(diaSemNombre)

#Versión 2
diaSemNombre=""
if diaSemana==0:
    diaSemNombre="Lunes"
if diaSemana==1:
    diaSemNombre="Martes"
if diaSemana==2:
    diaSemNombre="Miércoles"
if diaSemana==3:
    diaSemNombre="Jueves"
if diaSemana==4:
    diaSemNombre="Viernes"
if diaSemana==5:
    diaSemNombre="Sábado"
if diaSemana==6:
    diaSemNombre="Domingo"

print(diaSemNombre)

#Versión 3
diaSemNombre=""

match diaSemana:
    case 0:
        diaSemNombre="Lunes"
    case 1:
        diaSemNombre="Martes"
    case 2:
        diaSemNombre="Miércoles"
    case 3:
        diaSemNombre="Jueves"
    case 4:
        diaSemNombre="Viernes"
    case 5:
        diaSemNombre="Sábado"
    case 6:
        diaSemNombre="Domingo"  

print(diaSemNombre)

print(mes)
nombreMes=""

if mes==1:
    nombreMes="Enero"
if mes==2:
    nombreMes="Febrero"
if mes==3:
    nombreMes="Marzo"
if mes==4:
    nombreMes="Abril"
if mes==5:
    nombreMes="Mayo"
if mes==6:
    nombreMes="Junio"
if mes==7:
    nombreMes="Julio"
if mes==8:
    nombreMes="Agosto"
if mes==9:
    nombreMes="Septiembre"
if mes==10:
    nombreMes="Octubre"
if mes==11:
    nombreMes="Noviembre"
if mes==12:
    nombreMes="Diciembre"

print(nombreMes)

frase="Hoy es "+diaSemNombre+" "+str(dia)+" de "+nombreMes+" del "+str(anio)
#print(frase)

# Determinar si estamos en día laboral o no (Día laboral, Día de descanso)
#Tipo de Día
tipoDia=""

# diaSemana= 0                  Odio los lunes porque hay que ir a trabajar
# diaSemana= 1, 2, 3            Día laboral
# diaSemana= 4                  Hoy es viernes y tu cuerpo lo sabe
# diaSemana= 5, 6               Día de descanso

tipoDia=""

if diaSemana==0:
    tipoDia="Odio los lunes, hay que ir a trabajar!"
if diaSemana==1 or diaSemana==2 or diaSemana==3:
    tipoDia="Hoy hay que ir a trabajar!"
if diaSemana==4:
    tipoDia="Hoy es viernes y tu cuerpo lo sabe!!"
if diaSemana==5 or diaSemana==6:
    tipoDia="Dia de descanso!"

# Obtener la estación del año (Verano, Otoño, Invierno, Primavera)
# mes=1, 2                          Verano
# mes=4, 5                          Otoño
# mes=7, 8                          Invierno
# mes=10, 11                        Primavera
# mes=3 and dia<21                  Verano
# mes=3 and dia>=21                 Otoño
# mes=6 and dia<21                  Otoño
# mes=6 and dia>=21                 Invierno
# mes=9 and dia<21                  Invierno
# mes=9 and dia>=21                 Primavera
# mes=12 and dia<21                 Primavera
# mes=12 and dia>=21                Verano

estacion=""
# if mes==1 or mes==2:
#     estacion="Verano"
# if mes==4 or mes==5:
#     estacion="Otoño"
# if mes==7 or mes==8:
#     estacion="Invierno"
# if mes==10 or mes==11:
#     estacion="Primavera"
# if mes==3 and dia<21:
#     estacion="Verano"
# if mes==3 and dia>=21:
#     estacion="Otoño"
# if mes==6 and dia<21:
#     estacion="Otoño"
# if mes==6 and dia>=21:
#     estacion="Invierno"
# if mes==9 and dia<21:
#     estacion="Invierno"
# if mes==9 and dia>=21:
#     estacion="Primavera"
# if mes==12 and dia<21:
#     estacion="Primavera"
# if mes==12 and dia>=21:
#     estacion="Verano"


# if mes==1 or mes==2 or (mes==3 and dia<21) or (mes==12 and dia>=21):
#     estacion="Verano"
# if mes==4 or mes==5 or (mes==6 and dia<21) or (mes==3 and dia>=21):
#     estacion="Otoño"
# if mes==7 or mes==8 or (mes==9 and dia<21) or (mes==6 and dia>=21):
#     estacion="Invierno"
# if mes==10 or mes==11 or (mes==12 and dia<21) or (mes==9 and dia>=21):
#     estacion="Primavera"

if mes==1:
    estacion="Verano"
if mes==2:
    estacion="Verano"
if mes==3:
    if dia<21:
        estacion="Verano"
    else:
        estacion="Otoño"
if mes==4:
    estacion="Otoño"
if mes==5:
    estacion="Otoño"
if mes==6:
    if dia<21:
        estacion="Otoño"
    else:
        estacion="Invierno"
if mes==7:
    estacion="Invierno"
if mes==8:
    estacion="Invierno"
if mes==9:
    if dia<21:
        estacion="Invierno"
    else:
        estacion="Primavera"
    if mes==10:
        estacion="Primavera"
if mes==11:
    estacion="Primavera"
if mes==12:
    if dia<21:
        estacion="Primavera"
    else:
        estacion="Verano"

frase+=", "+tipoDia+", Estamos en "+estacion
print(frase)
 
import locale
print(locale.getlocale())

