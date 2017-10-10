from scipy import misc
import matplotlib.pyplot as plt

f = misc.face()
plt.imshow(f)
plt.show()

misc.imsave("hola.png", f)
adios = misc.imread("hola.png")
