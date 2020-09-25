class Persona():
    def __init__(self, nombreIngresado, edadIngresado, idIn):
        self.nombre = nombreIngresado
        self.edad = edadIngresado
        self.id = idIn
    #Acciones
    #Hablar 
    def hablar (self, mensaje): 
        print (f'Hola soy {self.nombre} y tengo algo que decir : {mensaje}')
    #comer
    def comer (self, plato):
        print (f'Hola soy {self.nombre} y voy a comer un delicioso: {plato}')
