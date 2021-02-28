
#polimorfismo: muchas formas: Un objeto puede cambiar de forma

class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")



class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")



class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")



miVehiculo=Moto()
miVehiculo.desplazamiento()

miVehiculo2=Coche()
miVehiculo2.desplazamiento()

miVehiculo3=Camion()
miVehiculo3.desplazamiento()


#*******CON POLIMORFISMO************#


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo4=Camion()    
miVehiculo5=Moto()  
miVehiculo6=Coche()  
desplazamientoVehiculo(miVehiculo4)
desplazamientoVehiculo(miVehiculo5)
desplazamientoVehiculo(miVehiculo6)