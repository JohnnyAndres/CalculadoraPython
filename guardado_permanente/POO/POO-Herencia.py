#Herencia: Hay una clase en la parte alta: la clase padre o superclase,
#Y luego esta una subclase de la clase alta que tambien puede
# ser superclase de otras clases hijas o subclases. 

#La herencia sirve para reutilizar código en caso de crear objetos similares.

#¿Que caracteristicas, comportamientos tienen en comun los obejtos que se van a crear?

class vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False


    def arrancar(self):
        self.enMarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True    

    def estado(self):
        print("marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", 
        self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


class Moto(vehiculos): #Sintaxis para herencia de una clase: class nuevaInstancia(clase_de_donde_hereda)
    pass

miMoto=Moto("Honda","CBR") #Instancia 

miMoto.estado()