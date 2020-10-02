#ejercicio 1 
a = int(input('Ingrese un numero : '))
b = int(input('Ingrese otro numero : '))

def numero (numero1, numero2):
    if numero1 > numero2: 
        print (f'{numero1} es mayor que {numero2}')
    elif numero2 > numero1:
        print (f'{numero2} es mayor que {numero1}')
    else : 
        print ('los dos numeros son iguales')



#ejercicio 2
def lalista (lista):
    for elemento in lista: 
        print (elemento)

nombres = ['santiago, mario, melany, karla']
lalista(nombres)



#ejercicio 3 

def calcularIMC (peso, altura): 
    return peso/(altura**2)
imc = calcularIMC (70, 1.77)
print (imc)
calcularIMC(70, 177)



#ejercicio 4 

def mostrarIMC (IMC, peso, altura):
    imc=  IMC (peso, altura)
    print (f'El IMC es de {imc}')

mostrarIMC(calcularIMC, 70, 1.77)



#ejercicio 5
class persona():
    def __init__ (self, idIN, nombreIN, pesoIN, alturaIN, sexoIN):
        self.id = idIN 
        self.nombre = nombreIN
        self.peso = pesoIN 
        self.altura = alturaIN 
        self.sexo = sexoIN 
        print ('se ha creado un nuevo perfil')
    def atributos (self):
        print (f'Hola me llamo {self.nombre}, mi sexo es {self.sexo}, peso {self.peso}, mido {self.altura} y mi id es {self.id}')
humano1 = persona (10293930493, 'maribel', 68, 1.65, 'femenino')
humano1.atributos()

#ejercicio 6
class Estudiante(persona):
    def __init__ (self, idIN, nombreIN, pesoIN, alturaIN, sexoIN, carreraIN, semestreIN, universidadIN):
        persona.__init__ (self, idIN, nombreIN, pesoIN, alturaIN, sexoIN)
        self.carrera = carreraIN 
        self.semestre = semestreIN
        self.universidad = universidadIN 
    def mostrar (self):
        print (f'Hola me llamo {self.nombre}, mi sexo es {self.sexo}, peso {self.peso}, mido {self.altura}, mi id es {self.id}, estudio {self.carrera}, esto en el semestre {self.semestre} y estudio en {self.universidad}')
    def estudiar (self, materia):
        print(f'Voy para {materia}')

estudiante1 = Estudiante(10293930493, 'maribel', 68, 1.65, 'femenino', 'Biomedica', 3, 'Universidad CES')
estudiante1.mostrar()
estudiante1.estudiar ('programación')





