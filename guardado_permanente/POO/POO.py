#clases
class Coche(): #clase
    largoChasis=250  #Propiedad de la clase coche
    anchoChasis=120
    ruedas=4
    enMarcha=False

    #def:palabra reservada para crear funciones. Una funcion especial son los
    #metodos; funciones que pertenecen a una clase
    
    def arrancarCoche(self): #self: objeto perteneciente a la clase O_O o_O similar al this, self si debe ponerse obligatoriamente
        self.enMarcha=True

    def estado(self):
        if(self.enMarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"        

#El comportamiento (Que es capaz de hacer un objeto) viene determinado por los metodos 

miCoche = Coche() #nombre del objeto, instancia o ejemplar = la clase a la que pertenece -> Instanciar una clase

print("El largo del coche es " , miCoche.largoChasis)

miCoche.arrancarCoche() #Llama al metodo y recibe por parametro el propio objeto

print(miCoche.estado())

#Nuestra clase coche tiene 4 propiedades y 2 comportamientos 
