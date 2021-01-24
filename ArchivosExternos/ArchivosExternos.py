
#Para trabajar con metodos externos utilizamos el modulo io

from io import open #Open para poder abrir un archivos externo

archivo_texto=open("archivos.txt", "w") #(w:write)  #como llamaremos al archivo = open( Nombre_del_Archivo_que_vamos_a_abrir, modo en que lo vamos a abrir (lectura, escritura. append))

#Si el archivo no existe open lo crea

frase = "Buen dia para todos \n adios"

archivo_texto.write(frase)  #Escribimos la frase en el archivo

#Luego de manipularlo debemos cerrar el archivo

archivo_texto.close() #Cerrar el archivo en memoria

archivo_texto=open("archivos.txt", "r") 

texto=archivo_texto.read() #Leemos lo que hay en el archivo

archivo_texto.close()

print(texto)

#readlines: Lee la informacion del archivo linea a linea y lo almacena en una lista

archivo_texto=open("archivos.txt", "r") 

lineas_text=archivo_texto.readlines()

archivo_texto.close()

print(lineas_text[1])

#Para agregar informacion usamos append como argumento de open

archivo_texto = open("archivos.txt","a")

archivo_texto.write("\n Hola de nuevo")

archivo_texto.close()

archivo_texto = open("archivos.txt","r")

lineas_txt=archivo_texto.readlines()

archivo_texto.close()

print(lineas_txt)

#Al leer un archivo el puntero se ubica al final por lo cual no podemos imprimir dos veces el mismo texto

#Modificar la ubicacion del puntero, usamos el metodo seek()

#seek(_posicion_del_parametro_donde_se_ubicara_el_cursor)

archivo_texto=open("archivos.txt","r")

print("1", archivo_texto.read(11)) #11 parameto para ver donde esta el puntero, solo llega hasta ahi

archivo_texto.seek(11)

print("2", archivo_texto.read())

#Tambien se puede usar read para cambiar el puntero, seek posiciona el puntero en donde le indiquemos  
#read realiza una lectura del archivo hasta donde le indiquemos

archivo_texto=open("archivos.txt","r")

archivo_texto.seek(len(archivo_texto.read())/2)

print("3", archivo_texto.read())

#Para que el archivo sea de lectura y escritura 

archivo_texto=open("archivos.txt", "r+") #lectura y escritura

#print(archivo_texto.readlines())

lista_texto=archivo_texto.readlines()

lista_texto[1] = "Esta linea cambio \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()

