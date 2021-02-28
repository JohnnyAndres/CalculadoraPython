from tkinter import *

root = Tk()
root.geometry("1000x720") 
root.config(bg="blue") 
miFrame=Frame(root)
miFrame.pack()

miFrame.config(width="650", height="350")

miNombre=StringVar() #miNombre como cadena de caracteres

name=Entry(miFrame, textvariable=miNombre)
name.grid(row=0, column=1, padx=10, pady=10) 

lastName=Entry(miFrame)
lastName.grid(row=1, column=1, padx=10, pady=10) 

phone=Entry(miFrame)
phone.grid(row=2, column=1, padx=10, pady=10) 

password=Entry(miFrame)
password.grid(row=3, column=1, padx=10, pady=10) 
password.config(show="*") 

direccion=Entry(miFrame)
direccion.grid(row=4, column=1, padx=10, pady=10) 

comentarios=Text(miFrame, width="20", height="5") #Text: widget para cuadro de texto
comentarios.grid(row=5, column=1, padx=10, pady=10) 

#Construir scroll para el text
textScroll=Scrollbar(miFrame, command=comentarios.yview) #scrollbar(donde pertenece, posiciion, yview: en el eje y, vertical)
textScroll.grid(row=5, column=2, sticky="nsew") #Posicionamos el scroll, nsew permite que el scroll se adapta al tamaño del widget al que pertenece 
comentarios.config(yscrollcommand=textScroll.set) #Configuramos scroll para que se mueva en el posicionador
 
nameLabel=Label(miFrame, text="Nombre cliente:").grid(row=0,column=0, sticky="e", padx=10, pady=10) 
lastNameLabel=Label(miFrame, text="Apellido:").grid(row=1,column=0, sticky="e", padx=10, pady=10)
phoneLabel=Label(miFrame, text="Telefono:").grid(row=2,column=0, sticky="e", padx=10, pady=10)
password=Label(miFrame, text="Contraseña:").grid(row=3,column=0, sticky="e", padx=10, pady=10)
direccion=Label(miFrame, text="Direccion:").grid(row=4,column=0, sticky="e", padx=10, pady=10)
comentarios=Label(miFrame, text="Comentarios:").grid(row=5,column=0, sticky="e", padx=10, pady=10)

#Agregar Botones

def save():
    miNombre.set("Johnny")

def clean():
    miNombre.set("")
    
cleanButton=Button(miFrame, text="Guardar", command=save) #command: para decirle que ejecute una acción
cleanButton.grid(row=6, column=1, sticky="w")

cleanButton=Button(miFrame, text="Limpiar", command=clean)
cleanButton.grid(row=6, column=1, sticky="e")

saveButton=Button(root, text="Enviar")
saveButton.pack()


saveButton.pack()


root.mainloop()