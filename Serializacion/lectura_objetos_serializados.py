import pickle 

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

fichero_serializado=open("vehiculos_serializados", "rb") #Abrmos el archivo donde hemos serializado

misVehiculos=pickle.load(fichero_serializado) #Cargamos el archivo con el metodo load
 
fichero_serializado.close()

for vehiculo in misVehiculos:
    print(vehiculo.estado())
    print("***********************")

    
