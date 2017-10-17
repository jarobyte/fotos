from os import listdir
import argparse
import requests 

url="http://www.daic.infotec.com.mx:8080"
#carpeta = "imagenes"

parser = argparse.ArgumentParser()
parser.add_argument("carpeta")
args = parser.parse_args()
carpeta = args.carpeta

print "Monitoreando " + carpeta
print

contenidoActual = listdir(carpeta)
print "El contenido actual de la carpeta es:" + str(contenidoActual)

historial = open("historial", "r")
contenidoAnteriorCadena = historial.read()
historial.close()
contenidoAnterior = contenidoAnteriorCadena.splitlines()
contenidoAnterior = contenidoAnterior[1:]
print "El contenido anterior de la carpeta era:" + str(contenidoAnterior)

def difference(a, b):
    return list(set(a).difference(set(b)))

diff = difference(contenidoActual, contenidoAnterior)
print "Los siguientes archivos no estaban:" + str(diff)
print

def registrar(archivo):
    registro = open("registro", "a")
    registro.write(archivo + "\n")
    print "Registrado como enviado " + archivo
    registro.close()

def enviar(archivo):
    print
    print "Enviando " + archivo
    fin = open(carpeta + "/" + archivo, 'rb')
    data = {'file': fin}
    r = requests.post(url, files=data)
    r
    fin.close
    print "Enviado  " + archivo
    registrar(archivo)
    print

for i in diff:
    enviar(i)

nuevoHistorial = open("historial", "w")
nuevoHistorial.write(carpeta + "\n")
for i in contenidoActual:
    nuevoHistorial.write(str(i) + "\n")
nuevoHistorial.close()
