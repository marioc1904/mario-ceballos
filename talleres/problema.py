# Dado el peso (kg) y la altura del paciente (m), hallar el IMC
# IMC menor de 18.5 infrapeso
# IMC entre 18.5-24.9 peso normal
# IMC entre 25-29.9 sobrepeso 
# IMC entre 30-34.9 obesidad 
# IMC mayor de 35 obesidad mórbida 

Nombre = input("ingrese nombre del paciente :")
Peso = float(input("ingrese peso del paciente :"))
Altura = float(input("ingrese altura del paciente :"))
IMC = Peso/Altura**2 
if (IMC < 18.5) :
    print(f"El paciente {Nombre} tiene infrapeso")
elif (IMC >= 18.5 and IMC <25) :
    print (f"El paciente {Nombre} tiene peso normal")
elif (IMC >= 25 and IMC <30) :
    print (f"El paciente {Nombre} tiene sobrepeso")
elif (IMC >= 30 and IMC < 35) :
    print (f"El paciente {Nombre} tiene obesidad")
else :
    print (f"El paciente {Nombre} tiene obesidad mórvida")
