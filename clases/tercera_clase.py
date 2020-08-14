a = int(input("ingrese el primer número :"))
b = int(input("ingrese el segundo número :"))
print (a,b)

if (a == b):
    print("son números iguales")
elif (a>b):
    print ("el numero A", a, "es mayor que el numero", b)
else:
    print (f"el numero B {b} es mayor que A {a}")

#Dada una temperatura, determinar si el paciente esta sano o no
#Temperatura menor a 36 grados hipotermia
#Temperatura en el intervalo de 36-37.5 normal
#Temperatura en el intervalo de 37.5-38 alerta 
#Temperatura menor a 38- fiebre
#muestre el nombre del paciente y su estado 

nombre = input("ingrese nombre del paciente :")
temperatura = float (input("ingrese la temperatura del paciente :")) 
if (temperatura < 36) :
    print(f"El paciente llamado {nombre} sufre de hipotermia")
elif (temperatura>= 36 and temperatura < 37.5):
    print(f"El paciente llamado {nombre} se encuentra en buen estado")
elif (temperatura>= 37.5 and temperatura <38):
    print(f"El paciente llamado {nombre} se encuentra en estado de alerta")

else:
    print(f"el paciente llamado {nombre} se encuentra con fiebre")
