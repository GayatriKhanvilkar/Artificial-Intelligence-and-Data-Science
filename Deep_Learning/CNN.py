# Convolutional neural networks
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Conv2D
from scipy import misc

img = misc.ascent()
print(img.shape)
img_tensor = img.reshape((1, 512, 512, 1))

from keras.models import Sequential
model = Sequential()
model.add(Conv2D(1, (3,3), strides=(2,1), input_shape=(512, 512, 1)))
model.compile('adam', 'mse')

img_pred_tensor = model.predict(img_tensor)

print(img_pred_tensor.shape)

img_pred = img_pred_tensor[0, :, :, 0]

plt.imshow(img_pred, cmap='gray')
plt.show()

weights = model.get_weights()

print(weights[0].shape)

plt.imshow(weights[0][:, :, 0, 0], cmap='gray')
plt.show()

weights[0] = np.ones(weights[0].shape)

model.set_weights(weights)

img_pred_tensor = model.predict(img_tensor)

plt.imshow(img_pred, cmap='gray')
plt.show()

model=Sequential()
model.add(Conv2D(1, (3, 3), input_shape=(512, 512, 1), padding='same'))
model.compile('adam', 'mse')

img_pred_tensor = model.predict(img_tensor)

print(img_pred_tensor.shape)
