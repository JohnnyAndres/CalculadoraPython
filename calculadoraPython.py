from tkinter import *

root=Tk()
root.title("Calculadora")

#root.iconbitmap('calc.xbm')

miFrame=Frame(root)
miFrame.pack()
 
userInput = ""
#**************PANTALLA*****************
screen=Entry(miFrame, textvariable=userInput)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
screen.config(background="black", fg="red", justify="right")
#***************************************

class button():
    def __init__(self, key, row, column):
        self.key=key
        self.row=row
        self.column=column

    def showInput(self):
        userInput = userInput + self.key

    def createButton(self):
        button=Button(miFrame, text=self.key, width=3, command=self.showInput)
        button.grid(row=self.row, column=self.column)


class operButton(button):
    def __init__(self, key, row, column):
        super().__init__(key, row, column)

#*******FILA 1*******
button7=button("7",2,1)
button7.createButton()
button8=button("8",2,2)
button8.createButton()
button9=button("9",2,3)
button9.createButton()
divButton=button('/',2,4)
divButton.createButton()

#*******FILA 2*******
button4=button("4",3,1)
button4.createButton()
button5=button("5",3,2)
button5.createButton()
button6=button("6",3,3)
button6.createButton()
mulButton=button('x',3,4)
mulButton.createButton()

#*******FILA 3*******
button1=button("1",4,1)
button1.createButton()
button2=button("2",4,2)
button2.createButton()
button3=button("3",4,3)
button3.createButton()
minusButton=button('-',4,4)
minusButton.createButton()

#*******FILA 4*******
button0=button("0",5,1)
button0.createButton()
pointButton=button('.',5,2)
pointButton.createButton()
equalButton=button('=',5,3)
equalButton.createButton()
sumButton=button('+',5,4)
sumButton.createButton()


root.mainloop()