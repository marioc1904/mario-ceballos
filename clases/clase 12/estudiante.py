import persona as p
class Estudiante (p.Persona):
    def __init__ (self, nombreIngresado, edadIngresado, idIn, carreraIn, semestreIn):
        p.Persona.__init__(self, nombreIngresado, edadIngresado, idIn)
        self.carrera = carreraIn
        self. semestre = semestreIn
    
    def estudiar (self, materia):
        print (f'Hola soy{self.nombre} y estoy muy motivad@ pues estudiare {materia}')