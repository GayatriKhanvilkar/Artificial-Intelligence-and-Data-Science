# Image filters with convolutions

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
from scipy import misc

img = misc.ascent() # Load misc image
print(img.shape)

plt.imshow(img, cmap='gray') # Convert image to gray scale image
plt.show()

h_kernel = np.array([[1, 2, 1], # Pattern matching filter
                     [0, 0, 0],
                     [-1, -2, -1]])
plt.imshow(h_kernel)
plt.show()

res=convolve2d(img, h_kernel) # 2D convolution

plt.imshow(res, cmap='gray') # Image after convolution
plt.show()
