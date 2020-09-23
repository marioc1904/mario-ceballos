class Persona:
    def __init__(self, estaturaingresado, pesoingresado, nombreingresado, idingresado, edadingresado):
        self.raza = 'Humana'
        self.estatura = estaturaingresado
        self.edad = edadingresado
        self.nombre = nombreingresado
        self.peso = pesoingresado
        self.id = idingresado
        print ('Hola mundo estoy viv@')
    def caminar(self):
        print ("hola voy a caminar")
    def saludo (self, saludoespecial):
        print (saludoespecial)
class Biomedico (Persona):

    def cultivar_celulas (self):
        print( f'Hola soy {self.nombre} voy a cultivar celulas')
class arquitecto (Persona):

    def dibujarplanos (self):
        print( f'Hola soy {self.nombre} voy a cultivar celulas')


Karla = Persona(1.62, 48, 'Karla', 10239483892, 18)
Karla.caminar()

juan = Persona(1.80, 64, 'Juan Pablo', 9289392821, 23)
juan.caminar()
Karla.saludo('Holi crayoli')
juan.saludo ('Hola cocacola')

