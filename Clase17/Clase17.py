print("-- Clase17 --")
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

#Versión 4
semana=['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
diaSemNombre=semana[diaSemana]
print(diaSemNombre)


meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
nombreMes=meses[mes-1]
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

#funciones
def cartel():
    print("***************************************************************************")
    print("*                          HOLA A TODOS !!!                               *")
    print("***************************************************************************")

#función parámetrica
def cartel2(texto):
    print("***************************************************************************")
    print(texto)
    print("***************************************************************************")

#función con devolución de valor
def sumar(nro1, nro2):
    return nro1+nro2

cartel()
cartel()
cartel()
cartel2("Hoy es lunes")
cartel2(frase)
print(sumar(23,39))


#Crear una función que devuelva el nombre del mes actual
def getNombreMes():
    ahora = datetime.now()
    mes=ahora.month
    meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    return meses[mes-1]

print(getNombreMes())

#Crear una función que devuelva el nombre del día de la semana
def getNombreDía():
    ahora = datetime.now()
    diaSemana=ahora.weekday()
    semana=['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
    return semana[diaSemana]

print(getNombreDía())