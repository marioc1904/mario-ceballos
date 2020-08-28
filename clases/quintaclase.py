#------preguntas-----#
preguntanumero = 'ingrese un numero del 1 al 10:'
#-------mensaje--------# 
mensajefallido = 'Fallaste!!, no es el número secreto'
mensajeexitoso ='Felicitaciones has acertado el número en el que pense'
mensajederrota= 'Douh, has perdido suerte en la proxima'
mensajedespedida = 'Gracias por haber participado'
mensajevida= 'Ten cuidado has perdido {} vida te quedan {}'
#ciclos while

numerosecreto = 6
numeroingresado = int(input(preguntanumero))
vidasperdidas = 0
while(numerosecreto != numeroingresado and vidasperdidas<=3) :
    vidasperdidas = vidasperdidas +1
    print(mensajevida.format(vidasperdidas, 3-vidasperdidas ))
    print(mensajefallido)
    if vidasperdidas <3: 
        numeroingresado = int(input(preguntanumero))

if vidasperdidas <3:
    print(mensajeexitoso)
else: 
    print(mensajederrota)


print(mensajedespedida)


#--------preguntas------# 
preguntaVocal = 'ingrese una vocal :'
#----------mensajes-------#
mensajeFallido ='Rayos!, no es la vocal que tengo en mente'
mensajeExitoso = 'Wow!!, lograste adivinar la palabra'
mensajeDespedida = 'Eres un crack, espero vencerte la proxima vez'
#ciclo while

vocalsecreta = "a" 
vocalingresada = input(preguntaVocal)
while(vocalsecreta != vocalingresada):
    print(mensajeFallido)
    vocalingresada = input(preguntaVocal)
print(mensajeExitoso)
print(mensajeDespedida)
