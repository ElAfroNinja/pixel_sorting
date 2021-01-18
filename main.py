import numpy
from skimage import data
import matplotlib.pyplot as plt

image = data.camera()  
type(image)
numpy.ndarray #Image is a NumPy array: 

plt.imshow(image, cmap='gray')
plt.show()