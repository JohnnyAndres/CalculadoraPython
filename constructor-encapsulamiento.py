#Estado inicial: Se especifica ese estado inicial de la clase con un constructor
# #Un constructor es un metodo que da estado inicial a los objetos pertenecientes a una clase
class Coche():

    def __init__(self):  #Nomenclatura para el constructor de una clase
        self.largoChasis=250  
        self.anchoChasis=120
        self.__ruedas=4  #La variable no es accesible desde fuera de la clase
        self.enMarcha=False 
    
    def arrancarCoche(self, arrancamos): 
        self.enMarcha=arrancamos
        if (self.enMarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"    

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.anchoChasis, " y un largo de",
        self.largoChasis)      

miCoche = Coche() 
print(miCoche.arrancarCoche(True))
miCoche.estado()

print("*************A continuación creamos el segundo objeto******************")

miCoche2 = Coche()
print(miCoche2.arrancarCoche(False))
miCoche2.__ruedas=5 #Modificamos el estado de las ruedas del objeto: Para evitar que una propiedad no se pueda
#modificar desde fuera de la clase se debe encapsular la propiedad cuando sea necesario. self.__propiedad
miCoche2.estado()
