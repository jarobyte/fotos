from os import listdir

carpeta = "imagenes"
print("Monitoreando /" + carpeta)
print()

contenidoActual = listdir(carpeta)
print("El contenido actual de la carpeta es:" + str(contenidoActual))

historial = open("historial", "r")
contenidoAnteriorCadena = historial.read()
historial.close()
contenidoAnterior = contenidoAnteriorCadena.splitlines()
print("El contenido anterior de la carpeta era:" + str(contenidoAnterior))

def difference(a, b):
    return list(set(a).difference(set(b)))

diff = difference(contenidoActual, contenidoAnterior)
print("Los siguientes archivos no estaban:" + str(diff))
print()

def registrar(archivo):
    registro = open("registro", "a")
    registro.write(archivo + "\n")
    print("Registrado como enviado " + archivo)
    registro.close()

def enviar(archivo):
    print()
    print("Enviando " + archivo)
    print("Enviado  " + archivo)
    registrar(archivo)
    print()

for i in diff:
    enviar(i)

nuevoHistorial = open("historial", "w")
for i in contenidoActual:
    nuevoHistorial.write(str(i) + "\n")
nuevoHistorial.close()
