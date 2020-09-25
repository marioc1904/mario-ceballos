import persona as p 
import estudiante as es

class Egresado (es.Estudiante):
    def __init__ (self, nombreIngresado, edadIngresado, idIn, carreraIn, fechaIn):
        es.Estudiante.__init__(self, nombreIngresado, edadIngresado, idIn, carreraIn, 'Egresado')
        self.fecha = fechaIn
    def trabajar (self, emprender):
        print (f'Hola soy {self.nombre} voy a emprender en {emprender}')
