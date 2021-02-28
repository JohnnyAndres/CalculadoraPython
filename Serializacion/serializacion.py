#Serialización: Consiste en guardar en un fichero externo una colección, un diccionario o 
#un objeto, codificado en codigo binario, con el proposito por ejemplo de distribuirlo por internet,
#guardarlo en un dispositivo externo o en una base de datos. 

#Para la serialización hacemos uso de la libreria Pickle.

#Método dump(): Permite hacer un volcado de datos al fichero binario externo.
#Método load(): Permite cargar de los datos del fichero externo. 

#EJEMPLO

import pickle 

lista_nombres=["Johnny","Andres","Ana","Viviana","Ximena","Alvaro","Yolanda"]

fichero_binario=open("lista_nombres","wb") #Creamos un fichero externo, que tenga acceso de escritura binaria (wb: write binary)

pickle.dump(lista_nombres, fichero_binario) #Hacemos un volcado de la lista al fichero externo: pickle.dump(la_informacion_que_queremos_volcar, nombre_del_fichero_al_que_vamos_a_volcar)

#El fichero en este punto ya esta guardado con la informacion en el disco duro por lo tanto podemos cerrarlo y borrarlo

fichero_binario.close()
del (fichero_binario)

#Para leerlo hacemos

fichero_recuperado = open("lista_nombres","rb")

lista=pickle.load(fichero_recuperado)

print(lista)