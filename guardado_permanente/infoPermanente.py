import pickle

class persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una nueva persona con el nombre:", self.nombre)

    def __str__(self): #Metodo especial __srt__ que convierte en cadena de texto la info de un texto
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class listaPersonas:
    personas=[]

    def __init__(self):
        listaDePersonas=open("ficheroExternoPersonas","ab+") #ab+ = agregar información binaria
        listaDePersonas.seek(0)
        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo:".format(len(self.personas)))
        except:
            print("No existen personas")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)    

    def agregarPersonas(self, personaNueva):
        self.personas.append(personaNueva)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for persona in self.personas:
            print(persona)  

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open("ficheroExternoPersonas","wb")
        pickle.dump(self.personas, listaDePersonas)         
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFicheroExterno(self): 
        print("La información del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)

miLista = listaPersonas()
personaNueva = persona("Johnny","M","30")
miLista.agregarPersonas(personaNueva)
miLista.mostrarInfoFicheroExterno()