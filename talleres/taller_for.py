#ejercicio 1

sumatoriatotal = 0 
for i in range (101): 
    sumatoria += i 
print (sumatoriatotal)

#ejercicio 2
preguntanumerofactorial = 'Ingresa un número para calcular su facturial :'
numerofactorial = 1 
numeroingresado = int(input(preguntanumerofactorial))
for i in range (numeroingresado):
    numerofactorial = numerofactorial* (i+1)
print (numerofactorial)

#ejercicio 3 

sumapositivos = 0
totalpositivos = 0
sumanegativos = 0
totalnegativos = 0
for i in range (6):
    nro=int(input('Número: '))
    if nro > 0: 
        sumapositivos = sumapositivos + nro 
        totalpositivos = totalpositivos+1 
    else: 
        sumanegativos = sumanegativos+nro
print('Sumatoria total de negativos: ', sumanegativos)
if totalpositivos !=0 :
    print('Promedio total de positivos: ', sumapositivos/totalpositivos)
else: 
    print('No se reconocio ningun numero positivo')





#ejercicio 4

import random 
canciones = ['canción1', 'canción2', 'canción3', 'canción4', 'canción5']
for cancion in canciones :
    print(cancion)
aleatorio = random.randint(0,4)
print(f'se seleccionó la siguiente canción: {canciones[aleatorio]}')
