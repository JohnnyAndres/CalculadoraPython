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



coche1=vehiculos("Mazda","MX5")
coche2=vehiculos("Seat","Leon")
coche3=vehiculos("Renault","Magane")

coches=[coche1, coche2, coche3]  #Objeto a serializar

fichero=open("vehiculos_serializados", "wb") #Creamos el archivo externo donde vamos a serizalizar, con permiso de write binary, escritura binaria

pickle.dump(coches, fichero)

fichero.close()
del(fichero)

#Ahora recuperamos el archivo

fichero_serializado=open("vehiculos_serializados", "rb") #Abrmos el archivo donde hemos serializado

misVehiculos=pickle.load(fichero_serializado) #Cargamos el archivo con el metodo load
 
fichero_serializado.close()

for vehiculo in misVehiculos:
    print(vehiculo.estado())
    print("***********************")

    
