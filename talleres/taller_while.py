#ejercicio 1 

preguntanumero= "Por favor ingresa un número entero o para finalizar ingresa el numero 0 : "

numeroingresado = int(input(preguntanumero))
sumatoriatotal = 0 
while (numeroingresado != 0):
    sumatoriatotal += numeroingresado
    numeroingresado = int(input(preguntanumero))
print (sumatoriatotal)

#ejercicio 2 

preguntanumero1 = 'Ingresa un número por favor : '
preguntanumero2 = 'Ingrese un número mayor al ingresado previamente por favor: '
mensajeError = 'Ingresa un número mayor a {}' 

primernumero = int (input(preguntanumero1))
segundonumero = int (input(preguntanumero2))

while (primernumero > segundonumero) :
    print (mensajeError.format(primernumero))
    segundonumero = int(input (preguntanumero2))
mensajedespedida= print ('Gracias por participar')


#ejercicio 3 

PreguntanumeroA = 'Ingrese un numero entero por favor :'
PreguntanumeroB = 'Ingrese un numero entero mayor al numero anterior por favor :'
Mensajedeerror = 'Recuerda ingresar un numero mayor, el {}  es mayor que {}, por lo cual, no es valido'
mensajeentrada = 'ingresa un numero mayor al anterior, para finalizar escriba un numero menor'
numeroA = int(input(PreguntanumeroA))
numeroB = int(input(PreguntanumeroB))

while (numeroB > numeroA) :
    print (Mensajedeerror.format (numeroB, numeroA))
    numeroA = numeroB
    print(mensajeentrada)
numeroB = int(input(PreguntanumeroB))

mensajeDespedida = print('Gracias por participar')

#ejercicio 4 

total = 0 
montocompra = float(input('monto de la venta: $'))
while montocompra!= 0 :
    if montocompra <0 : 
        print ('Monto no válido')
    else:
        total+=montocompra 
    montocompra = float(input('Monto de la venta: $'))
if total>1000:
    total-=total*0.1 
    print('Monto total a pagar: $', total)
