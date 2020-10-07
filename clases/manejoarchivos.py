#leer

archivo = open ('poema.txt', encoding= 'UTF-8')
print (archivo)
archivo.close()

lineas = archivo.readlines()
print (lineas)
listaRenglones =[]
with open ('poema.txt', encoding= 'UTF-8')as lineas: 
    for line in lineas:
        print(line)
        listaRenglones.append(line)

print (listaRenglones)

print ('saludo: \nHola como estas')
print ('saludo: \t\t\t\t hola como estas')

nombre = input ('ingrese su nombre: ')
edad = int (input('ingrese su edad: '))
opinion = input ('ingrese su opinion : \n')

archivo = open ('opinion.txt', 'w', encoding='UTF-8')
archivo.write(f'opinion de {nombre}\n')
archivo.write(f'edad : {edad}\n')
archivo.write(f'reseña:\n {opinion}\n')

archivo.close()