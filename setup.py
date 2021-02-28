#Setup: poner la descripcion del paquete que se va a distribuir
from setuptools import setup

setup(
    name="paqueteCalculos",
    version="1.0",
    description="Paquete de operaciones matematicas basicas",
    author="Johnny",
    author_email="johnnyjojoa7@gmail.com",
    url="www.johnny.com",
    packages=["paquetes","paquetes.paqueteDistribuible"]
)


#Correr python3 setup.py sdist  en la consola para crear una carpeta dist donde esta el paquete que se podra distribuir
#Para instalar vamos a la carpeta dist y damos pip3 install nombre_del_paquete (completo, con extensiones)

#Para desinstalar el paquete pip3 uninstall nombre_del_paquete Ej: pip3 uninstall paqueteCalculos

