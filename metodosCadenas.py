#python considera a las cadenas (string) como objetos, por lo cual tienen sus métodos y propiedades.

#upper() convierte a mayusculas todas las letras
#lower() convierte un string a minusculas
#capitalize() pone en mayuscula la primera letra
#count() cuantas veces aparece una letra o una cadena dentro de un texto
#find() representar la posicion
#iddigit() dice si es un digito o no: true o false
#isalnum() comprobar si son alfanumericos
#isalpha() comprobar si son solo letras, no cuentan los espacios
#split()separa por álabras usando espacios
#strip()borrar espacios sobrantes al principio y al final
#replace() cambia una palabra o letra por otra
#rfind() representa el indice contanto desde atras

'''nombreUsuario=input("Instroduce un nombre: ")
print("el nombre es: ", nombreUsuario.upper())
print("el nombre es: ", nombreUsuario.lower())
print("el nombre es: ", nombreUsuario.capitalize())'''

'''edad=input("Instroduce tu edad: ")
print(edad.isdigit())

while(edad.isdigit()==False):
    print("Introduce un numero valido")
    edad=input("Instroduce tu edad: ")

if (int(edad)<18):
    print("No puede pasar")
else:
    print("puede pasar")'''


email=input("Ingrese su email: ")    

def saveEmail():
    print("Guardando Email...")      


while (email.count('@') != 1 or email.find('@') == 0 or email.rfind('@') == len(email)-1):
    print("Ingrese un email valido")           
    email=input("Ingrese su email: ")       
else:
    saveEmail()
