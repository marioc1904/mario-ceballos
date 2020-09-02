#------se crea la listanombres----# 
listanombres = []
listanombres = ['Melany', 
        'Karla',
        'Laura Paredes',
        'Laura Montoya', 
        'Mario', 
        'Valeria',
        'Santi',]
listaedades =[20, 18, 18, 18, 21, 20, 18, 18]
print (listanombres)
print (listanombres [2])
print (listanombres [-1])
listanombres.append('Daniel')
listaedades.append(27)
print(listanombres[-1])
print (listanombres)

listanombres.pop(-1)
print (listanombres)
listanombres.append("Daniel")
sizelist = len (listanombres)
print (sizelist)

for i in range (sizelist):
    print (f"hola soy {listanombres[i]} y estoy feliz programando")
print ("segundo metodo")
for nombre in listanombres: 
    print(f"hola soy {nombre} y estoy feliz programando") 

for i in range (sizelist):
    print (f"nombre: {listanombres [i]} edad: {listaedades [i]}")

Listahobbies = []
decision = 0
while (decision ==0):
    hobbie =input("cual es tu hobbie favorito? : ")
    Listahobbies.append(hobbie)
    decision= input("""ingrese:
            si- para seguir agregando hobbies
            no- para finalizar
    : """)
print (Listahobbies)