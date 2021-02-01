from tkinter import *

root = Tk()
root.geometry("1000x720") 
root.config(bg="blue") 
miFrame=Frame(root)
miFrame.pack()

miFrame.config(width="650", height="350")


#Para ubicar label e inputs u otros widgets es conveniente usar grid()

name=Entry(miFrame)
name.grid(row=0, column=1, padx=10, pady=10) #grid(row, column)
name.config(fg="red", justify="center") 

lastName=Entry(miFrame)
lastName.grid(row=1, column=1, padx=10, pady=10) 

phone=Entry(miFrame)
phone.grid(row=2, column=1, padx=10, pady=10) 

password=Entry(miFrame)
password.grid(row=3, column=1, padx=10, pady=10) #grid(row, column)
password.config(show="*") #Show para ocultar el texto que se escribe

nameLabel=Label(miFrame, text="Nombre cliente:").grid(row=0,column=0, sticky="e", padx=10, pady=10) #sticky me permite alienear los elementos basandose en los puntos cardinales(n, s, e, w, ne, nw, se, sw)
#padx y pady para hacer padding a la izquierda, derecha y arriba, abajo.

lastNameLabel=Label(miFrame, text="Apellido:").grid(row=1,column=0, sticky="e", padx=10, pady=10)
phoneLabel=Label(miFrame, text="Telefono:").grid(row=2,column=0, sticky="e", padx=10, pady=10)

password=Label(miFrame, text="Contraseña:").grid(row=3,column=0, sticky="e", padx=10, pady=10)


root.mainloop()