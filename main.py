import numpy
from skimage import data
from skimage import io
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt


ref_image = io.imread("D:\Dev\Pixel_Sorting\Resources\hokusai_tsunami.jpg", as_gray=True)

threshold = threshold_otsu(ref_image)
bin_image = ref_image > threshold

fig, axes = plt.subplots(ncols=2, figsize=(8, 2.5))
ax = axes.ravel()

ax[0] = plt.subplot(1, 3, 1)
ax[1] = plt.subplot(1, 3, 2)

ax[0].imshow(ref_image, cmap='gray')
ax[1].imshow(bin_image, cmap='gray')

plt.show()