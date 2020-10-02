# crear una función por cada uno de estos puntos 

#Dada un número devolver el número elevado al cuadrado 

def alcuadrado (numero1): 
    return numero1**2 
numeroalcuadrado = alcuadrado(2)
print (numeroalcuadrado)


#Dada un número devolver el número elevado a la tres
def alcubo (numero2): 
    return numero2**3
numeroalcubo = alcubo(3)
print (numeroalcubo)

#Dada un número devolver el número elevado a la cuatro 

def alacuatro (numero3):
    return numero3**4 
numeroalacuatro = alacuatro(4)
print(numeroalacuatro)

#Dada un número devolver el número elevado a la cinco

def alacinco (numero4):
    return numero4**5
numeroalacinco = alacinco(5)
print (numeroalacinco)

#Crear una función que dada una de las funciones anteriores y sus entradas muestre en pantalla el resultado de las mismas





#Como ingeniero Biomédico se le pide que cree unas clases referentes a los pacientes de un hospital, las cuales deben ser las siguientes

#--Doctor--# 

class Doctor ():
#caracteristicas
    def __init__ (self, idIN, nombreIN, sexoIN, universidadIN):
        self.id =idIN 
        self.nombre = nombreIN
        self.sexo = sexoIN 
        self.universidad = universidadIN

#atributos
    def atributos (self):
        print (f'Hola mi documento es {self.id}, me identifico como el Doc {self.nombre}, mi sexo es {self.sexo} y me gradue de la {self.universidad}. Segun lo que veo tienes: ')

#lista de sintomas
    def mostrarlista(self, lista):
        for elemento in lista :
            print (elemento)


doctor = Doctor (1001297439, 'Pepito', 'Masculino', 'Universidad CES')
sintomas = ['Dolor de cabeza', 'Malestar', 'Vomito', 'Diarrea']

doctor.atributos()
doctor.mostrarlista(sintomas)

#--Clase neurologo--# 

class Neurologo(Doctor):
    def __init__ (self, idIN, nombreIN, sexoIN, universidadIN, experienciaIN, consultorioIN, salarioIN):
        Doctor.__init__(self, idIN, nombreIN, sexoIN, universidadIN)
        self.experiencia1 = experienciaIN
        self.consultorio1 = consultorioIN
        self.salario1 = salarioIN

#Mostrar 
    def mostrar(self): 
        print (f'Hola soy neurologo; mi documento es {self.id}, me identifico como el Doc {self.nombre}, mi sexo es {self.sexo} y me gradue de la {self.universidad}. Tengo una experiencia de {self.experiencia1}, mi consultorio es {self.consultorio1} y gano un salario mensual de {self.salario1} ')

#Atención pacientes 
    def pacientes (self, list):
        for pacientes in listanombres:
            print (f'Atenderé al paciente {pacientes}')



neurologo = Neurologo(1001297439, 'Pepito', 'Masculino', 'Universidad CES', 'tres años', 1904, 10000000)
listanombres = ['El PEPE', 'El bicho', 'Messi', 'El soanfonson']
neurologo.mostrar()
neurologo.pacientes(listanombres)





#-- cardiologo--# 
class Cardiologo (Doctor):
    def __init__ (self, idIN, nombreIN, sexoIN, universidadIN, experienciaING, consultorioING, salarioING):
        Doctor.__init__(self, idIN, nombreIN, sexoIN, universidadIN)
        self.experiencia2 = experienciaING
        self.consultorio2 = consultorioING
        self.salario2 = salarioING 

#caracteristicas 
    def caracteristicas(self):
        print (f'Hola soy cardiologo; mi documento es {self.id}, me identifico como el Doc {self.nombre}, mi sexo es {self.sexo} y me gradue de la {self.universidad}. Tengo una experiencia de {self.experiencia2}, mi consultorio es {self.consultorio2} y gano un salario mensual de {self.salario2}')


# mostrar sintomas 
    def mostrarsintomas(self, listasintomas):
        for elemento in listasintomas :
            print (elemento)

cardiologo = Cardiologo(1001297439, 'Pepito', 'Masculino', 'Universidad CES', 'diez años', 8032, 30000000)
Sintomas = ['Taticardia', 'Sudoración fría', 'Dolor en el pecho']

cardiologo.caracteristicas()
cardiologo.mostrarsintomas(Sintomas)
print ('Ya se que tiene este paciente')





