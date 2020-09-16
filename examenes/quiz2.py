#---entrada---#
listaPesos = [20000, 30000, 4000, 2500, 1000, 7600]

#---preguntas---# 
menu = '''
            1- Convertir lista 
            2- Agregar un valor a la lista
            3- Ver maximo y minimos de la lista
            4- Eliminar un valor 
            5- Salir del programa
: '''

#---pregunta conversión---#  
conversionlista = '''
            C- Mostrar lista en pesos colombianos
            D- Mostrar lista en dolares 
            E- Mostrar lista en euros 
: ''' 

#---pregunta agregar valor---# 
mensajeAgregar = 'agregue un numero a la lista : '


#---maximo y minimo---# 
mayor = max (listaPesos)
menor = min (listaPesos)
promedio = len (listaPesos)/6

#--- eliminar valor---# 
mensajeeliminar= 'elimine un valor de la lista : '


#---mensaje error---# 
mensajeErrorC = 'ingresaste una opcion invalida, recuerda ingresar una opcion valida C, D, E'
mensajeErrorM = 'ingresaste una opcion invalida, recuerda ingresar una opcion valida 1, 2, 3, 4, 5'

#--- mensajes---#
mensajeopcion = 'Usted escogio la opción {}'
mensajesalida = 'Gracias por utilizar nuestro programa'
mensajepesos= 'No es necesaria la conversión, pero se muestra la lista'

#---Inicio---#
opcion = int(input(menu))

#---Calculo cambio de moneda---# 

listaDolares = []
listaEuros = []
listapesoscol= listaPesos

#---Cambio a dolares---# 
for elemento in listapesoscol: 
    dolares = elemento*0.00027
    listaDolares.append(dolares)


#---Cambio a euros---#
for elemento in listapesoscol:
    euros = elemento*0.00023
    listaEuros.append (euros)

#---Menu---#
while (opcion != 5):
    if (opcion == 1) :
        print (mensajeopcion.format(1))
        #pregunta conversión
        conversion = input(conversionlista)
        if (conversion == 'C'): 
            print (mensajepesos)
            print (listapesoscol)
        elif (conversion == 'D'):
            print (listaDolares)
        elif (conversion == 'E'):
            print(listaEuros)
        else:
            print(mensajeErrorC)
    elif (opcion == 2): 
        print(mensajeopcion.format(2))
        agregar= float(input(mensajeAgregar))
        listaPesos.append(agregar)
        print(listaPesos)
    elif (opcion == 3):
        print(mensajeopcion.format(3))
        print ('El valor minimo es', menor)
        print ('El valor maximo es', mayor)
        print ('El promedio es', promedio)
    elif (opcion == 4): 
        print(mensajeopcion.format(4))
        print(listaPesos)
        eliminar= int(input(mensajeeliminar))
        listaPesos.pop(eliminar)
        print(listaPesos)
    else: 
        print(mensajeErrorM)
    opcion = int(input(menu))



#---Salida---# 
print(mensajesalida)

