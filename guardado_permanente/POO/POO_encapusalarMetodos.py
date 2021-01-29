#Encapsular Metodo: Que el metodo solo sea accesible desde dentro de la clase

class Coche():

    def __init__(self):  
        self.largoChasis=250  
        self.anchoChasis=120
        self.__ruedas=4  
        self.enMarcha=False 
    
    def arrancarCoche(self, arrancamos): 
        self.enMarcha=arrancamos
        if (self.enMarcha):
            chequeo=self.__chequeo_interno()  

        if (self.enMarcha and chequeo):
            return "El coche está en marcha"
        elif(self.enMarcha and chequeo == False):
            return "Algo ha salido mal en el chequeo, no podemos arrancar"
        else:
            return "El coche está parado"        

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.anchoChasis, " y un largo de",
        self.largoChasis)     

    def __chequeo_interno(self): #Este metodo solo deberia usarse desde dentro de la clase, cuando el coche es por arrancar no cuando este en marcha o parado
        print("Realizando chequeo interno")    
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

#*************LLAMADAS DE LOS METODOS***************#
miCoche = Coche() 
print(miCoche.arrancarCoche(True))
miCoche.estado()

print("*************A continuación creamos el segundo objeto******************")

miCoche2 = Coche()
print(miCoche2.arrancarCoche(False))
miCoche2.__ruedas=5 #Esta propiedad no tiene funcionamiento, ya que la propiedad __ruedas esta encapsulada, solo tiene acceso desde la propia clase
miCoche2.estado()
