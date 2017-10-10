import face
import viewDicom
import pylab

hola2 = face.adios
hola = hola2[:,:,1]
viewDicom.ds.Rows = 768
viewDicom.ds.Columns = 512
viewDicom.ds.PixelData = hola.tostring()
pylab.imshow(viewDicom.ds.pixel_array, cmap = pylab.cm.bone)
pylab.show()
