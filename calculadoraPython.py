from tkinter import *

root=Tk()
root.title("Calculadora")

#root.iconbitmap('calc.xbm')

miFrame=Frame(root)
miFrame.pack()
 
userInput = StringVar()
selectedOperation = ""
result = 0

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

    def showNumberInput(self):
        global selectedOperation

        if (selectedOperation != ""):
            userInput.set(self.key)
            selectedOperation = ""
        else:
            userInput.set(userInput.get() + self.key)

    def createNumberButton(self):
        button=Button(miFrame, text=self.key, width=3, command=self.showNumberInput)
        button.grid(row=self.row, column=self.column)


class operButton(button):
    def __init__(self, key, row, column):
        super().__init__(key, row, column )

    def makeOperation(self, num):
        global selectedOperation
        global result 
        if (self.key == "/"):
            selectedOperation = "/" 
             
        elif (self.key == "x"):
            selectedOperation = "x" 

        if (self.key == "-"):
            selectedOperation = "-" 

        if (self.key == "+"):
            selectedOperation = "+"  
            result += int(num)
            userInput.set(result)

        if (self.key == "="):
            userInput.set(result+int(num))
            result = 0

    def createOperButton(self):
        button=Button(miFrame, text=self.key, width=3, command=lambda:self.makeOperation(userInput.get()))
        button.grid(row=self.row, column=self.column)    





#*******FILA 1*******
button7=button("7",2,1)
button7.createNumberButton()
button8=button("8",2,2)
button8.createNumberButton()
button9=button("9",2,3)
button9.createNumberButton()
divButton=operButton('/',2,4)
divButton.createOperButton()

#*******FILA 2*******
button4=button("4",3,1)
button4.createNumberButton()
button5=button("5",3,2)
button5.createNumberButton()
button6=button("6",3,3)
button6.createNumberButton()
mulButton=operButton('x',3,4)
mulButton.createOperButton()

#*******FILA 3*******
button1=button("1",4,1)
button1.createNumberButton()
button2=button("2",4,2)
button2.createNumberButton()
button3=button("3",4,3)
button3.createNumberButton()
minusButton=operButton('-',4,4)
minusButton.createOperButton()

#*******FILA 4*******
button0=button("0",5,1)
button0.createNumberButton()
pointButton=button('.',5,2)
pointButton.createNumberButton()
equalButton=operButton('=',5,3)
equalButton.createOperButton()
sumButton=operButton('+',5,4)
sumButton.createOperButton()


root.mainloop()