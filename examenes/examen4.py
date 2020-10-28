print ('opinion: \n Mira como agrego cosas jeje')

opinion= input('ingrese su opinion: \n')
archivo = open ('parrafo.txt', 'w', encoding= 'UTF-8')
archivo.write(f'Esto es lo que pienso: \n {opinion} \n')

archivo.close()


archivo = open ('parrafo.txt', encoding= 'UTF-8')
print(archivo)
archivo.close()









