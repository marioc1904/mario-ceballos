#Se quiere probar un medidor de temperatura para evaluar los pasajeros que ingresan del extranjero según su temperatura como medida preventiva del coronavirus.
#Temperatura menor de 36 el pasajero esta en estado de hipotermia.
#Temperatura entre 36-38.4 el pasajero se encuentra en estado saluable.
#Temperatura entre 38.5-40 el pasajero se encuentra en estado de alerta.
#Temperatura mayor de 40 el pasajero se encuentra en estado de peligro. 
#Adicional si el pasajero viene de China, Iran o Italia sera llevado a un quinto grupo llamado estado de observación.

print("Bienvenido a marito´s airline")
Nombre= input("Ingrese nombre del pasajero :")
Temperatura= float(input("Ingrese temperatura del pasajero :"))
Pais = input("Ingrese el país de procedencia del pasajero :")

if (Temperatura < 36):
    print (f"El pasajero {Nombre} se encuentra en estado de hipotermia")
elif (Temperatura>= 36 and Temperatura <38.5):
    print (f"El pasajero {Nombre} se encuentra en estado saludable")

elif (Temperatura> 38.5 and Temperatura <40 ):
    print(f"El pasajero {Nombre} se encuentra en estado de alerta")
else : 
    print(f"El pasajero {Nombre} se encuentra en estado de peligro")
if (Pais== "China"): 
    print (f"El pasajero {Nombre} debe ser sometido a estado de observación")
elif (Pais=="Iran") :
    print (f"El pasajero {Nombre} debe ser sometido a estado de observación")
elif (Pais== "Italia") :
    print (f"El pasajero {Nombre} debe ser sometido a estado de observación")
else : 
    print (f"{Nombre} bienvenido abordo, te deseamos un muy buen viaje!")
