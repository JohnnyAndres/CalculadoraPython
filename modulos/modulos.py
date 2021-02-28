#Archivos con extension py o pyc (python compilado) o escrito en c, que posee su propio espacio de nombres y
#que puede contener variables, funciones, clases e incluso otros módulos

#Sirven para organizar y reutilizar el código (modularización y reutilización)

'''import funcionesMatematicas  #Importamos el modulo

funcionesMatematicas.sumar(1,2)  #Hacemos llamdo de las funciones del modulo con nomenclatura del punto (POO)
funcionesMatematicas.restar(1,2)
funcionesMatematicas.multiplicar(1,2)
funcionesMatematicas.dividir(1,2)'''


#Podemos importar de la siguiente manera para optimizar

'''from funcionesMatematicas import sumar

sumar(1,2) ''' 


#Tambien podemos hacer de la siguiente manera para tener todo disponible

from funcionesMatematicas import * 

sumar(1,2)  
restar(1,2)
multiplicar(1,2)
dividir(1,2)
