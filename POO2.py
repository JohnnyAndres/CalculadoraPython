class Coche(): 
    largoChasis=250  
    anchoChasis=120
    ruedas=4
    enMarcha=False #Estado inicial: Se especifica ese estado inicial de la clase con un constructor
                   #Un constructor es un metodo que da estado inicial a los objetos pertenecientes a una clase
    
    def arrancarCoche(self, arrancamos): 
        self.enMarcha=arrancamos
        if (self.enMarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"    

    def estado(self):
        print("El coche tiene ", self.ruedas, " ruedas. Un ancho de ", self.anchoChasis, " y un largo de",
        self.largoChasis)      

miCoche = Coche() 
print(miCoche.arrancarCoche(True))
miCoche.estado()

print("*************A continuación creamos el segundo objeto******************")

miCoche2 = Coche()
print(miCoche2.arrancarCoche(False))
miCoche2.estado()
