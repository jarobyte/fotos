from os import listdir

contenidoActual = listdir("imagenes")
print("El contenido actual de la carpeta es:" + str(contenidoActual))

registro = open("registro", "r")
contenidoAnteriorCadena = registro.read()
contenidoAnterior = contenidoAnteriorCadena.splitlines()
print("El contenido anterior de la carpeta es:" + str(contenidoAnterior))

def difference(a, b):
    return list(set(a).difference(set(b)))

diff = difference(contenidoActual, contenidoAnterior)
print("Los siguientes archivos no estaban:" + str(diff))
