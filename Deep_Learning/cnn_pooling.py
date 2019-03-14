# Pooling Layers

import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import MaxPool2D, AvgPool2D
from scipy import misc

img = misc.ascent()
print(img.shape)

img_tensor = img.reshape((1, 512, 512, 1))
print(img_tensor.shape)

model = Sequential()
model.add(MaxPool2D((5,5), input_shape=(512, 512, 1))) #max pooling method
model.compile('adam', 'mse')

img_pred = model.predict(img_tensor)[0, :, :, 0]
print(img_pred.shape)

plt.imshow(img_pred, cmap='gray')
plt.show()

model = Sequential()
model.add(AvgPool2D((5,5), input_shape=(512, 512, 1))) #Avg pooling method
model.compile('adam', 'mse')

img_pred = model.predict(img_tensor)[0, :, :, 0]
plt.imshow(img_pred, cmap='gray')
plt.show()