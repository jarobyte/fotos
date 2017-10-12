import requests
url="http://www.daic.infotec.com.mx:8080"

archivo = "imagenes/pruebaJuan1.dcm"
print()
print("Enviando " + archivo)
fin = open(archivo, 'rb')
data = {'file': fin}
r = requests.post(url, files=data)
r
fin.close
print("Enviado  " + archivo)
