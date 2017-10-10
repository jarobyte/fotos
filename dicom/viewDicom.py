import dicom
import pylab
ds = dicom.read_file("image.dcm")
pylab.imshow(ds.pixel_array, cmap = pylab.cm.bone)
pylab.show()
