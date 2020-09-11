import random 
mensajefallido ='lo siento, ese no es el numero'
mensajeexitoso= 'felicidades, es el numero'
mensajedespedida='hasta lueguito'
mensajefallos = 'raios, te has equivocado {} sigue intentando'

dado = random.randint (1,6)
print(dado)
vecesfallidas=0
numeroparaadivinar = dado 
preguntanumero = 'juguemos un juego jejejeejej, Adivina el numero:'
numeroingresado = int(input(preguntanumero))

while (numeroparaadivinar != numeroingresado and vecesfallidas >=0) :
    vecesfallidas = vecesfallidas +1
    print (mensajefallos.format (vecesfallidas))
    print(mensajefallido)
    numeroingresado = int(input(preguntanumero))
print(mensajeexitoso)
print(mensajedespedida)



listacomidafavorita =[]

decision = "si"
while (decision == "si"):
    comidafavorita = input ('cual es tu comida favorita :')
    listacomidafavorita.append(comidafavorita)
    decision = input(""" ingrese :
            si- para agregar otra comida favorita
            no- para terminar lista
    :""")
sizelist= len(listacomidafavorita)
for i in range (sizelist): 
    print (listacomidafavorita[i])
print (listacomidafavorita[2])