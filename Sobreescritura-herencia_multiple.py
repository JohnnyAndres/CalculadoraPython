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


class Moto(vehiculos): 
    hCaballito=""
    def caballito(self):
        self.hCaballito="Voy haciendo el caballito"

    def estado(self): #Se sobreescribe el metodo estado, para poder mostrar el estado con las caracteristicas propias de la clase moto, esta sobreescritura anula el metodo estado de la clase padre y toma en cuenta el metodo estado de la clase Moto.
        print("marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", 
        self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena,
        "\n", self.hCaballito)

miMoto=Moto("Honda","CBR")
miMoto.caballito()

miMoto.estado()

class furgoneta(vehiculos):
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"    

miFurgoneta=furgoneta("Renault", "Kangoo")       

miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class vehiculosElectricos():
    cargando=False
    def __init__(self, marca_bicicleta, modelo_bicicleta):
        super().__init__(marca_bicicleta, modelo_bicicleta) #Super llama al metodo de la clase padre 
        self.autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True


class bicicletaElectrica(vehiculosElectricos, vehiculos): #La clase bicicleta hereda de vehiculos y de vehiculos electricos
    def estado(self): #Se sobreescribe el metodo estado, para poder mostrar el estado con las caracteristicas propias de la clase moto, esta sobreescritura anula el metodo estado de la clase padre y toma en cuenta el metodo estado de la clase Moto.
        super().estado()
        print("\nAutonomia",self.autonomia, "\nCargando",self.cargando)


miBici=bicicletaElectrica("Orbea", "modelo") #Le da prioridad al constructor de la primera clase pasada primero (vehiculos)
miBici2=vehiculos("Orbea", "modelo") #Le da prioridad al constructor de la primera clase pasada primero (vehiculos)

miBici.cargarEnergia()
miBici.estado()
miBici2.estado()


#Principio de sustitucion: "es siempre un/a" Cuando hay herencia una subclase siempre sera 
#un objeto de la superclase. Una bicileta siempre sera primero un vehiculo. Pero un vehiculo no siempre es una bicicleta.

#isinstance() función que nos indica si un objeto es instancia de una clase determinada. 
#Devuelve True o False.

print("Es instancia: ", isinstance(miBici, vehiculos))

print("Es instancia: ", isinstance(miBici, vehiculosElectricos ))

print("Es instancia: ", isinstance(miBici2, vehiculosElectricos ))
