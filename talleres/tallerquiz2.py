# entradas
Temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

#preguntas
preguntamenu = '''
            1- convertir temperatura
            2- Estado de salud de c/U de las temperaturas
            3- Ver máximo y minimo de temperaturas
            4- Para salir del programa
: '''
preguntaconversiontemperatura = '''
            F- convertir temperatura fahrenheit
            F- convertir temperatura Kelvin
            K- 
            C- Ver máximo y minimo de temperaturas

: '''


#mensaje error#
mensajentradanovalidaT = 'recuerde ingresar una opcion valida F, K, C'
mensajeentradanovalidaN ='recuerde ingresar una opcion valida 1, 2, 3, 4'

# mensajes
mensajeopcion = 'usted escogio la opcion {}'
mensajesalida = 'gracias por usar el programa'
mensajecelsius = 'No es necesaria la conversión, pero se muestra la lista'

#Inicio codigo
opcion = int(input(preguntamenu))

# calculos preliminares
#------pasarlo a kelvin-----
listaKelvin = []
listaFahrenheit = []
listacelcius= Temperatura_Corporal
listaestadosSalud = []

# ----pasando a kelvin xc +237.15--- #
for elemento in listacelcius:
    kelvin = elemento + 273.15
    listaKelvin.append(kelvin)

# ---- pasando a fahrenheit (xc*1.8) + 32----#
for elemento in listacelcius:
    fahrenheit = (elemento*1.8) + 32
    listaFahrenheit.append (fahrenheit)

#--- detectando los estados de salud ---#
for elemento in listacelcius :
    estado = ''
    if elemento < 36 : 
        estado = 'Hipotermia'
    elif (elemento >= 36 and elemento < 37.6):
        estado = 'Normal'
    else :
        estado = 'Fiebre'
    listaestadosSalud.append(estado)

#---- calcular maximo y minimo ----# 
mayor = max (listacelcius)
menor = min (listacelcius)
frecuencia = len (listacelcius)/24

#Menu 
while (opcion != 4) :
    if (opcion == 1): 
        print (mensajeopcion.format(1))
        #pregunta conversion 
        conversion = input(preguntaconversiontemperatura)
        if (conversion == 'K'):
            print (listaKelvin)
        elif (conversion =='f') :
            print (listaFahrenheit)
        elif (conversion == 'c'):
            print (listacelcius)
        else :
            print(mensajeentradanovalidaN)
    elif (opcion == 2):
        print(mensajeopcion.format(2))
        print (listaestadosSalud)
    elif (opcion == 3) :
        print (mensajeopcion.format (3))
        print ('la temperatura máxima fue', mayor)
        print('la temperatura minima fue', menor)
        print ('la temperatura fue comata con una frecuencia de', frecuencia)
    else :
        print (mensajeentradanovalidaN)


#salida del programa
print(mensajesalida)