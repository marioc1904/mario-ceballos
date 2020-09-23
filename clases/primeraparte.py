class TortaRedonda: 
    def __init__ (self, saborIngresado): 
        self.forma = 'Redonda' 
        self.sabor = saborIngresado
        #acción al crear objeto 
        print ('Soy una torta nueva')
    def __mostrar_atributos (self): 
        print (f"soy de forma {self.forma} y de sabor {self.sabor}")
tortaChocolate = TortaRedonda('Chocolate')
tortaVainilla = TortaRedonda('Vainilla')

print (tortaChocolate.sabor)
print (tortaVainilla.sabor)
print (tortaChocolate.forma)
print (tortaVainilla.forma)

