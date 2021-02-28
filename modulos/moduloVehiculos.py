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


class furgoneta(vehiculos):
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"    


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


