import face
import viewDicom
import pylab

hola2 = face.f
hola = hola2[:,:,1]
viewDicom.ds.Rows = 3168 
viewDicom.ds.Columns = 2376
viewDicom.ds.PixelData = hola.tostring()
pylab.imshow(viewDicom.ds.pixel_array, cmap = pylab.cm.bone)
pylab.show()
