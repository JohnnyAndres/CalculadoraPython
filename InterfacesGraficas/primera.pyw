#Se utiliza para la creación de GUIs (Grafic User Interface) la libreria de python Tkinter
#Instalacion en Linux sudo apt-get install python3-tk

#Raiz - Ventana

from tkinter import *
raiz=Tk() #Creamos la ventana llamando a la clase Tk

raiz.title("Mi primera ventana en Python")
#raiz.iconbitmap("icon.ico")
raiz.resizable(1,1) #rezizable recibe valores booleanos (ancho y alto) false, false: No permite redireccionar el tamaño de la ventana
raiz.geometry("1200x720") #Tamaño de la ventana
raiz.config(bg="blue")  #Config: configuracion de la ventana


miFrame=Frame() #Crear un frame - contenedor que ira dentro de la raiz
miFrame.pack() #Se empaqueta el frame dentro de la raiz, side=right lo ancla a la derecha
'''miFrame.pack(fill="x")''' #fill: rellenar y se expande horizontalmente
'''miFrame.pack(fill="y", expand="True")'''  #Para que se rellene  expanda verticalmente usamos expand
#Para expandir en ambas direccioanes usamos el valor both -> fill = "both"
'''miFrame.pack(fill="both", expand="True")'''

miFrame.config(bg="red")
miFrame.config(width="650", height="350") #Se da tamaño al frame y no a la raiz, la raiz se adapta al tamaño del frame
#El frame tiene un tamaño fijo
miFrame.config(bd="35") #Ancho Borde 
miFrame.config(relief="groove") #Tipo de borde
miFrame.config(cursor="hand2")

raiz.mainloop()  #Se llama al metodo mainloop es necesario para que la ventana este activa, funciona como un bucle infinito. 
 #El metodo mainloop debe estar siempre al final
#Se coloca al archivo extension pyw para que no se abra el ejecutable con la consola de comandos por detras

#Todo lo que se aplica al frame se puede aplicar tambien a la raiz

